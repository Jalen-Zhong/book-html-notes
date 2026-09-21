# Sources — 《乱世华尔街》第十六章「潘多拉的盒子」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML. Book-side rhetoric (trader-desk POV on Monday noise, Reserve Primary as “boring cash,” AIG AAA no-collateral trap, NYSE Wednesday visit, short-ban irony, week ending near the prior Friday, foreshadow of the Paulson Plan) is rewrite/guide aligned to public trial-read *beats*; public events are off-book supplements. Not a verbatim reproduction of the copyrighted book.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| Lehman HQ (Times Square) | `File:Lehman_Brothers_Times_Square_by_David_Shankbone.jpg` | Chapter opener; 745 Seventh Ave. (David Shankbone) |
| American International Building | `File:American_International_Building.jpg` | Former AIG-associated tower, 70 Pine St. (Sergio Rodríguez) |
| New York Stock Exchange | `File:New_York_Stock_Exchange_Exterior.jpg` | NYSE exterior for Wednesday floor visit beat |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized.

## Fact / footnote research URLs

### Lehman bankruptcy and recovery
- Yale Program on Financial Stability / *Journal of Financial Crises*: Lehman Brothers Bankruptcy overview cases
- FRASER / Federal Reserve Bank of St. Louis Financial Crisis Timeline (15 Sep 2008 filing)
- Contemporary reports of ISDA Lehman CDS auction recovery (~8.625 cents)

### Money funds and commercial paper
- Yale / SEC materials on Reserve Primary Fund (~$785M Lehman CP; NAV ~$0.97 on 16 Sep 2008)
- FCIC Final Report chapters on money-market runs and CP freeze
- U.S. Treasury temporary guarantee program announcements (late Sep 2008 context)

### AIG rescue
- Federal Reserve Board / New York Fed: Actions Related to AIG ($85B facility, 79.9% equity, LIBOR+8.5%)
- FCIC Final Report Chapter 19 (September 2008 AIG bailout)
- Rating-agency downgrade and collateral-call chronologies (15–16 Sep)

### Short bans and market week
- SEC / FSA September 2008 emergency short-sale restrictions on financials
- Contemporary market coverage of 17 Sep equity plunge and late-week rebound

### Book chapter framing (public trial / catalog only — rewrite, do not paste)
- Public TOC: §16「潘多拉的盒子」/「潘朵拉的盒子」 after §15「沙中的红线」, before §17「保尔森计划」
- Public trial-read pages (e.g. FX110 chapter listing) used only for beat alignment: largest bankruptcy → nine-cent recovery / collateral → Pandora seal metaphor → Monday desk → Reserve Primary → AIG AAA/CDS → $85B rescue → NYSE/shorts → foreshadow Paulson Plan

## Delivery notes
- Full self-contained HTML (`pandoras-box-zh.html` / `pandoras-box-en.html`) — no `document.write` loaders
- Story rewrite for reading along; official edition required for the complete copyrighted text
- Home links use `../../../index.html` from `books/luan-shi-wall-street/ch16/`
