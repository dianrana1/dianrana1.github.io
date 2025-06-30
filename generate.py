import feedparser
from datetime import datetime, timedelta
import pytz

RSS_URL = 'https://www.dianrana.id/feeds/posts/default?alt=rss'
TIMEZONE = 'Asia/Makassar'
MAX_ARTICLES = 100

feed = feedparser.parse(RSS_URL)
tz = pytz.timezone(TIMEZONE)
now = datetime.now(tz)
yesterday = now - timedelta(days=2)

items = []

for entry in feed.entries[:MAX_ARTICLES]:
    if hasattr(entry, 'published_parsed'):
        published = datetime(*entry.published_parsed[:6], tzinfo=pytz.utc).astimezone(tz)
        if published >= yesterday:
            items.append(f"""
  <url>
    <loc>{entry.link}</loc>
    <news:news>
      <news:publication>
        <news:name>Dian Rana</news:name>
        <news:language>id</news:language>
      </news:publication>
      <news:publication_date>{published.isoformat()}</news:publication_date>
      <news:title>{entry.title}</news:title>
    </news:news>
  </url>""")

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset
  xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
{''.join(items)}
</urlset>"""

with open('news-sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap.strip())
