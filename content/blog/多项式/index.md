---
title: "多项式"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "多项式"
aliases:
  - "/blog/duo-xiang-shi/"
tags:
  - "Polynomials"
  - "NTT"
categories:
  - "CP"
---

## 拉格朗日插值

插值问题形如 ：给定 \(n\) 个点的坐标 \((x, y)\)，要求出一个经过所有点的最低次多项式。

### 一般插值

容易构造出 \(f(x)\) 即为下式 ：

\[
f(x) = \sum _{i = 1} ^{n} y_i \prod _{j \not= i} \frac{x - x_j}{x_i - x_j}\tag{1.1.1}
\]

正确性显然。

容易证明多项式次数至少为 \(n - 1\) 才可以确保穿过 \(n\) 个点，故最优性得证。

时间复杂度 \(\Theta(n^{2})\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 2e3 + 10, mod = 998244353;

int n, k, x[N], y[N], ans;

int Pow (int a, int k) {
    int res = 1;
    for ( ; k; a = 1ll * a * a % mod, k >>= 1)
        if(k & 1) res = 1ll * res * a % mod;
    return res;
}

int main () {

    scanf("%d%d", &n, &k);
    rep(i, 1, n) scanf("%d%d", &x[i], &y[i]);

    rep(i, 1, n) {
        int S1 = 1, S2 = 1;
        rep(j, 1, n) if (j != i) {
            S1 = 1ll * S1 * (k - x[j]) % mod;
            S2 = 1ll * S2 * (x[i] - x[j]) % mod;
        }
        ans = (ans + 1ll * y[i] * S1 % mod * Pow(S2, mod - 2)) % mod;
    }

    printf("%d\n", (ans + mod) % mod);

    return 0;
}
```

### 点值连续的插值

当给定的点值连续时，式子可以改写为 ：

\[
\begin{aligned}
    f(x) = \sum _{i = 1} ^{n} y_i \prod _{j \not= i} \frac{x - j}{i - j} = \sum _{i = 1} ^{n} y_i \frac{\prod \limits _{j \not= i}(x - j)}{\prod \limits_{j \not= i}(i - j)}
\end{aligned}
\]

考虑计算分子，记 \(pre_{i} = \prod_{j = 1}^{i} (x - j), suf_{i} = \prod_{j = i}^{n} (x - j)\)，显然 \(\prod_{j \not= i}(x - j) = pre_{i - 1}\times suf_{i + 1}\)。

考虑计算分母，记 \(sym(x) = 1 - 2[x \equiv 1 \pmod 2]\)，显然 \(\prod_{j \not= i}(i - j) = (i - 1)!\times sym(n - i)(n - i)!\)。

全部带入可将式 \((1.2.1)\) 改写为 ：

\[
f(x) = \sum _{i = 1} ^n y_i \frac{pre_{i - 1}\times suf_{i + 1}}{(i - 1)!\times sym(n - i)(n - i)!} \tag{1.2.2}
\]

时间复杂度 \(\Theta(n)\)。

```cpp
int F (int n, int k) {
    fac[0] = 1;
    rep(i, 1, k + 2) fac[i] = fac[i - 1] * i % mod;
    inv[k + 2] = Pow(fac[k + 2], mod - 2);
    dep(i, k + 1, 0) inv[i] = inv[i + 1] * (i + 1) % mod;

    pre[0] = suf[k + 3] = 1;
    rep(i, 1, k + 2) pre[i] = pre[i - 1] * (n - i) % mod;
    dep(i, k + 2, 1) suf[i] = suf[i + 1] * (n - i) % mod;
    rep(i, 1, k + 2) y[i] = (y[i - 1] + Pow(i, k)) % mod;

    int res = 0;
    rep(i, 1, k + 2) res = (res + y[i] * pre[i - 1] % mod * suf[i + 1] % mod * inv[i - 1] % mod * inv[k + 2 - i] * (((k + 2 - i) & 1) ? -1 : 1)) % mod;
    return (res + mod) % mod;
}
```

### 重心拉格朗日插值法

考虑一般插值的优化。

观察式 \((1.1.1)\)，设 :

\[
G = \prod _{i = 1} ^n (x - x_i) \tag{1.3.1}
\]

\[
T_i = \frac{y_i}{\prod \limits_{j \not= i} (x_i - x_j)} \tag{1.3.2}
\]

将式 \((1.3.1)\) 和 \((1.3.2)\) 带入式 \((1.1.1)\) 可得 ：

\[
f(x) = G \sum _{i = 1} ^{n} \frac{T_i}{x - x_i} \tag{1.3.3}
\]

如此一来，新加入一个点就只需要计算它的 \(T\) 值了，时间复杂度为 \(\Theta(n)\)。

### 还原插值多项式的系数

考虑对式 \((1.1.1)\) 作变形 ：

\[
f(x) = \sum _{i = 1} ^{n} \frac{y_i}{\prod \limits_{j \not= i}(x_i - x_j)} \prod _{j \not= i} (x - x_j)\tag{1.4.1}
\]

可以 \(\Theta(n^{2})\) 预处理 \(\prod_{i = 1}^{n} (x - x_{i})\)，然后在需要求 \(\prod_{j \not= i} (x - x_{j})\) 时将预处理出的多项式除以 \((x - x_{i})\) ，可以做到单次 \(\Theta(n)\) 的时间复杂度。

还原插值多项式系数的时间复杂度为 \(\Theta(n^{2})\)。

### 自然数幂前缀和

有定理：不大于 \(n\) 的自然数 \(k\) 次幂和是一个关于 \(n\) 的 \(k + 1\) 次多项式。

\(\rm Proof :\)

设 \(f_{k}(n) = \sum \limits_{i = 1}^{n} i^{k}\)。

当 \(k = 1\) 时，\(f_{k}(n) = \sum \limits_{i = 1}^{n} i = \frac{1}{2}n^{2} + \frac{1}{2} n\)，是一个 \(k + 1\) 次多项式。

假设 \(f_{k - 1}(n)\) 是一个关于 \(n\) 的 \(k\) 次多项式。

即 \(f_{k - 1}(n) = a_{0} + a_{1} n + a_{2} n^{2} + \cdots + a_{k} n^{k}\)。

\[
\begin{aligned}
    f_k(n) &= \sum _{i = 1} ^n i\times i ^ {k - 1}\\
    &= \sum _{i = 0} ^{n - 1} f_{k - 1}(n) - f_{k - 1}(i)\\
    &= nf_{k - 1}(n) - \sum _{i = 1} ^{n - 1} f_{k - 1}(i)\\
    &= a_0 n + a_1 n ^ 2 + \cdots + a_k n ^ {k + 1} - \sum _{i = 1} ^{n - 1} f_{k - 1}(i)
\end{aligned}
\]

容易发现，由于 \(f_{k - 1}(i)\) 中次数最高的项为 \(k\) 次项，并且 \(f_{k}(n)\) 中含有关于 \(n\) 的 \(k + 1\) 次项，所以 \(f_{k}(n)\) 是关于 \(n\) 的 \(k + 1\) 次多项式。

归纳可得 ：\(\forall k\geqslant 1,\ f_{k}(n)\) 是关于 \(n\) 的 \(k\) 次多项式。

于是可以使用点值连续的拉格朗日插值计算 \(\sum \limits_{i = 1}^{n} i^{k}\)，时间复杂度 \(\Theta(k)\)。

## 快速傅里叶变换

快速傅里叶变换 \(\rm(Fast\ Fourier\ Transformation,FFT)\) 被用来在 \(\Theta(n\log n)\) 的时间复杂度下求两个多项式的乘积（和卷积）。

若称 \(h(x) = f(x) \times g(x)\)，则应满足关系式 ：

\[
h(k) = \sum _{i + j = k} f(i) \times g(j) \tag{2.0.1}
\]

### 单位根

众所周知，有欧拉公式 ：

\[
e^{i\theta} = \cos \theta + i\sin \theta \tag{2.1.1}
\]

根据高中课本上所讲的，我们知道任意一个复数可以被表示成 \(r(\cos \theta + i\sin \theta)\) 的形式，根据式 \((2.1.1)\)，可以发现其等价于 \(r \cdot e^{i\theta}\)，所以两个复数相乘，模长 \((r)\) 相乘，幅角 \((\theta)\) 相加。

考虑方程 \(x^{n} = 1\)，容易发现它在复数域内有 \(n\) 个解，解集为 \(\{e^{i\theta} \mid \theta = \frac{2k\pi}{n},k = 0,1,2, \cdots, n - 1 \}\)，将其简记为 \(\omega_{n}^{0},\omega_{n}^{1},\cdots,\omega_{n}^{n - 1}\)，进一步观察可以发现，它们是复平面中单位圆上的 \(n\) 等分点。

之所以会在 \(\rm FFT\) 中用到单位根，主要是因为它具有以下性质 ：

**折半性质 ：**

\[
\omega_{2n} ^ {2k} = \omega _n ^k \tag{2.1.2}
\]

\(\rm Proof :\) 显然有 \(\omega_{n}^{k} = (\omega_{n}^{1})^{k}\) 和 \(\omega_{n}^{1} = \omega_{2n}^{2}\)。

**对称性质 ：**

\[
\omega _{2n} ^ {k + n} = -\omega _{2n} ^{k} \tag{2.1.3}
\]

\(\rm Proof :\) 这里定义 \(-z\) 为 \(z\) 关于原点的对称点，显然有 \(\omega_{2n}^{n} = -1\)，\(\omega_{2n}^{k + n} = \omega_{2n}^{k}\times \omega_{2n}^{n} = -\omega_{2n}^{k}\)。

**求和性质** ：

\[
\sum _{i = 0} ^{n - 1} \left(\omega_{n} ^k\right) ^i = n[k = 0] \tag{2.1.4}
\]

\(\rm Proof :\)

首先使用等比数列求和公式 ：

\[
\sum _{i = 0} ^{n - 1} \left(\omega_{n} ^k\right) ^i = \frac{1 - \left(\omega_{n} ^k\right)^n}{1 - \omega_n^k} \tag{2.1.5}
\]

考虑分类讨论 ：

- 当 \(k = 0\) 时，原式显然等于 \(n\)。
- 当 \(k \not = 0\) 时，\(1 - \omega_{n}^{k} \not = 0\)，\(1 - \left(\omega_{n}^{k}\right)^{n} = 0\)，故原式等于 \(0\)。

### 离散傅里叶变换

离散傅里叶变换 \(\rm(Discrete\ Fourier\ Transform,DFT)\) 被用于求出多项式的 \(n\) 个点值，其中 \(n\) 为多项式的项数，\(\rm DFT\) 是 \(\rm FFT\) 的前半部分。

对于一个多项式 \(F(x) = a_{0} + a_{1} x + a_{2} x^{2} + \cdots + a_{n - 1} x^{n - 1}\)，不妨设 ：

\[
\begin{aligned}
    F_1(x) = a_0 + a_2x + a_4x^2 + \cdots + a_{n - 2}x^{\frac{n}{2} - 1}\\
    F_2(x) = a_1 + a_3x + a_5x^2 + \cdots + a_{n - 1}x^{\frac{n}{2} - 1}
\end{aligned}
\]

于是有 \(F(x) = F_{1}(x^{2}) + xF_{2}(x^{2})\)。

将 \(\omega_{n}^{k}\) 带入可得 ：

\[
F(\omega_n^k) = F_1(\omega_n^{2k}) + \omega_n^k F_2(\omega_n^{2k}) \tag{2.2.1}
\]

根据式 \((2.1.2)\) 可得 ：

\[
F(\omega_n^k) = F_1(\omega_{n/2}^{k}) + \omega_n^k F_2(\omega_{n/2}^{k}) \tag{2.2.2}
\]

考虑分类讨论 ：

对于 \(k \lt \frac{n}{2} \)，只需要直接递归处理 \(F_{1}\) 和 \(F_{2}\) 即可。
对于 \(k \geqslant \frac{n}{2}\)，我们不妨它为 \(k + \frac{n}{2}\ (k \lt \frac{n}{2})\)，于是有 ：

\[
F(\omega_n^{k + n/2}) = F_1(\omega_n^{2k + n}) + \omega_n^{k + n/2} F_2(\omega_n^{2k + n}) \tag{2.2.3}
\]

根据式 \((2.1.2)\) 和 \((2.1.3)\) 可得 ：

\[
F(\omega _ n ^ k) = F_1(\omega_{n / 2} ^ k) - \omega _ n ^ k F_2(\omega_{n/2}^k) \tag{2.2.4}
\]

观察发现，式 \((2.2.2)\) 和 \((2.2.4)\) 之间仅相差一个符号，这意味着我们只需要递归求出 \(F_{1}\) 和 \(F_{2}\) 的 \(\frac{n}{2}\) 个点值就可以在 \(\Theta(n)\) 的时间复杂度下求出 \(F\) 的 \(n\) 个点值。

因为最多递归 \(\log n\) 次，每一层的总时间复杂度为 \(\Theta(n)\)，所以 \(\rm DFT\) 过程的时间复杂度为 \(\Theta(n\log n)\)。

### 离散傅里叶逆变换

离散傅里叶逆变换 \(\rm(Inverse\ Discrete\ Fourier\ Transform,IDFT)\) 被用于将多项式的点值表示还原成系数表示，是 \(\rm FFT\) 的后半部分。

在 \(\rm DFT\) 过程中我们已经将待乘函数 \(f(x)\) 和 \(g(x)\) 的点值表示分别求了出来，易知它们卷积的点值序列为它们点值序列各处分别相乘的结果。

设 \(\{G_{n}\}\) 为 \(F(x)\) 在 \(\rm DFT\) 过程中求出的点值序列，\(\{F_{n}\}\) 是 \(F(x)\) 的系数序列，则根据定义有 ：

\[
G_k = \sum _{i = 0} ^{n - 1} \left(\omega_{n}^{k}\right) ^ i F_i \tag{2.3.1}
\]

此处有反演结论 ：

\[
nF_k = \sum_{i = 0} ^{n - 1} \left(\omega_{n}^{-k}\right) ^ i G_i \tag{2.3.2}
\]

\(\rm Proof :\)

\[
\begin{aligned}
    nF_k &= \sum_{i = 0} ^ {n - 1} \sum _{j = 0} ^ {n - 1} \left(\omega_{n} ^{-k}\right) ^ i \left(\omega_{n} ^{i}\right) ^ j F_j\\
    &= \sum_{i = 0} ^ {n - 1} \sum _{j = 0} ^ {n - 1} \omega_{n} ^{i(j - k)} F_j
\end{aligned}
\]

将式 \((2.1.4)\) 带入 \((2.3.3)\) 可得 ：

\[
\begin{aligned}
    nF_k &=  \sum _{j = 0} ^ {n - 1} \sum_{i = 0} ^ {n - 1} \left(\omega_{n} ^{j - k}\right)^i F_j\\
    &= \sum_{j = 0} ^ {n - 1} n[j = k] F_j\\
    &= nF_k
\end{aligned}
\]

故利用式 \((2.3.2)\) 将 \(\{G_{n}\}\) 带入 \(\rm DFT\) 过程，以 \(\omega_{n}^{-1}\) 作为一次单位根得出的点值即为 \(F(x)\) 的系数序列。

\(\rm IDFT\) 过程的时间复杂度为 \(\Theta(n\log n)\)。

至此，我们已经推导出了一个时间复杂度为 \(\Theta(n\log n)\)，可以递归实现的 \(\rm FFT\) 算法，需要注意的是，由于递归时需要两边长度相等，所以 \(F(x)\) 的长度必须是 \(2\) 的幂，少了的部分通过在高次项以 \(0\) 作为系数来补齐。

### 位逆序置换

位逆序置换 \(\rm(Bit-Reversal\ Permutation)\) 是 \(\rm FFT\) 中一个较大的优化，在国内又称蝴蝶变换。

它的优化主要在于将原本的递归实现变成了迭代实现。

在递归实现中，我们每一次都会把整个多项式的奇数次项和偶数次项系数分开，一直分到只剩下一个系数。但是我们也可以先把这些系数在原数组中拆分，然后再倍增地去合并这些算出来的值。

以 \(8\) 项多项式为例，模拟拆分的过程 :

- 初始序列为 : \(\left\{x_{0}, x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7}\right\}\)。
- 一次二分之后 : \(\left\{x_{0}, x_{2}, x_{4}, x_{6}\right\},\left\{x_{1}, x_{3}, x_{5}, x_{7}\right\}\)。
- 两次二分之后 : \(\left\{x_{0}, x_{4}\right\}, \left\{x_{2}, x_{6}\right\},\left\{x_{1}, x_{5}\right\},\left\{x_{3}, x_{7}\right\}\)。
- 三次二分之后 : \(\left\{x_{0}\right\}, \left\{x_{4}\right\}, \left\{x_{2}\right\}, \left\{x_{6}\right\}, \left\{x_{1}\right\}, \left\{x_{5}\right\}, \left\{x_{3}\right\}, \left\{x_{7}\right\}\)。

可以发现，只要把最后一层每个位置对应的坐标求出来，然后每次迭代时插空合并相邻两项即可。

记 \(R(x)\) 表示 \(x\) 在全部分治完后去到的位置，观察发现 \(R(x)\) 是 \(x\) 在二进制意义下翻转后的值。

首先有 \(R(0) = 0\)，剩下的考虑从小到大求解，显然有 ：

\[
R(x) = \left\lfloor\frac{R\left(\left\lfloor\frac{x}{2}\right\rfloor\right)}{2}\right\rfloor+(x \bmod 2) \times 2^{k - 1} \tag{2.4.1}
\]

求解 \(R(x)\) 并将每个数换到应该去的位置时间复杂度为 \(\Theta(n)\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 3e6;
const double Pi = acos(-1.0);

struct Complex { double x, y; } F[N], G[N];
Complex operator + (Complex a, Complex b) { return (Complex){a.x + b.x, a.y + b.y}; }
Complex operator - (Complex a, Complex b) { return (Complex){a.x - b.x, a.y - b.y}; }
Complex operator * (Complex a, Complex b) { return (Complex){a.x * b.x - a.y * b.y, a.x * b.y + a.y * b.x}; }

int n, m, len, ln, R[N];

void FFT (Complex *F, int type) {
    rep(i, 0, len - 1) if (i < R[i]) swap(F[i], F[R[i]]);
    for (int k = 1; k < len; k <<= 1) {
        Complex eps = (Complex){cos(Pi / k), type * sin(Pi / k)};
        for (int i = 0; i < len; i += (k << 1)) {
            Complex w = (Complex){1, 0};
            for (int j = i; j < i + k; j++, w = w * eps) {
                Complex tmp1 = F[j], tmp2 = w * F[j + k];
                F[j] = tmp1 + tmp2, F[j + k] = tmp1 - tmp2;
            }
        }
    }
}

int main () {

    scanf("%d%d", &n, &m);
    rep(i, 0, n) scanf("%lf", &F[i].x);
    rep(i, 0, m) scanf("%lf", &G[i].x);

    for (len = 1, ln = 0; len <= n + m; len <<= 1, ln++);
    rep(i, 0, len - 1) R[i] = (R[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);

    FFT(F, 1), FFT(G, 1);
    rep(i, 0, len - 1) F[i] = F[i] * G[i];

    FFT(F, -1);
    rep(i, 0, n + m) printf("%d ", (int)round(F[i].x / len));

    return 0;
}
```

## 快速数论变换

由于 \(\rm FFT\) 对单位根的依赖，所以该算法必须使用浮点数保存，进而引发精度问题。糟糕的是，数学家已经证明了在复数域内仅有单位根满足所需性质。

值得庆幸的是，大多数计数问题是在模意义下完成的，于是我们希望为 \(\rm FFT\) 找一个模意义下的替代品，最终方案为快速数论变换 \(\rm(Number\ Theoretic\ Transform,NTT)\)。

### 原根

原根的定义如下 ：

如果有 \(a^{n} \equiv 1 \pmod p\)，则称满足此条件最小的 \(n\) 为 \(a\) 在模 \(p\) 意义下的阶。若一个数 \(g\) 在模 \(p\) 意义下的原根为 \(\varphi(p)\)，那么称 \(g\) 为 \(p\) 的原根。

我们尝试用原根代替单位根进行运算，所以需要先证明以下几条性质 ：

**不重性质：**

\[
\forall 0\leqslant i \lt j \lt \varphi (p),g^i \not \equiv g^j \pmod p \tag{3.1.1}
\]

\(\rm Proof :\) 若存在 \(0\leqslant i \lt j \lt \varphi (p)\) 满足 \(g^{i} \equiv g^{j} \pmod p\)，那么 \(0\leqslant j - i \lt \varphi (p)\) 且 \(g^{j - i} \equiv 1 \pmod p\)，与原根的定义矛盾，故原命题得证。

**折半性质：**

定义 \(g_{n}^{1} = g^{\frac{p - 1}{n}},g_{n}^{k} = (g_{n}^{1})^{k}\) 则 ：

\[
g_{2n}^{2k} \equiv g_n^k \pmod p \tag{3.1.2}
\]

\(\rm Proof :\) 由式 \((3.1.1)\) 可得 \(g_{n}^{0},g_{n}^{1},g_{n}^{2},\cdots,g_{n}^{n - 1}\) 互不相同。将 \(g_{n}^{k}\) 的定义带入易证式 \((3.1.2)\)。

**对称性质：**

\[
g_{2n}^{k + n} \equiv -g_{2n}^k \pmod p \tag{3.1.3}
\]

\(\rm Proof :\)

参照式 \((2.1.3)\) 的证明方法，我们只需要证明 \(g_{2n}^{n} \equiv -1 \pmod p\) 即可。

\[
(g_{2n}^n) ^ 2 \equiv (g^{\frac{p - 1}{2}}) ^ 2 \equiv g^{p - 1} \equiv 1 \pmod p \tag{3.1.4}
\]

所以 \(g_{2n}^{n} \equiv 1\ or-1 \pmod p\)。

根据式 \((3.1.1)\)，我们知道 \(g_{2n}^{n} \not \equiv g^{p - 1} \pmod p\)，又因为 \(g^{p - 1} \equiv 1 \pmod p\)，故 \(g_{2n}^{n} \equiv -1 \pmod p\)。

**求和性质：**

\[
\sum _{i = 0} ^{n - 1} \left(g_{n} ^k\right) ^i \equiv n[k = 0] \pmod p \tag{3.1.5}
\]

\(\rm Proof :\) 参照式 \((2.1.4)\) 的证明。

有了以上 \(4\) 条性质，我们就可以直接将原根带入 \(\rm DFT\) 运算了。

另外，由于 \(\rm DFT\) 运算中的多项式长度 \(n\) 均为 \(2\) 的幂，并且我们取的模数 \(p\) 需要满足 \(p - 1\) 能整除足够大的 \(n\)，所以 \(p - 1\) 要包含一个较大的因子是 \(2\) 的幂。

比较常用的 \(\rm NTT\) 模数是 \(998244353 = 119 \times 2^{23} + 1\)，它的最小原根是 \(3\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 3e6, mod = 998244353;

int n, m, len, ln, F[N], G[N], rev[N];

int Pow (int a, int k) {
    int res = 1;
    for ( ; k; a = 1ll * a * a % mod, k >>= 1)
        if(k & 1) res = 1ll * res * a % mod;
    return res;
}

void NTT (int *F, bool type) {
    rep(i, 0, len) if (i < rev[i]) swap(F[i], F[rev[i]]);
    for (int k = 1; k < len; k <<= 1) {
        int eps = Pow(type ? 3 : 332748118, (mod - 1) / (k << 1));
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i, g = 1; j < i + k; j++, g = 1ll * g * eps % mod) {
                int tmp1 = F[j], tmp2 = 1ll * g * F[j + k] % mod;
                F[j] = tmp1 + tmp2 >= mod ? tmp1 + tmp2 - mod : tmp1 + tmp2;
                F[j + k] = tmp1 - tmp2 < 0 ? tmp1 - tmp2 + mod : tmp1 - tmp2;
            }
    }
}

int main () {

    scanf("%d%d", &n, &m);
    rep(i, 0, n) scanf("%d", &F[i]);
    rep(i, 0, m) scanf("%d", &G[i]);

    for (len = 1, ln = 0; len <= n + m; len <<= 1, ln++);
    rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);

    NTT(F, true), NTT(G, true);
    rep(i, 0, len - 1) F[i] = 1ll * F[i] * G[i] % mod;
    NTT(F, false);
    int Inv = Pow(len, mod - 2);
    rep(i, 0, n + m) printf("%lld ", 1ll * F[i] * Inv % mod);

    return 0;
}
```

### Chirp Z 变换

\(\rm Chirp\ Z-Transform\) 又称 \(\rm Bluestein\) 算法，与 \(\rm DFT\) 类似，它被用于在 \(\Theta[(n + m) \log n]\) 的时间复杂度内求解如下问题 ：

给定 \(n\) 次多项式 \(F(x)\)，求出 \(F(1),F(c),F(c^{2}),\cdots,F(c^{m})\)，\(c \in \mathbb{C}\)。

考虑组合恒等式 ：

\[
ik = \dbinom{i + k}{2} - \dbinom{i}{2} - \dbinom{k}{2} \tag{3.2.1}
\]

\(\rm Proof :\)

\[
\begin{aligned}
    ik &= \frac{2ik}{2}\\
    &= \frac{(i ^ 2 + 2ik + k ^ 2 - i - k) - (i ^ 2 - i) - (k ^ 2 - k)}{2}\\
    &= \dbinom{i + k}{2} - \dbinom{i}{2} - \dbinom{k}{2}
\end{aligned}
\]

于是有 ：

\[
\begin{aligned}
    F(c ^ k) &= \sum _{i = 0} ^ {n - 1} a_i c ^ {ik}\\
    &= \sum _{i = 0} ^ {n - 1} a_i c ^ {\binom{i + k}{2} - \binom{i}{2} - \binom{k}{2}}\\
    &= c ^ {-\binom{k}{2}} \sum _{i = 0} ^{n - 1} \left[a_i c ^ {-\binom{i}{2}} \right] \left[c ^ {\binom{i + k}{2}} \right]
\end{aligned}
\]

设 \(f(x) = c^{\binom{x}{2}}, g(x) = a_{xc}^{-\binom{x}{2}}\)，则有 ：

\[
\frac{F(c ^ k)}{c ^ {-\binom{k}{2}}} = \sum _ {i - j = k} f(i) \times g(j) \tag{3.2.4}
\]

可以使用减法卷积来计算，时间复杂度 \(\Theta[(n + m) \log n]\)。

具体来说，计算减法卷积时一般将 \(g(x)\) 翻转，即 \(g'(i) = g(m - i)\)，于是有 ：

\[
\begin{aligned}
    \frac{F(c ^ k)}{c ^ {-\binom{k}{2}}} &= \sum _ {i - j = k} f(i) \times g(j)\\
    &= \sum _ {i + j = m + k} f(i) \times g'(j)
\end{aligned}
\]

计算式 \((3.2.5)\) 时可以先对 \(f(x)\) 和 \(g(x)\) 求和卷积，称得到的多项式为 \(F(x)\)。

假设 \(f(x)\) 的次数为 \(n\)，\(g(x)\) 的次数为 \(m\)，那么 \(F(x)\) 有 \(n + m + 1\) 项。可以发现，现在 \(F(x)\) 的第 \(k\) 个位置实际上为答案的第 \(m + k\) 项，所以要将多项式向左平移 \(m\) 位，即 \(F'(k) = F(k + m)\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 3e6, mod = 998244353;

int n, m, c, len, ln, inv, tmp, a[N], p[N], R[N], F[N], G[N];

int Pow (int a, int k) {
    int res = 1;
    for ( ; k; a = 1ll * a * a % mod, k >>= 1)
        if(k & 1) res = 1ll * res * a % mod;
    return res;
}

void NTT (int *F, bool type) {
    rep(i, 0, len - 1) if (i < R[i]) swap(F[i], F[R[i]]);
    for (int k = 1; k < len; k <<= 1) {
        int E = Pow(type ? 3 : 332748118, (mod - 1) / (k << 1));
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i, G = 1; j < i + k; j++, G = 1ll * G * E % mod) {
                int tmp1 = F[j], tmp2 = 1ll * G * F[j + k] % mod;
                F[j] = tmp1 + tmp2 >= mod ? tmp1 + tmp2 - mod : tmp1 + tmp2;
                F[j + k] = tmp1 - tmp2 < 0 ? tmp1 - tmp2 + mod : tmp1 - tmp2;
            }
    }
}

int main () {

    scanf("%d%d%d", &n, &c, &m), n--, m--;
    rep(i, 0, n) scanf("%d", &a[i]);

    inv = Pow(c, mod - 2);
    for (len = 1, ln = 0; len <= n + m; len <<= 1, ln++);
    rep(i, 0, len - 1) R[i] = (R[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);

    F[0] = F[1] = tmp = 1;
    rep(i, 2, n + m) tmp = 1ll * tmp * c % mod, F[i] = 1ll * F[i - 1] * tmp % mod;
    p[0] = p[1] = tmp = 1;
    rep(i, 2, max(n, m)) tmp = 1ll * tmp * inv % mod, p[i] = 1ll * p[i - 1] * tmp % mod;
    rep(i, 0, n) G[i] = 1ll * a[i] * p[i] % mod;
    reverse(G, G + n + 1);

    NTT(F, true), NTT(G, true);
    rep(i, 0, len - 1) F[i] = 1ll * F[i] * G[i] % mod;
    NTT(F, false);
    
    int Inv = Pow(len, mod - 2);
    rep(i, 0, len - 1) F[i] = 1ll * F[i] * Inv % mod;
    rep(i, 0, m) printf("%d ", 1ll * F[n + i] * p[i] % mod);

    return 0;
}
```

### 分治多项式乘法

有些时候我们知道 \(G(x)\) 的所有项，需要计算 \(F(x)\)，并且它们满足关系 ：

\[
F_k = \sum _{i = 0} ^ {k - 1} F_iG_{k - i} \tag{3.3.1}
\]

这时候可以考虑采用 \(\rm CDQ\) 分治的思想，先递归计算左边半部分，再计算左边对右边的贡献。可以发现贡献是卷积的形式，于是可以用 \(\rm FFT/NTT\) 以 \(\Theta(n \log n)\) 的时间复杂度计算。

分治多项式乘法的时间复杂度为 \(T(n) = 2T(\frac{n}{2}) + \Theta(n \log n) = \Theta(n \log^{2} n)\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 3e5, mod = 998244353;

int n, F[N], G[N], rev[N], Ft[N], Gt[N];

int Pow (int a, int k) {
    int res = 1;
    for (; k; a = 1ll * a * a % mod, k >>= 1)
        if (k & 1) res = 1ll * res * a % mod;
    return res;
}

void NTT (int len, int *F, bool type) {
    rep(i, 0, len - 1) if (i < rev[i]) swap(F[i], F[rev[i]]);
    for (int k = 1; k < len; k <<= 1) {
        int eps = Pow(type ? 3 : 332748118, (mod - 1) / (k << 1));
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i, g = 1; j < i + k; j++, g = 1ll * g * eps % mod) {
                int tmp1 = F[j], tmp2 = 1ll * g * F[j + k] % mod;
                F[j] = tmp1 + tmp2 >= mod ? tmp1 + tmp2 - mod : tmp1 + tmp2;
                F[j + k] = tmp1 - tmp2 < 0 ? tmp1 - tmp2 + mod : tmp1 - tmp2;
            }
    }
}

void cdq (int l, int r) {
    if (r - l + 1 <= 30) {
        rep(i, l + 1, r) rep(j, l, i - 1)
            F[i] = (F[i] + 1ll * F[j] * G[i - j]) % mod;
        return;
    }

    int mid = l + r >> 1;
    cdq(l, mid);

    int len = 1, ln = 0;
    for (; len <= r + mid - 2 * l; len <<= 1, ln++);
    rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);

    rep(i, 0, mid - l) Ft[i] = F[i + l];
    rep(i, mid - l + 1, len - 1) Ft[i] = 0;
    rep(i, 0, r - l) Gt[i] = G[i];
    NTT(len, Ft, true), NTT(len, Gt, true);
    rep(i, 0, len - 1) Ft[i] = 1ll * Ft[i] * Gt[i] % mod;
    NTT(len, Ft, false);
    int Inv = Pow(len, mod - 2);
    rep(i, mid - l + 1, r - l) F[i + l] = (F[i + l] + 1ll * Ft[i] * Inv) % mod;

    cdq(mid + 1, r);
}

int main () {

    scanf("%d", &n), n--;
    rep(i, 1, n) scanf("%d", &G[i]);

    F[0] = 1, cdq(0, n);

    rep(i, 0, n) printf("%d ", F[i]);

    return 0;
}
```

## 快速沃尔什变换

快速沃尔什变换 \(\rm(Fast\ Walsh-Hadamard\ Transform,FWT)\) 被用来在 \(\Theta(n\log n)\) 的时间复杂度下求两个多项式的位运算卷积。

若称 \(h(x) = f(x) \oplus g(x)\)，其中 \(\oplus\) 是 \(\rm or,and\) 或 \(\rm xor\)，则应满足关系式 ：

\[
h(k) = \sum _{i \oplus j = k} f(i) \times g(j) \tag{4.0.1}
\]

### 构造 FWT 函数

在 \(\rm FFT\) 中，我们通过将多项式转换成点值表示并进行点积的方法避开了卷积，于是我们自然也希望将位运算卷积通过某种方式转换成点积运算。

设 \(F' = FWT(F)\) 表示幂级数 \(F\) 经过 \(\rm FWT\) 变换后得到的幂级数。

容易发现，我们构造的 \(\rm FWT\) 变换需要满足 ：

\[
A \times B = C \iff FWT(A) \cdot FWT(B) = FWT(C) \tag{4.1.1}
\]

由于 \(\rm DFT\) 是线性变换，我们自然希望 \(\rm FWT\) 也是线性变换。

因此，考虑设 \(k_{i, j}\) 表示 \(F_{j}\) 对 \(F'_{i}\) 的贡献系数，故有 ：

\[
F'_i = \sum _{j = 0} ^ {n - 1} k_{i, j} F_j \tag{4.1.2}
\]

根据 \(FWT(A) \cdot FWT(B) = FWT(C)\) 可以得到 ：

\[
A'_i \times B'_i = C'_i \tag{4.1.3}
\]

\[
\left(\sum _{j = 0} ^ {n - 1} k_{i, j} A_j\right)\left(\sum _{p = 0} ^ {n - 1} k_{i, p} B_p\right) = \sum_{j = 0} ^ {n - 1} k_{i, j} C_j \tag{4.1.4}
\]

\[
\sum _{j = 0} ^ {n - 1}\sum _{p = 0} ^ {n - 1} k_{i, j} k_{i, p} A_j   B_p = \sum_{j = 0} ^ {n - 1} k_{i, j} C_j \tag{4.1.5}
\]

根据 \(A \times B = C\) 可以得到 ：

\[
C_p = \sum _{i \oplus j = p} A_i\times B_j \tag{4.1.6}
\]

\[
\sum_{p = 0} ^ {n - 1} k_{i, p} C_p = \sum_{p = 0} ^ {n - 1} k_{i, p}\sum _{t \oplus j = p} A_t B_j \tag{4.1.7}
\]

\[
\begin{aligned}
    \sum _{j = 0} ^ {n - 1}\sum _{p = 0} ^ {n - 1} k_{i, j} k_{i, p} A_j  B_p &= \sum_{p = 0} ^ {n - 1} k_{i, p}\sum _{t \oplus j = p} A_t B_j \\
    &= \sum _{p = 0} ^{n - 1} \sum _{t \oplus j = p} k_{i, t \oplus j} A_t B_j\\
    &= \sum _{t = 0} ^ {n - 1} \sum_{j = 0} ^ {n - 1} k_{i, t \oplus j} A_t B_j
\end{aligned}
\]

对比式 \((4.1.8)\) 中两边系数可以发现只需要满足 ：

\[
k_{i, j}k_{i, p} = k_{i, j \oplus p} \tag{4.1.9}
\]

假设我们已经求出了 \(k_{0, 0},k_{0,1},k_{1,0},k_{1,1}\)，那么可以构造 \(k_{i, j} = \prod_{t} k_{i_{t},j_{t}}\)，其中 \(a_{t}\) 表示 \(a\) 在二进制下的第 \(t\) 位。这种构造方式导出的变换系数 \(k\) 推导 \(k_{i, j}k_{i, p} = k_{i, j \oplus p}\) 的充分性容易证明。

### 求解 FWT 变换

现在我们需要快速求解下式 ：

\[
F'_i = \sum _{j = 0} ^{n - 1} k_{i, j} F_j \tag{4.2.1}
\]

我们考虑按位折半计算，下面设 \(\hat{x}\) 表示 \(x\) 去除二进制首位以后的值。

\[
\begin{aligned}
    F'_i &= \sum _{j = 0} ^{n / 2 - 1} k_{i, j} F_j + \sum _{j = n / 2} ^{n - 1} k_{i, j} F_j \\
    &= \sum _{j = 0} ^{n / 2 - 1} k_{i_0, j_0}k_{\hat{i}, \hat{j}} F_j + \sum _{j = n / 2} ^{n - 1} k_{i_0, j_0}k_{\hat{i}, \hat{j}} F_j \\
    &= k_{i_0, 0}\sum _{j = 0} ^{n / 2 - 1} k_{\hat{i}, \hat{j}} F_j + k_{i_0, 1}\sum _{j = n / 2} ^{n - 1} k_{\hat{i}, \hat{j}} F_j
\end{aligned}
\]

设 \(F^{0}\) 表示幂级数 \(F'\) 下标的二进制首位为 \(0\) 的部分，相似地定义 \(F^{1}\)。

- 若 \(i_{0} = 0\)，则有 \(F'_{i} = k_{0, 0} F^{0}_{i} + k_{0, 1} F^{1}_{i}\)。
- 若 \(i_{0} = 1\)，则有 \(F'_{i + n/2} = k_{1, 0} F^{0}_{i} + k_{1, 1} F^{1}_{i}\)。

在该算法中，每次迭代会将长度减半，合并一层的时间复杂度为 \(\Theta(n)\)，所以总时间复杂度为 \(\Theta(n\log n)\)。

此外，逆变换 \(\rm(IFWT)\) 时对变换矩阵 \(k\) 求个逆即可。

### 构造位矩阵

针对不同的位运算，我们需要构造不同的位矩阵 \(k\) 以拟合 \(\rm FWT\) 变换。

#### 或卷积

首先我们知道 ：

\[
k_{p, i}\times k_{p, j} = k_{p, i | j} \tag{4.3.1}
\]

首先可以观察到 \(k_{p, i} \times k_{p, i} = k_{p, i}\)，故 \(k_{p, i} \in \{0, 1\}\)。

然后可以发现 \(k_{p, 0} \times k_{p, 1} = k_{p, 1}\)，所以 \(k_{p, 0} = 1\)。 又因为矩阵如果一列都是 \(1\)，那么它没有逆，故 \(k\) 仅可能为以下两种之一 ：

\[
\begin{bmatrix} 1&0\\ 1&1 \end{bmatrix}~or~\begin{bmatrix} 1&1\\ 1&0 \end{bmatrix} \tag{4.3.2}
\]

由于右边那种等价于高维前缀和，所以我选择右边那种（事实上两种都可以）。

\[
\begin{aligned}
    F'_i &= F^0_i\\
    F'_{i + n/2} &= F^0_i + F^1_i
\end{aligned}
\]

对于逆变换，将矩阵求个逆就可以得到 \(k^{-1} = \begin{bmatrix} 1&0\\ -1&1 \end{bmatrix}\)。

\[
\begin{aligned}
    IF_i &= IF^{0}_i\\
    IF_{i + n/2} &= -IF^0_i + IF^1_i
\end{aligned}
\]

#### 与卷积

可以发现与卷积同或卷积几乎完全一样，此处不赘述，仅给出其位矩阵和逆位矩阵 ：

\[
k = \begin{bmatrix} 1&1\\ 0&1 \end{bmatrix},k^{-1} = \begin{bmatrix} 1&-1\\ 0&1 \end{bmatrix} \tag{4.3.5}
\]

#### 异或卷积

首先我们知道 ：

\[
k_{p, i}\times k_{p, j} = k_{p, i~xor~j} \tag{4.3.6}
\]

因为 \(k_{0, 0} \times k_{x, y} = k_{x, y}\)，所以 \(k_{0, 0} = 1\)。

因为 \(k_{1, 1} \times k_{1, 1} = k_{1, 0}\)，此时若 \(k_{1, 1} = k_{1, 0} = 0\)，则有一行为 \(0\)，矩阵无逆，故 \(k_{1, 1},k_{1, 0} \not= 0\)。

因为 \(k_{1, 0} \times k_{1, 1} = k_{1, 1}\)，又因为 \(k_{1, 1} \not = 0\)，所以 \(k_{1, 0} = 1\)。

因为 \(k_{1, 1} \times k_{1, 1} = k_{1, 0} = 1\)，所以 \(k_{1, 1} \in \{1, -1\}\)。

因为 \(k_{0,1} \times k_{0, 1} = k_{0, 0} = 1\)，所以 \(k_{0, 1} \in \{1, -1\}\)。

因为 \(k_{0, 1}\) 和 \(k_{1, 1}\) 不能相等，否则行列式为 \(0\)，矩阵无逆，所以 \(k\) 仅可能为以下两种之一 ：

\[
\begin{bmatrix} 1&1\\ -1&1 \end{bmatrix}~or~\begin{bmatrix} 1&1\\ 1&-1 \end{bmatrix} \tag{4.3.7}
\]

我们采用第二种，可推知 ：

\[
\begin{aligned}
    F'_i &= F^0_i + F^1_i\\
    F'_{i + n/2} &= F^0_i - F^1_i
\end{aligned}
\]

对 \(k\) 求逆可以得到 \(k^{-1} = \begin{bmatrix} \frac{1}{2}&\frac{1}{2}\\ \frac{1}{2}&-\frac{1}{2} \end{bmatrix}\)。

\[
\begin{aligned}
    IF_i &= \frac{IF^0_i + IF^1_i}{2}\\
    IF_{i + n/2} &= \frac{IF^0_i - IF^1_i}{2}
\end{aligned}
\]

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 2e5, mod = 998244353, Inv = 499122177;

int n, len, a[N], b[N], F[N], G[N];

void OR (int *F, bool type) {
    for (int k = 1; k < len; k <<= 1)
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i; j < i + k; j++)
                F[j + k] = (F[j + k] + (type ? F[j] : -F[j])) % mod;
}

void AND (int *F, bool type) {
    for (int k = 1; k < len; k <<= 1)
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i; j < i + k; j++) {
                int tmp1 = F[j], tmp2 = F[j + k];
                F[j] = ((type ? 0 : -tmp1) + tmp2) % mod;
                F[j + k] = (tmp1 + (type ? tmp2 : 0)) % mod;
            }
}

void XOR (int *F, bool type) {
    for (int k = 1; k < len; k <<= 1)
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i; j < i + k; j++) {
                int tmp1 = F[j], tmp2 = F[j + k];
                F[j] = (type ? 2ll : 1ll) * Inv * (tmp1 + tmp2) % mod;
                F[j + k] = (type ? 2ll : 1ll) * Inv * (tmp1 - tmp2) % mod;
            }
}

int main () {

    scanf("%d", &n), len = 1 << n;
    rep(i, 0, len - 1) scanf("%d", &a[i]);
    rep(i, 0, len - 1) scanf("%d", &b[i]);

    rep(i, 0, len - 1) F[i] = a[i], G[i] = b[i];
    OR(F, true), OR(G, true);
    rep(i, 0, len - 1) F[i] = 1ll * F[i] * G[i] % mod;
    OR(F, false);
    rep(i, 0, len - 1) printf("%d ", F[i] < 0 ? F[i] + mod : F[i]); puts("");

    rep(i, 0, len - 1) F[i] = a[i], G[i] = b[i];
    AND(F, true), AND(G, true);
    rep(i, 0, len - 1) F[i] = 1ll * F[i] * G[i] % mod;
    AND(F, false);
    rep(i, 0, len - 1) printf("%d ", F[i] < 0 ? F[i] + mod : F[i]); puts("");

    rep(i, 0, len - 1) F[i] = a[i], G[i] = b[i];
    XOR(F, true), XOR(G, true);
    rep(i, 0, len - 1) F[i] = 1ll * F[i] * G[i] % mod;
    XOR(F, false);
    rep(i, 0, len - 1) printf("%d ", F[i] < 0 ? F[i] + mod : F[i]); puts("");

    return 0;
}
```

## 多项式基本操作

多项式之间除了乘法，还可以做一些其它的基本操作，但它们都是基于多项式乘法的。

### 多项式求逆

若两个多项式 \(F(x)\) 和 \(G(x)\) 满足 \(F(x)G(x) = 1\)，则称它们互为逆元，记作 \(G(x) = F^{-1}(x)\)。

求解多项式乘法逆元的时候考虑使用倍增的思想，不断扩大倍增上界。

当多项式的界为 \(\bmod\ x\) 时，直接对多项式的常数项求逆元即可。

设 \(G(x) = F^{-1}(x) \pmod {x^{n}}\)，如果我们已经求出了 \(G'(x) = F^{-1}(x) \pmod {x^{n/2}}\)，那么 ：

\[
G(x) - G'(x) \equiv 0 \pmod {x^{n/2}} \tag{5.1.1}
\]

为了能配出 \(x^{n}\) 作为模数，考虑将式子两边同时平方，得到 ：

\[
G^2(x) - 2G(x)G'(x) + G'^2(x) \equiv 0 \pmod {x ^ n} \tag{5.1.2}
\]

因为 \(F(x)G(x) = 1\)，所以式子两边同时乘 \(F(x)\) 并整理可得 ：

\[
G(x) = 2G'(x) - G'^2(x)F(x) \pmod {x ^ n} \tag{5.1.3}
\]

根据式 \((5.1.3)\) 可以倍增求出 \(F^{-1}(x)\)，时间复杂度为 \(T(n) = T(\frac{n}{2}) + \Theta(n \log n) = \Theta(n\log n)\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 3e5, mod = 998244353;

int n, len, ln, F[N], R[N], G[N], g[N];

int Pow (int a, int k) {
    int res = 1;
    for ( ; k; a = 1ll * a * a % mod, k >>= 1)
        if(k & 1) res = 1ll * res * a % mod;
    return res;
}

void NTT (int *F, bool type) {
    rep(i, 0, len - 1) if (i < R[i]) swap(F[i], F[R[i]]);
    for (int k = 1; k < len; k <<= 1) {
        int eps = Pow(type ? 3 : 332748118, (mod - 1) / (k << 1));
        for (int i = 0; i < len; i += k << 1)
            for (int j = i, g = 1; j < i + k; j++, g = 1ll * g * eps % mod) {
                int tmp1 = F[j], tmp2 = 1ll * g * F[j + k] % mod;
                F[j] = tmp1 + tmp2 >= mod ? tmp1 + tmp2 - mod : tmp1 + tmp2;
                F[j + k] = tmp1 - tmp2 < 0 ? tmp1 - tmp2 + mod : tmp1 - tmp2;
            }
    }
}

void INV (int n, int *F) {
    G[0] = Pow(F[0], mod - 2);
    for (len = 4, ln = 2; len <= (n << 2); len <<= 1, ln++) {
        rep(i, len >> 1, len - 1) G[i] = g[i] = 0;
        rep(i, 0, (len >> 1) - 1) g[i] = F[i];
        rep(i, 0, len - 1) R[i] = (R[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
        NTT(G, true), NTT(g, true);
        rep(i, 0, len - 1) G[i] = 1ll * G[i] * (2 - 1ll * G[i] * g[i] % mod + mod) % mod;
        NTT(G, false);
        int Inv = Pow(len, mod - 2);
        rep(i, 0, (len >> 1) - 1) G[i] = 1ll * G[i] * Inv % mod;
        rep(i, len >> 1, len - 1) G[i] = 0;
    }
    rep(i, 0, n) F[i] = G[i];
}

int main () {

    scanf("%d", &n), n--;
    rep(i, 0, n) scanf("%d", &F[i]);

    INV(n, F);
    rep(i, 0, n) printf("%d ", (F[i] + mod) % mod);

    return 0;
}
```

### 多项式开方

若两个多项式 \(F(x)\) 和 \(G(x)\) 满足 \(G^{2}(x) = F(x)\)，则称 \(F(x)\) 开根后为 \(G(x)\)，记作 \(G(x) = F^{\frac{1}{2}}(x)\)。

与多项式求逆一样，多项式开根也利用了倍增法。

当多项式的界为 \(\bmod\ x\) 时，直接对常数项使用二次剩余即可。

设 \(G(x) = F^{\frac{1}{2}}(x) \pmod {x^{n}}\)，如果我们已经求出了 \(G'(x) = F^{\frac{1}{2}}(x) \pmod {x^{n / 2}}\)，那么 ：

\[
G'^2 (x) - F(x) \equiv 0 \pmod {x ^ {n / 2}} \tag{5.2.1}
\]

对式 \((5.2.1)\) 两边同时平方并作简单变换，得到 ：

\[
\left[G'^2(x) + F(x)\right] ^ 2 \equiv 4G'^2(x)F(x) \pmod {x ^ n} \tag{5.2.2}
\]

对式子两边同时除以 \(4G'^{2}(x)\)，可以得到 ：

\[
\left[\frac{G'^2(x) + F(x)}{2G'(x)}\right] ^ 2 \equiv F(x) \pmod {x ^ n} \tag{5.2.3}
\]

结合 \(G(x)\) 的定义，可以发现 ：

\[
G(x) = \frac{1}{2}G'(x) + \frac{1}{2}G'^{-1}(x)F(x) \pmod {x ^ n} \tag{5.2.4}
\]

根据式 \((5.2.4)\) 可以倍增求出 \(F^{\frac{1}{2}}(x)\)，时间复杂度为 \(T(n) = T(\frac{n}{2}) + \Theta(n \log n) = \Theta(n\log n)\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 3e5, mod = 998244353;

int n, F[N], rev[N], GI[N], FI[N], iG[N], GS[N], FS[N];

int Pow (int a, int k) {
    int res = 1;
    for ( ; k; a = 1ll * a * a % mod, k >>= 1)
        if(k & 1) res = 1ll * res * a % mod;
    return res;
}

void NTT (int len, int *F, bool type) {
    rep(i, 0, len - 1) if (i < rev[i]) swap(F[i], F[rev[i]]);
    for (int k = 1; k < len; k <<= 1) {
        int eps = Pow(type ? 3 : 332748118, (mod - 1) / (k << 1));
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i, g = 1; j < i + k; j++, g = 1ll * g * eps % mod) {
                int tmp1 = F[j], tmp2 = 1ll * g * F[j + k] % mod;
                F[j] = tmp1 + tmp2 >= mod ? tmp1 + tmp2 - mod : tmp1 + tmp2;
                F[j + k] = tmp1 - tmp2 < 0 ? tmp1 - tmp2 + mod : tmp1 - tmp2;
            }
    }
}

void INV (int n, int *F) {
    rep(i, 0, n << 2) FI[i] = GI[i] = 0;
    GI[0] = Pow(F[0], mod - 2);
    for (int len = 4, ln = 2; len <= n << 2; len <<= 1, ln++) {
        rep(i, 0, (len >> 1) - 1) FI[i] = F[i];
        rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
        NTT(len, GI, true), NTT(len, FI, true);
        rep(i, 0, len - 1) GI[i] = 1ll * GI[i] * (2 - 1ll * GI[i] * FI[i] % mod + mod) % mod;
        NTT(len, GI, false);
        int Inv = Pow(len, mod - 2);
        rep(i, 0, (len >> 1) - 1) GI[i] = 1ll * GI[i] * Inv % mod;
        rep(i, len >> 1, len - 1) GI[i] = 0;
    }
    rep(i, 0, n) iG[i] = GI[i];
}

void SQR (int n, int *F) {
    rep(i, 0, n << 2) FS[i] = GS[i] = 0;
    GS[0] = sqrt(F[0]);
    for (int len = 4, ln = 2; len <= n << 2; len <<= 1, ln++) {
        rep(i, 0, (len >> 1) - 1) FS[i] = F[i];
        rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
        INV((len >> 1) - 1, GS);
        NTT(len, GS, true), NTT(len, FS, true), NTT(len, iG, true);
        rep(i, 0, len - 1) GS[i] = 499122177ll * (GS[i] + 1ll * FS[i] * iG[i] % mod) % mod;
        NTT(len, GS, false);
        int Inv = Pow(len, mod - 2);
        rep(i, 0, (len >> 1) - 1) GS[i] = 1ll * GS[i] * Inv % mod;
        rep(i, len >> 1, len - 1) GS[i] = 0; 
    }
    rep(i, 0, n) F[i] = GS[i];
}

int main () {

    scanf("%d", &n), n--;
    rep(i, 0, n) scanf("%d", &F[i]);

    SQR(n, F);

    rep(i, 0, n) printf("%d ", F[i]);

    return 0;
}
```

### 多项式带余除法

给定多项式 \(F(x)\) 和 \(G(x)\)，若满足关系式 \(Q(x)G(x) + R(x) = F(x)\)，则称 \(Q(x)\) 和 \(R(x)\) 分别是 \(F(x)\) 除以 \(G(x)\) 的商和余数。

可以发现如果能消除 \(R(x)\) 的影响则可以直接使用多项式求逆。

考虑构造变换 ：

\[
F' = x ^ {\deg F} F\left(\frac{1}{x}\right) \tag{5.3.1}
\]

可以发现，其本质就是翻转多项式系数。

设 \(n = \deg F,m = \deg G\)，将多项式带余除法定义式中的 \(x\) 替换成 \(\frac{1}{x}\)，并将两边同时乘 \(x^{n}\) 可得 ：

\[
x ^ n F\left(\frac{1}{x}\right) = x ^ {n - m} Q\left(\frac{1}{x}\right) x ^ m G\left(\frac{1}{x}\right) + x ^ {n - m + 1} x ^ {m - 1} R\left(\frac{1}{x}\right) \tag{5.3.2}
\]

将式 \((5.3.1)\) 带入可得 ：

\[
F'(x) = Q'(x) G'(x) + x ^ {n - m + 1} R'(x) \tag{5.3.3}
\]

注意到式 \((5.3.3)\) 中 \(R'(x)\) 带了一个 \(x^{n - m + 1}\) 作为系数，于是将上式放在 \(\bmod\ x^{n - m + 1}\) 意义下计算即可将这一项消去。又因为 \(\deg Q' = n - m \lt n - m + 1\)，故 \(Q'(x)\) 的计算不会受到影响。

综上，有 ：

\[
F'(x) = Q'(x)G'(x) \pmod {x ^ {n - m + 1}} \tag{5.3.4}
\]

使用多项式求逆即可计算 \(Q(x)\)，将其带入定义式可以得到 \(R(x)\)。

时间复杂度 \(\Theta(n \log n)\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 3e5, mod = 998244353;

int n, m, len, ln, F[N], G[N], rev[N], FR[N], GR[N], Q[N], R[N], FI[N], GI[N];

int Pow (int a, int k) {
    int res = 1;
    for ( ; k; a = 1ll * a * a % mod, k >>= 1)
        if(k & 1) res = 1ll * res * a % mod;
    return res;
}

void NTT (int len, int *F, bool type) {
    rep(i, 0, len - 1) if (i < rev[i]) swap(F[i], F[rev[i]]);
    for (int k = 1; k < len; k <<= 1) {
        int eps = Pow(type ? 3 : 332748118, (mod - 1) / (k << 1));
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i, g = 1; j < i + k; j++, g = 1ll * g * eps % mod) {
                int tmp1 = F[j], tmp2 = 1ll * g * F[j + k] % mod;
                F[j] = tmp1 + tmp2 >= mod ? tmp1 + tmp2 - mod : tmp1 + tmp2;
                F[j + k] = tmp1 - tmp2 < 0 ? tmp1 - tmp2 + mod : tmp1 - tmp2;
            }
    }
}

void INV (int n, int *F) {
    rep(i, 0, n << 2) FI[i] = GI[i] = 0;
    GI[0] = Pow(F[0], mod - 2);
    for (int len = 4, ln = 2; len <= n << 2; len <<= 1, ln++) {
        rep(i, 0, (len >> 1) - 1) FI[i] = F[i];
        rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
        NTT(len, GI, true), NTT(len, FI, true);
        rep(i, 0, len - 1) GI[i] = 1ll * GI[i] * (2 - 1ll * GI[i] * FI[i] % mod + mod) % mod;
        NTT(len, GI, false);
        int Inv = Pow(len, mod - 2);
        rep(i, 0, (len >> 1) - 1) GI[i] = 1ll * GI[i] * Inv % mod;
        rep(i, len >> 1, len - 1) GI[i] = 0;
    }
    rep(i, 0, n) F[i] = GI[i];
}

void DIV (int n, int m, int *F, int *G) {
    rep(i, 0, n) FR[i] = F[n - i];
    rep(i, 0, m) GR[i] = G[m - i];
    rep(i, n - m + 1, m) GR[i] = 0;
    INV(n - m, GR);
    for (len = 1, ln = 0; len <= 2 * n - m; len <<= 1, ln++);
    rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
    NTT(len, FR, true), NTT(len, GR, true);
    rep(i, 0, len - 1) FR[i] = 1ll * FR[i] * GR[i] % mod;
    NTT(len, FR, false);
    int Inv = Pow(len, mod - 2);
    rep(i, 0, n - m) Q[i] = 1ll * FR[n - m - i] * Inv % mod;
    rep(i, 0, n - m) printf("%d ", Q[i]); puts("");
    for (len = 1, ln = 0; len <= n; len <<= 1, ln++);
    rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
    NTT(len, G, true), NTT(len, Q, true);
    rep(i, 0, len - 1) G[i] = 1ll * G[i] * Q[i] % mod;
    NTT(len, G, false);
    Inv = Pow(len, mod - 2);
    rep(i, 0, m - 1) R[i] = (F[i] - 1ll * G[i] * Inv % mod + mod) % mod;
    rep(i, 0, m - 1) printf("%d ", R[i]);
}

int main () {

    scanf("%d%d", &n, &m);
    rep(i, 0, n) scanf("%d", &F[i]);
    rep(i, 0, m) scanf("%d", &G[i]);

    DIV(n, m, F, G);

    return 0;
}
```

### 多项式指对函数

两者均由麦克劳林级数定义 ：

\[
\begin{aligned}
    \ln F(x) &= -\sum_{i \geqslant 1} \frac{[1 - F(x)] ^ i}{i}\\
    \exp F(x) &= \sum _{i \geqslant 0} \frac{F^i(x)}{i!}
\end{aligned}
\]

之所以用麦克劳林级数这么复杂的方式，是因为这样就可以只用加法和乘法定义多项式指对函数了。

众所周知有多项式的求导 ：

\[
F'(x) = \sum _{i \geqslant 1} iF_i\cdot x ^ {i - 1} \tag{5.4.2}
\]

还有多项式的积分 ：

\[
F(x) = C + \sum _{i \geqslant 0} \frac{F'_i}{i} \cdot x ^ {i + 1} \tag{5.4.3}
\]

#### 多项式对数函数

首先，对于多项式 \(F(x)\)，若 \(\ln F(x)\) 存在，则按照其定义，必须满足 ：

\[
[x ^ 0]F(x) = 1 \tag{5.4.4}
\]

先对 \(\ln F(x)\) 求导 ：

\[
\frac{\mathrm{d}\ln F(x)}{\mathrm{d} x} \equiv \frac{F'(x)}{F(x)} \pmod {x ^ n} \tag{5.4.5}
\]

再对其积分 ：

\[
\ln F(x) \equiv \int \mathrm{d}\ln F(x) \equiv \int \frac{F'(x)}{F(x)}\mathrm{d} x \pmod {x ^ n} \tag{5.4.6}
\]

多项式的求导和积分时间复杂度均为 \(\Theta(n)\)，多项式求逆和乘法的时间复杂度为 \(\Theta(n \log n)\)，所以求解多项式对数函数的时间复杂度为 \(\Theta(n \log n)\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 4e5 + 10, mod = 998244353;

int n, m, f[N], F[N], rev[N], FI[N], GI[N], iF[N], lnF[N];

int Pow (int a, int k) {
    int res = 1;
    for (; k; a = 1ll * a * a % mod, k >>= 1)
        if (k & 1) res = 1ll * res * a % mod;
    return res;
}

void NTT (int len, int *F, bool type) {
    rep(i, 0, len - 1) if (i < rev[i]) swap(F[i], F[rev[i]]);
    for (int k = 1; k < len; k <<= 1) {
        int eps = Pow(type ? 3 : 332748118, (mod - 1) / (k << 1));
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i, g = 1; j < i + k; j++, g = 1ll * g * eps % mod) {
                int tmp1 = F[j], tmp2 = 1ll * g * F[j + k] % mod;
                F[j] = tmp1 + tmp2 >= mod ? tmp1 + tmp2 - mod : tmp1 + tmp2;
                F[j + k] = tmp1 - tmp2 < 0 ? tmp1 - tmp2 + mod : tmp1 - tmp2;
            }
    }
}

void INV (int n, int *F, int *iF) {
    rep(i, 0, n << 2) GI[i] = FI[i] = 0;
    GI[0] = Pow(F[0], mod - 2);
    for (int len = 4, ln = 2; len <= n << 2; len <<= 1, ln++) {
        rep(i, 0, (len >> 1) - 1) FI[i] = F[i];
        rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
        NTT(len, GI, true), NTT(len, FI, true);
        rep(i, 0, len - 1) GI[i] = 1ll * GI[i] * (2 - 1ll * GI[i] * FI[i] % mod + mod) % mod;
        NTT(len, GI, false);
        int Inv = Pow(len, mod - 2);
        rep(i, 0, (len >> 1) - 1) GI[i] = 1ll * GI[i] * Inv % mod;
        rep(i, len >> 1, len - 1) GI[i] = 0;
    }
    rep(i, 0, n) iF[i] = GI[i];
    rep(i, n + 1, n << 2) iF[i] = 0;
}

void LN (int n, int *F, int *lnF) {
    rep(i, 0, n - 1) lnF[i] = 1ll * (i + 1) * F[i + 1] % mod;
    rep(i, n, n << 2) lnF[i] = 0;
    INV(n, F, iF);
    int len = 1, ln = 0;
    while (len < n << 1) len <<= 1, ln++;
    rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
    NTT(len, lnF, true), NTT(len, iF, true);
    rep(i, 0, len - 1) lnF[i] = 1ll * lnF[i] * iF[i] % mod;
    NTT(len, lnF, false);
    int Inv = Pow(len, mod - 2);
    rep(i, 0, n - 1) lnF[i] = 1ll * lnF[i] * Inv % mod;
    rep(i, n, n << 2) lnF[i] = 0;
    dep(i, n, 1) lnF[i] = 1ll * Pow(i, mod - 2) * lnF[i - 1] % mod;
    lnF[0] = 0;
}

int main () {

    cin >> n, n--;
    rep(i, 0, n) cin >> F[i];

    LN(n, F, lnF);

    rep(i, 0, n) cout << lnF[i] << " ";

    return 0;
}
```

#### 多项式指数函数

首先，对于多项式 \(F(x)\)，若 \(\exp F(x)\) 存在，则按照其定义，必须满足 ：

\[
[x ^ 0] F(x) = 1 \tag{5.4.7}
\]

否则 \(\exp F(x)\) 的常数项不收敛。

对 \(\exp F(x)\) 求导可得 ：

\[
\frac{\mathrm{d} \exp F(x)}{\mathrm{d}x} \equiv F'(x) \exp F(x) \pmod {x ^ n} \tag{5.4.8}
\]

若记 \(\exp F(x)\) 为 \(G(x)\)，则可以得到 ：

\[
G'(x) \equiv F'(x)G(x) \pmod {x ^ n} \tag{5.4.9}
\]

用系数关系表示为 ：

\[
G'_n = \sum _{i = 0} ^ n F'_i G_{n - i} \tag{5.4.10}
\]

将导函数积回来，可以得到 ：

\[
G_{n + 1} = \frac{1}{n + 1}\sum _{i = 0} ^ n (i + 1)F_{i + 1}G_{n - i} \tag{5.4.11}
\]

上式的递推可以用分治多项式乘法优化至 \(\Theta(n \log^{2} n)\)。

### 多项式牛顿迭代

定义多项式的复合 ：

\[
F \circ G (x) = \sum _{i\geqslant 0} F_i G^i(x) \tag{5.5.1}
\]

已知函数 \(G(x)\)，求多项式 \(F(x) \pmod {x^{n}}\)，满足 \(G \circ F(x) = 0\)。

首先当多项式的界为 \(\bmod\ x\) 时，可以手算出 \(F(x) \pmod x\)。

假设现在已经求得 \(\bmod\ x^{n / 2}\) 意义下的解 \(F_{0}(x)\)，要进一步求出 \(\bmod\ x^{n}\) 意义下的解 \(F(x)\)。

众所周知有泰勒公式 ：

\[
f(x) = \sum _{i = 0} ^ {\infty} \frac{f^{(i)}(x_0)}{i!}(x - x_0) ^ i \tag{5.5.2}
\]

将 \(G[F(x)]\) 在 \(F_{0}(x)\) 处进行泰勒展开，有 ：

\[
\sum _{i = 0} ^ {\infty} \frac{G^{(i)}[F_0(x)]}{i!}[F(x) - F_0(x)] ^ i \equiv 0 \pmod {x ^ n} \tag{5.5.3}
\]

由于当 \(i\) 取大于 \(1\) 的值时 \([F(x) - F_{0}(x)]^{i}\) 的最低次项都会超过 \(x^{n}\)，所以 ：

\[
G[F_0(x)] + G'[F_0(x)][F(x) - F_0(x)] \equiv 0 \pmod {x ^ n} \tag{5.5.4}
\]

化简得到牛顿迭代的经典公式 ：

\[
F(x) = F_0(x) - \frac{G[F_0(x)]}{G'[F_0(x)]} \pmod {x ^ n} \tag{5.5.5}
\]

使用多项式牛顿迭代也可以解决一些其它的多项式基本操作。

#### 多项式求逆

设需要求逆的函数为 \(H(x)\)，\(F(x) = H^{-1}(x)\)，有方程 ：

\[
G \circ F(x) \equiv \frac{1}{F(x)} - H(x) \equiv 0 \pmod {x ^ n} \tag{5.5.6}
\]

运用式 \((5.5.5)\) 可得 ：

\[
F(x) \equiv F_0(x) - \frac{\frac{1}{F_0(x)} - H(x)}{-\frac{1}{F_0^{2}(x)}} \equiv 2F_0(x) - F_0^2(x)H(x) \pmod {x ^ n} \tag{5.5.7}
\]

时间复杂度 \(T(n) = T\left(\frac{n}{2}\right) + \Theta(n \log n) = \Theta(n \log n)\)。

#### 多项式开方

设需要开方的函数为 \(H(x)\)，\(F(x) = H^{\frac{1}{2}}(x)\)，有方程 ：

\[
G \circ F(x) \equiv F^2(x) - H(x) \equiv 0 \pmod {x ^ n} \tag{5.5.8}
\]

运用式 \((5.5.5)\) 可得 ：

\[
F(x) \equiv F_0(x) - \frac{F_0^2(x) - H(x)}{2F_0(x)} \equiv 2F_0^{-1}(x)[F_0^2(x) + H(x)] \pmod {x ^ n} \tag{5.5.9}
\]

时间复杂度 \(T(n) = T\left(\frac{n}{2}\right) + \Theta(n \log n) = \Theta(n \log n)\)。

#### 多项式指数函数

设需要求 \(\exp\) 的函数为 \(H(x)\)，\(F(x) = \exp H(x)\)，有方程 ：

\[
G \circ F(x) \equiv \ln F(x) - H(x) \equiv 0 \pmod {x ^ n} \tag{5.5.10}
\]

运用式 \((5.5.5)\) 可得 ：

\[
F(x) \equiv F_0(x) - \frac{\ln F_0(x) - H(x)}{\frac{1}{F_0(x)}} \equiv F_0(x)[1 - \ln F_0(x) + H(x)] \pmod {x ^ n} \tag{5.5.11}
\]

时间复杂度 \(T(n) = T\left(\frac{n}{2}\right) + \Theta(n \log n) = \Theta(n \log n)\)。

```cpp
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 3e5, mod = 998244353;

int n, k, F[N], rev[N], FI[N], GI[N], iF[N], FE[N], GE[N], lnF[N];

int Pow (int a, int k) {
    int res = 1;
    for (; k; a = 1ll * a * a % mod, k >>= 1)
        if (k & 1) res = 1ll * res * a % mod;
    return res;
}

void NTT (int len, int *F, bool type) {
    rep(i, 0, len - 1) if (i < rev[i]) swap(F[i], F[rev[i]]);
    for (int k = 1; k < len; k <<= 1) {
        int eps = Pow(type ? 3 : 332748118, (mod - 1) / (k << 1));
        for (int i = 0; i < len; i += (k << 1))
            for (int j = i, g = 1; j < i + k; j++, g = 1ll * g * eps % mod) {
                int tmp1 = F[j], tmp2 = 1ll * g * F[j + k] % mod;
                F[j] = tmp1 + tmp2 >= mod ? tmp1 + tmp2 - mod : tmp1 + tmp2;
                F[j + k] = tmp1 - tmp2 < 0 ? tmp1 - tmp2 + mod : tmp1 - tmp2;
            }
    }
}

void INV (int n, int *F) {
    rep(i, 0, n << 2) FI[i] = GI[i] = 0;
    GI[0] = Pow(F[0], mod - 2);
    for (int len = 4, ln = 2; len <= n << 2; len <<= 1, ln++) {
        rep(i, 0, (len >> 1) - 1) FI[i] = F[i];
        rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
        NTT(len, GI, true), NTT(len, FI, true);
        rep(i, 0, len - 1) GI[i] = 1ll * GI[i] * (2 - 1ll * GI[i] * FI[i] % mod + mod) % mod;
        NTT(len, GI, false);
        int Inv = Pow(len, mod - 2);
        rep(i, 0, (len >> 1) - 1) GI[i] = 1ll * GI[i] * Inv % mod;
        rep(i, len >> 1, len - 1) GI[i] = 0;
    }
    rep(i, 0, n) iF[i] = GI[i];
}

void LN (int n, int *F) {
    INV(n, F);
    rep(i, 0, n - 1) F[i] = 1ll * (i + 1) * F[i + 1] % mod;
    F[n] = 0;
    int len = 1, ln = 0;
    for (; len < n << 1; len <<= 1, ln++);
    rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
    NTT(len, F, true), NTT(len, iF, true);
    rep(i, 0, len - 1) F[i] = 1ll * F[i] * iF[i] % mod;
    NTT(len, F, false);
    int Inv = Pow(len, mod - 2);
    rep(i, 0, n - 1) F[i] = 1ll * F[i] * Inv % mod;
    rep(i, n, len - 1) F[i] = 0;
    dep(i, n, 1) F[i] = 1ll * Pow(i, mod - 2) * F[i - 1] % mod;
    F[0] = 0;
}

void EXP (int n, int *F) {
    rep(i, 0, (n << 2)) FE[i] = GE[i] = 0;
    GE[0] = exp(F[0]);
    for (int len = 2, ln = 1; len <= n << 2; len <<= 1, ln++) {
        rep(i, 0, (len >> 1) - 1) FE[i] = F[i], lnF[i] = GE[i];
        LN((len >> 1) - 1, lnF);
        rep(i, 0, len - 1) rev[i] = (rev[i >> 1] >> 1) + (i & 1) * (1 << ln - 1);
        NTT(len, GE, true), NTT(len, FE, true), NTT(len, lnF, true);
        rep(i, 0, len - 1) GE[i] = 1ll * GE[i] * (1 - lnF[i] + FE[i] + mod) % mod;
        NTT(len, GE, false);
        int Inv = Pow(len, mod - 2);
        rep(i, 0, len - 1) GE[i] = 1ll * GE[i] * Inv % mod;
    }
    rep(i, 0, n) F[i] = GE[i];
}

void read (int &x) {
    x = 0; char c = getchar();
    while (c < '0' || c > '9') c = getchar();
    while (c >= '0' && c <= '9')
        x = (10ll * x + (c ^ 48)) % mod, c = getchar();
}

int main () {

    read(n), n--;
    rep(i, 0, n) read(F[i]);

    EXP(n, F);

    rep(i, 0, n) printf("%d ", F[i]);

    return 0;
}
```

### 多项式三角函数

#### 三角函数

给定多项式 \(F(x)\)，求模 \(x^{n}\) 意义下的 \(\sin F(x), \cos F(x)\) 与 \(\tan F(x)\)。

首先由欧拉公式 \(\left(e^{i x}=\cos x+i \sin x\right)\) 可以得到三角函数的另一个表达式 ：

\[
\begin{aligned}
&\sin x=\frac{e^{i x}-e^{-i x}}{2 i} \\
&\cos x=\frac{e^{i x}+e^{-i x}}{2}
\end{aligned}
\]

那么代入 \(F(x)\) 就有 :

\[
\begin{aligned}
\sin F(x) &=\frac{\exp [iF(x)] - \exp [-iF(x)]}{2i} \\
\cos F(x) &=\frac{\exp [iF(x)] + \exp [-iF(x)]}{2}
\end{aligned}
\]

直接按上述表达式编写程序即可得到模 \(x^{n}\) 意义下的 \(\sin F(x)\) 与 \(\cos F(x)\)。

再由 \(\tan F(x)=\frac{\sin F(x)}{\cos F(x)}\) 可求得 \(\tan F(x)\)。

时间复杂度 \(\Theta(n \log n)\)。

#### 反三角函数

仿照求多项式对数函数的方法，对反三角函数求导再积分可得 ：

\[
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d} x} \arcsin x &=\frac{1}{\sqrt{1-x^{2}}} \\
\arcsin x &=\int \frac{1}{\sqrt{1-x^{2}}} \mathrm{~d} x \\
\frac{\mathrm{d}}{\mathrm{d} x} \arccos x &=-\frac{1}{\sqrt{1-x^{2}}} \\
\arccos x &=-\int \frac{1}{\sqrt{1-x^{2}}} \mathrm{~d} x \\
\frac{\mathrm{d}}{\mathrm{d} x} \arctan x &=\frac  
\arctan x &=\int \frac{1}{1+x^{2}} \mathrm{~d} x
\end{aligned}
\]

那么代入 \(F(x)\) 就有:

\[
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d} x} \arcsin F(x) &=\frac{F^{\prime}(x)}{\sqrt{1-F^{2}(x)}} \\
\arcsin F(x) &=\int \frac{F^{\prime}(x)}{\sqrt{1-F^{2}(x)}} \mathrm{d} x \\
\frac{\mathrm{d}}{\mathrm{d} x} \arccos F(x) &=-\frac{F^{\prime}(x)}{\sqrt{1-F^{2}(x)}} \\
\arccos F(x) &=-\int \frac{F^{\prime}(x)}{\sqrt{1-F^{2}(x)}} \mathrm{d} x \\
\frac{\mathrm{d}}{\mathrm{d} x} \arctan F(x) &=\frac{F^{\prime}(x)}{1+F^{2}(x)} \\
\arctan F(x) &=\int \frac{F^{\prime}(x)}{1+F^{2}(x)} \mathrm{d} x
\end{aligned}
\]

直接按式子求就可以了。

时间复杂度均为 \(\Theta(n \log n)\)。
