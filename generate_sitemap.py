import os
from datetime import datetime

base_url = "https://dianrana1.github.io"
root_dir = "."
valid_extensions = [".html", ".md"]
now = datetime.now().strftime("%Y-%m-%d")

urls = []

for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = os.path.splitext(file)[1]
        if ext in valid_extensions:
            if file == "sitemap.xml":
                continue
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, root_dir)
            url_path = relative_path.replace("\\", "/").replace("index.html", "").replace("index.md", "")
            if url_path.endswith(ext):
                url_path = url_path.replace(ext, ".html")
            url = f"{base_url}/{url_path}".rstrip("/")
            urls.append(url)

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for url in urls:
    sitemap_content += "  <url>\n"
    sitemap_content += f"    <loc>{url}</loc>\n"
    sitemap_content += f"    <lastmod>{now}</lastmod>\n"
    sitemap_content += "    <changefreq>monthly</changefreq>\n"
    sitemap_content += "    <priority>0.8</priority>\n"
    sitemap_content += "  </url>\n"

sitemap_content += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print("✅ sitemap.xml berhasil dibuat.")
