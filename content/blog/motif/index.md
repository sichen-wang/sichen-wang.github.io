---
title: "Motif"
date: "2025-02-23 20:21:36"
card_summary: ""
tags:
  - "Network Science"
  - "Network Motifs"
categories:
  - "Research"
---

## Definitions

**Motif 标准定义**: Motif 是多次出现在图中的子结构，其出现频率显著高于在随机网络中的频率.

一般而言, k-motif 在 \(k \geqslant 3\) 时才有意义, 于是 3-motif 也成为被研究最多的结构.

另外, 在生成随机网络时需要满足:

- 每个点的入度和出度需要与真实网络中相似. (为了确保子图的数量尽可能一致)
- 在计算 k-motif 时, (k-1)-motif 的出现频率需要与真实网络中相似. (为了确保 k-motif 的出现频率高并不仅仅因为其某个子结构的出现频率高)

而很多时候点是有其自身属性的, 于是可以用若干个标签刻画一个点的属性, 于是有 colored-motif 的定义如下

**带标签 Motif**: colored-motif 是元素取自标签全集 \(\mathbb{C}\) 中的一个可重集.

而在很多情况下, 在图中显著欠表达的子结构也是需要关注的, 于是有 anti-motif 的定义如下

**欠表达 Motif**: anti-motif 是很少出现在图中的子结构，其出现频率显著低于在随机网络中的频率.

**概率阈值 P**: 通过实验可以确定一个阈值, 一个子结构在随机图中出现的频率大于其在原图中出现的频率的概率不大于 \(P\) 则该子结构可能被认为是 motif. 该阈值 \(P\) 可以通过 z-score 来刻画, z-score 被定义为超过平均频率多少个标准差, 形式化的有
\[
\text{z-score}(G_k) = \frac{f_{\text{ori}} - \text{eva}(f_{\text{ran}})}{\sigma(f_{\text{ran}})}
\]

其中 \(f_{\text{ori}}\) 表示原始网络中该 motif 的频率, \(\text{eva}(f_{\text{ran}})\) 表示随机图中该 motif 的平均频率, \(\sigma(f_{\text{ran}})\) 表示随机图中 motif 频率的标准差.

**唯一性阈值 U**: 通过实验可以确定一个阈值, 出现频率超过该阈值 \(U\) 的子结构可能被认为是 motif.

**差异度阈值 D**: 通过实验可以确定一个阈值, 满足 \(f_{\text{ori}} - \text{eva}(f_{\text{ran}}) \gt D \times \text{eva}(f_{\text{ran}})\) 的子结构可能被认为是 motif.

**Motif 参数化定义**: 在图 \(G\) 中, motif 是指由参数集 \(\{P, U, D, N\}\) 限制的导出子图 \(G_{k}\). 其中 \(P, U, D\) 的定义如上所述, \(N\) 为随机图的数量, 一组可供参考的超参数为 \(\{0.01, 4, 0.1, 1000\}\).
