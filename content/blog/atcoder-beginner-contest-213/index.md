---
title: "AtCoder Beginner Contest 213"
date: "2023-06-24 11:00:56"
card_summary: ""
tags:
  - "AtCoder"
categories:
  - "CP"
---

## E

考虑使用 \(\rm bfs\)。

观察到每一步的代价都是 \(0\) 或 \(1\)，于是建立双端队列。每次迭代取队头，如果走了代价为 \(0\) 的边就将出点加入队首，否则加入队尾。

考虑其正确性，因为走代价为 \(0\) 的边不会增加当前点的答案，所以可以维护住当前取出的点一定是答案最小点的性质。

时间复杂度 \(\Theta(nm)\)。

另外，这种模型还可拓展到代价为 \(0 \sim k\)，只需要对每种贡献维护一个队列即可，容易发现仍然满足单调性。时间复杂度 \(\Theta(nk)\)。

## G

考虑使用状压 \(\rm DP\)。

设 \(f_{S}\) 表示仅考虑 \(S\) 的导出子图，令它与 \(1\) 连通的方案数。设 \(cnt_{S}\) 表示 \(S\) 导出子图中的边数，显然有：

\[
ans_k = \sum _ {1, k \in S} f_S \times 2 ^ {cnt_{U-S}}
\]

考虑容斥求解 \(f_{S}\)，有：

\[
f_S = 2 ^ {cnt_S} - \sum _ {1 \in T, T \subsetneq S} f_T \times 2 ^ {cnt_{S - T}}
\]

求解两部分的时间复杂度分别为 \(\Theta(n^{2} 2^{n})\) 和 \(\Theta(3^{n})\)。

另外，后半部分可以使用 \(\rm FWT\) 优化或卷积做到 \(\Theta(n^{2} 2^{n})\)。

## H

考虑 \(\rm DP\)。设 \(f_{i, j}\) 表示到 \(i\) 为止经过长度为 \(j\) 的路径的方案数，记 \(E_{u, v, w}\) 表示从 \(u\) 到 \(v\) 长度为 \(w\) 的路径数量。显然有转移方程：

\[
f_{i, j} = \sum _ {k = 1} ^ n \sum _ {l = 1} ^ T f_{k, j - l} \times E_{k, i, l}
\]

考虑用 \(\rm GF\) 拟合这个过程，设 \(F_{i}(x) = \sum \limits_{j} f_{i, j} x^{j}\)，\(G_{i, j}(x) = \sum \limits_{k \geqslant 1} E_{i, j, k} x^{k}.\) 有方程：

\[
F_i(x) = \sum _ {j = 1} ^ n F_j(x) \times G_{j, i}(x)
\]

使用分治多项式乘法即可，时间复杂度 \(\Theta(n^{2} T \log^{2} T)\)。

[Code Link](https://atcoder.jp/contests/abc213/submissions?f.Task=&f.LanguageName=C%2B%2B&f.Status=AC&f.User=WA_on_test_233)
