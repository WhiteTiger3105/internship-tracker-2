##!/usr/bin/env python3
"""
Scraper pentru anunturi de internship / stagiu de practica la firme de avocatura
din Bucuresti si Iasi. Best-effort: cauta cuvinte-cheie relevante in paginile
de cariere ale firmelor + cateva job boards generale.

Ruleaza zilnic via GitHub Actions (.github/workflows/daily-update.yml).
"""
import json
import time
import hashlib
from pathlib import Path
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; InternshipTrackerBot/1.0; "
                  "+https://github.com/) AppleWebKit/537.36"
}
TIMEOUT = 15

KEYWORDS_POSITIVE = [
    "stagiu", "stagiar", "internship", "practica", "junior", "trainee",
    "avocat colaborator", "scoala de avocatura", "barou", "student drept",
    "voluntariat juridic", "summer internship", "vacation scheme"
]
KEYWORDS_PRIORITY = [
    "m&a", "fuziuni si achizitii", "corporate", "drept civil",
    "imobiliare", "real estate", "due diligence", "drept societar",
    "contracte comerciale", "litigii civile"
]
QUALIFICATION_HINTS = [
    "engleza", "english", "germana", "german", "franceza", "french",
    "an iii", "an iv", "anul iii", "anul iv", "licenta",
    "permis", "excel", "word", "cunostinte", "experienta",
    "disponibil", "full time", "part time"
]


def fetch(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"  [WARN] Failed to fetch {url}: {e}")
        return None


def extract_snippets(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    text_blocks = soup.find_all(["p", "li", "a", "h1", "h2", "h3", "div"])
    snippets = []
    seen_hashes = set()

    for block in text_blocks:
        text = block.get_text(separator=" ", strip=True)
        if not text or len(text) < 15 or len(text) > 1200:
            continue
        lower = text.lower()
        if any(kw in lower for kw in KEYWORDS_POSITIVE):
            h = hashlib.md5(text.encode()).hexdigest()
            if h in seen_hashes:
                continue
            seen_hashes.add(h)

            link = base_url
            if block.name == "a" and block.get("href"):
                href = block["href"]
                link = href if href.startswith("http") else requests.compat.urljoin(base_url, href)
            else:
                parent_link = block.find("a")
                if parent_link and parent_link.get("href"):
                    href = parent_link["href"]
                    link = href if href.startswith("http") else requests.compat.urljoin(base_url, href)

            priority = any(kw in lower for kw in KEYWORDS_PRIORITY)
            quals = [hint for hint in QUALIFICATION_HINTS if hint in lower]

            snippets.append({
                "text": text[:600],
                "link": link,
                "priority": priority,
                "qualifications_detected": quals,
            })
    return snippets


def scrape_source(name, url, region):
    print(f"Scraping {name} ({url}) ...")
    html = fetch(url)
    if not html:
        return []
    snippets = extract_snippets(html, url)
    results = []
    for s in snippets:
        results.append({
            "firma": name,
            "regiune": region,
            "sursa_url": url,
            **s,
        })
    print(f"  -> {len(results)} potential matches")
    return results


def main():
    sources = json.loads((DATA_DIR / "sources.json").read_text(encoding="utf-8"))
    all_results = []

    for entry in sources.get("bucuresti", []):
        all_results.extend(scrape_source(entry["firma"], entry["url"], "Bucuresti"))
        time.sleep(1)

    for entry in sources.get("iasi", []):
        all_results.extend(scrape_source(entry["firma"], entry["url"], "Iasi"))
        time.sleep(1)

    for entry in sources.get("joburi_generale", []):
        all_results.extend(scrape_source(entry["sursa"], entry["url"], "General"))
        time.sleep(1)

    all_results.sort(key=lambda r: (not r["priority"], r["firma"]))

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_found": len(all_results),
        "results": all_results,
    }

    out_path = DATA_DIR / "results.json"
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nSalvat {len(all_results)} rezultate in {out_path}")


if __name__ == "__main__":
    main()
