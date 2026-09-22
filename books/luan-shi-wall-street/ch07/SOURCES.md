# Sources — 《乱世华尔街》第七章「连环计」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML. “Lucy Bank / 鲁西银行” and personal desk anecdotes are book-side; public events are off-book supplements.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| Wall Street sign (2005) | `File:Wall_Street_Sign_New_York_2005.jpg` | Party / Street shared stage |
| Fannie Mae headquarters | `File:Fannie_Mae_headquarters.jpg` | GSE / MBS infrastructure |
| Battle of Red Cliffs imagery | `File:Battle_of_Red_Cliffs.jpg` | Interlocking-ships metaphor |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized.

## Fact / footnote research URLs

### Subprime / prime & GSEs
- Standard housing-finance definitions of prime vs subprime (credit, documentation, pricing)
- Public explainers on Fannie Mae / Freddie Mac roles in conforming mortgages and agency MBS

### Tranching / CDO / CDO²
- Structured-credit primers on senior/mezz/equity waterfalls
- Post-crisis public postmortems on CDO and CDO-squared correlation sensitivity

### 2006 bulge-bracket bonuses (publicly cited figures used in retell)
- NY State Comptroller / USA Today: Wall Street bonus pool ~$23.9B (avg bonus ~$137k) for 2006
- Goldman Sachs FY2006: compensation & benefits ~$16.4B; ~$622k per employee (CNN / company disclosures)
- NYT Dec 2006: Blankfein ~$53.4M bonus; Mack ~$41M; Fuld restricted-stock / long-term award headlines

### HSBC Household (Feb 2007)
- HSBC Holdings trading update, 8 Feb 2007 (U.S. Mortgage Services / impairment charges above consensus)
- Reuters contemporary coverage of HSBC bad-debt charge warning and Household lineage

### New Century (2007)
- Reuters: New Century Chapter 11 filing (~2 Apr 2007), lending halt, mass layoffs
- BIS / bankruptcy-examiner case literature on originate–warehouse–securitize failure

### LBO / bridge loan / EOP / TXU / Zell Tribune
- Contemporary coverage of Blackstone–Equity Office and KKR–TXU-scale LBO financing
- Primers on acquisition bridge loans and packaged takeout risk on IB books
- Sam Zell / Tribune going-private transaction (SEC / company releases, 2007); irony vs EOP sale timing is narrative framing grounded in public deal chronology

### Blackstone / CIC precursor
- Blackstone press release: State Investment Company ~$3B non-voting units at IPO, stake kept under 10%, multi-year hold
- CRS and later public summaries treating the stake as early CIC-related capital

### Bear Stearns related hedge funds (June 2007)
- NYT 23 Jun 2007: Bear pledges up to ~$3.2B to rescue High-Grade Structured Credit fund
- Contemporary coverage of Enhanced Leverage sister fund distress and creditor margin calls

## Copyright note
Story prose is an original retelling based on the user’s beat list and publicly available trial-read narrative flow — not a verbatim copy of the book. Footnotes and diagrams are off-book research supplements.

## Bilingual pages (ch07)

| File | Language |
|---|---|
| `interlocking-stratagem-zh.html` | Chinese story guide (on GitHub: thin loader assembling `parts/zh-part-*.txt`) |
| `interlocking-stratagem-en.html` | English parallel edition (on GitHub: thin loader assembling `parts/en-part-*.txt`) |
| `SOURCES.md` | This file |

## GitHub Pages assembly note

On GitHub, `interlocking-stratagem-{zh,en}.html` are thin assemblers that `fetch` + `document.write` the `parts/*-part-*.txt` files (MCP payload-size workaround, same pattern as ch01–ch06). Local `*.standalone.html` copies may also exist for offline full-inline viewing.

Prefer Wikimedia `Special:FilePath/...` URLs in HTML so the GitHub Pages push stays text-sized.
