---
title: "The Price of Order in the Logarithmic Method"

authors:
  - me
  - Zhipeng Lu
  - Jingbang Chen

# arXiv v1 提交日期
date: 2026-08-09

# 预印本用 manuscript：它是 Hugo Blox 里表示「未经同行评审的稿件」的类型，
# 与 ICML 那篇的 paper-conference 区分开。
#
# publication_short 是列表页徽章的取值。这里写 Preprint 而不是 arXiv 编号或
# 投稿目标会议：编号在一瞥之下不可读、也没人靠 ID 认论文；写目标会议会被读成
# 已录用。Preprint 直接回答读者唯一在意的问题——过没过同行评审。
# 论文录用后把这里改成会议名（如 SODA 2027），徽章自动跟着变。
publication_types: ["manuscript"]
publication: "*Preprint*, arXiv:2608.06388"
publication_short: "Preprint"

abstract: >-
  The logarithmic method is a classical static-to-dynamic transformation: it
  stores one dynamic ordered set as several immutable static components and
  rebuilds them by merges. The same component-and-merge discipline underlies
  write-optimized ordered indexes, where cheap insertions must be reconciled with
  exact ordered queries. In this paper, we study the insertion-only version after
  n insertions, over abstract keys, in a strongly materialized merge-stack model
  with sequential component merges and one forward scan of the live components per
  query. We bound the product between the total amount of data written during the
  n insertions and the worst-case amount of data read by a single query, known as
  the write-read product. The optimal bounds are Θ(n log² n) for membership and
  local certificates, Θ(n log³ n) for order and range queries with named keys or
  endpoints, and Θ(n²) for select. Thus, the logarithmic method does not impose a
  universal dynamic overhead: under materialized one-way access, the optimum
  depends on what information the query reveals before the scan starts. This
  pinpoints the access-model obstruction behind the extra logarithm for exact
  order and range queries, and the quadratic barrier for select.

tags:
  - Data Structures
  - Lower Bounds
  - Write-Optimized Indexes

# featured 是「代表作」机制，目前站上没有任何地方在用它。等论文攒够再统一启用，
# 现在两篇都标或都不标都没有意义。
featured: false

links:
  - type: preprint
    provider: arxiv
    id: 2608.06388
    label: arXiv
---
