import urllib.request

with open("index.html", encoding="utf-8") as f:
    html = f.read()

libs = [
    ("https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js",
     '<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>'),
    ("https://unpkg.com/@zxing/library@0.19.1/umd/index.min.js",
     '<script src="https://unpkg.com/@zxing/library@0.19.1/umd/index.min.js"></script>'),
    ("https://unpkg.com/tesseract.js@5.0.4/dist/tesseract.min.js",
     '<script src="https://unpkg.com/tesseract.js@5.0.4/dist/tesseract.min.js"></script>'),
]

for url, tag in libs:
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            code = r.read().decode("utf-8", errors="replace")
        html = html.replace(tag, f"<script>{code}</script>")
        print(f"OK inlined {url}")
    except Exception as e:
        print(f"FAILED {url}: {e}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
