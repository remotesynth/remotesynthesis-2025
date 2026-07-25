#!/usr/bin/env python3
"""Merge audit results + known dates into publications.json."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PUBS = ROOT / "src/data/publications.json"
AUDIT = ROOT / "scripts/publications-audit.json"
KNOWN = ROOT / "scripts/known-publication-dates.json"


def slug(path: str) -> str:
    return path.rstrip("/").split("/")[-1].lower()


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def is_homepage(url: str) -> bool:
    path = (urlparse(url).path or "/").rstrip("/") or "/"
    return path in {"/", "/blog", "/blogs", "/blogs/digital-experience"}


def good_relocation(original: str, final: str) -> bool:
    if not final or final == original or is_homepage(final):
        return False
    o = slug(urlparse(original).path)
    f_path = urlparse(final).path
    if not o or len(o) < 6:
        return False
    return norm(o) in norm(f_path) or norm(slug(f_path)) in norm(o)


def https_archive(url: str) -> str:
    if url.startswith("http://web.archive.org"):
        return "https://" + url[len("http://") :]
    return url


def needs_archive(row: dict) -> bool:
    url = row.get("url") or ""
    final = row.get("finalUrl") or ""
    host = urlparse(url).netloc.lower().replace("www.", "")
    archive = row.get("archiveUrl")
    if not archive:
        return False

    # Sites whose content is gone even if HTTP 200 / redirects elsewhere
    force_hosts = {
        "stackbit.com",
        "modernweb.com",
        "flippinawesome.org",
        "stepzen.com",
        "angularattack.com",
        "fusionauthority.com",
        "flex-authority.com",
        "digitalthirst.com",
        "mobilebusinessinsights.com",
        "coldfusion.sys-con.com",
        "devarticles.com",
        "bsminfo.com",
        "onwardsearch.com",
        "kendoui.com",
    }
    if host in force_hosts or host.endswith(".sys-con.com"):
        return True

    if row.get("preferArchive"):
        return True

    if final and is_homepage(final):
        return True

    # Cross-host redirect that isn't clearly the same article
    if final and urlparse(final).netloc.lower().replace("www.", "") != host:
        if not good_relocation(url, final):
            return True

    return False


def date_for(row: dict | None, url: str | None, known: dict) -> str | None:
    if url and url in known:
        return known[url]
    if not row or not row.get("date"):
        return None
    # Skip unreliable Wayback capture dates for still-usable live links
    if row.get("dateSource") == "wayback" and not needs_archive(row):
        return None
    return row["date"]


def main() -> None:
    pubs = json.loads(PUBS.read_text())
    audit = { (r["gi"], r["pi"]): r for r in json.loads(AUDIT.read_text()) }
    known = json.loads(KNOWN.read_text())

    url_updates = archives = dates = 0

    for gi, group in enumerate(pubs):
        for pi, pub in enumerate(group["publications"]):
            row = audit.get((gi, pi))
            url = pub.get("url")

            date = date_for(row, url, known)
            if date:
                pub["date"] = date
                dates += 1

            if not row or not url:
                continue

            final = row.get("finalUrl") or ""

            if needs_archive(row):
                pub["archiveUrl"] = https_archive(row["archiveUrl"])
                archives += 1
            elif final and good_relocation(url, final) and final != url:
                pub["url"] = final
                url_updates += 1

    ordered = []
    for group in pubs:
        items = []
        for pub in group["publications"]:
            item = {"title": pub["title"]}
            for key in ("url", "archiveUrl", "date", "coauthors", "type", "note"):
                if key in pub:
                    item[key] = pub[key]
            items.append(item)
        ordered.append({"publisher": group["publisher"], "publications": items})

    PUBS.write_text(json.dumps(ordered, indent=2) + "\n")
    total = sum(len(g["publications"]) for g in ordered)
    dated = sum(1 for g in ordered for p in g["publications"] if p.get("date"))
    archived = sum(1 for g in ordered for p in g["publications"] if p.get("archiveUrl"))
    print(f"Updated {PUBS}")
    print(f"  wrote dates={dates} archiveUrls={archives} urlUpdates={url_updates}")
    print(f"  coverage: {dated}/{total} dated, {archived}/{total} use archive links")


if __name__ == "__main__":
    main()
