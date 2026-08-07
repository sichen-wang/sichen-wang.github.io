---
title: "整除性校验的本质"
date: "2024-04-09 16:43:16"
card_summary: ""
slug: "整除性校验的本质"
aliases:
  - "/blog/zheng-chu-xing-jian-yan-de-ben-zhi/"
tags:
  - "Number Theory"
  - "Divisibility Tests"
categories:
  - "Research"
---

从小学开始我们就知道, 一个数能被 \(3\) 整除当且仅当其各位数字之和能被 \(3\) 整除. 一个数能被 \(4\) 整除, 当且仅当其最后 \(2\) 位数能被 \(4\) 整除. 一个数能被 \(11\) 整除, 当且仅当其奇数位减去偶数位数字之和能被 \(11\) 整除(个位数记为第 \(1\) 位).

长大一点后, 我们可以用数学语言来刻画这个规律 :

\[
\begin{cases}
\overline{a_ta_{t - 1}\cdots a_2a_1} \equiv a_1 + a_2 + \cdots + a_t \pmod 3 \\
\overline{a_ta_{t - 1}\cdots a_2a_1} \equiv \overline{a_2a_2} \pmod 4 \\
\overline{a_ta_{t - 1}\cdots a_2a_1} \equiv a_1 - a_2 + a_3 - \cdots + (-1)^{t - 1} a_t \pmod {11} \\
\overline{a_ta_{t - 1}\cdots a_2a_1} \equiv \overline{a_3a_2a_1} - \overline{a_6a_5a_4} + \cdots + (-1)^{\frac{t}{3} - 1} \overline{a_ta_{t - 1}a_{t - 2}} \pmod 7
\end{cases}
\]

容易发现, 其分为 \(3\) 类 :

- 第一类: \(x\) 与 \(x\) 的末 \(k\) 位在模 \(n\) 意义下同余.
- 第二类: \(x\) 与 \(x\) 每 \(k\) 位一段求和得到的数在模 \(n\) 意义下同余.
- 第三类: \(x\) 与 \(x\) 每 \(k\) 位一段正负交替求和得到的数在模 \(n\) 意义下同余.

现在我们来探寻 \(b\) 进制数在模 \(n\) 意义下可以使用哪种同余化简方式(或不满足三类中任意一种).

1. 若存在 \(k\) 满足 \(b^{k} \equiv 0 \pmod n\), 那么 \(\overline{a_{t}a_{t - 1}\cdots a_{k + 1}00 \cdots 0} \equiv 0 \pmod n\), 则 \(\overline{a_{t}a_{t - 1}\cdots a_{2}a_{1}} \equiv \overline{a_{k}a_{k - 1}\cdots a_{2}a_{1}} \pmod n\), 可以使用第一类化简方式.
2. 若存在 \(k\) 满足 \(b^{k} \equiv 1 \pmod n\), 那么 \(\overline{a_{t}a_{t - 1}\cdots a_{k + 1}00 \cdots 0} \equiv \overline{a_{t}a_{t - 1}\cdots a_{k + 1}} \pmod n\), 则 \(\overline{a_{t}a_{t - 1}\cdots a_{2}a_{1}} \equiv \overline{a_{k}a_{k - 1}\cdots a_{1}} + \overline{a_{2k}a_{2k - 1}\cdots a_{k + 1}} + \cdots \pmod n\), 可以使用第二类化简方式.
3. 若存在 \(k\) 满足 \(b^{k} \equiv -1 \pmod n\), 那么 \(\overline{a_{pk}a_{pk - 1}\cdots a_{(p - 1)k + 1} 00\cdots 0} \equiv (-1)^{p}\overline{a_{pk}a_{pk - 1}\cdots a_{(p - 1)k + 1}}\), 则 \(\overline{a_{t}a_{t - 1}\cdots a_{2}a_{1}} \equiv \overline{a_{k}a_{k - 1}\cdots a_{1}} - \overline{a_{2k}a_{2k - 1}\cdots a_{k + 1}} + \cdots \pmod n\), 可以使用第三类化简方式.

于是想找到 \(b\) 进制数在模 \(n\) 意义下的化简方式, 只需要找到最小的 \(k\) 满足 \(b^{k} \equiv 0\ \textrm{or}\ 1\ \textrm{or}- 1\) 即对应第 \(1/2/3\) 类化简方式. 若直到 \(k\) 等于 \(b\) 的幂在模 \(n\) 意义下的循环节长度仍未找到满足条件的 \(k\), 则 \(b\) 进制数在模 \(n\) 意义下不能使用这 \(3\) 种方式化简.

一种找最小 \(k\) 的代码实现如下 :

```cpp
#include <bits/stdc++.h>
using namespace std;

int T, b, n;
unordered_map <int, bool> vis;

int main () {
    scanf("%d", &T); while (T--) {
        scanf("%d%d", &b, &n), b %= n;
        int a = 0, k = 1, tmp = b;
        while (b != 0 && b != 1 && b != n - 1 && !vis[b]) {
            vis[b] = true;
            b = 1ll * b * tmp % n, k++;
        }
        if (b == 0) a = 1;
        if (b == 1) a = 2;
        if (b == n - 1) a = 3;
        a ? printf("kind = %d, k = %d\n", a, k) : puts("0");
        vis.clear();
    }
    return 0;
}
```
