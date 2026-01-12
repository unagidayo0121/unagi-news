import feedparser
import pandas as pd
from core.config import RSS_FEEDS

def fetch_rss(url):
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries:
        published = entry.get("published", "")
        # Try to parse date struct if available
        published_parsed = entry.get("published_parsed")
        
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": published,
            "published_parsed": published_parsed, # Keep struct_time for sorting
            "summary": entry.get("summary", ""),
            "source": feed.feed.get("title", "Unknown")
        })
    return articles

def fetch_all():
    all_articles = []
    for source, url in RSS_FEEDS.items():
        try:
            articles = fetch_rss(url)
            all_articles.extend(articles)
        except Exception as e:
            print(f"Error fetching {source}: {e}")
    return all_articles
