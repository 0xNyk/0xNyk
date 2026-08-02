#!/usr/bin/env python3
"""Build-surface graphic for the profile README.

Replaces a hand-edited SVG that still carried the retired palette (#C5F23F,
#6EF2A8, #0a0a0a) and, more importantly, spent prime README space on three
category labels. A reader who scrolls this far already knows the categories —
what they do not know is what actually exists, so each lane now names the
shipped artifacts and the layer it operates at.

Achroma (v5): the accent is maximum value, not a hue. Written as SVG so it stays
crisp at any width and one palette edit moves it; a PNG twin is rendered for
contexts that will not inline SVG.

Usage: python3 .github/scripts/gen_stack.py [out.svg]
"""
from __future__ import annotations

import sys
from pathlib import Path

W, H = 1200, 460

INK = "#0D0D0C"
CARD = "#141413"
RULE = "#2F2F2C"
STAR = "#F2F1EE"
DIM = "#9C9C96"
MUTED = "#6F6F69"
ACCENT = "#FFFFFF"

LANES = [
    {
        "title": "Solana infra",
        "layer": "execution path",
        "line": "RPC · gRPC · shreds · tx sender",
        "detail": "latency-sensitive execution, co-located with the cluster",
        "ships": ["rpc edge", "solbench", "solana-infra-mcp"],
    },
    {
        "title": "Agent operating systems",
        "layer": "the harness",
        "line": "skills · memory · jobs · verification",
        "detail": "the layer agents actually fail on, not the model",
        "ships": ["mission-control", "lacp", "council"],
    },
    {
        "title": "Dev tools",
        "layer": "operator surface",
        "line": "CLI · MCP · profiles · anti-slop",
        "detail": "small sharp tools people run every day",
        "ships": ["xint", "silo", "unmachined"],
    },
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build() -> str:
    mono = "ui-monospace, SFMono-Regular, Menlo, monospace"
    sans = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif"
    pad, gap = 48, 24
    cw = (W - pad * 2 - gap * 2) // 3
    top, ch = 118, 268

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" aria-label="Build surface: Solana '
        f'infrastructure, agent operating systems, developer tools">',
        f'<rect width="{W}" height="{H}" fill="{INK}"/>',
        # Header: the claim, then the aggregate that backs it.
        f'<text x="{pad}" y="56" fill="{DIM}" font-family="{mono}" font-size="13" '
        f'letter-spacing="3.4">BUILD SURFACE</text>',
        f'<text x="{pad}" y="90" fill="{STAR}" font-family="{sans}" font-size="25" '
        f'font-weight="700" letter-spacing="-0.4">Three layers, one operator.</text>',
        f'<text x="{W - pad}" y="90" text-anchor="end" fill="{STAR}" '
        f'font-family="{mono}" font-size="25" font-weight="700">16K+</text>',
        f'<text x="{W - pad}" y="56" text-anchor="end" fill="{DIM}" '
        f'font-family="{mono}" font-size="13" letter-spacing="2.2">OSS STARS</text>',
    ]

    for i, lane in enumerate(LANES):
        x = pad + i * (cw + gap)
        out += [
            f'<rect x="{x}" y="{top}" width="{cw}" height="{ch}" rx="6" '
            f'fill="{CARD}" stroke="{RULE}" stroke-width="1"/>',
            # One accent rule per lane — value, not hue.
            f'<rect x="{x}" y="{top}" width="{cw}" height="3" fill="{ACCENT}" '
            f'opacity="{0.9 - i * 0.25:.2f}"/>',
            f'<text x="{x + 22}" y="{top + 46}" fill="{STAR}" font-family="{sans}" '
            f'font-size="19" font-weight="700">{esc(lane["title"])}</text>',
            f'<text x="{x + 22}" y="{top + 70}" fill="{MUTED}" font-family="{mono}" '
            f'font-size="12" letter-spacing="1.6">{esc(lane["layer"].upper())}</text>',
            f'<line x1="{x + 22}" y1="{top + 88}" x2="{x + cw - 22}" y2="{top + 88}" '
            f'stroke="{RULE}" stroke-width="1"/>',
            f'<text x="{x + 22}" y="{top + 116}" fill="{DIM}" font-family="{mono}" '
            f'font-size="13">{esc(lane["line"])}</text>',
        ]
        # Wrap the detail line at ~34 characters.
        words, line, ly = lane["detail"].split(), "", top + 146
        for word in words:
            if len(f"{line} {word}".strip()) > 34:
                out.append(f'<text x="{x + 22}" y="{ly}" fill="{MUTED}" '
                           f'font-family="{sans}" font-size="13">{esc(line)}</text>')
                line, ly = word, ly + 19
            else:
                line = f"{line} {word}".strip()
        if line:
            out.append(f'<text x="{x + 22}" y="{ly}" fill="{MUTED}" '
                       f'font-family="{sans}" font-size="13">{esc(line)}</text>')

        # Shipped artifacts: the part that is proof rather than positioning.
        for j, ship in enumerate(lane["ships"]):
            sy = top + ch - 74 + j * 21
            out += [
                f'<rect x="{x + 22}" y="{sy - 9}" width="5" height="5" fill="{ACCENT}" opacity="0.55"/>',
                f'<text x="{x + 36}" y="{sy}" fill="{DIM}" font-family="{mono}" '
                f'font-size="12.5">{esc(ship)}</text>',
            ]

    out += [
        f'<text x="{pad}" y="{H - 24}" fill="{MUTED}" font-family="{mono}" '
        f'font-size="12" letter-spacing="1.2">nyk.dev · github.com/0xNyk</text>',
        f'<text x="{W - pad}" y="{H - 24}" text-anchor="end" fill="{MUTED}" '
        f'font-family="{mono}" font-size="12">shipped in public</text>',
        "</svg>",
    ]
    return "\n".join(out)


if __name__ == "__main__":
    dest = Path(sys.argv[1] if len(sys.argv) > 1 else "assets/stack.svg")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(build(), encoding="utf-8")
    print("wrote", dest)
