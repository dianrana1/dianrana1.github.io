import os
from datetime import datetime

# Ganti ini dengan domain GitHub Pages kamu
BASE_URL = "https://dianrana1.github.io/"

# Folder tempat file HTML berada
FOLDER = "."

# Ambil semua file .html di folder
files = [f for f in os.listdir(FOLDER) if f.endswith(".html")]

# Buat elemen <url> untuk setiap file
urls = []
for f in files:
    url = BASE_URL + f
    lastmod = datetime.today().strftime('%Y-%m-%d')
    urls.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod}</lastmod>
  </url>""")

# Gabungkan semua jadi satu file XML
sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>
"""

# Simpan ke file sitemap.xml
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print("✅ sitemap.xml berhasil dibuat.")
