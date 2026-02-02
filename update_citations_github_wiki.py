"""
collect citation counts from Github Wiki
"""

import requests
import re

URL = "https://raw.githubusercontent.com/wiki/toruseo/UXsim/Home.md"

r = requests.get(URL)
r.raise_for_status()
text = r.text

# Citations セクションを抽出
m = re.search(
    r'^##\s+Academic Publications\s*(.*?)(?:\n##\s+|\Z)',
    text,
    flags=re.DOTALL | re.MULTILINE
)

if not m:
    raise RuntimeError("Citations section not found")

section = m.group(1)

# 番号付きリストをカウント
pattern = re.compile(r'^\s*\d+\.\s+', re.MULTILINE)
count = len(pattern.findall(section))

print(count)

import json

out = {
    "total_citations": count
}

with open("citations.json", "w") as f:
    json.dump(out, f)