---
title: "树上背包"
date: "2024-06-22 15:11:24"
card_summary: ""
slug: "树上背包"
aliases:
  - "/blog/shu-shang-bei-bao/"
tags:
  - "Dynamic Programming"
  - "Trees"
categories:
  - "CP"
---

## 选取 m 个结点

这是最普遍的情况, 从树中选取 \(m\) 个结点, 最大化它们的价值之和.

符合直觉地, 设 \(f_{u, i}\) 表示从以 \(u\) 为根的子树中选取了 \(i\) 个结点的最大价值之和. 转移是显然的:

\[
f_{u, i + j} = \max\{f_{u, i} + f_{v, j}\}
\]

其中 \(i\), \(j\) 的范围应当分别为 \(u\) 此前枚举的子树大小和, 以 \(v\) 为根的子树大小.

其最优性和可行性都是显然的, 我们考虑这个算法的复杂度. 看起来似乎是 \(\Theta(n^{3})\), 但事实上对于任意点对 \((i \in S_{u}, j \in S_{v})\), 它只会在 \(u\) 处被枚举一次. 于是时间复杂度实际上是 \(\Theta(n^{2})\).

## 选取结点的代价之和至多为 m

在这个问题中为每个结点引入了代价, 此时上述的复杂度分析不再适用.

我们不妨考虑换一种思路, 正常的 \(0/1\) 背包复杂度之所以为 \(\Theta(nm)\), 是因为每次只需要对一个物品做是否选取的决策. 在这里, 我们同样考虑将物品独立起来, 只考虑当前物品选或不选. 为了保证无后效性, 接下来的结点编号都被重新设为其在后序遍历中的时间戳.

设 \(f_{i, j}\) 表示考虑了前 \(i\) 个物品, 背包大小为 \(j\), 能取到的最大价值和.

- 若选该物品, 则可以选择它子树中的物品, \(f_{i, j} \leftarrow f_{i - 1, j - w_{i}} + v_{i}\).
- 若不选该物品, 则它子树内的物品都不可以选, 而子树中的编号恰好是连续的, 于是 \(f_{i, j} \leftarrow f_{i - siz_{i}, j}\).

这样转移时间复杂度即为 \(\Theta(nm)\).

```cpp
int n, m, dfn;
std::vector<std::vector<int>> E, f;
std::vector<int> w, v, siz;

void dfs (int u) {
    for (int v : E[u]) dfs(v), siz[u] += siz[v];
    dfn++;
    for (int j = 0; j <= m; j++) {
        f[dfn][j] = f[dfn - siz[u]][j];
        if (j >= w[u]) f[dfn][j] = std::max(f[dfn][j], f[dfn - 1][j - w[u]] + v[u]);
    }
}

int knapsack_on_tree () {
    siz = std::vector<int>(n + 1, 1);
    f = std::vector<std::vector<int>>(n + 2, std::vector<int>(m + 1));
    dfs(0);
    return f[n + 1][m];
}
```
