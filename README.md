# TechCrunch Web Scraper with Python

## 📝 Description

This repository provides two Python-based scrapers to extract data from TechCrunch articles. It includes:

- A listing scraper for fetching articles from multiple pages.

- A detail scraper to extract full content from individual article URLs.

📖 Read the full tutorial: [How to Scrape TechCrunch with Python](https://crawlbase.com/blog/scrape-techcrunch-with-python/)

## 🔧 Tools Used

- `requests` – for HTTP requests
- `BeautifulSoup` – for HTML parsing
- `pandas` – for saving data to CSV

## 📦 Installation

Install required dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

## 🚀 Scraper 1: Article Listing Scraper (techcrunch_listing_scraper.py)

### ✅ What It Does

- Scrapes article listings from the TechCrunch homepage or paginated archive.

- Extracts:

- **Title**
- **Link**
- **Author**
- **Publication Date**
- **Summary**

### ⚙️ How to Run

Edit the number of pages to scrape (`num_pages_to_scrape`) and run:

```bash
python techcrunch_listing_scraper.py
```

### 📁 Output

Saves article listing data to `techcrunch_listing.csv`.

#### 🧪 Sample Output

```csv
Title,Link,Author,Publication Date,Summary
"AI startup gets acquired","https://techcrunch.com/2024/08/10/example-article/","Jane Doe","2024-08-10","This startup is changing the game..."
...
```

## 📄 Scraper 2: Article Content Scraper (`techcrunch_article_scraper.py`)

### ✅ What It Does

Scrapes individual article URLs and extracts:

- **Title**
- **Author**
- **Publication Date**
- **Full Article Content**

### ⚙️ How to Run

Update the `article_urls` list with your desired TechCrunch article links and run:

```bash
python techcrunch_article_scraper.py
```

### 📁 Output

Saves article content to `techcrunch_articles.csv`.

#### 🧪 Sample Output

```csv
Title,Author,Publication Date,Content
"AI startup gets acquired","Jane Doe","2024-08-10","TechCrunch reports the acquisition of..."
```

...

## 📌 To-Do

- Add CLI support for inputting URLs.

- Add option to save data in JSON.

- Retry logic for failed requests.

- Proxy support for stealth scraping.

## 💡 Why Scrape TechCrunch?

- Track breaking news in the tech world.

- Monitor coverage of startups or competitors.

- Build datasets for NLP and content analysis.
