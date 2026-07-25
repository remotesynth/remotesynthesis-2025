#!/usr/bin/env python3
"""Audit publication URLs via curl: status, Wayback snapshot, best-effort date."""

from __future__ import annotations

import json
import re
import subprocess
import time
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBS = ROOT / "src/data/publications.json"
OUT = ROOT / "scripts/publications-audit.json"
PROGRESS = ROOT / "scripts/publications-audit.progress.json"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# Domains/path patterns known to be gone or heavily rewritten
LIKELY_DEAD_HOSTS = {
    "modernweb.com",
    "www.modernweb.com",
    "flippinawesome.org",
    "www.flippinawesome.org",
    "developer.telerik.com",
    "www.kinvey.com",
    "kinvey.com",
    "www.angularattack.com",
    "angularattack.com",
    "mobilebusinessinsights.com",
    "www.digitalthirst.com",
    "digitalthirst.com",
    "www.fusionauthority.com",
    "fusionauthority.com",
    "www.flex-authority.com",
    "flex-authority.com",
    "coldfusion.sys-con.com",
    "www.devarticles.com",
    "devarticles.com",
    "www.kendoui.com",
    "kendoui.com",
    "blog.onwardsearch.com",
    "www.bsminfo.com",
    "bsminfo.com",
    "stepzen.com",
    "www.stepzen.com",
}


def curl_head(url: str) -> tuple[int | None, str]:
    """Return (status_code, final_url) using curl -I -L."""
    try:
        proc = subprocess.run(
            [
                "curl",
                "-sI",
                "-L",
                "--max-time",
                "25",
                "--max-redirs",
                "8",
                "-A",
                UA,
                "-o",
                "/dev/null",
                "-w",
                "%{http_code}\t%{url_effective}",
                url,
            ],
            capture_output=True,
            text=True,
            timeout=40,
        )
        out = (proc.stdout or "").strip()
        if "\t" not in out:
            return None, url
        code_s, final = out.split("\t", 1)
        code = int(code_s) if code_s.isdigit() else None
        return code, final or url
    except Exception:
        return None, url


def curl_get(url: str, max_bytes: int = 60000) -> tuple[int | None, str, str]:
    try:
        proc = subprocess.run(
            [
                "curl",
                "-sL",
                "--max-time",
                "30",
                "--max-redirs",
                "8",
                "-A",
                UA,
                "-w",
                "\n__STATUS__%{http_code}\t%{url_effective}",
                url,
            ],
            capture_output=True,
            text=True,
            timeout=45,
        )
        raw = proc.stdout or ""
        if "__STATUS__" not in raw:
            return None, url, raw[:max_bytes]
        body, meta = raw.rsplit("__STATUS__", 1)
        code_s, final = meta.strip().split("\t", 1)
        code = int(code_s) if code_s.isdigit() else None
        return code, final or url, body[:max_bytes]
    except Exception as e:
        return None, url, str(e)


def date_from_url(url: str) -> str | None:
    path = urllib.parse.urlparse(url).path
    for pat, fmt in (
        (r"/(20\d{2})/(\d{2})/(\d{2})(?:/|$)", 3),
        (r"/(20\d{2})-(\d{2})-(\d{2})", 3),
        (r"/(20\d{2})/(\d{2})(?:/|$)", 2),
        (r"/(20\d{2})(?:/|$)", 1),
    ):
        m = re.search(pat, path)
        if m:
            if fmt == 3:
                return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
            if fmt == 2:
                return f"{m.group(1)}-{m.group(2)}"
            return m.group(1)
    # Adobe Edge newsletter paths: /edge/april2012/ or /edge/february2009/
    m = re.search(
        r"/edge/(january|february|march|april|may|june|july|august|september|october|november|december)(20\d{2})",
        path,
        re.I,
    )
    if m:
        months = {
            "january": "01",
            "february": "02",
            "march": "03",
            "april": "04",
            "may": "05",
            "june": "06",
            "july": "07",
            "august": "08",
            "september": "09",
            "october": "10",
            "november": "11",
            "december": "12",
        }
        return f"{m.group(2)}-{months[m.group(1).lower()]}"
    # inspire/2013/11/
    m = re.search(r"/inspire/(20\d{2})/(\d{2})/", path)
    if m:
        return f"{m.group(1)}-{m.group(2)}"
    return None


def date_from_html(html: str) -> str | None:
    patterns = [
        r'property=["\']article:published_time["\']\s+content=["\']([^"\']+)',
        r'content=["\']([^"\']+)["\']\s+property=["\']article:published_time["\']',
        r'property=["\']og:published_time["\']\s+content=["\']([^"\']+)',
        r'itemprop=["\']datePublished["\']\s+content=["\']([^"\']+)',
        r'<time[^>]+datetime=["\']([^"\']+)["\']',
        r'"datePublished"\s*:\s*"([^"]+)"',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.I)
        if m:
            raw = m.group(1).strip()
            dm = re.match(r"(\d{4}-\d{2}-\d{2})", raw)
            if dm:
                return dm.group(1)
            dm = re.match(r"(\d{4}-\d{2})", raw)
            if dm:
                return dm.group(1)
            dm = re.match(r"(\d{4})", raw)
            if dm:
                return dm.group(1)
    return None


def wayback_snapshot(url: str) -> dict | None:
    # Prefer CDX for a 200 snapshot closest to original
    cdx = (
        "https://web.archive.org/cdx/search/cdx?"
        + urllib.parse.urlencode(
            {
                "url": url,
                "output": "json",
                "filter": "statuscode:200",
                "limit": "1",
                "fl": "timestamp,original,statuscode",
            }
        )
    )
    status, _, body = curl_get(cdx, max_bytes=5000)
    if status == 200 and body.strip().startswith("["):
        try:
            rows = json.loads(body)
            if len(rows) >= 2:
                ts, original, _ = rows[1][:3]
                return {
                    "archiveUrl": f"https://web.archive.org/web/{ts}/{original}",
                    "timestamp": ts,
                }
        except json.JSONDecodeError:
            pass

    api = "https://archive.org/wayback/available?" + urllib.parse.urlencode(
        {"url": url}
    )
    status, _, body = curl_get(api, max_bytes=5000)
    if status != 200:
        return None
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return None
    snap = data.get("archived_snapshots", {}).get("closest")
    if not snap or not snap.get("available"):
        return None
    archive_url = snap["url"]
    if archive_url.startswith("http://"):
        archive_url = "https://" + archive_url[len("http://") :]
    return {
        "archiveUrl": archive_url,
        "timestamp": snap.get("timestamp"),
    }


def host(url: str) -> str:
    return urllib.parse.urlparse(url).netloc.lower()


def looks_dead(status: int | None, final_url: str, original: str) -> bool:
    if status is None or status >= 400:
        return True
    h = host(original)
    if h in LIKELY_DEAD_HOSTS or h.replace("www.", "") in {
        x.replace("www.", "") for x in LIKELY_DEAD_HOSTS
    }:
        # still check if it redirected somewhere useful with 200
        fh = host(final_url)
        if fh == h or fh.replace("www.", "") == h.replace("www.", ""):
            return True
    # Adobe inspire/edge/devnet newsletter paths often 404 or soft-404
    if "adobe.com" in h and any(
        p in original for p in ("/inspire/", "/newsletters/edge/", "/devnet/")
    ):
        if status != 200:
            return True
    return False


def main() -> None:
    pubs = json.loads(PUBS.read_text())
    items = []
    for gi, group in enumerate(pubs):
        for pi, pub in enumerate(group["publications"]):
            items.append((gi, pi, group["publisher"], pub))

    done: dict[str, dict] = {}
    if PROGRESS.exists():
        for row in json.loads(PROGRESS.read_text()):
            done[f"{row['gi']}:{row['pi']}"] = row
        print(f"Resuming with {len(done)} cached results")

    results = []
    for gi, pi, publisher, pub in items:
        key = f"{gi}:{pi}"
        if key in done:
            results.append(done[key])
            continue

        url = pub.get("url")
        print(f"[{key}] {(url or pub['title'])[:100]}", flush=True)

        if not url:
            row = {
                "publisher": publisher,
                "title": pub["title"],
                "gi": gi,
                "pi": pi,
                "url": None,
                "live": False,
                "preferArchive": False,
                "date": pub.get("date"),
            }
            results.append(row)
            done[key] = row
            PROGRESS.write_text(json.dumps(list(done.values()), indent=2))
            continue

        status, final_url = curl_head(url)
        dead = looks_dead(status, final_url, url)

        date = pub.get("date") or date_from_url(url)
        date_source = "existing" if pub.get("date") else ("url" if date else None)

        body = ""
        if not dead and not date:
            status2, final_url, body = curl_get(url)
            status = status2 if status2 is not None else status
            dead = looks_dead(status, final_url, url)
            if not dead and body:
                html_date = date_from_html(body)
                if html_date:
                    date = html_date
                    date_source = "html"

        archive = None
        if dead or not date:
            time.sleep(0.2)
            archive = wayback_snapshot(url)
            if archive and archive.get("timestamp") and not date:
                ts = archive["timestamp"]
                if len(ts) >= 8:
                    date = f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]}"
                    date_source = "wayback"

        prefer_archive = bool(dead and archive and archive.get("archiveUrl"))

        row = {
            "publisher": publisher,
            "title": pub["title"],
            "gi": gi,
            "pi": pi,
            "url": url,
            "status": status,
            "finalUrl": final_url,
            "live": not dead,
            "preferArchive": prefer_archive,
            "archiveUrl": (archive or {}).get("archiveUrl"),
            "archiveTimestamp": (archive or {}).get("timestamp"),
            "date": date,
            "dateSource": date_source,
        }
        results.append(row)
        done[key] = row
        PROGRESS.write_text(json.dumps(list(done.values()), indent=2))
        time.sleep(0.15)

    # Keep stable order
    results.sort(key=lambda r: (r["gi"], r["pi"]))
    OUT.write_text(json.dumps(results, indent=2))
    live = sum(1 for r in results if r.get("live"))
    archived = sum(1 for r in results if r.get("preferArchive"))
    dated = sum(1 for r in results if r.get("date"))
    print(
        f"\nDone. {len(results)} items | live={live} preferArchive={archived} dated={dated}",
        flush=True,
    )
    print(f"Wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
