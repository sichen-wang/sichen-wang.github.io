---
title: "The 2024 ICPC St. Petersburg"
date: "2024-06-18 15:32:06"
card_summary: ""
tags:
  - "ICPC"
categories:
  - "CP"
---

Solution of “The 2024 ICPC St. Petersburg”, and it also be kown as “[The 3rd Universal Cup. Stage 1: St. Petersburg](https://contest.ucup.ac/contest/1696)”.

<!--more-->

## H

记 \(f(x)\) 为将 \(x\) 翻转后的数, 如 \(f(123) = 321\).

给定 \(n\), 求集合 \(\{f(1), f(2), \cdots, f(n)\}\) 中第一个没出现过的正整数.

---

显然为 \(n + 1\) 和 \(10\) 中的较小值.

```python
n = int(input())
print(min(n + 1, 10))
```

## K

将字符串的对应关系反过来, 按数字从小到大输出, 详见样例.

---

```python
link = {}
while True:
    try:
        key, values = input().split(": ")
        values = values.split(", ")
        link[key] = values
    except EOFError: break

rev = {}
for key, values in link.items():
    for value in values:
        if value in rev: rev[value].append(key)
        else: rev[value] = [key]

for key in sorted(rev.keys(), key = lambda x: int(x.split('-')[1])):
    values = rev[key]
    values.sort(key = lambda x: int(x.split('-')[1]))
    print("{}: {}".format(key, ", ".join(values)))
```

## O

长度为 \(n\) 的序列 \(\{x_{n}\}\) 存在递推关系 \(x_{i+2} = ax_{i+1} + bx_{i}\), 给定 \(a, b, n, x_{1}, x_{n}\), 要求还原这个序列.

---

注意到 \(x_{n}\) 可以被表示为 \(px_{1} + qx_{2}\), 于是可以解出 \(x_{2}\) 关于 \(x_{1}\) 和 \(x_{n}\) 的表达式.

```python
a, b, n, s, t = map(eval, input().split())
x = [(1, 0), (0, 1)]
for i in range(2, n):
    x.append(tuple(a * p + b * q for p, q in zip(x[i - 1], x[i - 2])))

f = [s, (t - x[n - 1][0] * s) / x[n - 1][1]]
for i in range(2, n): f.append(a * f[i - 1] + b * f[i - 2])
for x in f: print(x)
```

## C

给定长度为 \(n\) 的序列 \(\{a_{n}\}\) 和 \(0/1\) 串 \(s\).

求最大的 \(x\), 满足仅保留 \(s\) 中对应位 \(a\) 值不小于 \(x\) 的位后, \(0/1\) 串中存在 \(k\) 个连续的 `1`.

---

考虑从大到小将数加入, 用一棵线段树维护最大子段和, 若 \(s_{i} = 1\) 则将该位设为 \(1\), 否则设为 \(-\infty\).

时间复杂度 \(\Theta(n \log n)\).

```cpp
#include <bits/stdc++.h>

const int N = 1e5 + 10;

int n, k, a[N], p[N];
std::string s;

class SegmentTree {
private:
    class Node {
    public:
        Node *lc, *rc;
        long long sum, lmax, rmax, max;
        Node (int l, int r) : lc(nullptr), rc(nullptr), sum(0), lmax(0), rmax(0), max(0) {}
    } *root = nullptr;
    int limL, limR;

    void pushup (Node *p, int L, int R) {
        int mid = L + R >> 1;
        if (p->lc == nullptr) p->lc = new Node(L, mid);
        if (p->rc == nullptr) p->rc = new Node(mid + 1, R);
        p->sum = p->lc->sum + p->rc->sum;
        p->lmax = std::max(p->lc->lmax, p->lc->sum + p->rc->lmax);
        p->rmax = std::max(p->rc->rmax, p->rc->sum + p->lc->rmax);
        p->max = std::max(p->lc->rmax + p->rc->lmax, std::max(p->lc->max, p->rc->max));
    }

    void upd (int pos, int k, Node *&p, int L, int R) {
        if (p == nullptr) p = new Node(L, R);
        if (pos <= L and R <= pos) {
            p->sum = p->lmax = p->rmax = p->max = k;
            return;
        }
        int mid = L + R >> 1;
        if (pos <= mid) upd(pos, k, p->lc, L, mid);
        else upd(pos, k, p->rc, mid + 1, R);
        pushup(p, L, R);
    }

    void del (Node* u) {
        if (u->lc != nullptr) del(u->lc);
        if (u->rc != nullptr) del(u->rc);
        delete u;
        u = nullptr;
    }

public:
    SegmentTree (int l, int r) : limL(l), limR(r), root(nullptr) {}

    void upd (int pos, int k) { upd(pos, k, root, limL, limR); }

    int qry () {
        if (root == nullptr) return 0;
        return root->max;
    }

    ~SegmentTree () { del(root); }
};

int main () {
    std::cin >> n >> k;
    for (int i = 1; i <= n; i++)
        std::cin >> a[i], p[i] = i;
    std::sort(p + 1, p + n + 1, [&](int i, int j) { return a[i] > a[j]; });
    std::cin >> s, s = ' ' + s;

    SegmentTree tree(1, n);
    for (int i = 1; i <= n; i++) {
        if (s[p[i]] == '1') tree.upd(p[i], 1);
        else tree.upd(p[i], -1e9);
        if (a[p[i + 1]] != a[p[i]] and tree.qry() >= k)
            return std::cout << a[p[i]] << "\n", 0;
    }
    puts("0");
    return 0;
}
```

## D

这是一个交互题, 有 \(n\) 个独立的问题.

每个问题形如: 有一个人在每天的 \(1440\) 分钟中恰好睡固定的 \(720\) 分钟, 你想知道他从什么时候开始睡觉. 你每次可以询问一个时刻, 并知道他在这一刻是醒着的还是睡着的. 在每个问题中最多进行 \(50\) 次询问.

---

```python
def encode(t: int) -> str:
    t %= 1440
    ho = t // 60
    mi = t % 60
    return f'{ho:02d}:{mi:02d}'

def ask(idx: int, t: int) -> bool:
    print(f'at {encode(t)} check {idx}', flush=True)
    res = input()
    return (res == 'awake')

ans = []

if __name__ == '__main__':
    T = int(input())
    for idx in range(1, T + 1):
        resori = ask(idx, 0)
        l, r = 1, 720
        while l < r:
            mid = (l + r) // 2
            if ask(idx, mid) == resori: l = mid + 1
            else: r = mid
        if resori: l += 720
        ans.append(l)
    print('answer')
    for t in ans: print(encode(t))
```

以上是一份错误的代码, 提交上去会有莫名其妙的 `RE`, 在此仅作记录.

## J

给定 \(2n\) 个正整数, 选出其中的一些使它们的和恰好为 \(10^{9}\).

请注意, 数据用以下方式生成:

- 生成有 \(n\) 个元素的正整数集 \(\mathbb{S}\), 其元素和为 \(10^{9}\), 且对于所有元素集服从随机分布.
- 用相同的方式生成 \(\mathbb{T}\), 将两个集合合并为一个可重集作为最终输入.

---

该题的一个经典做法为, 随意将所有数分为两半, 求出其中一半能组合出的所有和存入 `map`. 然后枚举另一半能组合出的所有和 \(s\), 在 `map` 中查询是否存在 \(10^{9} - s\) 即可. 该做法又被称为 meet in the middle.

容易发现, 上述做法最多处理到 \(n\) 约为 \(20\) 的情况, 于是我们不妨将所有数随机打包成至多 \(40\) 个组, 每组中的数同时选择, 在这种情况下使用 meet in the middle. 考虑该做法的正确性: 由于本题特别的数据生成方式, 这 \(40\) 个数能组合出的和差不多是在 \([n, 2 \times 10^{9}]\) 内以某种中心集中的方式随机的. 注意到 \(2^{40} \gg 2 \times 10^{9}\), 于是打包以后也几乎必然能找到一个解.

```cpp
#include <bits/stdc++.h>

constexpr unsigned int b = 20, aim = 1e9;

std::mt19937 gen(std::chrono::system_clock::now().time_since_epoch().count());

unsigned int n;
std::map<int, unsigned int> exi;

int main() {
    std::cin >> n;
    std::vector a(n, 0);
    for (unsigned int i = 0; i < n; i++) std::cin >> a[i];

    std::vector S(b, std::vector(1, 0)), T(b, std::vector(1, 0));
    for (unsigned int i = 0; i < std::min(n, b << 1); i++)
        if (i & 1) T[i >> 1].push_back(i), T[i >> 1][0] += a[i];
        else S[i >> 1].push_back(i), S[i >> 1][0] += a[i];
    for (unsigned int i = (b << 1); i < n; i++) {
        int opt = (gen() & 1), pos = gen() % b;
        if (opt) S[pos].push_back(i), S[pos][0] += a[i];
        else T[pos].push_back(i), T[pos][0] += a[i];
    }

    for (unsigned int R = 0; R < (1 << b); R++) {
        int sum = 0;
        for (unsigned int i = 0; i < b; i++)
            if ((R >> i) & 1) sum += S[i][0];
        exi[sum] = R;
    }
    for (unsigned int R = 0; R < (1 << b); R++) {
        int sum = 0;
        for (unsigned int i = 0; i < b; i++)
            if ((R >> i) & 1) sum += T[i][0];
        if (exi.contains(aim - sum)) {
            std::vector<int> ans;
            for (unsigned int i = 0; i < b; i++)
                if ((R >> i) & 1)
                    for (unsigned int j = 1; j < T[i].size(); j++)
                        ans.push_back(T[i][j]);
            unsigned int P = exi[aim - sum];
            for (unsigned int i = 0; i < b; i++)
                if ((P >> i) & 1)
                    for (unsigned int j = 1; j < S[i].size(); j++)
                        ans.push_back(S[i][j]);
            std::cout << ans.size() << " ";
            for (int x : ans) std::cout << x + 1 << " ";
            return 0;
        }
    }
}
```
