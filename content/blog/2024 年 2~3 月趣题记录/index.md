---
title: "2024 年 2~3 月趣题记录"
date: "2024-04-09 16:37:05"
card_summary: ""
slug: "2024 年 2~3 月趣题记录"
aliases:
  - "/blog/2024-nian-2-3-yue-qu-ti-ji-lu/"
tags:
  - "AtCoder"
  - "Codeforces"
categories:
  - "CP"
---

# [CF1929D](https://codeforces.com/contest/1929/problem/D) (*1974)

给定一颗 \(n\) 个点的树, 求黑白染色的方案数, 使任意一条路径上的黑点数量不超过 \(2\).

\(2 \leqslant n \leqslant 3 \times 10^{5}, \mathrm{mod} = 998244353\).

---

最自然的想法肯定是设 \(f_{u, 0/1/2}\) 表示考虑以 \(u\) 为根的子树, 所有从 \(u\) 到叶子的链中, 包含黑点数量最大的恰好为 \(0/1/2\) 的方案数. 转移考虑 \(u\) 是否为黑点进行分类讨论即可.

但出题人给出了一种另辟蹊径的做法, 设 \(f_{u}\) 表示考虑以 \(u\) 为根的子树, 所有从 \(u\) 到叶子的链中, 包含黑点数量最大的**恰好**为 \(1\) 的方案数. 设 \(v \in son_{u}\), 则所有 \(v\) 的染色方案互不干扰, 故有 \(f_{u} = \prod (f_{v} + 1)\).

考虑如何计算被漏掉的, 存在黑色点对 \((u, v)\) 满足 \(u\) 是 \(v\) 的祖先的情况. 我们发现如果枚举 \(u\), \(\sum_{v \in son_{u}} f_{v}\) 即为点对 \((u, v)\) 的数量, 若枚举所有 \(u\), 则 \(2 \sim n\) 号结点恰好均被计算一次. 再加上不存在黑色点对 \((u, v)\) 满足 \(u\) 是 \(v\) 的祖先的情况 \(f_{1} + 1\), 答案即为 \(1 + \sum f_{u}\).

该算法时间复杂度 \(\Theta(n)\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 3e5 + 10, mod = 998244353;

int T, n, f[N];
vector <int> E[N];

void dfs (int u, int fa) {
    f[u] = 1;
    for (int v : E[u]) if (v != fa)
        dfs(v, u), f[u] = 1ll * f[u] * (f[v] + 1) % mod;
}

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    cin >> T; while (T--) {
        cin >> n;
        for (int u, v, i = 1; i < n; i++) {
            cin >> u >> v;
            E[u].push_back(v), E[v].push_back(u);
        }

        dfs(1, 0);
        
        int ans = 0;
        for (int i = 1; i <= n; i++) ans = (ans + f[i]) % mod;
        cout << (ans + 1) % mod << "\n";

        for (int i = 1; i <= n; i++) E[i].clear();
    }
    return 0;
}
```

# [CF1929E](https://codeforces.com/contest/1929/problem/D) (*2414)

有一棵 \(n\) 个顶点的树, 对于其上 \(k\) 对顶点 \((a_{1}, b_{1}), \ldots, (a_{k}, b_{k})\) 中的任意一对, 在顶点 \(a_{i}\) 与 \(b_{i}\) 之间的简单路径上至少有一条边为黑色. 为了满足该条件, 求树上最少有多少条黑色边.

\(n \leqslant 10^{5}, k \leqslant 20\).

---

**注意到选择的边一定是至少一条路径上深度最浅的边**.

证明: 选深度最浅的边更劣, 当且仅当可以构造出两条路径 \(L_{1},L_{2}\) 在某条边 \(e\) 处相交, 且满足:

- \(e\) 不是 \(L_{1}, L_{2}\) 最浅的边.
- \(e\) 的父边不同时属于 \(L_{1}, L_{2}\).

否则 \(e\) 用其父边替换一定不劣.

但是, 若 \(e\) 不是 \(L\) 最浅的边, 则 \(e\) 的父边一定属于 \(L\), 故 \(e\) 的父边同时属于 \(L_{1}, L_{2}\), 产生矛盾, 故原命题得证.

因此我们发现, 该树中可能成为答案的边最多 \(2k\) 条, 且每条边 \(e\) 分别对应了一个集合 \(S\), 满足 \(\forall L \in S, e \in L\).

考虑记 \(T_{i}\) 表示第 \(i\) 条有可能成为答案的边属于哪些路径, \(f_{S}\) 表示将 \(S\) 表示的路径全部覆盖至少需要选择多少条边, 转移时枚举选择哪条边加入即可, 方程为 \(f_{S | T_{i}} = \min\{f_{S} + 1\}\).

总时间复杂度 \(\Theta(nk + k2^{k})\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 10, K = 22;

int T, n, k, a[K], b[K], dep[N], fa[N], f[1 << K];
vector <int> E[N];
map <pair<int, int>, int> tag, M;

void dfs (int u, int f) {
    fa[u] = f, dep[u] = dep[f] + 1;
    for (int v : E[u]) if (v != f) dfs(v, u);
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    cin >> T; while (T--) {
        cin >> n;
        for (int u, v, i = 1; i < n; i++)
            cin >> u >> v, E[u].push_back(v), E[v].push_back(u);
        cin >> k;
        for (int i = 1; i <= k; i++) cin >> a[i] >> b[i];

        dfs(1, 0);
        for (int i = 0; i < k; i++) {
            int u = a[i + 1], v = b[i + 1];
            while (dep[u] > dep[v] && fa[u] != v) u = fa[u];
            while (dep[v] > dep[u] && fa[v] != u) v = fa[v];
            if (fa[u] == v) { tag[make_pair(v, u)] |= 1 << i; continue; }
            if (fa[v] == u) { tag[make_pair(u, v)] |= 1 << i; continue; }
            while (fa[u] != fa[v]) u = fa[u], v = fa[v];
            tag[make_pair(fa[u], u)] |= 1 << i;
            tag[make_pair(fa[v], v)] |= 1 << i;
        }
        for (int i = 0; i < k; i++) {
            int u = a[i + 1], v = b[i + 1];
            while (dep[u] > dep[v] && fa[u] != v) {
                if (tag[make_pair(fa[u], u)])
                    M[make_pair(fa[u], u)] |= 1 << i;
                u = fa[u];
            }
            while (dep[v] > dep[u] && fa[v] != u) {
                if (tag[make_pair(fa[v], v)])
                    M[make_pair(fa[v], v)] |= 1 << i;
                v = fa[v];
            }
            if (fa[u] == v) { M[make_pair(v, u)] |= 1 << i; continue; }
            if (fa[v] == u) { M[make_pair(u, v)] |= 1 << i; continue; }
            while (fa[u] != fa[v]){
                if (tag[make_pair(fa[u], u)])
                    M[make_pair(fa[u], u)] |= 1 << i;
                if (tag[make_pair(fa[v], v)])
                    M[make_pair(fa[v], v)] |= 1 << i;
                u = fa[u], v = fa[v];
            }
            M[make_pair(fa[u], u)] |= 1 << i;
            M[make_pair(fa[v], v)] |= 1 << i;
        }

        int lim = 1 << k;
        for (int S = 1; S < lim; S++) f[S] = 1e9;
        for (int S = 0; S < lim; S++) for (auto it : M)
            f[S | it.second] = min(f[S | it.second], f[S] + 1);
        cout << f[lim - 1] << "\n";

        for (int i = 1; i <= n; i++) E[i].clear();
        M.clear();
    }
    return 0;
}
```

# [ABC341G](https://atcoder.jp/contests/abc341/tasks/abc341_g) (*2208)

给定长度为 \(n\) 的序列 \(\{a_{n}\}\), 对每个整数 \(k \in [1, n]\), 求 \(\max_{r \geqslant k} \left\{\frac{1}{r - k + 1}\sum_{i = k}^{r} a_{i}\right\}\).

\(n \leqslant 2 \times 10^{5}, \forall i, a_{i} \leqslant 10^{6}\).

---

考虑将平均数转化为直线的斜率, 构造平面上如下 \(n + 1\) 个点 :

- 编号为 \(0\) 的点为 \((0, 0)\).
- 编号为 \(i (i \in [1, n] \cup \mathbb{Z})\) 的点为 \((i, a_{1} + a_{2} + \cdots + a_{i})\).

注意到 \(l \to r\) 的平均数即为点 \(l - 1\) 和 \(r\) 之间的斜率, 于是从右往左用单调栈维护一个上凸壳转移即可.

时间复杂度 \(\Theta(n)\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 10;

int n, sta[N], top;
long long s[N];
double ans[N];

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> s[i], s[i] += s[i - 1];

    sta[++top] = n;
    for (int i = n - 1; i >= 0; i--) {
        while (top > 1 && (s[sta[top - 1]] - s[i]) * (sta[top] - i) >= (s[sta[top]] - s[i]) * (sta[top - 1] - i)) top--;
        ans[i + 1] = 1.0 * (s[sta[top]] - s[i]) / (sta[top] - i);
        sta[++top] = i;
    }

    for (int i = 1; i <= n; i++)
        cout << fixed << setprecision(10) << ans[i] << "\n";
    return 0;
}
```

# [ARC172E](https://atcoder.jp/contests/arc172/tasks/arc172_e) (*2358)

有 \(q\) 次询问, 每次询问给定正整数 \(x\), 求最小的 \(n\) 满足 \(n^{n} \equiv x \pmod p\).

\(q \leqslant 10^{4}, 1 \leqslant x \lt p = 10^{9}, 2, 5 \nmid x\).

---

**引理**

设集合 \(U_{k}\) 为 \(10^{k} (k \in \mathbb{Z^{+}})\) 的简化剩余系, 命题 \(P_{k} : \{n^{n} \mid n \in U_{k}\} = U_{k}\) 成立.

**证明**

对于 \(P_{1}\), \(U_{1} = \{1, 3, 7, 9\}\). 注意到 \(1^{1} \equiv 1, 3^{3} \equiv 7, 7^{7} \equiv 3, 9^{9} \equiv 9 \pmod {10}\), 于是 \(P_{1}\) 成立.

对于 \(P_{2}\), 与 \(P_{1}\) 类似的, 同样注意到 \(n \in U_{2}\) 时, \(n\) 与 \(n^{n}\) 在模 \(10^{2}\) 意义下一一对应, 于是 \(P_{2}\) 成立.

假设 \(P_{k} (k \geqslant 2)\) 成立, 即 \(\{n^{n} \mid n \in U_{k}\} = U_{k}\).

注意到二项式定理 : \((a + b)^{k} = \sum_{i = 0}^{k} \binom{k}{i} a^{i} b^{k - i}\), 代入得

\[
(n+t \cdot10 ^ k)^{n+t \cdot10 ^ k} = \sum _ {i = 0} ^ {n+t \cdot10 ^ k} \dbinom{n+t \cdot10 ^ k}{i} (t \cdot10 ^ k) ^ i n ^ {n+t \cdot10 ^ k - i}
\]

注意到 \((t \cdot10^{k})^{2} \equiv 0 \pmod {10^{k + 1}}\), 于是

\[
\begin{aligned}
&\quad\sum _ {i = 0} ^ {n+t \cdot10 ^ k} \dbinom{n+t \cdot10 ^ k}{i} (t \cdot10 ^ k) ^ i n ^ {n+t \cdot10 ^ k - i}\\
&\equiv n ^ {n+t \cdot10 ^ k} + (n+t \cdot10 ^ k) \cdot n ^ {n+t \cdot10 ^ k - 1} \cdot t \cdot10 ^ k \pmod {10 ^ {k + 1}} \\
&\equiv n ^ {n+t \cdot10 ^ k} + n ^ {n+t \cdot10 ^ k} \cdot t \cdot10 ^ k \pmod {10 ^ {k + 1}} \\
&\equiv (n ^ n + n ^ n \cdot t \cdot10 ^ k) (n ^ {10 ^ k}) ^ t \pmod {10 ^ {k + 1}}
\end{aligned}
\]

注意到欧拉定理 : 若 \(a \perp m\), 则 \(a^{\varphi(m)} \equiv 1 \pmod m\), 其中 \(\varphi(x)\) 表示 \([1, x]\) 中与 \(x\) 互质的整数数量.

因为 \(\varphi(2^{k + 1}) = 2^{k}\), 且 \(n \perp 2^{k + 1}\), 故 \(n^{2^{k}} \equiv 1 \pmod {2^{k + 1}}\), 进而 \(n^{10^{k}}\equiv (n^{2^{k}})^{5^{k}} \equiv 1 \pmod {2^{k + 1}}\). 因为 \(\varphi (5^{k + 1}) = 4 \times 5^{k}\), 且 \(n \perp 5^{k + 1}\), 故 \(n^{4 \times 5^{k}} \equiv 1 \pmod {5^{k + 1}}\), 进而 \(n^{10^{k}} \equiv (n^{4 \times 5^{k}})^{2^{k - 2}} \equiv 1 \pmod {5^{k + 1}}\). 又因为 \(2^{k + 1} \perp 5^{k + 1}\), 因此 \(n^{10^{k}} \equiv 1 \pmod {10^{k + 1}}\). 代入得

\[
(n ^ n + n ^ n \cdot t \cdot10 ^ k) (n ^ {10 ^ k}) ^ t \equiv n ^ n \cdot (t \cdot 10 ^ k + 1) \pmod {10 ^ {k + 1}}
\]

于是 \(\{n^{n} \mid n \in U_{k + 1}\}\) 中的每个数 \((n+t \cdot10^{k})^{n+t \cdot10^{k}} \equiv n^{n} \cdot (t \cdot 10^{k} + 1) \pmod {10^{k + 1}}\).

假设存在 \(t_{i} \not= t_{j}\), 满足 \(n^{n} (t_{i} \cdot 10^{k} + 1) \equiv n^{n} (t_{j} \cdot 10^{k} + 1) \pmod {10^{k + 1}}\), 因为 \(n^{n} \perp 10^{k + 1}\), 所以 \(n^{n}\) 存在逆元(可除), 故解得 \(t_{i} = t_{j}\), 矛盾. 于是 \(\forall i \not= j, n^{n} (i \cdot 10^{k} + 1) \not\equiv n^{n} (j \cdot 10^{k} + 1) \pmod {10^{k + 1}}\).

于是 \(\{n^{n} \mid n \in U_{k + 1}\}\) 是个不重集得证, 即 \(\textrm{card}\{n^{n} \mid n \in U_{k + 1}\} = U_{k + 1}\).

因为我们构造 \(n^{n}\) 构成的集合的方式为, 令其尾数为 \(\{1, 3, 7, 9\}\) 其中之一, 不断向首位前添加 \(\{0, 1, \cdots, 9\}\), 于是 \(n^{n}\) 的尾数一定是 \(\{1, 3, 7, 9\}\) 其中之一. 又因为 \(U_{k + 1}\) 包含了所有小于 \(10^{k + 1}\) 且尾数为 \(\{1, 3, 7, 9\}\) 其中之一的正整数, 所以 \(\{n^{n} \mid n \in U_{k + 1}\} \subseteq U_{k + 1}\).

综上, \(P_{k} : \{n^{n} \mid n \in U_{k + 1}\} = U_{k + 1}\) 也即 \(P_{k + 1}\) 得证.

归纳可证原命题.

回到原问题, 显然 \(n^{n} \to x\) 的映射是可以 \(\Theta(\log n)\) 确定的, 于是我们考虑一位位确定 \(x \to n\) 的映射.

对于最后两位, 可以直接枚举 \(n\) 检验 \(n^{n} \equiv x \pmod {100}\) 是否成立.

假设后 \(k\) 位已经确定, 我们有 \(n^{n} \equiv x \pmod {10^{k}}\), 且 \((t \cdot 10^{k} + n)^{t \cdot 10^{k} + n} \equiv x \pmod {x^{k + 1}}\) 对且仅对一个 \(t \in \{0, 1, \cdots, 9\}\) 成立, 于是可以枚举 \(t\) 检验是否成立.

综上我们找到了一个 \(\Theta(k^{2})\) 单次查询 \(x \to n\) 的映射满足 \(n^{n} \equiv x \pmod {x^{k}}\) 的算法.

```cpp
#include <bits/stdc++.h>
using namespace std;

int q, x, n, fac[10];

int Pow (int a, int k, int mod) {
    int res = 1;
    for (; k; k >>= 1, a = 1ll * a * a % mod)
        if (k & 1) res = 1ll * res * a % mod;
    return res;
}

int main () {
    fac[0] = 1;
    for (int i = 1; i <= 9; i++) fac[i] = fac[i - 1] * 10;

    cin >> q; while (q--) {
        cin >> x;

        for (int i = 0; i <= 99; i++)
            if (Pow(i, i, 100) == x % 100) n = i;

        for (int k = 2; k <= 8; k++) {
            for (int t = 0; t <= 9; t++)
                if (Pow(t * fac[k] + n, t * fac[k] + n, fac[k + 1]) == x % fac[k + 1]) {
                    n += t * fac[k]; break;
                }
        }
        cout << n << "\n";
    }
    return 0;
}
```

# [CF1864F](https://codeforces.com/contest/1864/problem/F) (*2415)

存在一个长度为 \(n\) 的整数序列 \(\{a_{n}\}\), 有 \(q\) 个独立的查询, 每次给出 \(l, r\).

求最小的操作次数 \(m\), 将**值**在 \([l, r]\) 内的所有数字变成 \(0\). 单次操作被定义为 :

- 选择一个区间 \([x, y]\), 满足这个区间与之前的所有区间不相交或包含或被包含于之前的某个区间.
- 选择一个非负整数 \(z\), 将区间 \([x, y]\) 中的所有数减去 \(z\).

\(n, q \leqslant 10^{6}, \forall i, 1 \leqslant a_{i} \leqslant n\).

---

首先, 对于询问 \(l, r\), 我们可以只考虑满足 \(a_{i} \in [l, r]\) 的数.

注意到我们每次必将至少一个数减成 \(0\), 若这个数不是序列中的非 \(0\) 最小值 \(a_{p}\), 那么\(a_{p}\)之后还是要单独再减一次, 于是取 \(z = a_{p}\) 是不劣的. 另外, 将 \(a_{p}\) 置为 \(0\) 的同时给以 \(0\) 划分的联通区间内所有的数减去 \(z\) 一定是不劣的. 减完后, 序列又以 \(p\) 为分界点被划分为两个区间分别考虑.

对于朴素的策略, 每次只删一个数, 我们发现所需操作次数即为值在 \([l, r]\) 之间的元素数量 \(\ell\). 而若采取上述策略, 两个数 \(a_{i}, a_{j}\) 可能同时被删, 当且仅当 \(\forall k \in [i + 1, j - 1], a_{k} \geqslant a_{i} = a_{j}\ \textrm{or}\ a_{k} \lt l\), 记满足该条件的二元组 \((i, j)\) 数量为 \(\tau\), 最终所需操作次数即为 \(\ell - \tau\).

考虑将询问按 \(r\) 排序, 从小到大加入数, 那 \(\exists k \in [i + 1, j - 1], a_{k} \geqslant a_{i} = a_{j}\) 就不可能成立了, 于是仅需考虑 \(a_{k} \lt l\), 也即 \(\max_{k \in [i + 1, j - 1]} \lt l\). 这个是好维护的, 只需要一棵支持单点修改, 区间查询最大值的线段树.

而对于 \(l\) 的查询, 可以将线段树上查出的最大值插入值域树状数组, 查询小于 \(l\) 的数有多少个即为 \(\tau\). 注意, 由于我们只想求值域在 \([l, r]\) 中数对应的最大值小于 \(l\) 的数量, 所以要减去 \([1, l - 1]\) 中数对应的最大值小于 \(l\) 的数量, 可以发现就是 \([1, l - 1]\) 中数的数量减去不同的小于 \(l\) 的数的数量. 于是最终每个询问的答案就是已经插入线段树中数的数量减去当前树状数组中 \(1 \sim l - 1\) 的值, 再减去本质不同的小于 \(l\) 的数的数量.

时间复杂度 \(\Theta(n \log n)\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 10;

int n, q, dif[N], ans[N];
vector <int> p[N];
pair <int, pair<int, int> > s[N];

namespace ST {
    #define ls (p << 1)
    #define rs (p << 1 | 1)
    int Max[N << 2], l[N << 2], r[N << 2];

    void Build (int p, int L, int R) {
        Max[p] = 0, l[p] = L, r[p] = R;
        if (L == R) return;
        int mid = (L + R) >> 1;
        Build(ls, L, mid), Build(rs, mid + 1, R);
    }

    void Modify (int p, int pos, int k) {
        if (l[p] == pos && r[p] == pos) {
            Max[p] = k; return;
        }
        r[ls] >= pos ? Modify(ls, pos, k) : Modify(rs, pos, k);
        Max[p] = max(Max[ls], Max[rs]);
    }

    int Query (int p, int L, int R) {
        if (L > R) return 0;
        if (l[p] >= L && r[p] <= R) return Max[p];
        int res = 0;
        if (r[ls] >= L) res = max(res, Query(ls, L, R));
        if (l[rs] <= R) res = max(res, Query(rs, L, R));
        return res;
    }
}

namespace BIT {
    #define lowbit(x) (x & (-x))
    int t[N];

    void add (int pos) {
        if (pos == 0) { t[0]++; return; }
        for (; pos <= n; pos += lowbit(pos)) t[pos]++;
    }

    int Query (int pos) {
        int res = 0;
        for (; pos >= 1; pos -= lowbit(pos)) res += t[pos];
        return res + t[0];
    }
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    cin >> n >> q;
    for (int a, i = 1; i <= n; i++)
        cin >> a, p[a].push_back(i), dif[a] = 1;
    for (int i = 1; i <= n; i++) dif[i] += dif[i - 1];
    for (int i = 1; i <= q; i++)
        cin >> s[i].second.first >> s[i].first,
        s[i].second.second = i;

    sort(s + 1, s + q + 1);
    ST::Build(1, 1, n);
    for (int cnt = 0, pos = 0, k = 1; k <= q; k++) {
        int l = s[k].second.first, r = s[k].first;
        while (pos < r) {
            pos++, cnt += p[pos].size();
            if (p[pos].empty()) continue;
            int num = p[pos].size();
            for (int i = 1; i < num; i++)
                BIT::add(ST::Query(1, p[pos][i - 1] + 1, p[pos][i] - 1));
            for (int i : p[pos]) ST::Modify(1, i, pos);
        }
        ans[s[k].second.second] = cnt - BIT::Query(l - 1) - dif[l - 1];
    }

    for (int i = 1; i <= q; i++) cout << ans[i] << "\n";
    return 0;
}
```

# [ARC172D](https://atcoder.jp/contests/arc172/tasks/arc172_d) (*2936)

给定 \(n\) 和 \(\frac{n(n - 1)}{2}\) 组条件 \((a_{i}, b_{i})\), 要求在 \(n\) 维空间中放置 \(n\) 个坐标在 \([0, 10^{8}]\) 内的整点, 满足 \(\textrm{dis}(p_{a_{i}}, p_{b_{i}})\) 按照给出条件的顺序从小到大排序.

\(3 \leqslant n \leqslant 20\).

---

考虑先构造任意两点之间距离相等, 再细微调整使其满足条件.

不妨令

\[
\begin{pmatrix}
p_1 = [1, 0, 0, \cdots, 0] \\
p_2 = [0, 1, 0, \cdots, 0] \\
\cdots \\
p_n = [0, 0, 0, \cdots, 1] \\
\end{pmatrix}
\]

这样就能使任意两点之间距离为 \(\sqrt2\), 然后给每个点的每个维度加上一个极小量

\[
\begin{pmatrix}
p_1 = [1 + \varepsilon_{1, 1},\varepsilon_{1, 2} , \varepsilon_{1, 3}, \cdots, \varepsilon_{1, n}] \\
p_2 = [\varepsilon_{2, 1}, 1 + \varepsilon_{2, 2},\varepsilon_{2, 3} , \cdots, \varepsilon_{3, 3}] \\
\cdots \\
p_n = [\varepsilon_{n, 1}, \varepsilon_{n, 2},\varepsilon_{n, 3} , \cdots, 1 + \varepsilon_{n, n}] \\
\end{pmatrix}
\]

此时两点距离为

\[
\textrm{dis} ^ 2(p_i, p_j) = \sum_{k \not= i, j} (\varepsilon_{i, k} - \varepsilon_{j, k}) ^ 2 + (1 + \varepsilon_{i, i} - \varepsilon_{j, i}) ^ 2 + (\varepsilon_{i, j} - 1 - \varepsilon_{j, j}) ^ 2
\]

注意到二阶小量对构造结果的影响很小, 于是消去, 得

\[
\textrm{dis}(p_i, p_j) = \sqrt{1 + \varepsilon_{i, i} + \varepsilon_{j, j} - \varepsilon_{i, j} - \varepsilon_{j, i}} \cdot \sqrt2
\]

我们不妨设 \(i \lt j\) 且 \(\varepsilon_{i, i}, \varepsilon_{j, j}, \varepsilon_{j, i} = 0\), 则原命题转化为

\[
\sqrt{1 - \varepsilon_{a_1, b_1}} \lt \sqrt{1 - \varepsilon_{a_2, b_2}} \lt \cdots \lt \sqrt{1 - \varepsilon_{a_n, b_n}}
\]

将坐标等比例放大 \(L\) 倍, 可设 \(\varepsilon_{a_{i}, b_{i}}\) 为 \(-i\), 考虑到坐标不能为负数, 于是再将所有点的坐标加上 \(l\).

此题可取 \(L = 9 \times 10^{7}, l = \frac{n(n - 1)}{2}\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 22, L = 9e7;

int n, p[N][N];

int main () {
    cin >> n;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            p[i][j] = n * (n - 1) / 2 + L * (i == j);

    for (int a, b, i = 1; i <= n * (n - 1) / 2; i++)
        cin >> a >> b, p[a][b] -= i;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            printf("%d%c", p[i][j], " \n"[j == n]);
    return 0;
}
```

# [CF1905E](https://codeforces.com/contest/1905/problem/E) (*2484)

递归定义长度为 \(n\) 的线段树. 根节点为 \(1\), 代表区间 \([1, n]\). 若一个结点 \(p\) 代表的区间为 \([l, r]\), 那么当且仅当 \(l \not= r\) 时它存在两个子节点 \(2p\) 和 \(2p + 1\), 分别代表区间 \([l, \lceil\frac{l + r}{2}\rceil]\) 和 \([\lceil\frac{l + r}{2}\rceil + 1, r]\).

共 \(T\) 组询问, 每次给定 \(n\), 求长度为 \(n\) 的线段树对应的 \(\sum \textrm{LCA}(S)\), 其中 \(S\) 表示任意一个叶子节点的非空集合, \(\textrm{LCA}(S)\) 表示 \(S\) 中所有结点的最近公共祖先的编号. 答案对 \(998244353\) 取模.

\(T \leqslant 10^{3}, 2 \leqslant n \leqslant 10^{18}\).

---

首先考察结点 \((p, l, r)\) 的贡献, 其作为最近公共祖先当且仅当 \(2p\) 和 \(2p + 1\) 内均至少存在一个结点被选择, 且 \([l, r]\) 之外没有结点被选择. 故其贡献为 :

\[
p(2 ^ {\lceil\frac{l + r}{2}\rceil - l + 1} - 1)(2 ^ {r - \lceil\frac{l + r}{2}\rceil} - 1)
\]

注意到线段树每层最多存在两种长度的区间, 且相同长度的区间被算进贡献的次数是相同的, 于是考虑合并计算. 递归时维护当前长度 \(l\) 对应的结点编号和 \(s\), 数量 \(c\) 即可, 用 `map` 存储.

时间复杂度 \(\Theta(T\log^{2} n)\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 100, mod = 998244353;

int T, ans;
long long n;
set <long long> S;
map <long long, int> s, c;

void Build (long long l) {
    S.insert(l);
    if (l == 1) return;
    if (S.find((l + 1) / 2) == S.end()) Build((l + 1) / 2);
    if (S.find(l / 2) == S.end()) Build(l / 2);
}

int Pow (int a, long long k) {
    int res = 1;
    for (; k; k >>= 1, a = 1ll * a * a % mod)
        if (k & 1) res = 1ll * res * a % mod;
    return res;
}

int main () {
    cin >> T; while (T--) {
        cin >> n;
        S.clear(), Build(n);

        s.clear(), c.clear(), ans = 0, s[n] = c[n] = 1;
        for (auto it = S.rbegin(); it != S.rend(); it++) {
            long long l = *it, lx = (l + 1) / 2, ly = l / 2;
            if (l == 1) ans = (ans + s[l]) % mod;
            else {
                ans = (ans + 1ll * s[l] * (Pow(2, lx) - 1) % mod * (Pow(2, ly) - 1)) % mod;
                s[lx] = (s[lx] + 2ll * s[l]) % mod, c[lx] = (c[lx] + c[l]) % mod;
                s[ly] = (s[ly] + 2ll * s[l] + c[l]) % mod, c[ly] = (c[ly] + c[l]) % mod;
            }
        }

        cout << ans << "\n";
    }
    return 0;
}
```

# [CF1923E](https://codeforces.com/contest/1923/problem/E) (*2044)

给定一棵 \(n\) 个结点的树, 每个结点有一个 \([1, n]\) 中的颜色, 求满足以下条件的路径的数量 :

- 至少由 \(2\) 个结点组成.
- 路径的起点与终点颜色相同.
- 路径上起点和终点以外的点颜色与起点不同.

\(n \leqslant 2 \times 10^{5}\).

---

此处给出一个优于官方 \(\Theta(n \log n)\) 做法的线性做法.

考虑按 \(\rm dfs\) 序枚举树上的每个结点, 统计当前结点 \(u\) 能和前面结点构成的合法路径 \((u, v)\) 的数量. 可以发现若设 \(f\) 为 \(u\) 的祖先中最近的与 \(u\) 颜色相同的结点, 则合法的 \(v\) 可以用以下方式刻画 :

- 若 \(f\) 存在则将其计入答案, 否则设 \(f = fa(1) = 0\), 不计入答案.
- 遍历 \(u\) 至 \(f\) 路径上的每个结点 \(r\) (不含 \(u, f\)), 从 \(r\) 开始向其子树(不含包括 \(u\) 的这棵)中遍历, 遇到与 \(u\) 颜色相同的结点则停下, 并将其计入答案.

设 \(c_{i}\) 表示若 \(u\) 的颜色为 \(i\), 能被计入答案的结点数量.

- 因为以 \(u\) 为根的子树中所有想走出来的合法路径都会被 \(u\) 拦住, 所以进入子树时要将 \(c_{i}\) 设为 \(1\).
- 因为出以 \(u\) 为根的子树时原本的答案会还原, 且 \(u\) 也是合法路径的端点, 所以出子树时要将 \(c_{i}\) 加 \(1\).

使用这种策略遍历一遍整棵树即可算出答案.

时间复杂度 \(\Theta(n)\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 10;

int T, n, col[N], cf[N], c[N];
long long ans;
vector <int> E[N];

void dfs (int u, int fa) {
    ans += c[col[u]];
    int mark = c[col[u]];
    for (int v : E[u]) if (v != fa) c[col[u]] = 1, dfs(v, u);
    c[col[u]] = mark + 1;
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    cin >> T; while (T--) {
        cin >> n;
        for (int i = 1; i <= n; i++) cin >> col[i];
        for (int u, v, i = 1; i < n; i++)
            cin >> u >> v,
            E[u].push_back(v), E[v].push_back(u);

        dfs(1, 0), cout << ans << "\n";

        ans = 0;
        for (int i = 1; i <= n; i++)
            E[i].clear(), cf[i] = c[i] = 0;
    }
    return 0;
}
```

# [CF1918F](https://codeforces.com/contest/1918/problem/F) (*2696)

给定一颗 \(n\) 个结点的树, 从 \(1\) 开始在树上行走, 求走到过所有结点的最小步数.

- 操作 \(1\) : 移动到相邻的结点, 花费 \(1\) 步.
- 操作 \(2\) : 移动到 \(1\) 号结点, 无花费, 但操作 \(2\) 最多进行 \(k\) 次.

\(2 \leqslant n \leqslant 2 \times 10^{5}, 0 \leqslant k \leqslant 10^{9}\).

---

可以发现如下性质 :

- 操作 \(2\) 只会在叶子结点进行.
- 题目等效于要求最后需要回到 \(1\) 号结点, 但操作 \(2\) 可以进行 \(k + 1\) 次.
- 如果只使用操作 \(1\), 则每条边会经过恰好 \(2\) 次, 总共需要 \(2(n - 1)\) 步.

考虑求操作 \(2\) 最多能节省多少步数. 假设遍历顺序已经确定下来了, 那对于其中一对访问时间相邻的叶子结点 \((u, v)\) (相邻被定义为 \(u \to v\) 的路径上不存在其它叶子结点), 如果在 \(u\) 处使用操作 \(2\), 设 \(f = \textrm{LCA}(u, v)\), 能够节省的步数为 \(\textrm{dis}(u, v) - \textrm{dis}(1, v)\), 可转化为 \(\textrm{dis}(u, f) - \textrm{dep}(f)\).

考察每个非叶子结点 \(f\), 在以 \(f\) 为根的子树中如果存在某个叶节点使用了操作 \(2\), 考虑到要最大化 \(\textrm{dis}(u, f) - \textrm{dep}(f)\), 那么一定是深度最大的结点, 且它是最后一个被遍历到的. 于是对 \(f\) 的所有子节点 \(u\) 按以 \(u\) 为根的子树深度从小到大排序, 这样得出的叶节点访问顺序也即能最小化总步数的访问顺序.

注意到每个叶节点的贡献是独立的, 于是计算最大的 \(\sum \textrm{dis}(u, f) - \textrm{dep}(f)\) 只需要求出前 \(k\) 大即可.

时间复杂度 \(\Theta(n \log n)\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 10;

int n, k, fa[N], dep[N], siz[N], son[N], len[N], top[N], ans;
vector <int> E[N], leaf, val;

void dfs1 (int u, int f) {
    dep[u] = dep[f] + 1, siz[u] = 1;
    for (int v : E[u]) dfs1(v, u),
        siz[u] += siz[v], len[u] = max(len[u], len[v] + 1),
        son[u] = siz[v] > siz[son[u]] ? v : son[u];
}

void dfs2 (int u, int t) {
    top[u] = t;
    if (son[u]) dfs2(son[u], t);
    for (int v : E[u]) if (v != son[u]) dfs2(v, v);
}

int LCA (int u, int v) {
    while (top[u] != top[v]) {
        if (dep[top[u]] < dep[top[v]]) swap(u, v);
        u = fa[top[u]];
    }
    return dep[u] < dep[v] ? u : v;
}

int dis (int u, int v) {
    return dep[u] + dep[v] - 2 * dep[LCA(u, v)];
}

bool cmp (int a, int b) {
    return len[a]  < len[b];
}

void dfs3 (int u) {
    sort(E[u].begin(), E[u].end(), cmp);
    for (int v : E[u]) dfs3(v);
}

void dfs4 (int u) {
    if (E[u].empty()) leaf.push_back(u);
    for (int v : E[u]) dfs4(v);
}

int main () {
    scanf("%d%d", &n, &k);
    for (int i = 2; i <= n; i++)
        scanf("%d", &fa[i]), E[fa[i]].push_back(i);

    dfs1(1, 0), dfs2(1, 1), dfs3(1), dfs4(1);

    int num = leaf.size();
    for (int i = 0; i < num; i++)
        if (i < num - 1) val.push_back(dis(leaf[i], leaf[i + 1]) - dis(1, leaf[i + 1]));
        else val.push_back(dis(1, leaf[i]));
    
    sort(val.begin(), val.end(), greater <int> ());
    for (int i = 0; i <= k && i < num; i++)
        if (val[i] > 0) ans += val[i];
    printf("%d\n", 2 * (n - 1) - ans);
    return 0;
}
```

# [ARC173B](https://atcoder.jp/contests/arc173/tasks/arc173_b) (*1594+)

给定平面上的 \(n\) 个整点, 第 \(i\) 个点坐标为 \((x_{i}, y_{i})\).

问最多能用这些顶点构建多少个非退化三角形(每个点只能用一次).

\(3 \leqslant n \leqslant 300, |x_{i}|, |y_{i}| \leqslant 10^{9}.\)

---

设 \(l\) 为平面上穿过点数最多的直线, 其上点数为 \(m\).

- 若 \(m \geqslant n - \lfloor\frac{n}{3}\rfloor + 1\), 那么答案为 \(n - m\), 即每从 \(l\) 外取一个点, 从 \(l\) 内取两个点构成一个三角形.
- 若 \(m \leqslant n - \lfloor\frac{n}{3}\rfloor\), 那么可以取到答案上界 \(\lfloor\frac{n}{3}\rfloor\).

下归纳证明第二种情况的正确性, 假设对小于 \(n\) 个点的情况该结论均正确 :

尝试从 \(n\) 个点中选取 \(3\) 个先构成一个三角形, 钦点其中两个点从 \(l\) 上选, 则 \(l\) 上现在的点数 \(m' = m - 2\), 由 \(m \leqslant n - \lfloor\frac{n}{3}\rfloor\) 得 \(m' = m - 2 \leqslant n - \lfloor\frac{n}{3}\rfloor - 2 = n - 3 - \lfloor\frac{n - 3}{3}\rfloor\), 可以取到 \(n - 3\) 个点的答案上界 \(\lfloor\frac{n - 3}{3}\rfloor\), 进而 \(n\) 个点的第二种情况可以取到 \(n\) 个点的答案上界 \(\lfloor\frac{n}{3}\rfloor\) 得证. 归纳得原命题得证.

有这个结论, 则可以直接枚举两个点, 设过它们的直线为 \(l\) 并计算 \(m\), 时间复杂度 \(\Theta(n^{3})\), 可以通过原问题.

注意到若答案不为 \(\lfloor\frac{n}{3}\rfloor\) 则 \(l\) 上的点数占总点数的 \(\frac{2}{3}\) 以上, 用类摩尔投票法的方式来统计显然是一个更聪明的做法. 在一个栈中保存我们认为在 \(l\) 上的点, 若栈大小小于 \(2\) 则将当前点加入栈, 否则判断其跟栈内元素是否在同一条直线上. 若是, 则将其入栈, 否则踢出栈内一个元素. 注意到 \(l\) 上的元素为绝对众数, 所以最终栈内留下来的元素一定是 \(l\) 上的元素(若没留下来超过 \(1\) 个元素, 则说明栈中元素代表的 \(l\) 上的点数并非绝对众数, 答案为 \(\lfloor\frac{n}{3}\rfloor\)). 特别的, 若当前栈中只剩两个元素, 则需要全部踢出, 否则一个不在 \(l\) 上的点可能永远留在栈中. 注意到所求 \(l\) 上的点数大于总点数的 \(\frac{2}{3}\), 所以哪怕每次都踢出两个元素也不会影响投票法的正确性.

最后, 栈中剩下元素代表的 \(l\) 即为所求, 枚举判断一下有多少个点在 \(l\) 上即可.

时间复杂度被优化到 \(\Theta(n)\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 10;

int n, x[N], y[N], sta[N], top;

bool check (int i, int j, int k) {
    return (1ll * x[j] * y[k] - 1ll * y[j] * x[k])
         - (1ll * x[i] * y[k] - 1ll * y[i] * x[k])
         + (1ll * x[i] * y[j] - 1ll * y[i] * x[j]) == 0;
}

int main () {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> x[i] >> y[i];

    for (int i = 1; i <= n; i++) {
        if (top <= 1) sta[++top] = i;
        else if(check(sta[1], sta[2], i)) sta[++top] = i;
        else top -= 1 + (top == 2);
    }
    if (top < 2) return printf("%d\n", n / 3), 0;

    int m = 2;
    for (int i = 1; i <= n; i++)
        if (i != sta[1] && i != sta[2]) m += check(sta[1], sta[2], i);
    (m <= n - n / 3) ? printf("%d\n", n / 3) : printf("%d\n", n - m);
    return 0;
}
```

# [CF1946D](https://codeforces.com/contest/1946/problem/D) (*2006)

有一个长度为 \(n\) 的数列 \(\{a_{n}\}\) 和一个数 \(x\), 请找到最大的数\(k\), 使得可以选择一些数字对 \([l_{1}, r_{1}]\), \([l_{2}, r_{2}]\), \(\cdots\), \([l_{k}, r_{k}]\) 满足以下条件 :

- \(l_{1} = 1\), \(r_{k} = n\).
- 对于所有 \(i\) 从 \(1\) 到 \(k\) , \(l_{i} \leqslant r_{i}\).
- 对于所有 \(i\) 从 \(1\) 到 \(k - 1\), \(r_{i} + 1 = l_{i + 1}\).
- \((a_{l_{1}} \oplus a_{l_{1} + 1} \oplus \ldots \oplus a_{r_{1}}) | (a_{l_{2}} \oplus a_{l_{2} + 1} \oplus \ldots \oplus a_{r_{2}}) | \ldots | (a_{l_{k}} \oplus a_{l_{k} + 1} \oplus \ldots \oplus a_{r_{k}}) \leqslant x\).

如果不存在这样的 \(k\), 则输出 \(-1\).

---

设 \(s_{i} = \oplus_{j = 1}^{i} a_{j}\), 则原问题被转化为 \(s_{r_{1}}|(s_{r_{2}}\oplus s_{r_{1}})|\cdots|(s_{r_{k}} \oplus s_{r_{k - 1}}) \leqslant x\).

注意到 \(x | x \oplus y = x | y\), 于是问题被转化为从 \(\{s_{n}\}\) 中选尽可能多的数, 使其或和不超过 \(x\).

这就变成了经典问题, 枚举 \(x\) 最高的为 \(1\) 且或和中该位为 \(0\) 的是哪一位, 然后进行贪心即可.

时间复杂度 \(\Theta(n \log n)\).

```cpp
#include <bits/stdc++.h>
using namespace std;
 
const int N = 1e5 + 10;
 
int T, n, x, a[N], ans;
 
int calc (int y) {
    int res = 1;
    if ((a[n] | y) != y) return -1;
    for (int i = n - 1; i >= 1; i--)
        if ((a[i] | y) == y) res++;
    return res;
}
 
int main () {
    scanf("%d", &T); while (T--) {
        scanf("%d%d", &n, &x);
        for (int i = 1; i <= n; i++)
            scanf("%d", &a[i]), a[i] ^= a[i - 1];
 
        ans = -1;
        for (int k = 30; k >= 0; k--)
            if ((x >> k) & 1) ans = max(ans, calc(((x >> (k + 1)) << (k + 1)) + (1 << k) - 1));
        ans = max(ans, calc(x));
        printf("%d\n", ans);
    }
    return 0;
}
```

# [CF1944F2](https://codeforces.com/contest/1944/problem/F2) (*2828)

如果一个长度为 \(m\) 的数列 \(\{b_{m}\}\) 能通过若干次操作变成全 \(0\) 序列, 则该序列为合法的. 操作被定义为, 选择 \(1 \leqslant l \lt r \leqslant m\), 将所有满足 \(i \in [l, r]\) 的 \(b_{i}\) 减 \(1\).

给定 \(n, k, p\), 求有多少个长度为 \(n\) 的数列 \(\{a_{n}\}\) 是合法的, 且满足 \(\forall i, 0 \leqslant a_{i} \leqslant k\), 答案对 \(p\) 取模.

\(3 \leqslant n \leqslant 3000, 1 \leqslant k \leqslant n, 10^{8} \lt p \lt 10^{9}, p \in  \mathbb{P}\).

---

首先我们考虑\(\{a_{n}\}\) 合法的充要条件是什么, 容易想到为 \(\forall i, a_{i} \leqslant a_{i - 1} + a_{i + 1}\).

注意到 \(a_{i} \gt a_{i - 1} + a_{i + 1}\) 和 \(a_{i + 1} \gt a_{i} + a_{i + 2}\) 不可能同时成立, 于是同时计算合法和不合法的方案数只需要记录前 \(1\) 个元素. 具体来说, 设 \(f_{i, j}\) 为考虑到 \(a_{i}\), 且 \(a_{i} = j\) 的合法方案数, 设 \(g_{i},j\) 为考虑到 \(a_{i}\), 有且仅有 \(a_{i} = j\) 这一位不合法的方案数. 那么有转移式 :

\[
g_{i, j} = \sum_{t = 0}^k f_{i - 2}, t \times \max\{k - j - t, 0\}, f_{i, j} = \sum_{t = 0}^k f_{i - 1, t} - g_{i, j}
\]

前缀和优化后时间复杂度 \(\Theta(n^{2})\).

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 3e3 + 10;

int T, n, k, p, f[N][N], g[N][N], sum[N];

int main () {
    f[0][0] = 1;
    cin >> T; while (T--) {
        cin >> n >> k >> p;
        for (int sigma, i = 1; i <= n + 1; i++) {
            sum[0] = f[i - 2][0], sigma = f[i - 1][0];
            for (int j = 1; j <= k; j++)
                sum[j] = (sum[j - 1] + f[i - 2][j]) % p,
                sigma = (sigma + f[i - 1][j]) % p;
            for (int j = k; j >= 0; j--) {
                g[i][j] = (g[i][j + 1] + sum[k - 1 - j]) % p,
                f[i][j] = (sigma - g[i][j] + p) % p;
            }
        }
        cout << f[n + 1][0] << "\n";

        for (int i = 1; i <= n + 1; i++)
            for (int j = 0; j <= k; j++)
                f[i][j] = g[i][j] = 0;
    }
    return 0;
}
```

# [CF1944D](https://codeforces.com/contest/1944/problem/D) (*2072)

定义一个字符串为 \(\textrm {k-good}\) 的, 当且仅当其存在至少一个长度为 \(k\) 的子串不是回文的.

给定长度为 \(n\) 的字符串 \(s\), 共 \(q\) 次询问, 每次给定 \(l, r\), 求 \(\sum_{k} k[s_{l \sim r}\ \textrm{is\ k-good}]\).

\(n, q \leqslant 2 \times 10^{5}, 1 \leqslant l \lt r \leqslant n.\)

---

考虑计算一个特定的子串 \(t\) 对应的 \(\sum_{k} k[t\ \textrm{is\ k-good}]\). 对 \(k\) 分类讨论:

- \(k = 1\): 任意字符串均不是 \(\textrm {1-good}\) 的.
- \(k = |t|\): \(t\) 为 \(\textrm {|t|-good}\) 的当且仅当 \(t\) 本身为回文串.
- \(k\) 为偶数: 若 \(t\) 不为 \(\textrm {k-good}\) 的, 则任意长度为 \(k\) 的子串均为回文的, 则 \(t\) 中所有字符均相等.
- \(k\) 为奇数: 若 \(t\) 不为 \(\textrm {k-good}\) 的, 则任意长度为 \(k\) 的子串均为回文的, 则 \(t\) 中所有距离为 \(2\) 的字符均相等.

考虑如何判断 \(s\) 的子串是否满足以下几个条件:

- \(s_{l \sim r}\) 是回文的: 使用 \(\textrm{Manacher}\) 算法或哈希即可.
- \(s_{l \sim r}\) 是全部相等的: 对 \([s_{i} = s_{i - 1}]\) 做前缀和即可.
- \(s_{l \sim r}\) 是间隔相等的: 对 \([s_{i} = s_{i - 2}]\) 分奇偶做前缀和即可.

满足的条件判断出来后等差数列求和即可算出答案.

时间复杂度 \(\Theta(n + q)\).

```python
def manacher (n, s):
    if n == 0: return []
    res = [0] * (2 * n - 1)
    l, r = -1, -1
    for z in range(2 * n - 1):
        i = (z + 1) // 2
        j = z // 2
        p = 0 if i >= r else min(r - i, res[2 * (l + r) - z])
        while j + p + 1 < n and i - p - 1 >= 0:
            if s[j + p + 1] != s[i - p - 1]: break
            p += 1
        if j + p > r: l, r = i - p, j + p
        res[z] = p
    return res

T = int(input())
for _ in range(T):
    n, q = map(int, input().split())
    s = input().strip()
    p1 = [0] * (n + 2)
    p2 = [0] * (n + 2)
    for i in range(n + 1, -1, -1):
        if i >= n: p1[i] = p2[i] = i
        else:
            if i + 1 < n and s[i] != s[i + 1]: p1[i] = i
            else: p1[i] = p1[i + 1]
            if i + 2 < n and s[i] != s[i + 2]: p2[i] = i
            else: p2[i] = p2[i + 1]

    pal = manacher(n, s)
    for __ in range(q):
        l, r = map(int, input().split())
        l -= 1; r -= 1
        length = r - l + 1
        if p1[l] >= r:
            print(0)
            continue
        if p2[l] >= r - 1:
            k = length // 2
            print(k * (k + 1))
            continue
        ans = length * (length + 1) // 2 - 1
        if pal[l + r] >= length // 2: ans -= length
        print(ans)
```

# [ABC347F](https://atcoder.jp/contests/abc347/tasks/abc347_f) (*2120)

给定 \(n \times n\) 的由非负整数构成的矩阵, 要从中选出 \(3\) 个 \(m \times m\) 的不相交的子矩阵, 最大化所有子矩阵的元素和.

\(2 \leqslant n \leqslant 1000, 1 \leqslant m \leqslant \frac{n}{2}, a_{i, j} \leqslant 10^{9}\).

---

![](https://img.atcoder.jp/abc347/c8c4557905764a04a59ff89c7b249746.png)

尝试枚举三个子矩阵的相对位置关系, 可以发现, 一定存在以上 \(6\) 中划分方式的其中一种, 使 \(3\) 个子矩阵分属 \(3\) 个不同的区域, 且不会有任何部分被其它区域包含.

容易发现这 \(6\) 种划分方式本质上是两种.

- 对于 \(|\ |\) 型: 求出每一列上的点作为子矩阵左上角的点对应的最大元素和, 预处理列区间的最大值, 枚举划分方案即可.
- 对于 \(|-\) 型: 求出列前缀最大值和右上, 右下部分的前缀最大值, 枚举划分方案即可.

时间复杂度 \(\Theta(n^{2})\).

```python
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def calc (a):
    for i in range(n):
        for j in range(n - 1):
            a[i][j + 1] += a[i][j]
        a[i].append(0)
    for j in range(n):
        for i in range(n - 1):
            a[i + 1][j] += a[i][j]
    a.append([0] * (n + 1))
    b = [[0] * n for _ in range(n)]
    for i in range(m - 1, n):
        for j in range(m - 1, n):
            b[i][j] = a[i][j] - a[i][j - m] - a[i - m][j] + a[i - m][j - m]
    
    c = [max(b[i]) for i in range(n)]
    d = c[:]
    e = [0] * n
    res = 0
    for i in range(n - 1):
        d[i + 1] = max(d[i + 1], d[i])
    for i in range(n - m - 1, m - 2, -1):
        f = 0
        g = [0] * (i + m) + c[i + m : ]
        for j in range(n):
            e[j] = max(e[j], b[i + m][j])
        for j in range(2 * m - 1, n):
            f = max(f, e[j - m])
            res = max(res, d[i] + e[j] + f)
        for j in range(i + m, n - 1):
            g[j + 1] = max(g[j + 1], g[j])
        for j in range(i + 2 * m, n):
            res = max(res, d[i] + g[j - m] + c[j])
    return res

ans = 0
for _ in range(4):
    ans = max(ans, calc([list(l) for l in zip(*a)]))
    a = [list(l)[ : : -1] for l in zip(*a)]
print(ans)
```
