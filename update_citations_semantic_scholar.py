"""
collect citation counts of multiple papers from Semantic Scholar
"""

import requests
import json

dois = [
    "10.21105/joss.07617",
    "10.48550/arXiv.2309.17114"
]

total = 0
details = []

for doi in dois:
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
    params = {"fields": "title,citationCount"}
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()
    count = data.get("citationCount", 0)
    total += count
    details.append({
        "doi": doi,
        "title": data.get("title"),
        "citationCount": count
    })

out = {
    "total_citations": total,
    "papers": details
}

with open("citations.json", "w") as f:
    json.dump(out, f, indent=2)
