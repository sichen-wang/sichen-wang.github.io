---
title: "线性筛"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "线性筛"
aliases:
  - "/blog/xian-xing-shai/"
tags:
  - "Number Theory"
  - "Sieve"
categories:
  - "CP"
---

## 筛素数

考虑如何筛出 \(n\) 以内的所有素数，显然有一个最简单的想法，即将所有已求出的质数的倍数标记，表示它们不为质数，并且从小到大遍历到数 \(i\) 时，若它没有被标记，则 \(i\in Prime\)。 在此算法中，每个数都被自己所有本质不同的质因子筛了一次，所以总复杂度为 \(\Theta(n\ln \ln n)\)。

对于上面的算法，算力的浪费主要在于很多数被多个质数筛过，我们考虑让每个数都只被自己的最小质因子筛。当遍历到 \(i\) 时，枚举已经筛出来的所有质数，若当前枚举的质数为 \(p_{j}\)，显然 \(i\times p_{j}\) 不为质数。另一方面，若 \(p_{j}|i\)，则 \(i\) 中有一个质因子 \(p_{j}\)，那么后面枚举到 \(p_{j+1}\) 的时候，\(p_{j+1}\) 就一定不是 \(i\times p_{j+1}\) 的最小质因子，所以此时要停止枚举质数。这样，每个数都只被自己的最小质因子筛过，所以总复杂度为 \(\Theta(n)\)。

```cpp
for (int i = 2; i <= n; i++) {
    if (!vis[i]) p[++cnt] = i;
    for (int j = 1; j <= cnt && i * p[j] <= n; j++) {
        vis[i * p[j]] = true;
        if (i % p[j] == 0) break;
    }
}
```

## 筛欧拉函数

考虑到 \(\varphi\) 函数有如下性质：

\[
\begin{cases}
\varphi(p) = p - 1 & p \in Prime \\
\varphi(ap) = \varphi(a) \times p & p \in Prime \\
\varphi(ab) = \varphi(a) \times \varphi(b) & \gcd(a, b) = 1
\end{cases}
\]

- 对于 \(\varphi(p),p\in Prime\)，直接在筛出质数的同时求解即可。
- 对于 \(\varphi(ap),p\in Prime\)，在 \(p_{j}|i\) 时，\(\varphi(i\times p_{j})=\varphi(i)\times p_{j}\)。
- 对于 \(\varphi(ab),\gcd(a,b)=1\)，直接在筛去合数的时候 \(\varphi(i\times p_{j})=\varphi(i)\times \varphi(p_{j})\)。

```cpp
for (int i = 2; i <= n; i++) {
    if (!vis[i]) p[++cnt] = i, phi[i] = i - 1;
    for (int j = 1; j <= cnt && i * p[j] <= n; j++) {
        vis[i * p[j]] = true;
        if (i % p[j] == 0) {
            phi[i * p[j]] = phi[i] * p[j];
            break;
        }
        phi[i * p[j]] = phi[i] * phi[p[j]];
    }
}
```

## 筛不同质因子的个数

令 \(\alpha(x)\) 表示 \(x\) 不同质因子的个数，\(\beta(x)\) 表示 \(x\) 的所有最小质因子的乘积，考虑到 \(\alpha\) 函数有如下性质：

\[
\begin{cases}
\alpha(p^k) = 1 & p \in Prime \\
\alpha(ab) = \alpha(a) + \alpha(b) & \gcd(a, b) = 1 \\
\alpha(ap) = \alpha\left(\frac{a}{\beta(a)}\right) + 1 & p \text{ 为 } a \text{ 的最小质因子}
\end{cases}
\]

于是用与筛欧拉函数相似的方法：

```cpp
for (int i = 2; i <= n; i++) {
    if (!vis[i]) p[++cnt] = g[i]= i, f[i] = 1;
    for (int j = 1; j <= cnt && i * p[j] < N; j++) {
    vis[i * p[j]] = true;
    if (i % p[j] == 0) {
        g[i * p[j]] = g[i] * p[j];
        f[i * p[j]] = f[i / g[i]] + 1;
        break;
    }
    g[i * p[j]] = p[j];
    f[i * p[j]] = f[i] + 1;
    }
}
```
