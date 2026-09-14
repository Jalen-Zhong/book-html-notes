# Contributing

Thank you for helping grow open bilingual book notes on GitHub Pages.

**Upstream:** https://github.com/Jalen-Zhong/book-html-notes  
**Site:** https://jalen-zhong.github.io/book-html-notes/

## Quick path (humans)

1. Fork this repository.
2. Follow the skills in [`skills/`](./skills/) (or ask an AI agent to run them).
3. Add files under `books/<book-slug>/chNN/`.
4. Update root `index.html` and `README.md` with links to **中文** and **English**.
5. Open a Pull Request to `Jalen-Zhong/book-html-notes` (`main`).

## Quick path (AI agents)

Run the skill **[Contribute book HTML notes](./skills/contribute-book-html-notes/SKILL.md)**. It covers:

- User **uploads a book** (files they have rights to) **or** gives a **book title** for public-source research
- Per-chapter **[Book chapter to rich HTML](./skills/book-chapter-to-rich-html/SKILL.md)** → zh + en
- Whole-book orchestration via **[Book to GitHub Pages notes](./skills/book-to-github-pages-notes/SKILL.md)**
- **Fork → branch → commit → push → open PR** to upstream

## Layout

```text
books/
  <book-slug>/
    ch01/
      <section>-zh.html
      <section>-en.html
      SOURCES.md
      assets/                 # optional if HTML uses remote/Wikimedia images
    ch02/
      ...
index.html                    # Pages landing
README.md
skills/                       # agent recipes for this project
COMMUNITY.md
CONTRIBUTING.md
```

## Acceptance checklist (PR)

- [ ] zh + en pages for each new chapter (parallel structure)
- [ ] Story-first (or clearly labeled research guide if no public narrative)
- [ ] Footnotes / diagrams where terms or history need context
- [ ] `SOURCES.md` with real URLs
- [ ] Copyright notice on each page
- [ ] `index.html` updated with links
- [ ] No long verbatim copyrighted text; no full ebook dumps

## Licensing note

Contributed **original retellings, footnotes, and HTML/CSS** are submitted under the repository’s license (see `LICENSE` if present; otherwise CC BY 4.0 for original text + code unless stated otherwise). You must not contribute text you do not have rights to.
