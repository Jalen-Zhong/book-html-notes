# Sources — 《乱世华尔街》第六章「永不凋谢的花朵」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML. “Lucy Bank / 鲁西银行” is a book alias.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| Amaranthus caudatus | `File:Amaranthus_caudatus0.jpg` | Never-fading flower namesake |
| Federal Reserve Bank of New York | `File:Federal_Reserve_Bank_of_New_York.jpg` | LTCM 1998 coordination stage |
| Wall Street sign (2005) | `File:Wall_Street_Sign_New_York_2005.jpg` | Hero narrative vs liquidation street |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized.

## Fact / footnote research URLs

### LTCM / When Genius Failed
- Public crisis histories of Long-Term Capital Management (1998)
- Roger Lowenstein, *When Genius Failed* (2000) — secondary narrative widely cited
- New York Fed role in coordinating private counterparty rescue (not equity nationalization)

### Black–Scholes–Merton
- Nobel Prize official materials on Scholes & Merton (1997)
- Standard textbook statements of BSM idealizing assumptions (continuous trading, lognormal / Brownian noise)

### Russia 1998
- IMF / public economic histories of the August 1998 ruble devaluation and GKO default/restructuring
- Cross-references in LTCM literature on correlation breakdown

### Amaranth / Hunter / Katrina
- Contemporary press: naturalgasintel.com coverage of Amaranth energy-book transfer and ~$6B+ loss scale vs ~$9B AUM
- WSJ and other Sept 2006 coverage of Brian Hunter, calendar-spread / nat-gas losses
- Public reports of transfer to JPMorgan and Citadel; later CFTC/FERC enforcement context for Hunter

### Fed funds path 2004–06
- Federal Reserve FOMC chronology: 17 consecutive 25 bp hikes from 1.00% (June 30, 2004 start from 1%) to 5.25% (June 29, 2006)
- FRED target federal funds rate series
- Fed Monetary Policy Report accessible tables (2007)

### Money multiplier
- Money-and-banking textbook treatments of base money × multiplier
- Post-crisis discussions of how shadow pipes complicate “effective” multipliers

### Shadow banking / repo / haircuts
- NY Fed public explainers on repo markets
- Gorton & Metrick, “Securitized banking and the run on repo”
- Continuity with ch05 notes on warehouse / overnight funding

### Newton “madness of people” line
- Widely attributed reflection on the South Sea Bubble era (popular finance proverb form); used here as cultural shorthand, not a primary archival citation

## Copyright note
Story prose is an original retelling based on the user’s beat list and publicly available trial-read narrative flow — not a verbatim copy of the book. Footnotes and diagrams are off-book research supplements.

## Bilingual pages (ch06)

| File | Language |
|---|---|
| `never-fading-flower-zh.html` | Chinese story guide (on GitHub: thin loader assembling `parts/zh-part-*.txt`) |
| `never-fading-flower-en.html` | English parallel edition (on GitHub: thin loader assembling `parts/en-part-*.txt`) |
| `SOURCES.md` | This file |

## GitHub Pages assembly note

On GitHub, `never-fading-flower-{zh,en}.html` are thin assemblers that `fetch` + `document.write` the `parts/*-part-*.txt` files (MCP payload-size workaround, same pattern as ch01–ch05). Local `*.standalone.html` copies may also exist for offline full-inline viewing.

Prefer Wikimedia `Special:FilePath/...` URLs in HTML so the GitHub Pages push stays text-sized.
