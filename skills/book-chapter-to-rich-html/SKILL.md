---
name: Book chapter to rich HTML
description: >-
  Use this when the user wants a book chapter (or episode/section) turned into
  rich HTML reading pages: story-style narrative, section footnotes with
  researched background and term explanations, images, knowledge graphs,
  character maps, timelines — delivered as two self-contained HTML files
  (Chinese edition + English edition) they can open directly.
---
# Book chapter → rich HTML reading pages (ZH + EN)

## Goal
Produce **two self-contained HTML files** the user can open in a browser:
1. **Chinese edition** (`…-zh-standalone.html` or `…-zh.html`)
2. **English edition** (`…-en-standalone.html` or `…-en.html`)

Keep a **story-driven retelling** of what happens in the chapter (who did what, in order). Enrich hard spots with **off-book research** (footnotes, images, diagrams). Do **not** paste long verbatim copyrighted text — rewrite in original phrasing from public trial reads / summaries / the user’s own materials.

Both editions must cover the **same chapter beats**, figures, diagrams, and footnote topics; only the UI chrome and prose language differ. Do not ship a single mixed bilingual page unless the user explicitly asks for one file.

## Defaults (match unless the user overrides)
- **Two files:** always deliver Chinese + English standalones (default). If the user asks for only one language, then one file is OK.
- **Narrative first:** chronological story of the protagonist’s experiences; avoid “key takeaways / 要点清单” as the main structure.
- **Enrich when needed:** if a term, institution, event, or joke is hard to understand from the chapter alone, research it on the web and explain in a **footnote block at the end of that story section** (localized to that edition’s language).
- **Rich extras:** images, Mermaid knowledge graphs, character/relationship maps, timelines, period background cards — shared assets, captions localized per edition.
- **Delivery:** two **standalone HTML** files with images embedded as `data:` URIs (not a zip/tar unless asked). Also keep a working folder with shared `assets/` + non-embedded `…-zh.html` / `…-en.html` + one `SOURCES.md` for iteration.
- **Language:** Chinese edition fully in Chinese; English edition fully in English (including hero, TOC, footnote headings, figure captions, footer). Mirror structure section-for-section.
- **Copyright note** in each hero: story is a rewrite/guide; footnotes are outside research; full text → support the official edition.

## Workflow

### 1. Scope the chapter
- Confirm book, chapter/section title, and any preferred tone.
- Locate **public** sources only (trial reads, catalog blurbs, interviews, encyclopedic history). Never scrape or reproduce a full pirated chapter.

### 2. Retell the story (both languages)
- Draft the narrative outline once (section headings + beat list).
- Write the **Chinese** sectioned prose, then write a natural **English** retelling of the same beats (not a stiff machine calque).
- Prefer prose over bullet summaries. Short “scene” callouts are fine for a pivotal quote or turning point (paraphrased or short fair-use length); translate/adapt callouts per edition.

### 3. Mark enrichment targets
While drafting, flag places that need footnotes, e.g.:
- Industry jargon (front/back office, Sharpe ratio, product names)
- Historical events the book name-drops (crashes, reforms, wars)
- Institutions and people (banks, professors, regulators)
- Games, exams, instruments that assume prior knowledge

### 4. Research footnotes
For each flag, web-search period-accurate background. Each footnote should include:
- Plain-language explanation (ZH in Chinese file; EN in English file)
- Why it matters for **this** chapter beat
- A short source label (site/book name), with full URLs collected once in shared `SOURCES.md`

Aim for roughly **8+ footnotes** on a dense chapter unless the user asks for lighter notes. Keep footnote **count and topics aligned** across ZH/EN.

### 5. Visuals and diagrams
- Download **freely usable** images (prefer Wikimedia Commons); caption + license/source under each figure (localized captions).
- Save under `…/assets/` with clear filenames; both editions reuse the same assets.
- Embed at least (same diagrams in both files; labels/captions localized):
  - **Journey / event timeline** (Mermaid or CSS cards)
  - **Character / relationship map**
  - **Concept knowledge graph** tying the chapter’s core ideas
- Use Mermaid via CDN (`mermaid@10` on jsDelivr) unless the user forbids network.
- Optional: a small language switch link in the hero pointing to the sibling file’s expected filename (relative), if both will sit in the same folder.

### 6. Page design
Each HTML, dark readable theme, max-width ~720–920px:
- Hero: badge, title, subtitle, copyright/research note (`lang="zh-CN"` vs `lang="en"`)
- Optional TOC chips linking to story sections
- Story sections → figures → section footnote blocks (`本节脚注` / `Section notes`)
- Diagram panels with short captions
- Footer with book attribution

### 7. Package for the user
1. Build folder HTMLs with relative `assets/` paths: `…-zh.html`, `…-en.html`.
2. Generate standalones: `…-zh-standalone.html`, `…-en-standalone.html` (embed `assets/` as base64 `data:` URIs; Mermaid may still need CDN).
3. Send **both standalone HTML files as direct attachments** (default). Only send an archive if they ask.
4. Briefly list what was added (footnote count, diagram types, image count) once for both editions.
5. If the user also maintains a GitHub `book-html-notes`-style repo, offer to push both files into the chapter folder (do not assume; ask or follow an existing standing preference).

### 8. Iterate
If they say “too summary,” push more story in **both** editions. If “too thin,” add footnotes/diagrams in both. If they ask for only one language after the fact, send that standalone only.

## Quality bar
- Story readable without the footnotes; footnotes deepen, not replace, the plot.
- ZH and EN editions stay parallel in structure and research depth.
- No fabricated dates, quotes, or image sources — if research fails, say so in the footnote or omit.
- Diagrams must reflect the chapter’s actual people/events/ideas, not generic filler.
- Each standalone opens and shows images without unpacking.

## Out of scope
- Full-book OCR dumps or chapter-length verbatim reproduction
- Paywalled content scraping
- Claiming the HTML is the official book text
- A single side-by-side bilingual HTML as the default (only if the user asks)
