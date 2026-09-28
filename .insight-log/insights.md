# Insights

> Retro-mined 2026-08-31 from Codex CLI/app transcripts. Model state fields are reconstructed from surrounding transcript context rather than written at capture time — treat them as lower-confidence than live captures.

## I-001 · Respect an established ordering convention (chronological) rather than inserting by other criteria
- **Layer**: expression
- **Task**: Updating publication list ordering on CV
- **Model state**: Had inserted a new entry after a specific other entry rather than at the chronological end
- **Quote**: 请不要将 SODA 插入 ICML 后，而是逐一放在最后，我是按时间顺序排的
- **Outcome**: adopted

## I-002 · Don't regress a layout that was already correct in an earlier revision
- **Layer**: execution
- **Task**: Adjusting CV layout (column width) across a revision cycle
- **Model state**: Had changed the column width again after a version that was already correct
- **Quote**: 不是，中文版之前就是好的，一页，并且栏宽合适，SODA 的后两个一行。你怎么又把栏宽变窄了？
- **Outcome**: adopted

## I-003 · Match the existing publication format and leave unknown metadata unset
- **Layer**: execution
- **Task**: Adding four arXiv preprints and one accepted NeurIPS 2026 paper
- **Model state**: Before implementation, inspecting the existing publication bundles and rendering templates
- **Quote**: 记得仿照之前的格式，缺失的字段可以先空着。
- **Outcome**: adopted; retained the existing publication format and omitted unavailable links rather than inventing metadata

## I-004 · Matching publication format includes the readable full paper
- **Layer**: execution
- **Task**: Completing the five newly added publication pages
- **Model state**: Had added metadata, abstracts, PDFs, and citations but treated the existing full-text HTML as optional
- **Quote**: 论文正文没有转换并加入呀，你可以从 arXiv 下载
- **Outcome**: adopted; convert the complete papers from arXiv sources and the supplied local manuscript into the site's existing HTML format

## I-005 · Final publication acceptance requires visual coverage of every page
- **Layer**: execution
- **Task**: Final audit of the five new publication pages
- **Model state**: Automated checks and selected desktop/mobile previews had passed, but the user requested a stricter final review
- **Quote**: 最后再进行一遍最严格地检查，逐页视检确保没有任何问题
- **Outcome**: adopted; inspected 196 continuous overlapping viewport screenshots through all five papers, then rechecked every repaired formula group, footnotes, figures, algorithms, references, and footers on desktop and mobile alongside independent source and structural audits
