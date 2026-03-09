---
title: "向量三重积"
date: "2025-02-23 20:24:25"
card_summary: ""
slug: "向量三重积"
aliases:
  - "/blog/xiang-liang-san-chong-ji/"
tags:
  - "Geometry"
  - "Linear Algebra"
categories:
  - "Courses"
---

存在**向量三重积**公式
\[
\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}
\]

---

设向量为：
\[
\mathbf{a} = (a_1, a_2, a_3), \quad \mathbf{b} = (b_1, b_2, b_3), \quad \mathbf{c} = (c_1, c_2, c_3).
\]
\[
\mathbf{b} \times \mathbf{c} = \begin{pmatrix}
  b_2 c_3 - b_3 c_2 \\
  b_3 c_1 - b_1 c_3 \\
  b_1 c_2 - b_2 c_1
\end{pmatrix}
\]
\[
\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = \begin{pmatrix}
  a_2 (b_1 c_2 - b_2 c_1) - a_3 (b_3 c_1 - b_1 c_3) \\
  a_3 (b_2 c_3 - b_3 c_2) - a_1 (b_1 c_2 - b_2 c_1) \\
  a_1 (b_3 c_1 - b_1 c_3) - a_2 (b_2 c_3 - b_3 c_2)
\end{pmatrix}
\]

展开并整理各分量：

- 第一分量：

\[
a_2 b_1 c_2 - a_2 b_2 c_1 - a_3 b_3 c_1 + a_3 b_1 c_3 = b_1 (a_2 c_2 + a_3 c_3) - c_1 (a_2 b_2 + a_3 b_3)
\]

- 第二分量：

\[
a_3 b_2 c_3 - a_3 b_3 c_2 - a_1 b_1 c_2 + a_1 b_2 c_1 = b_2 (a_3 c_3 + a_1 c_1) - c_2 (a_3 b_3 + a_1 b_1)
\]

- 第三分量：

\[
a_1 b_3 c_1 - a_1 b_1 c_3 - a_2 b_2 c_3 + a_2 b_3 c_2 = b_3 (a_1 c_1 + a_2 c_2) - c_3 (a_1 b_1 + a_2 b_2)
\]

观察到每个分量中缺少 \(a_{1} b_{1} c_{1}\)（第一分量）、\(a_{2} b_{2} c_{2}\)（第二分量）、\(a_{3} b_{3} c_{3}\)（第三分量）

添加这些项后，表达式可统一写为：
\[
\mathbf{b} (\mathbf{a} \cdot \mathbf{c}) - \mathbf{c} (\mathbf{a} \cdot \mathbf{b})
\]
