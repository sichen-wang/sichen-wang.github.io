---
title: "复杂度分析"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "复杂度分析"
aliases:
  - "/blog/fu-za-du-fen-xi/"
tags:
  - "Complexity Analysis"
  - "Recurrence Relations"
categories:
  - "CP"
---

## 主定理

主定理 \(\rm(Master\ Theorem)\) 被用来求解一类递归算法的时间复杂度，假设有递推式形如:

\[
T(n) = aT\left(\frac{n}{b}\right) + f(n)
\]

上式的含义是，存在一个规模为 \(n\) 的问题可以被划分成 \(a\) 个规模为 \(\frac{n}{b}\) 的问题，且将它们合并的运算复杂度为 \(f(n)\)。

那么根据主定理，有 ：

\[
T(n) =
\begin{cases}
\Theta\left(n^{\log _{b} a}\right) & f(n)=O\left(n^{\log _{b} a-\epsilon}\right) \\
\Theta(f(n)) & f(n)=\Omega\left(n^{\log _{b} a+\epsilon}\right) \\
\Theta\left(n^{\log _{b} a} \log ^{k+1} n\right) & f(n)=\Theta\left(n^{\log _{b} a} \log ^{k} n\right), k \geq 0
\end{cases}
\]
