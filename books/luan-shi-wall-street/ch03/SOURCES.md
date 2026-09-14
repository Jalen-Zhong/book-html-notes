# Sources — 《乱世华尔街》第三章「鲁西银行」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML. “Lucy Bank / 鲁西银行” is the book’s employer alias.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| Federal Hall / Wall Street | `File:Federal_Hall_National_Memorial,_Wall_Street,_Manhattan,_New_York_(7236982206).jpg` | Financial-district public landmark |
| CME building aerial | `File:Cme_building_aerial_view.jpg` | Pork-belly futures geographic nod |
| NY Fed building | `File:Federal_Reserve_Bank_of_New_York,_Manhattan,_New_York_(7237032812).jpg` | Rates / money-markets landmark |
| Pipe organ | `File:Pipe_organ.jpg` | Visual nod to Vince’s church-organ hobby |
| Goldman 200 West Street | `File:200_West_Street.jpg` | Retention-pitch landmark (same family as ch01/ch02) |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized.

## Fact / footnote research URLs

### Commercial vs investment banks (Glass-Steagall / GLBA)
- https://www.congress.gov/crs-product/R44349
- https://www.everycrsreport.com/reports/R41181.html
- https://www.stlouisfed.org/publications/regional-economist/april-1995/commercial--investment-banking-should-this-divorce-be-saved

### Lehman prestige 2005–06
- https://www.euromoney.com/article/27bjsstsqxhkmh1flp3yn/capital-markets/us-investment-grade-bookrunners-year-end-2005/
- https://www.reuters.com/article/legal/government/table-global-and-european-2006-ma-rankings-dealogic-idUSL15114520/
- https://www.institutionalinvestor.com/article/2btghbmjywmblpwqqrqbk/home/the-2005-all-america-research-team
- https://www.sec.gov/Archives/edgar/data/806085/000110465906081389/a06-24932_9ex99d1.htm (Lehman 2006 results / research rankings)

### Pork belly futures
- https://www.reuters.com/article/markets/stocks/cme-shuts-down-iconic-pork-belly-futures-market-idUSN1E76E1ET/
- https://www.npr.org/sections/money/2011/08/10/138517906/requiem-for-pork-bellies
- https://marketswiki.com/wiki/Pork_Bellies

### Interest rate swaps
- ISDA / Federal Reserve public primers on interest-rate swaps
- LIBOR→SOFR transition public background (post-chapter contrast)

### Municipal bonds market basics
- MSRB public investor education materials
- https://am.gs.com/en-us/institutions/campaign/goldman-sachs-municipal-bonds (industry overview example)
- Standard Investopedia / market primers on tax-exempt munis

### “40 under 40” lists
- Fortune / Institutional Investor public “40 Under 40” list formats (industry prestige badges)

### Prop trading (pre-Volcker)
- https://www.efinancialcareers.com/news/2005/02/senior-proprietary-trader-how-much-am-i-worth
- https://www.efinancialcareers.co.uk/news/2004/10/prop-trading-is-training-ground-for-managers
- Volcker Rule / Dodd-Frank public background (post-crisis contrast)

### Goldman retention / culture
- Goldman Sachs public campus recruiting and culture narratives
- Cross-read with ch02 footnotes on 2005 compensation and “Because we are Goldman”

## Copyright note
Story prose is an original retelling based on publicly available trial-read narrative flow — not a verbatim copy of the book. Footnotes and diagrams are off-book research supplements. “Lucy Bank / 鲁西银行” is the book’s alias for the employer.

## Bilingual pages (ch03)

| File | Language |
|---|---|
| `lucy-bank-zh.html` | Chinese story guide (on GitHub: thin loader assembling `parts/zh-part-*.txt`) |
| `lucy-bank-en.html` | English parallel edition (on GitHub: thin loader assembling `parts/en-part-*.txt`) |
| `SOURCES.md` | This file |

## GitHub Pages assembly note

On GitHub, `lucy-bank-{zh,en}.html` are thin assemblers that `fetch` + `document.write` the `parts/*-part-*.txt` files (MCP payload-size workaround, same pattern as ch01/ch02). Local `*.standalone.html` copies may also exist for offline full-inline viewing.

Prefer Wikimedia `Special:FilePath/...` URLs in HTML so the GitHub Pages push stays text-sized.
