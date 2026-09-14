# Sources — 《乱世华尔街》第四章「宇宙的中心」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML. “Lucy Bank / 鲁西银行” is the book’s employer alias.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| NYSE trading floor (2001) | `File:NYSE-floor.jpg` | “Center of the universe” / wet-market visual |
| NYSE traders floor (1963) | `File:NY_stock_exchange_traders_floor_LC-U9-10548-6.jpg` | Open-floor culture cousin |
| NY Fed building | `File:Federal_Reserve_Bank_of_New_York,_Manhattan,_New_York_(7237032812).jpg` | Rates / Treasuries landmark |
| Federal Hall / Wall Street | `File:Federal_Hall_National_Memorial,_Wall_Street,_Manhattan,_New_York_(7236982206).jpg` | Licensing / district backdrop |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized.

## Fact / footnote research URLs

### 2006 pre-crisis boom
- Federal Reserve and public crisis chronologies for 2005–08
- Industry primers on leverage / structured-credit boom years

### Trading-floor culture / turret / squawk
- Industry oral histories of sales & trading floors
- Trading-comms vendor primers on turret phones and squawk boxes

### Eurodollar futures
- CME / textbook definitions of Eurodollar futures
- LIBOR-era money-market primers

### FICC structure & products
- Bank public FICC / S&T segment disclosures
- NY Fed materials on Treasuries and agency securities
- DTCC FICC Mortgage-Backed Securities Division overview
- ISDA interest-rate swap primers
- FINRA Series 7 Treasuries & agencies study materials

### Municipal bond tax exemption / federalism
- https://www.msrb.org/Tax-Treatment
- https://www.msrb.org/Education/Municipal-Bond-Basics-0
- https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-37
- https://encyclopedia.federalism.org/index.php?title=Municipal_Securities_%2F_Municipal_Bonds
- South Carolina v. Baker (1988) public case summaries

### Prop vs agency / market-making
- eFinancialCareers prop-trading culture pieces (mid-2000s)
- Volcker Rule / Dodd-Frank public background (post-crisis contrast)

### Inter-dealer brokers
- Fixed-income market-structure primers on IDBs

### Series 7 / 63
- https://www.finra.org/registration-exams-ce/qualification-exams/series7
- Series 63 (Uniform Securities Agent State Law) public exam primers

## Copyright note
Story prose is an original retelling based on publicly available trial-read narrative flow — not a verbatim copy of the book. Footnotes and diagrams are off-book research supplements. “Lucy Bank / 鲁西银行” is the book’s alias for the employer.

## Bilingual pages (ch04)

| File | Language |
|---|---|
| `center-of-universe-zh.html` | Chinese story guide (on GitHub: thin loader assembling `parts/zh-part-*.txt`) |
| `center-of-universe-en.html` | English parallel edition (on GitHub: thin loader assembling `parts/en-part-*.txt`) |
| `SOURCES.md` | This file |

## GitHub Pages assembly note

On GitHub, `center-of-universe-{{zh,en}}.html` are thin assemblers that `fetch` + `document.write` the `parts/*-part-*.txt` files (MCP payload-size workaround, same pattern as ch01–ch03). Local `*.standalone.html` copies may also exist for offline full-inline viewing.

Prefer Wikimedia `Special:FilePath/...` URLs in HTML so the GitHub Pages push stays text-sized.
