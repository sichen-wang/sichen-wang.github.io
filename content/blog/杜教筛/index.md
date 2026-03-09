---
title: "杜教筛"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "杜教筛"
aliases:
  - "/blog/du-jiao-shai/"
tags:
  - "Number Theory"
  - "Multiplicative Functions"
categories:
  - "CP"
---

杜教筛被用来求积性函数的前缀和。

设有积性函数 \(f(x)\)，其前缀和为 \(S(n) = \sum \limits_{i = 1}^{n} f(i)\)。

考虑构造 \(h(x)\) 和 \(g(x)\)，满足 \(h = f \times g\)。

推一下式子 ：

\[
\begin{aligned}
    \sum _ {i = 1} ^ n h(i) &= \sum _ {i = 1} ^ n \sum _ {d | i} g(d) \times f\left(\frac{i}{d}\right) \\
    &= \sum _ {d = 1} ^ n g(d) \sum _ {i = 1} ^ {\left\lfloor\frac{n}{d}\right\rfloor} f(i) \\
    &= \sum _ {d = 1} ^ n g(d) S\left(\left\lfloor\frac{n}{d}\right\rfloor\right)
\end{aligned}
\]

众所周知有数论分块。

具体来说，观察到式子右边的 \(S\left(\left\lfloor\frac{n}{d}\right\rfloor\right)\) 最多有 \(2\sqrt{n}\) 种取值。证明考虑 \(\sum \limits_{d = 1}^{\sqrt{n}} \left\lfloor\frac{n}{d}\right\rfloor\) 显然最多有 \(\sqrt{n}\) 种取值，\(\forall d \gt \sqrt{n},\left\lfloor\frac{n}{d}\right\rfloor \lt \sqrt{n}\)，故 \(\sum \limits_{d = \sqrt{n} + 1}^{n} \left\lfloor\frac{n}{d}\right\rfloor\) 也最多有 \(\sqrt{n}\) 种取值。

于是这时候只需要考虑对于一个数 \(i\)，满足 \(\left\lfloor\frac{n}{i}\right\rfloor = \left\lfloor\frac{n}{j}\right\rfloor\) 的最大的 \(j\) 是多少。

设 \(k = \left\lfloor\frac{n}{i}\right\rfloor\)，则有 \(\left\lfloor\frac{n}{j}\right\rfloor = k\)，将向下取整去掉，有 \(k \leqslant \frac{n}{j} \lt k + 1\)，取倒数，得到 \(\frac{1}{k + 1} \lt \frac{j}{n} \leqslant \frac{1}{k}\)，全部乘上 \(n\) 得到 \(\frac{n}{k + 1} \lt j \leqslant \frac{n}{k}\)，又因为 \(j\) 为整数，所以 \(j_{\max} = \left\lfloor\frac{n}{k}\right\rfloor = \left\lfloor\frac{n}{\left\lfloor\frac{n}{i}\right\rfloor}\right\rfloor\)。

言归正传，求解杜教筛最终式子时可以直接递归，中间需要记忆化一下，但其实不需要用到 \(\rm map\) 系列 \(\rm STL\)，因为可以证明需要求解的 \(S(x)\) 中 \(x \in \{\left\lfloor\frac{n}{d}\right\rfloor{}|d \in [1, n]\}\)。

稍加思考就可以发现，上式的一个充分条件为 \(\left\lfloor\frac{\left\lfloor\frac{n}{i}\right\rfloor}{j}\right\rfloor = \left\lfloor\frac{n}{ij}\right\rfloor\)，考虑其证明：\(\forall x \in Z\)，若有 \(x \leqslant \left\lfloor\frac{\left\lfloor\frac{n}{i}\right\rfloor}{j}\right\rfloor\)，那么有 \(xj \leqslant \left\lfloor\frac{n}{i}\right\rfloor\)，进一步有 \(xij \leqslant n\)，再将 \(ij\) 放回去有 \(x \leqslant \left\lfloor\frac{n}{ij}\right\rfloor\)，原式得证。

故我们只需要将 \(\left\lfloor\frac{n}{d}\right\rfloor\ (d \in [1, n] \cap Z)\) 的所有取值映射到一个数组上就可以直接记忆化了。

考虑复杂度证明，记忆化以后每个 \(S(x)\) 只需要算一次，而算一次 \(S(x)\) 的时间复杂度为 \(\Theta(\sqrt{x})\)。 故总时间复杂度为 \(\sum\limits_{x} \sqrt{x}\ (x \in \{\left\lfloor\frac{n}{d}\right\rfloor|d \in [1, n] \cap Z\})\)。 对于不大于 \(\sqrt{n}\) 的 \(d\)，其贡献的复杂度上界为 \(\sum \limits_{i = 1}^{\sqrt{n}} \Theta\left(\sqrt{\frac{n}{i}}\right)\)，而对于大于 \(\sqrt{n}\) 的 \(d\)，\(\left\lfloor\frac{n}{d}\right\rfloor\) 的取值不大于 \(\sqrt{n}\)，所以其贡献的上界为 \(\sum \limits_{i = 1}^{\sqrt{n}} \Theta(\sqrt{i})\)，其和为 \(T(n) = \sum \limits_{i = 1}^{\sqrt{n}} \Theta\left(\sqrt{\frac{n}{i}}\right) + \sum \limits_{i = 1}^{\sqrt{n}} \Theta(\sqrt{i})\)，积分求个近似可以得到 \(T(n) \approx \int_{1}^{\sqrt{n}} \Theta\left(\sqrt{\frac{n}{x}}\right) dx + \int_{1}^{\sqrt{n}} \Theta(\sqrt{x}) dx = \Theta(n^{\frac{3}{4}})\)。

事实上还可以做到更优，线性预处理 \(f\) 的前 \(m\) 项，易知复杂度变成了 \(\Theta(m) + \Theta\left(\sum \limits_{i = 1}^{\frac{n}{m}} \sqrt{\frac{n}{i}}\right)\)，跟之前一样积分近似一下可以得到复杂度即为 \(\Theta(m + nm^{-\frac{1}{2}})\)，易知其下界为 \(\Theta(n^{\frac{2}{3}})\)。

---

在此列举一些常见的构造（其证明需要用到迪利克雷生成函数，略过）：

- \((id^{k} \cdot \mu) \times id^{k} = \varepsilon\)
- \((id^{k} \cdot \varphi) \times id^{k} = id^{k + 1}\)
- \((id^{k} \cdot \sigma_{k}) \times (id^{k} \cdot \mu) = id^{2k}\)
