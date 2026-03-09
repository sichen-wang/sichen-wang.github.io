---
title: "三种曲线方程刻画方式的相互转换"
date: "2025-01-13 20:20:13"
card_summary: ""
slug: "三种曲线方程刻画方式的相互转换"
aliases:
  - "/blog/san-chong-qu-xian-fang-cheng-ke-hua-fang-shi-de-xiang-hu-zhuan-huan/"
tags:
  - "Analytic Geometry"
categories:
  - "Courses"
---

**直角坐标方程**形如 \(y = f(x)\) 或 \(f(x, y) = 0\)，**参数方程**形如
\[
\begin{cases}
x = f(t) \\
y = g(t)
\end{cases}
\]
**极坐标方程**形如 \(\ell = \rho(\theta)\)。

### 直角坐标方程转参数方程
\[
y = f(x) \Longrightarrow
\begin{cases}
x = t \\
y = f(t)
\end{cases}
\]

### 参数方程转直角坐标方程

- 代入法: 直接从 \(x = f(t)\) 解出 \(t = f^{-1}(x)\), 然后将其带入 \(y = g(t)\) 解得 \(x\) 和 \(y\) 关系.
- 三角法: 如果方程涉及三角函数, 则可以利用三角恒等式解出直角坐标方程.
\[
\begin{cases}
x = r \cos t \\
y = r \sin t
\end{cases}
\Longrightarrow
x^2 + y^2 = r^2 (\sin^2 t + \cos^2 t) = r^2
\]

### 极坐标方程转参数方程
\[
\ell = \rho(\theta) \Longrightarrow
\begin{cases}
y = \rho(t) \sin t \\
x = \rho(t) \cos t
\end{cases}
\]

### 参数方程转极坐标方程

注意到在极坐标系中, 点的表示为
\[
\begin{aligned}
\ell &= \sqrt{x^2 + y^2} \\
\theta &= \arctan \frac{y}{x}
\end{aligned}
\]

于是将参数方程带入即可得出 \(\ell, \theta\) 与 \(t\) 的关系, 设 \(\ell = p(t), \theta = \arctan q(t)\), 则
\[
\ell = p \circ q^{-1}(\tan \theta)
\]
