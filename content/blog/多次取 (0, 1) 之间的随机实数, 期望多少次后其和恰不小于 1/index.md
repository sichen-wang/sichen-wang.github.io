---
title: "多次取 (0, 1) 之间的随机实数, 期望多少次后其和恰不小于 1"
date: "2024-08-27 19:42:49"
card_summary: ""
slug: "多次取 (0, 1) 之间的随机实数, 期望多少次后其和恰不小于 1"
aliases:
  - "/blog/duo-ci-qu-0-1-zhi-jian-de-sui-ji-shi-shu-qi-wang-duo-shao-ci-hou-qi-he-qia-bu-xiao-yu-1/"
tags:
  - "Probability"
  - "Expected Value"
  - "Calculus"
categories:
  - "Research"
---

设事件 \(\omega_{n}\) 表示随机取 \(n\) 个 \((0, 1)\) 中的实数, 其和小于 \(1\).

\[
\begin{aligned}
E &= \sum_{n = 1}^{\infty} n P(\omega_{n - 1} \overline{\omega_n}) \\
&= \sum_{n = 1}^{\infty} n \left[ P(\omega_{n - 1}) - P(\omega_{n - 1}\omega_n) \right] \\
&= \sum_{n = 1}^{\infty} n \left[ P(\omega_{n - 1}) - P(\omega_n) \right] \\
&= 1 + \sum_{n = 1}^{\infty} P(\omega_n)
\end{aligned}
\]

考虑根据定义求 \(\omega_{n}\):

\[
\omega_n = \int_{0}^1 \mathrm{d}x_1 \int_{0}^{1 - x_1} \mathrm{d}x_2 \int_{0}^{1 - x_1 -x_2} \mathrm{d}x_3 \cdots \int_{0}^{1 - \sum_{i \lt n} x_i} \mathrm{d}x_n
\]

将 \(1\) 用形式变量 \(x\) 代替, 即得

\[
\omega_n(x) = \int_{0}^x \mathrm{d}x_1 \int_{0}^{x - x_1} \mathrm{d}x_2 \int_{0}^{x - x_1 -x_2} \mathrm{d}x_3 \cdots \int_{0}^{x - \sum_{i \lt n} x_i} \mathrm{d}x_n
\]

考虑寻找 \(\omega_{n + 1}\) 和 \(\omega_{n}\) 之间的关系, 有

\[
\omega_{n + 1}(x) = \int_{0}^{x} \omega_n(x - x_{n + 1}) \mathrm{d}x_{n + 1}
\]

注意到在积分内部, \(\mathrm{d}(x - x_{n + 1})\) 与 \(\mathrm{d}x_{n + 1}\) 实际上是等价的, 于是得到递推式

\[
\omega_{n + 1}(x) = \int_{0}^{x} \omega_n(t) \mathrm{d}t
\]

根据定义 \(\omega_{1}(x) = x\), 于是归纳得

\[
\omega_{n}(x) = \int_{0}^{x} \frac{t^{n - 1}}{(n - 1)!} \mathrm{d}t = \frac{x^n}{n!}
\]

将 \(x\) 换回 \(1\), 回代得

\[
E = 1 + \sum_{n = 1}^{\infty} \frac{1}{n!} = \mathrm{e}
\]
