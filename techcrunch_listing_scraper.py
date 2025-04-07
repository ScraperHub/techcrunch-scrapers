import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape TechCrunch article listings
def scrape_techcrunch_listings(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.select('div.wp-block-group > div.wp-block-tc23-post-picker-group > div.wp-block-tc23-post-picker')
        data = []

        for article in articles:
            title_element = article.select_one('h2.wp-block-post-title')
            title = title_element.text.strip() if title_element else ''
            link = title_element.find('a')['href'] if title_element else ''
            author = article.select_one('div.wp-block-tc23-author-card-name').text.strip() if article.select_one('div.wp-block-tc23-author-card-name') else ''
            publication_date = article.select_one('time')['datetime'] if article.select_one('time') else ''
            summary = article.select_one('p.wp-block-post-excerpt__excerpt').text.strip() if article.select_one('p.wp-block-post-excerpt__excerpt') else ''

            data.append({
                'Title': title,
                'Link': link,
                'Author': author,
                'Publication Date': publication_date,
                'Summary': summary
            })

        return data
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Function to handle pagination
def scrape_techcrunch_with_pagination(base_url, start_page=1, num_pages=1):
    all_data = []

    for page in range(start_page, start_page + num_pages):
        url = f"{base_url}/page/{page}/"
        print(f"Scraping page: {page}")

        page_data = scrape_techcrunch_listings(url)
        if page_data:
            all_data.extend(page_data)
        else:
            print(f"Failed to retrieve data from page: {page}")
            break

    return all_data

# Function to save data to CSV
def save_data_to_csv(data, filename='techcrunch_listing.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Data successfully saved to {filename}")

# Main function to run the scraper
def main():
    base_url = 'https://techcrunch.com'
    num_pages_to_scrape = 5  # Specify the number of pages you want to scrape

    all_article_data = scrape_techcrunch_with_pagination(base_url, num_pages=num_pages_to_scrape)

    if all_article_data:
        save_data_to_csv(all_article_data)
    else:
        print("No data collected.")

if __name__ == "__main__":
    main()