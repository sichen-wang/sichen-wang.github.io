---
title: "The Movement Complexity of Sorting"

authors:
  - me

# arXiv v1 submission date.
date: 2026-10-31

publication_types: ["manuscript"]
publication: "*Preprint*, arXiv:2611.01157"
publication_short: "Preprint"

# 列表页卡片显示的一句话摘要（作者审定的中文稿译出）。
tldr: 'We determine the optimal head movement for sorting on a $d$-dimensional grid in $r$ rounds, up to polylogarithmic factors.'

# 与 arXiv v1 main.tex 的 \begin{abstract} 一致。
abstract: |
  The complexity of sorting is usually measured by the number of comparisons. This
  measure ignores the movement of the read heads between comparisons, which is a real
  cost on many machines. We study this cost on its own. Keys lie on a $d$-dimensional
  grid, two heads move over the grid and compare the keys beneath them, and the only
  cost is the total movement of the heads. The algorithm plans its route in $r$ rounds
  and sees the outcomes of each round only after running it. For every $d$ and $r$ we
  determine the expected movement needed to sort $n$ keys: it is $n^{\beta}$ up to
  polylogarithmic factors, where $\beta=1+D^{r-1}/(D^{r}-(D-1)^{r})$ and $D=2d$,
  falling from $n^{2}$ at $r=1$ to $n^{1+1/(2d)}$ with unlimited rounds. Our algorithm
  makes every round move about the same amount, and a matching lower bound holds
  against every algorithm.

tags:
  - Sorting
  - Lower Bounds
  - Data Movement

featured: false

links:
  - type: pdf
    url: paper.pdf
    label: Paper
  - type: preprint
    provider: arxiv
    id: 2611.01157
    label: arXiv
---

<article class="ltx_document ltx_authors_1line">




<div class="ltx_pagination ltx_role_newpage"></div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="introduction">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">The comparison model counts comparisons and nothing else, which for sorting gives the classical
$\Theta(n\log n)\text{.}$ This count is not the whole cost of sorting. On general sequential models the product
of time and space for sorting is $\Omega(n^{2}/\log n)$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib6" title="A time-space tradeoff for sorting on a general sequential model of computation" class="ltx_ref">BC82</a>]</cite>, later strengthened to
$\Omega(n^{2})$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib7" title="A general sequential time-space tradeoff for finding unique elements" class="ltx_ref">Bea91</a>]</cite>. On many machines the further cost is travel, because the two keys of a
comparison must first be brought within reach. On a Turing machine with one worktape and a two-way
read-only input tape, sorting an input of $N$ bits, made of strings of $3\log N$ bits each, takes
$\Omega(N^{3/2}/\sqrt{\log N})$ steps <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib33" title="An optimal lower bound for Turing machines with one work tape and a two-way input tape" class="ltx_ref">MS86</a>; <a href="#bib.bib14" title="The complexity of matrix transposition on one-tape off-line Turing machines" class="ltx_ref">DMS91</a>]</cite>. This bound comes from the distance the heads must
travel: two heads on tapes of length $t$ need $\Omega(t^{3/2})$ steps to reach the pairs of tape positions
given by a well-scattered permutation <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib14" title="The complexity of matrix transposition on one-tape off-line Turing machines" class="ltx_ref">DMS91</a>]</cite>.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">Adaptivity has its own classical measure. In the parallel comparison model <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib40" title="Parallelism in comparison problems" class="ltx_ref">Val75</a>]</cite>, an
algorithm commits a set of comparisons in each round and learns the outcomes when the round ends, and
the exponents of the number of comparisons for sorting, selection, and merging in $r$ rounds are
known <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib40" title="Parallelism in comparison problems" class="ltx_ref">Val75</a>; <a href="#bib.bib12" title="Parallel sorting" class="ltx_ref">BT83</a>; <a href="#bib.bib23" title="Sorting and merging in rounds" class="ltx_ref">HH82</a>; <a href="#bib.bib2" title="Tight complexity bounds for parallel comparison sorting" class="ltx_ref">AAV86</a>; <a href="#bib.bib1" title="Sorting, approximate sorting, and searching in rounds" class="ltx_ref">AA88</a>; <a href="#bib.bib36" title="Sorting and selecting in rounds" class="ltx_ref">Pip87</a>; <a href="#bib.bib5" title="Parallel selection with high probability" class="ltx_ref">BB90</a>]</cite>. This theory charges nothing for moving
between comparisons, and the bounds on travel above say nothing about rounds. We ask: <em class="ltx_emph ltx_font_italic">How much must
a processor travel to sort $n$ keys it cannot move, if it plans its route in $r$ rounds and learns the
outcomes of each round only after running it?</em></p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">We study the simplest model with this cost. The $n$ keys lie one at each position of the grid
$[m]^{d}\text{,}$ where $n=m^{d}\text{,}$ and they carry a hidden total
order. Two heads move over the grid in unit steps, and the algorithm learns about the order only by
comparing the two keys beneath the heads. It must output the list of positions in increasing order of
rank. The positions of the two heads form a point of the <em class="ltx_emph ltx_font_italic">comparison grid</em> $[m]^{2d}\text{,}$ and two keys are
compared when this point reaches their pair of positions, in either order. An
$r$-round algorithm commits a route at the start of each round, as a function of its coins and of the
outcomes of earlier rounds, and it receives the outcomes at all points of the route only after running it.
Comparisons, computation, and memory are free, and the only cost is the <em class="ltx_emph ltx_font_italic">movement</em>, the total
$\ell_{1}$ distance the heads move. The algorithm must be correct on every input and for every outcome of
its coins, and $M_{r}^{(d)}(n)$ is the least expected movement on a worst input. For $r=\infty$ the number
of rounds is free. <a href="#S2.SS1" title="2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.1</span></a> gives the precise definition. The grid is the basic metric space of polynomial
growth, and the proofs use little beyond the sizes of its balls and its partitions into cubes and boxes.</p>
</div>
<div id="S1.p4" class="ltx_para">
<p class="ltx_p">Two baselines bound the answer. For $r=1\text{,}$ the oblivious case, the single route is fixed in advance and must compare
all $\binom{n}{2}$ pairs, so $M_{1}^{(d)}(n)=\Theta(n^{2})\text{.}$ For $r=\infty\text{,}$ the fully adaptive case, a merge sort attains $O(n^{1+1/(2d)})\text{,}$ and this
matches the lower bound of <a href="#S4.Thmtheorem5" title="Proposition 4.5. ‣ 4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">4.5</span></a>.</p>
</div>
<section id="S1.SS0.SSS0.Px1" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="problem">Problem.</h4>

<div id="S1.SS0.SSS0.Px1.p1" class="ltx_para">
<p class="ltx_p">For every dimension $d$ and every round budget $r\text{,}$ determine $M_{r}^{(d)}(n)\text{,}$ the least
worst-case expected movement with which an $r$-round algorithm sorts $n$ keys on $[m]^{d}\text{.}$</p>
</div>
</section>
<section id="S1.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="our-results">
<span class="ltx_tag ltx_tag_subsection">1.1 </span>Our Results</h3>

<div id="S1.SS1.p1" class="ltx_para">
<p class="ltx_p">We determine the exponent for every $d$ and $r\text{.}$</p>
</div>
<div id="S1.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 1.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Movement Exponent)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S1.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix $d\geq 1$ and $r\in\{1,2,\dots\}\cup\{\infty\}\text{,}$ and let $D=2d\text{.}$ For finite $r$ put</span></p>
<table id="S1.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\beta_{r}^{(d)}=1+\frac{D^{\,r-1}}{D^{\,r}-(D-1)^{r}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p"><span class="ltx_text ltx_font_italic">so that $\beta_{1}^{(d)}=2\text{,}$ and let $\beta_{\infty}^{(d)}=\lim_{r\to\infty}\beta_{r}^{(d)}=1+\tfrac{1}{2d}\text{.}$
Then $M_{r}^{(d)}(n)=\widetilde{\Theta}\bigl(n^{\beta_{r}^{(d)}}\bigr)\text{,}$ and
$M_{r}^{(d)}(n)=\Theta\bigl(n^{\beta_{r}^{(d)}}\bigr)$ whenever $d=1\text{,}$ $r\leq 2\text{,}$ or $r=\infty\text{.}$ The upper
bounds are attained by explicit polynomial-time algorithms, deterministic for $r=1$ and $r=\infty$ and
randomized otherwise.</span></p>
</div>
</div>
<div id="S1.SS1.p2" class="ltx_para">
<p class="ltx_p">The exponent decreases from
$2$ at $r=1$ to $1+\tfrac{1}{2d}$ as $r\to\infty\text{,}$ each further round lowering
it by a geometrically shrinking amount (<a href="#S2.Thmtheorem6" title="Remark 2.6. ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>), and for $r\geq 2$ it also decreases in $d\text{.}$ The
number of heads, by contrast, does not affect it: two heads are what a comparison needs, and any fixed
number of heads changes the complexity by at most a constant factor (<a href="#S7.Thmtheorem1" title="Proposition 7.1. ‣ 7 Multiple Heads ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">7.1</span></a>). We call the range
$d\geq 2\text{,}$ $3\leq r&lt;\infty$ the <em class="ltx_emph ltx_font_italic">interior</em>. The logarithmic factors hidden by $\widetilde{\Theta}$ occur only there.
<a href="#S1.T1" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Table</span> <span class="ltx_text ltx_ref_tag">1</span></a> lists the exponent at small parameters, and <a href="#S6" title="6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6</span></a> ends with the proof of the theorem.</p>
</div>
<figure id="S1.T1" class="ltx_table">
<figcaption class="ltx_caption ltx_centering"><span class="ltx_tag ltx_tag_table">Table 1: </span>The movement exponent $\beta_{r}^{(d)}\text{.}$ Every entry gives the exact order
$\Theta\bigl(n^{\beta_{r}^{(d)}}\bigr)\text{,}$ except those marked $\dagger\text{,}$ which lie in the interior. There
the order is known up to a polylogarithmic factor and conjectured exact (<a href="#S8.Thmtheorem1" title="Conjecture 8.1. ‣ 8 Discussion ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Conjecture</span> <span class="ltx_text ltx_ref_tag">8.1</span></a>).</figcaption>
<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle" style="white-space:nowrap;">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_column ltx_th_row ltx_border_r ltx_border_tt" style="border-right:1px solid currentColor;"></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">$r=1$</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">$r=2$</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">$r=3$</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">$r=4$</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">$r=\infty$</th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_r ltx_border_t" style="border-right:1px solid currentColor;padding-bottom:2.0pt;">$d=1$</th>
<td class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom:2.0pt;">$2$</td>
<td class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom:2.0pt;">$\tfrac{5}{3}$</td>
<td class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom:2.0pt;">$\tfrac{11}{7}$</td>
<td class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom:2.0pt;">$\tfrac{23}{15}$</td>
<td class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom:2.0pt;">$\tfrac{3}{2}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_r" style="border-right:1px solid currentColor;padding-bottom:2.0pt;">$d=2$</th>
<td class="ltx_td ltx_align_center" style="padding-bottom:2.0pt;">$2$</td>
<td class="ltx_td ltx_align_center" style="padding-bottom:2.0pt;">$\tfrac{11}{7}$</td>
<td class="ltx_td ltx_align_center" style="padding-bottom:2.0pt;">$\tfrac{53}{37}^{\dagger}$</td>
<td class="ltx_td ltx_align_center" style="padding-bottom:2.0pt;">$\tfrac{239}{175}^{\dagger}$</td>
<td class="ltx_td ltx_align_center" style="padding-bottom:2.0pt;">$\tfrac{5}{4}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_bb ltx_border_r" style="border-right:1px solid currentColor;">$d=3$</th>
<td class="ltx_td ltx_align_center ltx_border_bb">$2$</td>
<td class="ltx_td ltx_align_center ltx_border_bb">$\tfrac{17}{11}$</td>
<td class="ltx_td ltx_align_center ltx_border_bb">$\tfrac{127}{91}^{\dagger}$</td>
<td class="ltx_td ltx_align_center ltx_border_bb">$\tfrac{887}{671}^{\dagger}$</td>
<td class="ltx_td ltx_align_center ltx_border_bb">$\tfrac{7}{6}$</td>
</tr>
</tbody>
</table>
</figure>
<div id="S1.SS1.p3" class="ltx_para">
<p class="ltx_p">On the line the exponent is tied to selection rather than to sorting (<a href="#S5.Thmtheorem12" title="Remark 5.12. ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark</span> <span class="ltx_text ltx_ref_tag">5.12</span></a>): $\beta_{r}^{(1)}=1+\tfrac{1}{2}s_{r}\text{,}$ where $s_{r}=1+1/(2^{r}-1)$ is the
exponent of the worst-case number of comparisons that a deterministic algorithm needs to find the maximum of $n$ keys in $r$
rounds <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib40" title="Parallelism in comparison problems" class="ltx_ref">Val75</a>; <a href="#bib.bib23" title="Sorting and merging in rounds" class="ltx_ref">HH82</a>]</cite>, while the number of comparisons for sorting in $r$ rounds has exponent $1+1/r$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib2" title="Tight complexity bounds for parallel comparison sorting" class="ltx_ref">AAV86</a>]</cite>.</p>
</div>
</section>
<section id="S1.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="overview">
<span class="ltx_tag ltx_tag_subsection">1.2 </span>Overview</h3>

<div id="S1.SS2.p1" class="ltx_para">
<p class="ltx_p">The cost of a round depends on how many pairs of positions it must visit and on how these pairs are spread. Call an
unordered pair of positions a <em class="ltx_emph ltx_font_italic">cell</em>. If $Q$ cells are spread evenly over the $n^{2}$ points of the comparison grid,
their nearest-neighbor spacing is about $(n^{2}/Q)^{1/D}\text{,}$ and a route through them moves about $Q\cdot(n^{2}/Q)^{1/D}\text{:}$
their number times their spacing, as for tours through random point sets <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib9" title="The shortest path through many points" class="ltx_ref">BHH59</a>; <a href="#bib.bib37" title="Subadditive Euclidean functionals and nonlinear growth in geometric probability" class="ltx_ref">Ste81</a>; <a href="#bib.bib43" title="Probability Theory of Classical Euclidean Optimization Problems" class="ltx_ref">Yuk98</a>]</cite>. The two baselines
are instances of this product. All $\binom{n}{2}$ cells have spacing $1\text{,}$ which gives $n^{2}\text{.}$ The $\Theta(n)$ cells of
consecutive ranks, which every algorithm must compare, have spacing about $n^{1/D}$ on a random input, which gives
$n^{1+1/(2d)}\text{.}$</p>
</div>
<div id="S1.SS2.p2" class="ltx_para">
<p class="ltx_p">With $r$ rounds, the early rounds can reduce the number of cells left for the final one, at the cost of their own movement.
Our algorithm makes every round move about the same amount. This gives one equation per round, and the solution of these equations
is the exponent of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Movement Exponent). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>. The lower bound leads to the same equations, which is why the two exponents agree.</p>
</div>
<section id="S1.SS2.SSS0.Px1" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="the-algorithm">The Algorithm.</h4>

<div id="S1.SS2.SSS0.Px1.p1" class="ltx_para">
<p class="ltx_p">The algorithm keeps <em class="ltx_emph ltx_font_italic">segments</em>, sets of keys of consecutive ranks whose internal order is not
yet known, and refines them round by round. In round $1$ it chooses $n/b_{0}$ random positions, the <em class="ltx_emph ltx_font_italic">splitters</em>, for a parameter $b_{0}\text{.}$ One head stops
on each splitter in turn while the other sweeps the grid, so the movement is $n^{2}/b_{0}\text{,}$ and the keys between two consecutive
splitters form a segment of about $b_{0}$ keys. The final round, the <em class="ltx_emph ltx_font_italic">cleanup</em>, compares all pairs inside segments. If round $2$ is the final one, these
are about $nb_{0}$ cells, known in advance, and a serpentine route through them moves about their number times their spacing
(<a href="#S5.SS1" title="5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>), as in the classical tours through given points <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib15" title="The shortest path and the shortest road through n points" class="ltx_ref">Few55</a>; <a href="#bib.bib34" title="Spacefilling curves and the planar travelling salesman problem" class="ltx_ref">PB89</a>]</cite>. Making the two movements equal gives the
exponent for $r=2\text{.}$</p>
</div>
<div id="S1.SS2.SSS0.Px1.p2" class="ltx_para">
<p class="ltx_p">With more rounds, refinement rounds come in between. A refinement round selects <em class="ltx_emph ltx_font_italic">pivots</em>, keys that are compared with every key of
their segment, and these cut the segments further. Selecting each key independently, at the rate the refinement needs, fails: the cells of the round are then spread over
the whole grid, and the route through them moves a polynomial factor more than the other rounds. So the round selects pivots in groups
of nearby positions. It cuts the grid into cubes of side $h\text{,}$ selects each cube with probability $p\text{,}$ and takes the keys of the selected
cubes as pivots. The cells then lie in the <em class="ltx_emph ltx_font_italic">product boxes</em> $I\times J$ of a selected cube $J$ and another cube $I\text{,}$ and the heads
go through these boxes one after another. If the segments entering the round have about $b$ keys, this moves about $p\,h\,nb$ for
$h=(n/b)^{1/D}\text{.}$</p>
</div>
<div id="S1.SS2.SSS0.Px1.p3" class="ltx_para">
<p class="ltx_p">The refined segments can still have many keys, but they meet few cubes. List a key’s segment in rank order, starting at the key: each new
cube is selected with probability $p\text{,}$ so a pivot appears after $1/p$ cubes in expectation. Hence the <em class="ltx_emph ltx_font_italic">dispersion</em>, the sum over the
keys of the number of cubes that the key’s segment meets, has expectation about $n/p\text{,}$ as for segments of $1/p$ keys. On the line, a bound
on the dispersion is all that the next round needs.</p>
</div>
<div id="S1.SS2.SSS0.Px1.p4" class="ltx_para">
<p class="ltx_p">So the parameters of the algorithm (<a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>) are a decreasing sequence of rank scales $b_{j}=n^{a_{j}}\text{,}$ $0\leq j\leq r-2\text{,}$ the
<em class="ltx_emph ltx_font_italic">schedule</em>, with finest scale $g=b_{r-2}\text{.}$ On the line, round $j+1$ uses $p=1/b_{j}$ and $h=(n/b_{j-1})^{1/D}\text{.}$ For $d\geq 2$ the
samples are more elaborate, as explained below, but the movement has the same exponent. Requiring every round to move the
same amount $n^{\beta}$ gives one equation per round:</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="Sx1.EGx1"></span><span class="paper-eq-anchor" id="S1.Ex2"></span><span class="paper-eq-anchor" id="S1.Ex3"></span><span class="paper-eq-anchor" id="S1.Ex4"></span><div class="paper-eqgroup-body">$$\begin{aligned}
 &amp; \text{splitter:}\qquad &amp; \displaystyle\beta &amp; \displaystyle=2-a_{0}, \\
 &amp; \text{refinement }j\text{:}\qquad &amp; \displaystyle\beta &amp; \displaystyle=1+\frac{1-a_{j-1}}{D}+a_{j-1}-a_{j}\qquad(1\leq j\leq r-2), \\
 &amp; \text{cleanup:}\qquad &amp; \displaystyle\beta &amp; \displaystyle=1+a_{r-2}+\frac{1-a_{r-2}}{D}.
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p class="ltx_p">The right-hand sides are the exponents of $n^{2}/b_{0}\text{,}$ of $p\,h\,nb_{j-1}\text{,}$ and of $ng\,(n/g)^{1/D}\text{,}$ which is again a number times a
spacing. By <a href="#S2.Thmtheorem5" title="Lemma 2.5. ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>, the unique solution has $\beta=\beta_{r}^{(d)}\text{.}$</p>
</div>
<div id="S1.SS2.SSS0.Px1.p5" class="ltx_para">
<p class="ltx_p">For $d\geq 2$ the cleanup needs more. Visiting $Q$ cells in the product box of two cubes of side $h$ moves about $h\,Q^{1-1/D}\text{.}$ On the line
this exponent is $\tfrac{1}{2}\text{,}$ and the sum of the $\sqrt{Q}$ over the boxes is at most the dispersion. For $d\geq 2$ the exponent is larger, and
the sum also depends on the sizes of the segments. So the cleanup needs small dispersion, for the tour between the product boxes, and a small
sum of squared segment sizes, for the visits inside them. Sampling cubes gives the first and sampling keys gives the second, so at $r=3$ the
refinement round draws both samples (<a href="#S6.SS2" title="6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6.2</span></a>). For $r\geq 4$ a refinement round can be followed by another one, whose cost depends
on the dispersion of its input, counted with boxes of many sizes. So each refinement round draws one sample for each box size of a nested
partition of the grid, up to a threshold, and the analysis keeps an upper bound on the expected dispersion for each of these sizes
(<a href="#S6.SS3" title="6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6.3</span></a>). This costs a factor $\log n$ for the number of samples and a factor $\log n$ for the number of box sizes per sample.</p>
</div>
</section>
<section id="S1.SS2.SSS0.Px2" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="the-lower-bound">The Lower Bound.</h4>

<div id="S1.SS2.SSS0.Px2.p1" class="ltx_para">
<p class="ltx_p">By Yao’s principle, it suffices to consider deterministic algorithms on the <em class="ltx_emph ltx_font_italic">uniform input</em>, a uniformly random assignment of the ranks to
the positions <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib41" title="Probabilistic computations: toward a unified measure of complexity" class="ltx_ref">Yao77</a>]</cite>. Call a cell <em class="ltx_emph ltx_font_italic">co-blocked at scale $b$</em> if its two ranks lie in one block of $b$ consecutive ranks, the blocks
being cut from rank $1$ upward. There are $\Theta(ng)$ cells co-blocked at scale $g\text{,}$ and the final round must visit every one of them whose two positions have not been compared in earlier rounds with another
position of their block. Take such a cell $\{u,v\}\text{.}$ The earlier outcomes do not determine the order of $u$ and $v\text{,}$ because a chain of outcomes from one to the other stays inside
the block and starts with a comparison of $u$ or $v$ with another position of the block. So these outcomes are consistent with two inputs that
give $u$ and $v$ adjacent ranks, in opposite orders. The final round runs the same route on both, and only the cell $\{u,v\}$ tells them apart, so
this route must visit it (<a href="#S4.Thmtheorem2" title="Lemma 4.2. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>). On the uniform input a constant fraction of these cells are at distance about $(n/g)^{1/D}$ from all
others (<a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>). So if the earlier rounds compare only a small fraction of the positions inside their blocks, the final route moves
about $ng\,(n/g)^{1/D}$ (<a href="#S3.Thmtheorem2" title="Fact 3.2. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>), and the cleanup equation says that this is $n^{\beta}\text{.}$</p>
</div>
<div id="S1.SS2.SSS0.Px2.p2" class="ltx_para">
<p class="ltx_p">It remains to show that rounds moving much less than $n^{\beta}$ compare few positions inside their blocks. The route of round $1$ is fixed before
any outcome is known, so each cell on it is co-blocked at scale $b_{0}$ with probability at most about $b_{0}/n\text{.}$ A route of movement $n^{\beta}$
therefore visits about $n^{\beta}b_{0}/n$ such cells, and the splitter equation says that this number is $n\text{.}$ So a much shorter route compares only a small fraction of the
positions inside their blocks. For $r=2$ we have $b_{0}=g\text{,}$ and the proof is complete.</p>
</div>
<div id="S1.SS2.SSS0.Px2.p3" class="ltx_para">
<p class="ltx_p">From round $2$ on, a route can use what the algorithm has learned to choose cells that are likely to be co-blocked, and this adaptivity is the hard part
of the lower bound. The proof handles it round by round, like the chronogram method for dynamic data-structure lower bounds <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib18" title="The cell probe complexity of dynamic data structures" class="ltx_ref">FS89</a>]</cite>, with rounds in
place of epochs, and like round elimination in communication complexity <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib32" title="On data structures and asymmetric communication complexity" class="ltx_ref">MNSW98</a>]</cite>. For round $j+1\text{,}$ two facts replace the estimate above.</p>
</div>
<div id="S1.SS2.SSS0.Px2.p4" class="ltx_para">
<p class="ltx_p">The first bounds the number
of cells a route can visit. On the uniform input, with high probability, every route of movement $L$ visits at most about
$\bigl(1+L(b_{j-1}/n)^{1/D}\bigr)\log n$ cells co-blocked at scale $b_{j-1}$ (<a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a>). This is a property of the input alone, so it holds for
adaptive routes.</p>
</div>
<div id="S1.SS2.SSS0.Px2.p5" class="ltx_para">
<p class="ltx_p">The second bounds the probability that such a cell is co-blocked at the next scale. The proof gives the algorithm more information, which
can only help it: after round $j\text{,}$ for $j\leq r-2\text{,}$ the index, or <em class="ltx_emph ltx_font_italic">label</em>, of the block of each position at scale $b_{j-1}$ is revealed at no cost. Given
all labels and outcomes so far, the positions of a block that have not been compared with another position of the block still receive the ranks left to them in
uniformly random order, because exchanging their ranks changes no label and no outcome. So if at least half of the block is of this kind, a cell that is co-blocked at
scale $b_{j-1}$ and contains such a position is co-blocked at scale $b_{j}$ with conditional probability only $O(b_{j}/b_{j-1})$ (<a href="#S4.Thmtheorem8" title="Lemma 4.8. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.8</span></a>). Blocks with fewer
such positions are counted as entirely compared.</p>
</div>
<div id="S1.SS2.SSS0.Px2.p6" class="ltx_para">
<p class="ltx_p">Multiplying the two bounds, a route of movement $n^{\beta}$ in round $j+1$ visits about
$n^{\beta}(b_{j-1}/n)^{1/D}\,b_{j}/b_{j-1}$ cells of this kind, up to a logarithmic factor, and the refinement equation says that this number is $n\text{.}$ So here too a much shorter route
compares only a small fraction of the positions inside their blocks.</p>
</div>
</section>
<section id="S1.SS2.SSS0.Px3" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="removing-the-logarithms">Removing the Logarithms.</h4>

<div id="S1.SS2.SSS0.Px3.p1" class="ltx_para">
<p class="ltx_p">The factors $\log^{2}n$ in the upper bound and $\log n$ in the lower bound do not always occur. The factor $\log^{2}n$ comes only from the samples for many
box sizes, so the upper bound has no logarithmic factor for $d=1$ and for $r\leq 3\text{.}$ The factor $\log n$ comes only from <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a>, where the
largest number of co-blocked cells in one product box enters. For $r\leq 2$ the route of the first round is fixed in advance, so this lemma is not needed. On
the line, <a href="#S4.Thmtheorem13" title="Lemma 4.13. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemmas</span> <span class="ltx_text ltx_ref_tag">4.13</span></a> and <a href="#S4.Thmtheorem14" title="Lemma 4.14. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.14</span></a> avoid the loss: they group nearby co-blocked cells into clusters, a route visits few cells of small clusters per
unit of movement, and the large clusters hold at most one cell in expectation. For $r=\infty\text{,}$ a merge sort over a partition of the grid into boxes matches the
bound $n^{1+1/(2d)}$ given by the cells of consecutive ranks (<a href="#S4.Thmtheorem5" title="Proposition 4.5. ‣ 4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Propositions</span> <span class="ltx_text ltx_ref_tag">4.5</span></a> and <a href="#S5.Thmtheorem3" title="Proposition 5.3. ‣ 5.2 The Fully Adaptive Bound ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.3</span></a>).</p>
</div>
<div id="S1.SS2.SSS0.Px3.p2" class="ltx_para">
<p class="ltx_p"><a href="#S2" title="2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a> defines the model and solves the equations, and <a href="#S3" title="3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a> proves the geometric facts used by the lower bound.
<a href="#S4" title="4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a> proves the lower bound, with the exact order on the line in <a href="#S4.SS4" title="4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.4</span></a>, and
<a href="#S5" title="5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Sections</span> <span class="ltx_text ltx_ref_tag">5</span></a> and <a href="#S6" title="6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a> prove the upper bounds. <a href="#S7" title="7 Multiple Heads ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7</span></a> treats more than two
heads, and <a href="#S8" title="8 Discussion ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">8</span></a> discusses the remaining gap.</p>
</div>
</section>
</section>
<section id="S1.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="related-work">
<span class="ltx_tag ltx_tag_subsection">1.3 </span>Related Work</h3>

<div id="S1.SS3.p1" class="ltx_para">
<p class="ltx_p">The models closest to ours attach costs to comparisons. Priced information charges every query and asks
for the cheapest correct computation <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib13" title="Query strategies for priced information" class="ltx_ref">CFG<sup class="ltx_sup">+</sup>02</a>]</cite>, and for sorting and selection the costs have been taken
structured or metric <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib21" title="Sorting and selection with structured costs" class="ltx_ref">GK01</a>; <a href="#bib.bib22" title="Where&#x27;s the winner? Max-finding and sorting with metric costs" class="ltx_ref">GK05</a>]</cite>. In the metric model a comparison costs the distance between its two keys.
There the costs of the comparisons add up independently, whereas here consecutive comparisons share the heads, so a
comparison costs only the move from the previous comparison. As a result, the cost of a round depends on how its
comparisons are distributed in the comparison grid, and not only on how many there are. <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemmas</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> and <a href="#S3.Thmtheorem2" title="Fact 3.2. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.2</span></a>
give the upper and the lower bound for a given distribution. The benchmark also differs: these
works measure a competitive ratio against the cheapest proof of the order, while we determine the absolute cost on a
worst input. For sorting this ratio is polylogarithmic for metric costs <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib22" title="Where&#x27;s the winner? Max-finding and sorting with metric costs" class="ltx_ref">GK05</a>]</cite>, and for general costs a
polylogarithmic ratio is known only in a bichromatic special case <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib20" title="An algorithm for bichromatic sorting with polylog competitive ratio" class="ltx_ref">GJ24</a>]</cite>. A separate line restricts which
comparisons are admissible at all, as in generalized sorting and the $1$-$\infty$ cost
model <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib24" title="Algorithms for the generalized sorting problem" class="ltx_ref">HKK11</a>; <a href="#bib.bib28" title="Stochastic and worst-case generalized sorting revisited" class="ltx_ref">KN21</a>; <a href="#bib.bib11" title="Sorting under forbidden comparisons" class="ltx_ref">BR16</a>]</cite>.</p>
</div>
<div id="S1.SS3.p2" class="ltx_para">
<p class="ltx_p">Sorting and selection in rounds come from Valiant’s parallel comparison model <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib40" title="Parallelism in comparison problems" class="ltx_ref">Val75</a>]</cite>. They were studied
extensively there <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib12" title="Parallel sorting" class="ltx_ref">BT83</a>; <a href="#bib.bib23" title="Sorting and merging in rounds" class="ltx_ref">HH82</a>; <a href="#bib.bib2" title="Tight complexity bounds for parallel comparison sorting" class="ltx_ref">AAV86</a>; <a href="#bib.bib1" title="Sorting, approximate sorting, and searching in rounds" class="ltx_ref">AA88</a>; <a href="#bib.bib36" title="Sorting and selecting in rounds" class="ltx_ref">Pip87</a>; <a href="#bib.bib5" title="Parallel selection with high probability" class="ltx_ref">BB90</a>]</cite> and remain active <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib10" title="Sorted top-k in rounds" class="ltx_ref">BMP19</a>]</cite>. These results count
comparisons, and the place of a comparison plays no role in them. We keep the round structure and replace the cost by
movement, and on the line the movement exponent is determined by the exponent $s_{r}$ of <a href="#S1.SS1" title="1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>.</p>
</div>
<div id="S1.SS3.p3" class="ltx_para">
<p class="ltx_p">A universal tour orders $n$ points once and serves every subset in that order. In the plane, the space-filling curve
gives a competitive ratio of $\Theta(\log n)$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib34" title="Spacefilling curves and the planar travelling salesman problem" class="ltx_ref">PB89</a>; <a href="#bib.bib8" title="Worst-case examples for the spacefilling curve heuristic for the Euclidean traveling salesman problem" class="ltx_ref">BG89</a>]</cite>, and no universal tour has a constant
ratio <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib25" title="Improved lower and upper bounds for universal TSP in planar metrics" class="ltx_ref">HKL06</a>; <a href="#bib.bib29" title="Lower bounds for the universal TSP on the plane" class="ltx_ref">Kra26</a>]</cite>. On general metrics, sparse partitions <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib17" title="Scattering and sparse partitions, and their applications" class="ltx_ref">Fil24</a>]</cite> give polylogarithmic
ratios <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib27" title="Universal approximations for TSP, Steiner tree, and set cover" class="ltx_ref">JLN<sup class="ltx_sup">+</sup>05</a>; <a href="#bib.bib19" title="Oblivious network design" class="ltx_ref">GHR06</a>]</cite>. The a priori TSP asks the same question in expectation <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib26" title="A priori solution of a traveling salesman problem in which a random subset of the customers are visited" class="ltx_ref">Jai88</a>]</cite>. These problems share
with ours the commitment of a route before it is known which visits matter. There the tour is fixed once and judged by
its ratio to the best tour for the subset, while our algorithm commits a new route every round and we determine the
absolute movement.</p>
</div>
<div id="S1.SS3.p4" class="ltx_para">
<p class="ltx_p">Travel has also been studied for element distinctness, on the Turing machine above <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib35" title="Element distinctness and sorting on one-tape off-line Turing machines" class="ltx_ref">Pet08</a>]</cite> and on the one-tape
machine without an input tape <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib31" title="New lower bounds for element distinctness on a one-tape Turing machine" class="ltx_ref">LO94</a>; <a href="#bib.bib4" title="Element distinctness on one-tape Turing machines: a complete solution" class="ltx_ref">BABP03</a>]</cite>. Other models charge for moving data. On a mesh-connected computer,
records travel along the links to their destinations <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib39" title="Sorting on a mesh-connected parallel computer" class="ltx_ref">TK77</a>]</cite>, and on a VLSI chip, the information that must cross the
chip gives area-time trade-offs <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib38" title="The VLSI complexity of sorting" class="ltx_ref">Tho83</a>]</cite>. Token swapping rearranges labeled tokens along the edges of a
graph and counts the swaps <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib42" title="Swapping labeled tokens on graphs" class="ltx_ref">YDI<sup class="ltx_sup">+</sup>15</a>]</cite>. External-memory sorting transports records between memory levels, and
its classical lower bound treats the records as indivisible <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib3" title="The input/output complexity of sorting and related problems" class="ltx_ref">AV88</a>]</cite>. Under the network-coding conjecture of Li and
Li, the same bound holds without this assumption <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib30" title="Network coding: the case of multiple unicast sessions" class="ltx_ref">LL04</a>; <a href="#bib.bib16" title="Lower bounds for external memory integer sorting via network coding" class="ltx_ref">FHLS19</a>]</cite>. Here the keys stay in their positions, so the
lower bound needs neither assumption, and the comparisons it counts are forced by correctness alone (<a href="#S4.Thmtheorem11" title="Remark 4.11. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark</span> <span class="ltx_text ltx_ref_tag">4.11</span></a>).</p>
</div>
</section>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="preliminaries">
<span class="ltx_tag ltx_tag_section">2 </span>Preliminaries</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">This section makes the model of <a href="#S1" title="1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">1</span></a> precise and solves the equations of <a href="#S1.SS2" title="1.2 Overview ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">1.2</span></a>, which
give the exponent and the rank scales used by both bounds.</p>
</div>
<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-model">
<span class="ltx_tag ltx_tag_subsection">2.1 </span>The Model</h3>

<div id="S2.Thmtheorem1" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.1</span></span><span class="ltx_text ltx_font_bold"> </span>(The Movement Model)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p">Fix $d\geq 1$ and $m\geq 2\text{,}$ let $n=m^{d}\text{,}$ and write $[m]=\{1,\dots,m\}\text{.}$</p>
<ol id="S2.I1" class="ltx_enumerate">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Input and output.</em> Every position $x\in[m]^{d}$ holds one key, and the keys carry a
hidden total order: the input is a bijection $\pi\colon[m]^{d}\to[n]\text{,}$ and
$\operatorname{rk}_{\pi}(x)=\pi(x)$ is the rank of the key at $x\text{.}$ The algorithm learns about $\pi$ only
through the outcomes of item 3. The output is the list of positions in increasing order of
rank.</p>
</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Configurations and routes.</em> Two heads occupy positions $x,y\in[m]^{d}\text{,}$ and the pair
$(x,y)$ is their <em class="ltx_emph ltx_font_italic">configuration</em>. The configurations are the points of the
<em class="ltx_emph ltx_font_italic">comparison grid</em> $[m]^{D}\text{,}$ where $D=2d\text{.}$ A <em class="ltx_emph ltx_font_italic">route</em> is a sequence of
configurations $z_{0},\dots,z_{L}$ with $\lVert z_{t+1}-z_{t}\rVert_{1}=1$ for $0\leq t&lt;L\text{.}$
The <em class="ltx_emph ltx_font_italic">movement</em> of the route is $L\text{.}$ Both heads start at the position $(1,\dots,1)\text{.}$</p>
</div>
</li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S2.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Comparisons.</em> The <em class="ltx_emph ltx_font_italic">outcome</em> at a configuration $(x,y)$ is whether
$\operatorname{rk}_{\pi}(x)&lt;\operatorname{rk}_{\pi}(y)\text{.}$ Comparisons, computation, and memory are free.</p>
</div>
</li>
<li id="S2.I1.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">4.</span> 
<div id="S2.I1.i4.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Rounds.</em> An <em class="ltx_emph ltx_font_italic">$r$-round algorithm</em> proceeds in $r$ rounds. At the start of each
round it commits, as a function of its random coins and of the outcomes received in
earlier rounds, a route that starts at the current configuration. It then runs the route
and receives the outcomes at all configurations on it. No choice made within a round
depends on outcomes of that round.</p>
</div>
</li>
<li id="S2.I1.i5" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">5.</span> 
<div id="S2.I1.i5.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Correctness and cost.</em> The algorithm must output the correct order for every input
and every outcome of its coins. We
write $\mathrm{Move}(\mathrm{ALG},\pi)$ for the total movement of an algorithm
$\mathrm{ALG}$ on input $\pi\text{,}$ and</p>
<table id="S2.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$M_{r}^{(d)}(n)=\inf_{\mathrm{ALG}}\ \max_{\pi}\ \mathbb{E}\bigl[\mathrm{Move}(\mathrm{ALG},\pi)\bigr],$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">the infimum over $r$-round algorithms. For $r=\infty\text{,}$ $M_{\infty}^{(d)}(n)=\inf_{r}M_{r}^{(d)}(n)\text{.}$</p>
</div>
</li>
</ol>
</div>
</div>
<div id="S2.Thmtheorem2" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.2</span></span><span class="ltx_text ltx_font_bold"> </span>(Cells)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">cell</em> is an unordered pair $\{x,y\}$ of distinct positions. Its two <em class="ltx_emph ltx_font_italic">orientations</em> are
the configurations $(x,y)$ and $(y,x)\text{.}$ On cells, the metric $\operatorname{dist}$ is</p>
<table id="S2.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{dist}\bigl(\{x,y\},\{x^{\prime},y^{\prime}\}\bigr)=\min\bigl\{\lVert x-x^{\prime}\rVert_{1}+\lVert y-y^{\prime}\rVert_{1},\ \lVert x-y^{\prime}\rVert_{1}+\lVert y-x^{\prime}\rVert_{1}\bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">and for a cell $w$ and a set $W$ of cells we put $\operatorname{dist}(w,W)=\min_{w^{\prime}\in W}\operatorname{dist}(w,w^{\prime})\text{,}$ with
$\operatorname{dist}(w,\emptyset)=+\infty\text{.}$</p>
</div>
</div>
<div id="S2.Thmtheorem3" class="ltx_theorem ltx_theorem_observation">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Observation 2.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem3.p1" class="ltx_para">
<ol id="S2.I2" class="ltx_enumerate">
<li id="S2.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(a)</span> 
<div id="S2.I2.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">A route of movement </span>$L$<span class="ltx_text ltx_font_italic"> visits at most </span>$L+1$<span class="ltx_text ltx_font_italic"> configurations.</span></p>
</div>
</li>
<li id="S2.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(b)</span> 
<div id="S2.I2.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The two orientations of a cell carry the same information, and a configuration </span>$(x,x)$<span class="ltx_text ltx_font_italic">
carries none. On the configurations with </span>$x\neq y$<span class="ltx_text ltx_font_italic">, the map
</span>$(x,y)\mapsto\{x,y\}$<span class="ltx_text ltx_font_italic"> is </span>$1$<span class="ltx_text ltx_font_italic">-Lipschitz from </span>$\ell_{1}$<span class="ltx_text ltx_font_italic"> to </span>$\operatorname{dist}$<span class="ltx_text ltx_font_italic">. Hence deleting the
configurations </span>$(x,x)$<span class="ltx_text ltx_font_italic"> from a route of movement </span>$L$<span class="ltx_text ltx_font_italic"> leaves a sequence of cells of
</span>$\operatorname{dist}$<span class="ltx_text ltx_font_italic">-length at most </span>$L$<span class="ltx_text ltx_font_italic">. The number of cells within </span>$\operatorname{dist}$<span class="ltx_text ltx_font_italic">-distance </span>$\rho$<span class="ltx_text ltx_font_italic"> of a cell
</span>$\{x,y\}$<span class="ltx_text ltx_font_italic"> is at most the number of points of </span>$[m]^{D}$<span class="ltx_text ltx_font_italic"> within </span>$\ell_{1}$<span class="ltx_text ltx_font_italic">-distance </span>$\rho$<span class="ltx_text ltx_font_italic"> of
</span>$(x,y)$<span class="ltx_text ltx_font_italic">.
On the line, </span>$(x,y)\mapsto(\min\{x,y\},\max\{x,y\})$<span class="ltx_text ltx_font_italic"> folds the configurations onto
</span>$\{x\leq y\}$<span class="ltx_text ltx_font_italic"> and the cells onto </span>$\{x&lt;y\}$<span class="ltx_text ltx_font_italic">, and </span>$\operatorname{dist}$<span class="ltx_text ltx_font_italic"> is the </span>$\ell_{1}$<span class="ltx_text ltx_font_italic"> distance between
the folded cells.</span></p>
</div>
</li>
</ol>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS1.p1" class="ltx_para">
<p class="ltx_p">Part (a) holds because the route consists of $z_{0},\dots,z_{L}\text{.}$ For (b), when $x\neq y$ the
outcome at $(y,x)$ is the negation of the outcome at $(x,y)\text{,}$ and the outcome at $(x,x)$ is always
negative. By definition, $\operatorname{dist}(\{x,y\},\{x^{\prime},y^{\prime}\})$ is the smaller of the $\ell_{1}$ distances from
$(x,y)$ to the two orientations of $\{x^{\prime},y^{\prime}\}\text{,}$ so the $\ell_{1}$ distance of two configurations is
at least the $\operatorname{dist}$ of their cells, which is the Lipschitz property. Since the swap
$(x,y)\mapsto(y,x)$ is an isometry of $\ell_{1}\text{,}$ $\operatorname{dist}$ is a metric on cells. Between two
consecutive configurations that survive the deletion, the route moves at least their $\ell_{1}$
distance, so the cells have $\operatorname{dist}$-length at most $L\text{.}$ A cell within $\operatorname{dist}$-distance $\rho$ of
$\{x,y\}$ has an orientation within $\ell_{1}$-distance $\rho$ of $(x,y)\text{,}$ and distinct cells have no
orientation in common, which gives the count. On the line, if $x&lt;y$ and $x^{\prime}&lt;y^{\prime}\text{,}$ then
$t\mapsto|t-y^{\prime}|-|t-x^{\prime}|$ is nonincreasing, and comparing its values at $x$ and at $y$ gives
$|x-x^{\prime}|+|y-y^{\prime}|\leq|x-y^{\prime}|+|y-x^{\prime}|\text{.}$ So the minimum in $\operatorname{dist}$ is the $\ell_{1}$ distance between
$(x,y)$ and $(x^{\prime},y^{\prime})\text{.}$
∎</p>
</div>
</div>
<div id="S2.SS1.p2" class="ltx_para">
<p class="ltx_p">Since the keys do not move, we identify each key with its position, so a set of keys is a set of
positions. When $\pi$ is fixed we write $\operatorname{rk}$ for $\operatorname{rk}_{\pi}\text{.}$ The algorithm <em class="ltx_emph ltx_font_italic">compares</em> $x$
and $y$ in round $t$ if the route of round $t$ visits an orientation of $\{x,y\}\text{.}$ In the same
way, a route visits a set of cells if it visits an orientation of each, and a cell lies in a set of
configurations if one of its orientations does.</p>
</div>
<section id="S2.SS1.SSS0.Px1" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="notation">Notation.</h4>

<div id="S2.SS1.SSS0.Px1.p1" class="ltx_para">
<p class="ltx_p">Throughout, $d$ and $r$ are fixed and asymptotic statements refer to $n\to\infty\text{.}$ A subscript on
an asymptotic symbol lists the parameters other than $n$ on which the hidden constant depends, in
the order $d\text{,}$ $r\text{,}$ and, in <a href="#S7" title="7 Multiple Heads ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7</span></a>, $k\text{,}$ as in $O_{d}$ or $\Omega_{d,r}\text{.}$ A symbol without a subscript hides an
absolute constant. <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Movement Exponent). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> carries no subscripts, and its constants depend on
$d$ and $r\text{.}$ A tilde, as in $\widetilde{\Theta}\text{,}$ also hides factors polylogarithmic in $n\text{.}$
Logarithms are to base $2\text{.}$ When the algorithm and the input are clear, we write $\mathrm{Move}$
for $\mathrm{Move}(\mathrm{ALG},\pi)\text{.}$</p>
</div>
<div id="S2.SS1.SSS0.Px1.p2" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">box</em> is a product of intervals of integers, viewed as a set of lattice points. Its
<em class="ltx_emph ltx_font_italic">side</em> along an axis is the number of its points on a line parallel to that axis, and a
<em class="ltx_emph ltx_font_italic">cube</em> is a box whose sides are equal. A <em class="ltx_emph ltx_font_italic">ball</em> is the set of grid points within a given
$\ell_{1}$ distance of a center. When we partition the line into
intervals of $h$ positions, or $[m]^{d}$ into cubes of side $H\text{,}$ the last piece along each axis may
be shorter, which affects only constants.</p>
</div>
</section>
</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-scale-schedule">
<span class="ltx_tag ltx_tag_subsection">2.2 </span>The Scale Schedule</h3>

<div id="S2.Thmtheorem4" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.4</span></span><span class="ltx_text ltx_font_bold"> </span>(Scales and Blocks)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">scale</em> is a number $b$ with $1\leq b\leq n\text{.}$ For an integer scale $b\text{,}$ the <em class="ltx_emph ltx_font_italic">scale-$b$ blocks</em> are the sets of ranks
$\{(i-1)b+1,\dots,ib\}\cap[n]$ for $i=1,\dots,\lceil n/b\rceil\text{.}$ Each holds $b$ ranks except
possibly the last, and $i$ is the <em class="ltx_emph ltx_font_italic">label</em> of the $i$-th block. A position lies in a block if
its rank does. The scale $b$ is <em class="ltx_emph ltx_font_italic">dyadic</em> if it is a power of two. Every block of a dyadic
scale lies in a block of each larger dyadic scale. For finite $r\geq 2\text{,}$ a <em class="ltx_emph ltx_font_italic">schedule</em> is a
sequence $b_{j}=n^{a_{j}}\text{,}$ $0\leq j\leq r-2\text{,}$ with exponents $1&gt;a_{0}&gt;a_{1}&gt;\dots&gt;a_{r-2}&gt;0\text{.}$ Its
finest term is $g=b_{r-2}\text{.}$</p>
</div>
</div>
<div id="S2.SS2.p1" class="ltx_para">
<p class="ltx_p">For finite $r\geq 2\text{,}$ both bounds use the schedule determined by the following system in the
unknowns $\beta,a_{0},\dots,a_{r-2}\text{.}$ It has one equation for the splitter round of the algorithm,
one for each refinement round $j=1,\dots,r-2\text{,}$ and one for the cleanup round. Each states that the
movement of that round is $n^{\beta}\text{,}$ and <a href="#S1.SS2" title="1.2 Overview ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">1.2</span></a> explains the three expressions.</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="Sx1.EGx2"></span><span class="paper-eq-anchor" id="S2.E1"></span><span class="paper-eq-anchor" id="S2.E2"></span><span class="paper-eq-anchor" id="S2.E3"></span><div class="paper-eqgroup-body">$$\begin{aligned}
 &amp; \text{splitter:}\qquad &amp; \displaystyle\beta &amp; \displaystyle=2-a_{0}, \\
 &amp; \text{refinement }j\text{:}\qquad &amp; \displaystyle\beta &amp; \displaystyle=1+\frac{1-a_{j-1}}{D}+a_{j-1}-a_{j}\qquad(1\leq j\leq r-2), \\
 &amp; \text{cleanup:}\qquad &amp; \displaystyle\beta &amp; \displaystyle=1+a_{r-2}+\frac{1-a_{r-2}}{D}.
\end{aligned}$$</div><div class="paper-eqgroup-no paper-eqgroup-no-rows"><span class="paper-eqgroup-number">(2.1)</span><span class="paper-eqgroup-number">(2.2)</span><span class="paper-eqgroup-number">(2.3)</span></div></div>

</div>
<div id="S2.Thmtheorem5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 2.5</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $r\geq 2$ and let $q=(D-1)/D\text{.}$ The system of <a href="#S2.E1" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, <a href="#S2.E2" title="Equation 2.2 ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a> and <a href="#S2.E3" title="Equation 2.3 ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.3</span></a> has
the unique solution</span></p>
<table id="S2.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\beta=\beta_{r}^{(d)}=1+\frac{1-q}{1-q^{\,r}},\qquad a_{j}=\frac{q^{\,j+1}-q^{\,r}}{1-q^{\,r}}\quad(0\leq j\leq r-2),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p"><span class="ltx_text ltx_font_italic">and $1&gt;a_{0}&gt;a_{1}&gt;\dots&gt;a_{r-2}&gt;0\text{,}$ so the $a_{j}$ define a schedule. We write
$\delta=\beta_{r}^{(d)}-1=(1-q)/(1-q^{\,r})\text{,}$ so $a_{0}=1-\delta\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS2.p2" class="ltx_para">
<p class="ltx_p">For a solution, write $\delta=\beta-1$ and $t_{j}=1-a_{j}\text{.}$ <a href="#S2.E1" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.1</span></a> gives $t_{0}=\delta\text{.}$
Since $q=1-1/D\text{,}$ <a href="#S2.E2" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> reads $t_{j}=q\,t_{j-1}+\delta\text{,}$ so</p>
<table id="S2.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$t_{j}=\delta\,(1+q+\dots+q^{\,j})\qquad(0\leq j\leq r-2),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">and <a href="#S2.E1" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">2.1</span></a> and <a href="#S2.E2" title="Equation 2.2 ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a> determine every $a_{j}$ from $\delta\text{.}$ <a href="#S2.E3" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a> reads
$\delta=1-q\,t_{r-2}\text{,}$ that is, $\delta\,(1+q+\dots+q^{\,r-1})=1\text{,}$ whose unique solution is
$\delta=(1-q)/(1-q^{\,r})\text{.}$ Hence $\beta=\beta_{r}^{(d)}\text{,}$ and $t_{j}=(1-q^{\,j+1})/(1-q^{\,r})$ gives
$a_{j}=(q^{\,j+1}-q^{\,r})/(1-q^{\,r})\text{.}$ Finally,
$a_{j}-a_{j+1}=q^{\,j+1}(1-q)/(1-q^{\,r})&gt;0$ for $0\leq j\leq r-3\text{,}$
$a_{r-2}=q^{\,r-1}(1-q)/(1-q^{\,r})&gt;0\text{,}$ and $a_{0}=1-\delta&lt;1\text{.}$
∎</p>
</div>
</div>
<div id="S2.SS2.p3" class="ltx_para">
<p class="ltx_p">From now on, for given $d$ and finite $r\geq 2\text{,}$ the exponents $a_{0},\dots,a_{r-2}$ are those of
<a href="#S2.Thmtheorem5" title="Lemma 2.5. ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>, $b_{j}=n^{a_{j}}$ is their schedule, and $g=b_{r-2}\text{.}$ The algorithms use the
$b_{j}$ as real parameters. In <a href="#S4" title="4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a>, where blocks must nest, $b_{j}$ denotes the largest
power of two not exceeding $n^{a_{j}}\text{,}$ which differs from $n^{a_{j}}$ by a factor less than $2\text{.}$</p>
</div>
<div id="S2.Thmtheorem6" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 2.6</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S2.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p">Since $(1-q)/(1-q^{\,r})=1/(1+q+\dots+q^{\,r-1})\text{,}$ and the sum $1+q+\dots+q^{\,r-1}$ increases
strictly in $r$ and, for $r\geq 2\text{,}$ in $q=1-1/(2d)\text{,}$ the exponent $\beta_{r}^{(d)}$ decreases strictly in $r$
and, for $r\geq 2\text{,}$ in $d\text{.}$ It lies in $(1+\tfrac{1}{2d},\,2]\text{.}$ Its distance to the fully adaptive
exponent satisfies</p>
<table id="S2.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\beta_{r}^{(d)}-\Bigl(1+\frac{1}{2d}\Bigr)=\frac{q^{\,r}(1-q)}{1-q^{\,r}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="geometry-of-the-comparison-grid">
<span class="ltx_tag ltx_tag_section">3 </span>Geometry of the Comparison Grid</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">This section proves three facts about the comparison grid that the lower bound uses. A route that
visits many cells far apart from one another has large movement (<a href="#S3.Thmtheorem2" title="Fact 3.2. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>). The other two facts
concern the <em class="ltx_emph ltx_font_italic">uniform input</em>, a uniformly random bijection $\pi\colon[m]^{d}\to[n]\text{.}$ With
probability at least $7/8\text{,}$ at least half of the cells whose two positions lie in a common block of
ranks are far from all other such cells (<a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>). With probability at least $1-n^{-10}\text{,}$
every route, however it is chosen, visits few such cells per unit of movement (<a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a>).</p>
</div>
<div id="S3.Thmtheorem1" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 3.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Co-Blocked Cells)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p">Two positions are <em class="ltx_emph ltx_font_italic">co-blocked</em> at an integer scale $b$ if their ranks lie in the same scale-$b$ block. A
cell is co-blocked at scale $b$ if its two positions are. We write $\mathcal{C}_{b}$ for the
set of cells co-blocked at scale $b\text{.}$</p>
</div>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">The set $\mathcal{C}_{b}$ depends on the input, but its size does not. For integer $b$ with $2\leq b\leq n$ we have $\tfrac{1}{4}n(b-1)\leq|\mathcal{C}_{b}|\leq\tfrac{1}{2}n(b-1)\text{,}$ and in particular
$|\mathcal{C}_{b}|\geq nb/8\text{.}$ Indeed, $2|\mathcal{C}_{b}|$ is the sum over all positions $x$ of
the number of other positions co-blocked with $x\text{.}$ Every position is co-blocked with at most $b-1$
others, which gives the upper bound. At least $n/2$ positions lie in blocks of exactly $b$ ranks,
since $b\lfloor n/b\rfloor\geq n/2\text{,}$ and each of them is co-blocked with exactly $b-1$ others, which
gives the lower bound. On the uniform input, two fixed positions are co-blocked at scale $b$ with
probability at most $b/n\text{:}$ given the rank of one, the rank of the other is uniform over the
remaining $n-1$ ranks, at most $b-1$ of which lie in its block, and $(b-1)/(n-1)\leq b/n\text{.}$</p>
</div>
<div id="S3.Thmtheorem2" class="ltx_theorem ltx_theorem_fact">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Fact 3.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $Y$ be a metric space with metric $\operatorname{dist}_{Y}\text{,}$ and let $W\subseteq Y$ be finite with
$|W|\geq 2\text{.}$ For $w\in W$ let $\nu_{W}(w)=\min_{w^{\prime}\in W\setminus\{w\}}\operatorname{dist}_{Y}(w,w^{\prime})\text{.}$ Then every
finite sequence of points of $Y$ that contains every point of $W$ has length at least
$\tfrac{1}{2}\sum_{w\in W}\nu_{W}(w)\text{,}$ where the length of a sequence is the sum of the distances
between consecutive points.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">Keeping only the first occurrence of each point of $W$ gives a path through $W$ that, by the
triangle inequality, is no longer than the sequence. So the sequence is at least as long as a
minimum spanning tree of $W\text{.}$ Charge each $w\in W$ to a shortest edge of this tree at $w\text{.}$ That
edge has length at least $\nu_{W}(w)\text{,}$ and each edge is charged at most twice, so
$\sum_{w\in W}\nu_{W}(w)$ is at most twice the length of the tree.
∎</p>
</div>
</div>
<div id="S3.p4" class="ltx_para">
<p class="ltx_p">We apply <a href="#S3.Thmtheorem2" title="Fact 3.2. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">3.2</span></a> to cells with the metric $\operatorname{dist}\text{.}$ Let $\rho&gt;0\text{,}$ and let a route of movement
$L$ visit every cell of a set $W$ of at least two cells that are pairwise more than $\rho$ apart.
Deleting the configurations $(x,x)$ from the route leaves a sequence of cells of $\operatorname{dist}$-length at
most $L$ that contains every cell of $W$ (<a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(b)). Since $\nu_{W}(w)&gt;\rho$ for every
$w\in W\text{,}$ <a href="#S3.Thmtheorem2" title="Fact 3.2. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">3.2</span></a> gives $L\geq\tfrac{1}{2}|W|\rho\text{.}$</p>
</div>
<div id="S3.Thmtheorem3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every integer scale $b\geq 2$ there is a radius $\rho=\Theta_{d}\bigl((n/b)^{1/D}\bigr)$ such that, with
probability at least $7/8$ over the uniform input, at least half of the cells $w\in\mathcal{C}_{b}$
satisfy $\operatorname{dist}(w,\mathcal{C}_{b}\setminus\{w\})&gt;\rho\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.p5" class="ltx_para">
<p class="ltx_p">We bound the expected number of pairs of cells of $\mathcal{C}_{b}$ that are close to each other
and apply Markov’s inequality. Let $\rho=\varepsilon_{0}(n/b)^{1/D}\text{,}$ where $0&lt;\varepsilon_{0}\leq 1$ depends only
on $d$ and is chosen below. Distinct cells are at distance at least $1\text{,}$ so if $\rho&lt;1$ every cell
satisfies the condition. Assume therefore that $\rho\geq 1\text{.}$ Let $Z$ be the number of ordered pairs $(w,w^{\prime})$ of
distinct cells of $\mathcal{C}_{b}$ with $\operatorname{dist}(w,w^{\prime})\leq\rho\text{.}$ A cell $w\in\mathcal{C}_{b}$ with
$\operatorname{dist}(w,\mathcal{C}_{b}\setminus\{w\})\leq\rho$ is the first entry of such a pair, so at most $Z$
cells violate the condition. It therefore suffices to show that
$\mathbb{E}Z\leq\tfrac{1}{16}|\mathcal{C}_{b}|\text{:}$ then Markov’s inequality applied to $Z$ gives
$Z\leq\tfrac{1}{2}|\mathcal{C}_{b}|$ with probability at least $7/8\text{.}$</p>
</div>
<div id="S3.p6" class="ltx_para">
<p class="ltx_p">A ball of radius $\rho$ in $[m]^{d}$ contains at most $(2\rho+1)^{d}\leq(3\rho)^{d}$ positions, and
by <a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(b) at most $(3\rho)^{D}$ cells lie within distance $\rho$ of a given cell. Two
distinct cells share at most one position, so every pair counted by $Z$ falls into exactly one of
the following two cases.</p>
<ul id="S3.I1" class="ltx_itemize">
<li id="S3.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I1.i1.p1" class="ltx_para">
<p class="ltx_p">The cells share a position: $w=\{u,v\}$ and $w^{\prime}=\{u,v^{\prime}\}$ with $v\neq v^{\prime}\text{.}$ Both lie in
$\mathcal{C}_{b}$ only if the ranks of $u\text{,}$ $v\text{,}$ and $v^{\prime}$ lie in one block. Given the rank of
$u\text{,}$ this has probability at most $\frac{b-1}{n-1}\cdot\frac{b-2}{n-2}\leq(b/n)^{2}\text{.}$ The
condition $\operatorname{dist}(w,w^{\prime})\leq\rho$ requires $\lVert v-v^{\prime}\rVert_{1}\leq\rho\text{,}$ or
$\lVert u-v^{\prime}\rVert_{1}+\lVert v-u\rVert_{1}\leq\rho\text{,}$ in which case both $v$ and $v^{\prime}$ lie
within distance $\rho$ of $u\text{.}$ There are therefore at most $n^{2}(3\rho)^{d}+n(3\rho)^{2d}$
such triples $(u,v,v^{\prime})\text{,}$ and these pairs contribute at most</p>
<table id="S3.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Bigl(\frac{b}{n}\Bigr)^{2}\bigl(n^{2}(3\rho)^{d}+n(3\rho)^{2d}\bigr)=3^{d}\varepsilon_{0}^{d}\,nb\Bigl(\frac{b}{n}\Bigr)^{1/2}+9^{d}\varepsilon_{0}^{2d}\,b\leq 2\cdot 9^{d}\varepsilon_{0}^{d}\,nb.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</li>
<li id="S3.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I1.i2.p1" class="ltx_para">
<p class="ltx_p">The cells have four distinct positions. There are at most $\tfrac{1}{2}n^{2}(3\rho)^{D}$ such
pairs. For each of them both cells lie in $\mathcal{C}_{b}$ with probability $O(b^{2}/n^{2})\text{,}$
because the first cell is co-blocked with probability at most $b/n$ and, given the ranks of
its positions, the second with probability at most $(b-1)/(n-3)\text{.}$ These pairs contribute</p>
<table id="S3.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$O\Bigl(\frac{b^{2}}{n^{2}}\Bigr)\cdot n^{2}(3\rho)^{D}=O\bigl(9^{d}\varepsilon_{0}^{2d}\,nb\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</li>
</ul>
<p class="ltx_p">Since $|\mathcal{C}_{b}|\geq nb/8$ and $\varepsilon_{0}\leq 1\text{,}$ there is a constant $c_{d}$ depending only
on $d$ such that the two contributions give $\mathbb{E}Z\leq c_{d}\,\varepsilon_{0}^{d}\,|\mathcal{C}_{b}|\text{.}$
Choosing $\varepsilon_{0}$ with $c_{d}\varepsilon_{0}^{d}\leq\tfrac{1}{16}$ completes the proof.
∎</p>
</div>
</div>
<div id="S3.Thmtheorem4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.4</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix a constant $\alpha&lt;1\text{.}$ There is a constant $c$ depending only on $d$ and $\alpha$ with the
following property. For a dyadic scale $b\leq n^{\alpha}\text{,}$ let $E_{b}$ be the event that every
route visits at most $c\bigl(1+L(b/n)^{1/D}\bigr)\log n$ cells of $\mathcal{C}_{b}\text{,}$ where $L$ is the
movement of the route. Then, for sufficiently large $n\text{,}$ with probability at least $1-n^{-10}$ over
the uniform input, $E_{b}$ holds for every dyadic scale $b\leq n^{\alpha}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.p7" class="ltx_para">
<p class="ltx_p">We partition the comparison grid into products of two cubes, show that with high probability none
of these products contains many cells of $\mathcal{C}_{b}\text{,}$ and then cut a route into pieces that
each stay in few of them. Let $n$ be large enough for the estimates below, and fix a dyadic scale
$b\leq n^{\alpha}\text{.}$</p>
</div>
<div id="S3.p8" class="ltx_para">
<p class="ltx_p">Let $s=\lceil(n/b)^{1/D}\rceil$ and partition $[m]^{d}$ into cubes of side $s\text{,}$ clipped at the
boundary. Since $(n/b)^{1/D}\geq 1\text{,}$ each cube contains at most $s^{d}\leq V$ positions, where
$V=2^{d}(n/b)^{1/2}\text{.}$ A <em class="ltx_emph ltx_font_italic">product box</em> is a set $I\times J\subseteq[m]^{D}$ for two of these
cubes $I$ and $J\text{.}$ There are at most $n^{2}$ product boxes. The <em class="ltx_emph ltx_font_italic">load</em> of $I\times J$ is
$|\mathcal{C}_{b}\cap(I\times J)|\text{,}$ the number of cells of $\mathcal{C}_{b}$ that lie in
$I\times J\text{.}$ Cells that share a position are correlated, while disjoint cells are nearly independent, so we
show that a product box of large load contains either many disjoint cells or a block with many of its positions.
Let $\zeta=\lceil 30/(1-\alpha)\rceil\text{,}$ $\mu=\lceil\max\{12\cdot 4^{d},\,13\log n\}\rceil\text{,}$
and $\Lambda_{0}=2\zeta\mu=O_{d,\alpha}(\log n)\text{.}$ We show that a fixed product box $I\times J$ has
load at least $\Lambda_{0}$ with probability at most $2n^{-13}\text{.}$ View the cells counted by the load
as the edges of a graph on $I\cup J\text{.}$ Every edge joins two positions of one block. If every block
contains fewer than $\zeta$ positions of $I\cup J\text{,}$ then every vertex has degree less than $\zeta\text{,}$
and a greedy matching, which discards fewer than $2\zeta$ edges for each edge it keeps, finds $\mu$
disjoint edges among any $\Lambda_{0}=2\zeta\mu$ edges. Hence, if the load is at least
$\Lambda_{0}\text{,}$ one of the following two events occurs.</p>
<ul id="S3.I2" class="ltx_itemize">
<li id="S3.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I2.i1.p1" class="ltx_para">
<p class="ltx_p">Some block contains at least $\zeta$ positions of $I\cup J\text{.}$ The probability that $\zeta$
given positions all lie in a given block is at most $(b/n)^{\zeta}\text{,}$ and $I\cup J$ has at
most $2V$ positions. A union bound over the at most $n$ blocks and the at most
$(2V)^{\zeta}$ sets of $\zeta$ positions bounds the probability of this event by</p>
<table id="S3.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$n\Bigl(\frac{2Vb}{n}\Bigr)^{\zeta}\leq n\bigl(2^{d+1}n^{-(1-\alpha)/2}\bigr)^{\zeta}\leq n^{-13},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">using $b\leq n^{\alpha}$ and $(1-\alpha)\zeta/2\geq 15\text{.}$</p>
</div>
</li>
<li id="S3.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I2.i2.p1" class="ltx_para">
<p class="ltx_p">Some $\mu$ disjoint cells of $\mathcal{C}_{b}$ lie in $I\times J\text{.}$ At most $V^{2}$ cells
lie in $I\times J\text{,}$ so there are at most $(V^{2})^{\mu}/\mu!$ sets of $\mu$ disjoint cells in
$I\times J\text{.}$ Given the ranks of the positions of the earlier cells of such a set, the next
cell is co-blocked with probability at most $(b-1)/(n-2\mu)\leq 2b/n\text{,}$ so all its cells are
co-blocked with probability at most $(2b/n)^{\mu}\text{.}$ Since $V^{2}b/n=4^{d}$ and
$\mu!\geq(\mu/3)^{\mu}\text{,}$ a union bound over these sets bounds the probability of this event
by</p>
<table id="S3.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{(2\cdot 4^{d})^{\mu}}{\mu!}\leq\Bigl(\frac{6\cdot 4^{d}}{\mu}\Bigr)^{\mu}\leq 2^{-\mu}\leq n^{-13}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</li>
</ul>
<p class="ltx_p">A union bound over the at most $\log n+1$ dyadic scales $b\leq n^{\alpha}$ and the at most $n^{2}$
product boxes of each shows that, with probability at least $1-n^{-10}\text{,}$ at every dyadic scale
$b\leq n^{\alpha}$ every product box has load less than $\Lambda_{0}\text{.}$</p>
</div>
<div id="S3.p9" class="ltx_para">
<p class="ltx_p">On this event we bound the number of cells of $\mathcal{C}_{b}$ that a route visits. Cut a route
$z_{0},\dots,z_{L}$ into the pieces $z_{is},\dots,z_{\min\{(i+1)s,L\}}$ for
$0\leq i\leq\lfloor L/s\rfloor\text{.}$ There are at most $1+L/s\leq 1+L(b/n)^{1/D}$ of them. Every
configuration $(x^{\prime},y^{\prime})$ of a piece lies within $\ell_{1}$-distance $s$ of the first configuration
$(x,y)$ of the piece, so $x^{\prime}$ lies in the cube of side $2s+1$ centered at $x\text{,}$ and $y^{\prime}$ in the cube
of side $2s+1$ centered at $y\text{.}$ Along each axis, $2s+1$ consecutive integers meet at most three
intervals of the partition, so each of these two cubes meets at most $3^{d}$ cubes of the
partition, and the piece stays in at most $9^{d}$ product boxes. Every cell that the piece visits
lies in one of them, so the piece visits fewer than $9^{d}\Lambda_{0}$ cells of $\mathcal{C}_{b}\text{,}$
and the route visits fewer than $9^{d}\Lambda_{0}\bigl(1+L(b/n)^{1/D}\bigr)\text{.}$ Since
$\Lambda_{0}=O_{d,\alpha}(\log n)\text{,}$ this is the bound of $E_{b}$ for a suitable constant $c$
depending only on $d$ and $\alpha\text{.}$
∎</p>
</div>
</div>
<div id="S3.p10" class="ltx_para">
<p class="ltx_p">The logarithm in <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> comes from the largest load over all product boxes. The
expected load of a fixed product box is at most $4^{d}\text{,}$ since at most $4^{d}n/b$ cells lie in it,
each co-blocked with probability at most $b/n\text{.}$</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-lower-bound-1">
<span class="ltx_tag ltx_tag_section">4 </span>The Lower Bound</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">This section proves the lower-bound half of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Movement Exponent). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>.</p>
</div>
<div id="S4.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 4.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Lower Bound)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every fixed $d\geq 1$ and $r\geq 1\text{,}$ $M_{r}^{(d)}(n)=\Omega_{d,r}\bigl(n^{\beta_{r}^{(d)}}/\log n\bigr)\text{.}$</span></p>
</div>
</div>
<div id="S4.p2" class="ltx_para">
<p class="ltx_p">The proof has the same plan for every finite $r\geq 2\text{.}$ Correctness forces the final round to visit every cell that is
co-blocked at the finest scale and whose positions the earlier rounds have not compared inside their block
(<a href="#S4.SS1" title="4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>). Unless an earlier round already has movement about $n^{\beta_{r}^{(d)}}\text{,}$ up to a logarithmic factor, many such cells
remain and lie far apart, so the final round has this movement. For $r\leq 2$ this argument is short and loses no
logarithmic factor. <a href="#S4.SS2" title="4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> gives it, together with the bound $\Omega_{d}(n^{1+1/(2d)})$ for every $r\text{,}$
including $r=\infty\text{.}$ For $r\geq 3$ the middle rounds are adaptive, and <a href="#S4.SS3" title="4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> controls what they can
learn. <a href="#S4.SS4" title="4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.4</span></a> removes the logarithmic factor on the line.</p>
</div>
<div id="S4.p3" class="ltx_para">
<p class="ltx_p">The lower bounds are proved on the uniform input. Fixing the coins of an $r$-round algorithm that is
correct on every input and for every outcome of its coins gives a deterministic $r$-round algorithm
that is correct on every input. Hence, by Yao’s principle <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib41" title="Probabilistic computations: toward a unified measure of complexity" class="ltx_ref">Yao77</a>]</cite>, a lower bound on the
expected movement on the uniform input that holds for every deterministic $r$-round algorithm
correct on every input is a lower bound on $M_{r}^{(d)}(n)\text{.}$ The lemmas of <a href="#S4.SS1" title="4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>
hold for every input, and the uniform input enters only when we count.</p>
</div>
<section id="S4.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-augmented-model-and-forced-comparisons">
<span class="ltx_tag ltx_tag_subsection">4.1 </span>The Augmented Model and Forced Comparisons</h3>

<div id="S4.SS1.p1" class="ltx_para">
<p class="ltx_p">For finite $r\geq 2\text{,}$ let $\beta=\beta_{r}^{(d)}\text{.}$ Recall from <a href="#S2.SS2" title="2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> that in this
section $b_{j}$ is the largest power of two not exceeding $n^{a_{j}}\text{,}$ where $a_{0}&gt;\dots&gt;a_{r-2}$
are the exponents of <a href="#S2.Thmtheorem5" title="Lemma 2.5. ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>, and that $g=b_{r-2}\text{.}$ Thus
$n^{a_{j}}/2&lt;b_{j}\leq n^{a_{j}}\text{.}$ The scales $b_{j}$ are powers of two, so every scale-$b_{j}$ block
lies in a scale-$b_{i}$ block for $i&lt;j\text{.}$ Since $a_{r-2}&gt;0$ and $a_{j-1}&gt;a_{j}\text{,}$ for $n$ larger than a
constant depending on $d$ and $r$ we have $g\geq 2$ and $b_{j-1}\geq 2b_{j}$ for $1\leq j\leq r-2\text{,}$ and we
assume this throughout the section.</p>
</div>
<div id="S4.SS1.p2" class="ltx_para">
<p class="ltx_p">A scale-$b$ block is <em class="ltx_emph ltx_font_italic">full</em> if it holds $b$ ranks. Otherwise it is <em class="ltx_emph ltx_font_italic">partial</em>. Every
$b_{j}$ divides $b_{0}\text{,}$ so the positions whose rank lies in a partial block of some scale $b_{j}$
are exactly those of rank greater than $b_{0}\lfloor n/b_{0}\rfloor\text{,}$ and there are fewer than
$b_{0}$ of them. The proofs below set these positions aside, because their counts need blocks of exactly $b$ ranks.</p>
</div>
<div id="S4.SS1.p3" class="ltx_para">
<p class="ltx_p">From round $2$ on, a route can use earlier outcomes to choose cells that are likely to be co-blocked, so the
probability $b/n$ no longer applies to the cells it visits. We therefore give the algorithm more information, which can
only help it, in a form that leaves, inside most blocks, the ranks of the positions not yet compared in the block
uniformly random (<a href="#S4.Thmtheorem8" title="Lemma 4.8. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.8</span></a>). In the <em class="ltx_emph ltx_font_italic">augmented model</em>, after round $j\text{,}$ for $1\leq j\leq r-2\text{,}$ the label of the
scale-$b_{j-1}$ block of every position is revealed at no cost, and the route of each later round
may depend on the revealed labels. Thus the route of round $1$ depends on no outcome and no label,
and for $j\geq 1$ the route of round $j+1$ may depend on the outcomes of rounds $1,\dots,j$ and on the
labels revealed after them. The <em class="ltx_emph ltx_font_italic">revealed scales</em> are $b_{0},\dots,b_{r-3}\text{,}$ and the labels at the
finest scale $g$ are never revealed. An algorithm of the original model is an algorithm of the
augmented model that ignores the labels, so a lower bound in the augmented model is a lower bound in
the original one. Once the labels at a scale are revealed, a comparison of two positions in
different blocks of that scale has a known outcome, so all further information about the ranks comes
from comparisons inside these blocks.</p>
</div>
<div id="S4.SS1.p4" class="ltx_para">
<p class="ltx_p">We now show which comparisons correctness forces. Let $P_{t}$ be the partial order on positions generated by the relations $x&lt;y\text{,}$ where $\{x,y\}$
ranges over the cells compared in rounds $1,\dots,t$ and $\operatorname{rk}(x)&lt;\operatorname{rk}(y)\text{.}$ Revealed labels separate
only positions in different blocks, so they do not help to order two positions that have the same
labels:</p>
</div>
<div id="S4.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let a deterministic $r$-round algorithm in the augmented model be correct on every input, and fix an
input. If two positions $u$ and $v$ are incomparable in $P_{r-1}$ and have the same label at every
revealed scale, then the route of round $r$ visits the cell $\{u,v\}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS1.p5" class="ltx_para">
<p class="ltx_p">We construct two inputs that agree with the given input on all revealed labels and on all outcomes
of rounds $1,\dots,r-1\text{,}$ but order $u$ and $v$ oppositely. Correctness then forces round $r$ to
compare $u$ and $v\text{.}$</p>
</div>
<div id="S4.SS1.p6" class="ltx_para">
<p class="ltx_p">If $r\leq 2\text{,}$ nothing is revealed, and we let $\lambda(x)=1$ for every position $x\text{.}$ If $r\geq 3\text{,}$ let
$\lambda(x)$ be the label of $x$ at the finest revealed scale $b_{r-3}\text{.}$ The revealed partitions
nest, so $\lambda(x)$ determines the labels of $x$ at all revealed scales. In both cases
$\lambda(u)=\lambda(v)\text{.}$ Let $P^{\prime}$ be the partial order generated by $P_{r-1}$ and the relations $x&lt;y$
for all positions $x,y$ with $\lambda(x)&lt;\lambda(y)\text{.}$ The given input extends $P^{\prime}\text{,}$ because blocks are intervals of ranks ordered
by their labels.</p>
</div>
<div id="S4.SS1.p7" class="ltx_para">
<p class="ltx_p">The positions $u$ and $v$ are incomparable in $P^{\prime}\text{.}$ Indeed, along a relation of $P_{r-1}$ the label
$\lambda$ does not decrease, because the two positions of a compared cell are ordered by rank and
every block is an interval of ranks. Along an added relation, $\lambda$ increases strictly. Hence
$\lambda$ does not decrease along a chain of $P^{\prime}$ from $u$ to $v\text{,}$ and since
$\lambda(u)=\lambda(v)\text{,}$ it is constant on the chain. So the chain uses no added relation and lies
in $P_{r-1}\text{,}$ which contradicts the incomparability of $u$ and $v$ in $P_{r-1}\text{.}$ The same argument
rules out a chain from $v$ to $u\text{.}$</p>
</div>
<div id="S4.SS1.p8" class="ltx_para">
<p class="ltx_p">We now build the two inputs. List first the positions that lie below $u$ or $v$ in $P^{\prime}\text{,}$ in an
order that extends $P^{\prime}\text{;}$ then $u$ and $v\text{,}$ in either order; then the remaining positions, in an
order that extends $P^{\prime}\text{.}$ No remaining position lies below a position of the first part, and since
$u$ and $v$ are incomparable in $P^{\prime}\text{,}$ neither of them lies below a position of the first part. So
both lists extend $P^{\prime}\text{.}$ Read as rank assignments, they are two inputs $\pi_{1}$ and $\pi_{2}$ that
differ by exchanging two adjacent ranks at $u$ and $v\text{.}$ For $r\geq 3\text{,}$ both have the given labels at
every revealed scale: in a linear extension of $P^{\prime}$ the positions with $\lambda=i$ receive
consecutive ranks, and there are as many of them as the block with label $i$ has ranks, so they
receive exactly those ranks.</p>
</div>
<div id="S4.SS1.p9" class="ltx_para">
<p class="ltx_p">Finally we compare the executions. Since $\pi_{1}$ and $\pi_{2}$ extend $P_{r-1}$ and have the given
labels, induction over the rounds shows that on both inputs the algorithm runs the same routes in
rounds $1,\dots,r-1$ as on the given input and receives the same outcomes, so it also runs the same
route in round $r\text{.}$ A comparison other than $\{u,v\}$ has the same outcome on $\pi_{1}$ and
$\pi_{2}\text{:}$ if it involves neither $u$ nor $v\text{,}$ its two ranks are unchanged, and if it involves $u$
or $v$ and a third position, the rank of the third position lies on the same side of the two
adjacent ranks. If the route of round $r$ did not visit $\{u,v\}\text{,}$ all outcomes on $\pi_{1}$ and
$\pi_{2}$ would agree, the algorithm would output the same list on both inputs, and it would be
wrong on one of them.
∎</p>
</div>
</div>
<div id="S4.SS1.p10" class="ltx_para">
<p class="ltx_p">Two positions of one block can be ordered only through a comparison inside the block:</p>
</div>
<div id="S4.Thmtheorem3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $P$ be the partial order generated, in the same way as $P_{t}\text{,}$ by the outcomes of a set of
comparisons. If $u&lt;_{P}v$ and $u$ and $v$ lie in a common scale-$b$ block, then one of these
comparisons involves $u$ and another position of this block.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS1.p11" class="ltx_para">
<p class="ltx_p">Write $u&lt;_{P}v$ as a chain $u=x_{0},x_{1},\dots,x_{i}=v$ in which every two consecutive positions
form a compared cell and have increasing ranks. The ranks along the chain lie between $\operatorname{rk}(u)$ and
$\operatorname{rk}(v)\text{,}$ hence in the block. So the first cell of the chain, $\{u,x_{1}\}\text{,}$ is a comparison of $u$
with another position of the block.
∎</p>
</div>
</div>
<div id="S4.SS1.p12" class="ltx_para">
<p class="ltx_p">Together, <a href="#S4.Thmtheorem2" title="Lemma 4.2. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemmas</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> and <a href="#S4.Thmtheorem3" title="Lemma 4.3. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.3</span></a> show that round $r$ must visit every cell co-blocked at scale
$g$ whose two positions have not been compared, in rounds $1,\dots,r-1\text{,}$ with other positions of
their scale-$g$ block. Indeed, by <a href="#S4.Thmtheorem3" title="Lemma 4.3. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> the two positions are incomparable in $P_{r-1}\text{,}$
and since every revealed scale is coarser than $g\text{,}$ they have the same revealed labels.</p>
</div>
</section>
<section id="S4.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="two-rounds-and-the-fully-adaptive-bound">
<span class="ltx_tag ltx_tag_subsection">4.2 </span>Two Rounds and the Fully Adaptive Bound</h3>

<div id="S4.SS2.p1" class="ltx_para">
<p class="ltx_p">The proof for $r=2$ has four stages, which the proof for $r\geq 3$ in <a href="#S4.SS3" title="4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> follows. The route of
round $1$ is fixed before any outcome is known, so there is no adaptivity to control, <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> is not needed,
and no logarithmic factor is lost.</p>
</div>
<div id="S4.Thmtheorem4" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Proposition 4.4</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every fixed $d$ and every $r\leq 2\text{,}$ $M_{r}^{(d)}(n)=\Omega_{d}\bigl(n^{\beta_{r}^{(d)}}\bigr)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS2.p2" class="ltx_para">
<p class="ltx_p">By Yao’s principle, fix a deterministic $r$-round algorithm that is correct on every input and let
$\pi$ be uniform. We show that $\mathbb{E}[\mathrm{Move}]=\Omega_{d}\bigl(n^{\beta_{r}^{(d)}}\bigr)\text{.}$</p>
</div>
<div id="S4.SS2.p3" class="ltx_para">
<p class="ltx_p">For $r=1\text{,}$ the order $P_{0}$ is empty and no label is revealed, so by <a href="#S4.Thmtheorem2" title="Lemma 4.2. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> the route
visits every cell. By <a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(a), $\mathrm{Move}\geq\binom{n}{2}-1=\Omega(n^{2})\text{,}$ and
$\beta_{1}^{(d)}=2\text{.}$</p>
</div>
<div id="S4.SS2.p4" class="ltx_para">
<p class="ltx_p">Now let $r=2\text{,}$ so that $g=b_{0}$ and, by <a href="#S2.E1" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, $\beta=2-a_{0}\text{.}$ Write $L_{1}$ and
$L_{2}$ for the movements of the two routes. No outcome is known before round $1\text{,}$ so the route of
round $1$ and $L_{1}$ do not depend on $\pi\text{.}$ Let $\varepsilon=1/192\text{.}$ If $L_{1}\geq\varepsilon n^{\beta}\text{,}$ then
$\mathrm{Move}\geq\varepsilon n^{\beta}$ and there is nothing to prove, so assume $L_{1}&lt;\varepsilon n^{\beta}\text{.}$
Call a position <em class="ltx_emph ltx_font_italic">clean</em> if its rank lies in a full scale-$g$ block and it lies in no cell that
round $1$ visits and that is co-blocked at scale $g\text{.}$</p>
</div>
<div id="S4.SS2.p5" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Exposure.</em> The route of round $1$ visits at most $L_{1}+1$ cells (<a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(a)), each
co-blocked at scale $g$ with probability at most $g/n\text{,}$ and fewer than $g$ positions lie in a partial
block. So the expected number of positions that are not clean is less than
$g+2(L_{1}+1)g/n\leq n^{a_{0}}+2\varepsilon n^{\beta+a_{0}-1}+2\text{.}$ Since $\beta+a_{0}-1=1\text{,}$ this is
$n/96+o(n)\text{,}$ which is at most $n/64$ for large $n\text{.}$</p>
</div>
<div id="S4.SS2.p6" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Survivors.</em> Every position lies in fewer than $g$ cells of $\mathcal{C}_{g}\text{,}$ so the expected
number of cells of $\mathcal{C}_{g}$ with a position that is not clean is at most
$gn/64\leq|\mathcal{C}_{g}|/8\text{.}$ By Markov’s inequality, with probability at least $1/2$ at most
$|\mathcal{C}_{g}|/4$ cells of $\mathcal{C}_{g}$ have such a position. By <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> at
scale $g\text{,}$ with probability at least $7/8$ at least half of the cells $w\in\mathcal{C}_{g}$ satisfy
$\operatorname{dist}(w,\mathcal{C}_{g}\setminus\{w\})&gt;\rho\text{,}$ where $\rho=\Theta_{d}\bigl((n/g)^{1/D}\bigr)\text{.}$ On the
intersection of the two events, which has probability at least $1-\tfrac{1}{2}-\tfrac{1}{8}=\tfrac{3}{8}\text{,}$ let
$\mathcal{H}$ be the set of cells of $\mathcal{C}_{g}$ that have two clean positions and satisfy this
condition. Then $|\mathcal{H}|\geq|\mathcal{C}_{g}|/4\geq ng/32\text{,}$ and any two cells of $\mathcal{H}$
are more than $\rho$ apart.</p>
</div>
<div id="S4.SS2.p7" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Forcing.</em> Let $\{u,v\}\in\mathcal{H}\text{.}$ Since $u$ and $v$ are clean, neither has been compared in
round $1$ with another position of its scale-$g$ block, so by <a href="#S4.Thmtheorem3" title="Lemma 4.3. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> they are
incomparable in $P_{1}\text{.}$ No label is revealed, so by <a href="#S4.Thmtheorem2" title="Lemma 4.2. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> the route of round $2$ visits
$\{u,v\}\text{.}$</p>
</div>
<div id="S4.SS2.p8" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Cost of the Final Round.</em> Since $|\mathcal{H}|\geq 2\text{,}$ <a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(b) and <a href="#S3.Thmtheorem2" title="Fact 3.2. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>
give</p>
<table id="S4.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$L_{2}\ \geq\ \tfrac{1}{2}|\mathcal{H}|\rho\ =\ \Omega_{d}\bigl(ng\,(n/g)^{1/D}\bigr)\ =\ \Omega_{d}\bigl(n^{1+a_{0}+(1-a_{0})/D}\bigr)\ =\ \Omega_{d}(n^{\beta}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where the second step uses $g&gt;n^{a_{0}}/2$ and the last is <a href="#S2.E3" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a> for $r=2\text{.}$ So, when
$L_{1}&lt;\varepsilon n^{\beta}\text{,}$ we have $L_{2}=\Omega_{d}(n^{\beta})$ on an event of probability at least $3/8\text{,}$ and hence
$\mathbb{E}[L_{2}]=\Omega_{d}(n^{\beta})\text{.}$ In both cases
$\mathbb{E}[\mathrm{Move}]=\Omega_{d}(n^{\beta})\text{.}$
∎</p>
</div>
</div>
<div id="S4.SS2.p9" class="ltx_para">
<p class="ltx_p">The next bound holds for every number of rounds and needs no schedule. It uses the cells of
$\mathcal{C}_{2}\text{,}$ which join the positions of ranks $2i-1$ and $2i\text{.}$</p>
</div>
<div id="S4.Thmtheorem5" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Proposition 4.5</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every fixed $d$ and every $r\text{,}$ including $r=\infty\text{,}$
$M_{r}^{(d)}(n)=\Omega_{d}\bigl(n^{1+1/(2d)}\bigr)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS2.p10" class="ltx_para">
<p class="ltx_p">Let $r$ be finite. By Yao’s principle, fix a deterministic $r$-round algorithm that is correct on
every input and let $\pi$ be uniform. Every cell $\{u,v\}\in\mathcal{C}_{2}$ joins the positions of ranks $2i-1$ and $2i$ for some $i\text{,}$ and every
correct algorithm must compare it. Indeed, if the algorithm never compares $u$ and $v\text{,}$ then
exchanging their two ranks changes the outcome of no comparison that it makes. So, by induction
over the rounds, it runs the same routes on both inputs and gives the same output, which is wrong on
one of them. By <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> at scale $2\text{,}$ with probability at least $7/8$ at least half of
the $\lfloor n/2\rfloor$ cells $w\in\mathcal{C}_{2}$ satisfy $\operatorname{dist}(w,\mathcal{C}_{2}\setminus\{w\})&gt;\rho\text{,}$
where $\rho=\Theta_{d}(n^{1/(2d)})\text{,}$ and these cells are pairwise more than $\rho$ apart. The routes of
all rounds, joined end to end, form one route of movement $\mathrm{Move}$ that visits all of them,
so by <a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(b) and <a href="#S3.Thmtheorem2" title="Fact 3.2. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>,
$\mathrm{Move}\geq\tfrac{1}{2}\cdot\tfrac{1}{2}\lfloor n/2\rfloor\cdot\rho=\Omega_{d}(n^{1+1/(2d)})$ on this
event. Hence $\mathbb{E}[\mathrm{Move}]=\Omega_{d}(n^{1+1/(2d)})\text{.}$ The constant depends only on $d\text{,}$
so the bound also holds for $M_{\infty}^{(d)}(n)=\inf_{r}M_{r}^{(d)}(n)\text{.}$
∎</p>
</div>
</div>
</section>
<section id="S4.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="adaptive-rounds">
<span class="ltx_tag ltx_tag_subsection">4.3 </span>Adaptive Rounds</h3>

<div id="S4.SS3.p1" class="ltx_para">
<p class="ltx_p">Throughout <a href="#S4.SS3" title="4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Sections</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> and <a href="#S4.SS4" title="4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.4</span></a>, let $r\geq 3\text{,}$ fix a deterministic
$r$-round algorithm in the augmented model that is correct on every input, let $\pi$ be uniform, and
write $L_{t}$ for the movement of its route in round $t\text{.}$ Since rounds $2,\dots,r-1$ are adaptive, we keep
track of what the first $r-1$ rounds can have learned. The bad set contains, scale by scale, the
positions that these rounds compare inside their blocks. It also contains all positions of
every block in which more than half of the positions are already bad, so that every other block keeps at
least half of its positions outside the bad set, which <a href="#S4.Thmtheorem8" title="Lemma 4.8. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.8</span></a> uses.</p>
</div>
<div id="S4.Thmtheorem6" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 4.6</span></span><span class="ltx_text ltx_font_bold"> </span>(The Bad Set)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p">The <em class="ltx_emph ltx_font_italic">bad set</em> is built in levels $j=0,1,\dots,r-2\text{,}$ and level $j$ concerns round $j+1\text{.}$ It starts from the set $\mathcal{A}_{-1}$ of positions whose rank lies in a partial block
of some scale $b_{i}\text{.}$ Level $j$ has two steps.</p>
<ol id="S4.I1" class="ltx_enumerate">
<li id="S4.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(a)</span> 
<div id="S4.I1.i1.p1" class="ltx_para">
<p class="ltx_p">For $j\geq 1\text{,}$ a scale-$b_{j-1}$ block is <em class="ltx_emph ltx_font_italic">heavy at level $j$</em> if more than half of its
positions lie in $\mathcal{A}_{j-1}\text{.}$ Let $\mathcal{A}_{j}^{-}$ consist of
$\mathcal{A}_{j-1}$ and all positions of the blocks that are heavy at level $j\text{.}$ Let
$\mathcal{A}_{0}^{-}=\mathcal{A}_{-1}\text{.}$</p>
</div>
</li>
<li id="S4.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(b)</span> 
<div id="S4.I1.i2.p1" class="ltx_para">
<p class="ltx_p">Let $X_{j}$ be the set of positions outside $\mathcal{A}_{j}^{-}$ that lie in a cell visited
in round $j+1$ and co-blocked at scale $b_{j}\text{,}$ and let
$\mathcal{A}_{j}=\mathcal{A}_{j}^{-}\cup X_{j}\text{.}$</p>
</div>
</li>
</ol>
<p class="ltx_p">The bad set is $\mathcal{A}=\mathcal{A}_{r-2}\text{.}$ A position is <em class="ltx_emph ltx_font_italic">bad</em> if it lies in
$\mathcal{A}\text{,}$ and <em class="ltx_emph ltx_font_italic">clean</em> otherwise. It is <em class="ltx_emph ltx_font_italic">clean at level $j$</em> if it lies outside
$\mathcal{A}_{j}^{-}\text{.}$</p>
</div>
</div>
<div id="S4.Thmtheorem7" class="ltx_theorem ltx_theorem_observation">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Observation 4.7</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem7.p1" class="ltx_para">
<ol id="S4.I2" class="ltx_enumerate">
<li id="S4.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(a)</span> 
<div id="S4.I2.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For </span>$1\leq j\leq r-2$<span class="ltx_text ltx_font_italic">, a position clean at level </span>$j$<span class="ltx_text ltx_font_italic"> lies in a full scale-</span>$b_{j-1}$<span class="ltx_text ltx_font_italic"> block that
is not heavy at level </span>$j$<span class="ltx_text ltx_font_italic">, and in rounds </span>$1,\dots,j$<span class="ltx_text ltx_font_italic"> it has not been compared with another
position of this block.</span></p>
</div>
</li>
<li id="S4.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(b)</span> 
<div id="S4.I2.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">A clean position has not been compared, in rounds </span>$1,\dots,r-1$<span class="ltx_text ltx_font_italic">, with another position of
its scale-</span>$g$<span class="ltx_text ltx_font_italic"> block.</span></p>
</div>
</li>
</ol>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p2" class="ltx_para">
<p class="ltx_p">For every $i\text{,}$ both positions of a cell that round $i+1$ visits and that is co-blocked at scale
$b_{i}$ lie in $\mathcal{A}_{i}\text{.}$ Let $x$ be clean at level $j\text{,}$ and suppose that in round
$i+1\leq j$ it was compared with another position $y$ of its scale-$b_{j-1}$ block. The cell
$\{x,y\}$ is co-blocked at scale $b_{j-1}\text{,}$ hence at the coarser scale $b_{i}\text{,}$ so
$x\in\mathcal{A}_{i}\subseteq\mathcal{A}_{j}^{-}\text{,}$ a contradiction. The block of $x$ is full because
$\mathcal{A}_{-1}\subseteq\mathcal{A}_{j}^{-}\text{,}$ and it is not heavy because otherwise
$x\in\mathcal{A}_{j}^{-}\text{.}$ This proves (a). For (b), let $x$ be clean, and suppose that in round
$i+1\leq r-1$ it was compared with another position $y$ of its scale-$g$ block. The cell $\{x,y\}$ is
co-blocked at scale $g\text{,}$ hence at scale $b_{i}\text{,}$ so $x\in\mathcal{A}_{i}\subseteq\mathcal{A}\text{,}$ a
contradiction.
∎</p>
</div>
</div>
<div id="S4.SS3.p3" class="ltx_para">
<p class="ltx_p">To keep the bad set small, we bound $\mathbb{E}|X_{j}|$ for $1\leq j\leq r-2$ by combining two facts. A position enters $X_{j}$
only if it is clean at level $j$ and lies in a cell that round $j+1$ visits and that is co-blocked
at scale $b_{j}\text{,}$ and hence also at scale $b_{j-1}\text{.}$ <a href="#S4.Thmtheorem8" title="Lemma 4.8. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.8</span></a> below shows that a cell
that is co-blocked at scale $b_{j-1}$ and contains a position clean at level $j$ is co-blocked at scale $b_{j}$
with conditional probability $O(b_{j}/b_{j-1})\text{,}$ given what the algorithm knows before round
$j+1\text{,}$ and <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> shows that a short route visits few cells co-blocked at scale
$b_{j-1}\text{.}$ <a href="#S4.Thmtheorem9" title="Lemma 4.9. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a> combines the two.</p>
</div>
<div id="S4.SS3.p4" class="ltx_para">
<p class="ltx_p">For $1\leq j\leq r-2\text{,}$ let $\mathcal{F}_{j}$ be the $\sigma$-field generated by the labels at scales
$b_{0},\dots,b_{j-1}$ and the outcomes of rounds $1,\dots,j\text{.}$ In words, $\mathcal{F}_{j}$ is what
the algorithm knows when it commits the route of round $j+1\text{.}$ An <em class="ltx_emph ltx_font_italic">atom</em> of $\mathcal{F}_{j}$ is
one possible value of these labels and outcomes. Given an atom, that route is fixed. The lemma below
conditions on the positions clean at level $j\text{,}$ so they must be determined by $\mathcal{F}_{j}\text{.}$ Indeed, by induction on $i\text{,}$ the sets $\mathcal{A}_{i-1}$ and
$\mathcal{A}_{i}^{-}$ are determined by $\mathcal{F}_{j}$ for every $i\leq j\text{.}$ The set
$\mathcal{A}_{-1}$ is determined by the labels at scale $b_{0}\text{.}$ Whether a block is heavy at level
$i$ depends only on $\mathcal{A}_{i-1}$ and the labels at scale $b_{i-1}\text{.}$ For $i&lt;j\text{,}$ the set
$X_{i}$ depends only on $\mathcal{A}_{i}^{-}\text{,}$ the route of round $i+1\text{,}$ and the labels at scale
$b_{i}\text{,}$ and the last two are determined by $\mathcal{F}_{i+1}\subseteq\mathcal{F}_{j}\text{.}$</p>
</div>
<div id="S4.Thmtheorem8" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.8</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem8.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $1\leq j\leq r-2\text{,}$ and let $\{u,v\}$ be a cell. On the event that
$\{u,v\}$ is co-blocked at scale $b_{j-1}$ and $u$ is clean at level $j\text{,}$</span></p>
<table id="S4.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Pr\bigl[\{u,v\}\text{ is co-blocked at scale }b_{j}\bigm|\mathcal{F}_{j}\bigr]\leq\frac{4b_{j}}{b_{j-1}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p5" class="ltx_para">
<p class="ltx_p">Fix an atom of $\mathcal{F}_{j}$ on which $\{u,v\}$ is co-blocked at scale $b_{j-1}$ and $u$ is
clean at level $j\text{,}$ and let $B$ be the scale-$b_{j-1}$ block of $u\text{.}$ By <a href="#S4.Thmtheorem7" title="Observation 4.7. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">4.7</span></a>(a), $B$ is
full and not heavy at level $j\text{.}$ Since $\mathcal{A}_{j}^{-}$ adds to $\mathcal{A}_{j-1}$ only
positions of heavy blocks, at most half of the $b_{j-1}$ positions of $B$ lie in
$\mathcal{A}_{j}^{-}\text{,}$ so the set $Y_{B}$ of positions of $B$ that are clean at level $j$ has at
least $b_{j-1}/2$ elements. Condition further on the ranks of all positions outside $Y_{B}\text{.}$ The
ranks of $B$ not assigned to these positions are the <em class="ltx_emph ltx_font_italic">free slots</em>. The positions of $Y_{B}$
occupy them.</p>
</div>
<div id="S4.SS3.p6" class="ltx_para">
<p class="ltx_p">We show that $\operatorname{rk}$ restricted to $Y_{B}$ is a uniformly random bijection onto the free slots. Since
$\pi$ is uniform, it suffices to show that permuting the ranks of $Y_{B}$ among the free slots does
not change the atom of $\mathcal{F}_{j}\text{.}$ Such a permutation keeps every rank inside $B\text{,}$ so it
changes no label at scales $b_{0},\dots,b_{j-1}\text{.}$ By <a href="#S4.Thmtheorem7" title="Observation 4.7. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">4.7</span></a>(a), every comparison of
rounds $1,\dots,j$ that involves a position of $Y_{B}$ has its other position outside $B\text{.}$ The rank
of that position lies above all ranks of $B$ or below all of them, so the outcome does not change.
The outcome of a comparison that involves no position of $Y_{B}$ does not change either. By induction
over the rounds, the routes and outcomes of rounds $1,\dots,j$ do not change, so the atom of
$\mathcal{F}_{j}$ does not change.</p>
</div>
<div id="S4.SS3.p7" class="ltx_para">
<p class="ltx_p">It remains to count. Since $\{u,v\}$ is co-blocked at scale $b_{j-1}\text{,}$ $v$ lies in $B\text{.}$ If
$v\notin Y_{B}\text{,}$ the rank of $v$ is fixed, and $\operatorname{rk}(u)$ is uniform over at least $b_{j-1}/2$ free
slots, of which at most $b_{j}$ lie in the scale-$b_{j}$ block of $\operatorname{rk}(v)\text{,}$ so the probability is at
most $2b_{j}/b_{j-1}\text{.}$ If $v\in Y_{B}\text{,}$ condition also on $\operatorname{rk}(v)\text{.}$ Then $\operatorname{rk}(u)$ is uniform over the
remaining at least $b_{j-1}/2-1$ free slots, of which at most $b_{j}$ lie in the scale-$b_{j}$ block
of $\operatorname{rk}(v)\text{,}$ so the probability is at most $b_{j}/(b_{j-1}/2-1)\leq 4b_{j}/b_{j-1}\text{,}$ because
$b_{j-1}\geq 2b_{j}\geq 4\text{.}$ These bounds hold for every value of the further conditioning and every
such atom of $\mathcal{F}_{j}\text{,}$ which proves the lemma.
∎</p>
</div>
</div>
<div id="S4.Thmtheorem9" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.9</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem9.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">We have $\mathbb{E}|X_{0}|\leq 2(L_{1}+1)\,b_{0}/n\text{,}$ and for every
$1\leq j\leq r-2\text{,}$</span></p>
<table id="S4.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}|X_{j}|=O_{d,r}\Bigl(\frac{b_{j}}{b_{j-1}}\Bigl(1+\mathbb{E}[L_{j+1}]\Bigl(\frac{b_{j-1}}{n}\Bigr)^{1/D}\Bigr)\log n\Bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p8" class="ltx_para">
<p class="ltx_p">No outcome and no label is known before round $1\text{,}$ so its route and $L_{1}$ do not depend on $\pi\text{,}$
and by <a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(a) the route visits at most $L_{1}+1$ cells. Each of them is co-blocked at scale
$b_{0}$ with probability at most $b_{0}/n$ and contributes at most two positions to $X_{0}\text{,}$ which
gives the bound on $\mathbb{E}|X_{0}|\text{.}$</p>
</div>
<div id="S4.SS3.p9" class="ltx_para">
<p class="ltx_p">Now let $1\leq j\leq r-2\text{,}$ and fix an atom of $\mathcal{F}_{j}\text{.}$ The route of round $j+1$ is then
fixed, and so is the set $K_{j}$ of the cells that it visits, that are co-blocked at scale
$b_{j-1}\text{,}$ and that contain a position clean at level $j\text{.}$ Every position of $X_{j}$ is clean at
level $j$ and lies in a cell visited in round $j+1$ and co-blocked at scale $b_{j}\text{,}$ hence also at
scale $b_{j-1}\text{,}$ so it lies in a cell of $K_{j}$ that is co-blocked at scale $b_{j}\text{.}$ Applying
<a href="#S4.Thmtheorem8" title="Lemma 4.8. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.8</span></a> to each cell of $K_{j}\text{,}$ with $u$ a position clean at level $j\text{,}$ gives</p>
<table id="S4.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl[|X_{j}|\bigm|\mathcal{F}_{j}\bigr]\leq 2\cdot|K_{j}|\cdot\frac{4b_{j}}{b_{j-1}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">We bound $|K_{j}|$ by <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> with $\alpha=a_{0}\text{,}$ which applies at scale $b_{j-1}$
because $a_{0}&lt;1$ and $b_{j-1}\leq b_{0}\leq n^{a_{0}}\text{.}$ Its constant $c$ then depends only on $d$
and $r\text{.}$ The event $E_{b_{j-1}}$ depends only on $\mathcal{C}_{b_{j-1}}\text{,}$ which the labels at scale
$b_{j-1}$ determine, so it is determined by $\mathcal{F}_{j}\text{.}$ On $E_{b_{j-1}}$ we have
$|K_{j}|\leq c\bigl(1+L_{j+1}(b_{j-1}/n)^{1/D}\bigr)\log n\text{,}$ so taking expectations gives</p>
<table id="S4.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl[|X_{j}|\,\mathbf{1}_{E_{b_{j-1}}}\bigr]\leq\frac{8c\,b_{j}}{b_{j-1}}\Bigl(1+\mathbb{E}[L_{j+1}]\Bigl(\frac{b_{j-1}}{n}\Bigr)^{1/D}\Bigr)\log n.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Off $E_{b_{j-1}}$ we use $|X_{j}|\leq n\text{.}$ The complement of $E_{b_{j-1}}$ has probability at most
$n^{-10}$ for large $n\text{,}$ so it contributes at most $n^{-9}\text{,}$ which is at most $b_{j}/b_{j-1}$ because
$b_{j}\geq 1$ and $b_{j-1}\leq n\text{.}$ Adding the two parts proves the bound on $\mathbb{E}|X_{j}|\text{.}$
∎</p>
</div>
</div>
<div id="S4.SS3.p10" class="ltx_para">
<p class="ltx_p">The first stage of the proof of <a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a> uses <a href="#S4.Thmtheorem9" title="Lemma 4.9. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a> together with the following observation.</p>
</div>
<div id="S4.Thmtheorem10" class="ltx_theorem ltx_theorem_observation">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Observation 4.10</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem10.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For $0\leq j\leq r-2\text{,}$ $|\mathcal{A}_{j}|\leq 3|\mathcal{A}_{j-1}|+|X_{j}|\text{.}$ Consequently
$\mathbb{E}|\mathcal{A}|\leq 3^{r-1}\bigl(|\mathcal{A}_{-1}|+\max_{0\leq j\leq r-2}\mathbb{E}|X_{j}|\bigr)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p11" class="ltx_para">
<p class="ltx_p">At level $j\geq 1\text{,}$ a full heavy block holds more than $b_{j-1}/2$ positions of $\mathcal{A}_{j-1}\text{,}$
so at most $2|\mathcal{A}_{j-1}|/b_{j-1}$ full blocks are heavy, and together they hold at most
$2|\mathcal{A}_{j-1}|$ positions. The positions of a partial block lie in
$\mathcal{A}_{-1}\subseteq\mathcal{A}_{j-1}$ already. Hence $|\mathcal{A}_{j}^{-}|\leq 3|\mathcal{A}_{j-1}|\text{,}$ also for $j=0\text{,}$ and the first claim follows from
$\mathcal{A}_{j}=\mathcal{A}_{j}^{-}\cup X_{j}\text{.}$ Iterating it over the $r-1$ levels gives
$|\mathcal{A}|\leq 3^{r-1}|\mathcal{A}_{-1}|+\sum_{j=0}^{r-2}3^{r-2-j}|X_{j}|\text{,}$ and the second claim
follows by taking expectations, because $\sum_{j=0}^{r-2}3^{r-2-j}&lt;3^{r-1}\text{.}$
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>.</h6>
<div id="S4.SS3.p12" class="ltx_para">
<p class="ltx_p">For $r\leq 2$ the theorem is <a href="#S4.Thmtheorem4" title="Proposition 4.4. ‣ 4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">4.4</span></a>, so let $r\geq 3\text{.}$ By Yao’s principle, and because
an algorithm of the original model is an algorithm of the augmented model that ignores the labels,
it suffices to show that the algorithm fixed in <a href="#S4.SS3" title="4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> has
$\mathbb{E}[\mathrm{Move}]=\Omega_{d,r}(n^{\beta}/\log n)\text{.}$ The proof has the four stages of the
proof of <a href="#S4.Thmtheorem4" title="Proposition 4.4. ‣ 4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">4.4</span></a>. The new difficulty is that rounds $2,\dots,r-1$ are adaptive. We
first show that the bad set is small, then find many cells of $\mathcal{C}_{g}$ with clean positions
that are pairwise far apart, show that round $r$ visits all of them, and bound the movement of a
route that does so.</p>
</div>
<div id="S4.SS3.p13" class="ltx_para">
<p class="ltx_p">Recall that $L_{t}$ is the movement of the route of round $t\text{,}$ so that
$\mathrm{Move}=L_{1}+\dots+L_{r}\text{.}$ Let $T=\varepsilon n^{\beta}/\log n\text{,}$ where $\varepsilon&gt;0$ depends only on
$d$ and $r$ and is chosen below. If $\mathbb{E}[L_{t}]\geq T/100$ for
some $t\leq r-1\text{,}$ then $\mathbb{E}[\mathrm{Move}]\geq T/100\text{,}$ and we call this Case 1. Otherwise
$\mathbb{E}[L_{t}]&lt;T/100$ for every $t\leq r-1\text{.}$ This is Case 2, which we assume until the last
paragraph.</p>
</div>
<div id="S4.SS3.p14" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Exposure.</em> We show that $\mathbb{E}|\mathcal{A}|\leq n/64$ for large $n\text{.}$ By
<a href="#S4.Thmtheorem9" title="Lemma 4.9. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a> and Case 2, $\mathbb{E}|X_{0}|\leq 2(T/100+1)b_{0}/n\text{.}$ Since
$b_{0}\leq n^{a_{0}}$ and, by <a href="#S2.E1" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, $\beta+a_{0}-1=1\text{,}$ this gives
$\mathbb{E}|X_{0}|\leq\varepsilon n/50+2\text{.}$ For $1\leq j\leq r-2\text{,}$ let $C$ be the constant of <a href="#S4.Thmtheorem9" title="Lemma 4.9. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a>,
which depends only on $d$ and $r\text{.}$ With Case 2 and $T\log n=\varepsilon n^{\beta}\text{,}$ that lemma gives
$\mathbb{E}|X_{j}|\leq C\log n+C\varepsilon\,(b_{j}/b_{j-1})\,n^{\beta}(b_{j-1}/n)^{1/D}\text{.}$
Since $b_{j}\leq n^{a_{j}}\text{,}$ $b_{j-1}&gt;n^{a_{j-1}}/2\text{,}$ and $1-1/D&gt;0\text{,}$</p>
<table id="S4.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{b_{j}}{b_{j-1}}\,n^{\beta}\Bigl(\frac{b_{j-1}}{n}\Bigr)^{1/D}=n^{\beta-1/D}\,b_{j}\,b_{j-1}^{-(1-1/D)}\leq 2\,n^{\beta+a_{j}-a_{j-1}+(a_{j-1}-1)/D}=2n,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where the last step is <a href="#S2.E2" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>. Hence $\mathbb{E}|X_{j}|\leq C\log n+2C\varepsilon n\text{.}$ By
<a href="#S4.Thmtheorem10" title="Observation 4.10. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">4.10</span></a> and $|\mathcal{A}_{-1}|&lt;b_{0}\leq n^{a_{0}}\text{,}$
$\mathbb{E}|\mathcal{A}|\leq 3^{r-1}\bigl(n^{a_{0}}+(2C+1/50)\,\varepsilon n+C\log n+2\bigr)\text{.}$ Choose $\varepsilon$ with
$3^{r-1}(2C+1/50)\,\varepsilon\leq 1/128\text{.}$ Then $\mathbb{E}|\mathcal{A}|\leq n/64$ for large $n\text{,}$ since $a_{0}&lt;1\text{.}$</p>
</div>
<div id="S4.SS3.p15" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Survivors.</em> Every position lies in fewer than $g$ cells of $\mathcal{C}_{g}\text{,}$ so at most
$g|\mathcal{A}|$ cells of $\mathcal{C}_{g}$ have a bad position. Since
$\mathbb{E}[g|\mathcal{A}|]\leq ng/64\leq|\mathcal{C}_{g}|/8\text{,}$ Markov’s inequality applied to the
number of these cells shows that, with probability at least $1/2\text{,}$ at most $|\mathcal{C}_{g}|/4$
cells of $\mathcal{C}_{g}$ have a bad position. By <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> at scale $g\text{,}$ with probability
at least $7/8$ at least half of the cells $w\in\mathcal{C}_{g}$ satisfy
$\operatorname{dist}(w,\mathcal{C}_{g}\setminus\{w\})&gt;\rho\text{,}$ where $\rho=\Theta_{d}\bigl((n/g)^{1/D}\bigr)\text{.}$ On the
intersection of the two events, which has probability at least $1-\tfrac{1}{2}-\tfrac{1}{8}=\tfrac{3}{8}\text{,}$ let
$\mathcal{H}$ be the set of cells of $\mathcal{C}_{g}$ that have two clean positions and satisfy this
condition. Then $|\mathcal{H}|\geq|\mathcal{C}_{g}|/4\geq ng/32\text{,}$ and any two cells of $\mathcal{H}$
are more than $\rho$ apart.</p>
</div>
<div id="S4.SS3.p16" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Forcing.</em> Let $\{u,v\}\in\mathcal{H}\text{.}$ Both $u$ and $v$ are clean, so by <a href="#S4.Thmtheorem7" title="Observation 4.7. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">4.7</span></a>(b)
neither has been compared, in rounds $1,\dots,r-1\text{,}$ with another position of its scale-$g$ block.
By <a href="#S4.Thmtheorem3" title="Lemma 4.3. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a>, applied to $P_{r-1}\text{,}$ the positions $u$ and $v$ are incomparable in $P_{r-1}\text{.}$
The revealed scales $b_{0},\dots,b_{r-3}$ are coarser than $g\text{,}$ and $u$ and $v$ are co-blocked at
scale $g\text{,}$ so they have the same label at every revealed scale. By <a href="#S4.Thmtheorem2" title="Lemma 4.2. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>, the route of
round $r$ visits $\{u,v\}\text{.}$</p>
</div>
<div id="S4.SS3.p17" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Cost of the Final Round.</em> By the previous stage, the route of round $r$ visits every cell of
$\mathcal{H}\text{.}$ Since $|\mathcal{H}|\geq 2$ and the cells of $\mathcal{H}$ are pairwise more than
$\rho$ apart, <a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(b) and <a href="#S3.Thmtheorem2" title="Fact 3.2. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">3.2</span></a> give</p>
<table id="S4.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$L_{r}\ \geq\ \tfrac{1}{2}|\mathcal{H}|\rho\ =\ \Omega_{d}\bigl(ng\,(n/g)^{1/D}\bigr)\ =\ \Omega_{d}\bigl(n^{1+a_{r-2}+(1-a_{r-2})/D}\bigr)\ =\ \Omega_{d}(n^{\beta}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where the second step uses $g&gt;n^{a_{r-2}}/2$ and the last is <a href="#S2.E3" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>. So
$L_{r}=\Omega_{d}(n^{\beta})$ on an event of probability at least $3/8\text{.}$</p>
</div>
<div id="S4.SS3.p18" class="ltx_para">
<p class="ltx_p">In Case 2 this gives $\mathbb{E}[L_{r}]=\Omega_{d}(n^{\beta})\text{,}$ and in Case 1 we have
$\mathbb{E}[\mathrm{Move}]\geq T/100=\varepsilon n^{\beta}/(100\log n)\text{.}$ In both cases
$\mathbb{E}[\mathrm{Move}]=\Omega_{d,r}(n^{\beta}/\log n)\text{,}$ which proves <a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>.
∎</p>
</div>
</div>
<div id="S4.Thmtheorem11" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 4.11</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S4.Thmtheorem11.p1" class="ltx_para">
<p class="ltx_p"><a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a> holds with free computation and memory: comparisons are the algorithm’s only access to
the order. After Yao’s principle fixes
a deterministic algorithm, the proof of <a href="#S4.Thmtheorem2" title="Lemma 4.2. ‣ 4.1 The Augmented Model and Forced Comparisons ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> gives, for every pair of positions with
the same revealed labels that the first $r-1$ rounds leave incomparable, two inputs that agree on all
revealed labels and on all outcomes of these rounds but order the pair oppositely. Hence no computation on these outcomes orders the pair, and
the comparisons of the final round, with their movement, are required of every correct algorithm.</p>
</div>
</div>
</section>
<section id="S4.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="exact-order-on-the-line">
<span class="ltx_tag ltx_tag_subsection">4.4 </span>Exact Order on the Line</h3>

<div id="S4.SS4.p1" class="ltx_para">
<p class="ltx_p">The logarithmic factor in <a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a> comes from <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> alone, and on the line we remove it. In this
subsection $d=1\text{,}$ and we write $\beta_{r}=\beta_{r}^{(1)}\text{.}$</p>
</div>
<div id="S4.Thmtheorem12" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 4.12</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem12.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For $d=1$ and every fixed $r\geq 1\text{,}$ $M_{r}^{(1)}(n)=\Omega_{r}\bigl(n^{\beta_{r}}\bigr)\text{.}$</span></p>
</div>
</div>
<div id="S4.SS4.p2" class="ltx_para">
<p class="ltx_p">Together with <a href="#S5.Thmtheorem11" title="Theorem 5.11. ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">5.11</span></a>, it gives $M_{r}^{(1)}(n)=\Theta_{r}\bigl(n^{\beta_{r}}\bigr)\text{.}$</p>
</div>
<div id="S4.SS4.p3" class="ltx_para">
<p class="ltx_p">The logarithm in <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> comes from a product box that holds about $\log n$ cells, and such crowded
places are rare. So we group nearby cells into clusters. Small clusters are far apart for their size, so a route must
move to visit their cells, and large clusters almost never occur. The bound that replaces <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> has an
additive term $\Xi_{b}\text{,}$ which counts the cells of large clusters and which we define first.</p>
</div>
<div id="S4.SS4.p4" class="ltx_para">
<p class="ltx_p">Fix a dyadic scale $b\leq\sqrt{n}\text{,}$ and identify each cell with its fold, a point of
$\{(x,y):x&lt;y\}\text{.}$ By <a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(b), the distance $\operatorname{dist}$ between two cells is the $\ell_{1}$ distance between their folds. Let $H=\lceil\sqrt{n/b}\rceil\text{,}$
let $\varepsilon_{\star}&gt;0$ and $n_{0}$ be absolute constants chosen in the proof of <a href="#S4.Thmtheorem14" title="Lemma 4.14. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.14</span></a>,
and put</p>
<table id="S4.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\rho_{t}=\varepsilon_{\star}H\,4^{t}\quad(0\leq t\leq t_{\star}),\qquad t_{\star}=\lceil\log\log n\rceil,\qquad\kappa=2^{t_{\star}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">cluster</em> is a set of cells of $\mathcal{C}_{b}\text{.}$ Clusters are formed in phases
$t=0,1,\dots,t_{\star}\text{,}$ and the clusters of phase $0$ are the single cells of $\mathcal{C}_{b}\text{.}$
Two clusters of phase $t$ are <em class="ltx_emph ltx_font_italic">close</em> if some cell of one lies within distance $\rho_{t}$ of
some cell of the other. Phase $t$ merges each connected component of the closeness relation that
contains two or more clusters into one cluster of phase $t+1\text{.}$ A cluster of phase $t$ that is close
to no other cluster is <em class="ltx_emph ltx_font_italic">isolated</em>. An isolated cluster <em class="ltx_emph ltx_font_italic">retires</em> if it has at most
$2^{t+1}$ cells. Otherwise it is also a cluster of phase $t+1\text{.}$ The <em class="ltx_emph ltx_font_italic">residual clusters</em> are the
clusters of phase $t_{\star}+1\text{.}$ For $n\geq n_{0}\text{,}$ let $\Xi_{b}$ be the total number of cells in residual
clusters, and for $n&lt;n_{0}\text{,}$ let $\Xi_{b}=0\text{.}$</p>
</div>
<div id="S4.SS4.p5" class="ltx_para">
<p class="ltx_p">By induction on $t\text{,}$ every cluster of phase $t$ has at least $2^{t}$ cells: a merged component
consists of at least two clusters with at least $2^{t}$ cells each, and an isolated cluster that
does not retire has more than $2^{t+1}$ cells. In particular every residual cluster has at least
$2\kappa$ cells, and every cell of $\mathcal{C}_{b}$ ends in exactly one retired or residual cluster.</p>
</div>
<div id="S4.SS4.p6" class="ltx_para">
<p class="ltx_p">From one phase to the next, the distance $\rho_{t}$ grows by a factor of $4\text{,}$ while the largest size
of a retiring cluster only doubles. So the clusters that retire in a phase are far apart for their
size.</p>
</div>
<div id="S4.Thmtheorem13" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.13</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem13.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $d=1\text{.}$ There are absolute constants $C$ and $C^{\prime}$ such that, for every input and every dyadic
scale $b\leq\sqrt{n}\text{,}$ every route of movement $L$ visits at most $C\,L\sqrt{b/n}+\Xi_{b}+C^{\prime}\log n$
cells of $\mathcal{C}_{b}\text{.}$</span></p>
</div>
</div>
<div id="S4.SS4.p7" class="ltx_para">
<p class="ltx_p"><a href="#S4.Thmtheorem13" title="Lemma 4.13. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.13</span></a> is the analog of <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> on the line, and the next lemma shows
that its additive term $\Xi_{b}$ is at most $1$ in expectation.</p>
</div>
<div id="S4.Thmtheorem14" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.14</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem14.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $d=1\text{.}$ For a suitable choice of the absolute constants $\varepsilon_{\star}&gt;0$ and $n_{0}\text{,}$
$\mathbb{E}[\Xi_{b}]\leq 1$ over the uniform input, for every dyadic scale $b\leq\sqrt{n}\text{.}$</span></p>
</div>
</div>
<div id="S4.SS4.p8" class="ltx_para">
<p class="ltx_p">With these two lemmas, <a href="#S4.Thmtheorem9" title="Lemma 4.9. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a> has the following analog on the line.</p>
</div>
<div id="S4.Thmtheorem15" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.15</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem15.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">We have $\mathbb{E}|X_{0}|\leq 2(L_{1}+1)\,b_{0}/n\text{,}$ and for every
$1\leq j\leq r-2\text{,}$</span></p>
<table id="S4.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}|X_{j}|\leq\frac{8b_{j}}{b_{j-1}}\Bigl(C\,\mathbb{E}[L_{j+1}]\Bigl(\frac{b_{j-1}}{n}\Bigr)^{1/2}+C^{\prime}\log n+1\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p"><span class="ltx_text ltx_font_italic">where $C$ and $C^{\prime}$ are the constants of <a href="#S4.Thmtheorem13" title="Lemma 4.13. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.13</span></a>.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS4.p9" class="ltx_para">
<p class="ltx_p">The bound on $\mathbb{E}|X_{0}|$ is that of <a href="#S4.Thmtheorem9" title="Lemma 4.9. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a>. Let $1\leq j\leq r-2\text{.}$ At $q=1/2$ we
have $\delta=1/\bigl(2(1-2^{-r})\bigr)&gt;1/2\text{,}$ so $a_{0}=1-\delta&lt;1/2$ and
$b_{j-1}\leq b_{0}&lt;\sqrt{n}\text{,}$ so <a href="#S4.Thmtheorem13" title="Lemma 4.13. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.13</span></a> applies at scale $b_{j-1}\text{.}$ We follow
the proof of <a href="#S4.Thmtheorem9" title="Lemma 4.9. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a> with <a href="#S4.Thmtheorem13" title="Lemma 4.13. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.13</span></a> in place of <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a>. As
there, $\mathbb{E}\bigl[|X_{j}|\bigm|\mathcal{F}_{j}\bigr]\leq(8b_{j}/b_{j-1})|K_{j}|\text{.}$ By
<a href="#S4.Thmtheorem13" title="Lemma 4.13. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.13</span></a>, $|K_{j}|\leq C\,L_{j+1}(b_{j-1}/n)^{1/2}+\Xi_{b_{j-1}}+C^{\prime}\log n$ on every
input. Taking expectations and using $\mathbb{E}[\Xi_{b_{j-1}}]\leq 1$ (<a href="#S4.Thmtheorem14" title="Lemma 4.14. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.14</span></a>) gives the
bound.
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S4.Thmtheorem12" title="Theorem 4.12. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.12</span></a>.</h6>
<div id="S4.SS4.p10" class="ltx_para">
<p class="ltx_p">For $r\leq 2$ the theorem is <a href="#S4.Thmtheorem4" title="Proposition 4.4. ‣ 4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">4.4</span></a>, so let $r\geq 3\text{.}$ As in the proof of
<a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>, it suffices to show that the algorithm fixed in <a href="#S4.SS3" title="4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> has
$\mathbb{E}[\mathrm{Move}]=\Omega_{r}(n^{\beta_{r}})\text{.}$ We follow the proof of <a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a> with three
changes.</p>
</div>
<div id="S4.SS4.p11" class="ltx_para">
<p class="ltx_p">First, $T=\varepsilon_{r}n^{\beta_{r}}\text{,}$ where $\varepsilon_{r}&gt;0$ depends only on $r$ and is chosen below.
Cases 1 and 2 are defined with this $T\text{.}$</p>
</div>
<div id="S4.SS4.p12" class="ltx_para">
<p class="ltx_p">Second, the first stage uses <a href="#S4.Thmtheorem15" title="Lemma 4.15. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.15</span></a> in place of <a href="#S4.Thmtheorem9" title="Lemma 4.9. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a>. In Case 2 it
gives $\mathbb{E}|X_{0}|\leq 2(T/100+1)b_{0}/n\leq\varepsilon_{r}n/50+2\text{,}$ as in the proof of <a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>,
and, for $1\leq j\leq r-2\text{,}$</p>
<table id="S4.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}|X_{j}|\leq\frac{8b_{j}}{b_{j-1}}\Bigl(\frac{C\,T}{100}\Bigl(\frac{b_{j-1}}{n}\Bigr)^{1/2}+C^{\prime}\log n+1\Bigr)\leq\frac{C}{4}\,\varepsilon_{r}n+8C^{\prime}\log n+8,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">because $(b_{j}/b_{j-1})\,n^{\beta_{r}}(b_{j-1}/n)^{1/2}\leq 2n$ by the computation in the proof of
<a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a> with $D=2\text{.}$ By <a href="#S4.Thmtheorem10" title="Observation 4.10. ‣ 4.3 Adaptive Rounds ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">4.10</span></a>,
$\mathbb{E}|\mathcal{A}|\leq 3^{r-1}\bigl(b_{0}+(C/4+1/50)\,\varepsilon_{r}n+8C^{\prime}\log n+10\bigr)\text{.}$</p>
</div>
<div id="S4.SS4.p13" class="ltx_para">
<p class="ltx_p">Third, choose $\varepsilon_{r}$ with $3^{r-1}(C/4+1/50)\,\varepsilon_{r}\leq 1/128\text{.}$ Then
$\mathbb{E}|\mathcal{A}|\leq n/64$ for large $n\text{.}$ The remaining stages use only this bound, and they
give $\mathbb{E}[L_{r}]=\Omega_{r}(n^{\beta_{r}})$ in Case 2. In Case 1,
$\mathbb{E}[\mathrm{Move}]\geq\varepsilon_{r}n^{\beta_{r}}/100\text{.}$ Hence
$\mathbb{E}[\mathrm{Move}]=\Omega_{r}(n^{\beta_{r}})\text{,}$ which proves <a href="#S4.Thmtheorem12" title="Theorem 4.12. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.12</span></a>.
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S4.Thmtheorem13" title="Lemma 4.13. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.13</span></a>.</h6>
<div id="S4.SS4.p14" class="ltx_para">
<p class="ltx_p">If $n&lt;n_{0}\text{,}$ then $\Xi_{b}=0\text{,}$ and a route visits at most $|\mathcal{C}_{b}|\leq nb/2\leq n^{3/2}\leq n_{0}^{3/2}$ cells of $\mathcal{C}_{b}\text{.}$ Let $n\geq n_{0}\text{.}$ Deleting the configurations $(x,x)$ from
a route of movement $L$ and folding the others gives a sequence of folds of $\ell_{1}$-length at most
$L$ (<a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(b)), and the cells of $\mathcal{C}_{b}$ that the route visits are those whose folds occur in this sequence. The
residual clusters contain $\Xi_{b}$ cells in all, and every other cell of $\mathcal{C}_{b}$ lies in
a retired cluster. Fix a phase $t\text{.}$ Two clusters that retire in phase $t$ are isolated in phase
$t\text{,}$ so every cell of one is more than $\rho_{t}$ from every cell of the other. Order the clusters
retired in phase $t$ that have a cell in the sequence by the first occurrence of one of their cells.
Consecutive first occurrences are more than $\rho_{t}$ apart, so at most $1+L/\rho_{t}$ of these
clusters have a cell in the sequence, and each of them has at most $2^{t+1}$ cells. Summing over the
phases, the route visits at most</p>
<table id="S4.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{t=0}^{t_{\star}}2^{t+1}\Bigl(1+\frac{L}{\rho_{t}}\Bigr)\leq 2^{t_{\star}+2}+\frac{L}{\rho_{0}}\sum_{t\geq 0}\frac{2^{t+1}}{4^{t}}=2^{t_{\star}+2}+\frac{4L}{\rho_{0}}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">cells of retired clusters. Since $2^{t_{\star}}&lt;2\log n$ and $\rho_{0}=\varepsilon_{\star}H\geq\varepsilon_{\star}\sqrt{n/b}\text{,}$ this is at most $8\log n+(4/\varepsilon_{\star})L\sqrt{b/n}\text{.}$ Adding the $\Xi_{b}$
cells of residual clusters gives the bound for $n\geq n_{0}\text{.}$ Hence the lemma holds with
$C=4/\varepsilon_{\star}$ and $C^{\prime}=\max\{8,n_{0}^{3/2}\}\text{.}$
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S4.Thmtheorem14" title="Lemma 4.14. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.14</span></a>.</h6>
<div id="S4.SS4.p15" class="ltx_para">
<p class="ltx_p">If $n&lt;n_{0}\text{,}$ then $\Xi_{b}=0\text{,}$ so let $n\geq n_{0}\text{,}$ where $n_{0}$ is chosen at the end of the
proof. We charge $\Xi_{b}$ to sets of between $\kappa$ and $2\kappa$ cells of $\mathcal{C}_{b}$ that
carry a tree of short edges, bound the probability that a fixed set of cells lies in
$\mathcal{C}_{b}\text{,}$ and bound the expected number of such sets.</p>
</div>
<div id="S4.SS4.p16" class="ltx_para">
<p class="ltx_p">For a finite set $W$ of cells, its <em class="ltx_emph ltx_font_italic">position graph</em> has the positions occurring in $W$ as
vertices and the cells of $W$ as edges. Let $c(W)$ be its number of vertices minus its number of
components, which is the number of rank constraints that $W\subseteq\mathcal{C}_{b}$ imposes, and let $h(W)=|W|-c(W)$ be its cyclomatic number. We say that $W$ is <em class="ltx_emph ltx_font_italic">eligible</em> if
some tree with vertex set $W$ carries a phase $\ell(e)\in\{0,\dots,t_{\star}\}$ on each of its
edges $e=\{w,w^{\prime}\}$ such that $\lVert w-w^{\prime}\rVert_{1}\leq\rho_{\ell(e)}$ for every edge and
$\sum_{e}\ell(e)\leq C_{0}|W|\text{,}$ where $C_{0}=16\text{.}$ A <em class="ltx_emph ltx_font_italic">witness</em> is an eligible subset of
$\mathcal{C}_{b}$ with between $\kappa$ and $2\kappa$ cells. Let $N_{s}$ be the number of eligible subsets of
$\mathcal{C}_{b}$ with $s$ cells.</p>
</div>
<div id="S4.SS4.p17" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Charging.</em> Let $F$ be a residual cluster. Its merge history gives a tree with vertex set $F\text{:}$
when phase $t$ merges a component of close clusters, choose a spanning tree of the component and,
for each of its edges, a pair of cells, one in each of the two clusters, at distance at most
$\rho_{t}\text{,}$ and these pairs become tree edges with phase $t\text{.}$ A merge in phase $t$ adds fewer edges than
it merges clusters, and every cluster of phase $t$ has at least $2^{t}$ cells, so at most
$2^{-t}|F|$ tree edges have phase $t\text{,}$ and the phases sum to at most
$\sum_{t\geq 0}t\,2^{-t}|F|=2|F|\text{.}$</p>
</div>
<div id="S4.SS4.p18" class="ltx_para">
<p class="ltx_p">We cut this tree into connected pieces. Root the tree and collect edges from
the leaves upward: at each vertex, add the edge to each child together with the edges left over at
that child, and emit the collected edges as one piece as soon as they number at least $\kappa-1\text{.}$
Every collected set is connected, and the edges left over at a vertex number fewer than $\kappa-1\text{,}$
so each piece has between $\kappa-1$ and $2\kappa-3$ edges and hence between $\kappa$ and $2\kappa$
cells. The pieces have disjoint edge sets, and fewer than $\kappa-1$ edges remain at the root. The
tree has $|F|-1$ edges and $|F|\geq 2\kappa\text{,}$ so there are more than
$(|F|-\kappa)/(2\kappa)\geq|F|/(4\kappa)$ pieces.
Their phase sums total at most $2|F|\text{,}$ so fewer than $|F|/(8\kappa)$ pieces have phase sum above
$16\kappa\text{.}$ Each of the remaining, more than $|F|/(8\kappa)\text{,}$ pieces has a cell set $W$ with
$|W|\geq\kappa$ and phase sum at most $16\kappa\leq C_{0}|W|\text{,}$ so $W$ is a witness. Distinct pieces
have distinct cell sets, since a connected subtree with cell set $W$ contains every tree edge inside
$W\text{,}$ and distinct residual clusters are disjoint. Hence each residual cluster $F$ yields more than
$|F|/(8\kappa)$ witnesses, all distinct, and</p>
<table id="S4.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Xi_{b}\ \leq\ 8\kappa\sum_{s=\kappa}^{2\kappa}N_{s}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
<div id="S4.SS4.p19" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Witness Probability.</em> Fix a set $W$ of $s\leq 2\kappa$ cells. Reveal the ranks of its positions
one component of the position graph at a time, each component in an order in which every vertex $x$
after the first has a neighbor $x^{\prime}$ earlier in the order. If $W\subseteq\mathcal{C}_{b}\text{,}$ then every
such $x$ receives a rank in the scale-$b$ block of $x^{\prime}\text{.}$ Given the earlier ranks, this block contains
at most $b$ of the at least $n-2s\geq n/4$ unrevealed ranks, so this happens with probability at most $4b/n\text{.}$ There are $c(W)$ such vertices, so
$\Pr[W\subseteq\mathcal{C}_{b}]\leq(4b/n)^{c(W)}=(4b/n)^{s-h(W)}\text{.}$</p>
</div>
<div id="S4.SS4.p20" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">First Moment.</em> Let $N_{s}^{(h)}$ be the number of eligible subsets of $\mathcal{C}_{b}$ with
$s$ cells and cyclomatic number $h\text{.}$ We bound $\mathbb{E}[N_{s}^{(h)}]$ for $h\leq\eta s/t_{\star}$
here, where $\eta$ is chosen below, and treat larger $h$ in the next paragraph. Given an eligible set
$W$ with $s$ cells, fix a tree as in the definition of eligibility, root it, order the children of
each vertex, and add the cells of $W$ one at a time in the preorder of this ordered rooted tree, so
that every cell comes after its parent. Adding a cell increases $c$ of the set added so far by one,
unless its two positions already lie in one component of the position graph of that set. We then say
that the cell <em class="ltx_emph ltx_font_italic">closes a cycle</em>. Since $c(W)=s-h\text{,}$ exactly $h$ cells close a cycle. Hence $W$ is encoded by the ordered rooted tree,
at most $4^{s}$ choices; the phases of its edges, which sum to at most $C_{0}s\text{,}$ at most
$2^{(C_{0}+1)s}$ choices; the set of cells that close a cycle, at most $2^{s}$ choices; and the
placement of the cells in preorder. A cell that closes a cycle is one of at most $(2s)^{2}$ pairs of
positions already present. The root is one of at most $n^{2}/2$ cells. Every other cell lies within
distance $\rho_{\ell}$ of its parent, where $\ell$ is the phase of the tree edge to its parent, so it
has at most $(2\rho_{\ell}+1)^{2}\leq 9\rho_{\ell}^{2}$ placements, since
$\rho_{\ell}\geq\varepsilon_{\star}H\geq\varepsilon_{\star}n^{1/4}\geq 1$ for $n\geq n_{0}\text{.}$ The bound
$\Pr[W\subseteq\mathcal{C}_{b}]\leq(4b/n)^{s-h}$ gives a factor $4b/n$ for each of the $s-h$ cells
that close no cycle. Since $H^{2}\leq 4n/b\text{,}$ we have
$9\rho_{\ell}^{2}\cdot 4b/n\leq 144\,\varepsilon_{\star}^{2}16^{\ell}\text{,}$ and the phases give
$\prod_{e}16^{\ell(e)}\leq 16^{C_{0}s}\text{.}$ Collecting the factors,</p>
<table id="S4.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl[N_{s}^{(h)}\bigr]\leq 2nb\;\varepsilon_{\star}^{-2}\,\bigl(C_{1}\varepsilon_{\star}^{2}\bigr)^{s}\,\bigl(4s^{2}/\varepsilon_{\star}^{2}\bigr)^{h}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">for an absolute constant $C_{1}\text{.}$ Let $\varepsilon_{\star}^{2}=1/(16C_{1})$ and
$\eta=\bigl(6+2\log(1/\varepsilon_{\star})\bigr)^{-1}\text{.}$ If $h\leq\eta s/t_{\star}\text{,}$ then
$(4s^{2}/\varepsilon_{\star}^{2})^{h}\leq 2^{s}\text{.}$ Indeed, $s\leq 2\kappa&lt;4\log n$ gives
$\log(4s^{2})\leq 6+2\log\log n\leq 6t_{\star}$ for $n\geq n_{0}\text{,}$ so
$h\log(4s^{2}/\varepsilon_{\star}^{2})\leq(\eta s/t_{\star})\bigl(6t_{\star}+2\log(1/\varepsilon_{\star})\bigr)\leq s\text{.}$
Hence $\mathbb{E}[N_{s}^{(h)}]\leq 2nb\,\varepsilon_{\star}^{-2}8^{-s}\text{,}$ and summing over the at most $s$
values of $h$ gives $\sum_{h\leq\eta s/t_{\star}}\mathbb{E}[N_{s}^{(h)}]\leq nb\,4^{-s}$ for
$s\geq\kappa$ and $n\geq n_{0}\text{.}$</p>
</div>
<div id="S4.SS4.p21" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">High Cyclomatic Number.</em> Let $N_{s}^{\mathrm{high}}$ be the number of eligible subsets $W$ of
$\mathcal{C}_{b}$ with $s$ cells and $h(W)&gt;\eta s/t_{\star}\text{.}$ For these we use the geometry of the
set instead. Tree edges join cells at distance at most $\rho_{t_{\star}}=\varepsilon_{\star}H\kappa^{2}\text{,}$ so
every cell of $W$ lies within distance $(s-1)\rho_{t_{\star}}$ of the root, and all positions of $W$
lie in the two intervals of radius $R=s\rho_{t_{\star}}$ around the two positions of the root. These
intervals contain $V\leq 4R+2=O\bigl(\sqrt{n/b}\,\log^{3}n\bigr)$ positions. Let $N_{s,\omega,\tau}$ be
the number of these sets whose position graph has $\omega$ vertices and $\tau$ components. Such a set
is encoded by its root, at most $n^{2}$ choices, its other $\omega-2$ positions, at most
$V^{\omega-2}$ choices, and its $s$ cells as pairs of its positions, at most $(2s)^{2s}$ choices.
With $\gamma=4b/n$ and $z=\omega-2\tau\text{,}$ the bound on $\Pr[W\subseteq\mathcal{C}_{b}]$ gives</p>
<table id="S4.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}[N_{s,\omega,\tau}]\leq n^{2}(2s)^{2s}V^{\omega-2}\gamma^{\omega-\tau}=n^{2}(2s)^{2s}V^{-2}\,\bigl(V^{2}\gamma\bigr)^{\tau}\,\bigl(V\gamma\bigr)^{z}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Here $V^{2}\gamma=O(\log^{6}n)\text{,}$ and $V\gamma\leq n^{-1/5}$ for $n\geq n_{0}$ because $b\leq\sqrt{n}\text{.}$
The position graph is simple, so a component with two vertices contributes nothing to $z$ or to $h\text{.}$
A component with $\omega^{\prime}\geq 3$ vertices contributes $\omega^{\prime}-2\geq\omega^{\prime}/3$ to $z\text{,}$ so
$z\geq\omega_{3}/3\text{,}$ where $\omega_{3}$ is the number of vertices in components with at least three vertices. Also
$h\leq\omega_{3}^{2}/2\text{,}$ because $h$ is at most the number of edges in these components. Hence
$z\geq\sqrt{2h}/3\text{,}$ and $h&gt;\eta s/t_{\star}\geq\eta\kappa/t_{\star}$ gives
$z=\Omega\bigl(\sqrt{\log n/\log\log n}\bigr)\text{.}$ So $(V\gamma)^{z}=n^{-\Omega(\sqrt{\log n/\log\log n})}\text{,}$
whereas $n^{2}(2s)^{2s}(V^{2}\gamma)^{\tau}=\exp\bigl(O(\log n\,\log\log n)\bigr)$ because
$s,\tau\leq 4\log n\text{.}$ For $n\geq n_{0}$ the product is at most $n^{-22}\text{,}$ and summing over the at most
$(2s)^{2}\leq n^{2}$ pairs $(\omega,\tau)$ gives $\mathbb{E}[N_{s}^{\mathrm{high}}]\leq n^{-20}\text{.}$</p>
</div>
<div id="S4.SS4.p22" class="ltx_para">
<p class="ltx_p">For $\kappa\leq s\leq 2\kappa$ the two regimes give $\mathbb{E}[N_{s}]\leq nb\,4^{-s}+n^{-20}\text{.}$ Since
$4^{-\kappa}\leq n^{-2}$ and $b\leq\sqrt{n}\text{,}$</p>
<table id="S4.Ex15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}[\Xi_{b}]\ \leq\ 8\kappa\sum_{s=\kappa}^{2\kappa}\mathbb{E}[N_{s}]\ \leq\ 8\kappa(\kappa+1)\bigl(n^{-1/2}+n^{-20}\bigr)\ \leq\ 1,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where $n_{0}$ is chosen so large that this inequality and the estimates above hold for all
$n\geq n_{0}\text{.}$
∎</p>
</div>
</div>
</section>
</section>
<section id="S5" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="routing-and-the-sampling-algorithm">
<span class="ltx_tag ltx_tag_section">5 </span>Routing and the Sampling Algorithm</h2>

<div id="S5.p1" class="ltx_para">
<p class="ltx_p">This section and the next prove the upper-bound half of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Movement Exponent). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>. Every route of our algorithms
visits configurations known when the round starts, and <a href="#S5.SS1" title="5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> bounds the movement this takes. A
merge sort then gives the fully adaptive bound (<a href="#S5.SS2" title="5.2 The Fully Adaptive Bound ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>). For a fixed number $r\geq 2$ of rounds we use the
sampling algorithm, which refines the rank order round by round (<a href="#S5.SS3" title="5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.3</span></a>). On the line, each refinement round
selects intervals of one length (<a href="#S5.SS4" title="5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.4</span></a>).</p>
</div>
<section id="S5.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="routing">
<span class="ltx_tag ltx_tag_subsection">5.1 </span>Routing</h3>

<div id="S5.SS1.p1" class="ltx_para">
<p class="ltx_p">The next lemma bounds the movement needed to visit a known set of configurations.</p>
</div>
<div id="S5.Thmtheorem1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem1.p1" class="ltx_para">
<ol id="S5.I1" class="ltx_enumerate">
<li id="S5.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(i)</span> 
<div id="S5.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let </span>$\mathcal{Q}$<span class="ltx_text ltx_font_italic"> be a set of </span>$Q\geq 1$<span class="ltx_text ltx_font_italic"> points of a box in </span>$\mathbb{Z}^{D^{\prime}}$<span class="ltx_text ltx_font_italic"> whose sides are at
most </span>$m^{\prime}$<span class="ltx_text ltx_font_italic">. From any given point of the box, a lattice path inside the box, that is, a
sequence of points with consecutive points at </span>$\ell_{1}$<span class="ltx_text ltx_font_italic"> distance </span>$1$<span class="ltx_text ltx_font_italic">, visits all points of
</span>$\mathcal{Q}$<span class="ltx_text ltx_font_italic"> and has length </span>$O_{D^{\prime}}\bigl(m^{\prime}Q^{1-1/D^{\prime}}+m^{\prime}\bigr)$<span class="ltx_text ltx_font_italic">. The path can be computed
from </span>$\mathcal{Q}$<span class="ltx_text ltx_font_italic"> in polynomial time.</span></p>
</div>
</li>
<li id="S5.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(ii)</span> 
<div id="S5.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">In the comparison grid, any </span>$Q\geq 1$<span class="ltx_text ltx_font_italic"> configurations are visited by a route that starts at
the current configuration and has movement </span>$O_{d}\bigl(n^{1/d}Q^{1-1/D}+n^{1/d}\bigr)$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
</ol>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS1.p2" class="ltx_para">
<p class="ltx_p">For (i), we cut the box into small cubes and traverse them in serpentine order, visiting the points
of $\mathcal{Q}$ in each cube on the way. Let $\Delta=\lceil m^{\prime}Q^{-1/D^{\prime}}\rceil$ and cut the box into
cubes of side $\Delta\text{.}$ There are at most $(m^{\prime}/\Delta+1)^{D^{\prime}}\leq(Q^{1/D^{\prime}}+1)^{D^{\prime}}\leq 2^{D^{\prime}}Q$ of
them. Consecutive cubes of the serpentine order are adjacent, so the path moves $O_{D^{\prime}}(\Delta)$
from one cube to the next. Inside a cube it moves $O_{D^{\prime}}(\Delta)$ from one point of $\mathcal{Q}$
to the next. Together with the $O_{D^{\prime}}(m^{\prime})$ steps from the given point to the first cube, this gives
length $O_{D^{\prime}}(\Delta Q+m^{\prime})\text{.}$ Since the box has at most $m^{\prime D^{\prime}}$ points, $Q^{1/D^{\prime}}\leq m^{\prime}\text{,}$ so
$\Delta Q\leq m^{\prime}Q^{1-1/D^{\prime}}+Q\leq 2m^{\prime}Q^{1-1/D^{\prime}}\text{.}$</p>
</div>
<div id="S5.SS1.p3" class="ltx_para">
<p class="ltx_p">Part (ii) is (i) for the box $[m]^{D}\text{,}$ with $D^{\prime}=D$ and $m^{\prime}=m=n^{1/d}\text{.}$
∎</p>
</div>
</div>
<div id="S5.SS1.p4" class="ltx_para">
<p class="ltx_p">Merging two sorted lists by walking them in rank order can cost a long jump per comparison. The next
lemma instead advances many binary searches in one round, so that one route serves them all.</p>
</div>
<div id="S5.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $R\subseteq[m]^{d}$ be a box of aspect ratio $O_{d}(1)$ with $|R|\geq 2\text{,}$ and let its positions be
partitioned into two lists, each sorted by rank. A deterministic algorithm finds the rank order of
$R$ in $O\bigl((\log|R|)^{2}\bigr)$ rounds with total movement $O_{d}\bigl(|R|^{1+1/(2d)}\bigr)\text{.}$
Its routes stay in $R\times R\text{,}$ and the bound holds whichever configuration of $R\times R$ each round
starts from.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS1.p5" class="ltx_para">
<p class="ltx_p">The algorithm splits the two lists at the median of their union by binary search, recurses on the
two parts, and advances all binary searches of one depth together. Write $N=|R|\text{.}$ A subproblem consists of a sublist of consecutive entries of each
list, $s$ entries in all, and asks for the $t=\lceil s/2\rceil$ lowest keys of their union. For
$1\leq i\leq t\text{,}$ the $i$-th entry of the first sublist, if it exists, has $i-1$ entries of its sublist below it, so it
is among these $t$ keys exactly when at most $t-i$ entries of the second sublist lie below it.
Equivalently, it lies below the $(t-i+1)$-th entry of the second sublist, or that entry does not
exist. This condition is monotone in $i\text{,}$ so a binary search on $i$ finds the $t$ lowest keys with
$O(\log(s+2))$ comparisons of one entry of each sublist. The $t$ lowest keys form a prefix of each sublist, so the two parts are
again subproblems, of sizes $\lceil s/2\rceil$ and $\lfloor s/2\rfloor\text{.}$ The recursion stops at subproblems with an empty
sublist, which are already sorted, and this gives the rank order of $R\text{.}$</p>
</div>
<div id="S5.SS1.p6" class="ltx_para">
<p class="ltx_p">Each round advances every binary search of the current depth by one comparison. At depth $\lambda$
there are at most $2^{\lambda}$ subproblems of size at most $\lceil N/2^{\lambda}\rceil\text{,}$ so this
depth takes $O\bigl(\log(N/2^{\lambda}+2)\bigr)$ rounds. There are $O(\log N)$ depths, which gives
the bound on the rounds. A round at depth $\lambda$ visits at most $2^{\lambda}$ known configurations
of $R\times R\text{,}$ a box whose sides are $O_{d}(N^{1/d})\text{.}$ By <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i), from any given
configuration of $R\times R$ its movement is $O_{d}\bigl(N^{1/d}2^{(1-1/D)\lambda}+N^{1/d}\bigr)\text{.}$
Substituting $i=\lceil\log_{2}N\rceil-\lambda\text{,}$ the main terms total</p>
<table id="S5.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$O_{d}\Bigl(N^{1/d}\sum_{\lambda}2^{(1-1/D)\lambda}\log\bigl(N/2^{\lambda}+2\bigr)\Bigr)=O_{d}\Bigl(N^{1/d}N^{1-1/D}\sum_{i\geq 0}(i+2)\,2^{-(1-1/D)i}\Bigr)=O_{d}\bigl(N^{1+1/(2d)}\bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">since the series converges and $1/d-1/D=1/(2d)\text{.}$ The additive terms total
$O_{d}\bigl(N^{1/d}(\log N)^{2}\bigr)=O_{d}\bigl(N^{1+1/(2d)}\bigr)\text{.}$
∎</p>
</div>
</div>
</section>
<section id="S5.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-fully-adaptive-bound">
<span class="ltx_tag ltx_tag_subsection">5.2 </span>The Fully Adaptive Bound</h3>

<div id="S5.SS2.p1" class="ltx_para">
<p class="ltx_p">For $r=\infty\text{,}$ a merge sort over a partition of the grid into boxes gives the upper bound in every
dimension. Together with <a href="#S4.Thmtheorem5" title="Proposition 4.5. ‣ 4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">4.5</span></a>, it determines $M_{\infty}^{(d)}(n)\text{.}$</p>
</div>
<div id="S5.Thmtheorem3" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Proposition 5.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every $d\geq 1\text{,}$ a deterministic algorithm sorts in $O\bigl((\log n)^{3}\bigr)$ rounds with movement
$O_{d}\bigl(n^{1+1/(2d)}\bigr)\text{.}$ Hence $M_{\infty}^{(d)}(n)=O_{d}\bigl(n^{1+1/(2d)}\bigr)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS2.p2" class="ltx_para">
<p class="ltx_p">We sort by merging along a tree of boxes of depth $T=d\lceil\log_{2}m\rceil\leq\log_{2}n+d\text{.}$ The root
is $[m]^{d}\text{.}$ At depth $t\text{,}$ every box whose side along axis $t\bmod d$ is $s\geq 2$ is halved along
that axis, into sides $\lceil s/2\rceil$ and $\lfloor s/2\rfloor\text{.}$ A box whose side along this axis is
$1$ has itself as its only child. At depth $T$ all boxes are single positions. The boxes of one depth
form a grid and have aspect ratio $O(1)\text{.}$ At height $i\text{,}$ that is, at depth $T-i\text{,}$ there are at most
$2^{T-i}\leq 2^{d}n/2^{i}$ boxes, and each has at most $2^{i}$ positions, because a box has at most two
children. The algorithm processes the heights in increasing order and merges the two halves of each
halved box by <a href="#S5.Thmtheorem2" title="Lemma 5.2. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>.</p>
</div>
<div id="S5.SS2.p3" class="ltx_para">
<p class="ltx_p">By <a href="#S5.Thmtheorem2" title="Lemma 5.2. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>, the movement inside the boxes of height $i$ is
$O_{d}\bigl((n/2^{i})\cdot 2^{i(1+1/(2d))}\bigr)=O_{d}\bigl(n\,2^{i/(2d)}\bigr)\text{.}$ Summing over
$i\leq T$ gives a geometric series dominated by its last term, so the total is
$O_{d}\bigl(n\,2^{T/(2d)}\bigr)=O_{d}\bigl(n^{1+1/(2d)}\bigr)\text{.}$</p>
</div>
<div id="S5.SS2.p4" class="ltx_para">
<p class="ltx_p">The merges of one height share their rounds: a round of the algorithm is one round of each merge, and
its route visits the boxes in the serpentine order of their grid. The heads cross from one box to
the next with movement $O_{d}(2^{i/d})\text{,}$ so these crossings, together with the move to the first box,
add $O_{d}\bigl((n/2^{i})\,2^{i/d}+n^{1/d}\bigr)=O_{d}(n)$ per round. Each merge takes
$O\bigl((\log n)^{2}\bigr)$ rounds and there are $O(\log n)$ heights, so the algorithm has $O\bigl((\log n)^{3}\bigr)$ rounds
and the crossings total $O_{d}\bigl(n(\log n)^{3}\bigr)=O_{d}\bigl(n^{1+1/(2d)}\bigr)\text{.}$
∎</p>
</div>
</div>
<div id="S5.Thmtheorem4" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 5.4</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S5.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p">At $d=1$ the tree of boxes is the merge tree of ordinary merge sort, with the merges of <a href="#S5.Thmtheorem2" title="Lemma 5.2. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>. The exponent $3/2$ agrees with the bound of Maass and
Schnitger for sorting on a Turing machine with one worktape and a two-way read-only input
tape <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib33" title="An optimal lower bound for Turing machines with one work tape and a two-way input tape" class="ltx_ref">MS86</a>; <a href="#bib.bib14" title="The complexity of matrix transposition on one-tape off-line Turing machines" class="ltx_ref">DMS91</a>]</cite>. Their input consists of bit strings, so the agreement is up to logarithmic
factors.</p>
</div>
</div>
</section>
<section id="S5.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-sampling-algorithm">
<span class="ltx_tag ltx_tag_subsection">5.3 </span>The Sampling Algorithm</h3>

<div id="S5.SS3.p1" class="ltx_para">
<p class="ltx_p">Between rounds, the sampling algorithm knows the
rank order only up to a partition of the keys into sets of consecutive ranks.</p>
</div>
<div id="S5.Thmtheorem5" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 5.5</span></span><span class="ltx_text ltx_font_bold"> </span>(Segment)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">segment</em> is a nonempty set of positions whose ranks form an interval of $[n]$ known to the
algorithm. A segment may be a single position.</p>
</div>
</div>
<div id="S5.SS3.p2" class="ltx_para">
<p class="ltx_p">The comparisons that remain are the pairs within segments, and the movement they take depends on
where each segment lies: a segment with many keys in a small region is cheap. The following
quantity records this, by weighting each key with the number of boxes that its segment meets.</p>
</div>
<div id="S5.Thmtheorem6" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 5.6</span></span><span class="ltx_text ltx_font_bold"> </span>(Dispersion)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p">For a partition $\mathcal{P}$ of $[m]^{d}$ into boxes and a family of disjoint segments, let
$\mathcal{P}(G)$ be the set of boxes of $\mathcal{P}$ that a segment $G$ meets. The <em class="ltx_emph ltx_font_italic">dispersion</em>
of the family is</p>
<table id="S5.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$S_{\mathcal{P}}=\sum_{G}|G|\,|\mathcal{P}(G)|.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div id="S5.SS3.p3" class="ltx_para">
<p class="ltx_p">Splitting a segment never raises the dispersion: if $G_{1},G_{2}\subseteq G$ are disjoint, then
$\mathcal{P}(G_{i})\subseteq\mathcal{P}(G)\text{,}$ so
$|G_{1}|\,|\mathcal{P}(G_{1})|+|G_{2}|\,|\mathcal{P}(G_{2})|\leq|G|\,|\mathcal{P}(G)|\text{.}$</p>
</div>
<div id="S5.SS3.p4" class="ltx_para">
<p class="ltx_p">The algorithm has $r$ rounds. The first chooses random positions, the <em class="ltx_emph ltx_font_italic">splitters</em>. The next
$r-2$ are <em class="ltx_emph ltx_font_italic">refinement rounds</em>, which draw samples, and the last is the <em class="ltx_emph ltx_font_italic">cleanup</em>. A
<em class="ltx_emph ltx_font_italic">sample</em> is given by a partition $\mathcal{P}$ of $[m]^{d}$ into boxes and a rate $p\in(0,1]\text{.}$ Drawing it selects each box of $\mathcal{P}$ independently with
probability $p\text{,}$ and the keys in selected boxes that lie in segments are its <em class="ltx_emph ltx_font_italic">pivots</em>. The
splitters and the pivots are called <em class="ltx_emph ltx_font_italic">resolved keys</em>, since the order of each of them relative
to every other key is known after its round. Resolved keys lie in no segment.</p>
</div>
<figure id="alg1" class="ltx_float ltx_float_algorithm ltx_framed ltx_framed_top">
<figcaption class="ltx_caption"><span class="ltx_tag ltx_tag_float"><span class="ltx_text ltx_font_bold">Algorithm 1</span> </span> The sampling algorithm</figcaption>
<div class="ltx_listing ltx_listing">
<div id="alg1.l0" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"></span>
              
              
            <span class="ltx_text ltx_font_bold">Parameters:</span> $r\geq 2\text{;}$ the exponents $a_{0}&gt;\dots&gt;a_{r-2}$ of <a href="#S2.Thmtheorem5" title="Lemma 2.5. ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>, with $b_{j}=n^{a_{j}}\text{;}$
the samples of each refinement round; a route procedure for each refinement round and for the
cleanup round.

</div>
<div id="alg1.l1" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">1:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">Round $1$ (splitter).</span> Choose $\lceil n/b_{0}\rceil$ positions uniformly at random
without replacement, the splitters. 

</div>
<div id="alg1.l2" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">2:</span></span>
              
              
              The required configurations are all $(u,v)$ with $u\neq v$ and $v$ a splitter. For each
splitter $v$ in turn, place the second head on $v$ and sweep the first head through $[m]^{d}\text{.}$


</div>
<div id="alg1.l3" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">3:</span></span>
              
              
              The splitters become resolved keys. In rank order, they cut the other positions into sets,
and the nonempty sets are the segments. 

</div>
<div id="alg1.l4" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">4:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">for</span> $j=1,\dots,r-2$ <span class="ltx_text ltx_font_bold">do</span>



</div>
<div id="alg1.l5" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">5:</span></span>
              
              
                 <span class="ltx_text ltx_font_bold">Round $j+1$ (refinement).</span> Draw the samples of this round independently. The pivots
of the round are the pivots of its samples. 

</div>
<div id="alg1.l6" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">6:</span></span>
              
              
                 The required configurations are all $(u,v)$ with $u\neq v$ and $v$ a pivot in the
segment of $u\text{.}$ Visit them by the route procedure. 

</div>
<div id="alg1.l7" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">7:</span></span>
              
              
                 The pivots become resolved keys. In each segment, the nonempty maximal pivot-free sets of
consecutive ranks become the new segments. 

</div>
<div id="alg1.l8" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">8:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">end</span> <span class="ltx_text ltx_font_bold">for</span>
</div>
<div id="alg1.l9" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">9:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">Round $r$ (cleanup).</span> The required configurations are, for each cell whose two positions lie
in one segment, one fixed orientation. Visit them by the route procedure. 

</div>
<div id="alg1.l10" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">10:</span></span>
              
              
              Sort each segment, and output the resolved keys and the segments in rank order.


</div>
</div>
</figure>
<div id="S5.SS3.p5" class="ltx_para">
<p class="ltx_p"><a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a> is a template: each instance below specifies the samples and the routes. The
state between rounds is the sequence of resolved keys and nonempty segments in rank order, and the
analysis tracks the dispersion of the segments. The required configurations of a round are known when the round
starts, so its route depends only on the coins and on the outcomes of earlier rounds, and in every
instance it is computed in polynomial time. Line <a href="#alg1.l2" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a> moves $O(n)$ per splitter, so
round $1$ has movement $O(n\lceil n/b_{0}\rceil)=O(n^{2-a_{0}})\text{,}$ and $2-a_{0}=\beta_{r}^{(d)}$ by
<a href="#S2.E1" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>.</p>
</div>
<div id="S5.SS3.p6" class="ltx_para">
<p class="ltx_p">The algorithm is correct for every input and every outcome of its coins. Every key other than a
splitter is compared with all splitters in round $1\text{,}$ so its segment is known. In a refinement round,
every key of a segment, pivots included, is compared with all other pivots of this segment, so the
new state is known. The cleanup compares all pairs within a segment, and the state determines the
order of every other pair.</p>
</div>
<div id="S5.SS3.p7" class="ltx_para">
<p class="ltx_p">The next lemma bounds the <em class="ltx_emph ltx_font_italic">squared mass</em> $A=\sum_{G}|G|^{2}$ of the family after round $1\text{,}$ which counts the pairs of
keys in a common segment. The
squared mass is the dispersion for the partition into single positions, where $|\mathcal{P}(G)|=|G|\text{.}$</p>
</div>
<div id="S5.Thmtheorem7" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.7</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem7.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix an input and choose $s$ positions uniformly at random without replacement, where $1\leq s\leq n\text{.}$ In rank order, the chosen positions cut the other positions into sets $G_{0},\dots,G_{s}\text{,}$ which may be empty. Then
$\mathbb{E}\sum_{i}|G_{i}|^{2}\leq 3n^{2}/s\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS3.p8" class="ltx_para">
<p class="ltx_p">The sum $\sum_{i}|G_{i}|^{2}$ counts the ordered pairs of ranks that lie in a common set, and we bound
the probability of each pair. Since the input is a bijection, the chosen ranks form a uniformly random
set of $s$ ranks. Two ranks at distance $\Delta$ lie in a common set only if none of the $\Delta$ ranks starting at the lower one is
chosen, which has probability at most $(1-s/n)^{\Delta}\leq\exp(-s\Delta/n)\text{.}$ Hence</p>
<table id="S5.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\sum_{i}|G_{i}|^{2}\ \leq\ n+2n\sum_{\Delta\geq 1}\exp(-s\Delta/n)\ \leq\ n+\frac{2n^{2}}{s}\ \leq\ \frac{3n^{2}}{s},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">using $\sum_{\Delta\geq 1}\exp(-s\Delta/n)=(\exp(s/n)-1)^{-1}\leq n/s\text{.}$
∎</p>
</div>
</div>
<div id="S5.SS3.p9" class="ltx_para">
<p class="ltx_p">A sample of rate $p$ leaves dispersion about $n/p$ for its own partition, in every dimension and whatever the
family that enters the round.</p>
</div>
<div id="S5.Thmtheorem8" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.8</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem8.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix an input and a family of disjoint segments, and draw a sample with partition $\mathcal{P}$ and
rate $p\text{.}$ Within each segment, the pivots split the other keys into <em class="ltx_emph ltx_font_upright">refined segments</em>, the
nonempty maximal pivot-free sets of consecutive ranks. For a key $u$ in a segment, let $G_{u}$ be its
refined segment if $u$ is not a pivot, and $G_{u}=\emptyset$ otherwise. Then
$\mathbb{E}|\mathcal{P}(G_{u})|\leq 3/p\text{,}$ and hence the dispersion of the refined segments satisfies
$\mathbb{E}[S_{\mathcal{P}}]\leq 3n/p\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS3.p10" class="ltx_para">
<p class="ltx_p">We bound the number of boxes that $G_{u}$ meets above and below $u\text{,}$ and then sum over the keys. List
the segment of $u$ in rank order. Let $R_{u}^{+}$ be the number of boxes of $\mathcal{P}\text{,}$ other
than the box of $u\text{,}$ that the keys above $u$ meet before the first pivot above $u\text{.}$ If
$R_{u}^{+}\geq t\text{,}$ then the first $t$ such boxes in rank order are all unselected. These boxes are determined by the input and the family, and each is selected independently with probability $p\text{,}$ so $\Pr[R_{u}^{+}\geq t]\leq(1-p)^{t}\text{,}$ and $\mathbb{E}[R_{u}^{+}]\leq 1/p\text{.}$
Define $R_{u}^{-}$ in the same way for the keys below $u\text{.}$ Then
$|\mathcal{P}(G_{u})|\leq 1+R_{u}^{-}+R_{u}^{+}\text{,}$ whose expectation is at most $3/p\text{.}$ Finally,
$S_{\mathcal{P}}=\sum_{u}|\mathcal{P}(G_{u})|\text{,}$ and there are at most $n$ keys.
∎</p>
</div>
</div>
<div id="S5.SS3.p11" class="ltx_para">
<p class="ltx_p">The later rounds tour the product boxes of a partition and visit the required configurations inside each of them. Fix a family of disjoint
segments and a partition $\mathcal{P}$ of $[m]^{d}$ into boxes. For $I,J\in\mathcal{P}\text{,}$ the set
$I\times J$ is a product box, and we write $Q_{I,J}=\sum_{G}|G\cap I|\,|G\cap J|\text{.}$ The product box
$I\times J$ is <em class="ltx_emph ltx_font_italic">occupied</em> if $Q_{I,J}&gt;0\text{,}$ and $P$ is the number of occupied product boxes. If this
family enters a refinement round or the cleanup, a required configuration in $I\times J$ is a pair
$(u,v)$ with $u\in I\text{,}$ $v\in J\text{,}$ and $u$ and $v$ in a common segment, so at most $Q_{I,J}$ required
configurations lie in $I\times J\text{.}$ The number of occupied product boxes bounds the tour, and on the line the sum of the
$\sqrt{Q_{I,J}}$ bounds the visits. The dispersion bounds both:</p>
<table id="S5.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$P\ \leq\ \sum_{G}|\mathcal{P}(G)|^{2}\ \leq\ S_{\mathcal{P}},\qquad\sum_{I,J}\sqrt{Q_{I,J}}\ \leq\ \sum_{G}\Bigl(\sum_{I}\sqrt{|G\cap I|}\Bigr)^{2}\ \leq\ S_{\mathcal{P}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.1)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">For the first chain, a segment contributes to $Q_{I,J}$ only if it meets both $I$ and $J\text{,}$ which
holds for $|\mathcal{P}(G)|^{2}$ product boxes, and $|\mathcal{P}(G)|\leq|G|\text{.}$ For the second chain,
the first step is the subadditivity of the square root over the segments, and the second is the
Cauchy–Schwarz inequality over the $|\mathcal{P}(G)|$ nonzero terms $\sqrt{|G\cap I|}\text{.}$</p>
</div>
</section>
<section id="S5.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-upper-bound-on-the-line">
<span class="ltx_tag ltx_tag_subsection">5.4 </span>The Upper Bound on the Line</h3>

<div id="S5.SS4.p1" class="ltx_para">
<p class="ltx_p">On the line, the dispersion bounds both the tour of the next round and its visits (<a href="#S5.E1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>), so each refinement round draws one sample. In this
subsection $d=1\text{,}$ so $D=2$ and $q=\tfrac{1}{2}\text{,}$ and we write $\beta=\beta_{r}\text{.}$ An
<em class="ltx_emph ltx_font_italic">interval of length $h$</em> is a set of $h$ consecutive positions. We partition the line into
intervals of length $h\text{,}$ the last possibly shorter, and write $\mathcal{P}_{h}(G)$ and $S_{h}$ for
this partition. An interval of length $h$ meets at most two intervals of length $h^{\prime}\geq h\text{,}$ so
$S_{h^{\prime}}\leq 2S_{h}\text{.}$</p>
</div>
<div id="S5.SS4.p2" class="ltx_para">
<p class="ltx_p">For $1\leq j\leq r-1\text{,}$ let
$h_{j}=\lceil\sqrt{n/b_{j-1}}\rceil\text{,}$ so that $h_{1}\leq\dots\leq h_{r-1}=\lceil\sqrt{n/g}\rceil\text{,}$ and
for $1\leq j\leq r-2\text{,}$ let $p_{j}=n^{-a_{j}}\text{.}$ <a href="#alg2" title="In 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">2</span></a> is the instance of
<a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a> with these parameters. We also apply <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) to coarser grids whose points are intervals, cubes, or product
boxes. A step of the lattice path then moves the heads to an adjacent interval, cube, or product box.</p>
</div>
<figure id="alg2" class="ltx_float ltx_float_algorithm ltx_framed ltx_framed_top">
<figcaption class="ltx_caption"><span class="ltx_tag ltx_tag_float"><span class="ltx_text ltx_font_bold">Algorithm 2</span> </span> The line algorithm</figcaption>
<div class="ltx_listing ltx_listing">
<div id="alg2.l0" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"></span>
              
              
            <span class="ltx_text ltx_font_bold">Parameters:</span> $d=1\text{;}$ $r\geq 2\text{;}$ $h_{j}$ and $p_{j}$ as above.

</div>
<div id="alg2.l1" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">1:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">Round $1$ (splitter).</span> Lines <a href="#alg1.l1" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>–<a href="#alg1.l3" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a> of
<a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>.

</div>
<div id="alg2.l2" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">2:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">for</span> $j=1,\dots,r-2$ <span class="ltx_text ltx_font_bold">do</span>



</div>
<div id="alg2.l3" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">3:</span></span>
              
              
                 <span class="ltx_text ltx_font_bold">Round $j+1$ (refinement).</span> Draw one sample: intervals of length $h_{j}\text{,}$ rate
$p_{j}\text{.}$

</div>
<div id="alg2.l4" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">4:</span></span>
              
              
                 <span class="ltx_text ltx_font_bold">for</span> each selected interval $J\text{,}$ in order on the line <span class="ltx_text ltx_font_bold">do</span>

 

</div>
<div id="alg2.l5" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">5:</span></span>
              
              
                    Place the second head at the left endpoint of $J\text{,}$ and sweep the first head along the
line from left to right.

</div>
<div id="alg2.l6" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">6:</span></span>
              
              
                    When the first head reaches an interval $I$ with $Q_{I,J}&gt;0\text{,}$ visit the required configurations
in $I\times J$ by <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i). Then return the second head to the left endpoint of
$J$ and the first head to its place in the sweep. 

</div>
<div id="alg2.l7" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">7:</span></span>
              
              
                 <span class="ltx_text ltx_font_bold">end</span> <span class="ltx_text ltx_font_bold">for</span>
</div>
<div id="alg2.l8" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">8:</span></span>
              
              
                 Update the state as in Line <a href="#alg1.l7" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a> of <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>.

</div>
<div id="alg2.l9" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">9:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">end</span> <span class="ltx_text ltx_font_bold">for</span>
</div>
<div id="alg2.l10" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">10:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">Round $r$ (cleanup).</span> With $h=h_{r-1}\text{,}$ move along the lattice path of
<a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) through the occupied product boxes on the grid of $\lceil n/h\rceil^{2}$
product boxes. On first arrival at an occupied $I\times J\text{,}$ visit the required configurations in it by
<a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i). 

</div>
<div id="alg2.l11" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">11:</span></span>
              
              
              Output as in Line <a href="#alg1.l10" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">10</span></a> of <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>.

</div>
</div>
</figure>
<div id="S5.SS4.p3" class="ltx_para">
<p class="ltx_p">The next two lemmas bound the movement of these routes for any family of segments.</p>
</div>
<div id="S5.Thmtheorem9" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.9</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem9.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let a family of disjoint segments have dispersion $S_{h}$ for intervals of length $h\text{,}$ and let
$p\in(0,1]\text{.}$ For a sample with intervals of length $h$ and rate $p\text{,}$ the route of
Lines <a href="#alg2.l4" title="In Algorithm 2 ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>–<a href="#alg2.l6" title="In Algorithm 2 ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a> of <a href="#alg2" title="In 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">2</span></a> visits all required configurations and
has expected movement $O\bigl(p\,n^{2}/h+p\,h\,S_{h}+n\bigr)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS4.p4" class="ltx_para">
<p class="ltx_p">The route visits all required configurations, because every required configuration lies in a product box $I\times J$
with $J$ selected and $Q_{I,J}&gt;0\text{.}$ The first head moves at most $2n$ per selected interval on its
sweep, and the second head moves at most $2n$ between selected intervals over the whole round. In
expectation there are at most $p(n/h+1)$ selected intervals, so these moves total
$O(p\,n^{2}/h+n)\text{.}$ For an occupied $I\times J$ with $J$ selected, at most $Q_{I,J}$ required configurations lie
in $I\times J\text{,}$ so by <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) visiting them and returning takes movement
$O\bigl(h\sqrt{Q_{I,J}}\bigr)\text{,}$ because $Q_{I,J}\geq 1\text{.}$ Each $J$ is selected with probability $p\text{,}$ so by
<a href="#S5.E1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> these visits have expected total $O\bigl(p\,h\sum_{I,J}\sqrt{Q_{I,J}}\bigr)=O(p\,h\,S_{h})\text{.}$
∎</p>
</div>
</div>
<div id="S5.Thmtheorem10" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.10</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem10.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let a family of disjoint segments have dispersion $S_{h}$ for intervals of length $h\text{.}$ The route of
Line <a href="#alg2.l10" title="In Algorithm 2 ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">10</span></a> of <a href="#alg2" title="In 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">2</span></a>, run with this $h\text{,}$ visits the required configurations of the
cleanup and has movement $O\bigl(n\sqrt{S_{h}}+h\,S_{h}+n\bigr)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS4.p5" class="ltx_para">
<p class="ltx_p">By <a href="#S5.E1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>, $P\leq S_{h}\text{.}$ By <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) on the grid of $\lceil n/h\rceil^{2}$ product
boxes, the lattice path has $O\bigl(\lceil n/h\rceil\sqrt{P}+\lceil n/h\rceil\bigr)$ steps, each of
movement $O(h)\text{,}$ so it contributes $O\bigl(n\sqrt{S_{h}}+n\bigr)\text{.}$ Each occupied $I\times J$ holds at
most $Q_{I,J}$ required configurations, so by <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) visiting them and returning takes
movement $O\bigl(h\sqrt{Q_{I,J}}\bigr)\text{,}$ because $Q_{I,J}\geq 1\text{.}$ By <a href="#S5.E1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>, these visits total
$O(h\,S_{h})\text{.}$
∎</p>
</div>
</div>
<div id="S5.Thmtheorem11" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 5.11</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem11.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every fixed $r\text{,}$ an $r$-round algorithm sorts the line with expected movement
$O_{r}\bigl(n^{\beta_{r}}\bigr)$ on every input, and its output is correct for every outcome of its
coins. For $r\geq 2$ this is <a href="#alg2" title="In 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">2</span></a>.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS4.p6" class="ltx_para">
<p class="ltx_p">For $r=1\text{,}$ a serpentine route through $[n]^{2}$ visits every cell, with movement
$O(n^{2})=O(n^{\beta_{1}})\text{,}$ and it is deterministic. Let $r\geq 2\text{.}$ Correctness was shown after
<a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>. We bound the rounds in turn, writing $L_{t}$ for the movement of round $t\text{.}$ The
expectations are over the coins.</p>
</div>
<div id="S5.SS4.p7" class="ltx_para">
<p class="ltx_p">Round $1$ has movement $O(n^{\beta})\text{,}$ as noted after <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>. By <a href="#S5.Thmtheorem7" title="Lemma 5.7. ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.7</span></a>
with $s=\lceil n/b_{0}\rceil\text{,}$ its output has squared mass $A$ with $\mathbb{E}[A]\leq 3nb_{0}\text{.}$</p>
</div>
<div id="S5.SS4.p8" class="ltx_para">
<p class="ltx_p">We first bound the dispersion of the family that enters each later round: for $1\leq j\leq r-1\text{,}$ the family entering
round $j+1$ satisfies $\mathbb{E}[S_{h_{j}}]\leq 6nb_{j-1}\text{.}$ For $j=1$ this holds because $A$ is the
dispersion for intervals of length $1\text{,}$ so $S_{h_{1}}\leq 2A\text{.}$ For $j\geq 2\text{,}$ <a href="#S5.Thmtheorem8" title="Lemma 5.8. ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.8</span></a> applied
to round $j$ gives $\mathbb{E}[S_{h_{j-1}}]\leq 3n/p_{j-1}=3nb_{j-1}\text{,}$ whatever the family entering round $j\text{,}$ and
$S_{h_{j}}\leq 2S_{h_{j-1}}$ because $h_{j-1}\leq h_{j}\text{.}$</p>
</div>
<div id="S5.SS4.p9" class="ltx_para">
<p class="ltx_p">Now let $1\leq j\leq r-2\text{.}$ By <a href="#S5.Thmtheorem9" title="Lemma 5.9. ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.9</span></a>,</p>
<table id="S5.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}[L_{j+1}]=O\bigl(p_{j}n^{2}/h_{j}+p_{j}h_{j}\,nb_{j-1}+n\bigr)=O\bigl(p_{j}\,n\sqrt{nb_{j-1}}+n\bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">because $\sqrt{n/b_{j-1}}\leq h_{j}\leq 2\sqrt{n/b_{j-1}}\text{.}$ The exponent of $p_{j}\,n\sqrt{nb_{j-1}}$
is $\tfrac{3}{2}+a_{j-1}/2-a_{j}\text{,}$ which equals $\beta$ by <a href="#S2.E2" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> with $D=2\text{.}$ Hence
$\mathbb{E}[L_{j+1}]=O(n^{\beta})\text{.}$</p>
</div>
<div id="S5.SS4.p10" class="ltx_para">
<p class="ltx_p">For round $r\text{,}$ let $h=h_{r-1}\text{.}$ By <a href="#S5.Thmtheorem10" title="Lemma 5.10. ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.10</span></a> and Jensen’s inequality for the square root,</p>
<table id="S5.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}[L_{r}]=O\bigl(n\sqrt{ng}+\sqrt{n/g}\cdot ng+n\bigr)=O\bigl(n^{3/2}\sqrt{g}\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The exponent $\tfrac{3}{2}+a_{r-2}/2$ equals $\beta$ by <a href="#S2.E3" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a> with $D=2\text{.}$ Summing over the
$r$ rounds gives $\mathbb{E}[\mathrm{Move}]=O_{r}(n^{\beta})\text{.}$
∎</p>
</div>
</div>
<div id="S5.SS4.p11" class="ltx_para">
<p class="ltx_p">Together with <a href="#S4.Thmtheorem12" title="Theorem 4.12. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.12</span></a>, this gives the exact order on the line.</p>
</div>
<div id="S5.Thmtheorem12" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 5.12</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S5.Thmtheorem12.p1" class="ltx_para">
<p class="ltx_p">On the line, $\beta_{r}=1+\tfrac{1}{2}s_{r}\text{,}$ where $s_{r}=1+1/(2^{r}-1)$ is the
exponent of the worst-case number of comparisons that a deterministic algorithm needs to find the
maximum of $n$ keys, or to merge two sorted lists, in $r$ rounds <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib40" title="Parallelism in comparison problems" class="ltx_ref">Val75</a>; <a href="#bib.bib23" title="Sorting and merging in rounds" class="ltx_ref">HH82</a>]</cite>. Here $g=n^{1/(2^{r}-1)}\text{,}$ so the finest scale of <a href="#S4" title="4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a> has
$\Theta(ng)=\Theta(n^{s_{r}})$ co-blocked cells. Unless an earlier round already has expected movement $\Omega(n^{\beta_{r}})\text{,}$ with
constant probability the final round must visit a constant fraction of them, pairwise at distance
$\Omega\bigl((n/g)^{1/2}\bigr)\text{,}$ which takes movement $\Omega(n^{\beta_{r}})\text{.}$</p>
</div>
</div>
</section>
</section>
<section id="S6" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="higher-dimensions">
<span class="ltx_tag ltx_tag_section">6 </span>Higher Dimensions</h2>

<div id="S6.p1" class="ltx_para">
<p class="ltx_p">This section completes the upper-bound half of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Movement Exponent). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>. For $d\geq 2\text{,}$ the three ranges of $r$
use three kinds of refinement: none for $r\leq 2$ (<a href="#S6.SS1" title="6.1 At Most Two Rounds ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6.1</span></a>), two independent
samples in one round for $r=3$ (<a href="#S6.SS2" title="6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6.2</span></a>), and one sample for each box size of a nested
partition for $r\geq 4$ (<a href="#S6.SS3" title="6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6.3</span></a>). The section ends with the proof of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Movement Exponent). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>.</p>
</div>
<section id="S6.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="at-most-two-rounds">
<span class="ltx_tag ltx_tag_subsection">6.1 </span>At Most Two Rounds</h3>

<div id="S6.Thmtheorem1" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Proposition 6.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $d\geq 2\text{.}$ Then (i) $M_{1}^{(d)}(n)=O_{d}(n^{2})\text{,}$ attained by a deterministic algorithm, and
(ii) $M_{2}^{(d)}(n)=O_{d}\bigl(n^{\beta_{2}^{(d)}}\bigr)\text{,}$ where $\beta_{2}^{(d)}=\tfrac{6d-1}{4d-1}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS1.p1" class="ltx_para">
<p class="ltx_p">For $r=1\text{,}$ a serpentine route through $[m]^{D}$ visits every cell, with movement $O_{d}(n^{2})\text{,}$ and it
is deterministic.</p>
</div>
<div id="S6.SS1.p2" class="ltx_para">
<p class="ltx_p">For $r=2\text{,}$ we run <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a> without refinement rounds, with $b_{0}=n^{a_{0}}$ for the
exponent $a_{0}$ of <a href="#S2.Thmtheorem5" title="Lemma 2.5. ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.5</span></a> at $r=2\text{.}$ Round $1$ has movement $O(n^{\beta})\text{,}$ where
$\beta=\beta_{2}^{(d)}\text{.}$ By <a href="#S5.Thmtheorem7" title="Lemma 5.7. ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.7</span></a> with $s=\lceil n/b_{0}\rceil\text{,}$ its output has
squared mass $A$ with $\mathbb{E}[A]\leq 3nb_{0}\text{.}$ Round $2$ has at most $A$ required configurations, and they
are known, so by <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(ii) and Jensen’s inequality for the concave function
$t\mapsto t^{1-1/D}\text{,}$ its expected movement is
$O_{d}\bigl(n^{1/d}(nb_{0})^{1-1/D}+n^{1/d}\bigr)\text{.}$ The exponent
$\tfrac{1}{d}+(1+a_{0})\bigl(1-\tfrac{1}{D}\bigr)$ equals $1+a_{0}+(1-a_{0})/D\text{,}$ because $1/d=2/D\text{,}$ and this
is $\beta$ by <a href="#S2.E3" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>.
∎</p>
</div>
</div>
</section>
<section id="S6.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="two-samples-at-r3">
<span class="ltx_tag ltx_tag_subsection">6.2 </span>Two Samples at $r=3$
</h3>

<div id="S6.SS2.p1" class="ltx_para">
<p class="ltx_p">The cost of the cleanup has two parts. Its route moves along a lattice path through the occupied
product boxes $I\times J$ of two cubes of side $H\text{,}$ and inside each of them it visits the required configurations, with
movement $O_{d}\bigl(H\,Q_{I,J}^{1-1/D}+H\bigr)$ by <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i). On the line, $1-1/D=\tfrac{1}{2}\text{,}$ so by
<a href="#S5.E1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> the dispersion bounds both parts, and one sample of intervals suffices. For $d\geq 2$ the
exponent $1-1/D$ is larger, and we bound a visit by $H\,Q_{I,J}\text{,}$ whose sum over the boxes is $H$ times the squared mass. Sampling cubes controls the
dispersion, which bounds the lattice path, and sampling keys controls the squared mass, which bounds the visits, so
the refinement round does both.</p>
</div>
<div id="S6.SS2.p2" class="ltx_para">
<p class="ltx_p">We write $\mathcal{P}_{H}(G)$ and $S_{H}$ for the partition of $[m]^{d}$ into cubes of side $H\text{.}$</p>
</div>
<div id="S6.Thmtheorem2" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 6.2</span></span><span class="ltx_text ltx_font_bold"> </span>(Cube and Key Samples)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">cube sample</em> is a sample whose partition consists of the cubes of side $H\text{.}$ A <em class="ltx_emph ltx_font_italic">key
sample</em> is a sample on the partition into single positions.</p>
</div>
</div>
<div id="S6.SS2.p3" class="ltx_para">
<p class="ltx_p">Take $a_{0}&gt;a_{1}$ from <a href="#S2.Thmtheorem5" title="Lemma 2.5. ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.5</span></a> at $r=3\text{,}$ and let $b_{0}=n^{a_{0}}\text{,}$ $A_{\star}=nb_{0}\text{,}$
and $H=\lceil n^{(1-a_{0})/D}\rceil\text{.}$ Let $p=n^{-a_{1}}$ and
$\sigma=n^{-(a_{0}-a_{1})}\text{.}$ Both rates lie in $(0,1)\text{.}$ The rate $p$ serves the tour of the cleanup, since a cube
sample leaves dispersion about $n/p\text{,}$ and the rate $\sigma$ serves its visits, since a key sample leaves squared mass about
$n/\sigma\text{.}$ The minimum corner of a cube is its point
with all coordinates smallest. For the family entering round $2\text{,}$ let $P_{J}$ be the number of cubes
$I$ with $Q_{I,J}&gt;0\text{.}$</p>
</div>
<figure id="alg3" class="ltx_float ltx_float_algorithm ltx_framed ltx_framed_top">
<figcaption class="ltx_caption"><span class="ltx_tag ltx_tag_float"><span class="ltx_text ltx_font_bold">Algorithm 3</span> </span> The two-sample algorithm</figcaption>
<div class="ltx_listing ltx_listing">
<div id="alg3.l0" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"></span>
              
              
            <span class="ltx_text ltx_font_bold">Parameters:</span> $d\geq 2\text{;}$ $H\text{,}$ $p\text{,}$ and $\sigma$ as above.

</div>
<div id="alg3.l1" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">1:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">Round $1$ (splitter).</span> Lines <a href="#alg1.l1" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>–<a href="#alg1.l3" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a> of
<a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>.

</div>
<div id="alg3.l2" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">2:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">Round $2$ (refinement).</span> Draw a cube sample of side $H$ and rate $p$ and a key sample
of rate $\sigma\text{,}$ independently.

</div>
<div id="alg3.l3" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">3:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">for</span> each selected cube $J$ with $P_{J}\geq 1\text{,}$ in the serpentine order of the cubes <span class="ltx_text ltx_font_bold">do</span>




</div>
<div id="alg3.l4" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">4:</span></span>
              
              
                 Place the second head at the minimum corner of $J\text{,}$ and move the first head along the
lattice path of <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) through the cubes $I$ with $Q_{I,J}&gt;0\text{.}$

</div>
<div id="alg3.l5" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">5:</span></span>
              
              
                 On arriving at such a cube $I\text{,}$ visit the required configurations of the cube sample in $I\times J$
by <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i). Then return the second head to the minimum corner of $J$ and the first
head to its place on the path. 

</div>
<div id="alg3.l6" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">6:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">end</span> <span class="ltx_text ltx_font_bold">for</span>
</div>
<div id="alg3.l7" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">7:</span></span>
              
              
              Visit the required configurations of the key sample by <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(ii). 

</div>
<div id="alg3.l8" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">8:</span></span>
              
              
              Update the state as in Line <a href="#alg1.l7" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a> of <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>.

</div>
<div id="alg3.l9" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">9:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">Round $3$ (cleanup).</span> Move along the lattice path of <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) through the
occupied product boxes on the grid of product boxes of cubes of side $H\text{.}$ On first arrival at an
occupied $I\times J\text{,}$ visit the required configurations in it by <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i). 

</div>
<div id="alg3.l10" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">10:</span></span>
              
              
              Output as in Line <a href="#alg1.l10" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">10</span></a> of <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>.

</div>
</div>
</figure>
<div id="S6.SS2.p4" class="ltx_para">
<p class="ltx_p">The next lemma bounds the route of the cube sample for any family.</p>
</div>
<div id="S6.Thmtheorem3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 6.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let a family of disjoint segments have squared mass $A\text{,}$ let $1\leq H\leq n^{1/d}\text{,}$ and let $p\in(0,1]\text{.}$
The route of Lines <a href="#alg3.l3" title="In Algorithm 3 ‣ 6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>–<a href="#alg3.l5" title="In Algorithm 3 ‣ 6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5</span></a> of <a href="#alg3" title="In 6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">3</span></a> visits the
required configurations of a cube sample of side $H$ and rate $p\text{,}$ and its expected movement is</span></p>
<table id="S6.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$O_{d}\bigl(p\,n^{2/d}H^{-1}A^{1-1/d}+p\,H\,A+n\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS2.p5" class="ltx_para">
<p class="ltx_p">We bound in turn the moves of the second head between cubes, the paths of the first head, and the
visits inside product boxes. There are at most $(2n^{1/d}/H)^{d}=2^{d}n/H^{d}$ cubes. The second head
moves through them in serpentine order at $O_{d}(H)$ per cube, which totals
$O_{d}(n/H^{d-1})=O_{d}(n)\text{.}$</p>
</div>
<div id="S6.SS2.p6" class="ltx_para">
<p class="ltx_p">Fix a selected cube $J$ with $P_{J}\geq 1\text{.}$ By <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) on the grid of cubes, the path of
the first head has $O_{d}\bigl((n^{1/d}/H)P_{J}^{1-1/d}\bigr)$ steps, each of movement $O_{d}(H)\text{.}$
Here $P_{J}\geq 1$ absorbs the additive term, and also the $O_{d}(n^{1/d})$ movement of the first head
from the previous path to this one. So the first head moves $O_{d}\bigl(n^{1/d}P_{J}^{1-1/d}\bigr)$
for $J\text{.}$ Each $J$ is selected with probability $p\text{.}$ Moreover,
$\sum_{J}P_{J}=P\leq\sum_{G}|\mathcal{P}_{H}(G)|^{2}\leq A$ by <a href="#S5.E1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> and
$|\mathcal{P}_{H}(G)|\leq|G|\text{.}$ By the concavity of $t\mapsto t^{1-1/d}$ over the at most
$2^{d}n/H^{d}$ cubes,</p>
<table id="S6.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\sum_{J\text{ selected}}P_{J}^{1-1/d}\ \leq\ p\Bigl(\frac{2^{d}n}{H^{d}}\Bigr)^{1/d}A^{1-1/d}\ =\ 2p\,n^{1/d}H^{-1}A^{1-1/d},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">so the first head moves $O_{d}\bigl(p\,n^{2/d}H^{-1}A^{1-1/d}\bigr)$ in expectation.</p>
</div>
<div id="S6.SS2.p7" class="ltx_para">
<p class="ltx_p">Finally, for an occupied $I\times J$ with $J$ selected, at most $Q_{I,J}$ required configurations lie in
$I\times J\text{,}$ so by <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) visiting them and returning takes movement
$O_{d}\bigl(H\,Q_{I,J}^{1-1/D}+H\bigr)=O_{d}(H\,Q_{I,J})\text{,}$ because $Q_{I,J}$ is a positive integer.
Since $\sum_{I,J}Q_{I,J}=\sum_{G}|G|^{2}=A$ and each $J$ is selected with probability $p\text{,}$ these
visits have expected total $O_{d}(p\,H\,A)\text{.}$
∎</p>
</div>
</div>
<div id="S6.SS2.p8" class="ltx_para">
<p class="ltx_p">For a family of squared mass $A\text{,}$ the key sample has at most $\sigma A$ required configurations in expectation,
because each ordered pair of distinct keys in a common segment is required with probability $\sigma\text{.}$
By <a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(ii) and Jensen’s inequality,
Line <a href="#alg3.l7" title="In Algorithm 3 ‣ 6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a> of <a href="#alg3" title="In 6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">3</span></a> has expected movement
$O_{d}\bigl(n^{1/d}(\sigma A)^{1-1/D}+n^{1/d}\bigr)\text{.}$</p>
</div>
<div id="S6.Thmtheorem4" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 6.4</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every $d\geq 2\text{,}$ <a href="#alg3" title="In 6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">3</span></a> sorts with expected movement $O_{d}\bigl(n^{\beta_{3}^{(d)}}\bigr)$
on every input, and its output is correct for every outcome of its coins, where
$\beta_{3}^{(d)}=\tfrac{16d^{2}-6d+1}{12d^{2}-6d+1}\text{.}$ Hence $M_{3}^{(d)}(n)=O_{d}\bigl(n^{\beta_{3}^{(d)}}\bigr)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS2.p9" class="ltx_para">
<p class="ltx_p">Write $\beta=\beta_{3}^{(d)}\text{.}$ Correctness was shown after <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>. We bound the rounds in
turn. Round $1$ has movement $O(n^{\beta})\text{.}$ By <a href="#S5.Thmtheorem7" title="Lemma 5.7. ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.7</span></a>, its output has squared mass $A$
with $\mathbb{E}[A]\leq 3A_{\star}\text{.}$</p>
</div>
<div id="S6.SS2.p10" class="ltx_para">
<p class="ltx_p">For the cube sample in round $2\text{,}$ we take expectations in <a href="#S6.Thmtheorem3" title="Lemma 6.3. ‣ 6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.3</span></a>, using Jensen’s inequality
for $t\mapsto t^{1-1/d}\text{.}$ The value of $H$ makes the two main terms equal: since $H=\Theta\bigl(n^{(1-a_{0})/D}\bigr)\text{,}$ both are</p>
<table id="S6.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$O_{d}\bigl(p\,n^{2/d}H^{-1}A_{\star}^{1-1/d}+p\,H\,A_{\star}\bigr)=O_{d}\bigl(n^{-a_{1}+1+a_{0}+(1-a_{0})/D}\bigr)=O_{d}(n^{\beta}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where the last step is <a href="#S2.E2" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> for $j=1\text{.}$ For the key sample, $\sigma A_{\star}=n^{1+a_{1}}\text{,}$
so its expected movement is $O_{d}\bigl(n^{1/d+(1+a_{1})(1-1/D)}+n^{1/d}\bigr)\text{.}$ The exponent equals
$1+a_{1}+(1-a_{1})/D\text{,}$ which is $\beta$ by <a href="#S2.E3" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>.</p>
</div>
<div id="S6.SS2.p11" class="ltx_para">
<p class="ltx_p">For round $3\text{,}$ the output of round $2$ is obtained from the output of the cube sample by splitting
segments, so <a href="#S5.Thmtheorem8" title="Lemma 5.8. ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.8</span></a> gives $\mathbb{E}[S_{H}]\leq 3n/p\text{.}$ By <a href="#S5.E1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>, $P\leq S_{H}\text{.}$ By
<a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) on the grid of product boxes, the lattice path has
$O_{d}\bigl((n^{1/d}/H)(P^{1-1/D}+1)\bigr)$ steps, each of movement $O_{d}(H)\text{.}$ By Jensen’s
inequality, the path has expected movement $O_{d}\bigl(n^{1/d}(n/p)^{1-1/D}+n^{1/d}\bigr)\text{.}$ Since
$n/p=n^{1+a_{1}}\text{,}$ this is $O_{d}(n^{\beta})$ by the computation for the key sample. By
<a href="#S5.Thmtheorem1" title="Lemma 5.1. ‣ 5.1 Routing ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>(i) and $Q_{I,J}\geq 1\text{,}$ the visits inside the occupied product boxes take movement
$O_{d}\bigl(H\sum_{I,J}Q_{I,J}\bigr)\text{,}$ and $\sum_{I,J}Q_{I,J}$ is the squared mass of the output of round $2\text{.}$ This
output is obtained from the output of the key sample by splitting segments, so <a href="#S5.Thmtheorem8" title="Lemma 5.8. ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.8</span></a> for the partition
into single positions shows that its squared mass has expectation at most $3n/\sigma\text{.}$ Hence the visits have expected
movement $O_{d}(Hn/\sigma)=O_{d}\bigl(n^{1+(1-a_{0})/D+a_{0}-a_{1}}\bigr)=O_{d}(n^{\beta})\text{,}$ where the last step is
<a href="#S2.E2" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> for $j=1\text{.}$</p>
</div>
<div id="S6.SS2.p12" class="ltx_para">
<p class="ltx_p">Summing over the three rounds gives $\mathbb{E}[\mathrm{Move}]=O_{d}(n^{\beta})\text{.}$
∎</p>
</div>
</div>
</section>
<section id="S6.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="multiscale-refinement-for-rgeq-4">
<span class="ltx_tag ltx_tag_subsection">6.3 </span>Multiscale Refinement for $r\geq 4$
</h3>

<div id="S6.SS3.p1" class="ltx_para">
<p class="ltx_p">At $r=3$ the refinement round is followed by the cleanup, whose cost is controlled by one dispersion and
the squared mass. For $r\geq 4$ a refinement round can be followed by another one, whose route moves
at every box size (<a href="#S6.Thmtheorem6" title="Lemma 6.6. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.6</span></a>), so its cost depends on the dispersion of its input at all these sizes. So the analysis keeps an upper bound on the expected dispersion for each box size, and
the rates of each round are chosen in advance from this bound.</p>
</div>
<div id="S6.SS3.p2" class="ltx_para">
<p class="ltx_p">In this subsection $d\geq 2$ and $r\geq 4$ are fixed and $\beta=\beta_{r}^{(d)}\text{.}$ A scale here means a
spatial scale: $x$ and $y$ denote volume exponents of boxes, positions are written $u$ and $v\text{,}$ and
the rank scales enter only through the exponents $a_{j}\text{.}$ Let $c=1/d\text{,}$ and recall that $\delta=\beta-1$
and $a_{0}=1-\delta\text{.}$</p>
</div>
<div id="S6.Thmtheorem5" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 6.5</span></span><span class="ltx_text ltx_font_bold"> </span>(Scales and Samples at a Scale)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem5.p1" class="ltx_para">
<ol id="S6.I1" class="ltx_enumerate">
<li id="S6.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(1)</span> 
<div id="S6.I1.i1.p1" class="ltx_para">
<p class="ltx_p">Halving every axis $i$ times, for $0\leq i\leq\lfloor\log_{2}m\rfloor\text{,}$ partitions $[m]^{d}$
into $2^{id}$ boxes with sides $\lfloor m/2^{i}\rfloor$ and $\lceil m/2^{i}\rceil\text{.}$ Such a box
is a <em class="ltx_emph ltx_font_italic">scale-$x$ box</em>, where $n^{x}=(m/2^{i})^{d}\text{,}$ and $x$ is its <em class="ltx_emph ltx_font_italic">spatial scale</em>.
We call these $x$ <em class="ltx_emph ltx_font_italic">dyadic</em>, and also $x=0\text{,}$ whose scale-$0$ boxes are the single
positions. These partitions are nested, and a box contains at most $2^{d}$ boxes of the next
finer partition. There are $B_{x}=n^{1-x}$ scale-$x$ boxes, with sides at most $2n^{x/d}\text{,}$ and
there are $O(\log n)$ dyadic $x\text{.}$ We write $\mathcal{P}_{x}(G)$ and $S_{x}$ for the partition into
scale-$x$ boxes. Thus $S_{0}$ is the squared mass, and $S_{x}\leq\min\{S_{0},nB_{x}\}$ because
$|\mathcal{P}_{x}(G)|\leq\min\{|G|,B_{x}\}\text{.}$</p>
</div>
</li>
<li id="S6.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(2)</span> 
<div id="S6.I1.i2.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">sample at scale $y$</em> is a sample on the partition into scale-$y$ boxes. Its required
configurations are the set $W_{y}$ of pairs $(u,v)$ with $u\neq v$ and $v$ a pivot of this
sample in the segment of $u\text{.}$ For a set $W$ of configurations, $N_{x}(W)$ is the number of
product boxes of two scale-$x$ boxes that contain a configuration of $W\text{.}$ Thus
$N_{x}(W)\leq\min\{|W|,B_{x}^{2}\}\text{.}$</p>
</div>
</li>
</ol>
</div>
</div>
<div id="S6.Thmtheorem6" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 6.6</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">A set $W$ of configurations is visited by a route that starts at the current configuration and has
movement $O_{d}\bigl(n^{1/d}+\sum_{x}n^{cx}N_{x}(W)\bigr)\text{,}$ where the sum ranges over the dyadic
$x\text{.}$ The route can be computed from $W$ in polynomial time.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS3.p3" class="ltx_para">
<p class="ltx_p">The product boxes that contain a configuration of $W$ form a tree under inclusion, with the root
$[m]^{D}\text{.}$ A box has at most $2^{D}$ children, and the leaves are the single configurations of $W\text{.}$
Mark one configuration of $W$ in each node, and traverse the tree in depth-first order, moving between
marked configurations. Each edge is crossed twice. A crossing into or out of a child of a scale-$x$
node moves $O_{d}(n^{cx})\text{,}$ because both marked configurations lie in this node. So the traversal
visits every configuration of $W$ and moves $O_{d}\bigl(\sum_{x}n^{cx}N_{x}(W)\bigr)\text{,}$ and it moves
$O_{d}(n^{1/d})$ from the current configuration to the mark of the root.
∎</p>
</div>
</div>
<div id="S6.SS3.p4" class="ltx_para">
<p class="ltx_p">For the required configurations of a sample, the next lemma bounds $N_{x}$ at the coarse scales.</p>
</div>
<div id="S6.Thmtheorem7" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 6.7</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem7.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix a family of disjoint segments and draw a sample at scale $y$ with rate $p\text{.}$ For every dyadic $x\text{,}$
$\mathbb{E}\bigl[N_{x}(W_{y})\bigr]\leq p\,S_{x}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS3.p5" class="ltx_para">
<p class="ltx_p">A configuration of $W_{y}$ consists of a key of a segment $G$ and a pivot of $G\text{.}$ So a segment $G$
contributes to $N_{x}(W_{y})$ only through product boxes $I\times J$ such that $I$ meets $G$ and $J$
contains a pivot of $G\text{.}$ Let $t_{x}(G)$ be the number of scale-$x$ boxes that contain a pivot of $G\text{.}$
There are at most $|\mathcal{P}_{x}(G)|\,t_{x}(G)$ such product boxes. If $x\leq y\text{,}$ a scale-$x$ box that meets $G$ contains a pivot of $G$ exactly when the scale-$y$ box
containing it is selected, so $\mathbb{E}[t_{x}(G)]=p\,|\mathcal{P}_{x}(G)|\leq p\,|G|\text{.}$ If $x\geq y\text{,}$
a scale-$x$ box that contains a pivot of $G$ contains a selected scale-$y$ box that meets $G\text{,}$ so
$\mathbb{E}[t_{x}(G)]\leq p\,|\mathcal{P}_{y}(G)|\leq p\,|G|\text{.}$ In both cases
$\mathbb{E}\bigl[|\mathcal{P}_{x}(G)|\,t_{x}(G)\bigr]\leq p\,|G|\,|\mathcal{P}_{x}(G)|\text{,}$ and summing over
the segments gives the bound.
∎</p>
</div>
</div>
<div id="S6.SS3.p6" class="ltx_para">
<p class="ltx_p">The rate alone gives one more bound, for every family. A product box $I\times J$ contains a
configuration of $W_{y}$ only if $J$ contains a pivot. If $x\leq y\text{,}$ this requires the scale-$y$ box
containing $J$ to be selected, so $\mathbb{E}[N_{x}(W_{y})]\leq p\,B_{x}^{2}\text{.}$ If $x\geq y\text{,}$ it requires
$J$ to contain a selected scale-$y$ box, and $p\,B_{y}$ scale-$y$ boxes are selected in expectation,
so $\mathbb{E}[N_{x}(W_{y})]\leq p\,B_{x}B_{y}\text{.}$ In both cases,</p>
<table id="S6.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}[N_{x}(W_{y})]\ \leq\ p\,n^{2-x-\min\{x,y\}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(6.1)</span></td>
</tr></tbody>
</table>
</div>
<div id="S6.SS3.p7" class="ltx_para">
<p class="ltx_p">Only the scales $x\leq x_{\star}\text{,}$ where $x_{\star}=a_{0}/(2-c)\text{,}$ require control of the segments. For dyadic $x\geq x_{\star}\text{,}$
$n^{cx}B_{x}^{2}=n^{2-(2-c)x}\leq n^{2-a_{0}}=n^{\beta}\text{,}$ so each of these scales contributes at most
$n^{\beta}$ to the bound of <a href="#S6.Thmtheorem6" title="Lemma 6.6. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.6</span></a> for any set of configurations.</p>
</div>
<div id="S6.Thmtheorem8" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 6.8</span></span><span class="ltx_text ltx_font_bold"> </span>(Profiles)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem8.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">profile</em> of a random family of segments is a function $f\colon[0,x_{\star}]\to\mathbb{R}$
with $\mathbb{E}[S_{x}]\leq 3n^{1+f(x)}$ at every dyadic $x\leq x_{\star}\text{.}$ For a function $f$ on
$[0,x_{\star}]\text{,}$ let $\varphi_{f}(x)=f(x)+cx-\delta$ and
$\psi_{y}(x)=a_{0}-(1-c)x-\min\{x,y\}\text{,}$ and let</p>
<table id="S6.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(\Phi f)(y)=\sup_{0\leq x\leq x_{\star}}\ \min\bigl\{\varphi_{f}(x),\,\psi_{y}(x)\bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div id="S6.SS3.p8" class="ltx_para">
<p class="ltx_p">The functions $\varphi_{f}$ and $\psi_{y}$ give two ways to keep the contribution of a scale $x$ to the
movement of a sample at scale $y$ at $O(n^{\beta})\text{:}$ through the dispersion, with rate at most $n^{-\varphi_{f}(x)}\text{,}$ or
through the rate alone, with rate at most $n^{-\psi_{y}(x)}\text{.}$ So $n^{-(\Phi f)(y)}$ is the largest rate for
which one of the two applies at every $x\leq x_{\star}$ (<a href="#S6.Thmtheorem9" title="Lemma 6.9. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.9</span></a>).</p>
</div>
<div id="S6.SS3.p9" class="ltx_para">
<p class="ltx_p">We use two facts about $x_{\star}\text{,}$ in <a href="#S6.Thmtheorem10" title="Lemma 6.10. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.10</span></a> and <a href="#S6.Thmtheorem11" title="Theorem 6.11. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.11</span></a>. First,</p>
<table id="S6.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$a_{r-2}=\delta-c\,x_{\star}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(6.2)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">Indeed, <a href="#S2.Thmtheorem5" title="Lemma 2.5. ‣ 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.5</span></a> gives $\delta(1-q^{r})=1-q$ and $a_{r-2}=q^{r-1}\delta\text{,}$ and $c=2(1-q)$
and $2-c=2q\text{,}$ so</p>
<table id="S6.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\delta-c\,x_{\star}=\delta-\frac{c\,(1-\delta)}{2-c}=\frac{\delta-(1-q)}{q}=\frac{\delta\,q^{r}}{q}=a_{r-2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Second, $\delta\leq x_{\star}\text{.}$ This inequality is equivalent to $(1-q^{r})/(1-q)\geq 1+2q\text{,}$ which holds
for $r\geq 4$ because $q\geq\tfrac{3}{4}$ gives $q^{2}+q^{3}\geq q\text{.}$</p>
</div>
<div id="S6.SS3.p10" class="ltx_para">
<p class="ltx_p">Let $f_{0}(x)=\min\{a_{0},1-x\}$ and $f_{j}=\Phi f_{j-1}$ for $1\leq j\leq r-2\text{.}$ Thus $f_{0}$ is the bound that the
splitters and the trivial bound $S_{x}\leq n^{2-x}$ give, and $f_{j}$ is the bound that we keep after round $j+1\text{.}$ <a href="#alg4" title="In 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">4</span></a> is
the instance of <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a> that draws one sample per dyadic scale.</p>
</div>
<figure id="alg4" class="ltx_float ltx_float_algorithm ltx_framed ltx_framed_top">
<figcaption class="ltx_caption"><span class="ltx_tag ltx_tag_float"><span class="ltx_text ltx_font_bold">Algorithm 4</span> </span> The multiscale algorithm</figcaption>
<div class="ltx_listing ltx_listing">
<div id="alg4.l0" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"></span>
              
              
            <span class="ltx_text ltx_font_bold">Parameters:</span> $d\geq 2\text{;}$ $r\geq 4\text{;}$ the functions $f_{0},\dots,f_{r-2}$ as above.

</div>
<div id="alg4.l1" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">1:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">Round $1$ (splitter).</span> Lines <a href="#alg1.l1" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>–<a href="#alg1.l3" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a> of
<a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>.

</div>
<div id="alg4.l2" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">2:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">for</span> $j=1,\dots,r-2$ <span class="ltx_text ltx_font_bold">do</span>



</div>
<div id="alg4.l3" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">3:</span></span>
              
              
                 <span class="ltx_text ltx_font_bold">Round $j+1$ (refinement).</span> For every dyadic $y\leq x_{\star}\text{,}$ draw a sample at scale
$y$ with rate $n^{-f_{j}(y)}\text{,}$ independently. 

</div>
<div id="alg4.l4" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">4:</span></span>
              
              
                 For every such $y\text{,}$ visit $W_{y}$ by the route of <a href="#S6.Thmtheorem6" title="Lemma 6.6. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.6</span></a>, and join these routes end
to end. 

</div>
<div id="alg4.l5" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">5:</span></span>
              
              
                 Update the state as in Line <a href="#alg1.l7" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a> of <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>.

</div>
<div id="alg4.l6" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">6:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">end</span> <span class="ltx_text ltx_font_bold">for</span>
</div>
<div id="alg4.l7" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">7:</span></span>
              
              
              <span class="ltx_text ltx_font_bold">Round $r$ (cleanup).</span> Visit the required configurations by the route of <a href="#S6.Thmtheorem6" title="Lemma 6.6. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.6</span></a>.

</div>
<div id="alg4.l8" class="ltx_listingline">
              <span class="ltx_tag ltx_tag_listingline"><span class="ltx_text" style="font-size:80%;">8:</span></span>
              
              
              Output as in Line <a href="#alg1.l10" title="In Algorithm 1 ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">10</span></a> of <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>.

</div>
</div>
</figure>
<div id="S6.SS3.p11" class="ltx_para">
<p class="ltx_p">The next lemma is the inductive step of the analysis: it bounds the movement of one refinement round
and the profile of its output.</p>
</div>
<div id="S6.Thmtheorem9" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 6.9</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem9.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $f$ be a profile of the family entering a refinement round, and let $(\Phi f)(y)\geq 0$ at every
dyadic $y\leq x_{\star}\text{.}$ Suppose that the round draws, for every such $y\text{,}$ a sample at scale $y$ with
rate $n^{-(\Phi f)(y)}\text{,}$ independently, and visits $W_{y}$ by the route of <a href="#S6.Thmtheorem6" title="Lemma 6.6. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.6</span></a>. Then the
round has expected movement $O_{d}(n^{\beta}\log^{2}n)\text{,}$ and $\Phi f$ is a profile of its output.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS3.p12" class="ltx_para">
<p class="ltx_p">We bound the contribution of each scale to each sample, and then the profile of the output. Fix a dyadic
$y\leq x_{\star}\text{,}$ let $p=n^{-(\Phi f)(y)}\text{,}$ and fix a dyadic $x\text{.}$ We show that
$n^{cx}\,\mathbb{E}[N_{x}(W_{y})]\leq 3n^{\beta}\text{.}$ If $x\geq x_{\star}\text{,}$ this follows from
$N_{x}(W_{y})\leq B_{x}^{2}$ and $n^{cx}B_{x}^{2}\leq n^{\beta}\text{.}$ Let $x\leq x_{\star}\text{.}$ By the definition of
$\Phi\text{,}$ $p\leq n^{-\min\{\varphi_{f}(x),\psi_{y}(x)\}}\text{,}$ so $p\leq n^{-\varphi_{f}(x)}$ or
$p\leq n^{-\psi_{y}(x)}\text{.}$ In the first case, <a href="#S6.Thmtheorem7" title="Lemma 6.7. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.7</span></a> and the profile give</p>
<table id="S6.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$n^{cx}\,\mathbb{E}[N_{x}(W_{y})]\ \leq\ n^{cx}\,p\,\mathbb{E}[S_{x}]\ \leq\ 3\,n^{cx-f(x)-cx+\delta+1+f(x)}\ =\ 3n^{\beta}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">In the second case, <a href="#S6.E1" title="In 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">6.1</span></a> gives</p>
<table id="S6.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$n^{cx}\,\mathbb{E}[N_{x}(W_{y})]\ \leq\ n^{cx-a_{0}+(1-c)x+\min\{x,y\}+2-x-\min\{x,y\}}\ =\ n^{2-a_{0}}\ =\ n^{\beta}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">By <a href="#S6.Thmtheorem6" title="Lemma 6.6. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.6</span></a>, the route of this sample has expected movement
$O_{d}(n^{1/d}+n^{\beta}\log n)\text{,}$ since there are $O(\log n)$ dyadic $x\text{.}$ There are $O(\log n)$ samples,
which gives the bound on the movement.</p>
</div>
<div id="S6.SS3.p13" class="ltx_para">
<p class="ltx_p">For the output, <a href="#S5.Thmtheorem8" title="Lemma 5.8. ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.8</span></a> shows that the refined segments of the sample at scale $y$ satisfy
$\mathbb{E}[S_{y}]\leq 3n/p=3n^{1+(\Phi f)(y)}\text{,}$ whatever the entering family. The output of the round
is obtained from them by splitting segments, so it satisfies the same bound.
∎</p>
</div>
</div>
<div id="S6.SS3.p14" class="ltx_para">
<p class="ltx_p">The cleanup needs the value of $f_{r-2}$ at $x_{\star}\text{.}$ The next lemma gives it, together with the monotonicity that
carries it to smaller $x\text{.}$</p>
</div>
<div id="S6.Thmtheorem10" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 6.10</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem10.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For $1\leq j\leq r-2\text{,}$ the function $f_{j}$ is nonincreasing, $\varphi_{f_{j}}$ is nondecreasing, and
$f_{j}=a_{j}$ on $[\xi_{j},x_{\star}]\text{,}$ where $\xi_{j}=(a_{0}-a_{j})/(2-c)\text{.}$ Consequently $f_{j}\geq a_{j}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS3.p15" class="ltx_para">
<p class="ltx_p">We use induction on $j\text{.}$ For $j=1\text{,}$ recall that $\delta\leq x_{\star}\text{.}$ On $[0,\delta]$ we have $f_{0}=a_{0}\text{,}$ so
$\varphi_{f_{0}}(x)=1-2\delta+cx$ increases. On $[\delta,x_{\star}]$ we have $f_{0}(x)=1-x\text{,}$ so
$\varphi_{f_{0}}(x)=a_{0}-(1-c)x\geq\psi_{y}(x)\text{,}$ and the minimum in $\Phi$ is $\psi_{y}\text{,}$ which
decreases. So the supremum is attained on $[0,\delta]$ where $\varphi_{f_{0}}$ and $\psi_{y}$ cross. For
$y\geq\delta/2$ they cross at $x=\delta/2\text{,}$ and for $y\leq\delta/2$ they cross at $x=\delta-y\text{.}$ This gives</p>
<table id="S6.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$f_{1}(y)=\begin{cases}1-(2-c)\delta-cy&amp;\text{for }y\leq\delta/2,\\ 1-2\delta+c\delta/2&amp;\text{for }y\geq\delta/2.\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $q=1-c/2\text{,}$ the second value equals $q\,a_{0}+c/2-\delta=a_{1}\text{,}$ and hence
$\xi_{1}=\delta/2\text{.}$ The formula shows that $f_{1}$ is nonincreasing and $\varphi_{f_{1}}$ is
nondecreasing.</p>
</div>
<div id="S6.SS3.p16" class="ltx_para">
<p class="ltx_p">For the step, let $f=f_{j}\text{,}$ $a=a_{j}\text{,}$ and $\xi=\xi_{j}\text{,}$ with $j\leq r-3\text{.}$ Since $f$ is nonincreasing
and $\varphi_{f}$ is nondecreasing, $\varphi_{f}$ is $c$-Lipschitz. The function $\Phi f$ is
nonincreasing because $\psi_{y}$ decreases in $y\text{.}$ To see that $\varphi_{\Phi f}$ is nondecreasing, let
$z&gt;y\text{,}$ let $\Delta=z-y\text{,}$ and for $x\in[0,x_{\star}]$ let $x^{\prime}=\max\{x-\Delta,0\}\text{.}$ Then
$\varphi_{f}(x^{\prime})\geq\varphi_{f}(x)-c\Delta\text{.}$ Moreover $\psi_{z}(x^{\prime})\geq\psi_{y}(x)-c\Delta\text{:}$ for
$x&lt;\Delta$ we have $\psi_{z}(0)=a_{0}\geq\psi_{y}(x)\text{,}$ and for $x\geq\Delta$ this follows from
$\min\{x-\Delta,z\}\leq\min\{x,y\}+\Delta\text{.}$ Hence $(\Phi f)(z)\geq(\Phi f)(y)-c\Delta\text{,}$ which is the
claim.</p>
</div>
<div id="S6.SS3.p17" class="ltx_para">
<p class="ltx_p">For the value on the interval, let $a^{\prime}=q\,a+c/2-\delta$ and $\xi^{\prime}=(a_{0}-a^{\prime})/(2-c)\text{.}$ Since $c/2=1/D\text{,}$
<a href="#S2.E2" title="In 2.2 The Scale Schedule ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> gives $a^{\prime}=a_{j+1}\text{,}$ so $a&gt;a^{\prime}&gt;0$ and $\xi&lt;\xi^{\prime}&lt;x_{\star}\text{.}$ Thus $f(\xi^{\prime})=a\text{,}$ and a
direct computation from $a_{0}=1-\delta$ and $q+c/2=1$ gives $a+c\xi^{\prime}-\delta=a^{\prime}\text{.}$ Hence, for $y\geq\xi^{\prime}\text{,}$</p>
<table id="S6.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\varphi_{f}(\xi^{\prime})=a^{\prime}=a_{0}-(2-c)\xi^{\prime}=\psi_{y}(\xi^{\prime}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $\varphi_{f}\leq a^{\prime}$ to the left of $\xi^{\prime}$ and $\psi_{y}\leq a^{\prime}$ to the right of it, we get
$(\Phi f)(y)=a^{\prime}$ for $y\in[\xi^{\prime},x_{\star}]\text{.}$</p>
</div>
<div id="S6.SS3.p18" class="ltx_para">
<p class="ltx_p">Finally, $f_{j}\geq f_{j}(x_{\star})=a_{j}$ because $f_{j}$ is nonincreasing.
∎</p>
</div>
</div>
<div id="S6.SS3.p19" class="ltx_para">
<p class="ltx_p">Since $f_{j}\geq a_{j}&gt;0\text{,}$ the rates of <a href="#alg4" title="In 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">4</span></a> lie in $(0,1)\text{,}$ and <a href="#S6.Thmtheorem9" title="Lemma 6.9. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.9</span></a>
applies to round $j+1$ with $f=f_{j-1}\text{.}$</p>
</div>
<div id="S6.Thmtheorem11" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 6.11</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem11.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every fixed $d\geq 2$ and $r\geq 4\text{,}$ <a href="#alg4" title="In 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">4</span></a> sorts with expected movement
$O_{d,r}\bigl(n^{\beta_{r}^{(d)}}\log^{2}n\bigr)$ on every input, and its output is correct for every
outcome of its coins. Hence $M_{r}^{(d)}(n)=O_{d,r}\bigl(n^{\beta_{r}^{(d)}}\log^{2}n\bigr)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS3.p20" class="ltx_para">
<p class="ltx_p">Correctness was shown after <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>. We bound the rounds in turn. Round $1$ has movement
$O(n^{\beta})\text{.}$ By <a href="#S5.Thmtheorem7" title="Lemma 5.7. ‣ 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.7</span></a> with $s=\lceil n/b_{0}\rceil\text{,}$ its output satisfies
$\mathbb{E}[S_{0}]\leq 3nb_{0}=3n^{1+a_{0}}\text{.}$ Since $S_{x}\leq S_{0}$ and $S_{x}\leq n^{2-x}\text{,}$ the function
$f_{0}$ is a profile of this family.</p>
</div>
<div id="S6.SS3.p21" class="ltx_para">
<p class="ltx_p">By <a href="#S6.Thmtheorem9" title="Lemma 6.9. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemmas</span> <span class="ltx_text ltx_ref_tag">6.9</span></a> and <a href="#S6.Thmtheorem10" title="Lemma 6.10. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.10</span></a>, for $1\leq j\leq r-2\text{,}$ round $j+1$ has expected movement
$O_{d}(n^{\beta}\log^{2}n)\text{,}$ and $f_{j}$ is a profile of its output.</p>
</div>
<div id="S6.SS3.p22" class="ltx_para">
<p class="ltx_p">It remains to bound the cleanup, whose required configurations we call $W\text{.}$ At a dyadic $x\text{,}$ a product box of
two scale-$x$ boxes contains a configuration of $W$ only if a segment meets both boxes, so
$N_{x}(W)\leq\sum_{G}|\mathcal{P}_{x}(G)|^{2}\leq S_{x}\text{.}$ Also $N_{x}(W)\leq B_{x}^{2}\text{.}$ Let $x\leq x_{\star}\text{.}$
Since $\varphi_{f_{r-2}}$ is nondecreasing and $f_{r-2}(x_{\star})=a_{r-2}\text{,}$ <a href="#S6.E2" title="In 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">6.2</span></a> gives</p>
<table id="S6.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\varphi_{f_{r-2}}(x)\ \leq\ \varphi_{f_{r-2}}(x_{\star})\ =\ a_{r-2}+c\,x_{\star}-\delta\ =\ 0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">That is, $cx+f_{r-2}(x)\leq\delta\text{,}$ so $n^{cx}\,\mathbb{E}[S_{x}]\leq 3n^{cx+1+f_{r-2}(x)}\leq 3n^{\beta}\text{.}$
For $x\geq x_{\star}\text{,}$ we have $n^{cx}B_{x}^{2}\leq n^{\beta}\text{.}$ By <a href="#S6.Thmtheorem6" title="Lemma 6.6. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.6</span></a>, the cleanup has
expected movement $O_{d}(n^{\beta}\log n)\text{,}$ since there are $O(\log n)$ dyadic $x\text{.}$</p>
</div>
<div id="S6.SS3.p23" class="ltx_para">
<p class="ltx_p">Summing over the $r$ rounds gives $\mathbb{E}[\mathrm{Move}]=O_{d,r}(n^{\beta}\log^{2}n)\text{.}$
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Movement Exponent). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>.</h6>
<div id="S6.SS3.p24" class="ltx_para">
<p class="ltx_p">For finite $r\text{,}$ the lower bound is <a href="#S4.Thmtheorem1" title="Theorem 4.1 (Lower Bound). ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>. For the upper bounds, <a href="#S5.Thmtheorem11" title="Theorem 5.11. ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">5.11</span></a> treats $d=1\text{.}$ For
$d\geq 2\text{,}$ <a href="#S6.Thmtheorem1" title="Proposition 6.1. ‣ 6.1 At Most Two Rounds ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">6.1</span></a> treats $r\leq 2\text{,}$ <a href="#S6.Thmtheorem4" title="Theorem 6.4. ‣ 6.2 Two Samples at 𝑟=3 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.4</span></a> treats $r=3\text{,}$ and <a href="#S6.Thmtheorem11" title="Theorem 6.11. ‣ 6.3 Multiscale Refinement for 𝑟≥4 ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.11</span></a> treats
$r\geq 4\text{.}$ These algorithms are explicit and run in polynomial time. Those for $r=1$ are deterministic routes, and
the others are instances of <a href="#alg1" title="In 5.3 The Sampling Algorithm ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Algorithm</span> <span class="ltx_text ltx_ref_tag">1</span></a>. This gives $M_{r}^{(d)}(n)=\widetilde{\Theta}\bigl(n^{\beta_{r}^{(d)}}\bigr)$ for
finite $r\text{.}$ For $r=\infty\text{,}$ <a href="#S4.Thmtheorem5" title="Proposition 4.5. ‣ 4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Propositions</span> <span class="ltx_text ltx_ref_tag">4.5</span></a> and <a href="#S5.Thmtheorem3" title="Proposition 5.3. ‣ 5.2 The Fully Adaptive Bound ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.3</span></a> give $M_{\infty}^{(d)}(n)=\Theta_{d}\bigl(n^{1+1/(2d)}\bigr)\text{,}$
and the algorithm of <a href="#S5.Thmtheorem3" title="Proposition 5.3. ‣ 5.2 The Fully Adaptive Bound ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">5.3</span></a> is deterministic, explicit, and runs in polynomial time. The order is exact on the line by
<a href="#S4.Thmtheorem12" title="Theorem 4.12. ‣ 4.4 Exact Order on the Line ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorems</span> <span class="ltx_text ltx_ref_tag">4.12</span></a> and <a href="#S5.Thmtheorem11" title="Theorem 5.11. ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.11</span></a> and for $r\leq 2$ by <a href="#S4.Thmtheorem4" title="Proposition 4.4. ‣ 4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">4.4</span></a> together with
<a href="#S5.Thmtheorem11" title="Theorem 5.11. ‣ 5.4 The Upper Bound on the Line ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorems</span> <span class="ltx_text ltx_ref_tag">5.11</span></a> and <a href="#S6.Thmtheorem1" title="Proposition 6.1. ‣ 6.1 At Most Two Rounds ‣ 6 Higher Dimensions ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.1</span></a>.
∎</p>
</div>
</div>
</section>
</section>
<section id="S7" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="multiple-heads">
<span class="ltx_tag ltx_tag_section">7 </span>Multiple Heads</h2>

<div id="S7.p1" class="ltx_para">
<p class="ltx_p">So far the model has two heads. With $k\geq 2$ heads on $[m]^{d}\text{,}$ a configuration is a point of
$([m]^{d})^{k}\text{,}$ a route is a sequence of configurations at consecutive $\ell_{1}$ distance $1\text{,}$ and the
outcome at a configuration is the rank order of the distinct keys under the heads. Rounds, correctness,
and the complexity $M_{r}^{(k,d)}(n)$ are defined as in <a href="#S2.Thmtheorem1" title="Definition 2.1 (The Movement Model). ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Definition</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, so $M_{r}^{(2,d)}=M_{r}^{(d)}\text{.}$ Extra heads
can only help: an algorithm may leave them at the start and ignore what they read, so
$M_{r}^{(k,d)}\leq M_{r}^{(d)}\text{.}$</p>
</div>
<div id="S7.p2" class="ltx_para">
<p class="ltx_p">A fixed number of heads nevertheless changes the complexity by at most a constant factor. Two keys are
compared at every configuration that places two heads on them. So all that a $k$-head algorithm learns is read along the
$\binom{k}{2}$ projections of its route to pairs of heads, and each projection, with consecutive repetitions deleted, is a route in the same comparison grid $[m]^{D}\text{.}$</p>
</div>
<div id="S7.Thmtheorem1" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Proposition 7.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every fixed $k\geq 2$ and $d\text{,}$ and every $r\in\{1,2,\dots\}\cup\{\infty\}\text{,}$
$M_{r}^{(k,d)}(n)=\Theta_{d,r,k}\bigl(M_{r}^{(d)}(n)\bigr)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S7.p3" class="ltx_para">
<p class="ltx_p">The upper bound on $M_{r}^{(k,d)}$ was shown above. For the lower bound, a two-head algorithm simulates a given $k$-head
algorithm one pair of heads at a time when $r$ is finite, and for $r=\infty$ we bound the movement
directly. Let $r$ be finite. A round of the $k$-head algorithm commits a route $z_{0},\dots,z_{L}\text{.}$ Let $L^{(i)}$ be the movement of head $i$ on this route, so that
$L=\sum_{i}L^{(i)}\text{.}$ For a pair $i&lt;j\text{,}$ let $R_{ij}$ be the sequence of positions of heads $i$ and $j$
along the route, with consecutive repetitions deleted. It is a route in $[m]^{D}$ of movement at most
$L^{(i)}+L^{(j)}\text{.}$ In one round of its own, the simulator runs the routes $R_{ij}$ in turn. These runs
have total movement at most $\sum_{i&lt;j}(L^{(i)}+L^{(j)})=(k-1)L\text{,}$ because each head lies in $k-1$
pairs. The moves from one run to the next add $O_{d,k}(n^{1/d})$ per round. The pairwise outcomes
determine the rank order of the keys under the heads at every configuration of the route, so the
simulator knows all outcomes of the round and can compute the next route. Hence</p>
<table id="S7.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$M_{r}^{(d)}(n)\ \leq\ (k-1)\,M_{r}^{(k,d)}(n)+O_{d,r,k}\bigl(n^{1/d}\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $M_{r}^{(d)}(n)=\Omega_{d}\bigl(n^{1+1/(2d)}\bigr)$ by <a href="#S4.Thmtheorem5" title="Proposition 4.5. ‣ 4.2 Two Rounds and the Fully Adaptive Bound ‣ 4 The Lower Bound ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">4.5</span></a> and $1+1/(2d)&gt;1/d\text{,}$ the
additive term is $o\bigl(M_{r}^{(d)}(n)\bigr)\text{,}$ and the proposition follows.</p>
</div>
<div id="S7.p4" class="ltx_para">
<p class="ltx_p">The simulation adds a term in every round, so for $r=\infty$ we argue directly and bound the movement
of an algorithm with any finite number of rounds. By Yao’s principle, fix a deterministic $k$-head
algorithm that is correct on every input, and let the input be uniform. Let $\rho=\Theta_{d}(n^{1/(2d)})$ be
the radius of <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> at scale $2\text{,}$ whose cells join the ranks $2i-1$ and $2i\text{.}$ With probability at least $7/8\text{,}$ there is a set
$W\subseteq\mathcal{C}_{2}$ of at least $\tfrac{1}{2}\lfloor n/2\rfloor$ cells that are pairwise more than
$\rho$ apart. For every cell $\{u,v\}$ of $W\text{,}$ some configuration of the execution places two heads on
$u$ and $v\text{.}$ Otherwise, exchanging their two consecutive ranks changes no outcome, so the algorithm gives
the same output on two inputs with different orders. For a pair $i&lt;j\text{,}$ let $W_{ij}\subseteq W$ be the set
of cells that heads $i$ and $j$ visit together, and let $\widehat{L}^{(i)}$ be the total movement of head
$i\text{.}$ By <a href="#S2.Thmtheorem3" title="Observation 2.3. ‣ 2.1 The Model ‣ 2 Preliminaries ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Observation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(b), the positions of heads $i$ and $j$ over the whole execution, with
consecutive repetitions and diagonal configurations deleted, form a sequence of cells of $\operatorname{dist}$-length at
most $\widehat{L}^{(i)}+\widehat{L}^{(j)}\text{.}$ By <a href="#S3.Thmtheorem2" title="Fact 3.2. ‣ 3 Geometry of the Comparison Grid ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>, if $|W_{ij}|\geq 2\text{,}$ then
$\widehat{L}^{(i)}+\widehat{L}^{(j)}\geq\tfrac{1}{2}|W_{ij}|\rho\text{.}$ Summing over the pairs, and noting that the
pairs with $|W_{ij}|\leq 1$ cover at most $\binom{k}{2}$ cells, gives</p>
<table id="S7.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(k-1)\,\mathrm{Move}\ =\ \sum_{i&lt;j}\bigl(\widehat{L}^{(i)}+\widehat{L}^{(j)}\bigr)\ \geq\ \frac{\rho}{2}\Bigl(\frac{1}{2}\Bigl\lfloor\frac{n}{2}\Bigr\rfloor-\binom{k}{2}\Bigr)$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">on this event. Hence $\mathbb{E}[\mathrm{Move}]=\Omega_{d,k}\bigl(n^{1+1/(2d)}\bigr)\text{,}$ with a constant
that does not depend on the number of rounds, so
$M_{\infty}^{(k,d)}(n)=\Omega_{d,k}\bigl(n^{1+1/(2d)}\bigr)\text{.}$ With <a href="#S5.Thmtheorem3" title="Proposition 5.3. ‣ 5.2 The Fully Adaptive Bound ‣ 5 Routing and the Sampling Algorithm ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">5.3</span></a>, this is
$\Omega_{d,k}\bigl(M_{\infty}^{(d)}(n)\bigr)\text{.}$
∎</p>
</div>
</div>
</section>
<section id="S8" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="discussion">
<span class="ltx_tag ltx_tag_section">8 </span>Discussion</h2>

<div id="S8.p1" class="ltx_para">
<p class="ltx_p"><a href="#S1.Thmtheorem1" title="Theorem 1.1 (Movement Exponent). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> determines the movement exponent for all $d$ and $r\text{.}$ The order is exact on the line, for $r\leq 2\text{,}$ and for
$r=\infty\text{.}$ In the interior $d\geq 2\text{,}$ $3\leq r&lt;\infty\text{,}$ the two bounds differ by a factor $O_{d,r}(\log^{3}n)\text{,}$ and this gap is the one
question <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Movement Exponent). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Movement Complexity of Sorting" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> leaves open. The lower bound loses a factor $\log n$ throughout the interior, and the upper bound loses a
factor $\log^{2}n$ for $r\geq 4$ and nothing at $r=3\text{.}$ We conjecture that both losses can be removed.</p>
</div>
<div id="S8.Thmtheorem1" class="ltx_theorem ltx_theorem_conjecture">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Conjecture 8.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S8.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every $d\geq 2$ and $3\leq r&lt;\infty\text{,}$ $M_{r}^{(d)}(n)=\Theta_{d,r}\bigl(n^{\beta_{r}^{(d)}}\bigr)\text{.}$</span></p>
</div>
</div>
</section>
<section id="Sx1" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="ai-methodology-statement">AI Methodology Statement</h2>

<div id="Sx1.p1" class="ltx_para">
<p class="ltx_p">The author used OpenAI’s ChatGPT in Codex and Anthropic’s Claude in Claude Code to help organize and polish the
exposition of this paper, based on the author’s own drafts. The same tools assisted in surveying the related
literature, in understanding the current state of research in this area and its gaps, and in flagging possible
errors in draft proofs. The author formulated and proved all mathematical claims in this paper, and checked,
revised, and finalized every statement, proof, and reference. The author takes full responsibility for the
content of the submission.</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography" id="references">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bib1" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[AA88]</span>
<span class="ltx_bibblock">
Noga Alon and Yossi Azar.

</span>
<span class="ltx_bibblock">Sorting, approximate sorting, and searching in rounds.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">SIAM Journal on Discrete Mathematics</span>, 1(3):269–280, 1988.

</span>
</li>
      
<li id="bib.bib2" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[AAV86]</span>
<span class="ltx_bibblock">
Noga Alon, Yossi Azar, and Uzi Vishkin.

</span>
<span class="ltx_bibblock">Tight complexity bounds for parallel comparison sorting.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">27th Annual Symposium on Foundations of Computer Science
(FOCS)</span>, pages 502–510, 1986.

</span>
</li>
      
<li id="bib.bib3" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[AV88]</span>
<span class="ltx_bibblock">
Alok Aggarwal and Jeffrey Scott Vitter.

</span>
<span class="ltx_bibblock">The input/output complexity of sorting and related problems.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Communications of the ACM</span>, 31(9):1116–1127, 1988.

</span>
</li>
      
<li id="bib.bib4" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[BABP03]</span>
<span class="ltx_bibblock">
Amir M. Ben-Amram, Omer Berkman, and Holger Petersen.

</span>
<span class="ltx_bibblock">Element distinctness on one-tape Turing machines: a complete
solution.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Acta Informatica</span>, 40(2):81–94, 2003.

</span>
</li>
      
<li id="bib.bib5" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[BB90]</span>
<span class="ltx_bibblock">
Béla Bollobás and Graham Brightwell.

</span>
<span class="ltx_bibblock">Parallel selection with high probability.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">SIAM Journal on Discrete Mathematics</span>, 3(1):21–31, 1990.

</span>
</li>
      
<li id="bib.bib6" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[BC82]</span>
<span class="ltx_bibblock">
Allan Borodin and Stephen A. Cook.

</span>
<span class="ltx_bibblock">A time-space tradeoff for sorting on a general sequential model of
computation.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">SIAM Journal on Computing</span>, 11(2):287–297, 1982.

</span>
</li>
      
<li id="bib.bib7" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Bea91]</span>
<span class="ltx_bibblock">
Paul Beame.

</span>
<span class="ltx_bibblock">A general sequential time-space tradeoff for finding unique elements.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">SIAM Journal on Computing</span>, 20(2):270–277, 1991.

</span>
</li>
      
<li id="bib.bib8" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[BG89]</span>
<span class="ltx_bibblock">
Dimitris Bertsimas and Michelangelo Grigni.

</span>
<span class="ltx_bibblock">Worst-case examples for the spacefilling curve heuristic for the
Euclidean traveling salesman problem.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Operations Research Letters</span>, 8(5):241–244, 1989.

</span>
</li>
      
<li id="bib.bib9" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[BHH59]</span>
<span class="ltx_bibblock">
J. Beardwood, J. H. Halton, and J. M. Hammersley.

</span>
<span class="ltx_bibblock">The shortest path through many points.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Mathematical Proceedings of the Cambridge Philosophical
Society</span>, 55(4):299–327, 1959.

</span>
</li>
      
<li id="bib.bib10" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[BMP19]</span>
<span class="ltx_bibblock">
Mark Braverman, Jieming Mao, and Yuval Peres.

</span>
<span class="ltx_bibblock">Sorted top-$k$ in rounds.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">32nd Annual Conference on Learning Theory (COLT)</span>, volume 99
of <span class="ltx_text ltx_font_italic">Proceedings of Machine Learning Research</span>, pages 342–382, 2019.

</span>
</li>
      
<li id="bib.bib11" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[BR16]</span>
<span class="ltx_bibblock">
Indranil Banerjee and Dana Richards.

</span>
<span class="ltx_bibblock">Sorting under forbidden comparisons.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">15th Scandinavian Symposium and Workshops on Algorithm Theory
(SWAT)</span>, volume 53 of <span class="ltx_text ltx_font_italic">LIPIcs</span>, pages 22:1–22:13, 2016.

</span>
<span class="ltx_bibblock">arXiv:1508.03698.

</span>
</li>
      
<li id="bib.bib12" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[BT83]</span>
<span class="ltx_bibblock">
Béla Bollobás and Andrew Thomason.

</span>
<span class="ltx_bibblock">Parallel sorting.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Discrete Applied Mathematics</span>, 6(1):1–11, 1983.

</span>
</li>
      
<li id="bib.bib13" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[CFG<sup class="ltx_sup">+</sup>02]</span>
<span class="ltx_bibblock">
Moses Charikar, Ronald Fagin, Venkatesan Guruswami, Jon Kleinberg, Prabhakar
Raghavan, and Amit Sahai.

</span>
<span class="ltx_bibblock">Query strategies for priced information.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Journal of Computer and System Sciences</span>, 64(4):785–819, 2002.

</span>
</li>
      
<li id="bib.bib14" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[DMS91]</span>
<span class="ltx_bibblock">
Martin Dietzfelbinger, Wolfgang Maass, and Georg Schnitger.

</span>
<span class="ltx_bibblock">The complexity of matrix transposition on one-tape off-line Turing
machines.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Theoretical Computer Science</span>, 82(1):113–129, 1991.

</span>
</li>
      
<li id="bib.bib15" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Few55]</span>
<span class="ltx_bibblock">
L. Few.

</span>
<span class="ltx_bibblock">The shortest path and the shortest road through $n$ points.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Mathematika</span>, 2(2):141–144, 1955.

</span>
</li>
      
<li id="bib.bib16" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[FHLS19]</span>
<span class="ltx_bibblock">
Alireza Farhadi, MohammadTaghi Hajiaghayi, Kasper Green Larsen, and Elaine Shi.

</span>
<span class="ltx_bibblock">Lower bounds for external memory integer sorting via network coding.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">51st Annual ACM Symposium on Theory of Computing (STOC)</span>,
pages 997–1008, 2019.

</span>
<span class="ltx_bibblock">arXiv:1811.01313.

</span>
</li>
      
<li id="bib.bib17" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Fil24]</span>
<span class="ltx_bibblock">
Arnold Filtser.

</span>
<span class="ltx_bibblock">Scattering and sparse partitions, and their applications.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">ACM Transactions on Algorithms</span>, 20(4):1–42, 2024.

</span>
<span class="ltx_bibblock">arXiv:2001.04447.

</span>
</li>
      
<li id="bib.bib18" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[FS89]</span>
<span class="ltx_bibblock">
Michael L. Fredman and Michael E. Saks.

</span>
<span class="ltx_bibblock">The cell probe complexity of dynamic data structures.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">21st Annual ACM Symposium on Theory of Computing (STOC)</span>,
pages 345–354, 1989.

</span>
</li>
      
<li id="bib.bib19" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[GHR06]</span>
<span class="ltx_bibblock">
Anupam Gupta, Mohammad T. Hajiaghayi, and Harald Räcke.

</span>
<span class="ltx_bibblock">Oblivious network design.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">17th Annual ACM-SIAM Symposium on Discrete Algorithms
(SODA)</span>, pages 970–979, 2006.

</span>
</li>
      
<li id="bib.bib20" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[GJ24]</span>
<span class="ltx_bibblock">
Mayank Goswami and Riko Jacob.

</span>
<span class="ltx_bibblock">An algorithm for bichromatic sorting with polylog competitive ratio.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">15th Innovations in Theoretical Computer Science Conference
(ITCS)</span>, volume 287 of <span class="ltx_text ltx_font_italic">LIPIcs</span>, pages 56:1–56:17, 2024.

</span>
</li>
      
<li id="bib.bib21" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[GK01]</span>
<span class="ltx_bibblock">
Anupam Gupta and Amit Kumar.

</span>
<span class="ltx_bibblock">Sorting and selection with structured costs.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">42nd Annual Symposium on Foundations of Computer Science
(FOCS)</span>, pages 416–425, 2001.

</span>
</li>
      
<li id="bib.bib22" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[GK05]</span>
<span class="ltx_bibblock">
Anupam Gupta and Amit Kumar.

</span>
<span class="ltx_bibblock">Where’s the winner? Max-finding and sorting with metric costs.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Approximation, Randomization and Combinatorial Optimization
(APPROX/RANDOM)</span>, volume 3624 of <span class="ltx_text ltx_font_italic">Lecture Notes in Computer Science</span>,
pages 74–85. Springer, 2005.

</span>
</li>
      
<li id="bib.bib23" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[HH82]</span>
<span class="ltx_bibblock">
Roland Häggkvist and Pavol Hell.

</span>
<span class="ltx_bibblock">Sorting and merging in rounds.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">SIAM Journal on Algebraic and Discrete Methods</span>, 3(4):465–473,
1982.

</span>
</li>
      
<li id="bib.bib24" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[HKK11]</span>
<span class="ltx_bibblock">
Zhiyi Huang, Sampath Kannan, and Sanjeev Khanna.

</span>
<span class="ltx_bibblock">Algorithms for the generalized sorting problem.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">52nd Annual Symposium on Foundations of Computer Science
(FOCS)</span>, pages 738–747, 2011.

</span>
</li>
      
<li id="bib.bib25" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[HKL06]</span>
<span class="ltx_bibblock">
Mohammad Taghi Hajiaghayi, Robert D. Kleinberg, and Frank Thomson Leighton.

</span>
<span class="ltx_bibblock">Improved lower and upper bounds for universal TSP in planar
metrics.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">17th Annual ACM-SIAM Symposium on Discrete Algorithms
(SODA)</span>, pages 649–658, 2006.

</span>
</li>
      
<li id="bib.bib26" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Jai88]</span>
<span class="ltx_bibblock">
Patrick Jaillet.

</span>
<span class="ltx_bibblock">A priori solution of a traveling salesman problem in which a random
subset of the customers are visited.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Operations Research</span>, 36(6):929–936, 1988.

</span>
</li>
      
<li id="bib.bib27" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[JLN<sup class="ltx_sup">+</sup>05]</span>
<span class="ltx_bibblock">
Lujun Jia, Guolong Lin, Guevara Noubir, Rajmohan Rajaraman, and Ravi Sundaram.

</span>
<span class="ltx_bibblock">Universal approximations for TSP, Steiner tree, and set cover.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">37th Annual ACM Symposium on Theory of Computing (STOC)</span>,
pages 386–395, 2005.

</span>
</li>
      
<li id="bib.bib28" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[KN21]</span>
<span class="ltx_bibblock">
William Kuszmaul and Shyam Narayanan.

</span>
<span class="ltx_bibblock">Stochastic and worst-case generalized sorting revisited.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">62nd Annual Symposium on Foundations of Computer Science
(FOCS)</span>, pages 1056–1067, 2021.

</span>
<span class="ltx_bibblock">arXiv:2111.07222.

</span>
</li>
      
<li id="bib.bib29" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Kra26]</span>
<span class="ltx_bibblock">
Cosmas Kravaris.

</span>
<span class="ltx_bibblock">Lower bounds for the universal TSP on the plane.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">2026 Annual ACM-SIAM Symposium on Discrete Algorithms
(SODA)</span>, pages 1–9, 2026.

</span>
<span class="ltx_bibblock">arXiv:2412.16448.

</span>
</li>
      
<li id="bib.bib30" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[LL04]</span>
<span class="ltx_bibblock">
Zongpeng Li and Baochun Li.

</span>
<span class="ltx_bibblock">Network coding: the case of multiple unicast sessions.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">42nd Allerton Conference on Communication, Control, and
Computing</span>, 2004.

</span>
</li>
      
<li id="bib.bib31" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[LO94]</span>
<span class="ltx_bibblock">
Alejandro López-Ortiz.

</span>
<span class="ltx_bibblock">New lower bounds for element distinctness on a one-tape Turing
machine.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Information Processing Letters</span>, 51(6):311–314, 1994.

</span>
</li>
      
<li id="bib.bib32" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[MNSW98]</span>
<span class="ltx_bibblock">
Peter Bro Miltersen, Noam Nisan, Shmuel Safra, and Avi Wigderson.

</span>
<span class="ltx_bibblock">On data structures and asymmetric communication complexity.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Journal of Computer and System Sciences</span>, 57(1):37–49, 1998.

</span>
</li>
      
<li id="bib.bib33" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[MS86]</span>
<span class="ltx_bibblock">
Wolfgang Maass and Georg Schnitger.

</span>
<span class="ltx_bibblock">An optimal lower bound for Turing machines with one work tape and a
two-way input tape.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Structure in Complexity Theory</span>, volume 223 of <span class="ltx_text ltx_font_italic">Lecture
Notes in Computer Science</span>, pages 249–264. Springer, 1986.

</span>
</li>
      
<li id="bib.bib34" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[PB89]</span>
<span class="ltx_bibblock">
Loren K. Platzman and John J. Bartholdi.

</span>
<span class="ltx_bibblock">Spacefilling curves and the planar travelling salesman problem.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Journal of the ACM</span>, 36(4):719–737, 1989.

</span>
</li>
      
<li id="bib.bib35" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Pet08]</span>
<span class="ltx_bibblock">
Holger Petersen.

</span>
<span class="ltx_bibblock">Element distinctness and sorting on one-tape off-line Turing
machines.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">34th Conference on Current Trends in Theory and Practice of
Computer Science (SOFSEM)</span>, volume 4910 of <span class="ltx_text ltx_font_italic">Lecture Notes in Computer
Science</span>, pages 406–417. Springer, 2008.

</span>
</li>
      
<li id="bib.bib36" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Pip87]</span>
<span class="ltx_bibblock">
Nicholas Pippenger.

</span>
<span class="ltx_bibblock">Sorting and selecting in rounds.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">SIAM Journal on Computing</span>, 16(6):1032–1038, 1987.

</span>
</li>
      
<li id="bib.bib37" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Ste81]</span>
<span class="ltx_bibblock">
J. Michael Steele.

</span>
<span class="ltx_bibblock">Subadditive Euclidean functionals and nonlinear growth in geometric
probability.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">The Annals of Probability</span>, 9(3):365–376, 1981.

</span>
</li>
      
<li id="bib.bib38" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Tho83]</span>
<span class="ltx_bibblock">
Clark D. Thompson.

</span>
<span class="ltx_bibblock">The VLSI complexity of sorting.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">IEEE Transactions on Computers</span>, C-32(12):1171–1184, 1983.

</span>
</li>
      
<li id="bib.bib39" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[TK77]</span>
<span class="ltx_bibblock">
C. D. Thompson and H. T. Kung.

</span>
<span class="ltx_bibblock">Sorting on a mesh-connected parallel computer.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Communications of the ACM</span>, 20(4):263–271, 1977.

</span>
</li>
      
<li id="bib.bib40" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Val75]</span>
<span class="ltx_bibblock">
Leslie G. Valiant.

</span>
<span class="ltx_bibblock">Parallelism in comparison problems.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">SIAM Journal on Computing</span>, 4(3):348–355, 1975.

</span>
</li>
      
<li id="bib.bib41" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Yao77]</span>
<span class="ltx_bibblock">
Andrew Chi-Chih Yao.

</span>
<span class="ltx_bibblock">Probabilistic computations: toward a unified measure of complexity.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">18th Annual Symposium on Foundations of Computer Science
(FOCS)</span>, pages 222–227, 1977.

</span>
</li>
      
<li id="bib.bib42" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[YDI<sup class="ltx_sup">+</sup>15]</span>
<span class="ltx_bibblock">
Katsuhisa Yamanaka, Erik D. Demaine, Takehiro Ito, Jun Kawahara, Masashi
Kiyomi, Yoshio Okamoto, Toshiki Saitoh, Akira Suzuki, Kei Uchizawa, and
Takeaki Uno.

</span>
<span class="ltx_bibblock">Swapping labeled tokens on graphs.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Theoretical Computer Science</span>, 586:81–94, 2015.

</span>
</li>
      
<li id="bib.bib43" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">[Yuk98]</span>
<span class="ltx_bibblock">
Joseph E. Yukich.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Probability Theory of Classical Euclidean Optimization
Problems</span>, volume 1675 of <span class="ltx_text ltx_font_italic">Lecture Notes in Mathematics</span>.

</span>
<span class="ltx_bibblock">Springer, 1998.

</span>
</li>
    
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Sichen Wang"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="The Movement Complexity of Sorting"></div>

</article>
