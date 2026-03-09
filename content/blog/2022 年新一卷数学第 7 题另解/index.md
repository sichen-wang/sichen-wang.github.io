---
title: "2022 年新一卷数学第 7 题另解"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "2022 年新一卷数学第 7 题另解"
aliases:
  - "/blog/2022-nian-gao-kao-quan-guo-i-juan-shu-xue-ke-mu-di-qi-ti-de-yi-chong-fei-chang-gui-jie-fa/"
tags:
  - "High School Math"
categories:
  - "Courses"
---

设 \(a = 0.1 e^{0.1}, b = \frac{1}{9}, c = -\ln 0.9\)，试比较 \(a, b, c\) 的大小。

考虑到以下公式：

\[
e ^ {qx} = \sum _ {n} q ^ n \frac{x ^ n}{n!} \tag{7.1}
\]

\[
\ln(1 + x) = \sum _ n (-1) ^ n \frac{x ^ {n + 1}}{n + 1} \tag{7. 2}
\]

将 \(a\) 带入式 \((7. 1)\) 可得：

\[
\begin{aligned}
a &= 0.1(1 + 0.1 + \frac{0.01}{2} + \frac{0.001}{6} + \cdots) \\
  &= 0.1 + 0.01 + \frac{0.001}{2} + \frac{0.0001}{6} + \cdots
 \end{aligned}
\]

将 \(c\) 带入式 \((7.2)\) 可得：

\[
\begin{aligned}
c &= \ln (1 + \frac{1}{9}) \\
  &= \frac{1}{9} - \frac{\frac{1}{9 ^ 2}}{2} + \frac{\frac{1}{9 ^ 3}}{3} - \cdots
\end{aligned}
\]

分解 \(b\) 是简单的：

\[
b = 0.111\cdots = 0.1 + 0.01 + 0.001 + \cdots
\]

此时 \(b \gt a, c\) 应当是一目了然的，于是考虑对比 \(a, c\) 的大小。

取 \(c' = \frac{1}{9} - \frac{1}{2 \times 81} + \frac{1}{3 \times 729} \gt c\)，不够好算，再取 \(c'' = \frac{1}{9} - \frac{1}{400} + \frac{1}{2000} = \frac{1}{9} - 0.002 \gt c'\)。

取 \(a' = 0.1 + 0.01 \lt a\)，易知 \(c'' \lt a'\)，于是 \(c \lt c' \lt c'' \lt a' \lt a\)。

综上，有 \(c \lt a \lt b\)。
