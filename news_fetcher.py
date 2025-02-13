# Fetching News from Arabic Websites

import requests
from bs4 import BeautifulSoup
import sqlite3

# News sources with URLs
NEWS_SOURCES = {
    "Al Jazeera": "https://www.aljazeera.net/news",
    "Al Arabiya": "https://www.alarabiya.net/lastpage",
    "Sky News Arabia": "https://www.skynewsarabia.com/latest-news",
    "BBC Arabic": "https://www.bbc.com/arabic",
    "RT Arabic": "https://arabic.rt.com/news/"
}

# Database connection
conn = sqlite3.connect("news_cache.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY, title TEXT UNIQUE, link TEXT)")
conn.commit()

def fetch_news():
    """Fetch news from Arabic news sources."""
    news_list = []
    
    for source, url in NEWS_SOURCES.items():
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(response.text, "html.parser")

            # Extracting news titles based on the website structure
            if "aljazeera" in url:
                articles = soup.find_all("h2")
            elif "alarabiya" in url:
                articles = soup.find_all("h3")
            elif "skynewsarabia" in url:
                articles = soup.find_all("h3", class_="news-title")
            elif "bbc" in url:
                articles = soup.find_all("h3", class_="gs-c-promo-heading__title")
            elif "rt.com" in url:
                articles = soup.find_all("div", class_="card__title")

            # Store the first 5 news items per source
            for article in articles[:5]:
                title = article.text.strip()
                link = article.find_parent("a")["href"] if article.find_parent("a") else url
                
                # Prevent duplicate news
                cursor.execute("SELECT * FROM news WHERE title=?", (title,))
                if not cursor.fetchone():
                    news_list.append({"source": source, "title": title, "link": link})
                    cursor.execute("INSERT INTO news (title, link) VALUES (?, ?)", (title, link))
                    conn.commit()
        
        except Exception as e:
            print(f"⚠️ Error fetching news from {source}: {e}")

    return news_list
