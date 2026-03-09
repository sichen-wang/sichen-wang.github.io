---
title: "「省选联考 2021」矩阵游戏"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "「省选联考 2021」矩阵游戏"
aliases:
  - "/blog/sheng-xuan-lian-kao-2021-ju-zhen-you-xi/"
tags:
  - "OI"
categories:
  - "CP"
---

## Sol.

首先可以发现，若不考虑 \(a_{i} \leqslant 10^{6}\) 的限制，那么构造一组合法解是容易的。

同时可以发现，如果对一行或一列进行 \(+1, -1, +1, -1, \cdots \) 操作，那么得到的 \(a_{i}\) 还是合法的。

设 \(c_{i}\) 和 \(d_{i}\) 分别表示每行，每列进行了多少次操作，下面两个矩阵即为 \(a_{i, j}\) 得到真实值需要加上修改值的系数：

\[
\begin{bmatrix}
+1 & -1 & +1 & -1 \\
+1 & -1 & +1 & -1 \\
+1 & -1 & +1 & -1 \\
+1 & -1 & +1 & -1 \\
\end{bmatrix}
\rm and
\begin{bmatrix}
+1 & +1 & +1 & +1 \\
-1 & -1 & -1 & -1 \\
+1 & +1 & +1 & +1 \\
-1 & -1 & -1 & -1 \\
\end{bmatrix}
\]

列出需要满足的方程 ：
\[
0 \leqslant a_{i, j} \pm c_i \pm d_j \leqslant 10 ^ 6
\]

可以发现，若将 \(c_{i}\) 和 \(d_{i}\) 作为未知数，可能会出现 “求和约束”，这是难以解决的。

观察到发生这个问题的本质是因为在两个矩阵的相同位置出现了相同的符号，于是考虑重构矩阵：

\[
\begin{bmatrix}
+1 & -1 & +1 & -1 \\
-1 & +1 & -1 & +1 \\
+1 & -1 & +1 & -1 \\
-1 & +1 & -1 & +1 \\
\end{bmatrix}
\rm and
\begin{bmatrix}
-1 & +1 & -1 & +1 \\
+1 & -1 & +1 & -1 \\
-1 & +1 & -1 & +1 \\
+1 & -1 & +1 & -1 \\
\end{bmatrix}
\]

于是此时就可以使用差分约束的常规求解方式了。

使用 \(\rm SPFA\) 的时间复杂度为 \(\Theta[n^{2} (n + m)]\)，常数很小，可以通过。

## Code

```cpp
#include <bits/stdc++.h>
using namespace std;

#define int long long

const int N = 300 + 10, M = N * N << 1;

int T, n, m, a[N][N], b[N][N];
int last[N << 1], to[M], Next[M], W[M], tot;
int vis[N << 1], dis[N << 1], num[N << 1];
queue <int> Q;

void Link (int u, int v, int w) {
    to[++tot] = v, W[tot] = w, Next[tot] = last[u], last[u] = tot;
}

signed main () {

    scanf("%lld", &T); while (T--) {
        scanf("%lld%lld", &n, &m);
        tot = 0;
        for (int i = 0; i <= n + m; i++)
            last[i] = num[i] = 0, vis[i] = false, dis[i] = 1e9;
        while (!Q.empty()) Q.pop();
        for (int i = 2; i <= n; i++)
            for (int j = 2; j <= m; j++)
                scanf("%lld", &b[i][j]);
        for (int i = 1; i <= n; i++) a[i][1] = 0;
        for (int i = 1; i <= m; i++) a[1][i] = 0;
        for (int i = 2; i <= n; i++)
            for (int j = 2; j <= m; j++)
                a[i][j] = b[i][j] - a[i - 1][j] - a[i][j - 1] - a[i - 1][j - 1];

        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                if ((i + j) & 1) Link(n + j, i, a[i][j]), Link(i, n + j, 1e6 - a[i][j]);
                else Link(i, n + j, a[i][j]), Link(n + j, i, 1e6 - a[i][j]);
        for (int i = 1; i <= n + m; i++) Link(0, i, 0);

        dis[0] = 0, Q.push(0), vis[0] = 1;
        bool flag = false;
        while (!Q.empty()) {
            int u = Q.front();
            if (++num[u] > 10) { flag = true; break; }
            Q.pop(), vis[u] = false;
            for (int i = last[u]; i; i = Next[i])
                if (dis[to[i]] > dis[u] + W[i]) {
                    dis[to[i]] = dis[u] + W[i];
                    if (!vis[to[i]]) Q.push(to[i]), vis[to[i]] = true;
                }
        }

        if (flag) { puts("NO"); continue; }
        puts("YES");
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if ((i + j) & 1) a[i][j] += dis[n + j] - dis[i];
                else a[i][j] += dis[i] - dis[n + j];
                printf("%lld ", a[i][j]);
            }
            puts("");
        }
    }

    return 0;
}
```
