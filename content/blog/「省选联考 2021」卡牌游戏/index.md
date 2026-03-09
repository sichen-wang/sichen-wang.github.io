---
title: "「省选联考 2021」卡牌游戏"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "「省选联考 2021」卡牌游戏"
aliases:
  - "/blog/sheng-xuan-lian-kao-2021-qia-pai-you-xi/"
tags:
  - "OI"
categories:
  - "CP"
---

## Sol

### 法一

可以证明，若进行了操作 \(a_{i} \to b_{i}\)，那么 \(\forall j \lt i\)，操作 \(a_{j} \to b_{j}\) 都进行了。因为如果存在 \(j \lt i\)，\(a_{i} \to b_{i}\) 执行了，但 \(a_{j} \to b_{j}\) 没执行，那么 \(a_{i} \to b_{i}\) 执行就没有意义，因为 \(a_{j}\) 还是会作为最小值。

同理，我们可以证明操作序列也是后缀连续的。

于是我们可以枚举操作了的前缀，然后预处理出 \(b\) 序列后缀最大值等信息即可计算答案。

时间复杂度 \(\Theta(n).\)

### 法二

容易发现答案满足可二分性，于是二分答案 \(\rm mid.\)

如果选定了答案区间的左端点，那么右端点可以容易地确定。

于是问题转化成了一个前后缀 \(\rm RMQ.\)

时间复杂度 \(\Theta(n \log n).\)

### 法三

考虑将 \(a_{i}\) 和 \(b_{i}\) 全部取出来排序，可以发现答案是删去一些数后的最大值减最小值。

于是双指针维护，记录当前删去了多少个 \(a_{i}\) 和一张牌的 \(a_{i}\) 和 \(b_{i}\) 是否同时被删掉即可。

时间复杂度 \(\Theta(n \log n)\)，因为要排序。

## Code

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e6 + 10;

int n, m, num, ans = INT_MAX;
pair <int, int> a[N];
bool tag[N];

int idx (int pos) {
    return a[pos].second - (a[pos].second <= n ? 0 : n);
}

bool check (int pos) {
    if (a[pos].second <= n && num >= m) return false;
    if (tag[idx(pos)]) return false;
    return true;
}

void del (int pos) {
    if (a[pos].second <= n) num++;
    tag[idx(pos)] = true;
}

void rev (int pos) {
    if (a[pos].second <= n) num--;
    tag[idx(pos)] = false;
}

int main () {

    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n << 1; i++)
        scanf("%d", &a[i].first), a[i].second = i;
    sort(a + 1, a + 2 * n + 1);

    int l = 1, r = 2 * n;
    while (check(r)) del(r), r--;
    while (r <= n << 1) {
        ans = min(ans, a[r].first - a[l].first);
        if (a[l].second <= n) while (num >= m && r <= 2 * n) rev(r + 1), r++;
        while (tag[idx(l)] && r <= 2 * n) rev(r + 1), r++;
        del(l), l++;
    }
    printf("%d\n", ans);

    return 0;
}
```
