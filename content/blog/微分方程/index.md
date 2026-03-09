---
title: "微分方程"
date: "2025-01-14 00:00:00"
card_summary: ""
slug: "微分方程"
aliases:
  - "/blog/wei-fen-fang-cheng/"
tags:
  - "Differential Equations"
  - "Calculus"
categories:
  - "Courses"
---

## I. 可分离变量的微分方程
\[
\frac{\mathrm{d} y}{\mathrm{d} x} = p(x)q(y)
\]

直接分离变量得
\[
p(x) \mathrm{d} x = \frac{1}{q(y)} \mathrm{d} y
\]

对两边积分即有
\[
\int p(x) \mathrm{d} x = \int \frac{1}{q(y)} \mathrm{d} y
\]

### 齐次微分方程
\[
\frac{\mathrm{d} y}{\mathrm{d} x} = \varphi \left(\frac{y}{x}\right)
\]

设 \(u = \dfrac{y}{x}\), 则有
\[
\frac{\mathrm{d} (u x)}{\mathrm{d} x} = \varphi(u)
\]

整理得
\[
\int \frac{\mathrm{d} u}{\varphi (u) - u} = \int \frac{\mathrm{d} x}{x}
\]

最后将 \(u = \dfrac{y}{x}\) 回代即得原方程的解.

需要注意的是, 求解方程的过程中可能会丢失一些解, 需要考虑一些边界情况.

## II. 一阶线性微分方程
\[
\frac{\mathrm{d} y}{\mathrm{d} x} + p(x) y = q(x) \tag{2.1}
\]

### 齐次方程的通解

> 当 \(q(x) \equiv 0\) 时, 该方程称为一阶齐次线性微分方程, 可求其通解.
\[
\frac{\mathrm{d} y}{\mathrm{d} x} + p(x) y = 0
\]

考虑直接分离变量
\[
\frac{\mathrm{d} y}{y} = -p(x) \mathrm{d} x
\]

两边积分并整理得
\[
y = C \exp\left(-\int p(x) \mathrm{d} x\right)
\]

### 非齐次方程的特解

> 当 \(q(x) \not\equiv 0\) 时, 该方程称为一阶非齐次线性微分方程, 可先求其对应齐次方程的通解, 再求非齐次方程的一个特解, 两者相加即得该非齐次方程的通解.

对式 (2.1) 两边同时除以 \(y\), 并整理得
\[
\frac{\mathrm{d} y}{y} = -p(x) \mathrm{d} x + \frac{q(x)}{y} \mathrm{d} x
\]

两边积分并化简得
\[
y = C \exp\left(-\int p(x) \mathrm{d} x + \int \frac{q(x)}{y} \mathrm{d} x \right)
\]

设 \(c(x) = C \exp\left(\displaystyle \int \frac{q(x)}{y} \mathrm{d} x \right)\), 将其带入即有
\[
y = c(x) \exp(-\int p(x) \mathrm{d} x) \tag{2.2}
\]

将上式带入式 (2.1) 得
\[
c'(x) \exp(-\int p(x) \mathrm{d} x) - c(x) \exp(-\int p(x) \mathrm{d} x) p(x) + p(x) c(x) \exp(-\int p(x) \mathrm{d} x) = q(x)
\]

注意到中间两项是可以消去的, 于是
\[
c'(x) = q(x) \exp(\int p(x) \mathrm{d} x)
\]

两边积分得
\[
c(x) = \int q(x) \exp(\int p(x) \mathrm{d} x) + C
\]

将 \(c(x)\) 的表达式带入式 (2.2) 即得方程 (2.1) 的一个特解(消去 \(C\) 是因为常数项已经在通解中刻画了)
\[
y^{\ast} = \exp(-\int p(x) \mathrm{d} x) \int q(x) \exp(\int p(x) \mathrm{d} x)
\]

结合齐次方程的通解, 则方程 (2.1) 的通解为
\[
y = C \exp\left(-\int p(x) \mathrm{d} x\right) + \exp(-\int p(x) \mathrm{d} x) \int q(x) \exp(\int p(x) \mathrm{d} x)
\]

### 伯努利方程
\[
\frac{\mathrm{d} y}{\mathrm{d} x} + p(x) y = q(x) y^n
\]

两边同时除以 \(y^{n}\) 即得
\[
y^{-n}\frac{\mathrm{d} y}{\mathrm{d} x} + p(x) y^{1-n} = q(x)
\]

设 \(Y = y^{1-n}, P(x) = (1-n)p(x), Q(x) = (1-n)q(x)\), 将两边同乘 \((1-n)\) 即得
\[
\frac{\mathrm{d} Y}{\mathrm{d} x} + P(x) Y = Q(x)
\]

容易套用「一阶线性微分方程」的解法.

## III. 可降阶的高阶微分方程

### 变量分离
\[
y^{(n)} = f(x)
\]

两边同时做 \(n\) 次积分即可, 最后结果形如
\[
y = \int \left(\int \cdots \left(\int f(x) \mathrm{d} x\right) \cdots \mathrm{d} x \right)\mathrm{d} x + C_1 x^{n - 1} + C_2 x_{n - 2} + \cdots + C_n
\]

### 无显式原函数
\[
y'' = f(x, y')
\]

设 \(y' = g(x)\), 则原式化为一阶微分方程
\[
g'(x) = f(x, g(x))
\]

解得
\[
g(x) = \varphi(x, C_1)
\]

积分即得
\[
y = \int g(x) \mathrm{d} x + C = \int \varphi(x, C_1) \mathrm{d} x + C_2
\]

### 无显式自变量
\[
y'' = f(y, y')
\]

设 \(y' = p(y)\), 则
\[
y'' = \frac{\mathrm{d} p}{\mathrm{d} x} = \frac{\mathrm{d} p}{\mathrm{d} y} \frac{\mathrm{d} y}{\mathrm{d} x} = p(y) \frac{\mathrm{d} p}{\mathrm{d} y}
\]

回代得
\[
\frac{\mathrm{d} p}{\mathrm{d} y} = \frac{f(y, p(y))}{p(y)}
\]

设其通解为 \(p(y) = \varphi(y, C_{1})\), 则分离变量后积分可得
\[
\int \frac{\mathrm{d} y}{\varphi(y, C_1)} = x + C_2
\]

## IV. 常系数线性微分方程

研究「常系数线性微分方程」一般以二阶微分方程为主, 形如
\[
y'' + py' + qy = f(x)
\]

### 二阶常系数齐次线性微分方程

对于方程
\[
y'' + py' + qy = 0
\]

注意到 \(\mathrm{e}^{rx}\) 与其导数只差常数因子, 于是设 \(y = \mathrm{e}^{rx}\) 即得
\[
(r^2 + pr + q)\mathrm{e}^{rx} = 0
\]

称 \(r^{2} + pr + q = 0\) 为原方程的「特征方程」, 求出来的根称为「特征根」.

注意到方程的通解可以用两个线性无关的特解的线性组合刻画(此处不加以证明), 于是考虑根据特征根构造两个特解.

当特征方程 \(\Delta \gt 0\) 时, 存在两相异实根 \(r_{1}, r_{2}\), 则该微分方程的通解为
\[
y = C_1\mathrm{e}^{r_1 x} + C_2 \mathrm{e}^{r_2x}
\]

当特征方程 \(\Delta = 0\) 时, 存在两相同实根 \(r_{1} = r_{2}\), 则该微分方程有一个特解 \(y_{1} = \mathrm{e}^{r_{1} x}\).

设另一特解 \(y_{2} = y_{1} u(x) = \mathrm{e}^{r_{1} x}u(x)\), 将其带入方程得
\[
\mathrm{e}^{r_1x}\left( (u''(x) + 2r_1 u'(x) + {r_1}^2 u(x)) + p(u'(x) + r_1 u(x)) + qu(x) \right) = 0
\]

化简得
\[
u''(x) + (2r_1 + p)u'(x) + ({r_1}^2 + pr_1 + q) u(x) = 0
\]

由于 \(r_{1} = -\dfrac{p}{2}\) 且其为方程 \({r_{1}}^{2} + pr_{1} + q = 0\) 的根, 于是解得
\[
u''(x) = 0
\]

取 \(u(x) = x\) 即得特解 \(y_{2} = x \mathrm{e}^{r_{1} x}\), 结合特解 \(y_{1}\) 即有原方程通解
\[
y = \left( C_1 + C_2 x \right) \mathrm{e}^{r_1 x}
\]

当特征方程 \(\Delta \lt 0\) 时, 存在一对共轭复根 \(r_{1} = \alpha + i\beta, r_{2} = \alpha - i \beta\).

此时原方程有两个解
\[
y = \exp \left( (\alpha \pm i\beta) x \right)
\]

运用欧拉公式 \(\mathrm{e}^{i \theta} = \cos\theta + i\sin \theta\) 得到
\[
y = \mathrm{e}^{\alpha x} \left( \cos \beta x \pm i \sin \beta x \right)
\]

通过线性组合构造两个线性无关的解
\[
\begin{aligned}
y_1 &= \frac{1}{2} \sum y = \mathrm{e}^{\alpha x} \cos \beta x \\
y_2 &= \frac{1}{2i} \Delta y = \mathrm{e}^{\alpha x} \sin \beta x
\end{aligned}
\]

于是原方程的通解为
\[
y = \mathrm{e}^{\alpha x} \left( C_1 \cos \beta x + C_2 \sin \beta x \right)
\]

以上结论均可推广到高阶情形.

### 二阶常系数非齐次线性微分方程

对形如下式的微分方程
\[
y'' + py' + qy = \mathrm{e}^{\lambda x} f(x)
\]

根据前面的经验, 我们只需要求出该方程的一个特解.

设特解 \(y^{\ast} = \mathrm{e}^{\lambda x} g(x)\), 则有
\[
\begin{aligned}
\left(y^{\ast}\right)^{\prime} &= \mathrm{e}^{\lambda x} (\lambda g(x) + g'(x)) \\
\left(y^{\ast}\right)^{\prime\prime} &= \mathrm{e}^{\lambda x} (\lambda^2 g(x) + 2\lambda g'(x) + g''(x))
\end{aligned}
\]

带入原方程并化简得
\[
g''(x) + (2\lambda + p) g'(x) + (\lambda^2 + p\lambda + q) g(x) = f(x) \tag{4.1}
\]

注意到当 \(\lambda\) 分别为特征方程的 \(k = 0, 1, 2\) 重根的时候, \(g(x)\) 和 \(g'(x)\) 对应项会依次变为 \(0\). 这意味着当 \(k\) 取 \(0, 1, 2\) 时, \(g(x), g'(x)\) 和 \(g''(x)\) 需要分别为与 \(f(x)\) 同次数的多项式, 于是不妨设 \(r(x)\) 为与 \(f(x)\) 同次数的待定系数多项式, 特解即为
\[
y^{\ast} = g(x)\mathrm{e}^{\lambda x} = x^k r(x)\mathrm{e}^{\lambda x}
\]

将其带入式 (4.1) 中即可算出 \(r(x)\) 的各系数, 进而得到方程的一个特解.

对形如下式的微分方程
\[
y'' + py' + qy = \mathrm{e}^{\lambda x} \left( f(x) \cos \omega x + g(x) \sin \omega x \right)
\]

应用欧拉公式将等式右侧化为
\[
\begin{aligned}
h(x) &= \mathrm{e}^{\lambda x} \left( f(x) \cos \omega x + g(x) \sin \omega x \right) \\
&= \mathrm{e}^{\lambda x} \left( f(x) \frac{\mathrm{e}^{\omega x i} + \mathrm{e}^{-\omega x i}}{2} + g(x) \frac{\mathrm{e}^{\omega x i} - \mathrm{e}^{-\omega x i}}{2i} \right) \\
&= \left( \frac{f(x)}{2} + \frac{g(x)}{2i} \right) \mathrm{e}^{(\lambda + \omega i) x} + \left( \frac{f(x)}{2} - \frac{g(x)}{2i} \right) \mathrm{e}^{(\lambda - \omega i) x} \\
&= h_1(x) \mathrm{e}^{(\lambda + \omega i) x} + h_2(x) \mathrm{e}^{(\lambda - \omega i) x}
\end{aligned}
\]

其中 \(h_{1}(x)\) 和 \(h_{2}(x)\) 为从 \(f(x)\) 和 \(g(x)\) 线性组合得到的函数, 且对应项系数共轭.

设 \(\lambda  + \omega i\) 是特征方程的 \(k\) 重根(\(k = 0, 1\)), 则方程
\[
y'' + py' + qy = h_1(x) \mathrm{e}^{(\lambda + \omega i) x}
\]

有特解
\[
{y_1}^{\ast} = x^k r(x) \mathrm{e}^{(\lambda + \omega i) x} \tag{4.2}
\]

设 \(m\) 为 \(f(x), g(x)\) 中次数较大者的次数, \(r(x)\) 是待定系数的 \(m\) 次多项式. 对式 (4.2) 两边取共轭即得
\[
\left({y_1}^{\ast}\right)^{\prime\prime} + p\left({y_1}^{\ast}\right)^{\prime} + q({y_1}^{\ast}) \equiv h_1(x) \mathrm{e}^{(\lambda + \omega i) x} = h_2(x) \mathrm{e}^{(\lambda - \omega i) x}
\]

因此 \({y_{2}}^{\ast} = ({y_{1}}^{\ast})\) 为以下方程的特解
\[
y'' + py' + qy = h_2(x) \mathrm{e}^{(\lambda - \omega i) x}
\]

于是原方程的特解可以用两部分的特解之和来刻画, 即
\[
\begin{aligned}
y^{\ast} &= {y_1}^{\ast} + {y_2}^{\ast} \\
&= x^k \mathrm{e}^{\lambda x} \left( r(x) \mathrm{e}^{i\omega x} + (r(x))\mathrm{e}^{-i\omega x}  \right) \\
&= x^k \mathrm{e}^{\lambda x} \left( r_1(x) \cos \omega x + r_2(x) \sin \omega x \right)
\end{aligned}
\]

从上述推到中我们可以发现 \(y^{\ast}\) 实则是个实函数, 于是 \(r_{1}\) 和 \(r_{2}\) 也均为 \(m\) 次实多项式.

综上, 对于微分方程
\[
y'' + py' + qy = \mathrm{e}^{\lambda x} \left( f(x) \cos \omega x + g(x) \sin \omega x \right)
\]

可以设特解为
\[
y^{\ast} = x^k \mathrm{e}^{\lambda x} \left( r_1(x) \cos \omega x + r_2(x) \sin \omega x \right)
\]

然后代入原方程解出待定系数. 该结论也可推广到高阶形式.
