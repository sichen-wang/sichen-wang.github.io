---
title: "生成函数强化训练"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "生成函数强化训练"
aliases:
  - "/blog/sheng-cheng-han-shu-qiang-hua-xun-lian/"
tags:
  - "Generating Functions"
  - "Combinatorics"
categories:
  - "CP"
---

# [[集训队作业2013] 城市规划](https://www.luogu.com.cn/problem/P4841)

考虑 \(\rm EGF\) 的组合意义，可以发现若设任意图方案数的 \(\rm EGF\) 为 \(F(x)\)，连通图的 \(\rm EGF\) 为 \(G(x)\)，显然任意图计数可以被看做先将 \(n\) 个点分进若干个非空子集，然后做连通图计数的方案数，那么根据之前的结论，有 ：

<div>
\[
F(x) = \exp G(x) \iff G(x) = \ln F(x)
\]
</div>

显然有 \(F(x) = \sum_{n} 2^{\binom{n}{2}} x^{n}\)，于是只需直接对其求 \(\ln\) 即可。

时间复杂度 \(\Theta(n \log n).\)

## [Code Link](https://paste.ubuntu.com/p/xmQf5fsg9w/)

# [[CF438E] The Child and Binary Tree](http://codeforces.com/problemset/problem/438/E)

首先可以考虑一个 \(\rm DP\)，设 \(f_{S}\) 表示点权之和为 \(S\) 的二叉树数量，迭代时可以考虑枚举左子树的权值和 \(S_{l}\)，右子树的权值和 \(S_{r}\) 和根节点的权值 \(w\)，那么有 \(f_{S_{l} + S_{r} + w} = \sum_{S_{l}} \sum_{S_{r}} \sum_{w \in C} f_{S_{l}} f_{S_{r}}.\)

容易发现，这个式子可以用三个多项式的卷积来拟合，设 \(F(x) = \sum_{n} f_{n} x^{n}, G(x) = \sum_{n} [n \in C] x^{n}\)，于是有 ：

<div>
\[
F = F ^ 2 G + 1
\]
</div>

最后的 \(+1\) 是为了补齐常数项，因为 \(f_{0}\) 为 \(1.\)

解方程可以得到 ：

<div>
\[
F = \frac{1 \pm \sqrt{1 - 4G}}{2G}
\]
</div>

由于有两个解，显然不可能都成立，于是考虑 \(x \to 0\) 时的特殊情况。

当 \(x \to 0\) 时，\(F(x) \to 1,G(x) \to 0.\)

<div>
\[
\lim _ {x \to 0} \frac{1 + \sqrt{1 - 4G}}{2G} = +\infty \not= \lim _ {x \to 0} F
\]
</div>

<div>
\[
\lim _ {x \to 0} \frac{1 - \sqrt{1 - 4G}}{2G} = 1 = \lim _ {x \to 0} F
\]
</div>

于是选取 \(F= \frac{1 - \sqrt{1 - 4G}}{2G}\) 作为方程的解。

到这一步，我们发现一个问题，因为 \(G(x)\) 的常数项为 \(0\)，所以 \(G(x)\) 不可以求逆。

考虑对解做变换，这里选取分子有理化 ：

<div>
\[
F = \frac{\left(1 - \sqrt{1 - 4G}\right)\left(1 + \sqrt{1 - 4G}\right)}{2G\left(1 + \sqrt{1 - 4G}\right)} = \frac{2}{1 + \sqrt{1 - 4G}}
\]
</div>

可以发现分母的常数项必定不为 \(0\)，于是做多项式开方和多项式求逆即可。

时间复杂度 \(\Theta(n \log n).\)

## [Code Link](https://paste.ubuntu.com/p/YxyyhWmFh9/)

# [[国家集训队] 整数的 lqp 拆分](https://www.luogu.com.cn/problem/P4451)

设 \(\{f_{n}\},\{g_{n}\}\) 分别为斐波那契数列和答案序列，\(F(x)\) 和 \(G(x)\) 分别为它们的生成函数。

显然有斐波那契数列的生成函数 ：

<div>
\[
F(x) = \frac{x}{1 - x - x ^ 2}
\]
</div>

而对于 \(G(x)\)，可以发现如果 \(g_{i}\) 已经被求出来了，那么给所有的拆分加上一个数 \(n - i\) 即可得到 \(g_{n}\) 的所有拆分，\(g_{i}\) 对 \(g_{n}\) 的贡献为 \(g_{i} \times f_{n - i}.\) 于是有 \(g_{n}\) 的递推式 ：

<div>
\[
g_n = \sum _ {i = 0} ^ {n- 1} g_i \times f_{n - i}
\]
</div>

将 \(\{g_{n}\}\) 带入 \(G(x)\) 可得 ：

<div>
\[
G(x) = \sum _ n x ^ n \sum _ {i = 0} ^ {n - 1} g_i f_{n - i}
\]
</div>

可以发现等式右边实际上是卷积的形式，于是有 ：

<div>
\[
G = GF
\]
</div>

但是我们发现这样的话 \(G(x) = 0\)，原因是 \(g_{0} = 0\)，于是我们强制 \(g_{0} = 1\)，得到 ：

<div>
\[
G = GF + 1
\]
</div>

<div>
\[
G(x) = \frac{1}{1 - F(x)} = 1 + \frac{x}{1 - 2x - x ^ 2}
\]
</div>

可以发现现在求出的 \(G(x)\) 比实际值多了 \(1\)，因为我们将 \(g_{0} = 0\) 强制变成了 \(g_{0} = 1\)，修正后有 ：

<div>
\[
G(x) = \frac{x}{1 - 2x - x ^ 2} = \frac{\frac{\sqrt{2}}{4}}{1 - (1 + \sqrt{2})x} + \frac{-\frac{\sqrt{2}}{4}}{1 - (1 - \sqrt{2})x}
\]
</div>

<div>
\[
[x ^ n]G(x) = \frac{\sqrt{2}}{4}(1 + \sqrt{2}) ^ n - \frac{\sqrt{2}}{4}(1 - \sqrt{2}) ^ n
\]
</div>

最后求出 \(\sqrt{2}\) 在模 \(10^{9} + 7\) 意义下的二次剩余，并且用拓展欧拉定理即可计算出答案。

时间复杂度 \(\Theta(\log n).\)

## [Code Link](https://paste.ubuntu.com/p/4DCfYMF5tH/)

# [[HAOI2018] 染色](https://www.luogu.com.cn/problem/P4491)

首先考虑二项式反演 ：

设 \(f_{i}\) 表示恰好有 \(i\) 个数的数量为 \(S\) 的方案数，\(g_{i}\) 表示钦点 \(i\) 个数的数量为 \(S\) 的方案数，显然有 ：

<div>
\[
g_k = \dbinom{m}{k} \times \frac{n ^ {\underline{kS}}}{(S!) ^ k} \times (m - k) ^ {n - kS}
\]
</div>

<div>
\[
g_k = \sum_{i = k} ^ m \dbinom{i}{k} f_i \iff f_k = \sum _ {i = k} ^ m (-1) ^ {i - k} \dbinom{i}{k} g_i
\]
</div>

<div>
\[
Ans = \sum _ {i = 0} ^ m w_if_i
\]
</div>

于是我们考虑如何对于每个 \(i \in [0, m]\) 求出 \(f_{i}\)，这里有个技巧 ：

<div>
\[
\begin{aligned}
    f_k &= \sum _ {i = k} ^ m (-1) ^ {i - k} \frac{i!}{k!(i - k)!} g_i\\
    &= k! \sum _ {i = k} ^ m i! g_i \times \frac{(-1) ^ {i - k}}{(i - k)!}
\end{aligned}
\]
</div>

容易发现上式可以用差值卷积计算，时间复杂度 \(\Theta(n \log n).\)

# [付公主的背包](https://www.luogu.com.cn/problem/P4389)

容易发现若设每种大小的物品的数量为 \(f_{i}\)，那么答案的生成函数为 ：

<div>
\[
\prod _ i \left (\sum _ j x ^ {ji}\right) ^ {f _ i} = \prod _ i \left(\frac{1}{1 - x ^ i}\right) ^ {f _ i}
\]
</div>

可以直接使用欧拉变换的求解方式。

时间复杂度 \(\Theta(n \log n).\)

# [无标号无根树计数](https://www.luogu.com.cn/problem/P5900)

考虑设 \(f_{n}\) 表示大小为 \(n\) 的无标号有根树的方案数，\(F(x)\) 为数列 \(f\) 的生成函数。

可以发现，如果将一颗大小为 \(n\) 的无标号有根树的根去除，那么剩下的子树是一个个相同的子问题，只要子树大小的和为 \(n - 1\)，再加上根结点就可以唯一确定地拼出一颗无标号有根树。于是有生成函数方程 ：

<div>
\[
F(x) = x \cdot \varepsilon \circ F(x)
\]
</div>

求解这个生成函数方程有两种方法，第一种是直接化简，分治多项式乘法求解 ：

<div>
\[
F(x) = x \prod _ i (1 - x ^ i) ^ {-f_i}
\]
</div>

考虑对两边取 \(\ln\)，将连乘转连加 ：

<div>
\[
\ln F(x) = \ln x - \sum _ i f_i \ln (1 - x ^ i)
\]
</div>

对数不好处理，考虑求导 ：

<div>
\[
\frac{F'(x)}{F(x)} = \frac{1}{x} + \sum _ i if_i \times \frac{x ^ {i - 1}}{1 - x ^ i}
\]
</div>

将两边同时乘以 \(xF(x)\) ：

<div>
\[
xF'(x) = F(x) + F(x) \sum _ i if_i \frac{x ^ i}{1 - x ^ i}
\]
</div>

考虑将右半部分还原成 \(F(x)\) 表示 ：

<div>
\[
xF'(x) = F(x) + F(x)\left(\sum _ {i \geqslant 1} x ^ i F'(x ^ i)\right)
\]
</div>

设 \(G(x) = \sum_{k} x^{k} F'(x^{k})\)，简单推一推 ：

<div>
\[
G(x) = \sum _ k x ^ k \sum _ {i\geqslant 1} if _ i \left(x ^ {k}\right) ^ {i - 1} = \sum _ k \sum _ i i f _ i x ^ {ik} = \sum _ n x ^ n \sum _ {d | n} d f _ d
\]
</div>

故 \(g_{n} = \sum_{d | n} df_{d},g_{1} = f_{1} = 1.\)

因此 ：

<div>
\[
f_n = \frac{1}{n - 1} \sum _ {k = 1} ^ {n - 1} f _ k g _ {n - k}
\]
</div>

\(f\) 使用分治多项式乘法求解，\(g\) 暴力求解即可做到 \(\Theta(n \log^{2} n).\)

另一种方法是使用牛顿迭代 ：

显然我们要求解方程 \(G \circ F(x) = F(x) - x \cdot \varepsilon \circ F(x) = 0\).

假设当前已经求出了方程在模 \(x^{n}\) 意义下的解 \(F_{0}(x)\)，设方程在模 \(x^{2n}\) 意义下的解为 \(F(x)\)，众所周知有 ：

<div>
\[
F(x) = F_0(x) - \frac{G \circ F_0(x)}{G' \circ F_0(x)}
\]
</div>

我们知道，\(\varepsilon \circ F(x)\) 可以在 \(\Theta(n \log n)\) 的时间复杂度内求出，\(F'(x)\) 可以 \(\Theta(n)\) 求，所以可以在 \(\Theta(n \log n)\) 的时间复杂度内求下式 ：

<div>
\[
F(x) = F_0(x) - \frac{F_0(x)  - x \cdot \varepsilon \circ F_0(x)}{[F_0(x)  - x \cdot \varepsilon \circ F_0(x)]'}
\]
</div>

用上式迭代即可算出 \(F(x)\)，时间复杂度 \(\Theta(n \log n).\)

现在我们已经求出了无标号有根树的方案数，考虑将无标号无根树的方案数容斥出来。

考虑钦点无标号无根树的根是它的重心，于是只需要去掉根不是重心的无标号有根树的方案数可以了，分类讨论 ：

如果重心唯一，那么一定存在一颗子树的大小大于 \(\left\lfloor\frac{n}{2}\right\rfloor\)，考虑枚举它的大小 \(i\)，容易发现这颗子树的方案数和将它切除后树的方案数都是无标号有根树计数问题，其答案我们已经算出，于是总方案数需要减去 \(\sum_{i = \left\lfloor\frac{n}{2}\right\rfloor + 1}^{n - 1} f_{i} \times f_{n - i}.\)

如果重心不唯一，那么一棵树还会在两个重心上分别被计算，这种方案只会在 \(n\) 为偶数的情况下出现。考虑到这两个重心一定相连，于是将它们之间的连边断开后形成的两个子树的方案数是独立的。但是我们发现，当两颗子树完全相同时，分别以它的两个重心为根时形成的有根树是同构的，所以我们还是只会将它计算一次，故算重的方案中不包括两颗子树相同的情况，于是总方案数还需要减去 \(\binom{f_{\frac{n}{2}}}{2}.\)

综上，问题得到解决，时间复杂度为 \(\Theta(n \log^{2} n)\) 或 \(\Theta(n \log n).\)

# [[CEOI2004] Sweets](https://www.luogu.com.cn/problem/P6078)

考虑构造 \(F_{i}(x) = \sum_{j = 0}^{m_{i}} x^{j}\)，容易发现题目要求的就是 \(\prod_{i = 1}^{n} F_{i}(x)\) 的系数前缀和。

于是再构造 \(F_{0}(x) = \sum_{i} x^{i}\)，将它和原本的 \(n\) 个幂级数卷在一起，现在考虑求 \(F(x) = \prod_{i = 0}^{n} F_{i}(x)\) 的第 \(L\) 项系数。

容易发现有 ：

<div>
\[
F(x) = \frac{(1 - x ^ {m_1 + 1})(1 - x ^ {m_2 + 1})\cdots(1 - x ^ {m_n + 1})}{(1 - x) ^ {n + 1}}
\]
</div>

观察到 \(n\) 很小，考虑暴力将分子拆开，于是分式变成了 \(2^{n}\) 个形如 \(\frac{x^{k}}{(1 - x)^{n + 1}}\) 的部分之和。

容易发现 ：

<div>
\[
[x ^ L]\frac{x ^ k}{(1 - x) ^ {n + 1}} = \dbinom{n + L - k}{n}
\]
</div>

于是只需要求 \(2^{n + 1}\) 次形如 \(\binom{t}{n}\) 的组合数即可。

到这里我们又发现模数 \(p\) 不是质数，于是考虑将式子变形 ：

<div>
\[
\dbinom{t}{n}~\bmod~p = \frac{t^{\underline{n}}}{n!}~\bmod~p = \frac{t ^ {\underline{n}}~\bmod~n!\cdot p}{n!}~\bmod~p
\]
</div>

于是这样就可以 \(\Theta(n)\) 求解组合数了，总时间复杂度 \(\Theta(2^{n} n).\)

# [[51nod1728] 不动点](https://www.51nod.com/Challenge/Problem.html#problemId=1728)

简化题意 ：求有多少个从 \(\{1,2,\cdots,n\}\) 到 \(\{1,2,\cdots,n\}\) 的映射 \(f\)，满足 ：

<div>
\[
\underbrace{f \circ f \circ \cdots \circ f}_{k}=\underbrace{f \circ f \circ \cdots \circ f}_{k-1}
\]
</div>

保证 \(nk \leqslant 2 \times 10^{6},1\leqslant k \leqslant 3.\)

可以发现这题本质上就是在求深度不超过 \(k\)，环大小为 \(1\) 的基环内向树森林的数量，进一步发现其等价于树高不超过 \(k\) 的有标号有根树森林的数量。

考虑设树高不超过 \(k\) 的有标号有根树数量的 \(\rm EGF\) 为 \(\hat{F}_{k}(x).\) 计算考虑递推，深度不超过 \(k\) 的树可以看作若干棵深度不超过 \(k - 1\) 的树全部接在一个点上，于是有 ：

<div>
\[
\hat{F}_k(x) = x\cdot \exp \hat{F}_{k - 1}(x)
\]
</div>

考虑到需要求的是森林的数量，于是答案的指数型生成函数为 \(\exp \hat{F}_{k}(x).\)

时间复杂度 \(\Theta(kn\log n).\)

# [[CF891E] Lust](https://codeforces.com/contest/891/problem/E)

考虑一次对 \(x\) 的操作造成的影响，他会使 \(a_{x}\) 减少 \(1\)，答案增加 \(\prod_{i \not= x} a_{i}\)，\(\prod_{i} a_{i}\) 减少 \(\prod_{i \not= x} a_{i}.\)

于是我们可以发现，一次操作对答案的贡献等于 \(\prod_{i} a_{i}\) 的变化量。进一步的，最终答案等于 \(k\) 次操作进行完后 \(\prod_{i} a_{i}\) 的变化量。假设第 \(a_{i}\) 被操作了 \(b_{i}\) 次，那么答案为 \(\prod_{i} a_{i} - \prod_{i} (a_{i} - b_{i}).\)

考虑计算所有情况下 \(\prod_{i} (a_{i} - b_{i})\) 的和，最后再将答案除以 \(n^{k}.\)

假设有两个集合 \(S,T,S \cap T = \varnothing\)，\(f_{i}\) 表示 \(\sum b_{k} = i,k\in S\) 对答案的贡献，\(g_{i}\) 表示 \(\sum b_{k} = i,k\in T\) 对答案的贡献，\(h_{i}\) 表示 \(\sum b_{k} = i,k\in S \cup T\) 对答案的贡献，那么显然有 ：

<div>
\[
g_n = \sum _ {i = 0} ^ n \dbinom{n}{i} f_i \times g_{n - i}
\]
</div>

因为 \(f_{i}\) 和 \(g_{n - i}\) 联合起来的贡献是它们的乘积，并且由于操作有序，所以将 \(n\) 次操作分配到它们还导致要乘上 \(\binom{n}{i}\) 的方案数。

很明显，这个式子可以用 \(\rm EGF\) 来拟合，设 \(\hat{F}_{i}(x) = \sum_{j} (a_{i} - j) \frac{x^{j}}{j!}\)，那么答案的生成函数为 ：

<div>
\[
\begin{aligned}
    \hat{F}(x) &= \prod _ i F_i(x)\\
    &= \prod _ i \left( \sum _ j (a_i - j) \frac{x ^ j}{j!} \right)\\
    &= \prod _ i \left( a_i \sum _ j \frac{x ^ j}{j!} - \sum _ {j} \frac{x ^ {j + 1}}{j!} \right)\\
    &= \prod _ i (a_i - x)e ^ x\\
    &= e ^ {nx} \prod _ i (a_i - x)
\end{aligned}
\]
</div>

\(\prod_{i} (a_{i} - x)\) 直接分治乘可以做到 \(\Theta(n \log^{2} n)\)，\(e^{nx}\) 的系数可以直接求，由于 \(\prod_{i} (a_{i} - x)\) 的最高次数为 \(n\)，所以直接枚举计算即可。

总时间复杂度 \(\Theta(n \log^{2} n).\)
