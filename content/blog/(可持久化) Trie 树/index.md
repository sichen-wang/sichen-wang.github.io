---
title: "(可持久化) Trie 树"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "(可持久化) Trie 树"
aliases:
  - "/blog/ke-chi-jiu-hua-trie-shu/"
tags:
  - "Data Structures"
  - "Strings"
  - "Trie"
categories:
  - "CP"
---

## 字典树

顾名思义，字典树就是支持像字典一样加入和查询字符串的树形数据结构，实现如下：

```cpp
namespace Trie {
    int Next[N][K], cnt, tag[N];

    void Insert (char *s) {
        int n = strlen(s + 1), now = 0;
        for (int i = 1; i <= n; i++) {
            int c = s[i] - 'a';
            if (!Next[now][c]) Next[now][c] = ++cnt;
            now = Next[now][c];
        }
        tag[now]++;
    }

    int Find (char *s) {
        int n = strlen(s + 1), now = 0;
        for (int i = 1; i <= n; i++) {
            int c = s[i] - 'a';
            if (!Next[now][c]) return false;
            now = Next[now][c];
        }
        return tag[now];
    }
}
```

## 0/1 Trie

在很多问题中，字符串仅由 \(0\) 和 \(1\) 构成，这些问题存在一定的共性。

### 维护异或极值

考虑如下问题，给定一颗带边权的树，求 \(\max\limits_{i,j\in[1,n]} \oplus Path(i,j)\)。

由异或的性质，可知 \(\oplus Path(i,j)=\oplus Path(root,i)\oplus Path(root,j)\)。

所以可以把所有从根开始的路径的异或和表示成一个数字，这样就将问题转化成了求任意两个数字的异或的最大值，可以用 \(\rm 0/1\ Trie\) 解决。

### 维护异或和

考虑如下问题，给一些数，维护它们的异或和，支持插入，删除和全局 \(+1\)。

对于异或和的维护，发现 \(sum=\sum_{i=0}^{k2}^{i}\times [num_{i}\equiv 1\pmod 2]\)。

其中 \(sum\) 表示异或和，\(num_{i}\) 表示所有数中二进制的第 \(i\) 位为 \(1\) 的数量。这个式子体现在 \(\rm 0/1\ Trie\) 上就是对于所有以父亲边为 \(1\) 的结点为根的子树中有多少个 \(\rm Tag\)，令 \(\rm Tag\) 的数量为 \(num\)，这些结点的深度为 \(k\)，它们对答案的贡献即为 \(num\%2\times 2^{k}\)。

对于实现全局 \(+1\) 操作，从低位到高维建 \(\rm 0/1\ Trie\)，考虑将一个二进制数 \(+1\) 的一般操作，即找到从低位到高位的第一个 \(0\)，将它变成 \(1\)，数位比它低的 \(1\) 全部变成 \(0\)。 而这个做法体现在 \(\rm 0/1\ Trie\) 上可以将一个结点的两条指向儿子的出边交换，再递归向交换后的 \(0\) 边迭代操作。

### 0/1 Trie 合并

与线段树合并类似，实现如下：

```cpp
void Merge (int &p, int k) {
    if (!p || !k) { p = p + k; return; }
    tag[p] += tag[k];
    Merge(l[p], l[k]), Merge(r[p], r[k]);
    Push_up();
}
```

需要注意的是，Trie 树合并和线段树合并一样，只有当每次合并的集合没有交集的时候复杂度才是 \(\Theta(n\log n)\) 的。

## 可持久化 Trie 树

可持久化 Trie 的实现方式和可持久化线段树的方式是相似的，即每次只修改被添加或值被修改的节点，而保留没有被改动的节点，在上一个版本的基础上连边，使最后每个版本的 Trie 树的根遍历所能分离出的 Trie 树都是完整且包含全部信息的。实现如下：

```cpp
namespace Trie {
    int rt[N << 5], Next[N << 5][2], cnt, tag[N << 5];

    void Build (int &x, int y, int k, int pos) {
    	if (pos < 0) return;
        x = ++cnt;
        if (!pos) tag[x]++;
        tag[x] += tag[y];
        int d = (k & (1 << pos)) != 0;
        Next[x][d ^ 1] = Next[y][d ^ 1];
        Build(Next[x][d], Next[y][d], k, pos - 1);
    }

    int Query (int x, int y, int k, int pos) {
    	if (!x) return 0;
        int d = (k & (1 << pos)) != 0;
        return tag[x] - tag[y] + Query(Next[x][d], Next[y][d], k, pos - 1);
    }
}
```

## 经典例题

### [LG4735] 最大异或和

可持久化 \(0/1\) Trie 模板题。

考虑记所有的前缀和，答案变为统计 \(x\oplus sum_{n}\) 在 \([l-1,r-1]\) 这个区间的 \(0/1\) Trie 中的最大异或值。

### [CF455B] A Lot of Games

显然直接建立 Trie 树，每次相当于向 Trie 树的子树内走一步，不能走者为负。

考虑设 \(f\) 表示是否存在必胜策略，\(g\) 表示是否存在必败策略，转移显然。

对 \(f_{root}\) 和 \(g_{root}\) 分四种情况讨论，每种情况下的答案易得。需要注意的是，如果先手既存在必胜策略又存在必败策略，那他可以故意输以获得下一局的先手，然后在最后一局获得胜利。

### [CF888G] Xor-MST

\(\rm Trie+Boruvka\)。

考虑将所有树插入一个 Trie 中，枚举到某个连通块时将其中所有点从 Tire 中删除，再用连通块中每个结点从 Trie 中查找出最小边权，完成后再将连通块中的点权加回去。

发现一个性质，每次合并的连通块都是 Trie 中某个节点的左右子树，再由 Trie 的性质，我们甚至不需要把 Trie 建出来，只需要将 A 排序，二分 Trie 的左右儿子，再将其中一个儿子的所有结点建 Trie，用另一个儿子中的所有结点在其中查找连通块之间的最小边权即可。

由于每个结点最多被加进 Trie 树 \(\log n\) 次，每次复杂度为 \(\log W\)，所以总时间复杂度为 \(\Theta(n\log n\log W)\)。
