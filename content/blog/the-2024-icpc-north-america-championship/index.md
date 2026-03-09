---
title: "The 2024 ICPC North America Championship"
date: "2024-06-17 21:40:57"
card_summary: ""
tags:
  - "ICPC"
categories:
  - "CP"
---

Solution of “The 2024 ICPC North America Championship”, and it also be kown as “[The 3rd Universal Cup. Stage 0: Trial Contest](https://contest.ucup.ac/contest/1695)”.

<!--more-->

## D

给定一个长度为 \(n\) 的环, 其能进行翻转和旋转, 问另一个长度为 \(m\) 的串能否成为它的子串.

---

注意到最多翻转一次, 且等价于将原序列逆序.

于是定位 \(b_{1}\) 在 \(\{a_{n}\}\) 中的位置然后分别向左向右查找即可.

时间复杂度 \(\Theta(n)\).

```python
def check ():
    for pos in range(n):
        if a[pos] == b[0]:
            for i in range(m):
                if (a[(pos + i) % n] != b[i]): return False
            break
    return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if check(): print('1')
    else:
        a.reverse()
        if check(): print('1')
        else: print('0')
```

## A

有 \(n\) 个物品, 每个物品在 \(A\) 手中有 \(a_{i}\) 的价值, 在 \(B\) 手中有 \(b_{i}\) 的价值, 最小化 \(A, B\) 手中价值和的较大值.

---

设 \(f_{i, j}\) 表示考虑前 \(i\) 个物品, 此时 \(A\) 手中的价值和为 \(j\), \(B\) 手中价值和的最小值.

转移考虑第 \(i\) 个物品给 \(A\) 还是 \(B\) 即可.

时间复杂度 \(\Theta(n^{2}\max\{a_{i}, b_{i}\})\).

```cpp
#include <bits/stdc++.h>

const int N = 52, M = 1e5 + 5;

int n, a[N], b[N], suma, sumb;

int main () {
    std::cin >> n;
    for (int i = 1; i <= n; i++)
        std::cin >> a[i] >> b[i],
        suma += a[i], sumb += b[i];
    std::vector<std::vector<int>> f(n + 1, std::vector<int>(suma + 1, N * M));

    f[0][suma] = 0;
    for (int i = 1; i <= n; i++)
        for (int j = 0; j <= suma; j++) {
            f[i][j] = f[i - 1][j];
            if (j <= suma - a[i])
                f[i][j] = std::min(f[i][j], f[i - 1][j + a[i]] + b[i]);
        }

    int ans = N * M;
    for (int j = 0; j <= suma; j++)
        ans = std::min(ans, std::max(j, f[n][j]));
    std::cout << ans << "\n";
    return 0;
}
```

## J

有 \(n\) 个物品, 第 \(i\) 个物品占据一个长度为 \(a_{i}\) 的区间. 一开始空白区间长度为 \(p\), 从第 \(1\) 个物品开始, 依次令每个物品选择一个完全空白的区间并占据, 问最坏情况下到第几个物品无法找到可以占据的区间.

---

注意到若答案为 \(i\), 则至多需要 \(i(a_{i} - 1) + \sum\limits_{j \lt i}a_{j} + 1\) 的空间. 若 \(p\) 小于这个值则到第 \(i\) 个物品放不下.

时间复杂度 \(\Theta(n)\).

```python
if __name__ == "__main__":
    n, p = map(int, input().split())
    a = [int(input()) for _ in range(n)]

    sum = 0
    for i in range(n):
        if p <= (i + 1) * (a[i] - 1) + sum:
            print(i); exit(0)
        sum += a[i]
    print(n)
```

## G

存在 \(n \times m\) 的网格, 每个格子一开始随机等概率指向右或下, 且每个格子上都有一个计时器, 其值随机等概率取 \([0, p]\) 中的实数, 计时器归零时指向会改变, 然后其值重新变为 \(p\).

现在你要从 \((1, 1)\) 走到 \((n, m)\), 每走到一个格子可以选择沿着它的指向前进或等待计时器归零再前往另一个方向, 需要注意的是你只有到达一个格子的时候才能知道格子的指向和计时器值, 求最优策略下走完的期望等待时间.

---

设 \(f_{i, j}\) 表示从 \((i, j)\) 出发的期望时间.

注意到所有格子的决策都是独立的, 于是考虑求 \(f_{i, j}\). 设 \(f_{i + 1, j}\) 和 \(f_{i, j + 1}\) 是 \(a, b(a \leqslant b)\).

- 若 \(b \geqslant a + p\), 则一定选择走 \(a\) 的方向, 有 \(f_{i, j} = a + \frac{p}{4}\).
- 若 \(b \lt a + p\), 有 \(f_{i, j} = \frac{a}{2} + \frac{(p - b + a)b}{2p} + \frac{(b - a)(a + b)}{4p}\).
  - 若当前指向 \(a\), 则走 \(a\), 概率为 \(\frac{1}{2}\), 贡献为 \(a\).
  - 若到 \(a\) 的计时器大于 \(b - a\), 则走 \(b\), 概率为 \(\frac{p - (b - a)}{2p}\), 贡献为 \(b\).
  - 若到 \(a\) 的计时器不大于 \(b - a\), 则走 \(a\), 概率为 \(\frac{b - a}{2p}\), 贡献为 \(a + \frac{b - a}{2}\).

特别的, 若 \(i = n\) 或 \(j = m\), 则只有一个方向可以转移, 设其期望为 \(e\), 有 \(f_{i, j} = e + \frac{p}{4}\).

时间复杂度 \(\Theta(nm)\).

```python
n, m, p = map(int, input().split())
f = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        if i == n and j == m: continue
        if i == n: f[i][j] = f[i][j + 1] + p / 4
        elif j == m: f[i][j] = f[i + 1][j] + p / 4
        else:
            a, b = min(f[i + 1][j], f[i][j + 1]), max(f[i + 1][j], f[i][j + 1])
            if b >= a + p: f[i][j] = a + p / 4
            else: f[i][j] = a / 2 + ((p - b + a) * b) / (2 * p) + ((b - a) * (a + b)) / (4 * p)
        
print(f[1][1])
```

## H

如图所示, 每座山都是三角形, 用其顶点坐标代替.

有 \(q\) 次操作, 每次加入或者删除一座山, 动态维护从上到下能看到的线条长度.

---

注意到线条长度等于 \(\sqrt 2\) 倍的横坐标长度, 于是一座山 \((x, y)\) 转化为一个区间 \([x - y, x + y]\), 用动态开点线段树维护区间最小值和其数量即可.

时间复杂度 \(\Theta(q\log w)\).

```cpp
#include <bits/stdc++.h>

class SegmentTree {
private:
    class Node {
    public:
        Node *lc, *rc;
        int min, cnt, lazy;
        Node (int l, int r) : lc(nullptr), rc(nullptr), min(0), cnt(r - l + 1), lazy(0) {}
    } *root = nullptr;
    int limL, limR;

    void pushdown (Node *p, int L, int R) {
        if (p->lazy == 0) return;
        int mid = L + R >> 1;
        if (p->lc == nullptr) p->lc = new Node(L, mid);
        p->lc->min += p->lazy, p->lc->lazy += p->lazy;
        if (p->rc == nullptr) p->rc = new Node(mid + 1, R);
        p->rc->min += p->lazy, p->rc->lazy += p->lazy;
        p->lazy = 0;
    }

    std::pair<int, int> merge (std::pair<int, int> a, std::pair<int, int> b) {
        int min = std::min(a.first, b.first), cnt = 0;
        if (a.first == min) cnt += a.second;
        if (b.first == min) cnt += b.second;
        return std::make_pair(min, cnt);
    }

    void upd (int l, int r, int k, Node *&p, int L, int R) {
        if (p == nullptr) p = new Node(L, R);
        if (l <= L and R <= r) { p->min += k, p->lazy += k; return; }
        pushdown(p, L, R);
        int mid = L + R >> 1;
        if (l <= mid) upd(l, r, k, p->lc, L, mid);
        if (r >= mid + 1) upd(l, r, k, p->rc, mid + 1, R);
        if (p->lc == nullptr and p->rc == nullptr) std::tie(p->min, p->cnt) = std::make_pair(0, R - L + 1);
        else if (p->lc == nullptr) std::tie(p->min, p->cnt) = std::make_pair(0, mid - L + 1 + p->rc->cnt * (p->rc->min == 0));
        else if (p->rc == nullptr) std::tie(p->min, p->cnt) = std::make_pair(0, R - mid + p->lc->cnt * (p->lc->min == 0));
        else std::tie(p->min, p->cnt) = merge(std::make_pair(p->lc->min, p->lc->cnt), std::make_pair(p->rc->min, p->rc->cnt));
    }

    std::pair<int, int> qry (int l, int r, Node *p, int L, int R) {
        if (p == nullptr) return std::make_pair(0, std::min(r, R) - std::max(l, L) + 1);
        if (l <= L and R <= r) return std::make_pair(p->min, p->cnt);
        pushdown(p, L, R);
        int mid = L + R >> 1;
        auto res = std::make_pair(INT_MAX, 0);
        if (l <= mid) res = merge(res, qry(l, r, p->lc, L, mid));
        if (r >= mid + 1) res = merge(res, qry(l, r, p->rc, mid + 1, R));
        return res;
    }

public:
    SegmentTree (int l, int r) : limL(l), limR(r), root(nullptr) {}

    void upd (int l, int r, int k) {
        upd(l, r, k, root, limL, limR);
    }

    std::pair<int, int> qry (int l, int r) {
        return qry(l, r, root, limL, limR);
    }
};

int q, w, x, y;
std::set<std::pair<int, int>> S;

int main () {
    std::cin >> q >> w;
    SegmentTree tree(0, w - 1);
    while (q--) {
        std::cin >> x >> y;
        if (S.find(std::make_pair(x, y)) != S.end())
            tree.upd(std::max(0, x - y), std::min(x + y - 1, w - 1), -1),
            S.erase(std::make_pair(x, y));
        else
            tree.upd(std::max(0, x - y), std::min(x + y - 1, w - 1), 1),
            S.insert(std::make_pair(x, y));
        auto ans = tree.qry(0, w - 1);
        std::cout << std::fixed << std::setprecision(6) << sqrt(2) * (w - ans.second * (ans.first == 0)) << "\n";
    }
    return 0;
}
```

## I

给定长度为 \(n\) 的字符串, 你需要将其中的 `?` 改成 `N`/`A`/`C` 之一, 使最终的字符串中恰好存在 \(k\) 个 `NAC` 作为子序列.

---

设 \(f_{i, N, C, k}\) 表示考虑了长度为 \(i\) 的前缀中的 `A` 的贡献, 前缀中 `N` 的数量为 \(N\), 后缀中 `C` 的数量为 \(C\) 时, 能否恰有 \(k\) 个 `NAC` 作为子序列. 转移时枚举变成什么即可, 可以用 `bitset` 优化. 时间复杂度 \(\Theta(\frac{n^{3k}}{\omega})\).

```cpp
#include <bits/stdc++.h>

const int N = 50;

int n, k;
char s[N], ans[N];
std::bitset<2600> f[N][N][N];

int main() {
    scanf("%d%d%s", &n, &k, s + 1);
    
    for (int i = 0; i <= n; i++) f[0][0][i][0] = 1;
    for (int i = 1; i <= n; i++)
        for (int j = 0; j <= i; j++)
            for (int k = 0; k <= n - i + 1; k++) {
                if ((s[i] == 'N' or s[i] == '?') and j >= 1)
                    f[i][j][k] |= f[i - 1][j - 1][k];
                if (s[i] == 'A' or s[i] == '?')
                    f[i][j][k] |= (f[i - 1][j][k] << (j * k));
                if ((s[i] == 'C' or s[i] == '?') and k + 1 <= n)
                    f[i][j][k] |= f[i - 1][j][k + 1];
                if ((s[i] != 'N' and s[i] != 'A' and s[i] != 'C') or s[i] == '?')
                    f[i][j][k] |= f[i - 1][j][k];
            }
    
    for (int i = 0; i <= n; i++) {
        if (f[n][i][0][k]) {
            int p = i, q = 0, r = k;
            for (int i = n; i >= 1; i--) {
                if ((s[i] == 'N' or s[i] == '?') and p >= 1 and f[i - 1][p - 1][q][r])
                    ans[i] = 'N', p--;
                else if ((s[i] == 'A' or s[i] == '?') and r - p * q >= 0 and f[i - 1][p][q][r - p * q])
                    ans[i] = 'A', r -= p * q;
                else if ((s[i] == 'C' or s[i] == '?') and q + 1 <= n and f[i - 1][p][q + 1][r])
                    ans[i] = 'C', q++;
                else if (s[i] == '?') ans[i] = 'B';
                else ans[i] = s[i];
            }
            ans[n + 1] = 0;
            printf("%s\n", ans + 1);
            return 0;
        }
    }
    puts("-1");
    return 0;
}
```

## M

存在 \(n\) 个任务, 每个任务包含两个区间. 一开始有能力值 \(a\) 和 \(b\), 按顺序遍历 \(n\) 个任务, 对每个任务可以选择跳过, 或解决后使 `a++` 或 `b++`. 问最多能解决多少个任务.

---

一个自然的想法是设 \(f_{i, j}\) 表示能否恰好执行 \(i\) 次 `a++` 和 \(j\) 次 `b++`. 转移时枚举每个任务, 枚举每个值为 \(1\) 的 \(f_{i \in [a_{l} - a, a_{r} - a], j \in [b_{l} - b, b_{r} - b]}\), 将 \(f_{i + 1, j}\) 和 \(f_{i, j + 1}\) 置为 \(1\). 答案为最大的 \(i + j\), 满足 \(f_{i, j} = 1\). 时间复杂度 \(\Theta(n^{3})\).

注意到一个二元组 \((i, j)\) 对应的 \(f_{i, j}\) 被置为 \(1\) 后就不会变了, 于是考虑利用这个势能限制复杂度. 维护已经被置为 \(1\) 但还未用其更新其它 \(f\) 值的二元组集 \(S\), 每次更新将满足 \(i \in [a_{l} - a, a_{r} - a]\) 和 \(j \in [b_{l} - b, b_{r} - b]\) 的二元组从 \(S\) 中取出, 然后将它们能更新到的二元组置为 \(1\) 并加入 \(S\).

对于每个二元组, 它最多加入 \(S\) 一次, 从 \(S\) 中被删除一次, 单次操作的时间复杂度为 \(\Theta(\log n)\), 于是总时间复杂度为 \(\Theta(n^{2}\log n)\), 具体实现可以对每个 \(i\) 维护它对应的 \(j\) 的集合.

```cpp
#include <bits/stdc++.h>

const int N = 5e3 + 5;

int n, a, b, ans;
bool f[N][N];
std::set<int> S[N];
std::vector<std::pair<int, int>> upd;

int main () {
    std::cin >> n >> a >> b;
    f[0][0] = true, S[0].insert(0);
    for (int al, ar, bl, br, p = 1; p <= n; p++) {
        std::cin >> al >> ar >> bl >> br;
        upd.clear();
        for (int i = std::max(0, al - a); i <= std::min(p, ar - a); i++) {
            auto l = S[i].lower_bound(std::max(0, bl - b));
            if (l != S[i].end()) {
                auto r = S[i].upper_bound(std::min(p, br - b));
                for (auto it = l; it != r; it++) {
                    if (not f[i + 1][*it])
                        f[i + 1][*it] = true,
                        upd.push_back(std::make_pair(i + 1, *it));
                    if (not f[i][(*it) + 1])
                        f[i][(*it) + 1] = 1,
                        upd.push_back(std::make_pair(i, (*it) + 1));
                }
                S[i].erase(l, r);
            }
        }
        for (auto x : upd)
            S[x.first].insert(x.second),
            ans = std::max(ans, x.first + x.second);
    }
    std::cout << ans << "\n";
    return 0;
}
```
