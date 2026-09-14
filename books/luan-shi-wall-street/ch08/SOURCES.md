# Sources — 《乱世华尔街》第八章「夏季风暴」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML. Personal desk anecdotes (Vince, UBS lift at 75¾, ~$300k lesson, London risk “court martial”) are book-side; public events are off-book supplements.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| NY Fed 33 Liberty (Jul 2007) | `File:Federal-reserve-33-liberty.jpg` | Contemporaneous summer-2007 liquidity stage |
| Wall Street panorama (Dec 2007) | `File:Wall_Street_panorama_vc.jpg` | Street after the summer marks |
| NYSE façade | `File:NYC_NYSE.jpg` | Shared New York market stage |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized.

## Fact / footnote research URLs

### Bear Stearns hedge funds (Jun–Jul 2007)
- NYT 23 Jun 2007: Bear pledges large facility to rescue High-Grade fund
- Reuters / CNN Money: Merrill seizes ~$800M collateral and sells / threatens auction
- BSAM / Cayne investor update (mid-Jul 2007): ~$1.6B collateralized repo line (26 Jun); Enhanced Leverage effectively zero NAV; High-Grade little value left; orderly wind-down

### Collateralized lending / repo / mark-to-market
- Public repo-market primers on haircuts, margin calls, and collateral auctions
- Trading/accounting explainers of mark-to-market in illiquid markets

### ABX
- Markit ABX.HE public index descriptions
- Crisis histories of summer-2007 ABX declines as a subprime price thermometer

### Sowood (context)
- Contemporary coverage of Sowood Capital distress / closure amid July–Aug 2007 credit turmoil (narrative neighbor to Bear unwind)

### BNP Paribas freeze (9 Aug 2007)
- BNP Paribas Investment Partners press release suspending NAV / dealing for Parvest Dynamic ABS, BNP Paribas ABS Euribor, BNP Paribas ABS Eonia
- CNBC / Bloomberg contemporaneous reports (~€1.6B / ~$2.2B scale)
- FCIC archive PDF of the 9 Aug 2007 release; ECB same-day liquidity operations in public chronicles

### Global Alpha / Carhart / liquidity beta
- Contemporary reporting on Goldman Sachs Global Alpha August 2007 drawdowns and crowded quant unwinds
- Asset-pricing literature: Carhart four-factor model; discussions of liquidity risk / liquidity beta vs classic equity factors

### SIFMA / LIBOR ratio & muni basis
- SIFMA Municipal Swap Index (formerly BMA) public methodology materials
- Municipal derivatives practice notes on SIFMA–LIBOR ratio trades and cash-vs-hedge basis widening in stress

## Copyright note
Story prose is an original retelling based on the user’s beat list and publicly available trial-read narrative flow — not a verbatim copy of the book. Footnotes and diagrams are off-book research supplements.

## Bilingual pages (ch08)

| File | Language |
|---|---|
| `summer-storm-zh.html` | Chinese story guide (on GitHub: thin loader assembling `parts/zh-part-*.txt`) |
| `summer-storm-en.html` | English parallel edition (on GitHub: thin loader assembling `parts/en-part-*.txt`) |
| `SOURCES.md` | This file |

## GitHub Pages assembly note

On GitHub, `summer-storm-{zh,en}.html` are thin assemblers that `fetch` + `document.write` the `parts/*-part-*.txt` files (MCP payload-size workaround, same pattern as ch01–ch07). Local `*.standalone.html` copies may also exist for offline full-inline viewing.

Prefer Wikimedia `Special:FilePath/...` URLs in HTML so the GitHub Pages push stays text-sized.
