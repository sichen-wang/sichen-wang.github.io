---
title: "Project Euler Problem 918"
date: "2025-01-09 13:57:54"
card_summary: ""
tags:
  - "Project Euler"
  - "Integer Sequences"
categories:
  - "CP"
---

定义数列 \(\{a_{n}\}\) 满足 \(a_{1} = 1\), 对于 \(n \geqslant 1\) 有:
\[
\begin{aligned}
a_{2n} &= 2a_n \\
a_{2n + 1} &= a_n - 3a_{n + 1}
\end{aligned}
\]

定义 \(S_{n} = \sum\limits_{i = 1}^{n} a_{i}\), 求 \(S_{k}(k = 10^{12})\).

---
\[
\begin{aligned}
S_{2n} &= (a_1 + a_3 + \cdots + a_{2n - 1}) + (a_2 + a_4 + \cdots + a_{2n}) \\
&= [a_1 + (a_1 - 3a_2) + \cdots + (a_{n - 1} - 3a_n)] + (2a_1 + 2a_2 + \cdots + 2a_n) \\
&= 4a_1 + (-2a_1 - 2a_2 - \cdots - 2a_{n - 1} - 3a_n) + (2a_1 + 2a_2 + \cdots + 2a_n) \\
&= 4 - a_n
\end{aligned}
\]

故要求 \(S_{2n}\) 只需递归求 \(a_{n}\) 即可.

```cpp
#include <bits/stdc++.h>

using i64 = long long;
constexpr i64 n = 1e12;

i64 a(i64 i) {
    if (i == 1) return 1;
    if (i & 1) return a(i >> 1) - 3 * a(i + 1 >> 1);
    else return a(i >> 1) << 1;
}

int main() {
    std::cout << 4 - a(n >> 1);
    return 0;
}
```

Answer \(= -6999033352333308\)
