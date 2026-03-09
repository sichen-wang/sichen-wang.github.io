---
title: "2021 年计数题康复训练"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "2021 年计数题康复训练"
aliases:
  - "/blog/2021-nian-ji-shu-ti-kang-fu-xun-lian/"
tags:
  - "Combinatorics"
  - "Counting"
categories:
  - "CP"
---

## 技巧收集

- 将要计数的总体分成很多个部分，每个部分分别计算贡献。
- 有些时候一个集合 \(S\) 联合产生贡献，为了避免算重，可以将这个集合的贡献放在其中的某个元素上计算，比如标号最小的那一个。
- 可以考虑划分阶段，每次加入一个元素时计算答案增量。
- 如果需要计算在一个大的部分中选择一些状态的方案数，可以将这个大的部分分为几个，枚举在这几个部分中选择的状态数量，再分别计算并相乘。
- 可以先计算每一部分的答案，用某种数据结构维护，合并的时候考虑两个部分联合产生的答案。
- 如果子问题的答案容易计算，并且原问题与子问题之间存在容斥关系，可以用 \(\rm DP\) 计算，转移的时候容斥。

## 好题选做

### [[USACO20FEB] Help Yourself G](https://www.luogu.com.cn/problem/P6146)

**方法一：**

首先有一个直观的想法，计算每条线段对答案的贡献。

考虑将每个连通块的贡献放到这个连通块最左边的线段上去计算，于是我们发现在一种选择方案中，一条线段 \([l_{i},r_{i}]\) 有 \(1\) 的贡献当且仅当不存在另一条同时被选择的线段 \([l_{j},r_{j}]\) 满足 \(l_{j}\lt l_{i}\lt r_{j}\)，即其左端点不能被覆盖。

因为题目保证了所有端点互不相同，所以我们不需要经过比较复杂的分类讨论，直接将线段按左端点排序，右端点用线段树维护即可。

用线段树求出与当前线段不能同时选择的线段数，记为 \(x\)，则这条线段的贡献为 \(2^{n-x-1}\)。

总时间复杂度 \(\Theta(n\log n)\)。

```cpp
#include<bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 1e5 + 10, mod = 1e9 + 7;

int n, Pow[N], ans;
pair <int, int> seg[N];

namespace ST {
#define LS (p << 1)
#define RS (p << 1 | 1)
int sum[N << 3], l[N << 3], r[N << 3];

void Build (int p, int L, int R) {
    l[p] = L, r[p] = R, sum[p] = 0;
    if (L == R) return;
    int mid = (L + R) >> 1;
    Build(LS, L, mid), Build(RS, mid + 1, R);
}

void add (int p, int pos) {
    if (l[p] == pos && r[p] == pos) {
        sum[p]++; return;
    }
    pos <= r[LS] ? add(LS, pos) : add(RS, pos);
    sum[p] = sum[LS] + sum[RS];
}

int Query (int p, int L, int R) {
    if (l[p] >= L && r[p] <= R) return sum[p];
    int res = 0;
    if (L <= r[LS]) res += Query(LS, L, R);
    if (R >= l[RS]) res += Query(RS, L, R);
    return res;
}
}

int main () {

    scanf("%d", &n);
    rep(i, 1, n) scanf("%d%d", &seg[i].first, &seg[i].second);

    Pow[0] = 1;
    rep(i, 1, n) Pow[i] = (Pow[i - 1] << 1) % mod;

    sort(seg + 1, seg + n + 1);
    ST::Build(1, 1, 2 * n);
    rep(i, 1, n) {
        ans = (ans + Pow[n - ST::Query(1, seg[i].first + 1, 2 * n) - 1]) % mod;
        ST::add(1, seg[i].second);
    }
    printf("%d\n", ans);

    return 0;
}
```

**方法二：**

还是考虑将线段按左端点排序后一个个加入并计算贡献，但是我们这次只考虑已经枚举了的 \(i\) 条线段的答案，记为 \(f_{i}\)。

可以发现，如果当前枚举的线段不选，那么答案为 \(f_{i-1}\)，否则在选择某一个集合的时候答案会 \(+1\)，而这个集合中的线段即为右端点小于当前线段左端点的线段，记其数量为 \(x\)。 由于这个线段集合的每一个子集的答案都相比原来 \(+1\)，所以这种情况下的答案为 \(f_{i-1}+2^{x}\)。 故总的转移式为 \(f_{i}=2f_{i-1}+2^{x}\)。

至于 \(x\) 的值可以很方便地在最开始用前缀和求出。

```cpp
#include<bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 2e5 + 10, mod = 1e9 + 7;

int n, sum[N], Pow[N], ans;
pair <int, int> seg[N];

int main () {

    scanf("%d", &n);
    rep(i, 1, n) scanf("%d%d", &seg[i].first, &seg[i].second);

    Pow[0] = 1;
    rep(i, 1, n) Pow[i] = (Pow[i - 1] << 1) % mod;
    rep(i, 1, n) sum[seg[i].second]++;
    rep(i, 1, (n << 1)) sum[i] += sum[i - 1];

    sort(seg + 1, seg + n + 1);
    rep(i, 1, n) ans = (2 * ans % mod + Pow[sum[seg[i].first - 1]]) % mod;
    printf("%d\n", ans);

    return 0;
}
```

### [[JSOI2015] 子集选取](https://www.luogu.com.cn/problem/P6075)

看上去很简单，代码也很简洁，但如果要证明而非直接打表的话是一个有一定难度的题。

首先观察到题目限制等价于 \(\forall i'\leqslant i,j'\leqslant j,A_{i,j}\subseteq A_{i',j'}\)。

又观察到如果对每个元素分开考虑，那么一定存在一条从左下到右上的分界线，使分界线左边的集合都有这个元素，而右边都没有，形如下图 ：

![](https://s2.ax1x.com/2020/02/11/1oskl9.png)

容易发现，对于每个元素，这样的路径与每种方案一一对应，并且路径数为 \(2^{n}\)。

进一步的，容易发现每个元素的方案相互独立，于是将每个元素的方案数相乘即为最终答案 \(2^{nk}\)。

总时间复杂度 \(\Theta(\log n)\)。

```cpp
#include<bits/stdc++.h>
using namespace std;

const int mod = 1e9 + 7;

int n, k;

int Pow (int a, int k) {
    if (k == 1) return a;
    int S = Pow(a, k >> 1);
    if (k & 1) return 1ll * S * S % mod * a % mod;
    else return 1ll * S * S % mod;
}

int main () {

    scanf("%d%d", &n, &k);
    printf("%d\n", Pow(Pow(2, n), k));

    return 0;
}
```

### [[LG1350] 车的放置](https://www.luogu.com.cn/problem/P1350)

首先考虑在一个 \(k\times k\) 的矩形上放置 \(k\) 个车的方案数，显然为 \(k!\)。

然后考虑在一个 \(n\times m\) 的矩形上放置 \(k\) 个车的方案数，可以先从 \(n\) 行 \(m\) 列中分别选出 \(k\) 行 \(k\) 列，再按照 \(k\times k\) 矩形的方式计算，方案数为 \(\binom{n}{k}\binom{m}{k}k!\)。

考虑将原图形划分成右边一个 \(c\times d\) 的矩形和左边一个 \(a\times (b+d)\) 的矩形，然后枚举在右边放置多少个车，可以发现右边每放置一个车都可以使左边能放置车的行减少一个，于是容易独立计算两边的方案数，故答案为 :

\[
\sum_{i=0}^d \dbinom{c}{i}\dbinom{d}{i}i!\dbinom{a}{k-i}\dbinom{b+d-i}{k-i}(k-i)!
\]

总时间复杂度 \(\Theta(n)\)。

```cpp
#include<bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 2e3 + 10, mod = 1e5 + 3;

int a, b, c, d, k, fac[N], inv[N], ans;

int Pow (int a, int k) {
    if (k == 0) return 1;
    if (k == 1) return a;
    int S = Pow(a, k >> 1);
    if (k & 1) return 1ll * S * S % mod * a % mod;
    else return 1ll * S * S % mod;
}

int C (int n, int m) {
    if (n < m) return 0;
    return 1ll * fac[n] * inv[m] % mod * inv[n - m] % mod;
}

int main () {

    fac[0] = 1;
    rep(i, 1, N - 1) fac[i] = 1ll * fac[i - 1] * i % mod;
    inv[N - 1] = Pow(fac[N - 1], mod - 2);
    dep(i, N - 2, 0) inv[i] = 1ll * inv[i + 1] * (i + 1) % mod;

    cin >> a >> b >> c >> d >> k;
    rep(i, 0, k) ans = (ans + 1ll * C(c, i) * C(d, i) % mod * fac[i] % mod * C(a, k - i) % mod * C(b + d - i, k - i) % mod * fac[k - i]) % mod;
    printf("%d\n", ans);

    return 0;
}
```

### [[USACO20JAN] Cave Paintings P](https://www.luogu.com.cn/problem/P6008)

想这题时思路容易往如何建图上跑偏，但其实完全不用建图，直接对着原模型考虑即可。

考虑从底层往上加水的过程，容易发现一些联通块会逐渐被连接在一起，可以考虑用并查集维护，两个连通块合并的答案显然为原本答案的乘积加上 \(1\)，因为所有的点都加上水也是一种方案。

最终的答案即为所有连通块的方案数之积。

总时间复杂度 \(\Theta(nm\log (nm))\)。

```cpp
#include<bits/stdc++.h>
using namespace std;

#define int long long
#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)
#define idx(x, y) ((x - 1) * m + y)

const int N = 1e3 + 10, mod = 1e9 + 7;

int n, m, fa[N * N], f[N * N], ans = 1;
char s[N][N];

int Find (int x) {
    if (x != fa[x]) fa[x] = Find(fa[x]);
    return fa[x];
}

signed main () {

    cin >> n >> m;
    rep(i, 1, n) cin >> s[i] + 1;

    rep(i, 1, n * m) fa[i] = i, f[i] = 1;
    dep(i, n - 1, 2) {
        rep(j, 3, m - 1) if (s[i][j] == '.' && s[i][j - 1] == '.') fa[Find(idx(i, j))] = Find(idx(i, j - 1));
        rep(j, 2, m - 1) if (s[i][j] == '.' && s[i + 1][j] == '.' && Find(idx(i, j)) != Find(idx(i + 1, j)))
            f[Find(idx(i, j))] = f[Find(idx(i, j))] * f[Find(idx(i + 1, j))] % mod, fa[Find(idx(i + 1, j))] = Find(idx(i, j));
        rep(j, 2, m - 1) if (s[i][j] == '.' && Find(idx(i, j)) == idx(i, j)) f[idx(i, j)]++;
    }

    rep(i, 2, n - 1) rep(j, 2, m - 1) if (Find(idx(i, j)) == idx(i, j)) ans = ans * f[idx(i, j)] % mod;
    cout << ans << endl;

    return 0;
}
```

### [[HNOI2012] 排队](https://www.luogu.com.cn/problem/P3223)

运用插板法和捆绑法易得答案即为 ：

\[
(n + 2)! A_{n + 3}^{m} - 2 (n + 1)! A_{n + 2}^{m}
\]

高精差评。

```cpp
#include<bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 2e3 + 10;

namespace BigInt_Class {
const int MaxL = 5e3 + 10;

struct BigInt {
    int len, bit[MaxL];
    void Clear () {
        for (int i = 1; i <= len; i++) bit[i] = 0;
        len = 1;
    }
};

void read (BigInt &x) {
    char s[MaxL];
    scanf("%s", s + 1), x.len = strlen(s + 1);
    for (int i = 1; i <= x.len; i++)
        x.bit[i] = s[x.len - i + 1] - '0';
}

void Write (BigInt x, char End) {
    for (int i = x.len; i >= 1; i--)
        printf("%d", x.bit[i]);
    putchar(End);
}

bool operator < (BigInt a, BigInt b) {
    if (a.len != b.len) return a.len < b.len;
    for (int i = a.len; i >= 1; i--)
        if (a.bit[i] != b.bit[i])
            return a.bit[i] < b.bit[i];
    return false;
}

BigInt Change (int x) {
    BigInt res;
    res.Clear();
    if (x == 0) return res;
    else res.len = 0;
    while (x) res.bit[++res.len] = x % 10, x /= 10;
    return res;
}

BigInt operator + (BigInt a, BigInt b) {
    BigInt res;
    res.Clear();
    res.len = max(a.len, b.len);
    for (int i = 1; i <= res.len; i++)
        res.bit[i] = a.bit[i] + b.bit[i];
    for (int i = 1; i <= res.len; i++)
        if (res.bit[i] >= 10)
            res.bit[i] -= 10, res.bit[i + 1]++;
    if (res.bit[res.len + 1] > 0) res.len++;
    return res;
}

BigInt operator - (BigInt a, BigInt b) {
    BigInt res;
    res.Clear();
    res.len = max(a.len, b.len);
    for (int i = 1; i <= res.len; i++)
        res.bit[i] = a.bit[i] - b.bit[i];
    for (int i = 1; i <= res.len; i++)
        if (res.bit[i] < 0)
            res.bit[i] += 10, res.bit[i + 1]--;
    while (res.bit[res.len] == 0 && res.len > 1) res.len--;
    return res;
}

BigInt operator * (BigInt a, BigInt b) {
    BigInt res;
    res.Clear();
    res.len = a.len + b.len;
    for (int i = 1; i <= a.len; i++)
        for (int j = 1; j <= b.len; j++)
            res.bit[i + j - 1] += a.bit[i] * b.bit[j];
    for (int i = 1; i <= res.len; i++)
        if (res.bit[i] >= 10)
            res.bit[i + 1] += res.bit[i] / 10, res.bit[i] %= 10;
    while (res.bit[res.len] == 0 && res.len > 1) res.len--;
    return res;
}

BigInt operator / (BigInt a, BigInt b) {
    BigInt res, tmp;
    res.Clear();
    if (a < b) return res;
    res.len = a.len - b.len + 1;
    for (int i = a.len; i >= b.len; i--) {
        tmp.Clear(), tmp.len = i;
        for (int j = 1; j <= b.len; j++)
            tmp.bit[j + i - b.len] = b.bit[j];
        while (!(a < tmp)) a = a - tmp, res.bit[i - b.len + 1]++;
    }
    while (res.bit[res.len] == 0 && res.len > 1) res.len--;
    return res;
}

BigInt operator % (BigInt a, BigInt b) {
    BigInt tmp;
    if (a < b) return a;
    for (int i = a.len; i >= b.len; i--) {
        tmp.Clear(), tmp.len = i;
        for (int j = 1; j <= b.len; j++)
            tmp.bit[j + i - b.len] = b.bit[j];
        while (!(a < tmp)) a = a - tmp;
    }
    return a;
}
}
using namespace BigInt_Class;

int n, m;
BigInt fac[N];

BigInt A (int n, int m) { return n < m ? Change(0) : fac[n] / fac[n - m]; }

int main () {

    cin >> n >> m;

    fac[0] = Change(1);
    rep(i, 1, n + 3) fac[i] = fac[i - 1] * Change(i);

    Write(fac[n + 2] * A(n + 3, m) - Change(2) * fac[n + 1] * A(n + 2, m), '\n');

    return 0;
}
```

### [[SDOI2016] 排列计数](https://www.luogu.com.cn/problem/P4071)

看到题目一眼二项式反演，但事实上是不行的。

考虑钦点 \(m\) 个位置 \(a_{i}=i\)，剩下的显然是 \(n - m\) 个数的错排问题。

记 \(D_{n}\) 表示 \(n\) 个数的错排问题方案数，推导其递推式 ：

考虑在 \(n\) 个数的基础上再加入第 \(n + 1\) 个数，不妨设 \(a_{n+1}=k\)。

接下来对 \(a_{k}\) 做分类讨论 ：

- 如果 \(a_{k}=n+1\)，那么 \(k\) 和 \(n+1\) 互相占用，剩下的方案数为 \(D_{n-1}\)。
- 如果 \(a_{k}\not = n + 1\)，那么除了 \(a_{n + 1}\) 已经被确定之外，其它所有位置都有且仅有一个数不能填 （位置 \(k\) 不能填的数为 \(n + 1\)），于是方案即为 \(D_{n}\)。

再考虑到选取 \(k\) 的方式有 \(n\) 种，故 \(\{D_{n}\}\) 的递推式为 ：

\[
D_{n + 1} = n(D_n + D_{n - 1})
\]

根据错排数列的定义易知 \(D_{0} = 1, D_{1} = 0,D_{2} = 1\)。

综上，答案即为 \(\binom{n}{m}D_{n-m}\)。

总时间复杂度 \(\Theta(T+n)\)。

```cpp
#include<bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 1e6 + 10, mod = 1e9 + 7;

int T, n, m, fac[N], inv[N], D[N];

int Pow (int a, int k) {
    if (k == 0) return 1;
    if (k == 1) return a;
    int S = Pow(a, k >> 1);
    if (k & 1) return 1ll * S * S % mod * a % mod;
    else return 1ll * S * S % mod;
}

int C (int n, int m) {
    if (n < m) return 0;
    return 1ll * fac[n] * inv[m] % mod * inv[n - m] % mod;
}

int main () {

    fac[0] = 1;
    rep(i, 1, N - 1) fac[i] = 1ll * fac[i - 1] * i % mod;
    inv[N - 1] = Pow(fac[N - 1], mod - 2);
    dep(i, N - 2, 0) inv[i] = 1ll * inv[i + 1] * (i + 1) % mod;

    D[0] = 1, D[1] = 0, D[2] = 1;
    rep(i, 3, N - 1) D[i] = 1ll * (i - 1) * (D[i - 1] + D[i - 2]) % mod;

    scanf("%d", &T); while (T--) {
        scanf("%d%d", &n, &m);
        printf("%lld\n", 1ll * C(n, m) * D[n - m] % mod);
    }

    return 0;
}
```

### [[HNOI2010] 合唱队](https://www.luogu.com.cn/problem/P3205)

考虑到一段区间内的方案数是独立的，于是使用区间 \(\rm DP\) 求解。

可以发现我们关心的状态除了区间端点 \(l,r\) 外，还有上一个填入值的大小，因为这关系到现在这个数填在左边还是右边。同时，我们观察到，上一个数只有可能填在区间的左端点或右端点，于是记 \(f_{l,r,0/1}\) 表示在 \([l,r]\) 这段区间内，上一次填的数在左端点\(/\)右端点的方案数。

转移是简单的，分 \(4\) 种情况 ：

- \(a_{i}\lt a_{i + 1},f_{i,j,0}\leftarrow f_{i+1,j,0}\)
- \(a_{i}\lt a_{j},f_{i,j,0}\leftarrow f_{i+1,j,1}\)
- \(a_{j}\gt a_{i},f_{i,j,1}\leftarrow f_{i,j-1,0}\)
- \(a_{j}\gt a_{j-1},f_{i,j,1}\leftarrow f_{i,j-1,1}\)

需要注意的是，赋初值时，可以钦点 \([i,j]\) 的数是从左端点填进去的，即 \(f_{i,i,0} = 1\)，如果不这样做的话会算重。

总时间复杂度 \(\Theta(n^{2})\)。

```cpp
#include<bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 1e3 + 10, mod = 19650827;

int n, a[N], f[N][N][2];

int main () {

    cin >> n;
    rep(i, 1, n) cin >> a[i];
    
    rep(i, 1, n) f[i][i][0] = 1;
    rep(len, 2, n) for (int i = 1; i + len - 1 <= n; i++) {
        int j = i + len - 1;
        if (a[i] < a[i + 1]) f[i][j][0] = (f[i][j][0] + f[i + 1][j][0]) % mod;
        if (a[i] < a[j]) f[i][j][0] = (f[i][j][0] + f[i + 1][j][1]) % mod;
        if (a[j] > a[i]) f[i][j][1] = (f[i][j][1] + f[i][j - 1][0]) % mod;
        if (a[j] > a[j - 1]) f[i][j][1] = (f[i][j][1] + f[i][j - 1][1]) % mod;
    }
    
    cout << (f[1][n][0] + f[1][n][1]) % mod << endl;

    return 0;
}
```

### [[HNOI2011] 卡农](https://www.luogu.com.cn/problem/P3214)

**形式化题意：**

定义全集 \(U=\{1,2,3,\cdots ,n\}\)，要从中选出 \(m\) 个子集，满足 ：

- 任意子集非空。
- 子集互不相同。
- 在选出的 \(m\) 个子集中，\(1\sim n\) 中每个数的出现次数均为偶数。

求方案数对 \(10^{8} + 7\) 取模后的值。

保证 \(n,m\leqslant 10^{6}\)。

考虑计算选出子集有序的方案数，容易发现最后将方案数除以 \(m!\) 就与原问题等价。

记 \(f_{i}\) 表示从 \(U\) 中选出 \(i\) 个合法子集的方案数，转移考虑容斥 ：

如果前面的 \(i - 1\) 个集合已经确定，那么这个集合中每个元素是否存在就已经被确定了，并且一定存在一种选择这个集合的方案，故在不考虑子集非空和子集互不相同的情况下，方案数为 \(A_{2^{n} - 1}^{i - 1}\)。

考虑将第 \(i\) 个集合为空的方案去除。可以发现在第 \(i\) 个集合为空的情况下，不合法方案与 \(f_{i - 1}\) 中的每种合法方案一一对应，故第 \(i\) 个集合为空的方案数为 \(f_{i - 1}\)。

考虑将第 \(i\) 个集合与前面某个集合 \(S_{j}\) 相同的方案去除。可以发现，将 \(S_{i}\) 和 \(S_{j}\) 同时去除后的方案还是合法的，且数量为 \(f_{i - 2}\)。 \(j\) 有 \(i - 1\) 种取值，\(S_{i}\) 和 \(S_{j}\) 由于不能与另外 \(i - 2\) 个集合相同，所以有 \((2^{n} - 1) - (i - 2)\) 种取法。故第 \(i\) 个集合与之前某个集合相同的方案数为 \(f_{i - 2}\times (i - 1)\times (2^{n} - i + 1)\)。

故转移方程为 ：

\[
f_{i} = A_{2^n - 1}^{i - 1} - f_{i - 1} - f_{i - 2}\times (i - 1)\times (2^n - i + 1)
\]

经过一些预处理后可以做到 \(\Theta(n)\)。

```cpp
#include<bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 1e6 + 10, mod = 1e8 + 7;

int n, m, A[N], f[N], M;

int Pow (int a, int k) {
    if (k == 0) return 1;
    if (k == 1) return a;
    int S = Pow(a, k >> 1);
    if (k & 1) return 1ll * S * S % mod * a % mod;
    else return 1ll * S * S % mod;
}

int main () {

    cin >> n >> m;

    A[0] = Pow(2, n), A[1] = A[0] - 1;
    rep(i, 2, m) A[i] = 1ll * A[i - 1] * (A[0] - i) % mod;

    f[0] = 1;
    rep(i, 2, m) f[i] = (A[i - 1] - f[i - 1] - 1ll * f[i - 2] * (i - 1) % mod * (A[0] - i + 1)) % mod;

    M = 1;
    rep(i, 1, m) M = 1ll * M * i % mod;

    cout << (1ll * f[m] * Pow(M, mod - 2) % mod + mod) % mod << endl;

    return 0;
}
```

### [[ZJOI2010] 排列计数](https://www.luogu.com.cn/problem/P2606)

可以发现 [[CSP-S2019 江西] 多叉堆](https://www.luogu.com.cn/problem/P5689) 是这个题的弱化版，但区别不算很大。

考虑依据偏序关系连边，可以发现构成一颗满足小根堆性质的树。

记 \(f_{i}\) 表示以点 \(i\) 为根的子树的方案数，显然子树内答案独立，故只需要考虑乘上分配给子树的方案数即可得 ：

\[
siz_i = siz_{2i} + siz_{2i + 1} + 1
\]

\[
f_i = f_{2i}\times f_{2i + 1}\times \dbinom{siz_i - 1}{siz_{2i}}
\]

因为模数有可能小于 \(n\)，所以求组合数需要用到 \(\rm Lucas\) 定理。

需要注意的是，在预处理阶乘逆元的时候最多预处理到 \(\rm mod - 1\)，否则会出现为 \(0\) 的情况。

总时间复杂度 \(\Theta(n\log n)\)。

```cpp
#include<bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define dep(i, r, l) for (int i = r; i >= l; i--)

const int N = 2e6 + 10;

int n, mod, Min, fac[N], inv[N], siz[N], f[N];

int Pow (int a, int k) {
    if (k == 0) return 1;
    if (k == 1) return a;
    int S = Pow(a, k >> 1);
    if (k & 1) return 1ll * S * S % mod * a % mod;
    else return 1ll * S * S % mod;
}

int Lucas (int n, int m) {
    if (n < mod && m < mod) {
        if (n < m) return 0;
        return 1ll * fac[n] * inv[m] % mod * inv[n - m] % mod;
    }
    return 1ll * Lucas(n / mod, m / mod) * Lucas(n % mod, m % mod) % mod;
}

int main () {

    cin >> n >> mod, Min = min(n, mod - 1);
    
    fac[0] = 1;
    rep(i, 1, Min) fac[i] = 1ll * fac[i - 1] * i % mod;
    inv[Min] = Pow(fac[Min], mod - 2);
    dep(i, Min - 1, 0) inv[i] = 1ll * inv[i + 1] * (i + 1) % mod;

    rep(i, 1, n) siz[i] = 1;
    dep(i, n, 1) siz[i] += siz[i << 1] + siz[i << 1 | 1];
    rep(i, ((n + 1) >> 1), n) f[i] = 1;
    dep(i, ((n + 1) >> 1) - 1, 1) {
        f[i] = 1ll * f[i << 1] * f[i << 1 | 1] % mod * Lucas(siz[i] - 1, siz[i << 1]) % mod;
    }

    printf("%d\n", f[1]);

    return 0;
}
```
