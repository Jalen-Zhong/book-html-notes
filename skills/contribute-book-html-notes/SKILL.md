---
name: Contribute book HTML notes
description: >-
  Use this when a contributor (or their agent) wants to add a book to the
  book-html-notes GitHub Pages project: accept an uploaded book they have rights
  to, or a book title for public-source research; produce bilingual chapter HTML
  via the project skills; then fork (if needed), push a branch, and open a pull
  request to upstream.
---
# Contribute book HTML notes (fork → push → PR)

## Goal
Add one book’s bilingual rich HTML notes to **upstream** `Jalen-Zhong/book-html-notes` (or the fork this project lives in) through a clean PR, using the same quality bar as the maintainer pipeline.

## Inputs (one of)
1. **Upload path:** user provides files they own or have rights to (PDF/EPUB/text excerpts, notes). Prefer chapter splits the user approves. Never scrape paid stores or pirate mirrors.
2. **Title path:** user gives a book title (+ author if known). Find **public** TOCs, trial reads, interviews, encyclopedia history only. If public narrative is thin, ship labeled **theme + public-history research guides**.

## Always run these project skills
1. Per chapter: [`book-chapter-to-rich-html`](../book-chapter-to-rich-html/SKILL.md) → **zh + en** standalones (or Pages-friendly HTML with shared assets / Wikimedia images).
2. Book orchestration + Pages index expectations: [`book-to-github-pages-notes`](../book-to-github-pages-notes/SKILL.md).

Do not weaken copyright rules.

## GitHub automation (required)

### A. Identify remotes
- **Upstream:** `https://github.com/Jalen-Zhong/book-html-notes` (default).
- If the agent only has write access to the user’s account, **fork** upstream first.

### B. Fork (when the user is not a maintainer with push rights)
Using GitHub CLI or GitHub MCP/API (authenticated as the contributor):
```bash
gh repo fork Jalen-Zhong/book-html-notes --clone=false
# ensure fork exists under the contributor login
```
Or MCP `fork_repository` with `owner=Jalen-Zhong`, `repo=book-html-notes`.

### C. Branch + commit
```bash
gh api user --jq .login   # contributor login
# clone fork OR work via Contents API / push_files on the FORK
git checkout -b book/<book-slug>
```
Add:
- `books/<book-slug>/chNN/*-zh.html`, `*-en.html`, `SOURCES.md`
- Update `index.html` and `README.md` with 中文 / English links

Commit messages: clear, one concern each (e.g. `Add 《书名》 ch01–ch03 bilingual notes`).

### D. Push
```bash
git push -u origin book/<book-slug>
```
Or MCP `push_files` / `create_or_update_file` targeting the **fork** `owner=<contributor>`, `repo=book-html-notes`.

### E. Open Pull Request to upstream
```bash
gh pr create \
  --repo Jalen-Zhong/book-html-notes \
  --head <contributor>:book/<book-slug> \
  --base main \
  --title "Add <book title> bilingual HTML notes" \
  --body "$(cat <<'MD'
## Summary
- Book: …
- Chapters included: …
- Source mode: upload (rights asserted) | public title research

## Checklist
- [x] zh + en per chapter
- [x] copyright notices
- [x] SOURCES.md
- [x] index.html updated
- [x] no verbatim full-text dump
MD
)"
```
Or MCP `create_pull_request` with `owner=Jalen-Zhong`, `repo=book-html-notes`, `head=<contributor>:book/<book-slug>`, `base=main`.

### F. Report back
Give the user the **PR URL**, branch name, and Pages preview note (site updates after merge + Pages build).

## Maintainer path (optional)
If the authenticated user **is** `Jalen-Zhong` (or has write access), you may push a branch on upstream and open a PR for review, or push to `main` only when they explicitly ask for direct publish.

## Quality bar
- Parallel zh/en; story-first or labeled research guides
- No long verbatim copyrighted text
- PR description lists chapters and source mode
- Never force-push to upstream `main`

## Out of scope
- Publishing pirated ebooks
- Opening PRs with secrets, credentials, or personal data dumps
- Spamming multiple unfinished books in one PR
