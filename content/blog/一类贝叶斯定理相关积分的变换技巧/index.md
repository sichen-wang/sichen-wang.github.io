---
title: "一类贝叶斯定理相关积分的变换技巧"
date: "2024-04-09 16:43:16"
card_summary: ""
slug: "一类贝叶斯定理相关积分的变换技巧"
aliases:
  - "/blog/yi-lei-bei-xie-si-ding-li-xiang-guan-ji-fen-de-bian-huan-ji-qiao/"
tags:
  - "Probability"
  - "Calculus"
  - "Bayesian Inference"
categories:
  - "Research"
---

考虑非负实数域上某可用条件概率刻画的期望：

\[
E(x) = \int_{0}^{+\infty} xP(t = x|q) \mathrm{d}x
\]

其中 \(q\) 为已知，且 \(P(q|t = x)\) 是可用初等函数刻画的，于是：

考虑贝叶斯定理：

\[
E(x) = \int_{0}^{+\infty} x\frac{P(q|t = x)P(t = x)}{P(q)} \mathrm{d}x
\]

观察发现对 \(x\) 微分本质上就是在枚举每个 \(t = x\) 的情况，于是 \(P(t = x)\) 已经被 \(\mathrm{d}x\) 包含，可以看作 \(1\)，故

\[
E(x) = \int_{0}^{+\infty} x\frac{P(q|t = x)}{P(q)} \mathrm{d}x
\]

大多数情况下，哪怕 \(P(q)\) 可以用初等函数刻画，整个式子也会难以化简，于是考虑拆 \(P(q)\)：

\[
E(x) = \int_{0}^{+\infty} x\frac{P(q|t = x)}{\int_{0}^{+\infty} P(q|t = y) \mathrm{d}y } \mathrm{d}x
\]

整理可得

\[
E(x) = \frac{\int_{0}^{+\infty} xP(q|t = x) \mathrm{d}x}{\int_{0}^{+\infty} P(q|t = x) \mathrm{d}x }
\]

设 \(P(q|t = x) = f(x)\)，其中 \(f(x)\) 是初等函数，又设 \(\delta\) 为积分算子（即 \([\delta f(x)]' = f(x)\) ），即得

\[
E(x) = \frac{\int_{0}^{+\infty} xf(x) \mathrm{d}x}{\int_{0}^{+\infty} f(x) \mathrm{d}x } = \lim_{\varepsilon \to 0^+}^{m \to +\infty}\frac{\delta mf(m) - \delta \varepsilon f(\varepsilon)}{\delta f(m) - \delta f(\varepsilon)}
\]
