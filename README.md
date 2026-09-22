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
  - **更新中**：导论 + §1–§6（第一部分完）已上线；全书计划约 13 单元（下一批 §7 起三国案例等）
  - §3 通缩型子章：总览 · 早期 · 泡沫 · 顶部 · 萧条 · 美丽去杠杆 · 推绳子 · 正常化
  - §4 通胀型子章：总览 · 早期 · 泡沫 · 顶部与护汇 · 萧条 · 正常化 · 恶性通胀螺旋
  - §5 战时经济 · §6 第一部分总结 — see [index](https://jalen-zhong.github.io/book-html-notes/)

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
