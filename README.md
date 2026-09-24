# Book HTML Notes

Story-first, research-enriched **bilingual (zh / en)** HTML reading notes for books — published with GitHub Pages.

## Read online

https://jalen-zhong.github.io/book-html-notes/

## Current books

- 《乱世华尔街》 / `luan-shi-wall-street`（渔阳 · 一位华人交易员的经历）
  - Chapters §1–§24 + 后记 on Pages — see [index](https://jalen-zhong.github.io/book-html-notes/)

- 《置身事内》 / `zhishen-shinei`（兰小欢 · 中国政府与经济发展，上海人民出版社 2021）
  - 前言 + §1–§8 + **结束语** complete on Pages — see [index](https://jalen-zhong.github.io/book-html-notes/)
  - Closing: [结束语 · 中文](books/zhishen-shinei/closing/closing-remarks-zh.html) · [Closing Remarks · English](books/zhishen-shinei/closing/closing-remarks-en.html)


- 《债务危机》 / `big-debt-crises`（瑞·达利欧 Ray Dalio · Bridgewater, 2018）
  - **已完结（13 / 13）**：导论 + §1–§12 全上线（含 §3/§4/§7/§8/§9/§10/§12 嵌套子章）
  - Pages：[index](https://jalen-zhong.github.io/book-html-notes/) · [§10 共性总览](https://jalen-zhong.github.io/book-html-notes/books/big-debt-crises/ch10/overview-zh.html) · [§11 术语](https://jalen-zhong.github.io/book-html-notes/books/big-debt-crises/ch11/glossary-zh.html) · [§12 宏观审慎](https://jalen-zhong.github.io/book-html-notes/books/big-debt-crises/ch12/overview-zh.html)
  - §3 通缩型 · §4 通胀型 · §5 战时 · §6 Part1 总结 · §7 德国 · §8 美 1928–37 · §9 美 2007–11
  - §10 48 案共性（本币/外币）· §11 关键术语要点 · §12 宏观审慎附录（工具箱 + 美国史要点）


- 《原则：应对变化中的世界秩序》 / `changing-world-order`（瑞·达利欧 Ray Dalio · Simon & Schuster, 2021）
  - **已完结（17 / 17）**：如何读 + 导论 + §1–§14 + 附录（含嵌套子章；跳过极短 glossary）
  - Pages：[index](https://jalen-zhong.github.io/book-html-notes/) · [§12 总览](https://jalen-zhong.github.io/book-html-notes/books/changing-world-order/ch12/overview-zh.html) · [§13 总览](https://jalen-zhong.github.io/book-html-notes/books/changing-world-order/ch13/overview-zh.html) · [§14 总览](https://jalen-zhong.github.io/book-html-notes/books/changing-world-order/ch14/overview-zh.html) · [附录](https://jalen-zhong.github.io/book-html-notes/books/changing-world-order/appendix/overview-zh.html)

## Contribute

Community guidelines: [COMMUNITY.md](./COMMUNITY.md)  
How to add a book (humans + agents): [CONTRIBUTING.md](./CONTRIBUTING.md)  
Agent skills: [`skills/`](./skills/)

Pipeline skills:
1. [Book chapter to rich HTML](./skills/book-chapter-to-rich-html/SKILL.md) — one chapter → zh + en
2. [Book to GitHub Pages notes](./skills/book-to-github-pages-notes/SKILL.md) — whole book orchestration
3. [Contribute book HTML notes](./skills/contribute-book-html-notes/SKILL.md) — upload or title → fork → push → PR

## Layout

```text
books/<book-slug>/chNN/*-zh.html
books/<book-slug>/chNN/*-en.html
books/<book-slug>/chNN/SOURCES.md
books/<book-slug>/closing/   # optional book closing (e.g. 结束语)
```

## License

Original notes & site code: see [LICENSE](./LICENSE) (CC BY 4.0).  
Underlying books remain © their authors/publishers.
