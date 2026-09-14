# Sources — 《乱世华尔街》第五章「杜邦公式」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML. “Lucy Bank / 鲁西银行” and “Hyper Goldman / 超盛” are book aliases or fable names.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| NYSE exterior (2011) | `File:New_York_Stock_Exchange_July_2011.jpg` | Board / ROE city stage |
| Federal Reserve Board building | `File:Federal_Reserve_Board_Building.jpg` | Greenspan-era liquidity backdrop |
| Wall Street sign (2005) | `File:Wall_Street_Sign_New_York_2005.jpg` | Overnight funding vs daytime myth |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized.

## Fact / footnote research URLs

### DuPont identity / ROE
- Corporate-finance textbook treatments of DuPont analysis (margin × turnover × leverage)
- Public primers on ROE as a bank/dealer KPI

### Shadow banking
- NY Fed and FSB public definitions of shadow banking
- Crisis retrospectives on repo / ABCP / securitization pipes

### ABS/CDO warehouse
- FCIC and structured-credit primers on CDO pipelines and warehouses

### Repo / haircut
- https://www.newyorkfed.org/research/staff_reports (repo market explainers)
- Gorton & Metrick, “Securitized banking and the run on repo”

### Broker-dealer leverage pre-crisis
- SEC / GAO / FCIC discussions of dealer leverage (~30× order of magnitude for some firms)
- Duffie, “The Failure Mechanics of Dealer Banks”

### CDS / CDX
- Markit/Nomura “CDO/CDS Update” 18 Dec 2006 (FCIC archive) — CDX.NA.IG ~34.5 bps
- https://fcic-static.law.stanford.edu/cdn_media/fcic-docs/2006-12-18%20Nomura%20Fixed%20Income%20Research,%20CDO_CDS%20Update.pdf
- Markit CDX index primers

### Greenspan-era rates
- FRED federal funds rate series
- Federal Reserve FOMC chronologies 2001–06

### Prop vs agency
- Industry primers on proprietary vs agency/market-making businesses
- Continuity with ch04 notes; Volcker Rule as post-crisis contrast

### SIV / TOB-style structures
- FCIC / contemporary press on SIV consolidations (e.g., Citi, HSBC 2007)
- Municipal tender-option-bond market-structure primers

### Author thesis (macro metaphor)
- Restated carefully from public trial-read narrative flow as *authorial thesis*, not official macro statistics
- Balance-of-payments / capital-flow literacy used only for contrast reading

## Copyright note
Story prose is an original retelling based on publicly available trial-read narrative flow and the user’s beat list — not a verbatim copy of the book. Footnotes and diagrams are off-book research supplements.

## Bilingual pages (ch05)

| File | Language |
|---|---|
| `dupont-formula-zh.html` | Chinese story guide (on GitHub: thin loader assembling `parts/zh-part-*.txt`) |
| `dupont-formula-en.html` | English parallel edition (on GitHub: thin loader assembling `parts/en-part-*.txt`) |
| `SOURCES.md` | This file |

## GitHub Pages assembly note

On GitHub, `dupont-formula-{zh,en}.html` are thin assemblers that `fetch` + `document.write` the `parts/*-part-*.txt` files (MCP payload-size workaround, same pattern as ch01–ch04). Local `*.standalone.html` copies may also exist for offline full-inline viewing.

Prefer Wikimedia `Special:FilePath/...` URLs in HTML so the GitHub Pages push stays text-sized.
