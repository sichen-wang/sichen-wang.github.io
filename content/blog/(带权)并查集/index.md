---
title: "(带权)并查集"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "(带权)并查集"
aliases:
  - "/blog/dai-quan-bing-cha-ji/"
tags:
  - "Data Structures"
  - "Disjoint Set Union"
  - "Graph Theory"
categories:
  - "CP"
---

## 用途

并查集可以用来维护一类具有传递性的关系，维护形如将 \(x\) 与 \(y\) 所在集合合并和询问 \(x\) 和 \(y\) 是否在同一个集合的操作。

## 实现

### 查询祖先节点

对于普通并查集来说，有路径压缩和按秩合并等优化，路径压缩一般实现如下 ：

```cpp
int Find (int x) {
    if (x != fa[x]) fa[x] = Find(fa[x]);
    return fa[x];
}
```

按秩合并则取点数小的连向点数大的即可。

而对于带边权的并查集，我们需要在路径压缩的时候考虑加上其父亲的权值以维护其到根的差值，有路径压缩优化的带权并查集一般实现如下 ：

```cpp
int Find (int x) {
    if (x != fa[x]) {
        int mark = fa[x];
        fa[x] = Find(fa[x]), val[x] += val[mark];
    }
    return fa[x];
}
```

由于路径压缩后 \(x\) 的父亲就是根节点了，所以需要记录其父亲到根的总权值并加到它的边权上。

另外，如果要查询某个点 \(x\) 到根的权值和，由于一次路径压缩以后 \(x\) 的父亲会变成根，而此时的 \(val_{x}\) 就是路径和，所以可以先调用一次 `Find(x)`，此时的 \(val_{x}\) 即为答案。

### 合并两个结点所在集合

对于普通并查集来说，两个集合合并直接将其中一个根节点接到另一个根节点上即可。

而对于带权并查集而言，我们必须求出需要连接的两个根节点之间连边的权值，而这个权值是可以直接确定的，假设现在要给 \(x\to y\) 连一条长度为 \(w\) 的边，设 \(x\) 的祖先为 \(Rx\)，则 \(val_{Rx}=val_{y}+w-val_{x}.\) 另外，如果 \(x\) 和 \(y\) 已经在同一个集合中，并且 \(val_{Rx}+val_{x}-val_{y}\not = w\)，则这条连边不合法。实现如下 ：

```cpp
bool Merge (int x, int y, int w) {
    int Rx = Find(x), Ry = Find(y);
    if (Rx != Ry) fa[Rx] = Ry, val[Rx] = val[y] + w - val[x];
    return val[Rx] + val[x] - val[y] == w;
}
```

## Code

带路径压缩和按秩合并优化的普通并查集 :

```cpp
int Find (int x) {
    if (x != fa[x]) fa[x] = Find(fa[x]);
    return fa[x];
}

bool Merge (int x, int y) {
    int Rx = Find(x), Ry = Find(y);
    if (x != y) {
        if (pnum[Rx] < pnum[Ry])
            fa[Rx] = Ry, pnum[Ry] += pnum[Rx];
        else fa[Ry] = Rx, pnum[Rx] += pnum[Ry];
    }
    return Rx != Ry;
}
```

带路径压缩和按秩合并优化的带权并查集 ：

```cpp
int Find (int x) {
    if (x != fa[x]) {
        int mark = fa[x];
        fa[x] = Find(fa[x]), val[x] += val[mark];
    }
    return fa[x];
}
bool Merge (int x, int y, int w) {
    int Rx = Find(x), Ry = Find(y);
    if (Rx == Ry) return (val[x] - val[y] == w);
    if (pnum[Rx] < pnum[Ry])
        fa[Rx] = Ry, pnum[Ry] += pnum[Rx], val[Rx] = val[y] + w - val[x];
    else fa[Ry] = Rx, pnum[Rx] += pnum[Ry], val[Ry] = val[x] - w - val[y];
    return true;
}
```

不带任何优化的并查集复杂度是 \(\Theta(n^{2})\) 的。

带路径压缩的并查集时间复杂度 \(\Theta(n \log n)\)，期望复杂度 \(\Theta(n \alpha(n))\)。

再加上按秩合并可以做到严格 \(\Theta(n \alpha(n))\)。
