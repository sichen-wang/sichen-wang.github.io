---
title: "线性同余方程"
date: "2023-06-24 11:00:56"
card_summary: ""
slug: "线性同余方程"
aliases:
  - "/blog/xian-xing-tong-yu-fang-cheng/"
tags:
  - "Number Theory"
  - "Linear Congruence"
categories:
  - "CP"
---

考虑如何求解以下方程 ：

<div>
\[
ax\equiv 1\pmod b
\]
</div>

显然可以转化为 ：

<div>
\[
ax+by=1
\]
</div>

有裴蜀定理 :

> 对于不定方程 \(ax+by=c\)，其有解当且仅当 \(\gcd(a,b)|c\)。

可以发现上述方程有解当且仅当 \(\gcd(a,b)=1\)，故可以转化为 ：

<div>
\[
ax+by=\gcd(a,b)
\]
</div>

观察到当 \(b=0\) 时方程有特解 \(x=1,y=0\)，于是考虑如何递归求解。

因为上式中有辗转相除的影子，于是尝试构造 ：

<div>
\[
bx'+(a~mod~b)y'=\gcd(b,a~mod~b)
\]
</div>

有 \(a\ mod\ b=a-\lfloor\frac{a}{b}\rfloor b\)，化简可得 ：

<div>
\[
ay'+b\left(x'-\lfloor\frac{a}{b}\rfloor y'\right)=\gcd(b,a~mod~b)=
\gcd(a,b)
\]
</div>

于是我们发现，如果求出了方程 \(bx'+(a\ mod\ b)y'=\gcd(b,a\ mod\ b)\) 的解 \(x'\) 和 \(y'\)，那么方程 \(ax+by=\gcd(a,b)\) 的解为 ：

<div>
\[
x=y',y=x'-\lfloor\frac{a}{b}\rfloor y'
\]
</div>

于是这样就可以在辗转相除的过程中递归求解了，时间复杂度 \(\Theta(\log n)\)。

```cpp
#include<bits/stdc++.h>
using namespace std;

int a, b, x, y;	

void Exgcd (int a, int b) {
	if (b == 0) {
		x = 1 , y = 0;
		return;
	}
	Exgcd(b, a % b);
	int tmp = x;
	x = y, y = tmp - a / b * y;
}

int main () {

	cin >> a >> b;
	
	Exgcd(a, b);
	
	cout << (x + b) % b << endl;

	return 0;
}
```
