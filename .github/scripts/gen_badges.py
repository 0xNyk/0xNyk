#!/usr/bin/env python3
"""Render star-count badges referenced in README.md as local SVGs.

Scans README.md for assets/badges/<owner>--<repo>[--gray].svg references,
fetches live star counts from the GitHub API, and writes flat-square badges:
label "stars" in white on #0A0A0A, count in near-black on mint (#6EF2A8)
or gray (#888888) for the --gray variant. Adding a badge reference to the
README is enough for the next run to start generating it.
"""

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "badges"

LABEL_BG = "#0A0A0A"
LABEL_FG = "#FFFFFF"
VALUE_FG = "#0A0A0A"
VARIANTS = {"": "#6EF2A8", "--gray": "#888888"}

# Approximate Verdana 11px advance widths for the characters badges use.
CHAR_W = {
    "0": 7.0, "1": 7.0, "2": 7.0, "3": 7.0, "4": 7.0,
    "5": 7.0, "6": 7.0, "7": 7.0, "8": 7.0, "9": 7.0,
    ".": 4.0, "K": 7.4, "?": 6.0, " ": 3.9,
    "s": 5.8, "t": 4.3, "a": 6.1, "r": 4.6,
    "O": 8.6, "S": 7.4,
}

TOTAL_MARKER = re.compile(r"<!-- oss-total -->.*?<!-- /oss-total -->", re.DOTALL)


def text_width(s: str) -> float:
    return sum(CHAR_W.get(c, 6.5) for c in s)


def fmt_count(n: int) -> str:
    if n < 1000:
        return str(n)
    k = f"{n / 1000:.1f}"
    if k.endswith(".0"):
        k = k[:-2]
    return k + "K"


def fetch_stars(owner: str, repo: str) -> int | None:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={"User-Agent": "badge-refresh"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)["stargazers_count"]
    except Exception as e:  # keep the old badge rather than fail the run
        print(f"warn: {owner}/{repo}: {e}", file=sys.stderr)
        return None


def render(value: str, value_bg: str, label: str = "stars") -> str:
    pad = 5
    lw = round(text_width(label)) + 2 * pad
    vw = round(text_width(value)) + 2 * pad
    total = lw + vw
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="20" role="img" aria-label="{label}: {value}">
<title>{label}: {value}</title>
<g shape-rendering="crispEdges">
<rect width="{lw}" height="20" fill="{LABEL_BG}"/>
<rect x="{lw}" width="{vw}" height="20" fill="{value_bg}"/>
</g>
<g text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
<text x="{lw * 5}" y="140" transform="scale(.1)" fill="{LABEL_FG}" textLength="{round(text_width(label) * 10)}">{label}</text>
<text x="{(lw + vw / 2) * 10:.0f}" y="140" transform="scale(.1)" fill="{VALUE_FG}" textLength="{round(text_width(value) * 10)}">{value}</text>
</g>
</svg>
"""


def main() -> None:
    readme = (ROOT / "README.md").read_text()
    refs = set(
        re.findall(
            r"assets/badges/([A-Za-z0-9_.-]+?)--([A-Za-z0-9_.-]+?)(--gray)?\.svg",
            readme,
        )
    )
    if not refs:
        print("no badge references found in README.md", file=sys.stderr)
        sys.exit(1)

    OUT.mkdir(parents=True, exist_ok=True)
    stars: dict[tuple[str, str], int | None] = {}
    for owner, repo, variant in sorted(refs):
        key = (owner, repo)
        if key not in stars:
            stars[key] = fetch_stars(owner, repo)
        count = stars[key]
        if count is None:
            continue
        path = OUT / f"{owner}--{repo}{variant}.svg"
        path.write_text(render(fmt_count(count), VARIANTS[variant]))
        print(f"{path.relative_to(ROOT)}: {count}")

    # Live OSS total: sum of unique repos referenced on this page. Only
    # updated when every fetch succeeded, so a flaky API call can't
    # publish an undercount.
    counts = [v for v in stars.values() if v is not None]
    if len(counts) == len(stars):
        total = sum(counts)
        (OUT / "total.svg").write_text(
            render(fmt_count(total), VARIANTS[""], label="OSS stars")
        )
        live = (
            f"<!-- oss-total -->**{fmt_count(total)}+ OSS stars** "
            f"({total:,} live across the open-source repos on this page)"
            f"<!-- /oss-total -->"
        )
        updated = TOTAL_MARKER.sub(live, readme)
        if updated != readme:
            (ROOT / "README.md").write_text(updated)
            print("README.md: oss-total updated")
        print(f"assets/badges/total.svg: {total}")
    else:
        print("warn: fetch failures — total left unchanged", file=sys.stderr)


if __name__ == "__main__":
    main()
