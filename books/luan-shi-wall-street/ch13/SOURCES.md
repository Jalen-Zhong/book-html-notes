# Sources — 《乱世华尔街》第十三章「小阳春」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML. Book-side rhetoric (trader-desk vantage, Merrill vs Lehman as moral contrast, “false spring / Indian summer” framing) is rewrite/guide; public events are off-book supplements. Not a verbatim reproduction of the copyrighted book.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| NYSE façade | `File:NYC_NYSE.jpg` | Chapter opener / spring 2008 mood (Arnoldius; 1 Apr 2008) |
| Federal Reserve Bank of NY | `File:Federal-reserve-33-liberty.jpg` | Alphabet-soup operations hub (Dmadeo; 2007) |
| Lehman Brothers building | `File:NYC_Lehman_Brothers_building.jpg` | “Next bear” candidate still standing (Arnoldius; 31 Mar 2008) |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized.

## Fact / footnote research URLs

### Post–Bear Stearns market narrative (Mar–Jun 2008)
- Federal Reserve Bank of New York: Timothy Geithner speech, 3 Apr 2008 — actions around Bear, PDCF, tentative calm vs remaining risks
- BIS 78th Annual Report (June 2008), Chapter VI Financial markets — post-Bear spread tightening through April; interbank markets failed to recover; sustainability unclear by mid-May
- Contemporaneous commentary on relief rally vs still-wide TED / LIBOR–OIS (e.g. April 2008 money-market notes)

### Fed liquidity facilities (“alphabet soup”)
- Federal Reserve: Term Auction Facility (TAF) overview — announced 12 Dec 2007; term auctions to sound depository institutions; stigma alternative to discount window
- NY Fed Current Issues / research: Term Securities Lending Facility (TSLF) — announced 11 Mar 2008; Treasuries lent vs less-liquid dealer collateral
- NY Fed Current Issues: Primary Dealer Credit Facility (PDCF) — announced 16 Mar 2008; overnight cash to primary dealers (Chinese book text sometimes says PDLF for the same facility)
- Fed press releases extending PDCF/TSLF (e.g. 30 Jul 2008)

### ARS / municipal short markets
- SEC press release 2008-181 (22 Aug 2008) and related ARS enforcement settlements — February 2008 auction failures when dealers stopped supporting auctions; later par buyback remedies
- Public muni-market reporting on shift from ARS to conventional fixed-maturity issuance in spring 2008

### Merrill Lynch (Thain) vs Lehman (Fuld)
- Merrill Lynch / SEC exhibit (late Jul 2008): ~$30.6B notional U.S. super-senior ABS CDOs sold to Lone Star affiliate for ~$6.7B; associated writedowns and equity raise
- CNBC / Reuters contemporaneous coverage of Merrill writedowns and capital raises
- MarketWatch and other profiles of Dick Fuld’s strategy and slower marks/capital response
- Public accounts of David Einhorn / Greenlight Capital critiques of Lehman (spring–summer 2008, including Ira Sohn reporting) and Erin Callan media exchanges; June 2008 Lehman quarterly loss and ~$6B capital raise

### Macro backdrop
- BLS unemployment and housing-investment narratives for H1 2008 (real-economy lag after financial stress)
- Crisis chronologies placing Lehman intraday panic on 17 Mar 2008 after the 16 Mar Bear/JPMorgan/PDCF weekend

## Delivery notes
- Full self-contained HTML (`false-spring-zh.html` / `false-spring-en.html`) — no `document.write` loaders
- Story rewrite for reading along; official edition required for the complete copyrighted text
- Home links use `../../../index.html` from `books/luan-shi-wall-street/ch13/`
