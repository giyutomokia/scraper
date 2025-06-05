# scraper/indiamart_scraper.py

import requests
from bs4 import BeautifulSoup
import json
import time
import os

BASE_URL = "https://dir.indiamart.com/impcat/industrial-machinery.html"

def parse_product(li):
    product = {}
    try:
        product['product_name'] = li.find('a', class_='ptitle').get_text(strip=True)
        product['product_url'] = li.find('a', class_='ptitle')['href']
        price_tag = li.find('p', class_='NP-3 price')
        product['price'] = price_tag.get_text(strip=True).replace('\n', ' ') if price_tag else None
        product['company_name'] = li.find('h2', class_='lcname').get_text(strip=True)
        location_tag = li.find('p', class_='sm clg')
        product['location'] = location_tag.get('data-rlocation') if location_tag else None
        product['city'] = li.get('data-city')
        product['state'] = li.get('data-state')
        img_tag = li.find('div', class_='prd-img').find('img')
        product['image_url'] = img_tag['src'] if img_tag else None
    except Exception as e:
        print(f"Error parsing product: {e}")
    return product

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    print(f"Scraping page: {url}")
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print(f"Failed to get page {url} with status {resp.status_code}")
        return []
    soup = BeautifulSoup(resp.text, 'html.parser')
    product_list = soup.find_all('li', class_='lst')
    return [parse_product(li) for li in product_list if li]

def scrape_all_pages(base_url, max_pages=3):
    all_products = []
    for page in range(1, max_pages + 1):
        url = base_url if page == 1 else f"{base_url}?page={page}"
        products = scrape_page(url)
        if not products:
            print("No products found on page, stopping.")
            break
        all_products.extend(products)
        time.sleep(2)
    return all_products

def save_to_json(data, filename="data/indiamart_industrial_machinery.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
