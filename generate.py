import feedparser
from datetime import datetime
import pytz

RSS_URL = "https://www.dianrana.id/feeds/posts/default?alt=rss"
BLOG_NAME = "Dian Rana News"
BLOG_LANGUAGE = "id"
TIMEZONE = pytz.timezone('Asia/Makassar')

feed = feedparser.parse(RSS_URL)

with open("news-sitemap.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n')
    f.write('        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n')

    for entry in feed.entries[:10]:  # max 10 artikel terakhir (aturan Google News)
        try:
            published = datetime(*entry.published_parsed[:6])
            published = TIMEZONE.localize(published)
            f.write("  <url>\n")
            f.write(f"    <loc>{entry.link}</loc>\n")
            f.write("    <news:news>\n")
            f.write("      <news:publication>\n")
            f.write(f"        <news:name>{BLOG_NAME}</news:name>\n")
            f.write(f"        <news:language>{BLOG_LANGUAGE}</news:language>\n")
            f.write("      </news:publication>\n")
            f.write(f"      <news:publication_date>{published.isoformat()}</news:publication_date>\n")
            f.write(f"      <news:title>{entry.title}</news:title>\n")
            f.write("    </news:news>\n")
            f.write("  </url>\n")
        except Exception as e:
            print("Error parsing entry:", e)

    f.write('</urlset>\n')
