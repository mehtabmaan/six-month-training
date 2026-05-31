import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# ==========================================
# CONFIGURATION
# ==========================================
BASE_URL = "https://indianexpress.com/"
INTERN_NAME = "YOUR_NAME_HERE" # TODO: Replace with your actual name!
TARGET_ARTICLES = 25           # Adjust this to be between 20 and 30
CSV_FILENAME = "Indian_Express_Scraped_Data.csv"

def fetch_page(url):
    """
    Fetches a web page and returns the BeautifulSoup object.
    Includes error handling for network failures.
    """
    # Using a standard User-Agent header to prevent 403 Forbidden errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Check for HTTP/Network errors
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Network error fetching {url}: {e}")
        return None

def get_homepage_links(base_url, max_links):
    """
    Scrapes the homepage for article links.
    Filters out non-news links to ensure we only get actual articles.
    """
    print(f"Fetching homepage: {base_url}")
    soup = fetch_page(base_url)
    if not soup:
        return []

    links = set() # Using a set automatically handles duplicate links
    
    # Find all 'a' tags with an 'href' attribute
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        
        # Indian Express articles typically contain '/article/' in the URL
        if '/article/' in href and href.startswith("https://"):
            links.add(href)
            
        # Stop collecting once we have a safe buffer over our target
        if len(links) >= max_links + 5: 
            break
            
    return list(links)[:max_links]

def scrape_article(url):
    """
    Visits a specific article page and extracts the Title and Full Text.
    """
    soup = fetch_page(url)
    if not soup:
        return None, None

    # Extract Title: Most articles use <h1> for the main headline
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else "Title Not Found"

    # Extract Article Text: Find all paragraph <p> tags
    paragraphs = soup.find_all('p')
    
    # Filter out short boilerplate text (e.g., "Click here to read more", copyright notices)
    # We only keep paragraphs with more than 30 characters
    text_content = [p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 30]
    full_text = ' '.join(text_content)

    return title, full_text

def main():
    print(f"Starting scraper. Target: {TARGET_ARTICLES} articles...\n")
    
    # Step 1: Get article links from the homepage
    article_links = get_homepage_links(BASE_URL, max_links=TARGET_ARTICLES)
    
    if not article_links:
        print("Failed to retrieve links from the homepage. Exiting.")
        return

    scraped_data = []
    
    # Step 2: Loop through each link and scrape the content
    for i, link in enumerate(article_links, 1):
        print(f"[{i}/{len(article_links)}] Scraping: {link}")
        title, full_text = scrape_article(link)
        
        # Only add to our dataset if we successfully grabbed text
        if title and full_text and full_text != "":
            scraped_data.append({
                'NEWS_TITLE': title,
                'Interns Name': INTERN_NAME,
                'NEWS_LINK': link,
                'FULL_SCRAPED_TEXT': full_text
            })
        else:
            print("  -> Skipped: Could not extract valid text.")
        
        # Step 3: Polite Scraping Strategy
        # Sleep for a random interval between 1.5 and 3.5 seconds to avoid overwhelming the server
        time.sleep(random.uniform(1.5, 3.5))

    # Step 4: Convert to Pandas DataFrame and export to CSV
    if scraped_data:
        df = pd.DataFrame(scraped_data)
        
        # Ensure the column order perfectly matches the prompt's requirements
        df = df[['NEWS_TITLE', 'Interns Name', 'NEWS_LINK', 'FULL_SCRAPED_TEXT']]
        
        # Save to CSV without the index column
        df.to_csv(CSV_FILENAME, index=False, encoding='utf-8')
        print(f"\n✅ Scraping complete! Successfully scraped {len(scraped_data)} articles.")
        print(f"✅ Data saved locally to: {CSV_FILENAME}")
    else:
        print("\n❌ No data was scraped. Please check your network connection or update the HTML parsers.")

if __name__ == "__main__":
    main()