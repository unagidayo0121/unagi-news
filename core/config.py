# Configuration for Antigravity News

RSS_FEEDS = {
    "Yahoo News (Top)": "https://news.yahoo.co.jp/rss/topics/top-picks.xml",
    "Hikkei (Top)": "https://assets.wor.jp/rss/nikkei/news.xml", # Alternative feed or official if available
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "WSJ": "https://feeds.a.dj.com/rss/RSSWorldNews.xml", # Example, might need adjustment
}

CATEGORIES = [
    "総合",
    "マーケティング",
    "政治",
    "経済",
    "スタートアップ",
    "IT/テクノロジー"
]

KEYWORDS = {
    "Startups": ["startup", "funding", "vc", "ipo", "unicorn", "saas"],
    "Marketing": ["marketing", "ad", "campaign", "brand", "seo"],
    "Politics": ["politics", "government", "election", "policy"],
    "Economy": ["economy", "market", "stock", "trade", "finance"],
    "IT/Tech": ["tech", "ai", "software", "hardware", "apple", "google", "microsoft"]
}

THEME_COLORS = {
    "primary": "#00FFFF", # Cyan/Neon Blue
    "background": "#0E1117", # Streamlit Dark
    "text": "#FAFAFA"
}
