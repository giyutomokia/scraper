# run_scraper.py

from scraper.indiamart_scraper import BASE_URL, scrape_all_pages, save_to_json

if __name__ == "__main__":
    products = scrape_all_pages(BASE_URL, max_pages=3)
    print(f"✅ Scraped {len(products)} products")
    save_to_json(products)
