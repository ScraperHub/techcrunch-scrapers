import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape individual TechCrunch article pages
def scrape_techcrunch_article(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting the title
        title = soup.select_one('h1.wp-block-post-title').text.strip()

        # Extracting the author
        author = soup.select_one('div.wp-block-tc23-author-card-name > a').text.strip()

        # Extracting the publication date
        publication_date = soup.select_one('div.wp-block-post-date > time')['datetime']

        # Extracting the content
        content = soup.select_one('div.wp-block-post-content').text.strip()

        return {
            'Title': title,
            'Author': author,
            'Publication Date': publication_date,
            'Content': content
        }
    else:
        print(f"Failed to retrieve the article. Status code: {response.status_code}")
        return None

# Function to save article data to CSV
def save_article_data_to_csv(data, filename='techcrunch_articles.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Article data successfully saved to {filename}")

# Example usage
if __name__ == "__main__":
    # Replace with actual article URLs
    article_urls = [
        'https://techcrunch.com/2024/08/10/example-article/',
        'https://techcrunch.com/2024/08/11/another-article/'
    ]

    all_article_data = []
    for url in article_urls:
        article_data = scrape_techcrunch_article(url)
        if article_data:
            all_article_data.append(article_data)

    save_article_data_to_csv(all_article_data)