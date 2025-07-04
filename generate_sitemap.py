import os
from datetime import datetime

# Ganti dengan URL GitHub Pages kamu:
base_url = "https://dianrana1.github.io/"

# Folder tempat file HTML disimpan ('.' = root folder)
html_folder = '.'

sitemap_entries = []

for filename in os.listdir(html_folder):
    if filename.endswith('.html'):
        full_url = base_url + filename
        lastmod = datetime.today().strftime('%Y-%m-%d')
        entry = f"""  <url>
    <loc>{full_url}</loc>
    <lastmod>{lastmod}</lastmod>
  </url>"""
        sitemap_entries.append(entry)

# Gabungkan semua entri ke dalam struktur XML
sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_entries)}
</urlset>
"""

# Simpan ke file sitemap.xml
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print("✅ sitemap.xml berhasil dibuat.")
