---
title: "生成函数"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "生成函数"
aliases:
  - "/blog/sheng-cheng-han-shu/"
tags:
  - "Combinatorics"
  - "Generating Functions"
categories:
  - "CP"
---

## 普通生成函数

序列 \(a\) 的普通生成函数 \(\rm(Ordinary\ Generating\ Function,OGF)\) 被定义为形式幂级数 ：

\[
F(x) = \sum _n a_n x ^ n \tag{1.0.1}
\]

\(a\) 既可以是有穷序列也可以是无穷序列，\(x\) 不具有实际意义，仅作为一个形式上的变量参与运算。

### 两种基本形式

#### 加法与乘法

假设两个序列 \(a,b\) 的 \(\rm OGF\) 分别为 \(F(x),G(x)\)。

加减不必多说 ：

\[
F(x) \pm G(x) = \sum _n (a_n \pm b_n) x ^ n \tag{1.1.1}
\]

乘法用卷积定义 ：

\[
F(x)G(x) = \sum _n x ^ n \sum _{i = 0} ^n a_ib_{n - i} \tag{1.1.2}
\]

#### 封闭形式

在使用生成函数的过程中，我们不会一直使用形式幂级数形式，有时候会为了计算方便将其替换成封闭形式。

\(F(x) = \sum_{n} x^{n}\)

\[
F(x) - xF(x) = 1
\]

\[
F(x) = \frac{1}{1 - x} \tag{1.2.1}
\]

\(F(x) = \sum_{n} q^{n} x^{n}\)

\[
F(x) - qxF(x) = 1
\]

\[
F(x) = \frac{1}{1 - qx} \tag{1.2.2}
\]

\(F(x) = \sum_{n} (n + 1)x^{n}\)

\[
\begin{aligned}
    F(x) &= \sum _{n \geqslant 1} nx ^ {n - 1}\\
    &= \sum _ {n} (x  ^ n)'\\
    &= \left(\frac{1}{1 - x}\right)'
\end{aligned}
\]

\[
F(x) = \frac{1}{(1 - x) ^ 2} \tag{1.2.3}
\]

\(F(x) = \sum_{n} \binom{m}{n} x^{n}\)

\[
F(x) = (1 + x) ^ m \tag{1.2.4}
\]

\(F(x) = \sum_{n} \binom{n + m}{n} x^{n}\)

\[
F(x) = \frac{1}{(1 - x) ^ {m + 1}} \tag{1.2.5}
\]

考虑归纳证明 ：

显然当 \(m = 0\) 时，有 \(F(x) = \sum_{n} \binom{n}{n} x^{n} = \frac{1}{1 - x}\)。

当 \(m \gt 0\) 时 ：

\[
\begin{aligned}
    \frac{1}{(1 - x) ^ {m + 1}} &= \frac{1}{(1 - x) ^ m}\frac{1}{1 - x}\\
    &= \left[\sum _ n \dbinom{m + n - 1}{n} x ^ n\right] \left(\sum _n x ^ n\right)\\
    &= \sum _ n x ^ n \sum _ {i = 0} ^ n \dbinom{m + i - 1}{i}\\
    &= \sum _ n \dbinom{m + n}{n} x ^ n
\end{aligned}
\]

关于上述推导过程中最后一步用到的组合恒等式 ：

\[
\sum _ {i = 0} ^ n \dbinom{m + i - 1}{i} = \dbinom{m + n}{n} \tag{1.2.6}
\]

考虑其组合意义，左边相当于将 \(i\) 个无标号石子放进 \(m\) 个有标号盒子里，盒子允许为空的方案数。

考虑将 \(n\) 个石子放进 \(m + 1\) 个盒子中的方案数，规则同上，显然方案数为 \(\binom{m + n}{n}\)。 假设从 \(m + 1\) 个盒子中取出一个，枚举要将 \(n\) 个石子中的多少个放入剩下的 \(m\) 个盒子中，剩余的石子就只能放进取出的盒子中了，则方案数为 \(\sum_{i = 0}^{n} \binom{m + i - 1}{i}\)。 故组合恒等式 \((1.2.6)\) 得证。

还有另一种仅通过组合意义证明式 \((1.2.5)\) 的方法 ：

可以发现 \(\frac{1}{(1 - x)^{m + 1}} = \left(\frac{1}{1 - x}\right)^{m + 1}\)，相当于将初始仅有 \(a_{0} = 1\) 的序列做了 \(m + 1\) 遍前缀和。又因为每做一遍前缀和的组合意义是一个位置可以走到任意一个不在自己左边的位置，所以实际上 \(\frac{1}{(1 - x)^{m + 1}}\) 的第 \(n\) 项系数即为从 \(0\) 开始，每次向右走非负整数步，走 \(m + 1\) 步到达 \(n\) 的方案数。归约到一个更加经典的问题，就是不定方程 \(\sum_{i = 1}^{m + 1} x_{i} = n\) 的非负整数解数量，众所周知，其值为 \(\binom{m + n}{n}\)。

#### 部分分式定理

在上文中，我们已经知道了形如 \(F(x) = \frac{1}{(1 - qx)^{m}}\) 的部分分式可以简单地被转换为形式幂级数形式，于是我们想找到一种方法能够将形如 \(\frac{P(x)}{Q(x)}\) 的一般分式拆成若干个部分分式之和。

部分分式定理指出，如果 \(\deg P \lt \deg Q\)，那么可以先将 \(Q(x)\) 因式分解，然后使用待定系数法构造若干个形如 \(\frac{A}{(1 - ax)^{p}}\) 的式子，使它们的和为 \(\frac{P(x)}{Q(x)}\)。

例如 \(F(x) = \frac{P(x)}{(x - 1)^{2} (x + 2)}\)，那么构造 \(\frac{A}{x - 1} + \frac{B}{(x - 1)^{2}} + \frac{C}{x + 2} = \frac{P(x)}{(x - 1)^{2} (x + 2)}\)。

### 两个经典数列的生成函数

#### 斐波那契数列

斐波那契数列 \(\rm(Fibonacci\ Sequence)\) 被定义为 \(a_{0} = 0, a_{1} = 1,a_{n} = a_{n - 1} + a_{n - 2}(n \gt 1)\)。

设 \(F(x) = \sum_{n} a_{n} x^{n}\)，显然有 ：

\[
F(x) = xF(x) + x ^ 2 F(x) - a_0x + a_1x + a_0
\]

解得 ：

\[
F(x) = \frac{x}{1 - x - x ^ 2} \tag{1.3.1}
\]

考虑使用部分分式定理，观察到分母多项式次数为 \(2\)，那么设 ：

\[
\frac{A}{1 - ax} + \frac{B}{1 - bx} = \frac{x}{1 - x - x ^ 2}
\]

解得 ：

\[
\begin{aligned}
    F(x) &= \frac{x}{1 - x - x ^ 2}\\
    &= \frac{\frac{\sqrt{5}}{5}}{1 - \frac{1 + \sqrt{5}}{2}x} + \frac{-\frac{\sqrt{5}}{5}}{1 - \frac{1 - \sqrt{5}}{2}x}\\
    &= \sum _ n x ^ n \frac{\sqrt{5}}{5}\left[\left(\frac{1 + \sqrt{5}}{2}\right) ^ n - \left(\frac{1 - \sqrt{5}}{2}\right) ^ n\right]
\end{aligned}
\]

于是上式即为斐波那契数列的形式幂级数形式和通项。

#### 卡特兰数

首先引入牛顿二项式定理。

让我们重定义组合数的运算 ：

\[
\dbinom{r}{k} = \frac{r ^ {\underline{k}}}{k!}~~(r \in \mathbb{C}, k \in \mathbb{N}) \tag{1.3.3}
\]

在这种情况下，对于 \(\alpha \in \mathbb{C}\)，有 ：

\[
(1 + x) ^ {\alpha} = \sum _n \dbinom{\alpha}{n} x ^ n \tag{1.3.4}
\]

对于卡特兰数序列，令 \(a_{0} = a_{1} = 1, a_{n} = \sum\limits_{i = 0}^{n - 1} a_{i} \times a_{n - i - 1}(n \gt 1)\)

令其 \(\rm OGF\) 为 \(F(x) = \sum\limits_{n} a^{n} x^{n}\)。

不难发现其递推式是一个卷积的形式，于是有：

\[
xF ^ 2(x) + 1 = F(x)
\]

解之得：

\[
F(x) = \frac{1 \pm \sqrt{1 - 4x}}{2x} \tag{1.3.5}
\]

要保留哪个根呢？

求解上式在 \(x \to 0\) 时的极限可以发现，当 \(F(x) = \dfrac{1 + \sqrt{1 - 4x}}{2x}\) 时不收敛。

原因是：

\[
F(x) = \dfrac{1 + \sqrt{1 - 4x}}{2x} = \frac{2}{1 - \sqrt{1 - 4x}}
\]

则有：

\[
\lim\limits_{x \to 0 ^ {+}} \frac{2}{1 - \sqrt{1 - 4x}} = \infty
\]

\[
\lim\limits_{x \to 0 ^ {-}} \frac{2}{1 - \sqrt{1 - 4x}} = -\infty
\]

故此时 \(x \to 0\) 时极限不存在。

因此可以得到：

\[
F(x) = \dfrac{1 - \sqrt{1 - 4x}}{2x} \tag{1.3.6}
\]

将分子部分单独拿出来考虑，令 \(G(x) = 1 - \sqrt{1 - 4x} = 1 - (1 - 4x)^{\frac{1}{2}}\)，使用牛顿二项式定理展开：

\[
\begin{aligned}
G(x) &= 1 - \sum\limits_{n \geqslant 0} \dbinom{\frac{1}{2}}{n} (-4x) ^ n \\
&= 1 - \sum\limits_{n \geqslant 0} \frac{\frac{1}{2} ^ {\underline n}}{n!} (-4x) ^ n \\
&= 1 - \sum\limits_{n \geqslant 0} \frac{\frac{1}{2} \times (-\frac{1}{2}) \times (-\frac{3}{2}) \times \cdots \times (-\frac{2n - 3}{2})}{n!} (-4x) ^ n \\
\end{aligned}
\]

特别要注意的是 \(\binom{\frac{1}{2}}{0} = \frac{\frac{1}{2}^{0}}{0!} = 1\) 但是用上面那个式子是不正确的，因此需要特别考虑：

\[
\begin{aligned}
G(x) &= \sum\limits_{n \geqslant 1} (-1) ^ {2n - 1} \frac{(2n - 3)!!}{n!2 ^ n} (4x) ^ n \\
&= \sum\limits_{n \geqslant 1} \frac{(2n - 2)!}{n!(2n - 2)!!2 ^ n} (4x) ^ n \\
&= \sum\limits_{n \geqslant 1} \frac{2(2n - 2)!}{n!(n - 1)!} x ^ n \\
&= \sum\limits_{n \geqslant 1} \frac{\binom{2n - 1}{n}}{2n - 1} 2x ^ n
\end{aligned}
\]

带回原式有：

\[
\begin{aligned}
F(x) &= \frac{\sum\limits_{n \geqslant 1} \frac{\binom{2n - 1}{n}}{2n - 1} 2x ^ n}{2x} \\
&= \sum\limits_{n \geqslant 0} \frac{\binom{2n + 1}{n + 1}}{2n + 1} x ^ n \\
&= \sum\limits_{n \geqslant 0} \frac{\binom{2n}{n}}{n + 1} x ^ n
\end{aligned}
\tag{1.3.9}
\]

因此可知 \(a_{n} = \dfrac{\binom{2n}{n}}{n + 1}\)。

### 欧拉变换

考虑求解形如下式的 \(\rm OGF\) ：

\[
F_i(x) = \left(\sum _ j x ^ {ji}\right) ^ {f _ i} =  \left(\frac{1}{1 - x ^ i}\right) ^ {f _ i} \tag{2.3.1}
\]

\[
\varepsilon\circ F(x) = \prod _ i F_i(x) = \prod _ i \left(\frac{1}{1 - x ^ i}\right) ^ {f _ i} \tag{2.3.2}
\]

这个 \(\rm OGF\) 的组合意义是将 \(n\) 个互不区分的小球分进若干个非空集合，大小为 \(i\) 的集合有 \(f_{i}\) 种方案的总方案数。

注意到式 \((2.3.2)\) 右边是连乘，于是对其取 \(\ln :\)

\[
\begin{aligned}
    \ln \varepsilon \circ F(x) &= \sum _ i \ln \left(\frac{1}{1 - x ^ i}\right) ^ {f _ i}\\
    &= \sum _ i f_i \times \ln\left(\frac{1}{1 - x ^ i}\right)\\
    &= -\sum _ i f_i \times \ln (1 - x ^ i)\\
    &= \sum _ i \sum _ j \frac{f_i}{j + 1} x ^ {i(j + 1)}
\end{aligned}
\]

关于上式中化简 \(\ln (1 - x^{i})\) 的步骤可以参考后文中式 \((2.1.5)\)。

由于我们一般只需求生成函数的前 \(n\) 项，观察到 \(i\) 和 \(j\) 的枚举构成了调和级数的关系，可以直接暴力计算。

最后将求出的幂级数 \(\rm exp\) 回去即可得到 \(\varepsilon \circ F(x)\)。

时间复杂度 \(\Theta(n \log n)\)。

## 指数型生成函数

序列 \(a\) 的指数型生成函数 \(\rm(Exponential\ Generating\ Function,EGF)\) 被定义为形式幂级数 ：

\[
\hat{F}(x) = \sum _n a_n \frac{x ^ n}{n!}\tag{2.0.1}
\]

### 两种基本形式

#### 加法与乘法

形式幂级数形式的加减法与 \(\rm OGF\) 基本相同，也是对应系数相加。

乘法被定义为 ：

\[
\begin{aligned}
    \hat{F}(x)\hat{G}(x) &= \sum _ i a _ i \frac{x ^ i}{i!} \sum _ j b _ j \frac{x ^ j}{j!}\\
    &= \sum _ n x ^ n \sum _ {i = 0} ^ n a _ i b _ {n - i} \frac{1}{i!(n - i)!}\\
    &= \sum _ n \frac{x ^ n}{n!} \sum _ {i = 0} ^ n\dbinom{n}{i} a _ i b _ {n - i}
\end{aligned}
\]

#### 麦克劳林级数

众所周知有泰勒展开 ：

\[
F(x) = \sum _ n \frac{F^{(n)}(x _ 0)}{n!}(x - x _ 0) ^ n \tag{2.1.2}
\]

取 \(x_{0} = 0\) 时的特殊情况可以得到麦克劳林级数 ：

\[
F(x) = \sum _ n F^{(n)}(0)\frac{x ^ n}{n!} \tag{2.1.3}
\]

有 \(\exp(0) = 1\)，故 \(e^{x}\) 的 \(\rm EGF\) 为 ：

\[
\hat{\exp}(x) = \sum _ n \frac{x ^ n}{n!} \tag{2.1.4}
\]

#### 常见幂级数的封闭形式

\[
\begin{aligned}
e ^ {qx} &= \sum _ n q ^ n \frac{x ^ n}{n!}\\
\frac{e^{x}+e^{-x}}{2}&=\sum_{n}\frac{x^{2 n}}{(2 n) !} \\
\frac{e^{x}-e^{-x}}{2}&=\sum_{n}\frac{x^{2 n+1}}{(2 n+1) !} \\
\ln (1-x)&=-\sum_{n} \frac{x ^ {n + 1}}{n + 1}\\
\ln (1+x)&=\sum_{n}(-1)^{n} \frac{x^{n+1}}{n+1} \\
(1+x)^{\alpha}&=\sum_{n} \alpha^{\underline{n}} \frac{x^{n}}{n !}
\end{aligned}
\]

### 组合意义

**结论：设 \(\hat{G}(x)\) 表示集合内部分配方案数关于集合大小的 \(\rm EGF\)，\(\hat{F}(x)\) 表示将问题划分成若干个无标号非空子问题，子问题的方案数为 \(\hat{G}(x)\) 的关于问题总规模的方案数的 \(\rm EGF\)。那么有关系式 ：**

\[
\hat{F}(x) = \exp \hat{G}(x) \tag{2.2.1}
\]

考虑证明上述结论，设 \(f_{i, j}\) 表示将 \(j\) 个**有标号**小球放进 \(i\) 个**有标号**盒子中的方案数，\(g_{i}\) 表示集合内有 \(i\) 个元素的方案数，显然有 ：

\[
f_{i, j} = \sum _{k = 1} ^ {j - i + 1} \dbinom{j}{k} f_{i - 1, j - k} \times g_k
\]

考虑到 \(f_{i - 1, j - k}\) 在 \(k \gt j - i + 1\) 时的值为 \(0\)，所以可以将 \(k\) 的枚举上界换成 \(j\)，发现有 ：

\[
\hat{F}_i(x) = \hat{F}_{i - 1}(x)\hat{G}(x)
\]

化简得到并根据 \(\hat{F}_{i}(x)\) 的定义得到 ：

\[
\hat{F}_i(x) = \sum _ j f_{i, j} \frac{x ^ j}{j!} = \hat{G}^i(x) \tag{2.2.2}
\]

于是有 ：

\[
\begin{aligned}
    \exp \hat{G}(x) &= \sum_n \frac{\hat{G}^n(x)}{n!}\\
    &= \sum _ n \frac{1}{n!} \sum _ i f_{n, i} \frac{x ^ i}{i!}\\
    &= \sum _ i \left(\sum _ n \frac{f _ {n, i}}{n!}\right) \frac{x ^ i}{i!}
\end{aligned}
\]

这恰好对应了 \(\hat{F}(x)\) 的定义，于是 \(\hat{F}(x) = \exp \hat{G}(x)\)。
