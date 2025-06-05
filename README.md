# IndiaMART Industrial Machinery Scraper & EDA

## Project Overview
This project scrapes product data from IndiaMART’s **Industrial Machinery** category, collects structured product information, and performs exploratory data analysis (EDA) to gain insights on the marketplace.

---

## Features
- Scrapes product details like name, price, company, location, and image URL.
- Supports multi-page scraping with polite rate limiting.
- Saves data as JSON for easy reuse.
- Jupyter Notebook for EDA with charts and summary statistics.
- Modular, easy-to-understand Python code.

---


nstall required packages:

bash
Copy code
pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:

bash
Copy code
pip install requests beautifulsoup4 pandas seaborn matplotlib jupyter
Usage
Run Scraper
bash
Copy code
python scraper/scraper.py
This will scrape product data and save it in data/indiamart_industrial_machinery.json.

Run EDA Notebook
Launch Jupyter Notebook:

bash
Copy code
jupyter notebook
Open eda/analysis.ipynb.

Run cells sequentially to perform data analysis and view visualizations.

