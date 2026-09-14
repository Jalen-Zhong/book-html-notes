---
name: Book to GitHub Pages notes
description: >-
  Use this when the user gives a book title (or asks to process a whole book)
  and wants it broken into chapters as bilingual rich HTML via Book chapter to
  rich HTML, then published to their book-html-notes GitHub repo and reflected
  on GitHub Pages.
---
# Whole book → bilingual HTML notes on GitHub Pages

## Goal
When the user gives a **book title** (and optional scope), produce a full set of **chapter HTML reading pages** in **Chinese and English**, publish them to their **book HTML notes GitHub repo**, and refresh the **GitHub Pages** index so the book is readable online.

This skill is the **pipeline**. For each chapter’s content quality and page design, **run [Book chapter to rich HTML](sand-workflow:book-chapter-to-rich-html)** (ZH + EN standalones, story-first, footnotes, images, diagrams). Do not re-specify that recipe here—follow it.

## When to use
- “把《…》整本按章节做成中英 HTML，推到 repo / Pages”
- “给书名，按 Book chapter to rich HTML 沉淀并更新 GitHub Pages”
- Any request that is **book-scale** (many chapters) plus **publish**, not a single chapter only

If they only want one chapter and no publish step, use **Book chapter to rich HTML** alone.

## Defaults
- **Languages:** Chinese + English per chapter (two files), via the chapter skill.
- **Copyright:** public sources / trial reads / summaries only; original retelling; never full verbatim pirated text.
- **Repo:** the user’s book-notes GitHub repository (commonly `owner/book-html-notes`). If unsure which repo, confirm once.
- **Layout on GitHub:**
  ```text
  books/<book-slug>/
    ch01/
      <section>-zh.html
      <section>-en.html
      SOURCES.md
      assets/          # optional if standalones embed images
    ch02/
      ...
  index.html           # Pages landing; list all books/chapters with ZH/EN links
  README.md            # short index + Pages URL
  ```
- **Filenames:** prefer `…-zh-standalone.html` / `…-en-standalone.html` in the chapter folder (or clearly named `…-zh.html` / `…-en.html` if they already use non-embedded + assets).
- **Pages URL pattern:** `https://<owner>.github.io/<repo>/` (e.g. `https://jalen-zhong.github.io/book-html-notes/`).
- **Language of chat updates:** match the user.

## Workflow

### 1. Scope the book
- Confirm book title, author if known, and scope: whole book vs selected chapters.
- Build a **chapter list** from public TOCs (publisher pages, library catalogs, reputable summaries). Show the planned chapter list briefly before a long run if the book is large; otherwise proceed and report the list in the first progress update.
- Choose a stable `book-slug` (kebab-case ASCII).

### 2. Process chapter by chapter
For each chapter in order:
1. Invoke / follow **Book chapter to rich HTML** for that chapter only.
2. Produce ZH + EN standalones (+ working folder + `SOURCES.md`).
3. Keep tone and enrichment depth consistent across the book.
4. After each chapter (or small batch), **commit/push** to the repo so progress is not lost on a long book.
5. Send the user a short progress beat (chapter N done; files pushed).

Do heavy research/build work via background executors when multi-step; stay responsive in chat.

### 3. Publish to GitHub
- Use the connected **GitHub connector / MCP** (or `gh` if authenticated) to create/update files on `main` (or the repo’s default branch).
- Paths under `books/<book-slug>/chNN/…`.
- Do not force-push. Do not delete unrelated books.
- If the repo is empty, seed `README.md` / `index.html` first so tooling that cannot start from an empty repo can proceed.

### 4. Update GitHub Pages surface
- Update root `index.html` to list the book and each chapter with **中文 / English** links.
- Update `README.md` with the online URL and current books.
- Ensure Pages is enabled (Deploy from `main` / root, or the repo’s existing Pages config). If the API/connector cannot toggle Pages, push content then give the user the one-screen Settings → Pages path and the expected site URL.
- After enablement, smoke-check the Pages URL when possible.

### 5. Finish
- Summarize: chapter count, repo URL, Pages URL, any chapters skipped and why.
- Offer the next missing chapter or another book—do not start a new book unprompted.

## Quality bar
- Every published chapter has both ZH and EN pages with parallel structure.
- Landing page links resolve on Pages.
- No fabricated citations; `SOURCES.md` per chapter (or shared book-level sources plus chapter notes).
- Long books: incremental pushes; never silent multi-hour runs without progress updates.

## Out of scope
- Selling/distributing copyrighted full text as “the book”
- Replacing the chapter skill’s narrative/footnote standards
- Creating a new GitHub account or bypassing the user’s chosen publish repo
