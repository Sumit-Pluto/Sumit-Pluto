#!/usr/bin/env python3
import os
import re
import requests

VISITOR_URL = "https://visitor-badge.laobi.icu/badge?page_id=Sumit-Pluto.Sumit-Pluto"
OUT_PATH = "assets/views-badge.svg"

try:
    resp = requests.get(VISITOR_URL, timeout=20)
    resp.raise_for_status()
    svg_text = resp.text
except Exception as e:
    print(f"Failed to fetch badge: {e}")
    svg_text = ""

count = "0"
if svg_text:
    match = re.search(r">([\d,]+)</text>", svg_text)
    if not match:
        match = re.search(r'message="([\d,]+)"', svg_text)
    if match:
        count = match.group(1)

label = "PROFILE VIEWS"
label_color = "#FFE500"
bg_color = "#1a1b27"
text_color = "#ffffff"

label_width = max(100, 10 * len(label))
value_width = max(60, 10 * len(count) + 20)
total_width = label_width + value_width

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="28" role="img" aria-label="{label}: {count}">
  <title>{label}: {count}</title>
  <rect width="{total_width}" height="28" rx="4" fill="{bg_color}"/>
  <rect width="{label_width}" height="28" rx="4" fill="{label_color}"/>
  <rect x="{label_width}" width="{value_width}" height="28" rx="4" fill="{bg_color}"/>
  <text x="{label_width / 2}" y="18" text-anchor="middle" font-family="Verdana,DejaVu Sans,sans-serif" font-size="11" font-weight="700" fill="#1a1b27">{label}</text>
  <text x="{label_width + value_width / 2}" y="18" text-anchor="middle" font-family="Verdana,DejaVu Sans,sans-serif" font-size="11" font-weight="700" fill="{text_color}">{count}</text>
</svg>
'''

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Updated {OUT_PATH} with count {count}")
