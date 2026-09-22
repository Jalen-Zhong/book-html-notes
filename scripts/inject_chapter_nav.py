#!/usr/bin/env python3
"""Inject consistent end-of-chapter navigation into bilingual book HTML pages.

Idempotent: safe to re-run. Source of truth for order: root index.html hrefs.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path("/workspace/book-html-notes")
INDEX = ROOT / "index.html"
HOME_HREF = "../../../index.html"

CHAPTER_NAV_CSS = """
    /* chapter end navigation */
    .chapter-nav {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
      margin: 22px 0 10px;
    }
    .chapter-nav .nav-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 10px 14px;
      border-radius: 10px;
      border: 1px solid var(--line, rgba(212, 175, 55, 0.28));
      background: rgba(212, 175, 55, 0.1);
      color: var(--gold-soft, #f0d78c);
      text-decoration: none;
      font-size: 14px;
      flex: 1 1 140px;
      max-width: 220px;
      text-align: center;
      min-height: 42px;
      box-sizing: border-box;
    }
    .chapter-nav .nav-btn:hover {
      background: rgba(212, 175, 55, 0.2);
      border-color: var(--gold, #d4af37);
    }
    .chapter-nav .nav-btn[aria-disabled="true"] {
      opacity: 0.38;
      pointer-events: none;
      cursor: not-allowed;
    }
""".rstrip() + "\n"

NAV_MARKER = 'class="chapter-nav"'


def rel_href(from_file: Path, to_file: Path) -> str:
    return Path(
        __import__("os").path.relpath(to_file, start=from_file.parent)
    ).as_posix()


def parse_orders(index_html: str) -> dict[str, dict[str, list[str]]]:
    """Return {book: {'zh': [relpath...], 'en': [...]}} in index document order."""
    hrefs = re.findall(r'href="(books/[^"]+\.html)"', index_html)
    orders: dict[str, dict[str, list[str]]] = defaultdict(lambda: {"zh": [], "en": []})
    for h in hrefs:
        book = h.split("/")[1]
        if h.endswith("-zh.html"):
            orders[book]["zh"].append(h)
        elif h.endswith("-en.html"):
            orders[book]["en"].append(h)
    return orders


def sibling_lang(path: str, lang: str) -> str:
    if lang == "zh":
        return re.sub(r"-zh\.html$", "-en.html", path)
    return re.sub(r"-en\.html$", "-zh.html", path)


def clean_attribution(inner: str) -> str:
    """Strip old nav-ish links; keep attribution + SOURCES.md."""
    # Drop existing chapter-nav entirely if re-running on partially processed content
    inner = re.sub(
        r'<nav\s+class="chapter-nav"[^>]*>.*?</nav>',
        "",
        inner,
        flags=re.DOTALL | re.IGNORECASE,
    )
    # Remove anchors that are home / language twin / prev-chapter style
    def drop_nav_a(m: re.Match) -> str:
        tag = m.group(0)
        href = m.group(1) or ""
        text = re.sub(r"<[^>]+>", "", m.group(0))
        text_l = text.lower()
        href_l = href.lower()
        keep = False
        if "sources.md" in href_l:
            keep = True
        # drop home, lang twins, chapter prev/next style
        drop_hints = [
            "index.html",
            "-zh.html",
            "-en.html",
            "返回首页",
            "back to home",
            "english edition",
            "中文版",
            "chinese edition",
            "上一章",
            "下一章",
            "previous",
            "next",
            "←",
            "→",
        ]
        if any(h in href_l or h in text_l for h in drop_hints) and "sources.md" not in href_l:
            return ""
        return tag if keep else tag

    inner = re.sub(
        r'<a\s[^>]*href="([^"]*)"[^>]*>.*?</a>',
        drop_nav_a,
        inner,
        flags=re.DOTALL | re.IGNORECASE,
    )
    # Clean leftover separators
    inner = re.sub(r"(?:\s*[·•|]\s*){2,}", " · ", inner)
    inner = re.sub(r"(?:<br\s*/?>\s*)+$", "", inner, flags=re.IGNORECASE)
    inner = re.sub(r"^[·•|\s]+|[·•|\s]+$", "", inner.strip())
    # Collapse whitespace around newlines but keep <br />
    inner = re.sub(r"[ \t]+\n", "\n", inner)
    inner = re.sub(r"\n{3,}", "\n\n", inner)
    # Trailing separator junk
    inner = re.sub(r"(?:<br\s*/?>|\s|[·•|])+$", "", inner.strip(), flags=re.IGNORECASE)
    return inner.strip()


def build_nav(
    lang: str,
    prev_rel: str | None,
    next_rel: str | None,
    lang_rel: str,
) -> str:
    if lang == "zh":
        labels = ("上一章", "下一章", "返回首页", "English edition")
    else:
        labels = ("Previous", "Next", "Back to home", "中文版")

    def btn(label: str, href: str | None) -> str:
        if href:
            return f'      <a class="nav-btn" href="{href}">{label}</a>'
        return (
            f'      <a class="nav-btn" href="#" aria-disabled="true" tabindex="-1">{label}</a>'
        )

    parts = [
        '    <nav class="chapter-nav" aria-label="Chapter navigation">',
        btn(labels[0], prev_rel),
        btn(labels[1], next_rel),
        btn(labels[2], HOME_HREF),
        btn(labels[3], lang_rel),
        "    </nav>",
    ]
    return "\n".join(parts)


def ensure_css_in_text(text: str) -> tuple[str, bool]:
    if ".chapter-nav" in text and ".nav-btn" in text:
        return text, False
    # Prefer inject before last </style>
    if "</style>" in text:
        # inject into the last style block
        idx = text.rfind("</style>")
        text = text[:idx] + CHAPTER_NAV_CSS + text[idx:]
        return text, True
    return text, False


def ensure_css_file(css_path: Path) -> bool:
    raw = css_path.read_text(encoding="utf-8")
    if ".chapter-nav" in raw and ".nav-btn" in raw:
        return False
    # append before trailing media query if present, else at end
    if "@media" in raw:
        # insert before last @media block
        idx = raw.rfind("@media")
        raw = raw[:idx] + CHAPTER_NAV_CSS + "\n" + raw[idx:]
    else:
        raw = raw.rstrip() + "\n" + CHAPTER_NAV_CSS
    css_path.write_text(raw, encoding="utf-8")
    return True


def transform_footer(html: str, nav_html: str) -> tuple[str, bool]:
    m = re.search(r"<footer\b[^>]*>(.*?)</footer>", html, flags=re.DOTALL | re.IGNORECASE)
    if not m:
        return html, False
    inner = m.group(1)
    attr = clean_attribution(inner)
    if attr:
        new_inner = "\n      " + attr + "\n" + nav_html + "\n    "
    else:
        new_inner = "\n" + nav_html + "\n    "
    new_footer = f"<footer>{new_inner}</footer>"
    # Only rewrite if different (normalize whitespace lightly)
    old = m.group(0)
    if old == new_footer:
        return html, False
    html = html[: m.start()] + new_footer + html[m.end() :]
    return html, True


def process_page(
    rel: str,
    lang: str,
    order: list[str],
    idx: int,
) -> bool:
    path = ROOT / rel
    if not path.exists():
        print(f"MISSING {rel}")
        return False
    html = path.read_text(encoding="utf-8")

    prev_rel = None
    next_rel = None
    if idx > 0:
        prev_rel = rel_href(path, ROOT / order[idx - 1])
    if idx < len(order) - 1:
        next_rel = rel_href(path, ROOT / order[idx + 1])
    lang_twin = sibling_lang(rel, lang)
    lang_rel = rel_href(path, ROOT / lang_twin)

    nav = build_nav(lang, prev_rel, next_rel, lang_rel)
    changed = False

    # CSS: embedded or linked
    if 'href="chapter.css"' in html or "href='chapter.css'" in html:
        css_path = path.parent / "chapter.css"
        if css_path.exists():
            if ensure_css_file(css_path):
                changed = True
        else:
            print(f"WARN missing chapter.css for {rel}")
    else:
        html2, css_changed = ensure_css_in_text(html)
        if css_changed:
            html = html2
            changed = True

    html2, foot_changed = transform_footer(html, nav)
    if foot_changed:
        html = html2
        changed = True

    if changed:
        path.write_text(html, encoding="utf-8")
    return changed


def main() -> None:
    orders = parse_orders(INDEX.read_text(encoding="utf-8"))
    counts: dict[str, int] = defaultdict(int)
    css_updated = 0

    css_paths = list(ROOT.glob("books/**/chapter.css"))
    for css in css_paths:
        if ensure_css_file(css):
            css_updated += 1

    for book, langs in orders.items():
        for lang in ("zh", "en"):
            seq = langs[lang]
            for i, rel in enumerate(seq):
                if process_page(rel, lang, seq, i):
                    counts[book] += 1

    print("CSS files updated:", css_updated)
    print("HTML files updated per book:")
    for book, n in sorted(counts.items()):
        print(f"  {book}: {n}")
    print("Total HTML updated:", sum(counts.values()))

    # Sanity: first/last for each book/lang
    for book, langs in orders.items():
        for lang in ("zh", "en"):
            seq = langs[lang]
            first = ROOT / seq[0]
            last = ROOT / seq[-1]
            ft = first.read_text(encoding="utf-8")
            lt = last.read_text(encoding="utf-8")
            assert 'class="chapter-nav"' in ft and 'class="chapter-nav"' in lt
            # first should disable prev
            fm = re.search(r'<nav class="chapter-nav".*?</nav>', ft, re.DOTALL)
            lm = re.search(r'<nav class="chapter-nav".*?</nav>', lt, re.DOTALL)
            assert fm and "aria-disabled=\"true\"" in fm.group(0)
            assert lm and "aria-disabled=\"true\"" in lm.group(0)
            print(f"OK first/last {book} {lang}: {seq[0].split('/')[-1]} .. {seq[-1].split('/')[-1]}")


if __name__ == "__main__":
    main()
