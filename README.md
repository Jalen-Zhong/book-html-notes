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
