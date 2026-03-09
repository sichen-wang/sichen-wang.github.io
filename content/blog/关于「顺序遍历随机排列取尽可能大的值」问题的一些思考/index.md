---
title: "关于「顺序遍历随机排列取尽可能大的值」问题的一些思考"
date: "2024-04-11 17:23:40"
card_summary: ""
slug: "关于「顺序遍历随机排列取尽可能大的值」问题的一些思考"
aliases:
  - "/blog/guan-yu-shun-xu-bian-li-sui-ji-pai-lie-qu-jin-ke-neng-da-de-zhi-wen-ti-de-yi-xie-si-kao/"
tags:
  - "Probability"
  - "Optimal Stopping"
categories:
  - "Research"
---

一个广为流传的结论是: 从前往后遍历 \(37\%\) 的元素(事实上是 \(\frac{1}{e}\)), 称其中最大的为 \(\max\), 继续往后遍历, 一旦一个元素大于 \(\max\) 就立刻选择, 找不到则选最后一个元素 .

写了一个程序来验证这个结论:

```python
import random
import matplotlib.pyplot as draw

n, t = map(int, input().split()) # n, t = 1000, 100000
p = [i for i in range(n)]
aveval = [0 for _ in range(n)]
maxval = [0 for _ in range(n)]

def calcave (pos):
    Max = -1
    for i in range(pos): Max = max(Max, p[i])
    for i in range(pos, n):
        if p[i] > Max: return p[i]
    return p[n - 1]

def calcmax (pos):
    Max = -1
    for i in range(pos): Max = max(Max, p[i])
    for i in range(pos, n):
        if p[i] > Max: return (p[i] == n - 1)
    return (p[n - 1] == n - 1)

for _ in range(t):
    random.shuffle(p)
    for i in range(n): aveval[i] += calcave(i)
    for i in range(n): maxval[i] += calcmax(i)

aveval = list(map(lambda x: x / t / n, aveval))
maxval = list(map(lambda x: x / t, maxval))

draw.plot([100 / n * i for i in range(n)], aveval)
draw.plot([100 / n * i for i in range(n)], maxval)

idx, val = 0, 0
for i in range(n):
    if aveval[i] > val:
        val, idx = aveval[i], 100 / n * i
draw.plot(idx, val, 'or')
draw.text(idx, val, "({:.1f}%, {:.2f})".format(idx, val), color = 'r')
idx, val = 0, 0
for i in range(n):
    if maxval[i] > val:
        val, idx = maxval[i], 100 / n * i
draw.plot(idx, val, 'or')
draw.text(idx, val, "({:.1f}%, {:.2f})".format(idx, val), color = 'r')

draw.show()
```

得到结果如下:

![pFXdXyd.png](https://s21.ax1x.com/2024/04/11/pFXdXyd.png)

其中蓝线为这种策略取到的元素大小期望除以 \(n\) 的值, 也即取到的元素占最大值百分比的期望. 橙线表示取到最大值的概率. 横坐标为观察的元素数量占总元素数量的比例.

可以发现, 虽然观察 \(37.1\%\) 的元素有最大的概率取到最大值, 但只观察 \(3.1\%\) 的元素就出手获得的元素期望是最大的, 这启发我们, 直接取某一个位置之后的第一个前缀最大值是否有些呆板了呢? 我们是否可以做一些更加动态的决策呢?

接下来会尝试训练一个神经网络用以决策, 未完待续……
