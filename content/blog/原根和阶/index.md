---
title: "原根和阶"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "原根和阶"
aliases:
  - "/blog/yuan-gen-he-jie/"
tags:
  - "Number Theory"
  - "Primitive Root"
  - "Multiplicative Order"
categories:
  - "CP"
---

## 阶的定义及求法

称使得 \(a^{t}\equiv 1\pmod p\) 成立的最小正整数 \(t_{min}\) 为 \(a\) 对模数 \(p\) 的阶，记为 \(\delta_{p}(a)\)。

有如下定理 ：\(\delta_{p}(a) \mid n\Longleftrightarrow a^{n}\equiv 1\pmod p\)。

又有 \(a^{\varphi(p)}\equiv 1\pmod p\Longrightarrow \delta_{p}(a) \mid \varphi(p)\) 可得一个 \(\Theta(\sqrt{p}+\log^{2p})\) 求阶的算法：

首先将 \(\varphi(p)\) 分解成 \(\varphi(p)=k_{1}^{q_{1}}\times k_{2}^{q_{2}}\times \cdots \times k_{r}^{q_{r}}\) 的形式，令 \(\delta_{p}(a)=\varphi(p)\)，然后试着用每一个质因子去除 \(\delta_{p}(a)\)，如果除了之后 \(a^{\frac{\delta_{p}(a)}{k_{i}}}\equiv 1\pmod p\) 那么 \(\frac{\delta_{p}(a)}{k_{i}}\) 就作为新的阶，直到不能再除，此时的 \(\delta_{p}(a)\) 就为 \(a\) 在模 \(p\) 意义下真正的阶。

## 原根的定义及求法

原根 \(g\) 是使得 \(g^{1\sim p-1}\) 在模 \(p\) 意义下的值与 \([1,p-1]\) 形成一一对应关系的值。

有如下定理 ：\(g\) 为 \(p\) 的原根当且仅当 \(\delta_{p}(g)=\varphi(p)\)。

于是可以导出一个计算 \(g_{min}\) 的算法，从小到大枚举 \(g\)，若 \(\delta_{p}(g)=\varphi(p)\)，则 \(g\) 为 \(p\) 的最小原根。

有如下定理 ：\(g_{min}\lt p^{\frac{1}{4}}\)。

所以以上算法时间复杂度为 \(\Theta(\sqrt{p}+p^{\frac{1}{4}}\omega(p))\)。
