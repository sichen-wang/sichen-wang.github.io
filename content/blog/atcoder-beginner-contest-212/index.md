---
title: "AtCoder Beginner Contest 212"
date: "2023-06-24 11:00:56"
card_summary: ""
tags:
  - "AtCoder"
categories:
  - "CP"
---

## E

考虑记 \(f_{i, u}\) 表示走 \(i\) 步到 \(u\) 的方案数。显然有转移式：

\[
f_{i, u} = \sum _ {(u, v) \in Edge} f_{i - 1, v}
\]

状态数为 \(nk\)，转移的时间复杂度为 \(\Theta(n)\)，于是总时间复杂度为 \(\Theta(n^{2} k).\)

考虑到删除的边数很少，于是将转移方程改写为：

\[
f_{i, u} = \sum _ {v = 1} ^ n f_{i - 1, v} - \sum _ {(u, v) \not\in Edge} f_{i - 1, v}
\]

前一项可以算完每个 \(i\) 以后记录一下，后一项合法转移数量之和为 \(m\)，于是总时间复杂度被优化至 \(\Theta(nk + mk).\)

## F

看到这个题，我们首先想到的肯定是倍增。

但是细想一下可以发现，从一个点 \(i\) 开始跳 \(2^{j}\) 步到的地方还与时间有关，是难以处理的。

我们考虑记 \(f_{i, j}\) 表示从 \(i\) 号**路径**开始，跳 \(2^{j}\) 步到的地方，容易发现此时 \(f_{i, j}\) 的值是唯一的。

于是用 \(\rm set\) 维护出 \(y\) 号点在 \(x\) 时刻开始要走上的路径，然后不断往后跳，直到停在最后一个时间不大于 \(z\) 的位置，判断一下是停在路上还是停在点上即可。

时间复杂度 \(\Theta(n \log n + q \log n).\)

## G

首先考虑到当 \(x = 0\) 时有且仅有 \(y = 0\) 满足条件，于是我们不妨设 \(1 \leqslant x, y \lt P\)，最后再给答案加上 \(1\)。

考虑 \(P\) 的一个原根 \(r\)，设 \(x = r^{a}, y = r^{b}\)，容易发现 \((x, y)\) 与 \((a, b)\) 一一对应，于是有：

\[
x ^ n \equiv y \iff r ^ {an} \equiv r ^ b \pmod P
\]

考虑拓展欧拉定理，可以发现：

\[
r ^ {an} \equiv r ^ b \pmod P \iff an \equiv b \pmod {P - 1}
\]

于是问题被转化为求满足 \(an \equiv b \pmod {P - 1}\) 的 \((a, b)\) 数量。

根据裴蜀定理，可以推导出：

\[
\sum _ {a = 1} ^ {P - 1} \sum _ {b = 1} ^ {P - 1} [an \equiv b \pmod {P - 1}] = \sum _ {a = 1} ^ {P - 1} \frac{P - 1}{(P - 1, a)}
\]

考虑对 \((P - 1, a)\) 相等的 \(a\) 一起计算。设 \(f(g)\) 表示满足 \(g = (P - 1, a)\) 的 \(a\) 的数量。可以发现 \(g \mid P - 1\) 且 \(f(g) = \varphi\left(\frac{P - 1}{g}\right)\)。

考虑求解 \(\varphi(n)\)，观察到 \(\varphi \times I = id\)，于是有：

\[
\varphi(n) = n - \sum _ {d \mid n,\ d \not= n} \varphi(d)
\]

进一步有：

\[
f(g) = \frac{P - 1}{g} - \sum _ {g \mid k,\ g \not= k} f(g)
\]

从大到小枚举 \(g\)，枚举其倍数转移一下即可，时间复杂度 \(\Theta(\sqrt{P} + d^{2}(P - 1))\)。

## H

考虑记 \(w + 1\) 为第一个大于所有 \(a_{i}\) 的 \(2\) 的幂，\(S\) 为 \(a\) 序列中数构成的集合。

造一个集合幂级数 \(F(x) = \sum_{i = 0}^{w} [i \in S]x^{i}\)，容易发现答案即为：

\[
\sum _ {i = 1} ^ n \left(k ^ i - [x ^ 0] F^i(x) \right)
\]

利用 \(\rm FWT\) 的线性性推一推式子：

\[
\begin{aligned}
&~~~~~\sum _ {i = 1} ^ n \left(k ^ i - [x ^ 0] F^i(x) \right) \\
&=\sum _ {i = 1} ^ n \left( k ^ i - [x ^ 0] \textrm{IFWT}(\textrm{FWT}\cdot F^i (x)) \right) \\
&=\sum _ {i = 1} ^ n k ^ i - [x ^ 0] \textrm{IFWT}\left( \sum _ {i = 1} ^ n \textrm{FWT} \cdot F^i(x)\right)
\end{aligned}
\]

\(\rm FWT\) 后 \(F\) 的幂表示对每一项系数做点乘。

设 \(G(x) = \textrm{FWT} \cdot F(x)\)，用一下等比数列求和公式，则有答案为：

\[
\sum _ {i = 1} ^ n k ^ i - [x ^ 0] \textrm{IFWT}\left[ \sum _ {i = 0} ^ w \left( \frac{g_i ^ {n + 1} - g_i}{g_i - 1} \right)x ^ i \right]
\]

计算上式所需时间复杂度为 \(\Theta((n + w) \log (n + w)).\)

[Code Link](https://atcoder.jp/contests/abc212/submissions?f.Task=&f.LanguageName=C%2B%2B&f.Status=AC&f.User=WA_on_test_233)
