---
title: "简单的代数反演"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "简单的代数反演"
aliases:
  - "/blog/jian-dan-de-dai-shu-fan-yan/"
tags:
  - "Combinatorics"
  - "Inversion"
  - "Number Theory"
categories:
  - "CP"
---

## 二项式反演

### 数列形式

\[
g(x)=\sum_{i=x}^n\dbinom{i}{x}f(i)\iff f(x)=\sum_{i=x}^n (-1)^{i-x}\dbinom{i}{x}g(i)
\]

\(\large\rm Proof:\)

将上式带入下式得 \(:\)

\[
f(x)=\sum_{i=x}^n (-1)^{i-x}\dbinom{i}{x}\sum_{j=i}^n\dbinom{j}{i}f(j)
\]

整理得 \(:\)

\[
f(x)=\sum_{i=x}^n\sum_{j=i}^n(-1)^{i-x}\dbinom{j}{i}\dbinom{i}{x}f(j)
\]

根据组合恒等式 \(\dbinom{i}{j}\dbinom{j}{k}=\dbinom{i}{k}\dbinom{i-k}{j-k}\) 得 \(:\)

\[
f(x)=\sum_{i=x}^n\sum_{j=i}^n(-1)^{i-x}\dbinom{j}{x}\dbinom{j-x}{i-x}f(j)
\]

交换枚举顺序得 \(:\)

\[
f(x)=\sum_{j=x}^n\sum_{i=x}^j(-1)^{i-x}\dbinom{j}{x}\dbinom{j-x}{i-x}f(j)
\]

改变代表字母，整理得 \(:\)

\[
f(x)=\sum_{i=x}^n\dbinom{i}{x}f(i)\sum_{j=x}^i(-1)^{j-x}\dbinom{i-x}{j-x}
\]

将靠后的 \(\sum\) 枚举的 \(j\) 替换成 \(j+x\) 得 \(:\)

\[
f(x)=\sum_{i=x}^n\dbinom{i}{x}f(i)\sum_{j=0}^{i-x}(-1)^{j}\dbinom{i-x}{j}
\]

\[
\because \sum_{i=0}^k(-1)^i\dbinom{k}{i}=(1-1)^k
\]

\[
\therefore \sum_{i=0}^k(-1)^i\dbinom{k}{i}=[k=0]
\]

所以此式不为 \(0\) 当且仅当 \(i=x\)，故 \(:\)

\[
f(x)=\sum_{i=x}\dbinom{x}{x}f(i)=f(x)
\]

原式得证。

**我们来看看二项式反演的数列形式有什么应用：**

**乱序排列问题：** 求有多少种不同的长度为 \(n\) 的排列 \(p\)，使得 \(\forall i\in [1,n],p_{i}\not = i\)。

令 \(g(i)\) 表示钦定有 \(i\) 个数一定在自己的位置上，剩下的随便排的方案数，显然有 :

\[
g(i)=\dbinom{n}{i}(n-i)!
\]

令 \(f(i)\) 表示恰好有 \(i\) 个数在自己的位置上的方案数，考虑到 \(f(i)\) 会被 \(g(j)\ (j\leqslant i)\) 计算 \(\dbinom{i}{j}\) 次，于是有 \(:\)

\[
g(i)=\sum_{j=i}^n\dbinom{j}{i}f(j)
\]

根据二项式反演 \(:\)

\[
f(i)=\sum_{j=i}^n(-1)^{j-i}\dbinom{j}{i}g(j)
\]

将 \(g(i)=\dbinom{n}{i}(n-i)!\) 带入得 \(:\)

\[
f(i)=\sum_{j=i}^n(-1)^{j-i}\dbinom{j}{i}\dbinom{n}{j}(n-j)!
\]

根据组合恒等式 \(\dbinom{i}{j}\dbinom{j}{k}=\dbinom{i}{k}\dbinom{i-k}{j-k}\)，整理得 \(:\)

\[
f(i)=\dbinom{n}{i}\sum_{j=i}^n(-1)^{j-i}\dbinom{n-i}{j-i}(n-j)!
\]

考虑到当 \(i=0\) 时为答案，所以 \(:\)

\[
\begin{aligned}
    Ans=f(0)&=\sum_{i=0}^n(-1)^i\dbinom{n}{i}(n-i)!\\
    &=\sum_{i=0}^n(-1)^i\dfrac{n!}{i!}\\
    &=(n+1)!\sum_{i=0}^n(-1)^i(i!)^{-1}
\end{aligned}
\]

### 集合形式

\[
f(S)=\sum_{S\subseteq T}g(T)\iff g(S)=\sum_{S\subseteq T} (-1)^{|T|-|S|}f(T)
\]

\(\large\rm Proof:\)

同样考虑带入证明 ：

\[
\begin{aligned}
    f(S)&=\sum_{S\subseteq T}\sum_{T\subseteq R}(-1)^{|R|-|T|}f(R)\\
    &=\sum_{S\subseteq R}f(R)\sum_{S\subseteq T\subseteq R}(-1)^{|R|-|T|}
\end{aligned}
\]

考虑枚举 \(T-S\) 的大小 ：

\[
\begin{aligned}
    f(S)&=\sum_{S\subseteq R}f(R)\sum_{i=0}^{|R|-|S|}\dbinom{|R|-|S|}{i}(-1)^{|R|-(|S|+i)}\\
    &=\sum_{S\subseteq R}[|S|=|R|]\\
    &=f(S)
\end{aligned}
\]

原式得证。

**我们来看看二项式反演的集合形式有什么应用：**

**有向图无环子图计数：** 给定一张 \(n\) 个点的有向图，求其无环子图的数量。

考虑动态规划，设 \(f_{S}\) 表示点集 \(S\) 导出子图的答案。

由于是 \(\rm DAG\) 计数，所以我们可以很自然地想到枚举入度为 \(0\) 的点，假设 \(T\) 是 \(S\) 的子集，并且其中的每个点都没有入边，那么显然有转移 ：

\[
f_S=\sum_{T\subseteq S,T\not = \varnothing}2^{cnt_{T,S-T}}\times f_{S-T}
\]

其中 \(cnt_{S,T}\) 表示集合 \(S\) 到集合 \(T\) 的连边总数。

但我们发现这样做实际上是错的，因为 \(T\) 不一定包含了 \(S\) 中所有入度为 \(0\) 的点，我们考虑容斥。

设 \(q_{T}=2^{cnt_{T,S-T}}\times f_{S-T}\)，\(p_{T}\) 表示 \(S\) 中恰好有 \(T\) 作为入度为 \(0\) 的点的方案数，有 \(q_{T}=\sum\limits_{T\subseteq S} p_{S}\)。

由二项式反演的集合形式可以得到 ：

\[
p_S=\sum_{S\subseteq T}(-1)^{|T|-|S|}q_T
\]

回到原本的 \(\rm DP\)，我们需要求 ：

\[
\begin{aligned}
    f_S&=\sum_{T\subseteq S,T\not= \varnothing}p_T\\
    &=\sum_{T\subseteq S,T\not= \varnothing}\sum_{T\subseteq R\subseteq S}(-1)^{|R|-|T|}q_R\\
    &=\sum_{R\subseteq S,R\not= \varnothing}q_R \sum_{T\subseteq R,T\not=\varnothing}(-1)^{|R|-|T|}\\
    &=\sum_{R\subseteq S,R\not= \varnothing}q_R (-1)^{|R|}\left(\sum_{T\subseteq R}(-1)^{-|T|}-1\right)\\
    &=\sum_{T\subseteq S,T\not= \varnothing}(-1)^{|T|-1}q_T
\end{aligned}
\]

于是转移方程为 ：

\[
f_S=\sum_{T\subseteq S,T\not= \varnothing}(-1)^{|T|-1}2^{cnt_{T,S-T}}f_{S-T}
\]

现在只需要 \(\Theta(1)\) 计算 \(cnt_{T,S-T}\) 即可做到 \(\Theta(3^{n})\) 计算计算答案，考虑预处理。

可以在枚举了每个 \(S\) 做转移的时候再算这个东西，此时只需要记 \(cnt_{T}\ (T\subseteq S,T\not=\varnothing)\) 表示 \(T\) 恰好作为 \(S\) 中没有入度的点集的路径数。考虑在进行所有计算之前预处理 \(A_{i,S}\) 表示 \(i\) 到 \(S\) 中的边数，\(D_{i,S}\) 表示 \(S\) 中的点到 \(i\) 的边数和，这两个数组都可以 \(\Theta(n2^{n})\) 预处理。

计算 \(cnt\) 时考虑从小到大枚举每个 \(T\) 计算答案，可以发现 \(T\) 的每个真子集的答案都已经被计算出来了，于是任取一个点从 \(T\) 中移到 \(S-T\) 即可算出答案，这里考虑 \(\Theta(1)\) 枚举 `lowbit`. 可以发现，转移式为 ：

\[
cnt_T=cnt_{T-\{u\}}+A_{u,S-T}-D_{T-\{u\},u}
\]

于是本题到此，可以做到时间复杂度 \(\Theta(3^{n})\)，空间复杂度 \(\Theta(n2^{n})\)。

### 子集反演

\[
f(S)=\sum_{T\subseteq S}g(T)\iff g(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}f(T)
\]

\(\large\rm Proof:\)

还是考虑带入证明，与二项式反演的集合形式类似 \(:\)

\[
\begin{aligned}
    f(S)&=\sum_{T\subseteq S}\sum_{R\subseteq T}(-1)^{|T|-|R|}f(R)\\
    &=\sum_{R\subseteq S}f(R)\sum_{R\subseteq T\subseteq S}(-1)^{|T|-|R|}\\
    &=\sum_{R\subseteq S}f(R)\sum_{i=0}^{|S|-|R|}\dbinom{|S|-|R|}{i}(-1)^{(|S|-i)-|R|}\\
    &=\sum_{R\subseteq S}[|R|=|S|]\\
    &=f(S)
\end{aligned}
\]

原式得证。

## 斯特林反演

### 第二类斯特林数

#### 定义

定义 \(\begin{Bmatrix}n \ m\end{Bmatrix}\) 为将 \(n\) 个有标号小球放入 \(m\) 个无标号盒子，每个盒子不能为空的方案。

#### 递推式

\[
\begin{Bmatrix}n \ m\end{Bmatrix} = \begin{Bmatrix}n - 1 \ m - 1\end{Bmatrix} + m \times \begin{Bmatrix}n - 1 \ m\end{Bmatrix}
\]

根据组合意义不难证明。

#### 求一行第二类斯特林数

考虑以下第二类斯特林数的组合意义，我们考虑使用容斥描述第二类斯特林数的答案。

首先我们求出将 \(n\) 个有标号小球放入 \(m\) 个有标号盒子，盒子不能为空的方案，根据这个问题的特殊性，任意一种无标号盒子的方案恰好双向对应 \(m!\) 中有标号盒子的方案，最后除 \(m!\) 即可。

对于盒子是否为空进行容斥：

\[
\begin{Bmatrix}n \ m\end{Bmatrix} = \frac{1}{m!} \sum\limits_i ^ m (-1) ^ i \dbinom{m}{i}(m - i) ^ n
\]

显然是一个卷积的形式，\(\rm NTT\) 即可做到 \(\mathcal{O(n \log n)}\)。

#### 求一列第二类斯特林数

不难发现第二类斯特林数的定义与 \(\exp\) 的组合意义很相似，于是我们考虑 \(\rm EGF:\) \(\widehat F(x) = \sum\limits_{i = 1}^{\infty} \frac{x^{i}}{i!} = e^{x} - 1\)。

那么根据 \(\rm EGF\) 相乘的组合意义，\([\dfrac{x^{n}}{n!}]\widehat F^{m}(x) = [\dfrac{x^{n}}{n!}](e^{x} - 1)^{m} = \begin{Bmatrix}n \ m\end{Bmatrix}\)。

使用多项式快速幂即可做到 \(\mathcal{O(n \log n)}\)。

### 第一类斯特林数

#### 定义

定义 \(\begin{bmatrix}n \ m\end{bmatrix}\) 为将 \(n\) 个数划分成 \(m\) 个互不区分的非空置换的方案数。

#### 递推式

\[
\begin{bmatrix}n \ m\end{bmatrix} = \begin{bmatrix}n - 1 \ m - 1\end{bmatrix} + (n - 1) \times \begin{bmatrix}n - 1 \ m\end{bmatrix}
\]

由组合意义不难证明。

#### 求一行第一类斯特林数

因为第一类斯特林数不具有较好的组合意义，因此不能像第二类斯特林数那样使用另一种方式来描述其，因此我们直接考虑第一类斯特林数的 \(\rm OGF\)：

\[
\begin{aligned}
F_i(x) &= \sum\limits_j ^ \infty \begin{bmatrix}i \ j\end{bmatrix} x ^ j \\
&= x \times F_{i - 1}(x) + (i - 1) F_{i - 1}(x) \\
&= (i + x - 1) F_{i - 1}(x) \\
&= \prod\limits_j ^ {i - 1} (x + j)
\end{aligned}
\]

那么就有：

\[
F_n(x) = \prod\limits_i ^ {n - 1} (x + i)
\]

当然可以直接使用启发式合并做到 \(\mathcal{O(n \log^{2n})}\)，但还存在一个更加优秀的方法：倍增法。

\[
F_{2n}(x) = F_n(x) \times F_n(x + n)
\]

只需快速计算 \(F_{n}(x + n)\) 即可，令 \(F_{n}(x) = \sum\limits_{i}^{\infty} f_{i} x^{i}\)：

\[
\begin{aligned}
F_n(x + n) &= \sum\limits_i ^ n f_i(x + n) ^ i \\
&= \sum\limits_i ^ n f_i\sum\limits_j ^ i x ^ j n ^ {i - j}
\end{aligned}
\]

后者很明显是一个卷积的形式，直接计算即可，根据倍增的复杂度，可以做到 \(\mathcal{O(n \log n)}\)。

#### 求一列第一类斯特林数

类似于求一列第二类斯特林数的方法，考虑 \(\rm EGF:\) \(\widehat F(x) = \sum\limits_{i}^{\infty} \dfrac{(i - 1)!x^{i}}{i!} = \sum\limits_{i}^{\infty} \dfrac{x^{i}}{i} = \ln\left(\dfrac{1}{1 - x}\right)\)

那么就有：

\[
\begin{bmatrix}n \ m\end{bmatrix} = [\frac{x ^ n}{n!}]\widehat F ^ m(x)
\]

使用多项式快速幂即可，复杂度 \(\mathcal{O(n \log n)}\)。

### 普通幂, 上升幂, 下降幂的转换

先介绍两个最简单的：上升幂和下降幂的转换：

\[
x ^ {\underline{n}} = (-1) ^ n (-x) ^ {\overline n}
\]

\[
x ^ {\overline{n}} = (-1) ^ n (-x) ^ {\underline n}
\]

再根据我们求一行斯特林数的方法，可以得到上升幂转普通幂公式：

\[
x ^ {\overline n} = \sum\limits_i ^ n \begin{bmatrix} n \ i \end{bmatrix} x ^ i
\]

而根据第二类斯特林数的组合意义，再根据普通幂 \(x^{n}\) 的组合意义，可以得到普通幂转下降幂公式：

\[
x ^ n = \sum\limits_i ^ x \dbinom{x}{i} \begin{Bmatrix} n \ i \end{Bmatrix} i! = \sum\limits_i ^ x \begin{Bmatrix} n \ i \end{Bmatrix} x ^ {\underline{i}}
\]

再利用最开始提到的下降幂转上升幂公式变形，我们可以得到普通幂转上升降幂公式：

\[
\begin{aligned}
(-x) ^ n &= \sum\limits_i ^ x \begin{Bmatrix} n \ i \end{Bmatrix} (-x) ^ {\underline{i}} \\
&= \sum\limits_i ^ x \begin{Bmatrix} n \ i \end{Bmatrix} (-1) ^ i x ^ {\overline{i}}
\end{aligned}
\]

\[
\Longleftrightarrow x ^ n = \sum\limits_i ^ x (-1) ^ {n - i}\begin{Bmatrix} n \ i \end{Bmatrix}x ^ {\overline{i}}
\]

同理可得下降幂转普通幂公式：

\[
x ^ {\underline{n}} = \sum\limits_i ^ x (-1) ^ {n - i} \begin{bmatrix} n \ i \end{bmatrix} x ^ i
\]

总结一下四个公式，普通幂转出去使用第二类斯特林数，转回来使用第一类斯特林数。阶数上升（下转普，普转上）加 \(-1\)。

通过这四个公式，我们也能完成一般多项式和上升幂下降幂多项式的互相转化。

**我们来看看这几个式子有什么应用：**

**例题：** 给定 \(k\) 次多项式 \(f(x)\) 的各项系数和一个整数 \(n\)，求以下式子对 \(998244353\) 取模后的值 ：

\[
\sum_{i=0}^n\dbinom{n}{i}2^{n-i}f(i)
\]

我们发现带 \(f(x)\) 的式子没有前途，于是将其拆开 ：

\[
\sum_{i=0}^n\dbinom{n}{i}2^{n-i}\sum_{j=0}^ka_ji^j
\]

这里有个套路是将整数幂转第二类斯特林数 ：

\[
\begin{aligned}
    m^n&=\sum_{k=0}^m\dbinom{m}{k}\begin{Bmatrix}n\\ m-k\end{Bmatrix}(m-k)!\\
    &=\sum_{k=0}^m\begin{Bmatrix}n\\ k\end{Bmatrix}m^{\underline{k}}
\end{aligned}
\]

转化的含义是将 \(m^{n}\) 看作 \(\rm LLA\) 问题的方案数，我们发现 \(\small\begin{Bmatrix}n\\ m\end{Bmatrix}\) 是 \(\rm LUB\) 问题的方案数，于是枚举 \(m\) 个集合中有 \(k\) 个 \(0\)，然后用第二类斯特林数将 \(\rm LUA\) 算出来后乘上 \((m-k)!\) 得到 \(\rm LLA\) 的方案数。

于是就可以开始推式子了 ：

\[
\begin{aligned}
    &\quad~\sum_{i=0}^n\dbinom{n}{i}2^{n-i}f(i)\\
    &=\sum_{i=0}^n\dbinom{n}{i}2^{n-i}\sum_{j=0}^ka_ji^j\\
    &=\sum_{i=0}^n\dbinom{n}{i}2^{n-i}\sum_{j=0}^ka_j\sum_{p=0}^i\dbinom{i}{p}\begin{Bmatrix}j\\ p\end{Bmatrix}p!\\
    &=\sum_{i=0}^n\sum_{j=0}^k\sum_{p=0}^i\dbinom{n}{i}\dbinom{i}{p}2^{n-i}a_j\begin{Bmatrix}j\\ p\end{Bmatrix}p!\\
    &=\sum_{j=0}^ka_j\sum_{p=0}^n\begin{Bmatrix}j\\ p\end{Bmatrix}p!\sum_{i=p}^n\dbinom{n}{i}\dbinom{i}{p}2^{n-i}\\
    &=\sum_{j=0}^ka_j\sum_{p=0}^n\begin{Bmatrix}j\\ p\end{Bmatrix}p!\sum_{i=p}^n\dbinom{n}{p}\dbinom{n-p}{i-p}2^{n-i}\\
    &=\sum_{j=0}^ka_j\sum_{p=0}^n\dbinom{n}{p}\begin{Bmatrix}j\\ p\end{Bmatrix}p!\sum_{i=0}^{n-p}\dbinom{n-p}{i}2^{n-p-i}\\
    &=\sum_{j=0}^k\sum_{p=0}^na_j\begin{Bmatrix}j\\ p\end{Bmatrix}\dbinom{n}{p}p!3^{n-p}\\
    &=\sum_{j=0}^k\sum_{p=0}^j\begin{Bmatrix}j\\ p\end{Bmatrix}a_j\times n^{\underline{p}}\times 3^{n-p}
\end{aligned}
\]

最后这个式子可以通过预处理第二类斯特林数，\(3\) 的次幂和 \(n\) 的 \(p\) 阶下降幂做到 \(\Theta(k^{2})\)。

### 斯特林反演

非常类似二项式反演的形式，有：

\[
f_n = \sum\limits_i ^ n \begin{Bmatrix} n \ i \end{Bmatrix} g_i \Longleftrightarrow g_n = \sum\limits_i ^ n (-1) ^ {n - i} \begin{bmatrix} n \ i \end{bmatrix} f_i
\]

我们首先需要了解斯特林反演基于的恒等式 \(-\) 反转公式：

\[
\sum\limits_{i = m} ^ n (-1) ^ {n - i} \begin{Bmatrix} n \ i \end{Bmatrix} \begin{bmatrix} i \ m \end{bmatrix} = [n = m]
\]

\[
\sum\limits_{i = m} ^ n (-1) ^ {n - i} \begin{bmatrix} n \ i \end{bmatrix} \begin{Bmatrix} i \ m \end{Bmatrix} = [n = m]
\]

不难发现两式的形式非常类似，我们只证明第一条式子，第二条式子是类似的。

\[
\begin{aligned}
x ^ n &= \sum\limits_i ^ n \begin{Bmatrix} n \ i \end{Bmatrix} x ^ {\underline{i}} \\
&= \sum\limits_i ^ n \begin{Bmatrix} n \ i \end{Bmatrix} (-1) ^ i (-x) ^ {\overline{i}} \\
&= \sum\limits_i ^ n (-1) ^ i \begin{Bmatrix} n \ i \end{Bmatrix} \sum\limits_j ^ i (-1) ^ j \begin{bmatrix} i \ j \end{bmatrix} x ^ j \\
&= \sum\limits_i ^ n \left( \sum\limits_{j = i} ^ n (-1) ^ {i - j} \begin{Bmatrix} n \ j \end{Bmatrix} \begin{bmatrix} j \ i \end{bmatrix}\right) x ^ i
\end{aligned}
\]

根据多项式恒等原理即可证明第一条反转公式。

有了这两条反转公式，就可以直接将斯特林反演左式带入右式以及右式带入左式来证明正确性了，过程是不难的。

## Min-Max 反演

令 \(\max\limits_{k}(S)\) 表示有限集 \(S\) 中的最大值，\(\min\limits_{k}(S)\) 表示有限集中的最小值。

### 基本形式

\[
\max(S)=\sum\limits_{T\subseteq S}(-1)^{|T|-1}\min(T)
\]

可以发现，对于所有 \(T\subseteq S-\{\max(S)\}\)，均存在 \(T+\max(S)\subseteq S\) 与之一一对应，且 \(\min(T)=\min(T+\max(S))\)。 由于它们的大小恰好相差 \(1\)，故对每个集合 \(S\) 配上 \((-1)^{|S|}\) 的系数可以恰好它们消掉，最后仅剩下集合 \(\{\max(S)\}\)，它的最小值恰好等于 \(\max(S)\)。

同理 ：

\[
\min(S)=\sum\limits_{T\subseteq S}(-1)^{|T|-1}\max(T)
\]

### 拓展形式

\[
\max_k(S)=\sum_{T\subseteq S,|T|\geqslant k}(-1)^{|T|-k}\dbinom{|T|-1}{k-1}\min(T)
\]

考虑 \(S\) 中的第 \(i\) 大数，它作为最小值被包含在大小为 \(|T|\) 的集合中共 \(\binom{i-1}{|T|-1}\) 次，每次出现会乘上 \(\binom{|T|-1}{k-1}\) 的权值，故一个数 \(\max\limits_{i}(S)\) 的总贡献为 ：

\[
\begin{aligned}
    val_i&=\max_i(S)\sum_{|T|=k}^i(-1)^{|T|-k}\dbinom{i-1}{|T|-1}\dbinom{|T|-1}{k-1}\\
    &=\max_i(S)\dbinom{i-1}{k-1}\sum_{|T|=k}^i(-1)^{|T|-k}\dbinom{i-k}{|T|-k}\\
    &=\max_i(S)\dbinom{i-1}{k-1}[i=k]
\end{aligned}
\]

所有数的贡献之和即为 \(\sum\limits_{i=1}^{|S|}val_{i}=\max\limits_{k}(S)\)，故原式成立。

另外，由于期望具有线性性，所以上面的式子在期望意义下也成立。

**我们来看看 \(\rm Min-Max\) 反演有什么应用：**

[**重返现世**](https://www.luogu.com.cn/problem/P4707) ：你需要收集 \(n\) 种物品中的任意 \(k\) 种，每个时刻会有一种物品被生成，第 \(i\) 种物品被生成的概率为 \(\frac{p_{i}}{m}\)，如果你还没有收集这种物品则可以收集它，求你收集到这 \(n\) 个物品中任意 \(k\) 个的期望时间。

保证 \(k\leqslant n\leqslant 10^{3},|n-k|\leqslant 10,0\leqslant p_{i}\leqslant m,\sum p=m,m\leqslant 10^{4}\)。

首先可以发现所有物品出现的时间不重，故构成一个集合，所以题目要求的为 \(E\left(\max (S)_{k}\right)\)。

套用拓展 \(\rm Min -Max\) 得到:

\[
E\left(\max (S)_{k}\right)=\sum_{T \subseteq S}\left(\begin{array}{c}
|T|-1 \\
k-1
\end{array}\right)(-1)^{|T|-k} E(\min (T))
\]

我们知道原来要求的是全集合中出现时间排第 \(k\) 的元素，由于变成了正过来看，此时的 \(k\) 变成了 \(n-k+ 1\) ，它的值非常小。

我们知道一个集合每次操作出现一个属于它的元素的概率为:

\[
e(S)=\sum_{i \in S} \frac{p_{i}}{m}
\]

于是我们知道期望时间为:

\[
\sum_{i=1}^{\infty} e(S)(1-e(S))^{i-1}=\frac{1}{e(S)}
\]

于是现在我们得到了一个复杂度为 \(\Theta\left(2^{n}\right)\) 的做法，暴力枚举子集，对于每个集合求出此式子并计算贡献。

然后我们来看这个式子:

\[
E\left(\max (S)_{k}\right)=\sum_{T \subseteq S}\left(\begin{array}{c}
|T|-1 \\
k-1
\end{array}\right)(-1)^{|T|-k} E(\min (T))
\]

考虑一个固定的集合大小 \(|T|\) ，其分配的系数相同均为 \(\left(\begin{array}{c}|T|-1 \ k-1\end{array}\right)(-1)^{|T|-k}\)

则我们只需要求出 \(\sum_{|T|=x} E(\min (T))\)

注意到 \(E(\min (T))=\frac{1}{e(S)}\)，于是我们可以给 \(d p\) 加一个维度记录 \(\sum p=e(S)\), 这样只需要统计有多少 个点满足 \(\sum p=i,|T|=j\)。

于是不妨记 \(d p_{i, j, k}\) 表示考虑到前 \(i\) 个数，满足 \(|T|=j, \sum p=k\) 的集合数，则可以得到转移:

\[
d p_{i, j, k}=d p_{i-1, j, k}+d p_{i-1, j-1, k-p_{i}}
\]

这样便可以得到一个复杂度为 \(\Theta\left(n^{2} m\right)\) 的做法了。

现在问题在于如何优化复杂度 \(?\)

我们发现转移已经是最优了，不能从这里下手，于是只能从状态下手。由于 \(k\) 这一维附带了一个 \(\frac{1}{k}\)，于是肯定定是不能省略的，唯一的办法是把记录中的 \(|T|\) 给去掉试试。

换而言之我们只统计到第 \(i\) 个数，任意放满足 \(\sum p=k\) 的数前面安排的系数之和。考虑系数为:

\[
\sum\left(\begin{array}{c}
|T|-1 \\
k-1
\end{array}\right)(-1)^{|T|-k}
\]

拆开试试 ?

\[
\sum \frac{(|T|-1) !}{(k-1) !(|T|-k) !}(-1)^{|T|-k}
\]

好像还是不行……

但是这个时候可以得到转移大致为：

\[
d p_{i, j}=d p_{i-1, j}+\ldots
\]

这个奇怪的东西应该表示为:

对于 \(d p_{i-1, j-p i}\) 的:

\[
\sum\left(\begin{array}{c}
|T|-1 \\
k-1
\end{array}\right)(-1)^{|T|-k}
\]

首先可以注意到所有 \(|T| \rightarrow|T|+1\) 于是整体需要乘一个 \(-1\)，注意到 \(|T| \rightarrow|T|+1\)，于是组合数变成了:

\[
\left(\begin{array}{c}
|T| \\
k-1
\end{array}\right)
\]

但是我们知道组合数可以递推所以有:

\[
\left(\begin{array}{c}
|T| \\
k-1
\end{array}\right)=\left(\begin{array}{c}
|T|-1 \\
k-1
\end{array}\right)+\left(\begin{array}{c}
|T|-1 \\
k-2
\end{array}\right)
\]

然而真正有趣的是这个式子可以放在一起一起递推，因为考虑计算 \(dp\) 时强制放入一个数则等价于 \(|T|\) 必然变大 \(1\)，于是我们可以给 \(dp\) 增加一个维度 \(k\) 来计算 \(dp\) 系数

\[
d p_{i, j, k}=d p_{i-1, j, k}+(-1) \times d p_{i-1, j-p i, k}+(-1)^{2} \times d p_{i-1, j-p i, k-1}
\]

即:

\[
d p_{i, j, k}=d p_{i-1, j, k}-d p_{i-1, j-p i, k}+d p_{i-1, j-p i, k-1}
\]

接下来考虑边界条件，这个好像有点难，因为我们的 \(dp\) 是按照转移的需求设计，所以它存在的实际意义也是为了方便转移而存在的。

我们知道 \(d p_{0, j, k}\) 的意义应该是: \(\sum_{\sum p=j}\left(\begin{array}{c}|T|-1 \ k-1\end{array}\right)\)，于是考虑前面的数，唯一的一个 \(\sum p=j\) 是空集，即 \(\sum p=0\)，此时有 \(|T|=0\) 求的则是:

\[
dp_{0,0, k}=\dbinom{-1}{k-1}
\]

这个时候我们需要拓宽组合数的意义, 你可以认为 \(\binom{-1}{-1}=1\) 而 \(\binom{x}{y}\) 在 \(x\lt y\) 的时候为 \(0\)，\(x=y\) 的时候为 \(1\)。 所以 \(dp\) 的边界为 \(dp_{0,0,0}=1\)。

转移的时候可以用滚动数组，总时间复杂度为 \(\Theta(nm(n-k))\)。

### Gcd-Lcm 反演

一般地，求 \(\rm lcm\) 通常转化为求解 \(\gcd\)，因为 \(\gcd\) 的性质更为优秀，也可以借助莫比乌斯反演。

通用形式为：

\[
\mathrm{lcm}(S) = \prod\limits_{T \subseteq S, T \ne \varnothing} \gcd(T) ^ {(-1) ^ {|T| - 1}}
\]

证明考虑使用 \(\rm Min-Max\) 容斥，考虑每个质因子 \(p\) 对左右的贡献：

\[
\begin{aligned}
p ^ {\max(p, S)} &= p ^ {\sum\limits_{T \subseteq S, T \ne \varnothing} (-1) ^ {|T| - 1} \min(p, T)} \\
&= \prod\limits_{T \subseteq S, T \ne \varnothing} p ^ {(-1) ^ {|T| - 1} \min(p, T)} \\
&= \prod\limits_{T \subseteq S, T \ne \varnothing} \left(p ^ {\min(p, T)}\right) ^ {(-1) ^ {|T| - 1} }
\end{aligned}
\]

那么有：

\[
\begin{aligned}
\mathrm{lcm}(S) &= \prod\limits_p p ^ {\max(p, S)} \\
&= \prod\limits_{p} \prod\limits_{T \subseteq S, T \ne \varnothing} \left(p ^ {\min(p, T)}\right) ^ {(-1) ^ {|T| - 1} } \\
&= \prod\limits_{T \subseteq S, T \ne \varnothing} \left(\prod\limits_p p ^ {\min(p, T)}\right) ^ {(-1) ^ {|T| - 1} } \\
&= \prod\limits_{T \subseteq S, T \ne \varnothing} \gcd(T) ^ {(-1) ^ {|T| - 1}}
\end{aligned}
\]

**我们来看看 \(\rm Gcd-Lcm\) 反演有什么应用：**

**前路（出题人：本校学长 @\(\rm remoon\)）:**

给定 \(A,B,C\)，求 ：

\[
\sum_{i=1}^A\sum_{j=1}^B\sum_{k=1}^C\mathrm{lcm}(i,j,k)
\]

保证 \(A,B,C\leqslant 5\times 10^{4}\)，答案对 \(10^{9}+7\) 取模。

**首先给出一个复杂度估界为 \(\Theta(n^{2})\) 的做法，但实测非常快。**

请注意，以下的推导遵循一个原则，对 \(i, j, k\) 做相同变换，不会先处理一部分再处理一部分。

\[
\begin{aligned}
Ans &= \sum\limits_{i = 1} ^ A \sum\limits_{j = 1} ^ B \sum\limits_{k = 1} ^ C \mathrm{lcm}(i, j, k) \\
&= \sum\limits_{i = 1} ^ A \sum\limits_{j = 1} ^ B \sum\limits_{k = 1} ^ C \frac{ijk(i, j, k)}{(i, j)(j, k)(k, i)} \qquad (\mathrm{Min-Max} ~ for ~ index) \\
&= \sum\limits_{i = 1} ^ A \sum\limits_{j = 1} ^ B \sum\limits_{k = 1} ^ C \frac{ijk}{(i, j)(j, k)(k, i)} \left( f \times \mu \times I \left((i, j, k)\right)\right) \qquad (f(i) = i)\\
&= \sum\limits_{d = 1} ^ A f \times \mu (d) \sum\limits_{i = 1} ^ {A / d} \sum\limits_{i = 1} ^ {B / d} \sum\limits_{i = 1} ^ {C / d} \frac{ijk}{(i, j)(j, k)(k, i)}
\end{aligned}
\]

令 \(F(A, B, C) = \sum\limits_{i = 1}^{A} \sum\limits_{i = 1}^{B} \sum\limits_{i = 1}^{C} \dfrac{ijk}{(i, j)(j, k)(k, i)}, g(i) = \dfrac{1}{i}, h = g \times \mu\) 则：

\[
\begin{aligned}
F(A, B, C) &= \sum\limits_{i = 1} ^ A \sum\limits_{i = 1} ^ B \sum\limits_{i = 1} ^ C ijk ( f \times \mu \times I ((i, j)))( f \times \mu \times I ((j, k)))( f \times \mu \times I ((k, i))) \\
&= \sum\limits_{i = 1} ^ A \sum\limits_{i = 1} ^ B \sum\limits_{i = 1} ^ C ijk \sum\limits_{x \mid (i, j)} g \times \mu(x) \sum\limits_{y \mid (j, k)} g \times \mu(y) \sum\limits_{z \mid (k, i)} g \times \mu(z) \\
&= \sum\limits_{x = 1} ^ A \sum\limits_{y = 1} ^ B \sum\limits_{z = 1} ^ C h(x) h(y) h(z) \sum\limits_{x, z \mid i} i \sum\limits_{x, y \mid j} j \sum\limits_{y, z \mid k} k \\
&= \sum\limits_{x = 1} ^ A \sum\limits_{y = 1} ^ B \sum\limits_{z = 1} ^ C h(x) h(y) h(z) \sum\limits_{i = 1} ^ {A / \mathrm{lcm}(x, z)} i \times \mathrm{lcm}(x, z) \sum\limits_{j = 1} ^ {B / \mathrm{lcm}(x, y)} j \times \mathrm{lcm}(x, y) \sum\limits_{k = 1} ^ {C / \mathrm{lcm}(y, z)} k \times \mathrm{lcm}(y, z) \\
&= \sum\limits_{x = 1} ^ A \sum\limits_{y = 1} ^ B \sum\limits_{z = 1} ^ C h(x) h(y) h(z) S(A, \mathrm{lcm}(x, z)) S(B, \mathrm{lcm}(x, y)) S(C, \mathrm{lcm}(y, z))
\end{aligned}
\]

可以发现，后者 \(x \rightarrow y \rightarrow z \rightarrow x\) 构成了一个三元环，我们可以大概给出估界为 \(\mathcal{O(n \log n \log \log n)}\)。 因此暴力找出所有三元环的复杂度为：\(\mathcal{O(n \log n \log \log n\sqrt{n \log n \log \log n})}\)。

同时，因为这个在 \(n = 5000\) 时与 \(n^{2}\) 无区别，因此连边可以使用暴力。但也可以枚举 \(\mathrm{Lcm}\) 再枚举其约数，使用 \(\mathcal{O(n \log^{3n})}\) 连边。

此时我们算完了 \(F\)，可知总共需要算的 \(F\) 只有 \(\sqrt{n}\) 种，若将单次复杂度看作 \(n^{2}\)，因此总复杂度：

\[
\mathcal{O(n ^ 2\sum\limits_{i = 1} ^ {n} \frac{1}{i ^ 2})} = O(n ^ 2)
\]

经过卡常之后，效率提升大约五倍多，以下是如何卡常的：

我写了一个大范围内的打表程序，发现实际原做法的连边数量大约是 \(n \log n \log \log n\) 级别的，因此这个做法很有卡常前途。

- 我们把暴力连边换掉，枚举其约数，使用 \(\mathcal{O(n \log^{3n})}\) 连边。连边暴力判断时不要求 \(\rm lcm\) 只需要求 \(\gcd(i / d_{j}, i / d_{k})\) 具体参见代码。如果你想要过本题，是一定要优化连边的。
- 可以发现我们需要调用的 \(\rm lcm\) 只有每条边的两个端点，而在枚举 \(\rm Lcm\) 时是可以 \(\mathcal{O(1)}\) 得知的，因此我们在连边时记录这个值。
- 可以发现，\(S\) 函数有很多是无用的，有用的第一维只有 \(\sqrt{A}\) 个，因此可以只预处理 \(A \sqrt{A}\) 个值。
- \(\gcd\) 请不要暴力求，我们记忆化 \(a, b \leqslant 2e4\) 的部分，并用 \(\rm short\) 类型存储，减少空间消耗。

**然后我们再给出一个复杂度为 \(\Theta(n^{1.5})\) 的正解做法。**

方便起见用 \((x, y)\) 代指 \(\operatorname{gcd}(x, y)\)

\[
\sum_{i=1}^{A} \sum_{j=1}^{B} \sum_{k=1}^{C} \frac{(i, j, k) i j k}{(i, j)(j, k)(i, k)}
\]

枚举 \(d\), 设 \(F(A, B, C)=\sum_{i=1}^{A} \sum_{j=1}^{B} \sum_{k=1}^{C} \frac{i j k}{(i, j)(j, k)(i, k)}\) 考虑计算:

\[
\sum_{d} \varphi(d) F\left(\frac{A}{d}, \frac{B}{d}, \frac{C}{d}\right)
\]

令 \(n=\max (A, B, C)\), 假定我们可以在 \(\mathcal{O}\left(n^{c} \log^{k} n\right)\) 的复杂度计算一组 \(F(A, B, C)\), 则当 \(c\gt 1\) 时，恒有 \(\sum \frac{1}{d^{c}}\) 是收敛的，可以认为其为常数。（不过比较大）

只需要考虑快速计算一组 \(F(A, B, C)\), \(\rm remoon\) 给出的做法是同时反演三组，然后考虑通过三元环计数来计算答案，这里给出略为不同的思路:

\[
\begin{aligned}
&F(A, B, C)=\sum_{i=1}^{A} \sum_{j=1}^{B} \sum_{k=1}^{C} \frac{i j k}{(i, j)(j, k)(i, k)} \\
&=\sum_{k} k \sum_{d}(f * \mu)(d) \sum_{d \mid i}^{A} \frac{i}{\operatorname{gcd}(i, k)} \sum_{d \mid j}^{B} \frac{j}{\operatorname{gcd}(j, k)} \\
&=\sum_{k} k \sum_{d}(f * \mu)(d) \frac{d^{2}}{\operatorname{gcd}(k, d)^{2}}\left(\sum_{i=1}^{A / d} \frac{i}{\operatorname{gcd}\left(i, \frac{k}{\operatorname{gcd}(k, d)}\right)}\right)\left(\sum_{i=1}^{B / d} \frac{i}{\operatorname{gcd}\left(i, \frac{k}{\operatorname{gcd}(k, d)}\right)}\right)
\end{aligned}
\]

不妨设 \(F(t, x)=\sum_{i \leq t} \frac{i}{\operatorname{gcd}(i, x)}\), 记 \(g(d)=(f * \mu)(d) d^{2}\)。

答案等价于：

\[
\sum_{k}^{C} k \sum_{d} \frac{g(d)}{\operatorname{gcd}(k, d)^{2}} F\left(\frac{A}{d}, \frac{k}{\operatorname{gcd}(k, d)}\right) F\left(\frac{B}{d}, \frac{k}{\operatorname{gcd}(k, d)}\right)
\]

枚举 \(\frac{k}{\operatorname{gcd}(k, d)}\) 为 \(x\), 此时考虑到我们只需要计算 \(\mathcal{O}(n \sqrt{n})\) 组 \(F(n, x)\)。

考虑到 \(F(n, x)\) 事实上就是:

\[
\begin{aligned}
&\sum_{i=1}^{n} \frac{i}{\operatorname{gcd}(i, x)} \\
&=\sum_{d \mid x}(f * \mu)(d) \times d S\left(\frac{n}{d}\right)
\end{aligned}
\]

枚举这 \(\sqrt{A}\) 种 \(n\), 可以发现后式就是一个高维前缀和的形式，可以在 \(\mathcal{O}\left(n^{1.5} \log \log n \sim n^{1.5} \log n\right)\) 的复杂度完成计算。 考虑前半部分，不妨枚举 \(d, \operatorname{gcd}(k, d)\) （设为 \(t\) ) 以及 \(x\), 此时我们知道:

- \(k=x t\), 故 \(x t \leq C\)
- \(t \mid d\)
- \(\operatorname{gcd}\left(\frac{d}{t}, x\right)=1\)
- 固定了 \(\frac{A}{d}, \frac{B}{d}\) 之后，我们可以发现 \(d\) 属于区间 \([l, r]\), 此时我们考虑将答案差分，简而言之，我们的任务是计算 \(n \sqrt{n}\) 次下式:

    \[
    \begin{aligned}
    &x \sum_{d \leq R} g(d) \sum_{t \mid d} \frac{1}{t}[x t \leq C]\left[\operatorname{gcd}\left(x, \frac{d}{t}\right)=1\right] \\
    &=x \sum_{c \mid x} \mu(c) \sum_{c \mid d, d \leq R} g(d) \sum_{t \mid \frac{d}{\epsilon}} \frac{1}{t}\left[t \leq \frac{C}{x}\right]
    \end{aligned}
    \]

首先，我们不难考虑到本质不同的 \(\frac{C}{x}\) 只有 \(\sqrt{n}\) 种，可以考虑枚举每种 \(\frac{C}{x}=m\) ，并在此时预处理:

\[
g(d) \sum_{t \mid d} \frac{1}{t}[t \leq m]
\]

对于某个 \(m\) ，这可以在 \(\mathcal{O}(n \log \log n)\) 的复杂度完成计算，总体而言，此部分可以在 \(\mathcal{O}\left(n^{1.5} \log \log n \sim n^{1.5} \log n\right)\) 完成预处理，设其为 \(G\left(d, \frac{C}{x}\right)\)。

最后，让我们为每个 \(c\) 考虑，穷举可能的 \(\sqrt{n}\) 种 \(m\) ，并为每个 \(c\) 建立大小为 \(\frac{\max R}{c}\) 的表格，显然表格的总大小为 \(n \log n\), 此时单组查询显然可以做到 \(\mathcal{O}(1)\), 由于 \(x\) 穷举 \(1 \sim n\) ，考察其约数个数和显然为 \(\mathcal{O}(n \log n)\), 总体而言我们可以在 \(\mathcal{O}\left(n^{1.5} \log n\right)\) 解决此问题。

一点新的思路:

我们考虑枚举 \(c\), 并为每个 \(c\), 对 \(\frac{C / c}{x}\) 的所有可能的取值进行预处理，不难发现这个部分的复杂度为 \(\sum\left(\frac{n}{c}\right)^{1.5}\)。

通过积分不难证明这部分等效于 \(n^{1.5}\)。

## 莫比乌斯反演

### 一些定义和性质

**\(\rm Dirichlet\) 卷积 :** \(\sum\limits_{d|n}f(d)g(\frac{n}{d})\) 被定义为 \(\rm Dirichlet\) 卷积。

**莫比乌斯 \((\mu)\) 函数 :**

\[
\mu(n)=
\begin{cases}
1 & n=1 \\
0 & n \text{ 含有平方因子 } \\
(-1)^k & k \text{ 为 } n \text{ 的本质不同质因子个数 }
\end{cases}
\]

显然，\(\mu\) 是积性函数，且它还有一些更加巧妙的性质，其中最常用的一个是 \(\mu \times 1=\varepsilon\)。

\(\large\rm Proof:\)

此处的乘号表示 \(\rm Dirichlet\) 卷积，\(1\) 表示常数函数 \(\forall x\in [1,+\infty),f(x)=1\)，\(\varepsilon\) 表示单位函数 \(\forall x\in [1,+\infty),f(x)=[x=1]\)。

设 \(n=\prod_{i=1}^{k} p_{i}^{c_{i}}, n^{\prime}=\prod_{i=1}^{k} p_{i}\)。

那么 \(\sum\limits_{d \mid n} \mu(d)=\sum\limits_{d \mid n^{\prime}} \mu(d)=\sum\limits_{i=0}^{k}\tbinom{k}{i}\cdot(-1)^{i}=(1+(-1))^{k}\)。

根据二项式定理，易知该式子的值在 \(k=0\) 即 \(n=1\) 时值为 \(1\) 否则为 \(0\)，这也同时证明了 \(\sum\limits_{d \mid n} \mu(d)=[n=1]=\varepsilon(n)\) 以及 \(\mu * 1=\varepsilon\)。

### 两个反演式子

\[
[n=1]=\sum_{d|n}\mu(d)
\]

\(\large\rm Proof:\)

\[
[n=1]=\varepsilon(n)=\mu \times 1(n)=\sum_{d|n}\mu(d)
\]

**我们来看看这个式子有什么应用：**

[**例题 :**](http://zhengruioi.com/contest/1010/problem/2017) 给定一个长度为 \(n\) 的序列 \(a\)，给定 \(m\) 个询问 \(l,r,x\)，求 \(a_{l},a_{l+1}......a_{r}\) 中有多少个数与 \(x\) 互质。

保证 \(n,m,a_{i},x\leqslant 10^{5}\)。

考虑莫比乌斯反演: \(\left[\left(a_{i}, x\right)=1\right]=\sum\limits_{\left.d \mid a_{i}, x\right)} \mu(d)=\sum\limits_{d\left|a_{i}, d\right| x} \mu(d)\)。

由于答案求 \(\sum\limits_{i=l}^{r}\left[\left(a_{i}, x\right)=1\right]=\sum\limits_{i=l}^{r} \sum\limits_{d\left|a_{i}, d\right| x} \mu(d)=\sum\limits_{d \mid x} \mu(d) \sum\limits_{i=l}^{r}\left[d \mid a_{i}\right]_{\text {.}}\)

考虑对于每一个数, 预处理出它的倍数出现在哪些位置, 然后询问时枚举所有 \(x\) 的因数, 二分一下即可求出 \([l, r]\) 内它的倍数有多少个。时间复杂度 \(\Theta(n \sigma(\operatorname{maxa}) \log n)\)。

考虑对上述算法进行优化 ：

- 我们可以只考虑 \(\mu\) 值不等于 \(0\) 的因数。
- 考虑预处理出小于 \(\sqrt{maxa}\) 的所有因数的前缀和，这样对于这些因数的询问是 \(\Theta(1)\) 的。
- 考虑我们相当于要求 \(q\) 个询问不大于 \(x\) 的为某个数的倍数的方案数。先将这些点排个序，然后就可以直接 \(\rm two\ pointers\) 求。时间复杂度可以降到 \(\Theta(n\sigma(maxa))\)。

三者实现其一即可通过本题。

\[
f(n)=\sum_{d|n}g(d)\iff g(n)=\sum_{d|n}\mu(d)f\left(\frac{n}{d}\right)
\]

\(\large\rm Proof:\)

\[
\because f=g\times I
\]

\[
\therefore f\times \mu=g\times I \times \mu
\]

\[
\therefore f\times \mu=g\times \varepsilon = g
\]

**我们来看看这个式子有什么应用：**

[**\(\rm [HAOI2011]Problem\ B\) :**](https://www.luogu.com.cn/problem/P2522) 给出 \(n\) 个询问，每个询问给定 \(5\) 个整数 \(a,b,c,d,k\)，求 ：

\[
\sum_{i=a}^{b}\sum_{j=c}^d[\gcd(i,j)=k]
\]

保证 \(n,a,b,c,d,k\leqslant 5\times 10^{4}\)。

根据容斥原理, 原式可以分成 \(4\) 块来处理，每一块的式子都形如 ：

\[
\sum_{i=1}^{n} \sum_{j=1}^{m}[\operatorname{gcd}(i, j)=k]
\]

考虑化简该式子 ：

\[
\sum_{i=1}^{\left\lfloor\frac{n}{k}\right\rfloor} \sum_{j=1}^{\left\lfloor\frac{m}{k}\right\rfloor}[\operatorname{gcd}(i, j)=1]
\]

因为 \(\operatorname{gcd}(i, j)=1\) 时对答案才有贡献，于是我们可以将其替换为 \(\varepsilon(\operatorname{gcd}(i, j))\)，故原式化为 ：

\[
\sum_{i=1}^{\left\lfloor\frac{n}{k}\right\rfloor} \sum_{j=1}^{\left\lfloor\frac{m}{k}\right\rfloor} \varepsilon(\operatorname{gcd}(i, j))
\]

将 \(\varepsilon\) 函数展开得到 ：

\[
\sum_{i=1}^{\left\lfloor\frac{n}{k}\right\rfloor} \sum_{j=1}^{\left\lfloor\frac{m}{k}\right\rfloor} \sum_{d \mid \operatorname{gcd}(i, j)} \mu(d)
\]

变换求和顺序, 先枚举 \(d \mid \operatorname{gcd}(i, j)\) 可得 ：

\[
\sum_{d=1}^{\min \left(\left\lfloor\frac{n}{k}\right\rfloor,\left\lfloor\frac{m}{k}\right\rfloor\right)} \mu(d) \sum_{i=1}^{\left\lfloor\frac{n}{k}\right\rfloor}[d \mid i] \sum_{j=1}^{\left\lfloor\frac{m}{k}\right\rfloor}[d \mid j]
\]

易知 \(1 \sim\left\lfloor\frac{n}{k}\right\rfloor\) 中 \(d\) 的倍数有 \(\left\lfloor\frac{n}{k d}\right\rfloor\) 个, 故原式化为 ：

\[
\sum_{d=1}^{\min \left(\left\lfloor\frac{n}{k}\right\rfloor,\left\lfloor\frac{m}{k}\right\rfloor\right)} \mu(d)\left\lfloor\frac{n}{k d}\right\rfloor\left\lfloor\frac{m}{k d}\right\rfloor
\]

很显然，式子可以数论分块求解。

时间复杂度 \(\Theta(W+n\sqrt{W})\)。

### 莫比乌斯反演的非卷积形式

对于数论函数 \(f,g\) 和完全积性函数 \(t\)，满足 \(t(1)=1\)，有 ：

\[
f(n)=\sum_{i=1}^nt(i)g\left(\left\lfloor\frac{n}{i}\right\rfloor\right)\ \iff g(n)=\sum_{i=1}^n\mu(i)t(i)f\left(\left\lfloor\frac{n}{i}\right\rfloor\right)
\]

\(\large\rm Proof:\)

\[
\begin{aligned}
g(n) &= \sum_{i=1}^n\mu(i)t(i)f\left(\left\lfloor\frac{n}{i}\right\rfloor\right) \\
&= \sum_{i=1}^n\mu(i)t(i) \sum_{j=1}^{\left\lfloor\frac{n}{i}\right\rfloor}t(j) g\left(\left\lfloor\frac{\left\lfloor\frac{n}{i}\right\rfloor}{j}\right\rfloor\right) \\
&= \sum_{i=1}^n\mu(i)t(i) \sum_{j=1}^{\left\lfloor\frac{n}{i}\right\rfloor}t(j) g\left(\left\lfloor\frac{n}{ij}\right\rfloor\right) \\
&= \sum_{T=1}^n \sum_{i=1}^n\mu(i)t(i) \sum_{j=1}^{\left\lfloor\frac{n}{i}\right\rfloor}[ij=T] t(j)g\left(\left\lfloor\frac{n}{T}\right\rfloor\right) \\
&= \sum_{T=1}^n \sum_{i \mid T}\mu(i)t(i) t\left(\frac{T}{i}\right)g\left(\left\lfloor\frac{n}{T}\right\rfloor\right) \\
&= \sum_{T=1}^n g\left(\left\lfloor\frac{n}{T}\right\rfloor\right) \sum_{i \mid T}\mu(i)t(i)t\left(\frac{T}{i}\right) \\
&= \sum_{T=1}^n g\left(\left\lfloor\frac{n}{T}\right\rfloor\right) \sum_{i \mid T}\mu(i)t(T) \\
&= \sum_{T=1}^n g\left(\left\lfloor\frac{n}{T}\right\rfloor\right)t(T) \sum_{i \mid T}\mu(i) \\
&= \sum_{T=1}^n g\left(\left\lfloor\frac{n}{T}\right\rfloor\right)t(T) \varepsilon(T) \\
&= g(n)t(1) \\
&= g(n)
\end{aligned}
\]
