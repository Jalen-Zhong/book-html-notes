# Sources — 《乱世华尔街》第二章「高盛实习」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| Goldman HQ / 200 West Street | `File:200 West Street.jpg` | Same family as ch01 |
| Roasted coffee beans | `File:Roasted coffee beans.jpg` | Visual nod to J. Aron coffee-trading origins |
| NYSE Broad Street exterior | `File:New York Stock Exchange Exterior.jpg` | Kidfly182, CC BY-SA 4.0 |
| Rockefeller Center Christmas tree | `File:Rockefeller Center christmas tree.jpg` | Year-end Manhattan public imagery |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized. Optional local `assets/` copies can be added later for offline use.

## Fact / footnote research URLs

### J. Aron (1981 acquisition)
- https://www.goldmansachs.com/our-firm/history/moments/1981-jaron
- https://www.nytimes.com/1981/10/30/business/goldman-sachs-buys-big-commodity-dealer.html

### Lloyd Blankfein
- https://www.goldmansachs.com/our-firm/history/moments/2006-blankfein-assumes-leadership
- https://en.wikipedia.org/wiki/Lloyd_C._Blankfein
- https://www.nytimes.com/2018/07/17/business/dealbook/lloyd-blankfein-goldman-career.html

### SecDB (Securities Database)
- https://www.goldmansachs.com/our-firm/history/moments/1993-secdb
- https://en.wikipedia.org/wiki/SecDB (Michael Dubno / SecDB public overview)
- https://fortune.com/2016/09/07/goldman-sachs-software/
- https://developer.gs.com/blog/posts/secdb-observability-journey
- UFO / YAMS: mentioned in trial-read internship context only; no independent public encyclopedia entries used — treated as internal desk toolchain labels without invented technical detail.

### 1999 IPO / partner system
- https://www.goldmansachs.com/our-firm/history/moments/1999-ipo
- https://money.cnn.com/1999/05/03/markets/goldman/
- https://www.goldmansachs.com/our-firm/history/ipo-anniversary
- SEC IPO prospectus summaries (e.g. EDGAR filings for The Goldman Sachs Group, Inc.)

### 2005 record compensation
- https://www.sec.gov/Archives/edgar/data/886982/000095012305014780/y15556exv99w1.htm
- https://www.efinancialcareers.com/news/2006/02/goldman-sachs-paid-staff-117-billion-in-2005

### NYSE–Archipelago 2005 dual-advisor controversy
- https://www.nbcnews.com/id/wbna7791518
- https://www.latimes.com/archives/la-xpm-2005-apr-28-fi-goldman28-story.html
- https://nypost.com/2005/12/06/judge-slaps-bank-nyse-ok-goldman-hit/
- Archipelago Holdings SEC Form 8-K (Apr 2005 merger agreement / Goldman letter agreement)
- Higgins v. NYSE public case summaries

### Insider trading / MNPI (general)
- SEC public primers on insider trading and material nonpublic information
- Standard IB compliance training summaries (Chinese walls, watch/restricted lists)

### Prop trading circa 2005
- https://www.efinancialcareers.com/news/2005/02/senior-proprietary-trader-how-much-am-i-worth
- https://www.efinancialcareers.co.uk/news/2004/10/prop-trading-is-training-ground-for-managers
- Volcker Rule / Dodd-Frank public background (post-crisis contrast)

### CFA Program
- https://www.cfainstitute.org/programs/cfa-program/exam
- https://www.cfainstitute.org/programs/cfa-program/charter

### Goldman / ICBC strategic investment (2006)
- https://www.icbc.com.cn/en/page/721853448638464043.html (ICBC announcement, 27 Jan 2006)
- https://www.icbc.com.cn/en/page/721853698501541917.html (capital settlement)
- Wharton / academic case PDFs summarizing ~$3.78bn consortium / ~5.75% Goldman stake

## Copyright note
Story prose is an original retelling based on publicly available trial-read narrative flow — not a verbatim copy of the book. Footnotes and diagrams are off-book research supplements. “Lucy Bank” is the book’s alias; Keen’s later insider-trading mention is summarized as the author’s cautionary beat, not a docket dump.

## Bilingual pages (ch02)

| File | Language |
|---|---|
| `goldman-internship-zh.html` | Chinese story guide (GitHub = loader; local = full ~31KB) |
| `goldman-internship-en.html` | English parallel edition (same) |
| `parts/zh-part-*.txt` / `parts/en-part-*.txt` | Split bodies assembled at runtime on GitHub Pages |
| `SOURCES.md` | This file |

## GitHub Pages assembly note

On GitHub, `goldman-internship-{zh,en}.html` are thin assemblers that `fetch` + `document.write` the `parts/*-part-*.txt` files (MCP payload-size workaround, same pattern as ch01). Local copies of those same filenames are the full inline HTML (~31KB each).

Prefer Wikimedia `Special:FilePath/...` URLs in HTML so the GitHub Pages push stays text-sized.
