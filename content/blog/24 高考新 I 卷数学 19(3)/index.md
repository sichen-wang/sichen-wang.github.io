---
title: "24 高考新 I 卷数学 19(3)"
date: "2024-06-08 16:03:33"
card_summary: ""
slug: "24 高考新 I 卷数学 19(3)"
aliases:
  - "/blog/24-xin-gao-kao-i-juan-shu-xue-19-3/"
tags:
  - "High School Math"
categories:
  - "Courses"
---

对 \(m = 1, 2\), 取几组合法 \((i, j)\) 即证.

对 \(m \geqslant 3\), 设 \(f_{m}\) 表示 \(a_{1 \sim 4m + 2}\) 中能取出的合法数对数量.

注意到 \(a_{1 \sim 4m + 2}\) 中任意长度为 \(4l + 2\) 的子区间对应的答案均为 \(f_{l}\), 则取分界点 \(p_{1} = 4, p_{2} = 4m - 2\) 进行容斥.

<div>
\[
\begin{aligned}
f_m &= f_m[i \not\in [1, p_1]~\textrm{or}~j \not\in [p_2 + 1, 4m + 2]] + f_m[i \in [1, p_1]~\textrm{and}~j \in [p_2 + 1, 4m + 2]]\\
&= f_m[i, j \in [p_1 + 1, 4m + 2]] + f_m[i, j \in [1, p_2]] - f_m[i, j \in [p_1 + 1, p_2]] \\&~~~~+ f_m[i \in [1, p_1]~\textrm{and}~j \in [p_2 + 1, 4m + 2]]\\
&= 2f_{m - 1} - f_{m - 2} + f_m[i \in [1, p_1]~\textrm{and}~j \in [p_2 + 1, 4m + 2]]
\end{aligned}
\]
</div>

考虑求 \(f_{m}[i \in [1, p_{1}]\ \textrm{and}\ j \in [p_{2} + 1, 4m + 2]]\) 的下界.

- 显然 \((i, j) = (1, 4m + 2)\) 是合法的.
- 对于 \((i, j) = (2, 4m + 1)\), 当 \(m = 3\) 时其合法性在第 \((2)\) 问中已证. 当 \(m \gt 3\) 时, 从前后各取 \(2\) 个下标公差为 \(2\) 的子序列, 注意到只看子区间 \([9, 4m - 6]\), 其中 \(10\) 和 \(4m - 7\) 已经被取过了, 于是变成了等价的子问题. 故归纳可证 \((i, j) = (2, 4m + 1)\) 是合法的.

此时有 \(f_{m}[i \in [1, p_{1}]\ \textrm{and}\ j \in [p_{2} + 1, 4m + 2]] \geqslant 2\), 于是 \(f_{m} \geqslant 2f_{m - 1} - f_{m - 2} + 2\).

取 \(f^{\prime}_{m} = 2f^{\prime}_{m - 1} - f^{\prime}_{m - 2} + 2 \leqslant f_{m}, f^{\prime}_{1} = 3, f^{\prime}_{2} = 7\).

变换得 \((f^{\prime}_{m} - f^{\prime}_{m - 1}) = (f^{\prime}_{m - 1} - f^{\prime}_{m - 2}) + 2\), 由熟知的方法解得 \(f_{m} \geqslant f^{\prime}_{m} = m^{2} + m + 1\).

于是 \(P_{m} = \frac{f_{m}}{\binom{4m + 2}{2}} \geqslant \frac{f^{\prime}_{m}}{\binom{4m + 2}{2}} = \frac{m^{2} + m + 1}{8m^{2} + 6m + 1} \gt \frac{1}{8}\), 原命题得证.
