#!/usr/bin/env python3
"""Maintainer script: fill missing authors, venues and links in data/authors_cache.csv from Crossref and DataCite.

    python3 scripts/ingest_sources.py ...        # first pass, writes data/studies.csv
    python3 scripts/enrich_metadata.py           # looks up rows that lack authors, venue or link
    python3 scripts/ingest_sources.py ...        # second pass reads the cache

Only DOIs and Crossref title matches with similarity >= 0.92 are used; nothing is guessed.
"""
import csv, difflib, json, os, re, sys, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
UA = {"User-Agent": "awesome-flow-medical-imaging/1.0 (mailto:hc666@cam.ac.uk)"}


def get(url):
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
                return json.load(r)
        except Exception:
            time.sleep(1.5)
    return None


def norm(t):
    return re.sub(r"[^a-z0-9]+", "", (t or "").lower())


def crossref_item(m):
    au = ", ".join(" ".join(x for x in (a.get("given"), a.get("family")) if x) or a.get("name", "") for a in m.get("author", []))
    ven = (m.get("container-title") or [""])[0]
    return au, ven, m.get("DOI", "")


def lookup(row):
    doi = re.sub(r"^https://doi.org/", "", row["link"]) if row["link"].startswith("https://doi.org/") else ""
    arx = re.search(r"arxiv.org/abs/(.+)$", row["link"])
    if not doi and not arx:
        for l in row["alt_links"].split(" ; "):
            if l.startswith("https://doi.org/"):
                doi = l[16:]
                break
    out = {"id": row["id"], "authors": "", "venue": "", "link": ""}
    if doi and not doi.startswith("10.48550"):
        j = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
        if j and j.get("message"):
            out["authors"], out["venue"], _ = crossref_item(j["message"])
            if out["authors"] or out["venue"]:
                return out
    ax = arx.group(1) if arx else (doi[15:] if doi.startswith("10.48550/arxiv.") else "")
    if ax:
        j = get("https://api.datacite.org/dois/10.48550/arxiv." + re.sub(r"v\d+$", "", ax))
        if j and j.get("data"):
            at = j["data"]["attributes"]
            out["authors"] = ", ".join(c.get("name", "") if not c.get("givenName") else f"{c['givenName']} {c['familyName']}" for c in at.get("creators", []))
            out["venue"] = "arXiv"
            return out
    if not row["link"] or not row["authors"]:
        q = urllib.parse.quote(row["title"])
        j = get(f"https://api.crossref.org/works?query.bibliographic={q}&rows=3&select=DOI,title,author,container-title,issued")
        for m in (j or {}).get("message", {}).get("items", []):
            t = (m.get("title") or [""])[0]
            yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
            if difflib.SequenceMatcher(None, norm(t), norm(row["title"])).ratio() >= 0.92 and (not row["year"] or not yr or abs(int(row["year"]) - yr) <= 1):
                out["authors"], out["venue"], d = crossref_item(m)
                if not row["link"] and d:
                    out["link"] = "https://doi.org/" + d
                return out
    return out


def main():
    rows = list(csv.DictReader(open(f"{DATA}/studies.csv", encoding="utf-8")))
    cache_p = f"{DATA}/authors_cache.csv"
    cache = {r["id"]: r for r in csv.DictReader(open(cache_p, encoding="utf-8"))} if os.path.exists(cache_p) else {}
    todo = [r for r in rows if (not r["authors"] or not r["link"] or not r["venue"]) and r["id"] not in cache]
    print("lookups:", len(todo))
    with ThreadPoolExecutor(6) as ex:
        for res in ex.map(lookup, todo):
            cache[res["id"]] = res
    with open(cache_p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, ["id", "authors", "venue", "link"])
        w.writeheader()
        w.writerows(cache.values())
    print("cache rows:", len(cache), "with authors:", sum(bool(r["authors"]) for r in cache.values()))


if __name__ == "__main__":
    main()
