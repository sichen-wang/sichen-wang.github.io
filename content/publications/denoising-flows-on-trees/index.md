---
title: "The Minimax Rate of Denoising Flows on Trees"

authors:
  - me

# arXiv v1 submission date.
date: 2026-09-12

publication_types: ["manuscript"]
publication: "*Preprint*, arXiv:2609.14091"
publication_short: "Preprint"

abstract: |
  Isotonic regression and mean estimation over a simplex are among the most classical
  denoising problems under geometric constraints. Chatterjee and Lafferty generalized
  both to the recovery of a flow on a rooted tree from Gaussian noise, with isotonic
  regression on a path and the simplex on a star. Their results reach only special
  trees; on a general tree the minimax risk remained unknown for a decade. We settle
  the question in full. On every tree with $n$ vertices, at every budget $V$ and noise
  level $\sigma$, the minimax risk is of order $\min\{V^2H_T,\ \sigma^2k_0\}$, with
  $H_T$ the diameter and $k_0$ the crossing index of a truncated ancestor profile. A
  deterministic estimator, an exponentially weighted aggregate over integer states,
  attains it in $O(n^2\log(n+1))$ arithmetic operations. Least squares at a known
  budget, the natural convex program for the model, is suboptimal in the worst case by
  a factor of order $(\log n)^{2/5}$. One functional, the truncated ancestor profile,
  carries the rate, the estimator, and the least squares comparison. It serves as
  covering radius, as packing entropy in the positive cone, and as the range of the
  one-dimensional state behind the exact computation. Two classical theories become
  one on trees, sharp and computable throughout.

tags:
  - Minimax Estimation
  - Shape-Constrained Inference
  - Tree Flows

featured: false

links:
  - type: pdf
    url: paper.pdf
    label: Paper
  - type: preprint
    provider: arxiv
    id: 2609.14091
    label: arXiv
---

<article class="ltx_document">




<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="introduction"><span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p id="S1.p1.1" class="ltx_p">Two classical problems anchor Gaussian denoising under geometric constraints. Isotonic regression, the estimation of a monotone sequence, obeys the cube-root phase diagram of shape-constrained estimation <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib2" title="" class="ltx_ref">Zhang, 2002</a>; <a href="#bib.bib4" title="" class="ltx_ref">Chatterjee et al., 2015</a>)</cite>. Mean estimation over a scaled simplex, the nonnegative part of an $\ell_{1}$ ball, obeys the $\sqrt{\log}$ diagram of sparse estimation <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib5" title="" class="ltx_ref">Donoho and Johnstone, 1994</a>; <a href="#bib.bib6" title="" class="ltx_ref">Birgé and Massart, 2001</a>)</cite>. The two diagrams, each carrying decades of theory, are unlike in kind: the monotone problem pays a power of its depth, the sparse problem a logarithm of its width. Between the sequence and the simplex lies every geometry in which depth and branching interact, and there the picture has remained incomplete.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p id="S1.p2.1" class="ltx_p">One model generalizes both. A <em id="S1.p2.1.1" class="ltx_emph ltx_font_italic">tree flow</em> <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty, 2018</a>)</cite> assigns to the vertices of a rooted tree nonnegative values such that each vertex passes to its children at most what it receives: a mass enters at the root, travels downward, and may leak at any vertex. A path, depth without branching, is bounded isotonic regression; a star, branching without depth, is mean estimation over the scaled simplex. The same inequalities arise wherever hierarchical totals are measured with noise. In the consistency post-processing of differentially private counts they hold with equality <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib7" title="" class="ltx_ref">Hay et al., 2010</a>; <a href="#bib.bib8" title="" class="ltx_ref">Abowd et al., 2022</a>)</cite>; in profiling a call tree the leak carries real mass, the self time of a procedure <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib9" title="" class="ltx_ref">Graham et al., 1982</a>)</cite>. Chatterjee and Lafferty studied the least squares estimator, the projection onto the flow cone and the natural tuning-free program for the model, and discovered that it behaves unlike its isotonic counterpart: its rate of convergence is not monotone in the depth of the tree, and it can miss the minimax rate by a power of $n\text{.}$ Where the projection fell short, the minimax rate was attained only by least squares over an exponentially large net, and their closing sentence poses the challenge of “closing the gap between the LSE and the minimax lower bound” with an efficient estimator. A decade later the challenge stood, and with it three gaps: the minimax risk was uncharacterized beyond two regimes of trees, the worst case of least squares at a fixed budget was unquantified, and no efficient estimator was known to attain the minimax rate where the projection did not.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p id="S1.p3.1" class="ltx_p">This paper closes all three. We ask: for every finite rooted tree and every budget and noise level, what is the minimax risk of denoising a tree flow, and is it attained by a computationally efficient estimator? One combinatorial functional of the tree organizes the answers, stated in <a href="#S1.SS1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>: a rate formula; an exact and efficient estimator; adaptation to the budget and, in an explicit regime, to the noise level; and the worst-case price of least squares. In the local entropy program for convex constraints <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib12" title="" class="ltx_ref">Neykov, 2023</a>)</cite>, the flow polytopes thereby form a nonsymmetric, combinatorially explicit family.</p>
</div>
<section id="S1.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="our-results"><span class="ltx_tag ltx_tag_subsection">1.1 </span>Our Results</h3>

<div id="S1.SS1.p1" class="ltx_para">
<p id="S1.SS1.p1.1" class="ltx_p">Let $T$ be a finite rooted tree with vertex set $\mathsf{V}\text{,}$ root $o\text{,}$ and $n:=|\mathsf{V}|$ vertices. Write $u\preceq v\text{,}$ and call $u$ an <em id="S1.SS1.p1.1.1" class="ltx_emph ltx_font_italic">ancestor</em> of $v\text{,}$ when $u$ lies on the path from $o$ to $v\text{,}$ so that every vertex is an ancestor of itself; let $d_{T}$ denote graph distance, and let $H_{T}:=\max_{u,w\in\mathsf{V}}d_{T}(u,w)$ denote the diameter of $T\text{.}$ Each vertex $u$ carries its root-path indicator $p_{u}\in\{0,1\}^{\mathsf{V}}\text{,}$ defined by $p_{u}(v)=\mathbf{1}\{v\preceq u\}\text{.}$ The <em id="S1.SS1.p1.1.2" class="ltx_emph ltx_font_italic">flow cone</em> of $T$ is</p>
<table id="S1.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{F}(T):=\Bigl\{\textstyle\sum_{u\in\mathsf{V}}s_{u}p_{u}:\ s_{u}\geq 0\text{ for all }u\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1.1)</span></td></tr></tbody>
</table>
<p id="S1.SS1.p1.2" class="ltx_p">whose elements are exactly the monotone flows on $T$ (<a href="#S2.Thmlemma1" title="Lemma 2.1 (Normal forms). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>). Fix a budget $V&gt;0$ and a noise level $\sigma&gt;0\text{.}$ The parameter set of this paper is the budget-$V$ slice of the cone, the <em id="S1.SS1.p1.2.1" class="ltx_emph ltx_font_italic">flow polytope</em></p>
<table id="S1.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{F}_{V}(T):=\bigl\{\mu\in\mathcal{F}(T):\ \mu(o)=V\bigr\}\ =\ V\operatorname{conv}\{p_{u}:u\in\mathsf{V}\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1.2)</span></td></tr></tbody>
</table>
<p id="S1.SS1.p1.3" class="ltx_p">The cone <a href="#S1.E1" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> is the flow cone of <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty (2018)</a></cite>; they cap the root value, $\mu(o)\leq V\text{,}$ where we fix it. For $n\geq 2$ the two constraints carry the same minimax risk up to universal constants: the capped body contains the slice, raising the root value of a capped signal to $V$ changes no other coordinate, and the cap therefore adds only the bounded scalar $\mu(o)\text{,}$ at a cost $\min\{V^{2},\sigma^{2}\}$ that the two-point bound <a href="#S3.E8" title="In 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.8</span></a> absorbs; the estimator of <a href="#Thmtheorem2" title="Theorem 2 (Efficient estimation). ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> transfers (<a href="#S1a" title="S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.1</span></a>). We observe $Y=\mu+\sigma Z$ with $Z\sim N(0,I_{n})$ and $\mu\in\mathcal{F}_{V}(T)\text{,}$ and study the minimax risk</p>
<table id="S1.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(V,\sigma):=\inf_{\widehat{\mu}}\ \sup_{\mu\in\mathcal{F}_{V}(T)}\mathbb{E}_{\mu}\bigl\|\widehat{\mu}(Y)-\mu\bigr\|_{2}^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1.3)</span></td></tr></tbody>
</table>
<p id="S1.SS1.p1.4" class="ltx_p">the infimum running over all measurable maps $\widehat{\mu}:\mathbb{R}^{\mathsf{V}}\to\mathbb{R}^{\mathsf{V}}\text{;}$ estimators are not required to take values in $\mathcal{F}_{V}(T)\text{.}$</p>
</div>
<div id="S1.SS1.p2" class="ltx_para">
<p id="S1.SS1.p2.1" class="ltx_p">An <em id="S1.SS1.p2.1.1" class="ltx_emph ltx_font_italic">ancestor $r$-net</em> is a set $R\subseteq\mathsf{V}$ such that every vertex $u$ has an ancestor $a\in R$ with $d_{T}(a,u)\leq r\text{,}$ and $N^{\uparrow}_{T}(r)$ denotes the minimum cardinality of an ancestor $r$-net. The <em id="S1.SS1.p2.1.2" class="ltx_emph ltx_font_italic">truncated ancestor profile</em> of $T$ is</p>
<table id="S1.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{k}(T):=\sup_{r&gt;0}\ r\,\min\Bigl\{k,\ \Bigl[\log\frac{N^{\uparrow}_{T}(r)}{k}\Bigr]_{+}\Bigr\},\qquad\delta_{k}(T):=\frac{\alpha_{k}(T)}{k}\qquad(k=1,2,\dots),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1.4)</span></td></tr></tbody>
</table>
<p id="S1.SS1.p2.2" class="ltx_p">where $[x]_{+}:=\max\{x,0\}\text{,}$ and the <em id="S1.SS1.p2.2.1" class="ltx_emph ltx_font_italic">crossing index</em> is</p>
<table id="S1.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$k_{0}=k_{0}(T,V,\sigma):=\min\Bigl\{k\geq 1:\ V^{2}\delta_{k}(T)\leq A_{0}\sigma^{2}k\ \text{ or }\ k&gt;n/C_{\star}\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1.5)</span></td></tr></tbody>
</table>
<p id="S1.SS1.p2.3" class="ltx_p">where $A_{0}$ and $C_{\star}$ are fixed universal constants; one may take $A_{0}=144$ and $C_{\star}=e^{2}\text{.}$ The truncation is the one nonstandard feature: once describing the branching below a vertex costs more than the information budget $k\text{,}$ the cluster is blurred at its own diameter rather than charged per descendant (<a href="#S2.Thmremark1" title="Remark 2.1 (Why the profile is truncated). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>).</p>
</div>
<div id="S1.SS1.p3" class="ltx_para">
<p id="S1.SS1.p3.1" class="ltx_p">The crossing index determines the minimax risk: <a href="#Thmtheorem1" title="Theorem 1 (Rate formula). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a>, proved in <a href="#S3" title="3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a>, shows that</p>
<table id="S1.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(V,\sigma)\ \asymp\ \min\bigl\{V^{2}H_{T},\ \sigma^{2}k_{0}(T,V,\sigma)\bigr\}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1.SS1.p3.2" class="ltx_p">for every finite rooted tree and all $V,\sigma&gt;0\text{.}$ The minimum has three readings: a diameter branch $V^{2}H_{T}\text{,}$ where the body is small and the constant estimator $Vp_{o}$ is already optimal; an information branch $\sigma^{2}k_{0}\text{,}$ the cost of $k_{0}$ effective coordinates; and, when the crossing clause never fires, a dimension branch $\sigma^{2}k_{0}\asymp\sigma^{2}n\text{,}$ where the identity estimator is optimal. The formula is computable: a surrogate index evaluates it to within a factor of two in $O(n\log(n+1))$ operations (<a href="#S2.Thmlemma3" title="Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>).</p>
</div>
<div id="S1.SS1.p4" class="ltx_para">
<p id="S1.SS1.p4.1" class="ltx_p">Behind the formula stands the entropy theory of Gaussian estimation, from global metric entropy to the local entropy fixed point of bounded convex constraints <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib11" title="" class="ltx_ref">Yang and Barron, 1999</a>; <a href="#bib.bib12" title="" class="ltx_ref">Neykov, 2023</a>)</cite>. That theory identifies the governing quantity; computing it on a given body, and constructing the packings it promises when the body is an asymmetric cone, are the separate problems solved in <a href="#S3" title="3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a>. For $t&gt;0$ let $H^{c}_{T}(t)$ denote the metric entropy of the flow polytope at squared radius $t\text{:}$ the logarithm of the smallest number of Euclidean balls of radius $\sqrt{t}\text{,}$ centered anywhere, whose union contains $\mathcal{F}_{V}(T)\text{.}$ Define the associated fixed point</p>
<table id="S1.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\rho_{T}(V,\sigma)\ :=\ \inf_{t&gt;0}\ \bigl[t+\sigma^{2}H^{c}_{T}(t)\bigr].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1.6)</span></td></tr></tbody>
</table>
<p id="S1.SS1.p4.2" class="ltx_p">Free centers are the convenient convention, because the covers of <a href="#S3" title="3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a> have centers outside the body; restricting centers to the body leaves <a href="#S1.E6" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.6</span></a> unchanged (<a href="#S1a" title="S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.1</span></a>). <a href="#Thmproposition1" title="Proposition 1 (Entropy fixed point). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">1</span></a> gives $R^{*}_{T}(V,\sigma)\asymp\min\{\rho_{T}(V,\sigma),\ V^{2}H_{T},\ \sigma^{2}n\}\text{;}$ <a href="#Thmtheorem1" title="Theorem 1 (Rate formula). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a> thus evaluates this entropy expression in closed combinatorial form.</p>
</div>
<figure id="S1.T1" class="ltx_table">
<figcaption class="ltx_caption"><span class="ltx_tag ltx_tag_table">Table 1: </span>The rate formula on three families
(<a href="#Thmcorollary1" title="Corollary 1 (Path). ‣ 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollaries</span> <span class="ltx_text ltx_ref_tag">1</span></a>, <a href="#Thmcorollary2" title="Corollary 2 (Star). ‣ 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a> and <a href="#Thmcorollary3" title="Corollary 3 (Complete binary tree). ‣ 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), with $n$ the number of
vertices and universal constants in $\asymp\text{;}$ the path $P_{L}$ has $L$
edges, the star $S_{m}$ has $m$ leaves, and the complete binary tree
$B_{h}$ has height $h\text{.}$
The first two rows recover the classical phase diagrams; the third
carries a full logarithm that occurs at neither endpoint.</figcaption>
<table id="S1.T1.2" class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr id="S1.T1.2.1" class="ltx_tr">
<th id="S1.T1.2.1.1" class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_th_row ltx_border_t">Tree</th>
<th id="S1.T1.2.1.2" class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_th_row ltx_border_t">$R^{*}\asymp$</th>
<th id="S1.T1.2.1.3" class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_border_t">Classical counterpart</th>
<th id="S1.T1.2.1.4" class="ltx_td ltx_nopad_r ltx_align_left ltx_th ltx_th_column ltx_border_t">Phenomenon</th></tr>
</thead>
<tbody class="ltx_tbody">
<tr id="S1.T1.2.2" class="ltx_tr">
<th id="S1.T1.2.2.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">path $P_{L}$</th>
<th id="S1.T1.2.2.2" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">$\min\bigl\{V^{2}L,\ V^{2/3}\sigma^{4/3}L^{1/3},\ \sigma^{2}(L{+}1)\bigr\}$</th>
<td id="S1.T1.2.2.3" class="ltx_td ltx_align_left ltx_border_t">bounded isotonic</td>
<td id="S1.T1.2.2.4" class="ltx_td ltx_nopad_r ltx_align_left ltx_border_t">cube root</td></tr>
<tr id="S1.T1.2.3" class="ltx_tr">
<th id="S1.T1.2.3.1" class="ltx_td ltx_align_left ltx_th ltx_th_row">star $S_{m}$</th>
<th id="S1.T1.2.3.2" class="ltx_td ltx_align_left ltx_th ltx_th_row">$\min\bigl\{V^{2},\ \sigma V\sqrt{1+[\log(m\sigma/V)]_{+}},\ \sigma^{2}m\bigr\}$</th>
<td id="S1.T1.2.3.3" class="ltx_td ltx_align_left">simplex mean</td>
<td id="S1.T1.2.3.4" class="ltx_td ltx_nopad_r ltx_align_left">$\sqrt{\log}$</td></tr>
<tr id="S1.T1.2.4" class="ltx_tr">
<th id="S1.T1.2.4.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_b">binary $B_{h}$</th>
<th id="S1.T1.2.4.2" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_b">$\min\bigl\{V^{2}h,\ \sigma V\bigl(1+[\log(n\sigma/V)]_{+}\bigr),\ \sigma^{2}n\bigr\}$</th>
<td id="S1.T1.2.4.3" class="ltx_td ltx_align_left ltx_border_b">no direct analogue</td>
<td id="S1.T1.2.4.4" class="ltx_td ltx_nopad_r ltx_align_left ltx_border_b">full logarithm</td></tr>
</tbody>
</table>
</figure>
<div id="S1.SS1.p5" class="ltx_para">
<p id="S1.SS1.p5.1" class="ltx_p">On three benchmark families the formula specializes in closed form; <a href="#S1.T1" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Table</span> <span class="ltx_text ltx_ref_tag">1</span></a> collects the three rates, proved as <a href="#Thmcorollary1" title="Corollary 1 (Path). ‣ 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollaries</span> <span class="ltx_text ltx_ref_tag">1</span></a>, <a href="#Thmcorollary2" title="Corollary 2 (Star). ‣ 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a> and <a href="#Thmcorollary3" title="Corollary 3 (Complete binary tree). ‣ 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a> in <a href="#S3.SS3" title="3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>. The first two are external checks: the path recovers the bounded isotonic diagram <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib2" title="" class="ltx_ref">Zhang, 2002</a>; <a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty, 2018</a>)</cite>; the star recovers the simplex diagram of sparse estimation <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib5" title="" class="ltx_ref">Donoho and Johnstone, 1994</a>; <a href="#bib.bib6" title="" class="ltx_ref">Birgé and Massart, 2001</a>)</cite>. The complete binary tree resembles neither: branching entropy repeats across $\Theta(\log n)$ depth scales, making the profile $\alpha_{k}$ quadratic in $\log(n/k)$ once $k$ exceeds that logarithm, and the crossing takes a square root, leaving the single full logarithm.</p>
</div>
<div id="S1.SS1.p6" class="ltx_para">
<p id="S1.SS1.p6.1" class="ltx_p">An exactly evaluable estimator attains the rate. <a href="#Thmtheorem2" title="Theorem 2 (Efficient estimation). ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a>, proved in <a href="#S4" title="4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a>, constructs a deterministic estimator with worst-case risk $O(R^{*}_{T}(V,\sigma))$ on every tree, computed exactly in $O(n^{2}\log(n+1))$ arithmetic operations: an exponentially weighted aggregate over a class of integer states. Together with <a href="#Thmtheorem5" title="Theorem 5 (Least squares). ‣ 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">5</span></a>, it answers the challenge of <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty (2018)</a></cite>: an efficient estimator closes the gap between least squares and the minimax risk.</p>
</div>
<div id="S1.SS1.p7" class="ltx_para">
<p id="S1.SS1.p7.1" class="ltx_p">The estimator of <a href="#Thmtheorem2" title="Theorem 2 (Efficient estimation). ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> takes $V$ and $\sigma$ as inputs; the next two theorems remove them. <a href="#Thmtheorem3" title="Theorem 3 (Budget adaptation). ‣ 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3</span></a>, proved in <a href="#S4.SS3" title="4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.3</span></a>, removes the budget: a deterministic polynomial-time estimator free of $V$ attains $C(R^{*}_{T}(V,\sigma)+\sigma^{2})\text{,}$ and no budget-free estimator stays below an $\Omega(\sigma^{2})$ floor on adjacent budgets. On the cone, where the original model carries no budget parameter, this adaptation is the return to the model as <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty (2018)</a></cite> posed it. <a href="#Thmtheorem4" title="Theorem 4 (Full adaptation). ‣ 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4</span></a> removes the noise level as well, in an explicit regime $Vw_{T}\leq c\sigma n\text{,}$ with $w_{T}$ a width functional that bounds how much of the tree’s difference structure the signal can contaminate, equal to $1$ on a path and $\Theta(\log n)$ on a balanced binary tree. Within the regime the noise dominates a majority of the tree’s difference statistics and a median estimates $\sigma\text{;}$ on families of bounded width, the regime sits within a $\sqrt{\log n}$ factor of a ceiling that no noise estimator can pass (<a href="#S6" title="S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.6</span></a>).</p>
</div>
<div id="S1.SS1.p8" class="ltx_para">
<p id="S1.SS1.p8.1" class="ltx_p">Every estimator above is built from the profile. The default estimator ignores it: the Euclidean projection onto the body, the tuning-free convex program of least squares at a known budget. <a href="#Thmtheorem5" title="Theorem 5 (Least squares). ‣ 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">5</span></a>, proved in <a href="#S5" title="5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5</span></a>, determines its worst case: on every tree and at all $V,\sigma&gt;0$ the projection loses at most a factor $C(1+\log(en))^{2/5}$ over the minimax risk, and on an explicit one-parameter family of brooms, at a single budget and noise level, it loses at least $c(\log n)^{2/5}\text{.}$ The separation is an exact power of the logarithm, matched from both sides, where the separations of <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib14" title="" class="ltx_ref">Chatterjee (2014)</a>; <a href="#bib.bib15" title="" class="ltx_ref">Kur et al. (2024)</a></cite> are polynomial in the sample size or the dimension. The equivalence of the fixed and capped budgets recorded above concerns minimax risks; <a href="#Thmtheorem5" title="Theorem 5 (Least squares). ‣ 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">5</span></a> concerns the projection itself.</p>
</div>
</section>
<section id="S1.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="technical-overview"><span class="ltx_tag ltx_tag_subsection">1.2 </span>Technical Overview</h3>

<div id="S1.SS2.p1" class="ltx_para">
<p id="S1.SS2.p1.1" class="ltx_p">The upper bound in <a href="#Thmtheorem1" title="Theorem 1 (Rate formula). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a> is soft: least squares over a covering net attains the entropy fixed point <a href="#S1.E6" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.6</span></a>, and two trivial estimators cap the risk at $V^{2}H_{T}$ and $\sigma^{2}n\text{.}$ Three tasks remain. The entropy must be <em id="S1.SS2.p1.1.1" class="ltx_emph ltx_font_italic">realized</em>, by hypotheses legal in a positive body (the lower bound); <em id="S1.SS2.p1.1.2" class="ltx_emph ltx_font_italic">searched</em>, exactly and quickly (the algorithm); and <em id="S1.SS2.p1.1.3" class="ltx_emph ltx_font_italic">measured</em> against the natural convex program (the least squares question). Two features of the flow polytope obstruct the classical routes to all three: positivity, the body being a simplex rather than a symmetric ball, so that a hypothesis moves only the leak mass it holds and sign-toggling lower bounds, whose one base point would have to fund every signed perturbation, fail; and overlap, root paths through a common vertex sharing coordinates, so that the contrast blocks realizing the entropy can overlap and are therefore priced (<a href="#S3.SS2" title="3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>).</p>
</div>
<div id="S1.SS2.p2" class="ltx_para">
<p id="S1.SS2.p2.1" class="ltx_p">The lower bound realizes the entropy inside the body. Ancestor-covering numbers force a separated vertex set (<a href="#S3.Thmlemma2" title="Lemma 3.2 (Cover to packing). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>); groups drawn from it, in subtrees with disjoint edge sets, share the budget exactly; a multiscale code fills each group; and a product form of Fano’s inequality (<a href="#S3.Thmlemma3" title="Lemma 3.3 (Fano’s inequality for overlapping blocks). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>) prices the overlap between scales once, through a normalized Gram row sum, returning $R^{*}_{T}\geq c\min\{V^{2}r/q,\ \sigma^{2}q\log(eM/q)\}$ for $M$ vertices at pairwise distance $r$ in $q$ groups; matching $q$ to the profile recovers its truncated logarithm. Where <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty (2018)</a></cite> allocate mass across vertex-disjoint paths, the same budget discipline runs on arbitrarily overlapping routes.</p>
</div>
<div id="S1.SS2.p3" class="ltx_para">
<p id="S1.SS2.p3.1" class="ltx_p">The upper bound builds one coded cover for all signals. Dyadic ancestor nets and their cells depend only on the tree and the information budget $k\text{;}$ for each signal, heavy cells split and light cells collapse to their roots, sparse sampling restoring the light exits; every subtree is an interval of the depth-first preorder, so one scalar, the running floor of cumulative masses along it, rounds all subtree sums at once. The resulting approximant is within squared error $O(V^{2}\delta_{k})$ of its signal and carries a fixed root sum, a code length $O(k)\text{,}$ and flow states confined to an $O(k)$ range; counting the class at $e^{O(k)}$ gives the entropy bound <a href="#S3.E2" title="In Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>. An integer-leak net already appears in the upper bound of <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty (2018)</a></cite>, at cost $\log n$ per unit of mass and at the diameter scale; the activation charges lower this to $O(1)$ per unit and the profile scale, and these reductions are what the estimator consumes.</p>
</div>
<div id="S1.SS2.p4" class="ltx_para">
<p id="S1.SS2.p4.1" class="ltx_p">The two halves meet at the crossing. In the interior case the nonincreasing profile scale $V^{2}\delta_{k}$ first falls below $A_{0}\sigma^{2}k$ at $k_{0}\text{;}$ the cover gives the rate $\sigma^{2}k_{0}$ there, the packing gives $\sigma^{2}(k_{0}-1)$ one step earlier, and the corner regimes are collected by a two-point bound and the dimension cap. This proves <a href="#Thmtheorem1" title="Theorem 1 (Rate formula). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a> and <a href="#Thmproposition1" title="Proposition 1 (Entropy fixed point). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition 1</span></a> as four cases of one argument.</p>
</div>
<div id="S1.SS2.p5" class="ltx_para">
<p id="S1.SS2.p5.1" class="ltx_p">The estimator replaces the search over the cover by an average, an exponentially weighted aggregate under a Kraft-type prior built from the code length. Its risk analysis composes two exact identities, Stein’s and the Gibbs variational identity, with no union bound and approximation constant one (<a href="#S4.Thmlemma1" title="Lemma 4.1 (Aggregation oracle). ‣ 4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>). The confinement is what makes the computation possible: one integer state in $[0,3k]$ per vertex turns the partition function into a tree recursion of polynomial messages, evaluated exactly; one reverse-mode sweep then reads off the posterior mean at every coordinate. The recursion is dynamic programming over distributions, not values.</p>
</div>
<div id="S1.SS2.p6" class="ltx_para">
<p id="S1.SS2.p6.1" class="ltx_p">Adaptation reuses the cover. Removing the quantization from the approximant of <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> leaves amplitude-free profile subspaces; a Kraft-weighted penalized selection over them, joined with finite grids of candidate budgets, attains $C(R^{*}_{T}+\sigma^{2})$ without knowing $V\text{,}$ the additive $\sigma^{2}$ forced on adjacent budgets by a two-point test at the root. For unknown $\sigma\text{,}$ a median of tree difference statistics survives contamination when $Vw_{T}\leq c\sigma n\text{,}$ and the selection runs at the rounded estimate.</p>
</div>
<div id="S1.SS2.p7" class="ltx_para">
<p id="S1.SS2.p7.1" class="ltx_p">The broom of <a href="#Thmtheorem5" title="Theorem 5 (Least squares). ‣ 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">5</span></a>, a handle of $L$ edges feeding $e^{\Theta(L^{5/2})}$ terminal leaves, makes the blindness of the projection quantitative: the extreme leaf noise repays the quadratic cost of the full-budget route through the handle, forcing least squares to lose $L^{3/2}\text{,}$ while the profile sees one ancestor covering the terminal star at every radius $r\geq 1$ and the minimax risk stays at order $\sqrt{L}\text{,}$ that of the handle alone; with $\log n\asymp L^{5/2}\text{,}$ the ratio is the $2/5$ power of the logarithm. For the matching upper bound, the localized-width analysis of <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib14" title="" class="ltx_ref">Chatterjee (2014)</a></cite> runs on the coded cover with centers chosen after the noise, and a width branch and a height branch meet at the same power.</p>
</div>
<div id="S1.SS2.p8" class="ltx_para">
<p id="S1.SS2.p8.1" class="ltx_p">Three devices are stated for reuse: the overlapping-block Fano inequality (<a href="#S3.Thmlemma3" title="Lemma 3.3 (Fano’s inequality for overlapping blocks). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>), which refers to no tree and prices overlap inside an arbitrary convex constraint; the positive packing of <a href="#S3.SS2" title="3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>, a template for bodies in which sign toggling is illegal; and the aggregate of <a href="#S4" title="4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a>, whose oracle inequality holds over any finite class and whose evaluation is exact whenever the class is dynamically
programmable. <a href="#S2" title="2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Sections</span> <span class="ltx_text ltx_ref_tag">2</span></a>, <a href="#S3" title="3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>, <a href="#S4" title="4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a> and <a href="#S5" title="5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5</span></a> prove the results in turn; the remaining details are in the appendices.</p>
</div>
</section>
<section id="S1.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="related-work"><span class="ltx_tag ltx_tag_subsection">1.3 </span>Related Work</h3>

<div id="S1.SS3.p1" class="ltx_para">
<p id="S1.SS3.p1.1" class="ltx_p">The closest work is <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty (2018)</a></cite>. They introduced tree flows and analyzed the projection onto the flow cone in two regimes: for trees of bounded depth they proved matching risk bounds in the principal range of budgets, and on trees consisting of many long disjoint paths they determined the exponents of both the projection and the minimax risk, which disagree. Their projection takes no budget input, and over part of that family its risk exceeds the minimax risk polynomially in $n$ at a fixed budget, by overfitting the zero signal where the cone has large statistical dimension; the projection of <a href="#Thmtheorem5" title="Theorem 5 (Least squares). ‣ 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">5</span></a> receives the budget, which removes that failure and leaves exactly the $2/5$ power of the logarithm. The constraint family itself predates the statistics: <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib10" title="" class="ltx_ref">Benabbas et al. (2011)</a></cite> smooth hierarchical data under the same inequalities in $\ell_{1}\text{.}$ Isotonic regression on richer orders <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib17" title="" class="ltx_ref">Han et al., 2019</a>)</cite> shares the ambient structure but not the geometry: it acts on differences, while the flow constraint transports mass, thereby making the body a simplex. On the path the model meets the isotonic tradition <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib2" title="" class="ltx_ref">Zhang, 2002</a>; <a href="#bib.bib4" title="" class="ltx_ref">Chatterjee et al., 2015</a>; <a href="#bib.bib20" title="" class="ltx_ref">Bellec, 2018</a>; <a href="#bib.bib24" title="" class="ltx_ref">Guntuboyina and Sen, 2018</a>)</cite>, in its bounded form <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib23" title="" class="ltx_ref">Luss and Rosset, 2017</a>)</cite>, and <a href="#Thmcorollary1" title="Corollary 1 (Path). ‣ 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1</span></a> returns its phase diagram. The obstacle on trees is therefore the budget slice, the simplex geometry, not monotonicity.</p>
</div>
<div id="S1.SS3.p2" class="ltx_para">
<p id="S1.SS3.p2.1" class="ltx_p">Metric entropy has determined minimax rates since <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib11" title="" class="ltx_ref">Yang and Barron (1999)</a></cite> tied them to the global entropy of the function class; for bounded convex constraints in the Gaussian sequence model, <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib12" title="" class="ltx_ref">Neykov (2023)</a></cite> gives the exact rate through a local entropy fixed point. On the flow polytopes the two halves of that program take concrete form: the profile computes the rate that the fixed point governs, in closed combinatorial form and in near-linear time, and the packing of <a href="#S3.SS2" title="3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.2</span></a> realizes the entropy inside a cone with no symmetry, one-sided perturbations replacing sign toggling; compare the cone geometry of testing in <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib19" title="" class="ltx_ref">Wei et al. (2019)</a></cite>. On the star, positivity leaves the sparse rate unchanged; what it changes is the lower bound, which must be built one-sided. The covering geometry has an operator-theoretic precedent: the body is $V$ times the image of the positive face of the $\ell_{1}$ ball under the tree’s summation operator, and <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib21" title="" class="ltx_ref">Lifshits and Linde (2011a)</a>; <a href="#bib.bib22" title="" class="ltx_ref">Lifshits and Linde (2011b)</a></cite> bound the entropy numbers of such operators through ancestor covering numbers; the critical case stops a heavy–light partition at its light sets and counts the outcomes, the combinatorial core that <a href="#S3.SS1" title="3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> shares. Compactness of the symmetric image is their question; the positive slice, the minimax risk, and the certificates behind the estimator are this paper’s.</p>
</div>
<div id="S1.SS3.p3" class="ltx_para">
<p id="S1.SS3.p3.1" class="ltx_p">That the projection onto a convex body can miss the minimax rate by a large factor was shown by <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib3" title="" class="ltx_ref">Zhang (2013)</a></cite> on an ellipsoid and by <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib14" title="" class="ltx_ref">Chatterjee (2014)</a></cite> on a designed body, in both cases by a factor as large as $\sqrt{n}\text{;}$ the fixed-point analysis of least squares in the latter is the engine of our upper bound in <a href="#S5" title="5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5</span></a>. Separations of polynomial order in the sample size or the dimension are known for several natural programs <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib15" title="" class="ltx_ref">Kur et al., 2024</a>; <a href="#bib.bib16" title="" class="ltx_ref">Vaškevičius and Zhivotovskiy, 2023</a>)</cite>, and on an $\ell_{p}$ ball <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib31" title="" class="ltx_ref">Aolaritei et al. (2025)</a></cite> separate the projection from the minimax rate by a power of the logarithm. <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib13" title="" class="ltx_ref">Prasadan and Neykov (2025)</a></cite> characterize the boundary exactly: least squares is minimax optimal if and only if the local Gaussian width map is Lipschitz at the relevant scales. By that characterization, <a href="#Thmtheorem5" title="Theorem 5 (Least squares). ‣ 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">5</span></a> shows the Lipschitz bound cannot hold uniformly along the brooms, and it goes past the optimal-or-not dichotomy by bounding the worst-case ratio of least squares to the minimax rate from both sides. The upper bound speaks for the projection as much as against it: a loss beyond the $2/5$ power of the logarithm is impossible on any tree.</p>
</div>
<div id="S1.SS3.p4" class="ltx_para">
<p id="S1.SS3.p4.1" class="ltx_p">The estimator of <a href="#Thmtheorem2" title="Theorem 2 (Efficient estimation). ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> belongs to the aggregation tradition. <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib25" title="" class="ltx_ref">Leung and Barron (2006)</a></cite> proved an exact Stein-based oracle inequality for exponentially weighted aggregates, and <a href="#S4.Thmlemma1" title="Lemma 4.1 (Aggregation oracle). ‣ 4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.1</span></a> descends from it; sharp PAC-Bayes bounds, optimal sparse aggregation, and unknown-variance mixing follow in <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib26" title="" class="ltx_ref">Dalalyan and Tsybakov (2008)</a>; <a href="#bib.bib27" title="" class="ltx_ref">Rigollet and Tsybakov (2011)</a>; <a href="#bib.bib28" title="" class="ltx_ref">Giraud (2008)</a></cite>. Exact mixtures over combinatorial families have a computing tradition of their own: context-tree weighting <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib29" title="" class="ltx_ref">Willems et al., 1995</a>)</cite> and circuit differentiation for marginals <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib30" title="" class="ltx_ref">Darwiche, 2003</a>)</cite>, without squared-loss risk guarantees. The class of integer states sits in both traditions: its code length ties the Kraft prior, in the tradition of minimum description length <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib32" title="" class="ltx_ref">Barron and Cover, 1991</a>)</cite>, to the minimax rate, and its confined states make the posterior mean a tree recursion, evaluated exactly. Shape-constrained solvers compute hard projections <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib33" title="" class="ltx_ref">Robertson et al., 1988</a>; <a href="#bib.bib18" title="" class="ltx_ref">Kyng et al., 2015</a>)</cite>, the object that <a href="#Thmtheorem5" title="Theorem 5 (Least squares). ‣ 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">5</span></a> measures; the recursion here averages where those optimize. A recent line attains polynomial-time near-optimality on symmetric bodies under further regularity and oracle hypotheses <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib34" title="" class="ltx_ref">Neykov, 2026</a>)</cite>; the flow polytope is a simplex. The trade is structure for exactness: a combinatorial family of bodies, in exchange for the exact rate and the exact estimator.</p>
</div>
</section>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-flow-polytope-and-the-ancestor-profile"><span class="ltx_tag ltx_tag_section">2 </span>The Flow Polytope and the Ancestor Profile</h2>

<div id="S2.p1" class="ltx_para">
<p id="S2.p1.1" class="ltx_p">This section records the interfaces used by the rest of the paper: the two normal forms of the flow polytope, the Euclidean realization of the tree metric, and the working properties of the ancestor profile, including the surrogate index through which the profile is computed. Proofs are collected in <a href="#S1a" title="S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.1</span></a>.</p>
</div>
<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-flow-polytope"><span class="ltx_tag ltx_tag_subsection">2.1 </span>The Flow Polytope</h3>

<div id="S2.SS1.p1" class="ltx_para">
<p id="S2.SS1.p1.1" class="ltx_p">We complete the tree notation of <a href="#S1.SS1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>. For $v\neq o$ we write $\operatorname{pa}(v)$ for the parent of $v$ and identify $v$ with its parent edge $(\operatorname{pa}(v),v)\text{,}$ of which $v$ is the <em id="S2.SS1.p1.1.1" class="ltx_emph ltx_font_italic">lower endpoint</em>; $\operatorname{ch}(v)$ is the set of children of $v\text{,}$ and $T_{v}:=\{u\in\mathsf{V}:v\preceq u\}$ is the subtree rooted at $v\text{.}$ The depth of a vertex is its distance from the root, and the height of $T$ is $h_{T}:=\max_{v\in\mathsf{V}}\operatorname{depth}(v)\text{,}$ so that $h_{T}\leq H_{T}\leq 2h_{T}\text{.}$ Universal constants $c,C,c^{\prime},C^{\prime},\dots$ may change value from occurrence to occurrence, while subscripted constants such as $A_{0}$ and $C_{\star}$ keep their values fixed once introduced. Logarithms are natural. Complexity statements count arithmetic operations in the real-RAM model: arithmetic, comparisons, integer part, and evaluations of $\exp$ and $\log$ on real registers are exact unit-cost operations, and two polynomials of degree $m$ can be multiplied in $O(m\log m)$ operations by the fast Fourier transform <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib39" title="" class="ltx_ref">von zur Gathen and Gerhard, 2013</a>)</cite>; what exactness means for the estimator is stated in <a href="#S4.Thmremark1" title="Remark 4.1 (Computational model). ‣ 4.2 Exact Evaluation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>.</p>
</div>
<div id="S2.SS1.p2" class="ltx_para">
<p id="S2.SS1.p2.1" class="ltx_p">The polytope has a barycentric normal form and a flow normal form: the first is the legality certificate behind every lower-bound construction of <a href="#S3" title="3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a>, the second identifies the body as a set of flows and explains its name.</p>
</div>
<div id="S2.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma 2.1</span></span><span id="S2.Thmlemma1.3" class="ltx_text ltx_font_bold"> (Normal forms).</span></h6>
<div id="S2.Thmlemma1.p1" class="ltx_para">
<p id="S2.Thmlemma1.p1.1" class="ltx_p"><span id="S2.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">For $\mu\in\mathbb{R}^{\mathsf{V}}$ the following are equivalent:</span></p>
<ol id="S2.I1" class="ltx_enumerate">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p id="S2.I1.i1.p1.1" class="ltx_p">$\mu\in\mathcal{F}_{V}(T)$<span id="S2.I1.i1.p1.1.1" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p id="S2.I1.i2.p1.1" class="ltx_p">$\mu=\sum_{u\in\mathsf{V}}s_{u}p_{u}$<span id="S2.I1.i2.p1.1.1" class="ltx_text ltx_font_italic"> with </span>$s_{u}\geq 0$<span id="S2.I1.i2.p1.1.2" class="ltx_text ltx_font_italic"> for all
</span>$u$<span id="S2.I1.i2.p1.1.3" class="ltx_text ltx_font_italic"> and </span>$\sum_{u\in\mathsf{V}}s_{u}=V$<span id="S2.I1.i2.p1.1.4" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S2.I1.i3.p1" class="ltx_para">
<p id="S2.I1.i3.p1.1" class="ltx_p">$\mu(o)=V$<span id="S2.I1.i3.p1.1.1" class="ltx_text ltx_font_italic"> and
</span>$\mu(v)\geq\sum_{c\in\operatorname{ch}(v)}\mu(c)$<span id="S2.I1.i3.p1.1.2" class="ltx_text ltx_font_italic"> for every </span>$v\in\mathsf{V}$<span id="S2.I1.i3.p1.1.3" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
<p id="S2.Thmlemma1.p1.2" class="ltx_p"><span id="S2.Thmlemma1.p1.2.1" class="ltx_text ltx_font_italic">The coefficients in </span>(<a href="#S2.I1.i2" title="Item 2 ‣ Lemma 2.1 (Normal forms). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>)<span id="S2.Thmlemma1.p1.2.2" class="ltx_text ltx_font_italic"> are unique, and they are tied to the coordinates by the subtree sums</span></p>
<table id="S2.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mu(v)\ =\ \sum_{u\succeq v}s_{u},\qquad s_{v}\ =\ \mu(v)-\sum_{c\in\operatorname{ch}(v)}\mu(c)\qquad(v\in\mathsf{V}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S2.SS1.p3" class="ltx_para">
<p id="S2.SS1.p3.1" class="ltx_p">Form (<a href="#S2.I1.i3" title="Item 3 ‣ Lemma 2.1 (Normal forms). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>) exhibits $\mathcal{F}_{V}(T)$ as the set of monotone flows at budget $V\text{,}$ with $s_{v}$ the <em id="S2.SS1.p3.1.1" class="ltx_emph ltx_font_italic">leak</em> at $v\text{,}$ the mass that stops there <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty, 2018</a>)</cite>. In a linear order of $\mathsf{V}$ that places ancestors before descendants, the matrix with columns $(p_{u})_{u\in\mathsf{V}}$ is upper triangular with unit diagonal (<a href="#S1a" title="S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.1</span></a>), so the $p_{u}$ are linearly independent and the body is a nondegenerate $(n-1)$-dimensional simplex with vertex set $\{Vp_{u}:u\in\mathsf{V}\}\text{.}$ Finally, $\mu(o)=V$ identically on the body: the root coordinate carries no statistical content, and all estimation error lives on the nonroot coordinates.</p>
</div>
<div id="S2.SS1.p4" class="ltx_para">
<p id="S2.SS1.p4.1" class="ltx_p">The second interface converts tree combinatorics into Euclidean geometry: squared Euclidean distance between root-path indicators is tree distance, which is why the ancestor profile, defined by the tree metric, controls Euclidean covering and packing of the body.</p>
</div>
<div id="S2.Thmlemma2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma2.2" class="ltx_text ltx_font_bold">Lemma 2.2</span></span><span id="S2.Thmlemma2.3" class="ltx_text ltx_font_bold"> (Isometry and edge supports).</span></h6>
<div id="S2.Thmlemma2.p1" class="ltx_para">
<ol id="S2.I2" class="ltx_enumerate">
<li id="S2.I2.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S2.I2.i1.p1" class="ltx_para">
<p id="S2.I2.i1.p1.1" class="ltx_p">$\|p_{u}-p_{w}\|_{2}^{2}=d_{T}(u,w)$<span id="S2.I2.i1.p1.1.1" class="ltx_text ltx_font_italic"> for all </span>$u,w\in\mathsf{V}$<span id="S2.I2.i1.p1.1.2" class="ltx_text ltx_font_italic">;
consequently </span>$\operatorname{diam}^{2}\mathcal{F}_{V}(T)=V^{2}H_{T}$<span id="S2.I2.i1.p1.1.3" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
<li id="S2.I2.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S2.I2.i2.p1" class="ltx_para">
<p id="S2.I2.i2.p1.1" class="ltx_p"><span id="S2.I2.i2.p1.1.1" class="ltx_text ltx_font_italic">For </span>$a\preceq b$<span id="S2.I2.i2.p1.1.2" class="ltx_text ltx_font_italic">, </span>$p_{b}-p_{a}=\mathbf{1}_{(a,b]}$<span id="S2.I2.i2.p1.1.3" class="ltx_text ltx_font_italic">, the
indicator of </span>$\{v:a\prec v\preceq b\}$<span id="S2.I2.i2.p1.1.4" class="ltx_text ltx_font_italic">; in general, the support of
</span>$p_{u}-p_{w}$<span id="S2.I2.i2.p1.1.5" class="ltx_text ltx_font_italic"> is exactly the set of lower endpoints of the edges on the
path from </span>$u$<span id="S2.I2.i2.p1.1.6" class="ltx_text ltx_font_italic"> to </span>$w$<span id="S2.I2.i2.p1.1.7" class="ltx_text ltx_font_italic">. In particular, differences </span>$p_{u}-p_{w}$<span id="S2.I2.i2.p1.1.8" class="ltx_text ltx_font_italic"> taken
within edge-disjoint connected subtrees have disjoint supports.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S2.SS1.p5" class="ltx_para">
<p id="S2.SS1.p5.1" class="ltx_p">Behind (<a href="#S2.I2.i1" title="Item 1 ‣ Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>) is the ancestor count $\langle p_{u},p_{w}\rangle=\operatorname{depth}(u\wedge w)+1\text{,}$ where $u\wedge w$ denotes the deepest common ancestor of $u$ and $w\text{.}$</p>
</div>
</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-ancestor-profile"><span class="ltx_tag ltx_tag_subsection">2.2 </span>The Ancestor Profile</h3>

<div id="S2.SS2.p1" class="ltx_para">
<p id="S2.SS2.p1.1" class="ltx_p">The profile $\alpha_{k},\delta_{k}$ and the crossing index $k_{0}$ were defined in <a href="#S1.E4" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">1.4</span></a> and <a href="#S1.E5" title="Equation 1.5 ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1.5</span></a>; this subsection collects the properties used below. A star shows why the truncation is there.</p>
</div>
<div id="S2.Thmremark1" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmremark1.2" class="ltx_text ltx_font_bold">Remark 2.1</span></span><span id="S2.Thmremark1.3" class="ltx_text ltx_font_bold"> (Why the profile is truncated).</span></h6>
<div id="S2.Thmremark1.p1" class="ltx_para">
<p id="S2.Thmremark1.p1.1" class="ltx_p"><span id="S2.Thmremark1.p1.1.1" class="ltx_text ltx_font_italic">On the star with $m$ leaves rooted at the hub, a leaf is ancestor-covered only by itself or by the hub, so $N^{\uparrow}_{T}(r)=m+1$ for $0\leq r&lt;1$ and $N^{\uparrow}_{T}(r)=1$ for $r\geq 1\text{;}$ the expression in <a href="#S1.E4" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.4</span></a> evaluates exactly to</span></p>
<table id="S2.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{k}\ =\ \min\Bigl\{k,\ \Bigl[\log\frac{m+1}{k}\Bigr]_{+}\Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.Thmremark1.p1.2" class="ltx_p"><span id="S2.Thmremark1.p1.2.1" class="ltx_text ltx_font_italic">Without the truncation, a star with $\lceil e^{2k^{2}}\rceil$ leaves would be assigned $\alpha_{k}\geq k^{2}\text{,}$ hence $V^{2}\alpha_{k}/k\geq A_{0}\sigma^{2}k$ at $V^{2}=A_{0}\sigma^{2}\text{,}$ and the profile-to-risk half of <a href="#S3" title="3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a> would assert a minimax risk of order at least $\sigma^{2}k\text{;}$ for large $k$ this contradicts the bound $R^{*}_{T}\leq V^{2}H_{T}=2A_{0}\sigma^{2}$ furnished by the constant estimator $Vp_{o}\text{,}$ since the star has $H_{T}=2\text{.}$</span></p>
</div>
</div>
<div id="S2.SS2.p2" class="ltx_para">
<p id="S2.SS2.p2.1" class="ltx_p">The root covers every vertex at radius $h_{T}\text{,}$ so $N^{\uparrow}_{T}(r)=1$ for $r\geq h_{T}$ and the supremum in <a href="#S1.E4" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.4</span></a> is effectively over $r&lt;h_{T}\text{.}$ Evaluating the profile exactly involves every integer radius below $h_{T}\text{;}$ a factor-of-two surrogate needs only geometrically spaced ones, and it is the surrogate that the estimator of <a href="#S4" title="4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a> consumes. Define</p>
<table id="S2.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\overline{\delta}_{k}(T):=\frac{2}{k}\,\max_{\begin{subarray}{c}q=2^{\ell}-1,\ \ell\in\{0,1,2,\dots\}\\ 2^{\ell}\leq h_{T}\end{subarray}}\ (q+1)\,\min\Bigl\{k,\ \Bigl[\log\frac{N^{\uparrow}_{T}(q)}{k}\Bigr]_{+}\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(2.1)</span></td></tr></tbody>
</table>
<p id="S2.SS2.p2.2" class="ltx_p">with $\overline{\delta}_{k}(T):=0$ if $h_{T}=0\text{,}$ and the <em id="S2.SS2.p2.2.1" class="ltx_emph ltx_font_italic">algorithmic crossing index</em></p>
<table id="S2.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$k_{\mathrm{alg}}=k_{\mathrm{alg}}(T,V,\sigma):=\min\Bigl\{k\geq 1:\ V^{2}\overline{\delta}_{k}(T)\leq 2A_{0}\sigma^{2}k\ \text{ or }\ k&gt;n/C_{\star}\Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(2.2)</span></td></tr></tbody>
</table>
</div>
<div id="S2.Thmlemma3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma3.2" class="ltx_text ltx_font_bold">Lemma 2.3</span></span><span id="S2.Thmlemma3.3" class="ltx_text ltx_font_bold"> (Profile toolkit).</span></h6>
<div id="S2.Thmlemma3.p1" class="ltx_para">
<p id="S2.Thmlemma3.p1.1" class="ltx_p"><span id="S2.Thmlemma3.p1.1.1" class="ltx_text ltx_font_italic">For every finite rooted tree $T\text{:}$</span></p>
<ol id="S2.I3" class="ltx_enumerate">
<li id="S2.I3.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S2.I3.i1.p1" class="ltx_para">
<p id="S2.I3.i1.p1.1" class="ltx_p">$\delta_{k+1}(T)\leq\delta_{k}(T)\leq h_{T}$<span id="S2.I3.i1.p1.1.1" class="ltx_text ltx_font_italic"> for every
</span>$k\geq 1$<span id="S2.I3.i1.p1.1.2" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S2.I3.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S2.I3.i2.p1" class="ltx_para">
<p id="S2.I3.i2.p1.1" class="ltx_p"><span id="S2.I3.i2.p1.1.1" class="ltx_text ltx_font_italic">for </span>$n\geq 2$<span id="S2.I3.i2.p1.1.2" class="ltx_text ltx_font_italic"> and every </span>$k\geq 1$<span id="S2.I3.i2.p1.1.3" class="ltx_text ltx_font_italic">,</span></p>
<table id="S2.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{k}(T)=\max_{0\leq q&lt;h_{T}}\ (q+1)\,\min\Bigl\{k,\ \Bigl[\log\frac{N^{\uparrow}_{T}(q)}{k}\Bigr]_{+}\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(2.3)</span></td></tr></tbody>
</table>
<p id="S2.I3.i2.p1.2" class="ltx_p"><span id="S2.I3.i2.p1.2.1" class="ltx_text ltx_font_italic">the maximum running over integer radii, and </span>$\alpha_{k}(T)=0$<span id="S2.I3.i2.p1.2.2" class="ltx_text ltx_font_italic"> when
</span>$n=1$<span id="S2.I3.i2.p1.2.3" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S2.I3.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S2.I3.i3.p1" class="ltx_para">
<p id="S2.I3.i3.p1.1" class="ltx_p">$\delta_{k}\leq\overline{\delta}_{k}\leq 2\delta_{k}$<span id="S2.I3.i3.p1.1.1" class="ltx_text ltx_font_italic">
for every </span>$k\geq 1$<span id="S2.I3.i3.p1.1.2" class="ltx_text ltx_font_italic">, the map </span>$k\mapsto\overline{\delta}_{k}(T)$<span id="S2.I3.i3.p1.1.3" class="ltx_text ltx_font_italic"> is
nonincreasing, and</span></p>
<table id="S2.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$k_{\mathrm{alg}}\ \leq\ k_{0}\ \leq\ 2\,k_{\mathrm{alg}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.I3.i3.p1.2" class="ltx_p"><span id="S2.I3.i3.p1.2.1" class="ltx_text ltx_font_italic">Moreover, a minimum ancestor </span>$q$<span id="S2.I3.i3.p1.2.2" class="ltx_text ltx_font_italic">-net can be computed exactly in </span>$O(n)$<span id="S2.I3.i3.p1.2.3" class="ltx_text ltx_font_italic">
operations for each integer </span>$q\geq 0$<span id="S2.I3.i3.p1.2.4" class="ltx_text ltx_font_italic">, by a one-pass
</span><em id="S2.I3.i3.p1.2.5" class="ltx_emph">residual-depth greedy</em><span id="S2.I3.i3.p1.2.6" class="ltx_text ltx_font_italic">; consequently </span>$k_{\mathrm{alg}}$<span id="S2.I3.i3.p1.2.7" class="ltx_text ltx_font_italic"> is computable in
</span>$O(n\log(n+1))$<span id="S2.I3.i3.p1.2.8" class="ltx_text ltx_font_italic"> operations, and </span>$k_{0}$<span id="S2.I3.i3.p1.2.9" class="ltx_text ltx_font_italic"> in </span>$O(n\,h_{T})$<span id="S2.I3.i3.p1.2.10" class="ltx_text ltx_font_italic"> operations.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S2.SS2.p3" class="ltx_para">
<p id="S2.SS2.p3.1" class="ltx_p">The greedy selects a center $q$ levels above a deepest uncovered vertex, or the root when fewer remain; its exactness and the remaining proofs are in <a href="#S1a" title="S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.1</span></a>.</p>
</div>
<div id="S2.SS2.p4" class="ltx_para">
<p id="S2.SS2.p4.1" class="ltx_p"><a href="#S3" title="3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a> now converts the profile into the minimax rate: an upper bound through a coded cover, and a matching lower bound through a positive packing.</p>
</div>
</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-rate-formula"><span class="ltx_tag ltx_tag_section">3 </span>The Rate Formula</h2>

<div id="S3.p1" class="ltx_para">
<p id="S3.p1.1" class="ltx_p">The main theorem of the paper is the rate formula.</p>
</div>
<div id="Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem1.2" class="ltx_text ltx_font_bold">Theorem 1</span></span><span id="Thmtheorem1.3" class="ltx_text ltx_font_bold"> (Rate formula).</span></h6>
<div id="Thmtheorem1.p1" class="ltx_para">
<p id="Thmtheorem1.p1.1" class="ltx_p"><span id="Thmtheorem1.p1.1.1" class="ltx_text ltx_font_italic">There are universal constants $c,C&gt;0$ such that for every finite rooted tree $T$ and all $V,\sigma&gt;0\text{,}$</span></p>
<table id="S3.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$c\,R^{*}_{T}(V,\sigma)\ \leq\ \min\bigl\{V^{2}H_{T},\ \sigma^{2}k_{0}(T,V,\sigma)\bigr\}\ \leq\ C\,R^{*}_{T}(V,\sigma).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S3.p2" class="ltx_para">
<p id="S3.p2.1" class="ltx_p">The formula is insensitive to the choice of $(A_{0},C_{\star})$ in <a href="#S1.E5" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.5</span></a>: any pair for which <a href="#Thmtheorem1" title="Theorem 1 (Rate formula). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a> holds yields a formula $\asymp R^{*}_{T}\text{.}$ The entropy reading is the following.</p>
</div>
<div id="Thmproposition1" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmproposition1.2" class="ltx_text ltx_font_bold">Proposition 1</span></span><span id="Thmproposition1.3" class="ltx_text ltx_font_bold"> (Entropy fixed point).</span></h6>
<div id="Thmproposition1.p1" class="ltx_para">
<p id="Thmproposition1.p1.1" class="ltx_p"><span id="Thmproposition1.p1.1.1" class="ltx_text ltx_font_italic">For every finite rooted tree $T$ and all $V,\sigma&gt;0\text{,}$</span></p>
<table id="S3.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(V,\sigma)\ \asymp\ \min\bigl\{\rho_{T}(V,\sigma),\ V^{2}H_{T},\ \sigma^{2}n\bigr\}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="Thmproposition1.p1.2" class="ltx_p"><span id="Thmproposition1.p1.2.1" class="ltx_text ltx_font_italic">with universal constants.</span></p>
</div>
</div>
<div id="S3.p3" class="ltx_para">
<p id="S3.p3.1" class="ltx_p"><a href="#S3.SS1" title="3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> converts the profile into a coded cover of the flow polytope, yielding the upper bounds and the certificates that the estimators of <a href="#S4" title="4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a> later consume; <a href="#S3.SS2" title="3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.2</span></a> converts the same profile into legal packings and the matching lower bounds; and <a href="#S3.SS3" title="3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> joins the two at the crossing index, proves both statements above, and derives the benchmark corollaries. The assembly is given here; the proofs of the two halves are in <a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Sections</span> <span class="ltx_text ltx_ref_tag">S.2</span></a> and <a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">S.3</span></a>.</p>
</div>
<section id="S3.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-coded-cover"><span class="ltx_tag ltx_tag_subsection">3.1 </span>The Coded Cover</h3>

<div id="S3.SS1.p1" class="ltx_para">
<p id="S3.SS1.p1.1" class="ltx_p">Fix an integer $2\leq k\leq n/C_{\star}\text{.}$ The construction runs at the <em id="S3.SS1.p1.1.1" class="ltx_emph ltx_font_italic">working scale</em></p>
<table id="S3.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\bar{\alpha}\ :=\ k\,\overline{\delta}_{k}(T),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS1.p1.2" class="ltx_p">built from the surrogate <a href="#S2.E1" title="In 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>; the centers, and ultimately the estimator, owe their computability to this one choice. Everything rests on a fixed hierarchy of nets. Set $m_{j}:=2^{j}$ for $0\leq j\leq J\text{,}$ where $m_{J}$ is the largest power of two strictly below $k\text{,}$ let $S_{j}$ be the minimum ancestor $\lfloor\bar{\alpha}/m_{j}\rfloor$-net computed by the residual-depth greedy of <a href="#S2.Thmlemma3" title="Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(<a href="#S2.I3.i3" title="Item 3 ‣ Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), and put $R_{j}:=S_{0}\cup\dots\cup S_{j}\text{,}$ so that $R_{0}\subseteq\dots\subseteq R_{J}$ and each $R_{j}$ is an ancestor $(\bar{\alpha}/m_{j})$-net containing the root. The nets depend only on $(T,k)\text{,}$ not on any signal; every counting statement below rests on this. Their sizes are controlled by the profile itself: $N^{\uparrow}_{T}(\lfloor\bar{\alpha}/m_{j}\rfloor)\leq ke^{m_{j}}\text{,}$ as $m_{j}&lt;k$ and a larger count would make the term of <a href="#S1.E4" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.4</span></a> at that radius exceed $\bar{\alpha}\geq\alpha_{k}(T)\text{;}$ consequently $|R_{j}|\leq 2ke^{m_{j}}\text{.}$</p>
</div>
<div id="S3.SS1.p2" class="ltx_para">
<p id="S3.SS1.p2.1" class="ltx_p">For $v\in\mathsf{V}$ let $a_{j}(v)$ be the deepest ancestor of $v$ in $R_{j}\text{,}$ and call the fibers $B_{a,j}:=\{v:a_{j}(v)=a\}\text{,}$ $a\in R_{j}\text{,}$ the level-$j$ <em id="S3.SS1.p2.1.1" class="ltx_emph ltx_font_italic">cells</em>. At each level the cells partition $\mathsf{V}\text{;}$ each cell is <em id="S3.SS1.p2.1.2" class="ltx_emph ltx_font_italic">rooted-connected</em>, containing with any of its vertices the whole segment from its root $a$ down to that vertex; the cells of level $j+1$ refine those of level $j\text{;}$ and every vertex of a cell is within tree distance $\bar{\alpha}/m_{j}$ of its root. These are elementary consequences of the net property (<a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>).</p>
</div>
<div id="S3.SS1.p3" class="ltx_para">
<p id="S3.SS1.p3.1" class="ltx_p">Define the <em id="S3.SS1.p3.1.1" class="ltx_emph ltx_font_italic">active support</em>, the first-appearance weight, and the <em id="S3.SS1.p3.1.2" class="ltx_emph ltx_font_italic">activation charge</em></p>
<table id="S3.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$A_{k}:=R_{J},\qquad\omega(v):=\min\{m_{j}:\ v\in R_{j}\},\qquad\widetilde{\omega}(v):=\omega(v)\,\mathbf{1}\{v\notin R_{0}\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS1.p3.2" class="ltx_p">and, for an integer vector $z$ supported on $A_{k}\text{,}$ the <em id="S3.SS1.p3.2.1" class="ltx_emph ltx_font_italic">code length</em></p>
<table id="S3.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Gamma(z)\ :=\ \sum_{v\in A_{k}}\Bigl(|z_{v}|+\widetilde{\omega}(v)\,\mathbf{1}\{z_{v}\neq 0\}\Bigr):$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.1)</span></td></tr></tbody>
</table>
<p id="S3.SS1.p3.3" class="ltx_p">coefficient mass, plus a charge on each support vertex equal to its dyadic discovery cost, the coarsest level being free. <a href="#S4" title="4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a> converts exactly this additive functional into a prior.</p>
</div>
<div id="S3.SS1.p4" class="ltx_para">
<p id="S3.SS1.p4.1" class="ltx_p">The next proposition is the key technical result of the upper half. Beyond the covering statement it certifies three additive budgets simultaneously: a fixed root sum, a bounded code length, and a confined flow state. It is through these certificates that the cover later becomes an estimator.</p>
</div>
<div id="S3.Thmlemma1" class="ltx_theorem ltx_theorem_prop">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma1.2" class="ltx_text ltx_font_bold">Proposition 3.1</span></span><span id="S3.Thmlemma1.3" class="ltx_text ltx_font_bold"> (Coded cover).</span></h6>
<div id="S3.Thmlemma1.p1" class="ltx_para">
<p id="S3.Thmlemma1.p1.1" class="ltx_p"><span id="S3.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">There are universal constants $C_{0},C_{1}$ such that for every finite
rooted tree, every $V&gt;0\text{,}$ and every integer $2\leq k\leq n/C_{\star}$ the
following hold.</span></p>
<ol id="S3.I1" class="ltx_enumerate">
<li id="S3.I1.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S3.I1.i1.p1" class="ltx_para">
<p id="S3.I1.i1.p1.1" class="ltx_p"><span id="S3.I1.i1.p1.1.1" class="ltx_text ltx_font_italic">For every </span>$\mu\in\mathcal{F}_{V}(T)$<span id="S3.I1.i1.p1.1.2" class="ltx_text ltx_font_italic"> there is an
integer vector </span>$z$<span id="S3.I1.i1.p1.1.3" class="ltx_text ltx_font_italic"> supported on </span>$A_{k}$<span id="S3.I1.i1.p1.1.4" class="ltx_text ltx_font_italic"> whose flow states
</span>$x_{v}:=\sum_{u\succeq v}z_{u}$<span id="S3.I1.i1.p1.1.5" class="ltx_text ltx_font_italic"> satisfy</span></p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S3.EGx1"></span><span class="paper-eq-anchor" id="S3.Ex5"></span><span class="paper-eq-anchor" id="S3.Ex6"></span><div class="paper-eqgroup-body">$$\begin{gathered}
\displaystyle\sum_{v}z_{v}=k,\qquad\Gamma(z)\leq 9k,\qquad 0\leq x_{v}\leq 3k\ \text{ for all }v\in\mathsf{V}, \\
\displaystyle\Bigl\|\mu-\frac{V}{k}\sum_{v}z_{v}p_{v}\Bigr\|_{2}^{2}\ \leq\ C_{0}V^{2}\delta_{k}(T).
\end{gathered}$$</div><div class="paper-eqgroup-no"></div></div>

</div></li>
<li id="S3.I1.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S3.I1.i2.p1" class="ltx_para">
<p id="S3.I1.i2.p1.1" class="ltx_p"><span id="S3.I1.i2.p1.1.1" class="ltx_text ltx_font_italic">The integer vectors supported on </span>$A_{k}$<span id="S3.I1.i2.p1.1.2" class="ltx_text ltx_font_italic"> that
satisfy the first three constraints displayed in
</span><span id="S3.I1.i2.p1.1.3" class="ltx_text">(<a href="#S3.I1.i1" title="Item 1 ‣ Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>)</span><span id="S3.I1.i2.p1.1.4" class="ltx_text ltx_font_italic"> number at most </span>$e^{C_{1}k}$<span id="S3.I1.i2.p1.1.5" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
<p id="S3.Thmlemma1.p1.2" class="ltx_p"><span id="S3.Thmlemma1.p1.2.1" class="ltx_text ltx_font_italic">Since $A_{k}$ and $\widetilde{\omega}$ depend only on $(T,k)\text{,}$ the centers
built from these vectors form a class</span></p>
<table id="S3.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{D}_{k}\ :=\ \Bigl\{\tfrac{V}{k}\textstyle\sum_{v}z_{v}p_{v}:\ z\in\mathbb{Z}^{A_{k}},\ \sum_{v}z_{v}=k,\ \Gamma(z)\leq 9k,\ 0\leq x_{v}\leq 3k\ \forall v\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.Thmlemma1.p1.3" class="ltx_p"><span id="S3.Thmlemma1.p1.3.1" class="ltx_text ltx_font_italic">the <em id="S3.Thmlemma1.p1.3.1.1" class="ltx_emph ltx_font_upright">coded cover</em>, which does not depend on the signal and covers
$\mathcal{F}_{V}(T)$ at squared radius $C_{0}V^{2}\delta_{k}(T)\text{;}$ in particular</span></p>
<table id="S3.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$H^{c}_{T}\bigl(C_{0}V^{2}\delta_{k}(T)\bigr)\ \leq\ C_{1}k\qquad\text{for every integer }2\leq k\leq n/C_{\star}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.2)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S3.SS1.p5" class="ltx_para">
<p id="S3.SS1.p5.1" class="ltx_p">Members of $\mathcal{D}_{k}$ may carry negative coefficients $z_{v}\text{,}$ so the cover is external to the body, which is why $H^{c}_{T}$ was taken with free centers; in flow coordinates, every member is nonnegative with root coordinate exactly $V$ and no coordinate above $3V\text{.}$</p>
</div>
<div id="S3.SS1.p6" class="ltx_para">
<p id="S3.SS1.p6.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S3.SS1.p7" class="ltx_para">
<p id="S3.SS1.p7.1" class="ltx_p">By homogeneity take $V=1$ and write $f=\sum_{u}\lambda_{u}p_{u}$ in barycentric form (<a href="#S2.Thmlemma1" title="Lemma 2.1 (Normal forms). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>), with $\lambda(B):=\sum_{u\in B}\lambda_{u}\text{.}$ The construction stops a refinement of the cells at the signal’s own masses, collapses each stopped cell to its root, rounds the resulting skeleton, and samples the light exits; the budgets are then read off and the class is counted. The cell properties above, the collapse and exit estimates, the charge and skeleton accounting, and the counting computation are carried out in <a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>.</p>
</div>
<div id="S3.SS1.p8" class="ltx_para">
<p id="S3.SS1.p8.1" class="ltx_p"><em id="S3.SS1.p8.1.1" class="ltx_emph ltx_font_italic">Stopped refinement.</em> Call a level-$j$ cell $B$ <em id="S3.SS1.p8.1.2" class="ltx_emph ltx_font_italic">heavy</em> when $\lambda(B)&gt;m_{j}/k$ and <em id="S3.SS1.p8.1.3" class="ltx_emph ltx_font_italic">light</em> otherwise. Starting from level $0\text{,}$ stop at every light cell, refine every heavy cell, and stop everything at level $J\text{.}$ The <em id="S3.SS1.p8.1.4" class="ltx_emph ltx_font_italic">terminal</em> cells partition $\mathsf{V}\text{;}$ write $\mathcal{L}$ for their collection, and for $L\in\mathcal{L}$ let $a_{L}$ be its root, $m(L)$ its level weight $m_{j}\text{,}$ and $\lambda_{L}:=\lambda(L)\text{.}$ Heaviness is inherited upward through the refinement, so the maximal heavy cells are pairwise disjoint (<a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>) and each has mass exceeding its own $m_{j}/k\text{;}$ since their masses total at most one,</p>
<table id="S3.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{C\ \text{maximal heavy}}m(C)\ &lt;\ k.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.3)</span></td></tr></tbody>
</table>
<p id="S3.SS1.p8.2" class="ltx_p">A heavy terminal cell sits at level $J$ and is maximal, so $m_{J}\geq k/2$ leaves room for at most one.</p>
</div>
<div id="S3.SS1.p9" class="ltx_para">
<p id="S3.SS1.p9.1" class="ltx_p"><em id="S3.SS1.p9.1.1" class="ltx_emph ltx_font_italic">Collapse.</em> Let $g:=\sum_{L\in\mathcal{L}}\lambda_{L}\,p_{a_{L}}\text{.}$ The error blocks $e_{L}:=\sum_{u\in L}\lambda_{u}(p_{u}-p_{a_{L}})$ are supported in $L\setminus\{a_{L}\}$ by rooted-connectedness and <a href="#S2.Thmlemma2" title="Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>(<a href="#S2.I2.i2" title="Item 2 ‣ Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>), so they have pairwise disjoint supports; each is controlled by the radius of its cell and, on a light cell, by its mass, and summing the disjoint blocks gives</p>
<table id="S3.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|f-g\|_{2}^{2}\ \leq\ \frac{3\bar{\alpha}}{k}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.4)</span></td></tr></tbody>
</table>
<p id="S3.SS1.p9.2" class="ltx_p">(<a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>).</p>
</div>
<div id="S3.SS1.p10" class="ltx_para">
<p id="S3.SS1.p10.1" class="ltx_p"><em id="S3.SS1.p10.1.1" class="ltx_emph ltx_font_italic">Skeleton and exits.</em> Let $U$ consist of $R_{0}$ together with the roots of all heavy cells. Attach each terminal cell to $U\text{:}$ set $h(L):=a_{L}$ if $L$ is a level-$0$ cell or the heavy terminal cell; otherwise the parent cell of $L$ is heavy, since $L$ was reached by the refinement, and $h(L)$ is its root, so that $h(L)\in U$ and $h(L)\preceq a_{L}\text{.}$ With $q_{L}:=p_{a_{L}}-p_{h(L)}\text{,}$ <a href="#S2.Thmlemma2" title="Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>(<a href="#S2.I2.i1" title="Item 1 ‣ Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>) and the parent cell’s radius give $\|q_{L}\|_{2}^{2}=d_{T}(h(L),a_{L})\leq 2\bar{\alpha}/m(L)\text{,}$ and</p>
<table id="S3.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$g\ =\ g_{0}+\sum_{L}\lambda_{L}\,q_{L},\qquad g_{0}:=\sum_{h\in U}b_{h}\,p_{h},\quad b_{h}:=\sum_{L:\,h(L)=h}\lambda_{L}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS1.p10.2" class="ltx_p">The nonzero $q_{L}$ are the <em id="S3.SS1.p10.2.1" class="ltx_emph ltx_font_italic">light exits</em>.</p>
</div>
<div id="S3.SS1.p11" class="ltx_para">
<p id="S3.SS1.p11.1" class="ltx_p"><em id="S3.SS1.p11.1.1" class="ltx_emph ltx_font_italic">Preorder rounding.</em> The skeleton masses are rounded through one scalar. List $U$ as $h_{1},\dots,h_{s}$ in a fixed depth-first preorder of $T\text{,}$ write $b_{i}:=b_{h_{i}}$ for the masses in this order, set $B_{0}:=0$ and $B_{i}:=\sum_{\ell\leq i}b_{\ell}\text{,}$ and put</p>
<table id="S3.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Q_{i}\ :=\ \lfloor kB_{i}\rfloor-\lfloor kB_{i-1}\rfloor\ \in\ \mathbb{Z}_{\geq 0},\qquad\text{so that}\qquad\Bigl|\sum_{i\in I}Q_{i}-k\sum_{i\in I}b_{i}\Bigr|\ &lt;\ 1$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS1.p11.2" class="ltx_p">for every interval $I$ of the list, the left side being a difference of two floor errors. Write $Q$ for the vector with entry $Q_{i}$ at $h_{i}$ and zero elsewhere, a nonnegative integer leak vector of total mass $k$ supported on $U$ (<a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>). The point of the preorder is that every subtree $T_{v}$ is a contiguous block of it, so $U\cap T_{v}$ is an interval of the list; coordinates being subtree sums (<a href="#S2.Thmlemma1" title="Lemma 2.1 (Normal forms). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>), the skeleton and its rounding $\bar{g}_{0}:=\frac{1}{k}\sum_{h\in U}Q_{h}\,p_{h}$ differ by less than $1/k$ at every vertex simultaneously. Both signals vanish outside the minimal rooted subtree spanning $U\text{,}$ which has $O(\bar{\alpha}k)$ edges (a chaining argument over the nets; <a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>), whence</p>
<table id="S3.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|g_{0}-\bar{g}_{0}\|_{2}^{2}\ \leq\ C\,\frac{\bar{\alpha}}{k}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.5)</span></td></tr></tbody>
</table>
</div>
<div id="S3.SS1.p12" class="ltx_para">
<p id="S3.SS1.p12.1" class="ltx_p"><em id="S3.SS1.p12.1.1" class="ltx_emph ltx_font_italic">Exit quantization.</em> A light exit has $\lambda_{L}\leq m(L)/k\text{,}$ so the independent variables $Z_{L}:=\frac{m(L)}{k}\,\xi_{L}$ with $\xi_{L}\sim\mathrm{Bernoulli}(k\lambda_{L}/m(L))$ are well defined and unbiased. Independence makes the cross terms vanish in expectation no matter how the exits overlap, so $\mathbb{E}\|\sum_{L}(Z_{L}-\lambda_{L})q_{L}\|_{2}^{2}=\sum_{L}\operatorname{Var}(Z_{L})\|q_{L}\|_{2}^{2}\leq 2\bar{\alpha}/k\text{.}$ The selection weight $W:=\sum_{L}m(L)\mathbf{1}\{Z_{L}\neq 0\}$ has $\mathbb{E}W\leq k\text{;}$ by Markov’s inequality, some realization satisfies both $W\leq 2k$ and squared exit error at most $8\bar{\alpha}/k$ (<a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>). Fix one and define, with $e_{v}$ the coordinate vector at $v\text{,}$ $z:=Q+\sum_{L:\,Z_{L}\neq 0}m(L)\bigl(e_{a_{L}}-e_{h(L)}\bigr)\text{.}$ Each transfer has coefficient sum zero, so $\sum_{v}z_{v}=k\text{;}$ and $z$ is supported on $A_{k}$ with $\|z\|_{1}\leq 5k\text{.}$</p>
</div>
<div id="S3.SS1.p13" class="ltx_para">
<p id="S3.SS1.p13.1" class="ltx_p"><em id="S3.SS1.p13.1.1" class="ltx_emph ltx_font_italic">The flow states.</em> Since $x_{v}=\sum_{u}z_{u}p_{u}(v)\text{,}$ the flow states of $z$ are the coordinates of $\sum_{u}z_{u}p_{u}\text{.}$ The skeleton $Q$ is a nonnegative leak vector of total mass $k\text{,}$ so its states lie in $[0,k]\text{;}$ and each selected transfer contributes $m(L)(p_{a_{L}}-p_{h(L)})=m(L)\mathbf{1}_{(h(L),a_{L}]}\geq 0$ by <a href="#S2.Thmlemma2" title="Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>(<a href="#S2.I2.i2" title="Item 2 ‣ Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>), a downward transport of mass that never creates a negative state and adds at most $m(L)$ to any state. Hence $0\leq x_{v}\leq k+W\leq 3k$ at every vertex.</p>
</div>
<div id="S3.SS1.p14" class="ltx_para">
<p id="S3.SS1.p14.1" class="ltx_p"><em id="S3.SS1.p14.1.1" class="ltx_emph ltx_font_italic">Code length and error.</em> The code length collects the activation charges: the selected exit roots contribute at most $W\leq 2k\text{,}$ and the heavy roots at most $2k\text{,}$ because the level weights along a chain of heavy cells total less than twice that of the maximal cell it descends to, which <a href="#S3.E3" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> caps; so $\Gamma(z)\leq 9k$ (<a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>). The error separates along the three stages of the construction,</p>
<table id="S3.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$f-\frac{1}{k}\sum_{v}z_{v}p_{v}\ =\ (f-g)+(g_{0}-\bar{g}_{0})+\sum_{L}(\lambda_{L}-Z_{L})q_{L},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS1.p14.2" class="ltx_p">so <a href="#S3.E4" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> and <a href="#S3.E5" title="Equation 3.5 ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.5</span></a> and the fixed realization give $\bigl\|f-\frac{1}{k}\sum_{v}z_{v}p_{v}\bigr\|_{2}^{2}\leq C\bar{\alpha}/k=C\overline{\delta}_{k}(T)\leq 2C\delta_{k}(T)$ by <a href="#S2.Thmlemma3" title="Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(<a href="#S2.I3.i3" title="Item 3 ‣ Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>). Restoring the amplitude proves (<a href="#S3.I1.i1" title="Item 1 ‣ Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>).</p>
</div>
<div id="S3.SS1.p15" class="ltx_para">
<p id="S3.SS1.p15.1" class="ltx_p"><em id="S3.SS1.p15.1.1" class="ltx_emph ltx_font_italic">Counting.</em> A vector obeying the three budgets has support split into a free part inside $R_{0}$ and a charged part of total activation charge at most $9k\text{;}$ the net sizes bound each charge group, so a generating-function estimate controls the number of supports, and on a fixed support, $\|z\|_{1}\leq 9k$ bounds the number of coefficient vectors. Multiplying the counts gives (<a href="#S3.I1.i2" title="Item 2 ‣ Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) (<a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>). The covering statement and <a href="#S3.E2" title="In Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.2</span></a> follow from (<a href="#S3.I1.i1" title="Item 1 ‣ Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>) and (<a href="#S3.I1.i2" title="Item 2 ‣ Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>).
∎</p>
</div>
<div id="S3.SS1.p16" class="ltx_para">
<p id="S3.SS1.p16.1" class="ltx_p">Two displays close the upper half. The first is generic. For any $t&gt;0\text{,}$ least squares over a covering of the body at squared radius $t$ with $\log$-cardinality $H^{c}_{T}(t)\text{,}$ or the single center itself when one ball suffices, has risk at most $C(t+\sigma^{2}H^{c}_{T}(t))$ uniformly over the body, by the oracle inequality for least squares over a finite set of candidates (<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>). We optimize over $t$ and adjoin the constant estimator $Vp_{o}\text{,}$ whose risk is at most $\sup_{\mu}\|\mu-Vp_{o}\|_{2}^{2}\leq V^{2}h_{T}$ by convexity and <a href="#S2.Thmlemma2" title="Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>, and the identity estimator $Y\text{,}$ whose risk is $\sigma^{2}n\text{.}$ This gives</p>
<table id="S3.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(V,\sigma)\ \leq\ C\bigl(\rho_{T}(V,\sigma)\wedge V^{2}H_{T}\wedge\sigma^{2}n\bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.6)</span></td></tr></tbody>
</table>
<p id="S3.SS1.p16.2" class="ltx_p">the upper half of <a href="#Thmproposition1" title="Proposition 1 (Entropy fixed point). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">1</span></a>. The second display is where the profile enters: evaluating the infimum <a href="#S1.E6" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.6</span></a> at $t=C_{0}V^{2}\delta_{k}(T)$ and inserting <a href="#S3.E2" title="In Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>,</p>
<table id="S3.E7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\rho_{T}(V,\sigma)\ \leq\ C\bigl(V^{2}\delta_{k}(T)+\sigma^{2}k\bigr)\qquad\text{for every integer }2\leq k\leq n/C_{\star}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.7)</span></td></tr></tbody>
</table>
<p id="S3.SS1.p16.3" class="ltx_p"><a href="#S3.E6" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.6</span></a> knows nothing of the profile; <a href="#S3.E7" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.7</span></a> is what the crossing argument of <a href="#S3.SS3" title="3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> consumes.</p>
</div>
</section>
<section id="S3.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-packing-lower-bound"><span class="ltx_tag ltx_tag_subsection">3.2 </span>The Packing Lower Bound</h3>

<div id="S3.SS2.p1" class="ltx_para">
<p id="S3.SS2.p1.1" class="ltx_p">The lower bound must realize the same entropy through hypotheses that live in the polytope, and here the two structural features of the body bind: a hypothesis may only move leak mass that it actually possesses, and root paths through a common vertex share coordinates, so the hypotheses cannot be taken orthogonal on an arbitrary tree. The construction of this subsection allocates disjoint mass budgets exactly, and measures the overlap it cannot remove.</p>
</div>
<div id="S3.Thmlemma2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma2.2" class="ltx_text ltx_font_bold">Lemma 3.2</span></span><span id="S3.Thmlemma2.3" class="ltx_text ltx_font_bold"> (Cover to packing).</span></h6>
<div id="S3.Thmlemma2.p1" class="ltx_para">
<p id="S3.Thmlemma2.p1.1" class="ltx_p"><span id="S3.Thmlemma2.p1.1.1" class="ltx_text ltx_font_italic">For every $r&gt;0$ there exist at least $N^{\uparrow}_{T}(r)$ vertices of $T$ whose pairwise tree distances are all at least $r/9\text{.}$</span></p>
</div>
</div>
<div id="S3.SS2.p2" class="ltx_para">
<p id="S3.SS2.p2.1" class="ltx_p"><em class="ltx_title_proof">Proof sketch.</em></p>
</div>
<div id="S3.SS2.p3" class="ltx_para">
<p id="S3.SS2.p3.1" class="ltx_p">Under the isometry of <a href="#S2.Thmlemma2" title="Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>(<a href="#S2.I2.i1" title="Item 1 ‣ Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>), a maximal $(\sqrt{r}/3)$-separated subset of $\{p_{u}:u\in\mathsf{V}\}$ is a packing at pairwise tree distances at least $r/9$ and, by maximality, a cover of the same set at Euclidean radius $\sqrt{r}/3\text{.}$ Each covering ball yields one ancestor: the deepest common ancestor of the vertices it captures lies within tree distance $\tfrac{4}{9}\,r$ of each of them, because every captured vertex below it meets some other captured vertex exactly there. Collecting one ancestor per ball gives an ancestor $r$-net, so the balls, and with them the separated vertices, number at least $N^{\uparrow}_{T}(r)$ (<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>).
∎</p>
</div>
<div id="S3.SS2.p4" class="ltx_para">
<p id="S3.SS2.p4.1" class="ltx_p">A product form of Fano’s inequality extracts risk from overlapping hypotheses. The construction in this subsection supplies all three assumptions: blockwise scalability is legality under shrinking toward a reference point, the aspect bound rules out degenerate alphabets, and the Gram row sum is the one quantity through which arbitrary overlap enters.</p>
</div>
<div id="S3.Thmlemma3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma3.2" class="ltx_text ltx_font_bold">Lemma 3.3</span></span><span id="S3.Thmlemma3.3" class="ltx_text ltx_font_bold"> (Fano’s inequality for overlapping blocks).</span></h6>
<div id="S3.Thmlemma3.p1" class="ltx_para">
<p id="S3.Thmlemma3.p1.1" class="ltx_p"><span id="S3.Thmlemma3.p1.1.1" class="ltx_text ltx_font_italic">Let $K\subseteq\mathbb{R}^{N}$ be convex, let $\mathcal{A}_{1},\dots,\mathcal{A}_{J}$ be finite alphabets with $|\mathcal{A}_{j}|\geq 2\text{,}$ and let</span></p>
<table id="S3.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mu_{\mathbf{a}}\ =\ \mu_{0}+\sum_{j=1}^{J}g_{j}(a_{j}),\qquad\mathbf{a}\in\textstyle\prod_{j}\mathcal{A}_{j},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.Thmlemma3.p1.2" class="ltx_p"><span id="S3.Thmlemma3.p1.2.1" class="ltx_text ltx_font_italic">be a family of points of $K\text{.}$ Write $d_{j}^{2}:=\min_{a\neq b}\|g_{j}(a)-g_{j}(b)\|_{2}^{2}\text{,}$ $D_{j}^{2}:=\max_{a,b}\|g_{j}(a)-g_{j}(b)\|_{2}^{2}\text{,}$ and $h_{j}:=\log|\mathcal{A}_{j}|\text{,}$ and assume, for constants $A\geq 1$ and $\gamma&lt;1\text{:}$</span></p>
<ol id="S3.I4" class="ltx_enumerate">
<li id="S3.I4.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S3.I4.i1.p1" class="ltx_para">
<p id="S3.I4.i1.p1.1" class="ltx_p">$\mu_{0}+\sum_{j}\tau_{j}g_{j}(a_{j})\in K$<span id="S3.I4.i1.p1.1.1" class="ltx_text ltx_font_italic"> for every
</span>$\tau\in[0,1]^{J}$<span id="S3.I4.i1.p1.1.2" class="ltx_text ltx_font_italic"> and every </span>$\mathbf{a}$<span id="S3.I4.i1.p1.1.3" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S3.I4.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S3.I4.i2.p1" class="ltx_para">
<p id="S3.I4.i2.p1.1" class="ltx_p">$0&lt;D_{j}^{2}\leq A\,d_{j}^{2}$<span id="S3.I4.i2.p1.1.1" class="ltx_text ltx_font_italic"> for every </span>$j$<span id="S3.I4.i2.p1.1.2" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S3.I4.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S3.I4.i3.p1" class="ltx_para">
<p id="S3.I4.i3.p1.1" class="ltx_p"><span id="S3.I4.i3.p1.1.1" class="ltx_text ltx_font_italic">every family of nonzero contrasts
</span>$\Delta_{j}=g_{j}(a_{j})-g_{j}(b_{j})$<span id="S3.I4.i3.p1.1.2" class="ltx_text ltx_font_italic"> satisfies
</span>$\ \sup_{i}\sum_{j\neq i}\frac{|\langle\Delta_{i},\Delta_{j}\rangle|}{\|\Delta_{i}\|_{2}\,\|\Delta_{j}\|_{2}}\leq\gamma$<span id="S3.I4.i3.p1.1.3" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
<p id="S3.Thmlemma3.p1.3" class="ltx_p"><span id="S3.Thmlemma3.p1.3.1" class="ltx_text ltx_font_italic">Then the minimax risk over $K$ in the model $Y\sim N(\mu,\sigma^{2}I_{N})\text{,}$ $\mu\in K\text{,}$ satisfies</span></p>
<table id="S3.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}(K,\sigma)\ \geq\ c_{A}(1-\gamma)\sum_{j=1}^{J}\min\bigl\{d_{j}^{2},\ \sigma^{2}h_{j}\bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.Thmlemma3.p1.4" class="ltx_p"><span id="S3.Thmlemma3.p1.4.1" class="ltx_text ltx_font_italic">where $c_{A}&gt;0$ depends only on $A\text{.}$ The bound holds already for the Bayes risk of an explicit product prior on a blockwise-shrunken subfamily; and if every contrast $g_{j}(a)-g_{j}(b)$ is supported in a common coordinate set $S\text{,}$ it holds for the loss restricted to $S\text{.}$</span></p>
</div>
</div>
<div id="S3.SS2.p5" class="ltx_para">
<p id="S3.SS2.p5.1" class="ltx_p"><em class="ltx_title_proof">Proof sketch.</em></p>
</div>
<div id="S3.SS2.p6" class="ltx_para">
<p id="S3.SS2.p6.1" class="ltx_p">For a small universal $\eta\text{,}$ shrink each block into its information budget by $\tau_{j}^{2}:=\min\{1,\,\eta\sigma^{2}h_{j}/D_{j}^{2}\}\text{,}$ legal by (<a href="#S3.I4.i1" title="Item 1 ‣ Lemma 3.3 (Fano’s inequality for overlapping blocks). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>), and place the uniform product prior on $\mathbf{a}\text{.}$ The scale-invariant Gram bound (<a href="#S3.I4.i3" title="Item 3 ‣ Lemma 3.3 (Fano’s inequality for overlapping blocks). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>) separates any two shrunken members by $(1-\gamma)\sum_{j}\tau_{j}^{2}\|\Delta_{j}\|_{2}^{2}\text{,}$ overlap paid for once through $\gamma\text{.}$ Revealing all other labels reduces block $j$ to a finite Gaussian test of Kullback–Leibler diameter $O(\eta h_{j})\text{,}$ on which Fano’s inequality <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib36" title="" class="ltx_ref">Tsybakov, 2009</a>)</cite>, or a direct binary test, makes every decoder err with probability at least $\tfrac{1}{4}\text{.}$ Decoding to the nearest shrunken member makes an error at block $j$ cost squared loss of order $(1-\gamma)\tau_{j}^{2}d_{j}^{2}\geq(\eta/A)(1-\gamma)\min\{d_{j}^{2},\sigma^{2}h_{j}\}$ by (<a href="#S3.I4.i2" title="Item 2 ‣ Lemma 3.3 (Fano’s inequality for overlapping blocks). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>). Taking expectations assembles the bound; the per-block constants, the binary-alphabet test, and the restricted-loss variant are in <a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>.
∎</p>
</div>
<div id="S3.SS2.p7" class="ltx_para">
<p id="S3.SS2.p7.1" class="ltx_p">The next proposition realizes these hypotheses inside the flow polytope.</p>
</div>
<div id="S3.Thmlemma4" class="ltx_theorem ltx_theorem_prop">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma4.2" class="ltx_text ltx_font_bold">Proposition 3.4</span></span><span id="S3.Thmlemma4.3" class="ltx_text ltx_font_bold"> (Positive packing).</span></h6>
<div id="S3.Thmlemma4.p1" class="ltx_para">
<p id="S3.Thmlemma4.p1.1" class="ltx_p"><span id="S3.Thmlemma4.p1.1.1" class="ltx_text ltx_font_italic">Let $U\subseteq\mathsf{V}$ consist of $M\geq 2$ vertices with pairwise tree
distances at least $r&gt;0\text{.}$ Then for every integer $1\leq q\leq M/2\text{,}$</span></p>
<table id="S3.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(V,\sigma)\ \geq\ c\,\min\Bigl\{\frac{V^{2}r}{q},\ \sigma^{2}q\log\frac{eM}{q}\Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S3.SS2.p8" class="ltx_para">
<p id="S3.SS2.p8.1" class="ltx_p"><em class="ltx_title_proof">Proof sketch.</em></p>
</div>
<div id="S3.SS2.p9" class="ltx_para">
<p id="S3.SS2.p9.1" class="ltx_p">The construction distributes the budget exactly and lets <a href="#S3.Thmlemma3" title="Lemma 3.3 (Fano’s inequality for overlapping blocks). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> price the overlap; the proof is completed in <a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>.</p>
</div>
<div id="S3.SS2.p10" class="ltx_para">
<p id="S3.SS2.p10.1" class="ltx_p"><em id="S3.SS2.p10.1.1" class="ltx_emph ltx_font_italic">Disjoint budgets.</em> A bin-packing pass from the leaves of the minimal subtree spanning $U$ upward, sealing a connected component whenever it has collected on the order of $M/q$ marked vertices, extracts from $U$ marked sets $U_{1},\dots,U_{q^{\prime}}$ of sizes $M_{i}\asymp M/q$ lying in connected subtrees $\mathcal{C}_{1},\dots,\mathcal{C}_{q^{\prime}}$ with pairwise disjoint edge sets, where $q^{\prime}\asymp q$ (<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>). Give every group the budget $a:=V/q^{\prime}\text{;}$ the budgets sum to $V\text{.}$</p>
</div>
<div id="S3.SS2.p11" class="ltx_para">
<p id="S3.SS2.p11.1" class="ltx_p"><em id="S3.SS2.p11.1.1" class="ltx_emph ltx_font_italic">A multiscale code in each group.</em> Fix a group with marked set $U_{i}\text{.}$ Set $r_{\ell}:=16^{\ell}r$ and let $N_{\ell}\subseteq N_{\ell-1}$ be nested maximal $r_{\ell}$-separated subsets of $N_{0}:=U_{i}\text{;}$ assigning each point of $N_{\ell-1}$ to a point of $N_{\ell}$ within distance $r_{\ell}$ organizes $U_{i}$ into a hierarchy with a singleton top. Descend from the top along children of maximal weight, the weight of a node being the number of members of $U_{i}$ at or below it, so that the child counts along the chain multiply to at least $M_{i}\text{.}$ Discarding single-child levels and keeping one residue class $I$ of the rest modulo four produces alphabets $\mathcal{A}_{\ell}\text{,}$ $\ell\in I\text{,}$ the children of the chain node at level $\ell\text{,}$ with $h_{\ell}:=\log|\mathcal{A}_{\ell}|$ and total entropy $H:=\sum_{\ell\in I}h_{\ell}\geq\tfrac{1}{4}\log M_{i}\text{.}$ Two points of $\mathcal{A}_{\ell}$ are $r_{\ell-1}$-separated and within $2r_{\ell}$ of each other, so each block has aspect at most $32$ (<a href="#S2.Thmlemma2" title="Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>(<a href="#S2.I2.i1" title="Item 1 ‣ Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>)). The per-scale masses $a_{\ell}:=a\sqrt{h_{\ell}/r_{\ell-1}}/S\text{,}$ with normalizer $S:=\sum_{\ell^{\prime}\in I}\sqrt{h_{\ell^{\prime}}/r_{\ell^{\prime}-1}}\text{,}$ spend $\sum_{\ell\in I}a_{\ell}=a$ exactly, and Cauchy–Schwarz against the geometric radii gives</p>
<table id="S3.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{\ell\in I}\min\{a_{\ell}^{2}r_{\ell-1},\,\sigma^{2}h_{\ell}\}\ \geq\ c\min\{a^{2}r,\,\sigma^{2}\log M_{i}\}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS2.p11.2" class="ltx_p">(<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>).
Fix a reference letter $u^{0}_{\ell}\in\mathcal{A}_{\ell}$ at each retained scale; the group’s hypotheses are $\mu_{\mathbf{u}}=\mu_{0}+\sum_{\ell\in I}g_{\ell}(u_{\ell})$ with $\mu_{0}:=\sum_{\ell\in I}a_{\ell}\,p_{u^{0}_{\ell}}$ and $g_{\ell}(u):=a_{\ell}(p_{u}-p_{u^{0}_{\ell}})\text{,}$ so that $\mu_{\mathbf{u}}=\sum_{\ell\in I}a_{\ell}p_{u_{\ell}}$ places mass $a_{\ell}$ at the letter chosen from $\mathcal{A}_{\ell}\text{.}$</p>
</div>
<div id="S3.SS2.p12" class="ltx_para">
<p id="S3.SS2.p12.1" class="ltx_p"><em id="S3.SS2.p12.1.1" class="ltx_emph ltx_font_italic">Overlap.</em> A level-$\ell$ contrast has entries bounded by $a_{\ell}$ and support of size at most $32\,r_{\ell-1}$ (<a href="#S2.Thmlemma2" title="Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>(<a href="#S2.I2.i2" title="Item 2 ‣ Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>)), so its normalized inner product with a level-$\ell^{\prime}$ contrast, $\ell&lt;\ell^{\prime}$ in $I\text{,}$ is at most $32\cdot 4^{-(\ell^{\prime}-\ell)}\text{;}$ retained levels differ by at least four, so every normalized Gram row sums to at most $\gamma=64/255&lt;\tfrac{1}{2}\text{.}$</p>
</div>
<div id="S3.SS2.p13" class="ltx_para">
<p id="S3.SS2.p13.1" class="ltx_p"><em id="S3.SS2.p13.1.1" class="ltx_emph ltx_font_italic">Assembly.</em> Each blockwise contraction $\mu_{0}+\sum_{\ell}\tau_{\ell}g_{\ell}(u_{\ell})$ replaces $p_{u^{0}_{\ell}}$ by a convex combination of $p_{u^{0}_{\ell}}$ and $p_{u_{\ell}}\text{,}$ so it remains a nonnegative leak combination of total mass $a\text{;}$ <a href="#S3.Thmlemma3" title="Lemma 3.3 (Fano’s inequality for overlapping blocks). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> therefore applies with $A=32$ and $\gamma=64/255$ and bounds the group’s Bayes risk from below by $c\min\{a^{2}r,\sigma^{2}\log M_{i}\}$ in the group’s own coordinates. Sums of one member per group are legal points of $\mathcal{F}_{V}(T)$ (<a href="#S2.Thmlemma1" title="Lemma 2.1 (Normal forms). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>), and the groups’ contrasts occupy the pairwise disjoint edge supports of the $\mathcal{C}_{i}$ (<a href="#S2.Thmlemma2" title="Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>(<a href="#S2.I2.i2" title="Item 2 ‣ Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>)), so the joint Bayes risk dominates the sum of the isolated group bounds (<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>). With $q^{\prime}\asymp q$ and $M_{i}\asymp M/q\text{,}$ the group bounds sum to $R^{*}_{T}(V,\sigma)\geq c\,q\min\{V^{2}r/q^{2},\,\sigma^{2}\log(eM/q)\}\text{,}$ which is the claim.
∎</p>
</div>
<div id="S3.SS2.p14" class="ltx_para">
<p id="S3.SS2.p14.1" class="ltx_p">The lower half of the crossing now follows by matching the free parameter $q$ to the profile.</p>
</div>
<div id="S3.Thmlemma5" class="ltx_theorem ltx_theorem_prop">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma5.2" class="ltx_text ltx_font_bold">Proposition 3.5</span></span><span id="S3.Thmlemma5.3" class="ltx_text ltx_font_bold"> (Profile to risk).</span></h6>
<div id="S3.Thmlemma5.p1" class="ltx_para">
<p id="S3.Thmlemma5.p1.1" class="ltx_p"><span id="S3.Thmlemma5.p1.1.1" class="ltx_text ltx_font_italic">There is a universal constant $c_{0}&gt;0$ such that for every finite
rooted tree, every integer $k\geq 1\text{,}$ and all $V,\sigma&gt;0\text{,}$</span></p>
<table id="S3.Ex15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}\delta_{k}(T)\ \geq\ A_{0}\sigma^{2}k\qquad\Longrightarrow\qquad R^{*}_{T}(V,\sigma)\ \geq\ c_{0}\,\sigma^{2}k.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S3.SS2.p15" class="ltx_para">
<p id="S3.SS2.p15.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S3.SS2.p16" class="ltx_para">
<p id="S3.SS2.p16.1" class="ltx_p">The supremum in <a href="#S1.E4" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.4</span></a> need not be attained, so choose $r&gt;0$ whose term is at least half the supremum:</p>
<table id="S3.Ex16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}r\,\min\Bigl\{1,\ \tfrac{1}{k}\Bigl[\log\tfrac{N^{\uparrow}_{T}(r)}{k}\Bigr]_{+}\Bigr\}\ \geq\ \tfrac{1}{2}\,V^{2}\delta_{k}(T)\ \geq\ \tfrac{A_{0}}{2}\,\sigma^{2}k\ &gt;\ 0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS2.p16.2" class="ltx_p">Positivity forces $N^{\uparrow}_{T}(r)&gt;k\text{.}$ <a href="#S3.Thmlemma2" title="Lemma 3.2 (Cover to packing). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.2</span></a> supplies $M\geq N^{\uparrow}_{T}(r)&gt;k$ vertices with pairwise tree distances at least $r^{\prime}:=r/9\text{,}$ and the displayed inequality survives with $(r^{\prime},M)$ in place of $(r,N^{\uparrow}_{T}(r))$ at the cost of a factor $18\text{,}$ absorbed into $A_{0}\text{.}$ It remains to choose $q$ in <a href="#S3.Thmlemma4" title="Proposition 3.4 (Positive packing). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.4</span></a>: the mass branch $V^{2}r^{\prime}/q$ shrinks and the entropy branch $\sigma^{2}q\log(eM/q)$ grows as $q$ increases, and at $q\asymp\max\bigl\{1,\ k/(1+\log(M/k))\bigr\}$ both sit above $\sigma^{2}k$ times a universal constant. This scalar matching, including the boundary cases, is proved in <a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>.
∎</p>
</div>
</section>
<section id="S3.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-crossing-and-the-benchmarks"><span class="ltx_tag ltx_tag_subsection">3.3 </span>The Crossing and the Benchmarks</h3>

<div id="S3.SS3.p1" class="ltx_para">
<p id="S3.SS3.p1.1" class="ltx_p">The two halves now meet. Throughout, $K:=\lfloor n/C_{\star}\rfloor\text{,}$ so that $k_{0}\leq K+1$ by <a href="#S1.E5" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.5</span></a>.</p>
</div>
<div id="S3.SS3.p2" class="ltx_para">
<p id="S3.SS3.p2.1" class="ltx_p"><em class="ltx_title_proof">Proof of <a class="ltx_ref" href="#Thmtheorem1">Theorem 1</a> and <a class="ltx_ref" href="#Thmproposition1">Proposition 1</a>.</em></p>
</div>
<div id="S3.SS3.p3" class="ltx_para">
<p id="S3.SS3.p3.1" class="ltx_p">The upper half of <a href="#Thmproposition1" title="Proposition 1 (Entropy fixed point). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">1</span></a> is <a href="#S3.E6" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.6</span></a>; it remains to prove</p>
<table id="S3.Ex17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\text{(I)}\quad R^{*}_{T}\ \geq\ c\,\bigl(\rho_{T}\wedge V^{2}H_{T}\wedge\sigma^{2}n\bigr),\qquad\qquad\text{(II)}\quad R^{*}_{T}\ \asymp\ \min\bigl\{V^{2}H_{T},\ \sigma^{2}k_{0}\bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS3.p3.2" class="ltx_p">For $n=1$ the body is the single point $Vp_{o}$ and $H_{T}=0\text{,}$ so $R^{*}_{T}=0$ and both sides of (I) and (II) vanish; assume $n\geq 2\text{.}$ Testing two points at distance $\min\{V\sqrt{H_{T}},\sigma\}$ along the diameter segment of the body, which lies in $\mathcal{F}_{V}(T)$ by <a href="#S2.Thmlemma2" title="Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>(<a href="#S2.I2.i1" title="Item 1 ‣ Lemma 2.2 (Isometry and edge supports). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>), records a two-point bound</p>
<table id="S3.E8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(V,\sigma)\ \geq\ c\,\min\bigl\{V^{2}H_{T},\ \sigma^{2}\bigr\}\qquad(n\geq 2)$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.8)</span></td></tr></tbody>
</table>
<p id="S3.SS3.p3.3" class="ltx_p">(<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>). The proof of (I) and (II) now splits into four exhaustive cases, according to how the crossing index fires.</p>
</div>
<div id="S3.SS3.p4" class="ltx_para">
<p id="S3.SS3.p4.1" class="ltx_p"><em id="S3.SS3.p4.1.1" class="ltx_emph ltx_font_italic">Case $n&lt;C_{\star}\text{.}$</em> Here $k_{0}=1$ through the dimension clause, and $\sigma^{2}\geq\sigma^{2}n/C_{\star}\text{,}$ so <a href="#S3.E8" title="In 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.8</span></a> gives (I) and the lower half of (II), while <a href="#S3.E6" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.6</span></a> gives the upper half (<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>).</p>
</div>
<div id="S3.SS3.p5" class="ltx_para">
<p id="S3.SS3.p5.1" class="ltx_p"><em id="S3.SS3.p5.1.1" class="ltx_emph ltx_font_italic">Case $n\geq C_{\star}$ and $V^{2}\delta_{1}\leq A_{0}\sigma^{2}\text{.}$</em> Here $k_{0}=1$ through the crossing clause. <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> starts at $k=2\text{,}$ so we supply the missing entropy bound at $k=1\text{.}$ Every ancestor $r$-net with $r&lt;h_{T}$ has at least two elements: the root lies in every net, being its own only ancestor, and it covers no deepest vertex. Hence $N^{\uparrow}_{T}(r)\geq 2$ for all $r&lt;h_{T}\text{,}$ and letting $r\uparrow h_{T}$ in <a href="#S1.E4" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.4</span></a> gives $\alpha_{1}\geq h_{T}\log 2\text{.}$ On the other hand the single center $Vp_{o}$ covers the body at squared radius $V^{2}h_{T}\text{,}$ since $\|\mu-Vp_{o}\|_{2}\leq\max_{u}\|Vp_{u}-Vp_{o}\|_{2}=V\sqrt{h_{T}}$ by convexity, so $H^{c}_{T}(V^{2}h_{T})=0$ and</p>
<table id="S3.Ex18" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\rho_{T}\ \leq\ V^{2}h_{T}\ \leq\ \frac{V^{2}\delta_{1}}{\log 2}\ \leq\ \frac{A_{0}}{\log 2}\,\sigma^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS3.p5.2" class="ltx_p">Both (I) and (II) follow, with <a href="#S3.E8" title="In 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.8</span></a> for the lower bounds and <a href="#S3.E6" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.6</span></a> for the upper ones (<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>).</p>
</div>
<div id="S3.SS3.p6" class="ltx_para">
<p id="S3.SS3.p6.1" class="ltx_p"><em id="S3.SS3.p6.1.1" class="ltx_emph ltx_font_italic">Case $2\leq k_{0}\leq K\text{.}$</em> The crossing clause fired at $k_{0}\text{:}$ $V^{2}\delta_{k_{0}}\leq A_{0}\sigma^{2}k_{0}\text{,}$ and $k_{0}\leq n/C_{\star}\text{,}$ so <a href="#S3.E7" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.7</span></a> at $k_{0}$ gives</p>
<table id="S3.E9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\rho_{T}\ \leq\ C\bigl(V^{2}\delta_{k_{0}}+\sigma^{2}k_{0}\bigr)\ \leq\ C(A_{0}+1)\,\sigma^{2}k_{0}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.9)</span></td></tr></tbody>
</table>
<p id="S3.SS3.p6.2" class="ltx_p">By minimality neither clause holds at $k_{0}-1\text{;}$ in particular $V^{2}\delta_{k_{0}-1}&gt;A_{0}\sigma^{2}(k_{0}-1)\text{,}$ so <a href="#S3.Thmlemma5" title="Proposition 3.5 (Profile to risk). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.5</span></a> at $k_{0}-1$ gives</p>
<table id="S3.E10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}\ \geq\ c_{0}\,\sigma^{2}(k_{0}-1)\ \geq\ \frac{c_{0}}{2}\,\sigma^{2}k_{0}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.10)</span></td></tr></tbody>
</table>
<p id="S3.SS3.p6.3" class="ltx_p">Combining <a href="#S3.E9" title="In 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">3.9</span></a> and <a href="#S3.E10" title="Equation 3.10 ‣ 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.10</span></a> proves (I). For (II) the same two inequalities identify the information branch: $V^{2}H_{T}\geq V^{2}h_{T}\geq V^{2}\delta_{k_{0}-1}&gt;A_{0}\sigma^{2}(k_{0}-1)\geq\sigma^{2}k_{0}$ by <a href="#S2.Thmlemma3" title="Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(<a href="#S2.I3.i1" title="Item 1 ‣ Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>), so $\min\{V^{2}H_{T},\sigma^{2}k_{0}\}=\sigma^{2}k_{0}\text{,}$ which <a href="#S3.E10" title="In 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.10</span></a> bounds below and <a href="#S3.E6" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">3.6</span></a> and <a href="#S3.E9" title="Equation 3.9 ‣ 3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.9</span></a> bound above.</p>
</div>
<div id="S3.SS3.p7" class="ltx_para">
<p id="S3.SS3.p7.1" class="ltx_p"><em id="S3.SS3.p7.1.1" class="ltx_emph ltx_font_italic">Case $k_{0}=K+1$ with $n\geq C_{\star}\text{.}$</em> No clause fired on $[1,K]\text{;}$ in particular $V^{2}\delta_{K}&gt;A_{0}\sigma^{2}K\text{,}$ so <a href="#S3.Thmlemma5" title="Proposition 3.5 (Profile to risk). ‣ 3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.5</span></a> at $K$ gives $R^{*}_{T}\geq c_{0}\sigma^{2}K\geq c\,\sigma^{2}n\text{,}$ using $K=\lfloor n/C_{\star}\rfloor\geq n/(2C_{\star})\text{.}$ This is (I), the three-term minimum being at most $\sigma^{2}n\text{;}$ and (II) follows because $\sigma^{2}k_{0}\asymp\sigma^{2}n$ while $V^{2}H_{T}\geq V^{2}\delta_{K}&gt;A_{0}\sigma^{2}K$ (<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>).</p>
</div>
<div id="S3.SS3.p8" class="ltx_para">
<p id="S3.SS3.p8.1" class="ltx_p">The four cases are exhaustive: for $n\geq C_{\star}\text{,}$ either the crossing clause fires at $k=1\text{,}$ or it first fires at some $2\leq k_{0}\leq K\text{,}$ or it never fires on $[1,K]$ and the dimension clause fires at $K+1\text{.}$ This proves (I) and (II). In the interior case the computation also pins the fixed point itself, $\rho_{T}\asymp\sigma^{2}k_{0}$ (<a href="#S3a" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.3</span></a>).
∎</p>
</div>
<div id="S3.SS3.p9" class="ltx_para">
<p id="S3.SS3.p9.1" class="ltx_p">The rate formula specializes in closed form on the three families of <a href="#S1.T1" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Table</span> <span class="ltx_text ltx_ref_tag">1</span></a>; in each corollary the equivalence holds for all $V,\sigma&gt;0$ with universal constants.</p>
</div>
<div id="Thmcorollary1" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmcorollary1.2" class="ltx_text ltx_font_bold">Corollary 1</span></span><span id="Thmcorollary1.3" class="ltx_text ltx_font_bold"> (Path).</span></h6>
<div id="Thmcorollary1.p1" class="ltx_para">
<p id="Thmcorollary1.p1.1" class="ltx_p"><span id="Thmcorollary1.p1.1.1" class="ltx_text ltx_font_italic">Let $P_{L}$ be the path with $L\geq 1$ edges, rooted at one endpoint, so that $\mathcal{F}_{V}(P_{L})=\{\mu:V=\mu_{0}\geq\mu_{1}\geq\cdots\geq\mu_{L}\geq 0\}\text{.}$ Then</span></p>
<table id="S3.Ex19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{P_{L}}(V,\sigma)\ \asymp\ \min\bigl\{V^{2}L,\ \ V^{2/3}\sigma^{4/3}L^{1/3},\ \ \sigma^{2}(L+1)\bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="Thmcorollary2" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmcorollary2.2" class="ltx_text ltx_font_bold">Corollary 2</span></span><span id="Thmcorollary2.3" class="ltx_text ltx_font_bold"> (Star).</span></h6>
<div id="Thmcorollary2.p1" class="ltx_para">
<p id="Thmcorollary2.p1.1" class="ltx_p"><span id="Thmcorollary2.p1.1.1" class="ltx_text ltx_font_italic">Let $S_{m}$ be the star with $m\geq 2$ leaves rooted at the hub; the hub coordinate is pinned at $V\text{,}$ and in leaf coordinates $\mathcal{F}_{V}(S_{m})=\{\mu\in\mathbb{R}_{\geq 0}^{m}:\sum_{i\leq m}\mu_{i}\leq V\}\text{.}$ Then</span></p>
<table id="S3.Ex20" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{S_{m}}(V,\sigma)\ \asymp\ \min\Bigl\{V^{2},\ \ \sigma V\sqrt{1+\bigl[\log(m\sigma/V)\bigr]_{+}},\ \ \sigma^{2}m\Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="Thmcorollary3" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmcorollary3.2" class="ltx_text ltx_font_bold">Corollary 3</span></span><span id="Thmcorollary3.3" class="ltx_text ltx_font_bold"> (Complete binary tree).</span></h6>
<div id="Thmcorollary3.p1" class="ltx_para">
<p id="Thmcorollary3.p1.1" class="ltx_p"><span id="Thmcorollary3.p1.1.1" class="ltx_text ltx_font_italic">Let $B_{h}$ be the complete binary tree of height $h\geq 1\text{:}$ every internal vertex has two children and all $2^{h}$ leaves lie at depth $h\text{,}$ so that $n=2^{h+1}-1\text{.}$ Then</span></p>
<table id="S3.Ex21" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{B_{h}}(V,\sigma)\ \asymp\ \min\bigl\{V^{2}h,\ \ \sigma V\bigl(1+[\log(n\sigma/V)]_{+}\bigr),\ \ \sigma^{2}n\bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S3.SS3.p10" class="ltx_para">
<p id="S3.SS3.p10.1" class="ltx_p">The three corollaries follow one recipe: the ancestor-covering counts determine the profile through <a href="#S2.E3" title="In Item 2 ‣ Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>, and the crossing selects the active branch. Interval covering gives the path counts $\lceil(L+1)/(q+1)\rceil\text{;}$ on the star only the radius $q=0$ contributes, and the profile is the exact expression of <a href="#S2.Thmremark1" title="Remark 2.1 (Why the profile is truncated). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>; on the binary tree the counts decay geometrically in the radius, and, for $k\leq n/C_{\star}\text{,}$ the profile $\alpha_{k}$ is quadratic in $\log(n/k)$ wherever $k$ exceeds that logarithm. The counts, the profiles, and the scalar optimizations that locate $k_{0}$ and match the branches in every parameter regime are carried out in <a href="#S4a" title="S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.4</span></a>.</p>
</div>
<div id="S3.SS3.p11" class="ltx_para">
<p id="S3.SS3.p11.1" class="ltx_p">The crossing consumed <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> only through <a href="#S3.E2" title="In Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>; the further certificates are spent in <a href="#S4" title="4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a>, the code length becoming a prior, the root sum an exact constraint, and the confined states a one-dimensional computation.</p>
</div>
</section>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="efficient-and-adaptive-estimation"><span class="ltx_tag ltx_tag_section">4 </span>Efficient and Adaptive Estimation</h2>

<div id="S4.p1" class="ltx_para">
<p id="S4.p1.1" class="ltx_p">This section proves the three estimation theorems; the first is stated here, the adaptation pair in <a href="#S4.SS3" title="4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.3</span></a>.</p>
</div>
<div id="Thmtheorem2" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem2.2" class="ltx_text ltx_font_bold">Theorem 2</span></span><span id="Thmtheorem2.3" class="ltx_text ltx_font_bold"> (Efficient estimation).</span></h6>
<div id="Thmtheorem2.p1" class="ltx_para">
<p id="Thmtheorem2.p1.1" class="ltx_p"><span id="Thmtheorem2.p1.1.1" class="ltx_text ltx_font_italic">There is a deterministic estimator $\widehat{\mu}=\widehat{\mu}(T,V,\sigma,Y)\text{,}$ computed exactly in $O(n^{2}\log(n+1))$ arithmetic operations of the real-RAM model fixed in <a href="#S2.SS1" title="2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, such that for every finite rooted tree $T$ and all $V,\sigma&gt;0\text{,}$</span></p>
<table id="S4.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sup_{\mu\in\mathcal{F}_{V}(T)}\mathbb{E}_{\mu}\bigl\|\widehat{\mu}-\mu\bigr\|_{2}^{2}\ \leq\ C\,R^{*}_{T}(V,\sigma)$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="Thmtheorem2.p1.2" class="ltx_p"><span id="Thmtheorem2.p1.2.1" class="ltx_text ltx_font_italic">with a universal constant $C\text{.}$</span></p>
</div>
</div>
<div id="S4.p2" class="ltx_para">
<p id="S4.p2.1" class="ltx_p">The estimator is an exponentially weighted aggregate over a class of integer states, evaluated exactly in the sense fixed by <a href="#S4.Thmremark1" title="Remark 4.1 (Computational model). ‣ 4.2 Exact Evaluation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>. <a href="#S4.SS1" title="4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.1</span></a> constructs it and proves the risk bound, <a href="#S4.SS2" title="4.2 Exact Evaluation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> gives the algorithm, and <a href="#S4.SS3" title="4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> removes first the budget and then the noise level.</p>
</div>
<section id="S4.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="aggregation-over-integer-states"><span class="ltx_tag ltx_tag_subsection">4.1 </span>Aggregation over Integer States</h3>

<div id="S4.SS1.p1" class="ltx_para">
<p id="S4.SS1.p1.1" class="ltx_p">Least squares over the coded cover converts <a href="#S3.E2" title="In Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.2</span></a> into the rate, but it is a search through as many as $e^{C_{1}k}$ centers (<a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>). The estimator of <a href="#Thmtheorem2" title="Theorem 2 (Efficient estimation). ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> replaces the search by an average under a prior built from the code length.</p>
</div>
<div id="S4.SS1.p2" class="ltx_para">
<p id="S4.SS1.p2.1" class="ltx_p">Fix an integer $2\leq k\leq n/C_{\star}$ and recall the active support $A_{k}\text{,}$ the charges $\widetilde{\omega}\text{,}$ and the code length <a href="#S3.E1" title="In 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>. The <em id="S4.SS1.p2.1.1" class="ltx_emph ltx_font_italic">integer states</em> at budget $k$ are the vectors</p>
<table id="S4.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{X}_{k}\ :=\ \Bigl\{x\in\{0,1,\dots,3k\}^{\mathsf{V}}:\ x_{o}=k\ \text{ and }\ z_{v}:=x_{v}-\textstyle\sum_{c\in\operatorname{ch}(v)}x_{c}=0\ \text{ for all }v\notin A_{k}\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4.1)</span></td></tr></tbody>
</table>
<p id="S4.SS1.p2.2" class="ltx_p">each with its leak vector $z\text{,}$ its code length $\Gamma(x):=\Gamma(z)\text{,}$ and its center $\nu_{x}:=\frac{V}{k}\,x\text{;}$ the leaks telescope to the root state, $\sum_{v}z_{v}=x_{o}=k\text{.}$ The approximant of <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> is an integer state: its coordinates lie in $[0,3k]\text{,}$ its root coordinate is $k\text{,}$ and its leaks are supported on $A_{k}\text{.}$ The class relaxes the coded cover in exactly one respect: the budget $\Gamma\leq 9k$ is dropped from the constraints, so that $\mathcal{D}_{k}=\{\nu_{x}:\ x\in\mathcal{X}_{k},\ \Gamma(x)\leq 9k\}\text{.}$ The dropped budget resurfaces as the prior: as a constraint it would add a second dimension to the recursions of <a href="#S4.SS2" title="4.2 Exact Evaluation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>; as a soft penalty it costs only a normalizing sum. Their leaks may be negative, as for the coded cover.</p>
</div>
<div id="S4.SS1.p3" class="ltx_para">
<p id="S4.SS1.p3.1" class="ltx_p">The estimator at budget $k$ is the exponentially weighted aggregate</p>
<table id="S4.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{\mu}_{k}\ :=\ \frac{\sum_{x\in\mathcal{X}_{k}}\nu_{x}\,e^{-2\Gamma(x)}\,e^{-\|Y-\nu_{x}\|_{2}^{2}/(4\sigma^{2})}}{\sum_{x\in\mathcal{X}_{k}}e^{-2\Gamma(x)}\,e^{-\|Y-\nu_{x}\|_{2}^{2}/(4\sigma^{2})}}\ ,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4.2)</span></td></tr></tbody>
</table>
<p id="S4.SS1.p3.2" class="ltx_p">the posterior mean at temperature $4\sigma^{2}$ under the Kraft-type prior $\pi_{k}(x)\propto e^{-2\Gamma(x)}\text{.}$ The normalizing sum $\sum_{x\in\mathcal{X}_{k}}e^{-2\Gamma(x)}\text{,}$ which cancels from <a href="#S4.E2" title="In 4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> and is never computed, is at most $e^{k}\text{,}$ by a generating-function estimate from the net sizes of <a href="#S3.SS1" title="3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> (<a href="#S5a" title="S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.5</span></a>). Every integer state has root coordinate $k$ and coordinates at most $3k\text{,}$ so $\widehat{\mu}_{k}(o)=V$ identically and every coordinate of $\widehat{\mu}_{k}$ lies in $[0,3V]\text{.}$</p>
</div>
<div id="S4.SS1.p4" class="ltx_para">
<p id="S4.SS1.p4.1" class="ltx_p">The risk of an exponentially weighted aggregate is controlled through the prior mass at a single candidate; no cardinality of the class enters <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib25" title="" class="ltx_ref">Leung and Barron, 2006</a>, cf.)</cite>. In the next lemma the true mean is arbitrary.</p>
</div>
<div id="S4.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma 4.1</span></span><span id="S4.Thmlemma1.3" class="ltx_text ltx_font_bold"> (Aggregation oracle).</span></h6>
<div id="S4.Thmlemma1.p1" class="ltx_para">
<p id="S4.Thmlemma1.p1.1" class="ltx_p"><span id="S4.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">Let $F\subseteq\mathbb{R}^{N}$ be finite and nonempty, let $\pi$ be a probability vector on $F$ with $\pi_{f}&gt;0$ for all $f\text{,}$ and let $Y=\mu+\sigma Z$ with $Z\sim N(0,I_{N})$ and $\mu\in\mathbb{R}^{N}\text{.}$ Define</span></p>
<table id="S4.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{f}_{\pi}(Y)\ :=\ \sum_{f\in F}\widehat{\pi}_{f}(Y)\,f,\qquad\widehat{\pi}_{f}(Y)\ :=\ \frac{\pi_{f}\,e^{-\|Y-f\|_{2}^{2}/(4\sigma^{2})}}{\sum_{g\in F}\pi_{g}\,e^{-\|Y-g\|_{2}^{2}/(4\sigma^{2})}}\ .$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.Thmlemma1.p1.2" class="ltx_p"><span id="S4.Thmlemma1.p1.2.1" class="ltx_text ltx_font_italic">Then</span></p>
<table id="S4.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}_{\mu}\bigl\|\widehat{f}_{\pi}-\mu\bigr\|_{2}^{2}\ \leq\ \min_{f\in F}\Bigl\{\|f-\mu\|_{2}^{2}+4\sigma^{2}\log\frac{1}{\pi_{f}}\Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4.SS1.p5" class="ltx_para">
<p id="S4.SS1.p5.1" class="ltx_p"><em class="ltx_title_proof">Proof sketch.</em></p>
</div>
<div id="S4.SS1.p6" class="ltx_para">
<p id="S4.SS1.p6.1" class="ltx_p">Two exact identities. Differentiating the weights shows that the aggregate is smooth and bounded and identifies its Jacobian as $\frac{1}{2\sigma^{2}}$ times the posterior covariance of $f\text{,}$ so Stein’s identity <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib35" title="" class="ltx_ref">Stein, 1981</a>)</cite> writes the risk through the divergence, a covariance trace; the bias–variance split of the posterior loss $\sum_{f}\widehat{\pi}_{f}(y)\,\|y-f\|_{2}^{2}$ produces the same trace with the opposite sign, and at this temperature the two cancel exactly, leaving $\mathbb{E}_{\mu}\|\widehat{f}_{\pi}-\mu\|_{2}^{2}=\mathbb{E}\sum_{f}\widehat{\pi}_{f}(Y)\,\|Y-f\|_{2}^{2}-N\sigma^{2}\text{.}$ The weights are the Gibbs minimizer of the posterior loss penalized by $4\sigma^{2}$ times the relative entropy to $\pi$ <cite class="ltx_cite ltx_citemacro_citep">(see, e.g., <a href="#bib.bib37" title="" class="ltx_ref">Boucheron et al., 2013</a>, Section 4.9)</cite>, so the value of the penalized objective at the point mass on any $f_{0}\in F$ bounds the posterior loss pathwise by $\|Y-f_{0}\|_{2}^{2}+4\sigma^{2}\log(1/\pi_{f_{0}})\text{;}$ take expectations and insert $\mathbb{E}\|Y-f_{0}\|^{2}=\|f_{0}-\mu\|^{2}+N\sigma^{2}\text{.}$ The differentiation, the domain of Stein’s identity, and the two expansions are carried out in <a href="#S5a" title="S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.5</span></a>.
∎</p>
</div>
<div id="S4.SS1.p7" class="ltx_para">
<p id="S4.SS1.p7.1" class="ltx_p">Set $K:=\lfloor n/C_{\star}\rfloor$ as in <a href="#S3.SS3" title="3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>. From here through <a href="#S4.SS2" title="4.2 Exact Evaluation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>, set $k:=k_{\mathrm{alg}}(T,V,\sigma)\text{,}$ the algorithmic crossing index of <a href="#S2.Thmlemma3" title="Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(<a href="#S2.I3.i3" title="Item 3 ‣ Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), so that $k\leq K+1\text{.}$ The root coordinate carries no statistical content (<a href="#S2.SS1" title="2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>), so define the root-corrected observation $\widetilde{Y}$ by $\widetilde{Y}(o):=V$ and $\widetilde{Y}(v):=Y(v)$ for $v\neq o\text{.}$ The estimator of <a href="#Thmtheorem2" title="Theorem 2 (Efficient estimation). ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> is</p>
<table id="S4.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{\mu}\ :=\ \begin{cases}Vp_{o},&amp;V^{2}H_{T}\leq\sigma^{2}k,\\ \widetilde{Y},&amp;V^{2}H_{T}&gt;\sigma^{2}k\ \text{ and }\ k&gt;K,\\ Vp_{o},&amp;V^{2}H_{T}&gt;\sigma^{2}k\ \text{ and }\ k=1\leq K,\\ \widehat{\mu}_{k},&amp;V^{2}H_{T}&gt;\sigma^{2}k\ \text{ and }\ 2\leq k\leq K,\end{cases},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4.3)</span></td></tr></tbody>
</table>
<p id="S4.SS1.p7.2" class="ltx_p">four exclusive and exhaustive branches: when the diameter is not the active scale, the index $k$ either exceeds the dimension range, or is too small for <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>, or is interior.</p>
</div>
<div id="S4.SS1.p8" class="ltx_para">
<p id="S4.SS1.p8.1" class="ltx_p">The risk bound of <a href="#Thmtheorem2" title="Theorem 2 (Efficient estimation). ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> follows. In the interior branch <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> applies, and evaluating the oracle of <a href="#S4.Thmlemma1" title="Lemma 4.1 (Aggregation oracle). ‣ 4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.1</span></a> at the approximant $x^{\star}$ of a given $\mu\in\mathcal{F}_{V}(T)\text{,}$ with $\log(1/\pi_{k}(x^{\star}))\leq 2\Gamma(x^{\star})+k\leq 19k\text{,}$ gives</p>
<table id="S4.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sup_{\mu\in\mathcal{F}_{V}(T)}\mathbb{E}_{\mu}\bigl\|\widehat{\mu}_{k}-\mu\bigr\|_{2}^{2}\ \leq\ C_{0}V^{2}\delta_{k}(T)+C\sigma^{2}k\ \leq\ C\,\sigma^{2}k\ =\ C\min\{V^{2}H_{T},\ \sigma^{2}k\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4.4)</span></td></tr></tbody>
</table>
<p id="S4.SS1.p8.2" class="ltx_p">the second inequality because the surrogate crossing clause fired at $k=k_{\mathrm{alg}}\leq K\text{,}$ so that $V^{2}\delta_{k}\leq V^{2}\overline{\delta}_{k}\leq 2A_{0}\sigma^{2}k\text{,}$ and the equality by the branch condition. The three elementary branches obey the same bound by the diameter and first-budget facts of <a href="#S3.SS3" title="3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> (<a href="#S5a" title="S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.5</span></a>). Since $k_{\mathrm{alg}}\leq k_{0}$ by <a href="#S2.Thmlemma3" title="Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(<a href="#S2.I3.i3" title="Item 3 ‣ Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), $\min\{V^{2}H_{T},\sigma^{2}k_{\mathrm{alg}}\}\leq\min\{V^{2}H_{T},\sigma^{2}k_{0}\}\text{,}$ which <a href="#Thmtheorem1" title="Theorem 1 (Rate formula). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a> bounds by $C\,R^{*}_{T}(V,\sigma)\text{.}$</p>
</div>
</section>
<section id="S4.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="exact-evaluation"><span class="ltx_tag ltx_tag_subsection">4.2 </span>Exact Evaluation</h3>

<div id="S4.SS2.p1" class="ltx_para">
<p id="S4.SS2.p1.1" class="ltx_p">It remains to evaluate <a href="#S4.E2" title="In 4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>, a ratio of sums over a class of exponential size. Computing $k_{\mathrm{alg}}$ and the nets behind $A_{k}$ costs $O(n\log(n+1))$ operations (<a href="#S2.Thmlemma3" title="Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>), and the elementary branches are linear; the content is the interior branch.</p>
</div>
<div id="S4.SS2.p2" class="ltx_para">
<p id="S4.SS2.p2.1" class="ltx_p">The confined states are the mechanism. Every coordinate of an integer state lies in $\{0,\dots,3k\}\text{,}$ so subtree weights factorize over one integer state per vertex. Write $\varphi_{v}(x):=e^{-(Y_{v}-(V/k)x)^{2}/(4\sigma^{2})}$ for the local weight, so that the summand of <a href="#S4.E2" title="In 4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> at $x$ is $e^{-2\Gamma(x)}\prod_{v}\varphi_{v}(x_{v})\text{,}$ and define for each vertex the <em id="S4.SS2.p2.1.1" class="ltx_emph ltx_font_italic">message</em></p>
<table id="S4.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$P_{v}(\zeta)\ :=\ \sum_{x=0}^{3k}P_{v}[x]\,\zeta^{x},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4.5)</span></td></tr></tbody>
</table>
<p id="S4.SS2.p2.2" class="ltx_p">a polynomial of degree at most $3k$ in an indeterminate $\zeta\text{,}$ whose coefficient $P_{v}[x]$ is the total weight, local weights times prior kernel, of the admissible assignments on the subtree $T_{v}$ with state $x$ at $v\text{.}$ The message at $v$ arises from the product $\prod_{c\in\operatorname{ch}(v)}P_{c}(\zeta)$ of its children’s messages by pairwise polynomial multiplications and an $O(k)$ local pass, and correctness is an induction over subtrees; since every integer state has root coordinate $k\text{,}$ the denominator of <a href="#S4.E2" title="In 4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> is the single coefficient $P_{o}[k]\text{.}$</p>
</div>
<div id="S4.SS2.p3" class="ltx_para">
<p id="S4.SS2.p3.1" class="ltx_p">A child sum can exceed $3k$ where a state cannot. At an inactive vertex conservation kills such terms; at an active vertex the prior kernel is geometric in the leak, so they enter through one scalar, the child product evaluated at $e^{-2}\text{;}$ evaluations multiply where messages multiply, so the scalar travels with each message, and no coefficient beyond degree $3k$ outlives a merge (<a href="#S5a" title="S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.5</span></a>).</p>
</div>
<div id="S4.SS2.p4" class="ltx_para">
<p id="S4.SS2.p4.1" class="ltx_p">The tree off the active support carries no state: a subtree disjoint from $A_{k}$ contributes a constant factor and is pruned, and a maximal chain of inactive vertices, each left with one child whose state it copies, compresses to a single edge whose diagonal kernel is generated in $O(k)$ from the chain’s length and observation sum.</p>
</div>
<div id="S4.SS2.p5" class="ltx_para">
<p id="S4.SS2.p5.1" class="ltx_p">The numerator of <a href="#S4.E2" title="In 4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> is recovered by differentiation. Treat the $3k+1$ local weights at each vertex as formal inputs of the arithmetic circuit that computes $P_{o}[k]\text{;}$ every admissible assignment carries the factor $\varphi_{v}(x_{v})$ exactly once, so</p>
<table id="S4.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{\mu}_{k}(v)\ =\ \frac{V}{k}\,\sum_{x=0}^{3k}x\cdot\frac{\varphi_{v}(x)}{P_{o}[k]}\,\frac{\partial P_{o}[k]}{\partial\varphi_{v}(x)}\ ,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4.6)</span></td></tr></tbody>
</table>
<p id="S4.SS2.p5.2" class="ltx_p">the ratio under the sum being the posterior probability of $\{x_{v}=x\}\text{.}$ One reverse-mode sweep of the circuit computes all these derivatives at once, at the same asymptotic cost as the forward pass (<a href="#S5a" title="S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.5</span></a>).</p>
</div>
<div id="S4.SS2.p6" class="ltx_para">
<p id="S4.SS2.p6.1" class="ltx_p">Each vertex contributes $O(k)$ local work, each of the fewer than $n$ merges costs one multiplication of degree-$3k$ polynomials, $O(k\log(k+1))$ operations in the model of <a href="#S2.SS1" title="2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, and the reverse sweep matches the forward cost, so with the preprocessing the total is $O(n\log(n+1)+nk\log(k+1))\leq O(n^{2}\log(n+1))$ operations, the count of <a href="#Thmtheorem2" title="Theorem 2 (Efficient estimation). ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a>. On structured trees the account improves: sibling messages that agree up to a dilation of the variable multiply in batch through power sums, and on stars the entire evaluation takes $O(n\log^{2}n)$ operations. Every tie break is fixed, so the estimator is a deterministic function of $(T,V,\sigma,Y)\text{;}$ together with the risk bound of <a href="#S4.SS1" title="4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>, this proves <a href="#Thmtheorem2" title="Theorem 2 (Efficient estimation). ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a>. The evaluation identities, the operation count, and the instance-sensitive refinements are proved in <a href="#S5a" title="S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.5</span></a>.</p>
</div>
<div id="S4.Thmremark1" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmremark1.2" class="ltx_text ltx_font_bold">Remark 4.1</span></span><span id="S4.Thmremark1.3" class="ltx_text ltx_font_bold"> (Computational model).</span></h6>
<div id="S4.Thmremark1.p1" class="ltx_para">
<p id="S4.Thmremark1.p1.1" class="ltx_p"><span id="S4.Thmremark1.p1.1.1" class="ltx_text ltx_font_italic">“Exact” refers to the estimator itself, not only to its risk order: in the arithmetic model fixed in <a href="#S2.SS1" title="2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, the messages, the overflow scalars, the compressed kernels, and the reverse sweep are algebraic identities, and the returned vector is <a href="#S4.E2" title="In 4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> with $k=k_{\mathrm{alg}}\text{,}$ evaluated without error.</span></p>
</div>
</div>
</section>
<section id="S4.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="adaptation"><span class="ltx_tag ltx_tag_subsection">4.3 </span>Adaptation</h3>

<div id="S4.SS3.p1" class="ltx_para">
<p id="S4.SS3.p1.1" class="ltx_p">The budget is not external to the model: on the cone <a href="#S1.E1" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> it is the root value of the signal, observed directly as $Y_{o}=V+\sigma Z_{o}\text{,}$ so adaptation to it is cheap but not free.</p>
</div>
<div id="Thmtheorem3" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem3.2" class="ltx_text ltx_font_bold">Theorem 3</span></span><span id="Thmtheorem3.3" class="ltx_text ltx_font_bold"> (Budget adaptation).</span></h6>
<div id="Thmtheorem3.p1" class="ltx_para">
<p id="Thmtheorem3.p1.1" class="ltx_p"><span id="Thmtheorem3.p1.1.1" class="ltx_text ltx_font_italic">There are universal constants $c,C&gt;0$ and a deterministic polynomial-time estimator $\widehat{\mu}=\widehat{\mu}(T,\sigma,Y)\text{,}$ not depending on $V\text{,}$ such that for every finite rooted tree $T\text{,}$ all $V,\sigma&gt;0\text{,}$ and every $\mu\in\mathcal{F}_{V}(T)\text{,}$</span></p>
<table id="S4.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}_{\mu}\|\widehat{\mu}-\mu\|_{2}^{2}\ \leq\ C\bigl(R^{*}_{T}(V,\sigma)+\sigma^{2}\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="Thmtheorem3.p1.2" class="ltx_p"><span id="Thmtheorem3.p1.2.1" class="ltx_text ltx_font_italic">Conversely, every estimator $\widehat{\mu}(T,\sigma,Y)$ satisfies, for every finite rooted tree $T$ and all $V,\sigma&gt;0\text{,}$</span></p>
<table id="S4.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\max_{V^{\prime}\in\{V,\,V+\sigma\}}\ \sup_{\mu\in\mathcal{F}_{V^{\prime}}(T)}\mathbb{E}_{\mu}\|\widehat{\mu}-\mu\|_{2}^{2}\ \geq\ c\,\sigma^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4.SS3.p2" class="ltx_para">
<p id="S4.SS3.p2.1" class="ltx_p"><em class="ltx_title_proof">Proof of <a class="ltx_ref" href="#Thmtheorem3">Theorem 3</a>, necessity.</em></p>
</div>
<div id="S4.SS3.p3" class="ltx_para">
<p id="S4.SS3.p3.1" class="ltx_p">The points $Vp_{o}$ and $(V+\sigma)p_{o}$ lie in the slices at budgets $V$ and $V+\sigma$ and are at distance $\sigma\text{.}$ For any estimator $\widehat{\mu}(T,\sigma,Y)\text{,}$ decode the nearer of the two points: a decoding error forces squared loss at least $\sigma^{2}/4\text{,}$ and deciding between two Gaussian means at distance $\sigma$ is a one-dimensional shift of size one, on which every test errs with probability at least a universal constant under the uniform two-point prior. The larger of the two risks is therefore at least $c\,\sigma^{2}\text{.}$
∎</p>
</div>
<div id="S4.SS3.p4" class="ltx_para">
<p id="S4.SS3.p4.1" class="ltx_p">The sufficiency halves of <a href="#Thmtheorem3" title="Theorem 3 (Budget adaptation). ‣ 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorems</span> <span class="ltx_text ltx_ref_tag">3</span></a> and <a href="#Thmtheorem4" title="Theorem 4 (Full adaptation). ‣ 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a> rest on candidate families free of the unknown parameters. The construction behind <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> consumes the budget in exactly one place, the quantization of leaks in units of $V/k\text{;}$ dropping the quantization leaves subspaces. For an integer $2\leq k\leq n/C_{\star}\text{,}$ call $S\subseteq A_{k}\setminus R_{0}$ <em id="S4.SS3.p4.1.1" class="ltx_emph ltx_font_italic">admissible</em> when $\sum_{v\in S}\widetilde{\omega}(v)\leq 4k\text{,}$ and define the <em id="S4.SS3.p4.1.2" class="ltx_emph ltx_font_italic">profile subspaces</em> $\mathcal{V}_{k,S}:=\operatorname{span}\{p_{v}:\ v\in R_{0}\cup S\}\text{,}$ of dimension $O(k)\text{.}$ Everything here depends on $(T,k)$ alone, and the admissible supports number at most $e^{C_{1}k}\text{,}$ by the counting argument of <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>. Every body point is close to one of these subspaces at the profile scale:</p>
<table id="S4.E7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\min_{S\ \mathrm{admissible}}\ \operatorname{dist}^{2}\bigl(\mu,\ \mathcal{V}_{k,S}\bigr)\ \leq\ C\,V^{2}\overline{\delta}_{k}(T)\qquad\text{for every }\mu\in\mathcal{F}_{V}(T),\ 2\leq k\leq n/C_{\star}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4.7)</span></td></tr></tbody>
</table>
<p id="S4.SS3.p4.2" class="ltx_p">The unrounded skeleton and the sampled exits of the proof of <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> realize the bound, their support carrying total charge at most $4k$ (<a href="#S6" title="S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.6</span></a>).</p>
</div>
<div id="S4.SS3.p5" class="ltx_para">
<p id="S4.SS3.p5.1" class="ltx_p">Selection is by penalized least squares with Kraft weights. <a href="#S6" title="S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.6</span></a> proves the following oracle, of Birgé–Massart type <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib6" title="" class="ltx_ref">Birgé and Massart, 2001</a>)</cite>, in the weighted and random-penalty form needed here: for Gaussian data on $\mathbb{R}^{N}$ with independent coordinates of variances at most $\sigma^{2}$ and mean $\theta\text{,}$ a countable collection $\mathcal{M}$ of affine models $m$ with weights $\Delta_{m}$ obeying $\sum_{m}e^{-\Delta_{m}}\leq 1\text{,}$ penalties $C_{2}\sigma^{2}(\dim m+\Delta_{m})$ for a sufficiently large universal $C_{2}\text{,}$ and a full model penalized at $C_{2}\sigma^{2}N\text{,}$ every minimizer $\widehat{\theta}$ of the criterion obeys</p>
<table id="S4.E8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl\|\widehat{\theta}-\theta\bigr\|_{2}^{2}\ \leq\ C\,\min\Bigl\{\ \inf_{m\in\mathcal{M}}\bigl(\operatorname{dist}^{2}(\theta,m)+\sigma^{2}(\dim m+\Delta_{m}+1)\bigr),\ \ \sigma^{2}N\Bigr\}\ +\ C\sigma^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4.8)</span></td></tr></tbody>
</table>
<p id="S4.SS3.p5.2" class="ltx_p">If the penalties are random, nonnegative, and bracketed on an event $E$ between fixed multiples of the displayed ones, the same right side bounds $\mathbb{E}\bigl[\|\widehat{\theta}-\theta\|_{2}^{2}\mathbf{1}_{E}\bigr]\text{;}$ this is how the estimated noise scale enters in <a href="#Thmtheorem4" title="Theorem 4 (Full adaptation). ‣ 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4</span></a>.</p>
</div>
<div id="S4.SS3.p6" class="ltx_para">
<p id="S4.SS3.p6.1" class="ltx_p">For $n$ below a universal threshold the estimator of <a href="#Thmtheorem3" title="Theorem 3 (Budget adaptation). ‣ 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3</span></a> returns $Y\text{,}$ at risk $O(\sigma^{2})\text{;}$ above it, the estimator is one such selection, conditional on the root observation, over three groups of candidates: the amplitude-free subspaces $\mathcal{V}_{k,S}$ at dyadic budgets $2\leq k\leq k^{\star}:=\lfloor\log n/(2C_{1})\rfloor\text{;}$ the integer-state points $\tfrac{V^{\prime}}{k}\,x\text{,}$ $x\in\mathcal{X}_{k}\text{,}$ at the $O(\log n)$ amplitudes $V^{\prime}$ of a root-anchored geometric grid and a low-amplitude dyadic grid, with $\operatorname{span}(p_{o})$ and the root points $V^{\prime}p_{o}$ adjoined; and the full model, each candidate weighted by its dimension and code length. The system depends on $Y$ through $Y_{o}$ alone, so conditionally on $Y_{o}$ it is deterministic while the noise in the remaining coordinates is unchanged, and unconditioning costs $\mathbb{E}(Y_{o}-V)^{2}=\sigma^{2}\text{;}$ the precise grids, weights, and thresholds are fixed in <a href="#S6" title="S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.6</span></a>.</p>
</div>
<div id="S4.SS3.p7" class="ltx_para">
<p id="S4.SS3.p7.1" class="ltx_p"><em class="ltx_title_proof">Proof sketch of <a class="ltx_ref" href="#Thmtheorem3">Theorem 3</a>, sufficiency.</em></p>
</div>
<div id="S4.SS3.p8" class="ltx_para">
<p id="S4.SS3.p8.1" class="ltx_p">By <a href="#Thmtheorem1" title="Theorem 1 (Rate formula). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a> and the sandwich of <a href="#S2.Thmlemma3" title="Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>(<a href="#S2.I3.i3" title="Item 3 ‣ Lemma 2.3 (Profile toolkit). ‣ 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), $\min\{V^{2}H_{T},\sigma^{2}k_{\mathrm{alg}}\}\asymp R^{*}_{T}(V,\sigma)\text{,}$ and there are three regimes, according to the candidate at which the oracle <a href="#S4.E8" title="In 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4.8</span></a> is evaluated. In the diameter regime $V^{2}H_{T}\leq\sigma^{2}k_{\mathrm{alg}}\text{,}$ the model $\operatorname{span}(p_{o})$ is within squared distance $V^{2}h_{T}$ of $\mu\text{,}$ at constant dimension and weight. In the entropy regime with small crossing, $k_{\mathrm{alg}}\leq k^{\star}/2\text{,}$ the smallest dyadic $k\geq\max\{k_{\mathrm{alg}},2\}$ stays below $k^{\star}\text{,}$ and <a href="#S4.E7" title="In 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4.7</span></a> with the surrogate clause fired at $k_{\mathrm{alg}}$ gives an amplitude-free admissible subspace within squared distance $C\sigma^{2}k_{\mathrm{alg}}$ of $\mu\text{,}$ at dimension plus weight $O(k_{\mathrm{alg}})\text{,}$ so no quantization is paid. In the entropy regime with large crossing, $k_{\mathrm{alg}}&gt;k^{\star}/2\text{,}$ the grids take over: for $V\geq\sigma/2\text{,}$ outside an event of loss contribution $O(\sigma^{2})\text{,}$ the anchored grid contains an amplitude $V^{\prime}\geq V$ with $\mathbb{E}(V^{\prime}/V)^{2}=O(1)$ and index price $O(\sigma^{2})\text{,}$ and, according to the regime that $V^{\prime}$ sees, the approximant of <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> at the dyadic budget nearest its crossing, the root candidate, or the full model is a candidate whose oracle value is $C(R^{*}_{T}(V,\sigma)+\sigma^{2})$ in expectation, by the scale bound $R^{*}_{T}(cV,\sigma)\leq Cc^{2}R^{*}_{T}(V,\sigma)$ for $c\geq 1\text{;}$ for $V&lt;\sigma/2$ the low-amplitude grid plays the same role, its index price absorbed because $k_{\mathrm{alg}}&gt;k^{\star}/2$ places the rate above $c\,\sigma^{2}\log n$ (<a href="#S6" title="S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.6</span></a>). The additive $\sigma^{2}$ collects the root replacement, the anchored-grid prices, and the constant floor in <a href="#S4.E8" title="In 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4.8</span></a>; the two families are complementary, amplitude quantization being expensive only at small crossing, where the subspaces are few enough to enumerate. The selection runs in deterministic polynomial time, each grid candidate’s inner minimization over $\mathcal{X}_{k}$ being a min-plus analogue of <a href="#S4.SS2" title="4.2 Exact Evaluation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>; the operation counts, the grid moment bounds, and the conditioning argument are completed in <a href="#S6" title="S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.6</span></a>.
∎</p>
</div>
<div id="S4.SS3.p9" class="ltx_para">
<p id="S4.SS3.p9.1" class="ltx_p">It remains to remove the noise level, which enters the selection only through the penalties; these tolerate a constant-factor error, so a robust estimate suffices. The regime in which the estimate succeeds is described by a width functional of the tree. At each internal vertex of $T$ fix a child $c$ maximizing the number of vertices $u$ with $c\preceq u\text{,}$ breaking ties by a fixed rule; call the edge to that child <em id="S4.SS3.p9.1.1" class="ltx_emph ltx_font_italic">heavy</em>, every other child edge <em id="S4.SS3.p9.1.2" class="ltx_emph ltx_font_italic">light</em>, and a vertex <em id="S4.SS3.p9.1.3" class="ltx_emph ltx_font_italic">branching</em> when it has at least two children. Set $w_{T}:=w_{\mathrm{lt}}(T)+w_{\mathrm{br}}(T)\text{,}$ where $w_{\mathrm{lt}}(T)$ is one plus the maximum number of light edges on a root-to-leaf path, and $w_{\mathrm{br}}(T)$ is the maximum number of branching vertices on such a path.</p>
</div>
<div id="Thmtheorem4" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem4.2" class="ltx_text ltx_font_bold">Theorem 4</span></span><span id="Thmtheorem4.3" class="ltx_text ltx_font_bold"> (Full adaptation).</span></h6>
<div id="Thmtheorem4.p1" class="ltx_para">
<p id="Thmtheorem4.p1.1" class="ltx_p"><span id="Thmtheorem4.p1.1.1" class="ltx_text ltx_font_italic">There are universal constants $c,C&gt;0$ and a deterministic polynomial-time estimator $\widehat{\mu}=\widehat{\mu}(T,Y)\text{,}$ depending on neither $V$ nor $\sigma\text{,}$ such that for every finite rooted tree $T$ and all $V,\sigma&gt;0\text{,}$</span></p>
<table id="S4.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sup_{\mu\in\mathcal{F}_{V}(T)}\mathbb{E}_{\mu}\|\widehat{\mu}-\mu\|_{2}^{2}\ \leq\ C\bigl(R^{*}_{T}(V,\sigma)+\sigma^{2}\bigr)\qquad\text{whenever}\quad Vw_{T}\leq c\sigma n.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4.SS3.p10" class="ltx_para">
<p id="S4.SS3.p10.1" class="ltx_p">For $n$ below a universal threshold the estimator behind <a href="#Thmtheorem4" title="Theorem 4 (Full adaptation). ‣ 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4</span></a> returns $Y\text{,}$ at risk $O(\sigma^{2})\text{;}$ above it, the estimator rounds a median. The tree supplies at least $(n-1)/2$ difference statistics: heavy-edge and sibling differences, each Gaussian of variance $2\sigma^{2}$ around a signal difference. Monotonicity caps the contamination collectively: heavy differences telescope along vertex-disjoint heavy paths to their tops, sibling excesses charge their branching vertices, and a root path meets at most $w_{T}$ of these sites; for every $\varepsilon&gt;0\text{,}$ at most $Vw_{T}/(\varepsilon\sigma)$ statistics therefore have mean magnitude at least $\varepsilon\sigma\text{.}$ Under $Vw_{T}\leq c\sigma n\text{,}$ the normalized median of the absolute values of an independent subfamily then lands in $[\sigma/2,\,2\sigma]$ except with probability $2e^{-cn}\text{;}$ rounded upward to a power of two, the estimate takes at most four values on that event, the penalties of <a href="#Thmtheorem3" title="Theorem 3 (Budget adaptation). ‣ 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3</span></a> stay bracketed at the estimated scale, a constant weight shift pays for the union over the four values, and the off-event loss contributes $O(\sigma^{2})\text{.}$ The statistics, the contamination count, the concentration of the median, and the moment bookkeeping are carried out in <a href="#S6" title="S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.6</span></a>.</p>
</div>
<div id="S4.SS3.p11" class="ltx_para">
<p id="S4.SS3.p11.1" class="ltx_p">Uniform recovery of the noise level has a ceiling: once monotone flows with root value of order $\sigma n\sqrt{\log n}$ are admitted, every estimator of $\sigma$ fails, with constant probability, to land strictly within a factor $\sqrt{2}$ of the truth (<a href="#S6" title="S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.6</span></a>). On families of bounded width, stars and brooms among them, the scale-based route of <a href="#Thmtheorem4" title="Theorem 4 (Full adaptation). ‣ 4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4</span></a> thus operates within a $\sqrt{\log n}$ factor of its ceiling.</p>
</div>
</section>
</section>
<section id="S5" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-suboptimality-of-least-squares"><span class="ltx_tag ltx_tag_section">5 </span>The Suboptimality of Least Squares</h2>

<div id="S5.p1" class="ltx_para">
<p id="S5.p1.1" class="ltx_p">The last theorem prices the default estimator. The body is compact and convex, so the data have a unique Euclidean projection onto it, the <em id="S5.p1.1.1" class="ltx_emph ltx_font_italic">constrained least squares estimator</em></p>
<table id="S5.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{\mu}_{\mathrm{LSE}}\ :=\ \Pi_{\mathcal{F}_{V}(T)}(Y)\ =\ \operatorname*{arg\,min}_{\theta\in\mathcal{F}_{V}(T)}\ \bigl\|Y-\theta\bigr\|_{2}^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.p1.2" class="ltx_p">the solution of a tuning-free convex program; write</p>
<table id="S5.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{\mathrm{worst}}_{\mathrm{LSE}}(T,V,\sigma)\ :=\ \sup_{\mu\in\mathcal{F}_{V}(T)}\mathbb{E}_{\mu}\bigl\|\widehat{\mu}_{\mathrm{LSE}}-\mu\bigr\|_{2}^{2}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.p1.3" class="ltx_p">for its worst-case risk.</p>
</div>
<div id="Thmtheorem5" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem5.2" class="ltx_text ltx_font_bold">Theorem 5</span></span><span id="Thmtheorem5.3" class="ltx_text ltx_font_bold"> (Least squares).</span></h6>
<div id="Thmtheorem5.p1" class="ltx_para">
<p id="Thmtheorem5.p1.1" class="ltx_p"><span id="Thmtheorem5.p1.1.1" class="ltx_text ltx_font_italic">There is a universal constant $C$ such that for every finite rooted tree with $n\geq 2$ and all $V,\sigma&gt;0\text{,}$</span></p>
<table id="S5.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{\mathrm{worst}}_{\mathrm{LSE}}(T,V,\sigma)\ \leq\ C\,\bigl(1+\log(en)\bigr)^{2/5}\,R^{*}_{T}(V,\sigma).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="Thmtheorem5.p1.2" class="ltx_p"><span id="Thmtheorem5.p1.2.1" class="ltx_text ltx_font_italic">Conversely, there are universal constants $c&gt;0$ and $n_{0}$ such that the following holds for every integer $n\geq n_{0}\text{.}$ Let $L$ be the largest integer with $e^{20L^{5/2}}\leq\sqrt{n}\text{,}$ and let $T_{L}$ be the broom on $n$ vertices whose handle $o=v_{0},v_{1},\dots,v_{L}$ is a path of $L$ edges and whose endpoint $v_{L}$ has $m:=n-L-1$ leaf children. Then, at budget $V=L^{1/4}$ and noise level $\sigma=1\text{,}$</span></p>
<table id="S5.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{\mathrm{worst}}_{\mathrm{LSE}}\bigl(T_{L},L^{1/4},1\bigr)\ \geq\ c\,(\log n)^{2/5}\,R^{*}_{T_{L}}\bigl(L^{1/4},1\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S5.p2" class="ltx_para">
<p id="S5.p2.1" class="ltx_p">We prove the broom lower bound first: the broom isolates the mechanism, extreme-value forcing through a terminal star, and every numerical threshold in the forcing step is explicit (<a href="#S4a" title="S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.4</span></a>). The universal upper bound shows the resulting separation extremal over all trees and parameters; its proof, sketched at the end of the section, runs the coded cover of <a href="#S3.SS1" title="3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> through a localized-width analysis.</p>
</div>
<div id="S5.p3" class="ltx_para">
<p id="S5.p3.1" class="ltx_p">The broom couples the two classical geometries in series, a path feeding a star. For integers $L\geq 1$ and $m\geq 1\text{,}$ the broom $T_{L}$ consists of a <em id="S5.p3.1.1" class="ltx_emph ltx_font_italic">handle</em>, the path $o=v_{0},v_{1},\dots,v_{L}$ of $L$ edges, and of $m$ <em id="S5.p3.1.2" class="ltx_emph ltx_font_italic">terminal leaves</em> $w_{1},\dots,w_{m}\text{,}$ the children of $v_{L}\text{,}$ so that $n=L+1+m$ and $h_{T_{L}}=H_{T_{L}}=L+1\text{;}$ the budget and the noise level are fixed at $V:=L^{1/4}$ and $\sigma:=1\text{.}$</p>
</div>
<div id="S5.p4" class="ltx_para">
<p id="S5.p4.1" class="ltx_p"><em class="ltx_title_proof">Proof of <a class="ltx_ref" href="#Thmtheorem5">Theorem 5</a>, lower bound.</em></p>
</div>
<div id="S5.p5" class="ltx_para">
<p id="S5.p5.1" class="ltx_p">Fix $n\geq n_{0}\text{,}$ with $n_{0}$ a universal constant large enough for the estimates below. The maximality of $L$ gives $e^{20L^{5/2}}\leq\sqrt{n}&lt;e^{20(L+1)^{5/2}}\text{;}$ for $n\geq n_{0}$ it forces $L\geq 4$ and $L+1\leq\sqrt{n}\text{,}$ whence $m=n-L-1\geq n-\sqrt{n}\geq\sqrt{n}\geq e^{20L^{5/2}}\text{.}$ The true signal is $\mu=Vp_{o}\text{:}$ all mass rests at the root, and every nonroot coordinate vanishes. We show that one extreme leaf noise forces the projection to carry more than half the budget through the entire handle, at squared loss exceeding $L^{3/2}/4\text{,}$ on an event of probability at least $3/8\text{;}$ and that the minimax risk of the broom is of order $\sqrt{L}\text{.}$</p>
</div>
<div id="S5.p6" class="ltx_para">
<p id="S5.p6.1" class="ltx_p"><em id="S5.p6.1.1" class="ltx_emph ltx_font_italic">Coordinates.</em> Write $h_{j}$ for the coordinate of a body point at $v_{j}$ and $\ell_{i}$ for its coordinate at $w_{i}\text{.}$ By <a href="#S2.Thmlemma1" title="Lemma 2.1 (Normal forms). ‣ 2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, nonnegativity of the leaks identifies the body, in these coordinates, with the chain</p>
<table id="S5.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V\ \geq\ h_{1}\ \geq\ h_{2}\ \geq\ \cdots\ \geq\ h_{L}\ \geq\ \sum_{i=1}^{m}\ell_{i},\qquad\ell_{i}\ \geq\ 0\quad(1\leq i\leq m).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.1)</span></td></tr></tbody>
</table>
<p id="S5.p6.2" class="ltx_p">The root coordinate equals $V$ on the whole body, and at the true signal the nonroot data are pure noise: $Y_{v_{j}}=Z_{v_{j}}$ and $Y_{w_{i}}=Z_{w_{i}}\text{.}$ Expanding $\|Y-\theta\|_{2}^{2}$ and discarding the terms that do not depend on $\theta$ shows that the nonroot coordinates of the projection maximize over <a href="#S5.E1" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> the objective</p>
<table id="S5.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Psi(h,\ell)\ :=\ 2\sum_{j=1}^{L}Z_{v_{j}}h_{j}-\sum_{j=1}^{L}h_{j}^{2}\ +\ 2\sum_{i=1}^{m}Z_{w_{i}}\ell_{i}-\sum_{i=1}^{m}\ell_{i}^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.2)</span></td></tr></tbody>
</table>
</div>
<div id="S5.p7" class="ltx_para">
<p id="S5.p7.1" class="ltx_p"><em id="S5.p7.1.1" class="ltx_emph ltx_font_italic">The forcing inequality.</em> Aggregate the noise into three statistics, local to this proof:</p>
<table id="S5.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$W:=\sum_{j=1}^{L}Z_{v_{j}},\qquad Q:=\sum_{j=1}^{L}\bigl[Z_{v_{j}}\bigr]_{+}^{2},\qquad M:=\max_{1\leq i\leq m}Z_{w_{i}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.p7.2" class="ltx_p">Routing the full budget to a leaf attaining $M\text{,}$ that is, taking $h_{j}=V$ for every $j\text{,}$ $\ell_{i^{\star}}=V$ at one index $i^{\star}$ with $Z_{w_{i^{\star}}}=M\text{,}$ and $\ell_{i}=0$ elsewhere, is feasible in <a href="#S5.E1" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>. Its objective value is $2VW+2VM-(L+1)V^{2}\text{.}$ On the other side, suppose $M&gt;0\text{;}$ then every feasible point with $h_{L}\leq V/2$ obeys</p>
<table id="S5.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Psi(h,\ell)\ \leq\ Q+MV,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.3)</span></td></tr></tbody>
</table>
<p id="S5.p7.3" class="ltx_p">since $2Z_{v_{j}}h_{j}-h_{j}^{2}\leq[Z_{v_{j}}]_{+}^{2}$ for every $h_{j}\geq 0\text{,}$ while discarding $-\sum_{i}\ell_{i}^{2}$ and replacing each $Z_{w_{i}}$ by $M$ bounds the leaf part by $2M\sum_{i}\ell_{i}\leq 2Mh_{L}\leq MV\text{,}$ the last two steps by <a href="#S5.E1" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> and by the hypothesis $h_{L}\leq V/2$ (<a href="#S4a" title="S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.4</span></a>). The routed candidate beats the cap <a href="#S5.E3" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.3</span></a> exactly when</p>
<table id="S5.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$M\ &gt;\ (L+1)V-2W+\frac{Q}{V}\ .$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.4)</span></td></tr></tbody>
</table>
<p id="S5.p7.4" class="ltx_p">When $M&gt;0$ and <a href="#S5.E4" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.4</span></a> hold, no maximizer of $\Psi$ can have $h_{L}\leq V/2\text{,}$ so the coordinates $(\widehat{h},\widehat{\ell})$ of $\widehat{\mu}_{\mathrm{LSE}}$ satisfy $\widehat{h}_{L}&gt;V/2\text{;}$ the chain <a href="#S5.E1" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> propagates the bound up the handle, and since the true nonroot signal is zero,</p>
<table id="S5.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\bigl\|\widehat{\mu}_{\mathrm{LSE}}-Vp_{o}\bigr\|_{2}^{2}\ \geq\ \sum_{j=1}^{L}\widehat{h}_{j}^{\,2}\ &gt;\ L\,\frac{V^{2}}{4}\ =\ \frac{L^{3/2}}{4}\ .$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.5)</span></td></tr></tbody>
</table>
</div>
<div id="S5.p8" class="ltx_para">
<p id="S5.p8.1" class="ltx_p"><em id="S5.p8.1.1" class="ltx_emph ltx_font_italic">The forcing event.</em> Let</p>
<table id="S5.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E\ :=\ \{W\geq-2\sqrt{L}\}\cap\{Q\leq 2L\}\cap\{M\geq 4L^{5/4}\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.p8.2" class="ltx_p">On $E\text{,}$ with $V=L^{1/4}\text{,}$ the right side of <a href="#S5.E4" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.4</span></a> is less than $4L^{5/4}\leq M$ for $L\geq 4\text{,}$ so the forcing inequality holds; Markov’s inequality on the handle statistics and a Gaussian tail estimate on the leaf maximum, using $m\geq e^{20L^{5/2}}\text{,}$ give $\mathbb{P}(E)\geq\tfrac{3}{8}$ (<a href="#S4a" title="S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.4</span></a>). Combining with <a href="#S5.E5" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.5</span></a>,</p>
<table id="S5.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}_{Vp_{o}}\bigl\|\widehat{\mu}_{\mathrm{LSE}}-Vp_{o}\bigr\|_{2}^{2}\ \geq\ \frac{L^{3/2}}{4}\,\mathbb{P}(E)\ \geq\ \frac{3}{32}\,L^{3/2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.6)</span></td></tr></tbody>
</table>
</div>
<div id="S5.p9" class="ltx_para">
<p id="S5.p9.1" class="ltx_p"><em id="S5.p9.1.1" class="ltx_emph ltx_font_italic">The minimax rate.</em> The ancestor-covering numbers of the broom are explicit: $N^{\uparrow}_{T}(0)=n\text{,}$ and for integers $1\leq j\leq L\text{,}$</p>
<table id="S5.E7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N^{\uparrow}_{T}(j)\ =\ \Bigl\lceil\frac{L+2}{j+1}\Bigr\rceil.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.7)</span></td></tr></tbody>
</table>
<p id="S5.p9.2" class="ltx_p">Both directions follow by counting along the root-to-leaf path $v_{0},\dots,v_{L},w_{1}\text{;}$ the single center $v_{L+1-j}$ covers every leaf at distance exactly $j$ (<a href="#S4a" title="S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.4</span></a>). Thus every radius $r\geq 1$ sees a covering count independent of $m\text{:}$ the terminal star enters the profile <a href="#S1.E4" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.4</span></a> only through radii $r&lt;1\text{,}$ where the truncation caps its term at $k\text{.}$ What survives is path geometry: <a href="#S4a" title="S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.4</span></a> turns <a href="#S5.E7" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.7</span></a> into the profile bounds</p>
<table id="S5.E8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\delta_{k}(T_{L})\ \leq\ \max\Bigl\{1,\ \frac{2(L+2)}{ek^{2}}\Bigr\}\quad\text{for }k\geq 1,\qquad\quad\delta_{k}(T_{L})\ \geq\ \frac{L+2}{2ek^{2}}\quad\text{for }k\leq\frac{L+2}{2e}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.8)</span></td></tr></tbody>
</table>
<p id="S5.p9.3" class="ltx_p">The crossing then solves at $k_{0}\asymp(V^{2}(L+2)/\sigma^{2})^{1/3}\asymp\sqrt{L}\text{,}$ with the dimension clause of <a href="#S1.E5" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.5</span></a> silent and the diameter branch of <a href="#Thmtheorem1" title="Theorem 1 (Rate formula). ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a> inactive, so</p>
<table id="S5.E9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T_{L}}\bigl(L^{1/4},1\bigr)\ \asymp\ k_{0}\ \asymp\ \sqrt{L}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.9)</span></td></tr></tbody>
</table>
<p id="S5.p9.4" class="ltx_p">(<a href="#S4a" title="S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.4</span></a>).</p>
</div>
<div id="S5.p10" class="ltx_para">
<p id="S5.p10.1" class="ltx_p"><em id="S5.p10.1.1" class="ltx_emph ltx_font_italic">Conclusion.</em> The maximality of $L$ gives $\sqrt{n}&lt;e^{20(L+1)^{5/2}}\text{,}$ so $\log n&lt;40(L+1)^{5/2}$ and $L\geq c(\log n)^{2/5}\text{.}$ Dividing <a href="#S5.E6" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.6</span></a> by <a href="#S5.E9" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.9</span></a> gives a ratio at least $cL\geq c^{\prime}(\log n)^{2/5}$ at this signal, and the worst-case risk dominates this single-signal risk.
∎</p>
</div>
<div id="S5.p11" class="ltx_para">
<p id="S5.p11.1" class="ltx_p">The upper half is a statement about every tree and every parameter pair at once; its proof has three blocks, completed in <a href="#S7" title="S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.7</span></a>.</p>
</div>
<div id="S5.p12" class="ltx_para">
<p id="S5.p12.1" class="ltx_p"><em class="ltx_title_proof">Proof sketch of <a class="ltx_ref" href="#Thmtheorem5">Theorem 5</a>, upper bound.</em></p>
</div>
<div id="S5.p13" class="ltx_para">
<p id="S5.p13.1" class="ltx_p"><em id="S5.p13.1.1" class="ltx_emph ltx_font_italic">A localized projection principle.</em> For $\mu\in\mathcal{F}_{V}(T)$ and $t&gt;0\text{,}$ let</p>
<table id="S5.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$w_{\mu}(t)\ :=\ \mathbb{E}\,\sup\bigl\{\langle Z,\theta-\mu\rangle:\ \theta\in\mathcal{F}_{V}(T),\ \|\theta-\mu\|_{2}\leq t\bigr\}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.p13.2" class="ltx_p">be the localized Gaussian width of the body at the truth. If $t\geq\sigma$ and $\sigma\,w_{\mu}(s)\leq s^{2}/4$ for every $s\geq t\text{,}$ then $\mathbb{E}_{\mu}\|\widehat{\mu}_{\mathrm{LSE}}-\mu\|_{2}^{2}\leq 33\,t^{2}\text{.}$ On the event $\|\widehat{\mu}_{\mathrm{LSE}}-\mu\|_{2}\geq s\text{,}$ projection optimality forces the supremum defining $w_{\mu}(s)$ above twice its mean; the supremum is $s$-Lipschitz in $Z\text{,}$ so Gaussian concentration bounds its probability, and integrating the tail from $t$ gives the claim (<a href="#S7" title="S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.7</span></a>). Localizing least squares at a fixed point of the width is Chatterjee’s argument <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib14" title="" class="ltx_ref">Chatterjee, 2014</a>)</cite>.</p>
</div>
<div id="S5.p14" class="ltx_para">
<p id="S5.p14.1" class="ltx_p"><em id="S5.p14.1.1" class="ltx_emph ltx_font_italic">The width of the body through the coded cover.</em> Fix an integer $2\leq k\leq n/C_{\star}\text{,}$ write $\overline{\delta}:=\overline{\delta}_{k}(T)$ for the surrogate profile <a href="#S2.E1" title="In 2.2 The Ancestor Profile ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, and let $\ell_{n}:=1+\log(en)\text{.}$ <a href="#S7" title="S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.7</span></a> proves the truth-localized width bound</p>
<table id="S5.E10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$w_{\mu}(t)\ \leq\ C\,\bigl(t+V\sqrt{\overline{\delta}}\,\bigr)\sqrt{k}\ +\ C\,V\Bigl[\sqrt{k\overline{\delta}}\,\log(2+\ell_{n})+\sqrt{\overline{\delta}\,\ell_{n}}\,\Bigr]\qquad\text{for all }t&gt;0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.10)</span></td></tr></tbody>
</table>
<p id="S5.p14.2" class="ltx_p">The first term is the width of the coded cover $\mathcal{D}_{k}$ seen from the truth: recentering at a deterministic center $\nu_{\mu}\in\mathcal{D}_{k}$ (<a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>) confines every center met by the local ball to distance $t+2CV\sqrt{\overline{\delta}}\text{,}$ and the class has logarithmic cardinality $O(k)\text{,}$ so the maximum of the recentered pairings obeys a $\sqrt{k}$ bound. The second term bounds the residual $\theta-\nu_{\theta}\text{,}$ uniformly over the body, through the three components of the construction behind <a href="#S3.Thmlemma1" title="Proposition 3.1 (Coded cover). ‣ 3.1 The Coded Cover ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>: the collapse and rounding residuals, bounded by a capped order-statistics sum and a union of norm concentrations over $e^{Ck}$ subspaces at $CV\sqrt{k\overline{\delta}}$ (<a href="#S7" title="S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.7</span></a>); and the exit quantization. Conditionally on $(\theta,Z)\text{,}$ the pairing of $Z$ with the quantization error is centered, so on the sampling event of that construction, of probability at least $\tfrac{1}{4}\text{,}$ its conditional expectation is at most four conditional standard deviations. Some realization in the event meets this bound, and the randomized rounding becomes, for each noise outcome, a deterministic choice of a nearby center in $\mathcal{D}_{k}\text{.}$</p>
</div>
<div id="S5.p15" class="ltx_para">
<p id="S5.p15.1" class="ltx_p"><em id="S5.p15.1.1" class="ltx_emph ltx_font_italic">Closure of the exponent.</em> Let $2\leq k_{0}\leq K\text{,}$ where $R^{*}_{T}\asymp\sigma^{2}k_{0}$ (<a href="#S3.SS3" title="3.3 The Crossing and the Benchmarks ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>). The crossing <a href="#S1.E5" title="In 1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1.5</span></a> and the sandwich $\overline{\delta}_{k_{0}}\leq 2\delta_{k_{0}}$ give $V\sqrt{\overline{\delta}_{k_{0}}}\leq C\sigma\sqrt{k_{0}}\text{,}$ hence also $V\sqrt{k_{0}\overline{\delta}_{k_{0}}}\leq C\sigma k_{0}\text{.}$ Inserting these into <a href="#S5.E10" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.10</span></a> at $k=k_{0}$ and feeding the result to the localization principle at $t^{2}\asymp\sigma^{2}[\,k_{0}\log(2+\ell_{n})+\sqrt{k_{0}\,\ell_{n}}\,]$ gives</p>
<table id="S5.E11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{R^{\mathrm{worst}}_{\mathrm{LSE}}(T,V,\sigma)}{R^{*}_{T}(V,\sigma)}\ \leq\ C\,\Bigl[\log(2+\ell_{n})+\sqrt{\ell_{n}/k_{0}}\,\Bigr].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.11)</span></td></tr></tbody>
</table>
<p id="S5.p15.2" class="ltx_p">This bound deteriorates as $k_{0}$ shrinks, but a small crossing index strengthens the projection: the profile remembers the height, $\delta_{k}\geq cH_{T}/k^{2}$ for $k\leq n/C_{\star}$ (<a href="#S7" title="S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.7</span></a>), so the crossing forces $V^{2}H_{T}\leq C\sigma^{2}k_{0}^{3}\text{,}$ while $R^{\mathrm{worst}}_{\mathrm{LSE}}\leq V^{2}H_{T}$ holds, the truth and its projection lying in the body. Hence</p>
<table id="S5.E12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{R^{\mathrm{worst}}_{\mathrm{LSE}}(T,V,\sigma)}{R^{*}_{T}(V,\sigma)}\ \leq\ C\,k_{0}^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5.12)</span></td></tr></tbody>
</table>
<p id="S5.p15.3" class="ltx_p">The two bounds meet at $k_{0}=\ell_{n}^{1/5}\text{:}$ for $k_{0}\leq\ell_{n}^{1/5}\text{,}$ <a href="#S5.E12" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.12</span></a> is at most $C\ell_{n}^{2/5}\text{;}$ for $k_{0}&gt;\ell_{n}^{1/5}\text{,}$ <a href="#S5.E11" title="In 5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5.11</span></a> is at most $C[\log(2+\ell_{n})+\ell_{n}^{2/5}]\leq C^{\prime}\ell_{n}^{2/5}\text{.}$ At the endpoints $k_{0}=K+1$ and $k_{0}=1$ the deterministic caps $R^{\mathrm{worst}}_{\mathrm{LSE}}\leq\min\{V^{2}H_{T},\ \sigma^{2}n\}$ close the argument against $R^{*}_{T}$ (<a href="#S7" title="S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.7</span></a>).
∎</p>
</div>
<div id="S5.p16" class="ltx_para">
<p id="S5.p16.1" class="ltx_p">The broom is where the two geometries of this paper part ways. Euclidean geometry sees $m$ orthogonal leaf directions, and the extreme noise among them pulls the projection through the handle; the ancestor geometry sees, at every radius $r\geq 1\text{,}$ one vertex that covers the entire star, and the truncation caps its cost at the information budget rather than per leaf. The truncated ancestor profile is therefore the right geometry for this body. On every finite tree it determines the minimax rate and yields an estimator evaluated exactly, one that survives the removal of the budget at an additive cost of order $\sigma^{2}\text{;}$ across all trees it prices the blindness of the default convex program at the power $2/5$ of the logarithm.</p>
</div>
<div class="ltx_pagination ltx_role_newpage"></div>
<div id="S5.p17" class="ltx_para">
<p id="S5.p17.1" class="ltx_p">The appendices below contain the complete proofs. References of the form Lemma 2.3, (1.4), or Section 2 point to the main body above; statements and equations proved here carry the prefix S, and the notation of the main body remains in force.</p>
</div>
</section>
<section id="S1a" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-profile-toolkit"><span class="ltx_tag ltx_tag_section">S.1 </span>The Profile Toolkit</h2>

<div id="S1a.p1" class="ltx_para">
<p id="S1a.p1.1" class="ltx_p">This section proves the statements deferred from Section 2, Lemmas 2.1 to 2.3, and verifies two comparisons stated in Section 1.1: the center convention behind (1.6), and the capped constraint of <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty (2018)</a></cite>. The two normal forms and the isometry come first; the computational claims of Lemma 2.3 then rest on an exact linear-time algorithm for minimum ancestor nets.</p>
</div>
<div id="S1a.p2" class="ltx_para">
<p id="S1a.p2.1" class="ltx_p"><em class="ltx_title_proof">Proof of Lemma&nbsp;2.1.</em></p>
</div>
<div id="S1a.p3" class="ltx_para">
<p id="S1a.p3.1" class="ltx_p"><em id="S1a.p3.1.1" class="ltx_emph ltx_font_italic">Item <span id="S1a.p3.1.1.1" class="ltx_text ltx_font_upright">(1)</span> is equivalent to item <span id="S1a.p3.1.1.2" class="ltx_text ltx_font_upright">(2)</span>.</em> Definition (1.2) reads $\mu=V\sum_{u}\lambda_{u}p_{u}$ with $\lambda$ a probability vector on $\mathsf{V}\text{,}$ and the substitution $s_{u}=V\lambda_{u}$ turns this into $\mu=\sum_{u}s_{u}p_{u}$ with $s_{u}\geq 0$ and $\sum_{u}s_{u}=V\text{.}$ For uniqueness, order $\mathsf{V}$ so that every vertex precedes its descendants, for instance by nondecreasing depth, and let $P$ be the matrix with columns $(p_{u})_{u\in\mathsf{V}}$ in that order. Its entry at row $v$ and column $u$ is $\mathbf{1}\{v\preceq u\}\text{,}$ which vanishes when $v$ follows $u\text{,}$ because a strict ancestor of $u$ precedes $u\text{;}$ and $p_{u}(u)=1$ on the diagonal. So $P$ is upper triangular with unit diagonal, hence $\det P=1$ and $P$ is invertible, and the coefficient vector is determined by $\mu\text{.}$</p>
</div>
<div id="S1a.p4" class="ltx_para">
<p id="S1a.p4.1" class="ltx_p"><em id="S1a.p4.1.1" class="ltx_emph ltx_font_italic">Item <span id="S1a.p4.1.1.1" class="ltx_text ltx_font_upright">(2)</span> implies item <span id="S1a.p4.1.1.2" class="ltx_text ltx_font_upright">(3)</span> and both displayed identities.</em> Evaluating $\mu=\sum_{u}s_{u}p_{u}$ at $v$ gives</p>
<table id="S1.E1a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mu(v)\ =\ \sum_{u\in\mathsf{V}}s_{u}\,\mathbf{1}\{v\preceq u\}\ =\ \sum_{u\succeq v}s_{u},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.1.1)</span></td></tr></tbody>
</table>
<p id="S1a.p4.2" class="ltx_p">the first identity; at $v=o$ it reads $\mu(o)=\sum_{u}s_{u}=V\text{,}$ every vertex being a descendant of the root. The strict descendants of $v$ are partitioned by the subtrees $T_{c}\text{,}$ $c\in\operatorname{ch}(v)\text{,}$ so subtracting <a href="#S1.E1a" title="In S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.1.1</span></a> at the children from <a href="#S1.E1a" title="In S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.1.1</span></a> at $v$ leaves the single term $u=v\text{:}$</p>
<table id="S1.Ex1a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mu(v)-\sum_{c\in\operatorname{ch}(v)}\mu(c)\ =\ \sum_{u\succeq v}s_{u}-\sum_{c\in\operatorname{ch}(v)}\sum_{u\succeq c}s_{u}\ =\ s_{v}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p4.3" class="ltx_p">This is the second identity; since $s\geq 0$ it gives $\mu(v)\geq\sum_{c\in\operatorname{ch}(v)}\mu(c)\text{,}$ which with $\mu(o)=V$ is item (3).</p>
</div>
<div id="S1a.p5" class="ltx_para">
<p id="S1a.p5.1" class="ltx_p"><em id="S1a.p5.1.1" class="ltx_emph ltx_font_italic">Item <span id="S1a.p5.1.1.1" class="ltx_text ltx_font_upright">(3)</span> implies item <span id="S1a.p5.1.1.2" class="ltx_text ltx_font_upright">(2)</span>.</em> Set $s_{v}:=\mu(v)-\sum_{c\in\operatorname{ch}(v)}\mu(c)\text{,}$ nonnegative by hypothesis. We prove <a href="#S1.E1a" title="In S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.1.1</span></a> by induction from the leaves upward. At a leaf the sum over children is empty, so $s_{v}=\mu(v)\text{,}$ which is the claim. At an internal vertex, the same partition of the strict descendants of $v$ and the inductive hypothesis at the children give</p>
<table id="S1.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{u\succeq v}s_{u}\ =\ s_{v}+\sum_{c\in\operatorname{ch}(v)}\sum_{u\succeq c}s_{u}\ =\ s_{v}+\sum_{c\in\operatorname{ch}(v)}\mu(c)\ =\ \mu(v).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p5.2" class="ltx_p">At $v=o$ this yields $\sum_{u}s_{u}=\mu(o)=V\text{,}$ and reading <a href="#S1.E1a" title="In S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.1.1</span></a> at every coordinate says exactly $\mu=\sum_{u}s_{u}p_{u}\text{.}$
∎</p>
</div>
<div id="S1a.p6" class="ltx_para">
<p id="S1a.p6.1" class="ltx_p"><em class="ltx_title_proof">Proof of Lemma&nbsp;2.2.</em></p>
</div>
<div id="S1a.p7" class="ltx_para">
<p id="S1a.p7.1" class="ltx_p"><em id="S1a.p7.1.1" class="ltx_emph ltx_font_italic">Part <span id="S1a.p7.1.1.1" class="ltx_text ltx_font_upright">(1)</span>.</em> A vertex is a common ancestor of $u$ and $w$ precisely when it is an ancestor of their deepest common ancestor $u\wedge w\text{,}$ and a vertex $x$ has exactly $\operatorname{depth}(x)+1$ ancestors, namely the vertices of the segment from $o$ to $x\text{.}$ Hence</p>
<table id="S1.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\langle p_{u},p_{w}\rangle\ =\ \#\{v:\ v\preceq u\ \text{and}\ v\preceq w\}\ =\ \operatorname{depth}(u\wedge w)+1,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p7.2" class="ltx_p">and in particular $\|p_{x}\|_{2}^{2}=\operatorname{depth}(x)+1\text{.}$ Expanding the square,</p>
<table id="S1.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|p_{u}-p_{w}\|_{2}^{2}\ =\ \operatorname{depth}(u)+\operatorname{depth}(w)-2\operatorname{depth}(u\wedge w)\ =\ d_{T}(u,w),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p7.3" class="ltx_p">the last equality because the $u$-to-$w$ path is the concatenation of the segments from $u$ up to $u\wedge w$ and from $u\wedge w$ down to $w\text{.}$ The diameter of a convex hull equals that of its generating set, so $\operatorname{diam}^{2}\mathcal{F}_{V}(T)=\max_{u,w}\|Vp_{u}-Vp_{w}\|_{2}^{2}=V^{2}H_{T}$ by (1.2).</p>
</div>
<div id="S1a.p8" class="ltx_para">
<p id="S1a.p8.1" class="ltx_p"><em id="S1a.p8.1.1" class="ltx_emph ltx_font_italic">Part <span id="S1a.p8.1.1.1" class="ltx_text ltx_font_upright">(2)</span>.</em> For $a\preceq b$ every ancestor of $a$ is an ancestor of $b\text{,}$ so</p>
<table id="S1.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(p_{b}-p_{a})(v)\ =\ \mathbf{1}\{v\preceq b\}-\mathbf{1}\{v\preceq a\}\ =\ \mathbf{1}\{a\prec v\preceq b\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p8.2" class="ltx_p">that is, $p_{b}-p_{a}=\mathbf{1}_{(a,b]}\text{.}$ For general $u,w$ put $m:=u\wedge w$ and subtract the two vertical cases,</p>
<table id="S1.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p_{u}-p_{w}\ =\ (p_{u}-p_{m})-(p_{w}-p_{m})\ =\ \mathbf{1}_{(m,u]}-\mathbf{1}_{(m,w]}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p8.3" class="ltx_p">The sets $(m,u]$ and $(m,w]$ are disjoint, since a common element would be a common ancestor of $u$ and $w$ strictly below $m\text{;}$ their union is the set of lower endpoints of the edges on the $u$-to-$w$ path, by the description of that path just used.</p>
</div>
<div id="S1a.p9" class="ltx_para">
<p id="S1a.p9.1" class="ltx_p">For the last assertion, let $u$ and $w$ lie in a connected subtree $C\text{.}$ The $u$-to-$w$ path then runs inside $C\text{,}$ so the support of $p_{u}-p_{w}$ consists of lower endpoints of edges of $C\text{.}$ Distinct edges have distinct lower endpoints, an edge being determined by its lower endpoint, so differences taken within edge-disjoint connected subtrees occupy disjoint coordinate sets.
∎</p>
</div>
<div id="S1a.p10" class="ltx_para">
<p id="S1a.p10.1" class="ltx_p">Fix an integer radius $q\geq 0\text{.}$ The <em id="S1a.p10.1.1" class="ltx_emph ltx_font_italic">residual-depth greedy</em> computes a minimum ancestor $q$-net in one postorder pass, maintaining one number per vertex. Process the vertices in postorder, with a fixed child order, and at each vertex $v$ compute, from the values $r_{c}$ already assigned at its children,</p>
<table id="S1.E2a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{v}:=\max\bigl(\{0\}\cup\{r_{c}+1:\ c\in\operatorname{ch}(v),\ r_{c}\neq-\infty\}\bigr);$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.1.2)</span></td></tr></tbody>
</table>
<p id="S1a.p10.2" class="ltx_p">if $d_{v}=q\text{,}$ select $v$ as a center and set $r_{v}:=-\infty\text{;}$ otherwise set $r_{v}:=d_{v}\text{.}$ After the root has been processed, select it as well if $r_{o}\neq-\infty\text{.}$ The number $r_{v}$ tracks the depth below $v$ of the deepest vertex of $T_{v}$ that no selected center covers, with $-\infty$ standing for none; the proof below verifies this reading.</p>
</div>
<div id="S1.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S1.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma S.1.1</span></span><span id="S1.Thmlemma1.3" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S1.Thmlemma1.p1" class="ltx_para">
<p id="S1.Thmlemma1.p1.1" class="ltx_p"><span id="S1.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">For every integer $q\geq 0\text{,}$ the residual-depth greedy outputs a minimum ancestor $q$-net of $T$ in $O(n)$ operations, and the output is a deterministic function of $(T,q)\text{.}$</span></p>
</div>
</div>
<div id="S1a.p11" class="ltx_para">
<p id="S1a.p11.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S1a.p12" class="ltx_para">
<p id="S1a.p12.1" class="ltx_p">We first verify feasibility, then exhibit the selected centers, in a suitable order, as a run of a conceptually simpler procedure, the <em id="S1a.p12.1.1" class="ltx_emph ltx_font_italic">deepest-uncovered greedy</em>, and finally prove by an exchange argument that every run of that procedure is minimum.</p>
</div>
<div id="S1a.p13" class="ltx_para">
<p id="S1a.p13.1" class="ltx_p"><em id="S1a.p13.1.1" class="ltx_emph ltx_font_italic">Feasibility.</em> Call a vertex <em id="S1a.p13.1.2" class="ltx_emph ltx_font_italic">uncovered</em> at a given moment when no center selected so far is an ancestor of it within distance $q\text{.}$ We claim that after $v$ is processed, $r_{v}$ is exactly the maximal depth below $v$ of an uncovered vertex of $T_{v}\text{,}$ with $r_{v}=-\infty$ when none exists, and that $r_{v}&lt;q\text{.}$ When $v$ is examined, every selected center is an already processed vertex, and no ancestor of $v$ has been processed, so $v$ is uncovered. Moreover, an ancestor of a vertex of $T_{c}\text{,}$ for a child $c$ of $v\text{,}$ lies in $T_{c}$ or strictly above $c\text{,}$ and no center selected after $c$ was processed is of either kind: the subtree $T_{c}$ is finished, and the vertices above $c$ are not yet processed. The uncovered part of $T_{c}$ is therefore still the one described by $r_{c}\text{,}$ and the uncovered vertices of $T_{v}$ are $v$ itself together with those of the children’s subtrees, one level deeper. Hence $d_{v}$ in <a href="#S1.E2a" title="In S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.1.2</span></a> is exactly the maximal depth below $v$ of an uncovered vertex of $T_{v}\text{,}$ and $d_{v}\leq q$ by the inductive bound $r_{c}&lt;q\text{.}$ If $d_{v}=q\text{,}$ selecting $v$ covers every uncovered vertex of $T_{v}\text{,}$ all being descendants of $v$ within distance $q\text{,}$ and $r_{v}=-\infty$ is correct; otherwise no center is added and $r_{v}=d_{v}&lt;q$ is correct. When the root has been processed, either $r_{o}=-\infty$ and nothing remains uncovered, or the final selection covers the remaining uncovered vertices, which lie within $r_{o}&lt;q$ of the root. Each vertex is examined once at cost proportional to its number of children, so the pass costs $O(n)\text{;}$ and the child order being fixed, the algorithm makes no arbitrary choices, so the output is a deterministic function of $(T,q)\text{.}$</p>
</div>
<div id="S1a.p14" class="ltx_para">
<p id="S1a.p14.1" class="ltx_p"><em id="S1a.p14.1.1" class="ltx_emph ltx_font_italic">Reduction to the deepest-uncovered greedy.</em> The comparison procedure repeats the following step until every vertex is covered: pick an uncovered vertex $u$ of maximum depth and select its ancestor at distance exactly $\min\{q,\operatorname{depth}(u)\}\text{.}$ To exhibit the algorithm’s output as a run of this procedure, attach to every center $g$ selected through the test $d_{g}=q$ a <em id="S1a.p14.1.2" class="ltx_emph ltx_font_italic">witness</em> $u_{g}\in T_{g}$ realizing $d_{g}\text{,}$ so that $d_{T}(g,u_{g})=q\text{;}$ if the root is selected at the end, its witness is a deepest vertex left uncovered, at distance $r_{o}&lt;q\text{.}$ Order the selected centers by nonincreasing depth, ties broken by processing order, with the final root selection last, and let $P$ denote the set of centers preceding a given center in this order.</p>
</div>
<div id="S1a.p15" class="ltx_para">
<p id="S1a.p15.1" class="ltx_p">Fix a center $g$ with $d_{T}(g,u_{g})=q\text{.}$ First, $u_{g}$ is uncovered when only $P$ is in place: a center covering $u_{g}$ is an ancestor of $u_{g}$ of depth at least $\operatorname{depth}(u_{g})-q=\operatorname{depth}(g)\text{,}$ so it lies on the vertical segment between $g$ and $u_{g}\text{,}$ inside $T_{g}\text{,}$ and was processed, and selected, before $g\text{;}$ had it covered $u_{g}\text{,}$ then $u_{g}$ would already be covered when $g$ was examined and could not realize $d_{g}\text{.}$ Second, every vertex $w$ strictly deeper than $u_{g}$ is covered by $P\text{:}$ the complete output is feasible, so some selected center $c$ satisfies $c\preceq w$ and $d_{T}(c,w)\leq q\text{,}$ whence</p>
<table id="S1.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{depth}(c)\ \geq\ \operatorname{depth}(w)-q\ &gt;\ \operatorname{depth}(u_{g})-q\ =\ \operatorname{depth}(g),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p15.2" class="ltx_p">and every selected center strictly deeper than $g$ precedes it. Thus at $g$’s turn the vertex $u_{g}$ is a deepest uncovered vertex, and $g$ is its ancestor at distance exactly $q=\min\{q,\operatorname{depth}(u_{g})\}\text{.}$</p>
</div>
<div id="S1a.p16" class="ltx_para">
<p id="S1a.p16.1" class="ltx_p">For the final root selection with witness $u\text{:}$ no nonroot center covers the witness, which is still uncovered after the whole tree has been processed; every $w$ strictly deeper than $u$ is covered by a nonroot center, since otherwise $w$ would be an uncovered vertex deeper than $u$ at that moment, contradicting the maximality defining $r_{o}\text{;}$ and the root is the ancestor of $u$ at distance $\operatorname{depth}(u)=\min\{q,\operatorname{depth}(u)\}\text{,}$ since $\operatorname{depth}(u)=r_{o}&lt;q\text{.}$</p>
</div>
<div id="S1a.p17" class="ltx_para">
<p id="S1a.p17.1" class="ltx_p"><em id="S1a.p17.1.1" class="ltx_emph ltx_font_italic">Optimality by exchange.</em> Suppose, inductively, that some minimum ancestor $q$-net $O$ contains the first $t-1$ centers of a run of the deepest-uncovered greedy; let $u$ be the uncovered vertex of maximum depth picked at step $t$ and $g$ its selected ancestor. Feasibility of $O$ provides $c\in O$ with $c\preceq u$ and $d_{T}(c,u)\leq q\text{;}$ being an ancestor of $u$ of depth at least $\operatorname{depth}(u)-q\text{,}$ the center $c$ lies on the segment between $g$ and $u\text{,}$ and $c$ is not among the first $t-1$ centers, which do not cover $u\text{.}$ Set $O^{\prime}:=(O\setminus\{c\})\cup\{g\}\text{.}$ A vertex $x$ covered by $c$ but not by $g$ is a descendant of $g\text{,}$ as $g\preceq c\preceq x\text{,}$ with $d_{T}(g,x)&gt;q\text{,}$ so that</p>
<table id="S1.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{depth}(x)\ &gt;\ \operatorname{depth}(g)+q\ \geq\ \operatorname{depth}(u),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p17.2" class="ltx_p">and $x$ is covered by the first $t-1$ centers, which lie in $O^{\prime}\text{.}$ Thus $O^{\prime}$ is feasible, contains the first $t$ centers, and $|O^{\prime}|\leq|O|\text{,}$ so $O^{\prime}$ is again a minimum net. By induction the complete run is contained in a minimum net, and being itself feasible, it is minimum.
∎</p>
</div>
<div id="S1a.p18" class="ltx_para">
<p id="S1a.p18.1" class="ltx_p"><em class="ltx_title_proof">Proof of Lemma 2.3.</em></p>
</div>
<div id="S1a.p19" class="ltx_para">
<p id="S1a.p19.1" class="ltx_p">Throughout, write $c_{q}:=\min\{k,[\log(N^{\uparrow}_{T}(q)/k)]_{+}\}$ for the truncated factor of the profile at integer radius $q\text{,}$ the dependence on the fixed index $k$ suppressed from the notation.</p>
</div>
<div id="S1a.p20" class="ltx_para">
<p id="S1a.p20.1" class="ltx_p"><em id="S1a.p20.1.1" class="ltx_emph ltx_font_italic">Part (1).</em> Dividing the truncated factor in (1.4) by $k$ and using $\min\{k,x\}/k=\min\{1,x/k\}$ gives</p>
<table id="S1.E3a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\delta_{k}(T)=\sup_{r&gt;0}\ r\,\min\Bigl\{1,\ \frac{1}{k}\Bigl[\log\frac{N^{\uparrow}_{T}(r)}{k}\Bigr]_{+}\Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.1.3)</span></td></tr></tbody>
</table>
<p id="S1a.p20.2" class="ltx_p">Fix $r\text{.}$ As $k$ increases, $[\log(N^{\uparrow}_{T}(r)/k)]_{+}$ is nonnegative and nonincreasing, and so is $1/k\text{;}$ a product of two nonnegative nonincreasing functions is nonincreasing, and the cap by $1$ preserves this. Every term of the supremum in <a href="#S1.E3a" title="In S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.1.3</span></a> is therefore nonincreasing in $k\text{,}$ and so is $\delta_{k}\text{.}$ For the upper bound, the root is an ancestor of every vertex within distance $h_{T}\text{,}$ so $N^{\uparrow}_{T}(r)=1$ and the term vanishes for $r\geq h_{T}\text{,}$ while for $r&lt;h_{T}$ the term is at most $r&lt;h_{T}\text{;}$ hence $\delta_{k}\leq h_{T}\text{.}$</p>
</div>
<div id="S1a.p21" class="ltx_para">
<p id="S1a.p21.1" class="ltx_p"><em id="S1a.p21.1.1" class="ltx_emph ltx_font_italic">Part (2).</em> Tree distances take integer values, so the covering constraint $d_{T}(a,u)\leq r$ is equivalent to $d_{T}(a,u)\leq\lfloor r\rfloor\text{,}$ and $N^{\uparrow}_{T}(r)=N^{\uparrow}_{T}(\lfloor r\rfloor)$ for every $r\geq 0\text{.}$ The supremum in (1.4) therefore splits along integer radii:</p>
<table id="S1.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{k}(T)=\sup_{q\geq 0}\ \sup_{r\in[q,q+1)\cap(0,\infty)}\ r\,c_{q}=\sup_{q\geq 0}\ (q+1)\,c_{q},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p21.2" class="ltx_p">the inner supremum being approached as $r\uparrow q+1\text{.}$ Radii $q\geq h_{T}$ have $N^{\uparrow}_{T}(q)=1$ and $c_{q}=0\text{,}$ so the outer supremum is a maximum over the integers $0\leq q&lt;h_{T}\text{,}$ an empty maximum being zero; this also covers $n=1\text{,}$ where $h_{T}=0\text{.}$</p>
</div>
<div id="S1a.p22" class="ltx_para">
<p id="S1a.p22.1" class="ltx_p"><em id="S1a.p22.1.1" class="ltx_emph ltx_font_italic">Part (3): the two-sided comparison.</em> Write $G:=\{2^{\ell}-1:\ \ell\in\{0,1,2,\dots\},\ 2^{\ell}\leq h_{T}\}$ for the grid, so that (2.1) reads $\overline{\delta}_{k}=\tfrac{2}{k}\max_{q\in G}(q+1)c_{q}\text{.}$ The grid consists of integer radii below $h_{T}\text{,}$ so part (2) gives $\max_{q\in G}(q+1)c_{q}\leq\alpha_{k}\text{,}$ that is, $\overline{\delta}_{k}\leq 2\delta_{k}\text{.}$ Conversely, fix an integer $0\leq q&lt;h_{T}$ and set $s:=q+1\in[1,h_{T}]\text{;}$ the largest power of two $p\leq s$ satisfies $p&gt;s/2\text{,}$ and $q^{\prime}:=p-1$ belongs to $G$ with $q^{\prime}\leq q\text{.}$ Every ancestor $q^{\prime}$-net is an ancestor $q$-net, so $N^{\uparrow}_{T}(q^{\prime})\geq N^{\uparrow}_{T}(q)$ and $c_{q^{\prime}}\geq c_{q}\text{,}$ whence</p>
<table id="S1.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(q^{\prime}+1)\,c_{q^{\prime}}\ =\ p\,c_{q^{\prime}}\ \geq\ \frac{s}{2}\,c_{q}\ =\ \frac{q+1}{2}\,c_{q}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p22.2" class="ltx_p">Maximizing over $q$ gives $\max_{q\in G}(q+1)c_{q}\geq\alpha_{k}/2\text{,}$ that is, $\overline{\delta}_{k}\geq\delta_{k}\text{.}$ When $h_{T}=0$ both sides vanish by convention. Monotonicity of $k\mapsto\overline{\delta}_{k}$ follows as in part (1), applied to the finite maximum over $G\text{.}$</p>
</div>
<div id="S1a.p23" class="ltx_para">
<p id="S1a.p23.1" class="ltx_p"><em id="S1a.p23.1.1" class="ltx_emph ltx_font_italic">Part (3): the sandwich.</em> Put $K:=\lfloor n/C_{\star}\rfloor\text{.}$ The dimension clause $k&gt;n/C_{\star}$ first holds at $k=K+1\text{,}$ so the minima in (1.5) and (2.2) are over nonempty sets and $k_{0},k_{\mathrm{alg}}\leq K+1\text{.}$ For the lower half: if $k_{0}\leq K\text{,}$ the dimension clause fails at $k_{0}\text{,}$ so the profile clause holds there, $V^{2}\overline{\delta}_{k_{0}}\leq 2V^{2}\delta_{k_{0}}\leq 2A_{0}\sigma^{2}k_{0}\text{,}$ and $k_{\mathrm{alg}}\leq k_{0}\text{;}$ if $k_{0}=K+1\text{,}$ then $k_{\mathrm{alg}}\leq K+1=k_{0}$ directly. For the upper half: if $k_{\mathrm{alg}}=K+1\text{,}$ the lower half forces $k_{0}=K+1=k_{\mathrm{alg}}\text{.}$ Otherwise $k_{\mathrm{alg}}\leq K\text{,}$ so the dimension clause of (2.2) fails at $k_{\mathrm{alg}}\text{,}$ its profile clause holds, and $V^{2}\delta_{k_{\mathrm{alg}}}\leq V^{2}\overline{\delta}_{k_{\mathrm{alg}}}\leq 2A_{0}\sigma^{2}k_{\mathrm{alg}}\text{.}$ If $k_{0}=k_{\mathrm{alg}}$ there is nothing to prove. If $k_{0}&gt;k_{\mathrm{alg}}\text{,}$ every integer $k$ with $k_{\mathrm{alg}}\leq k\leq k_{0}-1$ fails both clauses of (1.5) by the minimality of $k_{0}\text{;}$ in particular $V^{2}\delta_{k}&gt;A_{0}\sigma^{2}k\text{,}$ and combining this with the monotonicity of part (1),</p>
<table id="S1.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$A_{0}\sigma^{2}k\ &lt;\ V^{2}\delta_{k}\ \leq\ V^{2}\delta_{k_{\mathrm{alg}}}\ \leq\ 2A_{0}\sigma^{2}k_{\mathrm{alg}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p23.2" class="ltx_p">so $k&lt;2k_{\mathrm{alg}}\text{.}$ At $k=k_{0}-1$ this reads $k_{0}-1&lt;2k_{\mathrm{alg}}\text{,}$ that is, $k_{0}\leq 2k_{\mathrm{alg}}\text{.}$</p>
</div>
<div id="S1a.p24" class="ltx_para">
<p id="S1a.p24.1" class="ltx_p"><em id="S1a.p24.1.1" class="ltx_emph ltx_font_italic">Part (3): complexity.</em> <a href="#S1.Thmlemma1" title="Lemma S.1.1. ‣ S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.1.1</span></a> computes $N^{\uparrow}_{T}(q)$ exactly in $O(n)$ operations for each integer radius. The grid $G$ has $O(\log(h_{T}+1))$ elements, so storing $\{N^{\uparrow}_{T}(q)\}_{q\in G}$ costs $O(n\log(h_{T}+1))\text{,}$ after which each evaluation of $\overline{\delta}_{k}$ costs $O(\log(h_{T}+1))\text{.}$ The predicate in (2.2) is monotone in $k\text{:}$ in its profile clause the left side is nonincreasing by the monotonicity proved above and the right side is increasing, and its dimension clause is monotone; $k_{\mathrm{alg}}$ is therefore located by binary search over $\{1,\dots,K+1\}$ with $O(\log n)$ predicate evaluations. Since $h_{T}&lt;n\text{,}$ the total is $O(n\log(n+1))\text{.}$ For $k_{0}\text{,}$ running <a href="#S1.Thmlemma1" title="Lemma S.1.1. ‣ S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.1.1</span></a> at every integer radius $0\leq q&lt;h_{T}$ costs $O(n\,h_{T})$ and stores all counts; each $\alpha_{k}$ then costs $O(h_{T})$ by (2.3), and scanning $k=1,2,\dots$ until the first index satisfying (1.5), at most $K+1\leq n$ values, costs $O(n\,h_{T})$ in total.
∎</p>
</div>
<div id="S1a.p25" class="ltx_para">
<p id="S1a.p25.1" class="ltx_p">Finally, we verify the center-convention comparison stated with (1.6). Write $H^{c,\mathrm{int}}_{T}(t)$ for the covering entropy of $\mathcal{F}_{V}(T)$ at squared radius $t$ with centers restricted to the body, and</p>
<table id="S1.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\rho^{\mathrm{int}}_{T}(V,\sigma)\ :=\ \inf_{t&gt;0}\ \bigl[t+\sigma^{2}H^{c,\mathrm{int}}_{T}(t)\bigr].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p25.2" class="ltx_p">Since every cover with centers in the body is in particular a cover with free centers, $H^{c}_{T}(t)\leq H^{c,\mathrm{int}}_{T}(t)$ for every $t&gt;0\text{.}$ Conversely, fix $t&gt;0$ and a cover of the body by $\exp H^{c}_{T}(t)$ balls of radius $\sqrt{t}$ with arbitrary centers, and replace the center $y$ of each ball by its Euclidean projection $\pi_{y}:=\Pi_{\mathcal{F}_{V}(T)}(y)$ onto the body. The variational inequality of the projection, $\langle y-\pi_{y},\mu-\pi_{y}\rangle\leq 0$ for every $\mu\in\mathcal{F}_{V}(T)\text{,}$ gives</p>
<table id="S1.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|\mu-\pi_{y}\|_{2}^{2}\ \leq\ \|\mu-y\|_{2}^{2}-\|y-\pi_{y}\|_{2}^{2}\ \leq\ \|\mu-y\|_{2}^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p25.3" class="ltx_p">so every $\mu$ within $\sqrt{t}$ of $y$ is within $\sqrt{t}$ of $\pi_{y}\text{.}$ The projected balls, of the same radius and number, cover the body with internal centers, so $H^{c,\mathrm{int}}_{T}(t)\leq H^{c}_{T}(t)\text{.}$ The two entropies coincide at every radius, and $\rho^{\mathrm{int}}_{T}=\rho_{T}\text{:}$ the center convention is immaterial.</p>
</div>
<div id="S1a.p26" class="ltx_para">
<p id="S1a.p26.1" class="ltx_p">We also verify the comparison with the capped constraint of <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib1" title="" class="ltx_ref">Chatterjee and Lafferty (2018)</a></cite>, stated in Section 1.1. Let</p>
<table id="S1.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{K}_{V}(T)\ :=\ \bigl\{\mu\in\mathcal{F}(T):\ \mu(o)\leq V\bigr\},\qquad R^{\mathrm{cap}}_{T}(V,\sigma)\ :=\ \inf_{\widehat{\mu}}\ \sup_{\mu\in\mathcal{K}_{V}(T)}\mathbb{E}_{\mu}\bigl\|\widehat{\mu}(Y)-\mu\bigr\|_{2}^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p26.2" class="ltx_p">the infimum over the same maps as in (1.3), and assume $n\geq 2\text{.}$ Since $\mathcal{F}_{V}(T)\subseteq\mathcal{K}_{V}(T)\text{,}$ every estimator has at least as large a supremum risk on the larger set, so $R^{\mathrm{cap}}_{T}\geq R^{*}_{T}\text{.}$</p>
</div>
<div id="S1a.p27" class="ltx_para">
<p id="S1a.p27.1" class="ltx_p">For the reverse, split $\mu$ into its root value $\mu(o)$ and its remaining coordinates $\mu_{-}\text{,}$ and write $C_{a}$ for the set of $\mu_{-}$ arising from $\mu\in\mathcal{F}_{a}(T)\text{.}$ Adding $(V-a)p_{o}$ to such a $\mu$ raises its root value to $V$ and changes no other coordinate, so $C_{a}\subseteq C_{V}$ whenever $0&lt;a\leq V\text{,}$ and $C_{0}:=\{0\}\subseteq C_{V}$ as well. On the slice the root value is known, so it is estimated at no loss, while $Y_{o}$ is independent of $Y_{-}$ with a law free of $\mu_{-}$ and therefore acts as pure randomization, which cannot lower a maximum risk under squared loss; hence $R^{*}_{T}(V,\sigma)$ is exactly the minimax risk of estimating $\mu_{-}\in C_{V}$ from $Y_{-}\text{.}$ Fix $\varepsilon&gt;0\text{,}$ let $\widehat{\theta}$ attain that risk to within $\varepsilon\text{,}$ and on the capped body take $\widehat{\mu}_{-}:=\widehat{\theta}(Y_{-})$ together with</p>
<table id="S1.Ex15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{\mu}_{o}\ :=\ \begin{cases}0,&amp;V\leq\sigma,\\[2.0pt] \Pi_{[0,V]}(Y_{o}),&amp;V&gt;\sigma.\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p27.2" class="ltx_p">Every $\mu\in\mathcal{K}_{V}(T)$ has $\mu_{-}\in C_{\mu(o)}\subseteq C_{V}\text{,}$ so its nonroot risk is at most $R^{*}_{T}(V,\sigma)+\varepsilon\text{.}$ Its root risk is at most $\mu(o)^{2}\leq V^{2}$ in the first case, and at most $\mathbb{E}(Y_{o}-\mu(o))^{2}=\sigma^{2}$ in the second, projection onto an interval containing $\mu(o)$ being nonexpansive. Letting $\varepsilon\downarrow 0\text{,}$</p>
<table id="S1.Ex16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{\mathrm{cap}}_{T}(V,\sigma)\ \leq\ R^{*}_{T}(V,\sigma)+\min\{V^{2},\sigma^{2}\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p27.3" class="ltx_p">Finally $n\geq 2$ forces $H_{T}\geq 1\text{,}$ so the two-point bound (3.8) gives</p>
<table id="S1.Ex17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\min\{V^{2},\sigma^{2}\}\ \leq\ \min\{V^{2}H_{T},\ \sigma^{2}\}\ \leq\ c^{-1}R^{*}_{T}(V,\sigma):$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1a.p27.4" class="ltx_p">fixing the root value and capping it pose the same problem up to universal constants.</p>
</div>
<div id="S1a.p28" class="ltx_para">
<p id="S1a.p28.1" class="ltx_p">The comparison is constructive: the estimator of Theorem 2 transfers to the capped body. At budget $V$ its root coordinate is identically $V\text{,}$ and its nonroot coordinates depend on $Y$ only through $Y_{-}\text{:}$ every integer state has root coordinate $k\text{,}$ so the root factor cancels from the ratio (4.2), and the branch selection in (4.3) depends on $(T,V,\sigma)$ alone. Write $\widehat{\mu}^{V}_{-}(Y_{-})$ for this nonroot part. For $\mu\in\mathcal{K}_{V}(T)$ the raised signal $(V,\mu_{-})$ lies in $\mathcal{F}_{V}(T)\text{,}$ and $Y_{-}$ has the law of the nonroot data of the slice model there, so Theorem 2 bounds the risk of $\widehat{\mu}^{V}_{-}$ against $\mu_{-}$ by $C\,R^{*}_{T}(V,\sigma)\text{,}$ uniformly over $\mathcal{K}_{V}(T)\text{.}$ Paired with the root rule above, it yields a deterministic estimator, computed in $O(n^{2}\log(n+1))$ arithmetic operations, whose risk on the capped body is at most $C\bigl(R^{*}_{T}(V,\sigma)+\min\{V^{2},\sigma^{2}\}\bigr)\leq C^{\prime}\,R^{\mathrm{cap}}_{T}(V,\sigma)\text{.}$</p>
</div>
</section>
<section id="S2a" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-coded-cover-1"><span class="ltx_tag ltx_tag_section">S.2 </span>The Coded Cover</h2>

<div id="S2a.p1" class="ltx_para">
<p id="S2a.p1.1" class="ltx_p">This section completes the proof of Proposition 3.1. The main text gives the mechanism behind each stage. To make this section self-contained, we restate the objects below and supply the estimates and accounting: the floor on the working scale and the sizes of the nets, the structure of the cells, the disjointness and charge accounting of the heavy hierarchy, the collapse and exit estimates, the edge count of the skeleton together with the explicit constants of the error assembly, and the counting bound for the coded cover.</p>
</div>
<div id="S2a.p2" class="ltx_para">
<p id="S2a.p2.1" class="ltx_p">Throughout, $k$ is an integer with $2\leq k\leq n/C_{\star}$ and, as in Section 3.1, $\bar{\alpha}:=k\overline{\delta}_{k}(T)\text{;}$ the level weights are $m_{j}=2^{j}$ for $0\leq j\leq J\text{,}$ with $m_{J}$ the largest power of two strictly below $k\text{;}$ $S_{j}$ is the minimum ancestor $\lfloor\bar{\alpha}/m_{j}\rfloor$-net computed by the greedy of <a href="#S1.Thmlemma1" title="Lemma S.1.1. ‣ S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.1.1</span></a>; and $R_{j}:=S_{0}\cup\dots\cup S_{j}\text{.}$ The net hierarchy, the active support and the activation charges below therefore depend on $(T,k)$ alone, the signal entering only through the stopped refinement of the construction. The active support, the first-appearance weight, and the activation charge are</p>
<table id="S2.Ex1a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$A_{k}:=R_{J},\qquad\omega(v):=\min\{m_{j}:\ v\in R_{j}\},\qquad\widetilde{\omega}(v):=\omega(v)\,\mathbf{1}\{v\notin R_{0}\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p2.2" class="ltx_p">and the code length of an integer vector $z$ supported on $A_{k}$ is</p>
<table id="S2.Ex2a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Gamma(z)\ :=\ \sum_{v\in A_{k}}\Bigl(|z_{v}|+\widetilde{\omega}(v)\,\mathbf{1}\{z_{v}\neq 0\}\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p2.3" class="ltx_p">the display (3.1). Throughout, $e_{v}$ denotes the coordinate vector at $v\text{.}$</p>
</div>
<div id="S2a.p3" class="ltx_para">
<p id="S2a.p3.1" class="ltx_p">The first lemma contains the size facts quoted when the nets are introduced: the working scale is never degenerate, and the profile itself caps the size of every net.</p>
</div>
<div id="S2.Thmlemma1a" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma1a.2" class="ltx_text ltx_font_bold">Lemma S.2.1</span></span><span id="S2.Thmlemma1a.3" class="ltx_text ltx_font_bold"> (Scale floor and net sizes).</span></h6>
<div id="S2.Thmlemma1a.p1" class="ltx_para">
<p id="S2.Thmlemma1a.p1.1" class="ltx_p"><span id="S2.Thmlemma1a.p1.1.1" class="ltx_text ltx_font_italic">For every integer $2\leq k\leq n/C_{\star}\text{:}$</span></p>
<ol id="S2.I1a" class="ltx_enumerate">
<li id="S2.I1.i1a" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S2.I1.i1a.p1" class="ltx_para">
<p id="S2.I1.i1a.p1.1" class="ltx_p">$\bar{\alpha}\geq\alpha_{k}(T)\geq 2$<span id="S2.I1.i1a.p1.1.1" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S2.I1.i2a" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S2.I1.i2a.p1" class="ltx_para">
<p id="S2.I1.i2a.p1.1" class="ltx_p">$N^{\uparrow}_{T}(\lfloor\bar{\alpha}/m_{j}\rfloor)\leq ke^{m_{j}}$<span id="S2.I1.i2a.p1.1.1" class="ltx_text ltx_font_italic"> for every
</span>$0\leq j\leq J$<span id="S2.I1.i2a.p1.1.2" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S2.I1.i3a" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S2.I1.i3a.p1" class="ltx_para">
<p id="S2.I1.i3a.p1.1" class="ltx_p">$|R_{j}|\leq 2ke^{m_{j}}$<span id="S2.I1.i3a.p1.1.1" class="ltx_text ltx_font_italic"> for every </span>$0\leq j\leq J$<span id="S2.I1.i3a.p1.1.2" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S2a.p4" class="ltx_para">
<p id="S2a.p4.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S2a.p5" class="ltx_para">
<p id="S2a.p5.1" class="ltx_p"><em id="S2a.p5.1.1" class="ltx_emph ltx_font_italic">Part (1).</em> The surrogate dominates the profile, $\overline{\delta}_{k}\geq\delta_{k}$ by Lemma 2.3, so $\bar{\alpha}=k\overline{\delta}_{k}\geq k\delta_{k}=\alpha_{k}(T)\text{.}$ For the floor, tree distances are integers, so at radii $0&lt;r&lt;1$ every vertex is its own only ancestor within distance $r\text{;}$ every ancestor $r$-net then contains all of $\mathsf{V}\text{,}$ and $N^{\uparrow}_{T}(r)=n\text{.}$ Hence</p>
<table id="S2.Ex3a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{k}(T)\ \geq\ \sup_{0&lt;r&lt;1}\ r\,\min\Bigl\{k,\ \Bigl[\log\frac{n}{k}\Bigr]_{+}\Bigr\}\ =\ \min\Bigl\{k,\ \Bigl[\log\frac{n}{k}\Bigr]_{+}\Bigr\}\ \geq\ \min\{2,\ \log C_{\star}\}\ =\ 2,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p5.2" class="ltx_p">using $k\geq 2$ and $n/k\geq C_{\star}=e^{2}\text{.}$</p>
</div>
<div id="S2a.p6" class="ltx_para">
<p id="S2a.p6.1" class="ltx_p"><em id="S2a.p6.1.1" class="ltx_emph ltx_font_italic">Part (2).</em> Fix $0\leq j\leq J$ and suppose $N^{\uparrow}_{T}(\lfloor\bar{\alpha}/m_{j}\rfloor)&gt;ke^{m_{j}}\text{.}$ The radius $r:=\bar{\alpha}/m_{j}$ is positive by part (<a href="#S2.I1.i1a" title="Item 1 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>), and the covering constraint depends on $r$ only through $\lfloor r\rfloor\text{,}$ so $N^{\uparrow}_{T}(r)=N^{\uparrow}_{T}(\lfloor r\rfloor)&gt;ke^{m_{j}}\text{,}$ that is, $[\log(N^{\uparrow}_{T}(r)/k)]_{+}&gt;m_{j}\text{.}$ Since also $m_{j}\leq m_{J}&lt;k\text{,}$ the minimum of $k$ and this positive part exceeds $m_{j}\text{,}$ and the term of (1.4) at $r$ satisfies</p>
<table id="S2.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$r\,\min\Bigl\{k,\ \Bigl[\log\frac{N^{\uparrow}_{T}(r)}{k}\Bigr]_{+}\Bigr\}\ &gt;\ \frac{\bar{\alpha}}{m_{j}}\cdot m_{j}\ =\ \bar{\alpha}\ \geq\ \alpha_{k}(T),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p6.2" class="ltx_p">contradicting that $\alpha_{k}(T)$ is the supremum of these terms.</p>
</div>
<div id="S2a.p7" class="ltx_para">
<p id="S2a.p7.1" class="ltx_p"><em id="S2a.p7.1.1" class="ltx_emph ltx_font_italic">Part (3).</em> The sets $S_{i}$ are minimum nets, so $|S_{i}|=N^{\uparrow}_{T}(\lfloor\bar{\alpha}/m_{i}\rfloor)\leq ke^{m_{i}}$ by part (<a href="#S2.I1.i2a" title="Item 2 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>), and $|R_{j}|\leq k\sum_{i\leq j}e^{m_{i}}\text{.}$ For $j\geq 1$ the sum has $j$ terms before the last, each at most $e^{m_{j-1}}\text{,}$ and $j\leq e^{2^{j-1}}$ gives $je^{m_{j-1}}\leq e^{m_{j-1}+2^{j-1}}=e^{m_{j}}\text{,}$ so $\sum_{i\leq j}e^{m_{i}}\leq 2e^{m_{j}}\text{;}$ for $j=0$ this is immediate.
∎</p>
</div>
<div id="S2a.p8" class="ltx_para">
<p id="S2a.p8.1" class="ltx_p">The cells inherit their structure from the nesting of the nets alone. Parts (2)–(4) below are the rooted-connectedness, refinement, and radius properties quoted in the main body; part (3) also identifies the parent of each cell, the hierarchy used from here on.</p>
</div>
<div id="S2.Thmlemma2a" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma2a.2" class="ltx_text ltx_font_bold">Lemma S.2.2</span></span><span id="S2.Thmlemma2a.3" class="ltx_text ltx_font_bold"> (Cell structure).</span></h6>
<div id="S2.Thmlemma2a.p1" class="ltx_para">
<p id="S2.Thmlemma2a.p1.1" class="ltx_p"><span id="S2.Thmlemma2a.p1.1.1" class="ltx_text ltx_font_italic">Fix $0\leq j\leq J$ and let $a_{j}(v)$ be the deepest ancestor of $v$ in $R_{j}\text{.}$ Then:</span></p>
<ol id="S2.I3a" class="ltx_enumerate">
<li id="S2.I3.i1a" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S2.I3.i1a.p1" class="ltx_para">
<p id="S2.I3.i1a.p1.1" class="ltx_p"><span id="S2.I3.i1a.p1.1.1" class="ltx_text ltx_font_italic">the cells </span>$B_{a,j}=\{v:a_{j}(v)=a\}$<span id="S2.I3.i1a.p1.1.2" class="ltx_text ltx_font_italic">,
</span>$a\in R_{j}$<span id="S2.I3.i1a.p1.1.3" class="ltx_text ltx_font_italic">, partition </span>$\mathsf{V}$<span id="S2.I3.i1a.p1.1.4" class="ltx_text ltx_font_italic">, and each contains its root </span>$a$<span id="S2.I3.i1a.p1.1.5" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S2.I3.i2a" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S2.I3.i2a.p1" class="ltx_para">
<p id="S2.I3.i2a.p1.1" class="ltx_p"><span id="S2.I3.i2a.p1.1.1" class="ltx_text ltx_font_italic">if </span>$v\in B_{a,j}$<span id="S2.I3.i2a.p1.1.2" class="ltx_text ltx_font_italic"> and </span>$a\preceq z\preceq v$<span id="S2.I3.i2a.p1.1.3" class="ltx_text ltx_font_italic">,
then </span>$z\in B_{a,j}$<span id="S2.I3.i2a.p1.1.4" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S2.I3.i3a" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S2.I3.i3a.p1" class="ltx_para">
<p id="S2.I3.i3a.p1.1" class="ltx_p"><span id="S2.I3.i3a.p1.1.1" class="ltx_text ltx_font_italic">if </span>$j&lt;J$<span id="S2.I3.i3a.p1.1.2" class="ltx_text ltx_font_italic"> and </span>$a_{j+1}(u)=b$<span id="S2.I3.i3a.p1.1.3" class="ltx_text ltx_font_italic">, then
</span>$a_{j}(u)=a_{j}(b)$<span id="S2.I3.i3a.p1.1.4" class="ltx_text ltx_font_italic">; consequently every level-</span>$(j{+}1)$<span id="S2.I3.i3a.p1.1.5" class="ltx_text ltx_font_italic"> cell is contained
in a single level-</span>$j$<span id="S2.I3.i3a.p1.1.6" class="ltx_text ltx_font_italic"> cell, whose root is an ancestor of its root;</span></p>
</div></li>
<li id="S2.I3.i4" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">4.</span> 
<div id="S2.I3.i4.p1" class="ltx_para">
<p id="S2.I3.i4.p1.1" class="ltx_p">$d_{T}(a,v)\leq\lfloor\bar{\alpha}/m_{j}\rfloor$<span id="S2.I3.i4.p1.1.1" class="ltx_text ltx_font_italic"> for
every </span>$v\in B_{a,j}$<span id="S2.I3.i4.p1.1.2" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S2a.p9" class="ltx_para">
<p id="S2a.p9.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S2a.p10" class="ltx_para">
<p id="S2a.p10.1" class="ltx_p">All four parts are read off the chain structure of ancestors and the nesting $R_{j}\subseteq R_{j+1}\text{.}$</p>
</div>
<div id="S2a.p11" class="ltx_para">
<p id="S2a.p11.1" class="ltx_p"><em id="S2a.p11.1.1" class="ltx_emph ltx_font_italic">Part (1).</em> The root lies in every ancestor net, being its own only ancestor, so every vertex has an ancestor in $R_{j}\text{;}$ the ancestors of $v$ form a chain, so among them the elements of $R_{j}$ have a unique deepest member, and $a_{j}(v)$ is well defined. The fibers of $v\mapsto a_{j}(v)$ partition $\mathsf{V}\text{,}$ and $a_{j}(a)=a$ for $a\in R_{j}\text{.}$</p>
</div>
<div id="S2a.p12" class="ltx_para">
<p id="S2a.p12.1" class="ltx_p"><em id="S2a.p12.1.1" class="ltx_emph ltx_font_italic">Part (2).</em> Every ancestor of $z$ is an ancestor of $v\text{,}$ so every $R_{j}$-ancestor of $z$ has depth at most $\operatorname{depth}(a_{j}(v))=\operatorname{depth}(a)\text{;}$ and $a$ itself is an $R_{j}$-ancestor of $z\text{,}$ since $a\preceq z\text{.}$ Hence $a_{j}(z)=a\text{.}$</p>
</div>
<div id="S2a.p13" class="ltx_para">
<p id="S2a.p13.1" class="ltx_p"><em id="S2a.p13.1.1" class="ltx_emph ltx_font_italic">Part (3).</em> Let $s$ be an $R_{j}$-ancestor of $u\text{.}$ Then $s\in R_{j+1}\text{,}$ so $\operatorname{depth}(s)\leq\operatorname{depth}(b)\text{;}$ and $s$ and $b$ are comparable, both being ancestors of $u\text{,}$ so $s\preceq b$ and $s$ is an $R_{j}$-ancestor of $b\text{.}$ Conversely, every $R_{j}$-ancestor of $b$ is an ancestor of $u\text{,}$ since $b\preceq u\text{.}$ The $R_{j}$-ancestors of $u$ and of $b$ therefore coincide, and $a_{j}(u)=a_{j}(b)\text{.}$ In particular $B_{b,j+1}\subseteq B_{a_{j}(b),j}\text{,}$ and $a_{j}(b)\preceq b\text{.}$</p>
</div>
<div id="S2a.p14" class="ltx_para">
<p id="S2a.p14.1" class="ltx_p"><em id="S2a.p14.1.1" class="ltx_emph ltx_font_italic">Part (4).</em> The net property supplies $s\in R_{j}$ with $s\preceq v$ and $d_{T}(s,v)\leq\lfloor\bar{\alpha}/m_{j}\rfloor\text{.}$ The deepest $R_{j}$-ancestor $a=a_{j}(v)$ has $\operatorname{depth}(a)\geq\operatorname{depth}(s)\text{,}$ so $a$ lies on the segment from $s$ to $v$ and $d_{T}(a,v)\leq d_{T}(s,v)\leq\lfloor\bar{\alpha}/m_{j}\rfloor\text{.}$
∎</p>
</div>
<div id="S2a.p15" class="ltx_para">
<p id="S2a.p15.1" class="ltx_p">The remaining facts concern the stopped refinement that the proof of Proposition 3.1 runs for a fixed signal. Fix $f=\sum_{u}\lambda_{u}p_{u}$ with $\lambda_{u}\geq 0$ and $\sum_{u}\lambda_{u}=1\text{,}$ write $\lambda(B):=\sum_{u\in B}\lambda_{u}\text{,}$ write $m(B):=m_{j}$ for the <em id="S2a.p15.1.1" class="ltx_emph ltx_font_italic">level weight</em> of a level-$j$ cell $B\text{,}$ and call $B$ heavy when $\lambda(B)&gt;m(B)/k$ and light otherwise. The refinement begins at level $0\text{,}$ refines every heavy cell into its level-$(j{+}1)$ subcells, stops at every light cell, and stops everything at level $J\text{.}$ The cells at which it stops are the <em id="S2a.p15.1.2" class="ltx_emph ltx_font_italic">terminal</em> cells. They partition $\mathsf{V}$ because the cells of one level do and each refinement step replaces a cell by a partition of it (<a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i1a" title="Item 1 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>),(<a href="#S2.I3.i3a" title="Item 3 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>)), and $\mathcal{L}$ denotes their collection. For $L\in\mathcal{L}$ we write $a_{L}$ for its root and $\lambda_{L}:=\lambda(L)\text{.}$ As in the main proof, $U$ consists of $R_{0}$ together with the roots of all heavy cells; a heavy cell is <em id="S2a.p15.1.3" class="ltx_emph ltx_font_italic">maximal</em> when no heavy cell lies strictly below it in the hierarchy of <a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i3a" title="Item 3 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>).</p>
</div>
<div id="S2.Thmlemma3a" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma3a.2" class="ltx_text ltx_font_bold">Lemma S.2.3</span></span><span id="S2.Thmlemma3a.3" class="ltx_text ltx_font_bold"> (The heavy structure).</span></h6>
<div id="S2.Thmlemma3a.p1" class="ltx_para">
<p id="S2.Thmlemma3a.p1.1" class="ltx_p"><span id="S2.Thmlemma3a.p1.1.1" class="ltx_text ltx_font_italic">In this setting:</span></p>
<ol id="S2.I5" class="ltx_enumerate">
<li id="S2.I5.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S2.I5.i1.p1" class="ltx_para">
<p id="S2.I5.i1.p1.1" class="ltx_p"><span id="S2.I5.i1.p1.1.1" class="ltx_text ltx_font_italic">distinct maximal heavy cells have disjoint
underlying vertex sets;</span></p>
</div></li>
<li id="S2.I5.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S2.I5.i2.p1" class="ltx_para">
<p id="S2.I5.i2.p1.1" class="ltx_p"><span id="S2.I5.i2.p1.1.1" class="ltx_text ltx_font_italic">the minimal rooted subtree </span>$S$<span id="S2.I5.i2.p1.1.2" class="ltx_text ltx_font_italic"> spanning </span>$U$<span id="S2.I5.i2.p1.1.3" class="ltx_text ltx_font_italic">
has at most </span>$5\bar{\alpha}k$<span id="S2.I5.i2.p1.1.4" class="ltx_text ltx_font_italic"> edges;</span></p>
</div></li>
<li id="S2.I5.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S2.I5.i3.p1" class="ltx_para">
<p id="S2.I5.i3.p1.1" class="ltx_p">$\sum_{v\in U\setminus R_{0}}\widetilde{\omega}(v)&lt;2k$<span id="S2.I5.i3.p1.1.1" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S2.I5.i4" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">4.</span> 
<div id="S2.I5.i4.p1" class="ltx_para">
<p id="S2.I5.i4.p1.1" class="ltx_p">$\sum_{C\ \text{maximal heavy}}m(C)&lt;k$<span id="S2.I5.i4.p1.1.1" class="ltx_text ltx_font_italic">, which is the display (3.3) of
the main paper.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S2a.p16" class="ltx_para">
<p id="S2a.p16.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S2a.p17" class="ltx_para">
<p id="S2a.p17.1" class="ltx_p">Part (<a href="#S2.I5.i1" title="Item 1 ‣ Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>) is a chain argument in the hierarchy, and part (<a href="#S2.I5.i4" title="Item 4 ‣ Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>) follows from it; part (<a href="#S2.I5.i2" title="Item 2 ‣ Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) charges the skeleton to vertical segments along the nets; part (<a href="#S2.I5.i3" title="Item 3 ‣ Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>) charges activation weights to maximal heavy cells.</p>
</div>
<div id="S2a.p18" class="ltx_para">
<p id="S2a.p18.1" class="ltx_p"><em id="S2a.p18.1.1" class="ltx_emph ltx_font_italic">Parts (1) and (4).</em> Suppose two distinct heavy cells $(B,i)$ and $(B^{\prime},j)$ with $i\leq j$ have intersecting underlying sets. Cells at one level partition $\mathsf{V}\text{,}$ so $i&lt;j\text{.}$ Iterating <a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i3a" title="Item 3 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), $B^{\prime}$ is contained in a unique cell of each level below $j\text{;}$ its level-$i$ cell meets $B\text{,}$ hence equals $B\text{,}$ and the chain of cells containing $B^{\prime}$ at levels $i,\dots,j$ ascends from $(B^{\prime},j)$ to $(B,i)$ in the hierarchy. Each cell of this chain, at level $\ell$ say, has mass at least $\lambda(B^{\prime})&gt;m_{j}/k\geq m_{\ell}/k$ and is therefore heavy. In particular the chain member at level $i{+}1$ is a heavy cell strictly below $(B,i)\text{,}$ so $(B,i)$ is not maximal. Distinct maximal heavy cells therefore cannot intersect. Each carries mass exceeding $m(C)/k\text{,}$ and their supports being disjoint, their masses total at most $\lambda(\mathsf{V})=1\text{,}$ so</p>
<table id="S2.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{C\ \text{maximal heavy}}m(C)\ &lt;\ k,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p18.2" class="ltx_p">which is part (<a href="#S2.I5.i4" title="Item 4 ‣ Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>); the empty family satisfies it trivially.</p>
</div>
<div id="S2a.p19" class="ltx_para">
<p id="S2a.p19.1" class="ltx_p"><em id="S2a.p19.1.1" class="ltx_emph ltx_font_italic">Part (2).</em> The subtree $S$ lies in the union of two families of vertical segments, whose total length we bound.</p>
</div>
<div id="S2a.p20" class="ltx_para">
<p id="S2a.p20.1" class="ltx_p">First, connect $R_{0}$ to the root. For $a\in R_{0}\setminus\{o\}\text{,}$ the net property of $R_{0}$ at the parent of $a$ supplies $s\in R_{0}$ with $s\preceq\operatorname{pa}(a)$ and $d_{T}(s,\operatorname{pa}(a))\leq\lfloor\bar{\alpha}\rfloor\text{;}$ the deepest strict $R_{0}$-ancestor $\bar{a}$ of $a$ then lies on the segment from $s$ to $a\text{,}$ so</p>
<table id="S2.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{T}(\bar{a},a)\ \leq\ d_{T}(s,a)\ \leq\ \bar{\alpha}+1\ \leq\ \tfrac{3}{2}\,\bar{\alpha},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p20.2" class="ltx_p">by <a href="#S2.Thmlemma1a" title="Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.1</span></a>(<a href="#S2.I1.i1a" title="Item 1 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>). Iterating $a\mapsto\bar{a}$ from any element of $R_{0}$ reaches the root, which belongs to every ancestor net, so the segments $[\bar{a},a]\text{,}$ $a\in R_{0}\setminus\{o\}\text{,}$ connect $R_{0}$ to $o\text{;}$ by <a href="#S2.Thmlemma1a" title="Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.1</span></a>(<a href="#S2.I1.i2a" title="Item 2 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) their total length is at most $\tfrac{3}{2}\bar{\alpha}\,|R_{0}|\leq\tfrac{3}{2}e\,\bar{\alpha}k\text{.}$</p>
</div>
<div id="S2a.p21" class="ltx_para">
<p id="S2a.p21.1" class="ltx_p">Second, connect the heavy roots to $R_{0}\text{.}$ The root $b$ of a heavy cell $B$ at level $j\geq 1$ lies in its parent cell, whose root $a_{j-1}(b)$ is an ancestor of $b$ within distance $\lfloor\bar{\alpha}/m_{j-1}\rfloor\leq 2\bar{\alpha}/m_{j}$ (<a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i3a" title="Item 3 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>)–(<a href="#S2.I3.i4" title="Item 4 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>)); and the parent cell is heavy as well, its mass being at least $\lambda(B)&gt;m_{j}/k&gt;m_{j-1}/k\text{.}$ Iterating these segments joins every heavy root to the root of a level-$0$ cell, which lies in $R_{0}\text{.}$ At level $j$ the heavy cells are disjoint and each has mass exceeding $m_{j}/k\text{,}$ so there are fewer than $k/m_{j}$ of them, and the segments they contribute have total length less than</p>
<table id="S2.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{j\geq 1}\frac{k}{m_{j}}\cdot\frac{2\bar{\alpha}}{m_{j}}\ =\ 2\bar{\alpha}k\sum_{j\geq 1}4^{-j}\ =\ \tfrac{2}{3}\,\bar{\alpha}k.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p21.2" class="ltx_p">Every member of $U$ is thus connected to the root inside the union of the two families, so $S$ is contained in that union and $|E(S)|\leq\tfrac{3}{2}e\,\bar{\alpha}k+\tfrac{2}{3}\,\bar{\alpha}k\leq 5\bar{\alpha}k\text{.}$</p>
</div>
<div id="S2a.p22" class="ltx_para">
<p id="S2a.p22.1" class="ltx_p"><em id="S2a.p22.1.1" class="ltx_emph ltx_font_italic">Part (3).</em> The set $U\setminus R_{0}$ consists of roots of heavy cells at levels $j\geq 1\text{.}$ Charge each $v\in U\setminus R_{0}$ to a heavy cell rooted at $v$ of minimal level $j(v)\geq 1\text{;}$ roots of level-$j$ cells lie in $R_{j}\text{,}$ so $\widetilde{\omega}(v)=\omega(v)\leq m_{j(v)}\text{,}$ and the charging is injective into the set $\mathcal{H}$ of heavy cells. Hence</p>
<table id="S2.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{v\in U\setminus R_{0}}\widetilde{\omega}(v)\ \leq\ \sum_{(B,j)\in\mathcal{H}}m_{j}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p22.2" class="ltx_p">Assign every heavy cell to one maximal heavy cell weakly below it in the hierarchy, obtained by descending to heavy children while one exists. The cells assigned to a fixed maximal cell $(C,\ell)$ all lie on its ancestor chain, so their level weights total at most $m_{0}+m_{1}+\dots+m_{\ell}&lt;2m_{\ell}\text{,}$ and</p>
<table id="S2.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{(B,j)\in\mathcal{H}}m_{j}\ \leq\ 2\sum_{C\ \text{maximal heavy}}m(C)\ &lt;\ 2k,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p22.3" class="ltx_p">the last step by part (<a href="#S2.I5.i4" title="Item 4 ‣ Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>), which also covers the case of an empty family.
∎</p>
</div>
<div id="S2a.p23" class="ltx_para">
<p id="S2a.p23.1" class="ltx_p">The construction of the main proof samples the light exits at random. The next lemma supplies the collapse bound quoted there, the exit estimates behind the fixed realization, and the budgets that realization carries. Its objects are the following.</p>
</div>
<div id="S2a.p24" class="ltx_para">
<p id="S2a.p24.1" class="ltx_p">Collapsing every terminal cell to its root gives $g:=\sum_{L\in\mathcal{L}}\lambda_{L}p_{a_{L}}\text{.}$ A heavy terminal cell is one the refinement did not split, so it sits at level $J$ and no heavy cell lies below it; being maximal it contributes $m_{J}\geq k/2$ to the sum in <a href="#S2.Thmlemma3a" title="Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.3</span></a>(<a href="#S2.I5.i4" title="Item 4 ‣ Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>), and there is therefore at most one. Each terminal cell $L$ is attached to $U$ at $h(L):=a_{L}$ when $L$ is a level-$0$ cell or the heavy terminal one, and otherwise at the root of the parent cell of $L\text{,}$ which is heavy because $L$ was reached by the refinement; either way $h(L)\in U\text{,}$ and $h(L)\preceq a_{L}$ by <a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i3a" title="Item 3 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>). Put $q_{L}:=p_{a_{L}}-p_{h(L)}\text{.}$ In the first two cases $q_{L}=0\text{;}$ otherwise, $L$ sits at a level $j\geq 1\text{,}$ and its parent cell has level weight $m_{j}/2=m(L)/2$ and contains $a_{L}\text{,}$ so <a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i4" title="Item 4 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>) and Lemma 2.2(1) give</p>
<table id="S2.E1a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|q_{L}\|_{2}^{2}\ =\ d_{T}\bigl(h(L),a_{L}\bigr)\ \leq\ \Bigl\lfloor\frac{2\bar{\alpha}}{m(L)}\Bigr\rfloor\ \leq\ \frac{2\bar{\alpha}}{m(L)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.2.1)</span></td></tr></tbody>
</table>
<p id="S2a.p24.2" class="ltx_p">With $b_{h}:=\sum_{L:\,h(L)=h}\lambda_{L}$ this splits the collapsed signal as $g=g_{0}+\sum_{L}\lambda_{L}q_{L}\text{,}$ where $g_{0}:=\sum_{h\in U}b_{h}p_{h}$ is the <em id="S2a.p24.2.1" class="ltx_emph ltx_font_italic">skeleton</em> and the nonzero $q_{L}$ are the <em id="S2a.p24.2.2" class="ltx_emph ltx_font_italic">light exits</em>.</p>
</div>
<div id="S2a.p25" class="ltx_para">
<p id="S2a.p25.1" class="ltx_p">The skeleton is rounded through one scalar. List $U$ as $h_{1},\dots,h_{s}$ in a fixed depth-first preorder of $T\text{,}$ write $b_{i}:=b_{h_{i}}$ for the masses in that order, set $B_{i}:=\sum_{\ell\leq i}b_{\ell}$ with $B_{0}:=0\text{,}$ and put $Q_{i}:=\lfloor kB_{i}\rfloor-\lfloor kB_{i-1}\rfloor\in\mathbb{Z}_{\geq 0}\text{.}$ Let $Q$ be the integer vector with $Q_{h_{i}}:=Q_{i}$ and $Q_{v}:=0$ for $v\notin U\text{,}$ and set $\bar{g}_{0}:=\frac{1}{k}\sum_{h\in U}Q_{h}p_{h}\text{.}$ Over an interval of the list the $Q_{i}$ telescope, so their sum differs from $k$ times the corresponding mass by a difference of two floor errors, hence by less than $1\text{.}$ The terminal cells partition $\mathsf{V}\text{,}$ so $B_{s}=\sum_{L}\lambda_{L}=1$ and the whole list gives $\sum_{i}Q_{i}=\lfloor kB_{s}\rfloor=k\text{;}$ as the $B_{i}$ increase, $Q$ is a nonnegative integer leak vector of total mass $k$ supported on $U\text{.}$ Every subtree $T_{v}$ is a contiguous block of a depth-first preorder, so $U\cap T_{v}$ is such an interval, and coordinates are subtree sums by Lemma 2.1; therefore $g_{0}$ and $\bar{g}_{0}$ differ by less than $1/k$ at every vertex simultaneously.</p>
</div>
<div id="S2a.p26" class="ltx_para">
<p id="S2a.p26.1" class="ltx_p">Finally, write $\mathcal{L}_{\mathrm{ex}}:=\{L\in\mathcal{L}:q_{L}\neq 0\}$ for the light exits, every member of which is a light cell and therefore has $\lambda_{L}\leq m(L)/k\text{.}$ They are quantized by the independent variables $Z_{L}=\frac{m(L)}{k}\xi_{L}\text{,}$ $L\in\mathcal{L}_{\mathrm{ex}}\text{,}$ with $\xi_{L}\sim\mathrm{Bernoulli}(k\lambda_{L}/m(L))\text{,}$ which is a legitimate parameter by that bound. With the selection weight $W:=\sum_{L\in\mathcal{L}_{\mathrm{ex}}}m(L)\mathbf{1}\{Z_{L}\neq 0\}\text{,}$ the integer vector is</p>
<table id="S2.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$z\ =\ Q+\sum_{L\in\mathcal{L}_{\mathrm{ex}}:\,Z_{L}\neq 0}m(L)\bigl(e_{a_{L}}-e_{h(L)}\bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p26.2" class="ltx_p">and the <em id="S2a.p26.2.1" class="ltx_emph ltx_font_italic">flow states</em> of an integer vector $z$ are the subtree sums $x_{v}:=\sum_{u\succeq v}z_{u}\text{,}$ that is, the coordinates of $\sum_{u}z_{u}p_{u}\text{.}$</p>
</div>
<div id="S2.Thmlemma4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma4.2" class="ltx_text ltx_font_bold">Lemma S.2.4</span></span><span id="S2.Thmlemma4.3" class="ltx_text ltx_font_bold"> (Collapse and exit estimates).</span></h6>
<div id="S2.Thmlemma4.p1" class="ltx_para">
<p id="S2.Thmlemma4.p1.1" class="ltx_p"><span id="S2.Thmlemma4.p1.1.1" class="ltx_text ltx_font_italic">In this setting:</span></p>
<ol id="S2.I7" class="ltx_enumerate">
<li id="S2.I7.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S2.I7.i1.p1" class="ltx_para">
<p id="S2.I7.i1.p1.1" class="ltx_p">$\|f-g\|_{2}^{2}\leq 3\bar{\alpha}/k$<span id="S2.I7.i1.p1.1.1" class="ltx_text ltx_font_italic">, the display
(3.4);</span></p>
</div></li>
<li id="S2.I7.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S2.I7.i2.p1" class="ltx_para">
<p id="S2.I7.i2.p1.1" class="ltx_p"><span id="S2.I7.i2.p1.1.1" class="ltx_text ltx_font_italic">writing </span>$\Sigma$<span id="S2.I7.i2.p1.1.2" class="ltx_text ltx_font_italic"> for the sum
</span>$\sum_{L\in\mathcal{L}_{\mathrm{ex}}}(Z_{L}-\lambda_{L})q_{L}$<span id="S2.I7.i2.p1.1.3" class="ltx_text ltx_font_italic">, one has
</span>$\mathbb{E}\|\Sigma\|_{2}^{2}\leq 2\bar{\alpha}/k$<span id="S2.I7.i2.p1.1.4" class="ltx_text ltx_font_italic"> and
</span>$\mathbb{E}W\leq k$<span id="S2.I7.i2.p1.1.5" class="ltx_text ltx_font_italic">, so with probability at least </span>$\tfrac{1}{4}$<span id="S2.I7.i2.p1.1.6" class="ltx_text ltx_font_italic"> both </span>$W\leq 2k$<span id="S2.I7.i2.p1.1.7" class="ltx_text ltx_font_italic">
and </span>$\|\Sigma\|_{2}^{2}\leq 8\bar{\alpha}/k$<span id="S2.I7.i2.p1.1.8" class="ltx_text ltx_font_italic"> hold;</span></p>
</div></li>
<li id="S2.I7.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S2.I7.i3.p1" class="ltx_para">
<p id="S2.I7.i3.p1.1" class="ltx_p"><span id="S2.I7.i3.p1.1.1" class="ltx_text ltx_font_italic">on such a realization </span>$z$<span id="S2.I7.i3.p1.1.2" class="ltx_text ltx_font_italic"> is supported on
</span>$A_{k}$<span id="S2.I7.i3.p1.1.3" class="ltx_text ltx_font_italic"> and satisfies </span>$\|z\|_{1}\leq 5k$<span id="S2.I7.i3.p1.1.4" class="ltx_text ltx_font_italic">, and its selected exit roots carry
total activation charge at most </span>$W$<span id="S2.I7.i3.p1.1.5" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S2a.p27" class="ltx_para">
<p id="S2a.p27.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S2a.p28" class="ltx_para">
<p id="S2a.p28.1" class="ltx_p"><em id="S2a.p28.1.1" class="ltx_emph ltx_font_italic">Part (1).</em> The blocks $e_{L}=\sum_{u\in L}\lambda_{u}(p_{u}-p_{a_{L}})$ have pairwise disjoint supports, as recorded in the main proof, so $\|f-g\|_{2}^{2}=\sum_{L\in\mathcal{L}}\|e_{L}\|_{2}^{2}\text{.}$ Every $u\in L$ has $d_{T}(a_{L},u)\leq\bar{\alpha}/m(L)$ by <a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i4" title="Item 4 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>), so the triangle inequality and Lemma 2.2(1) give $\|e_{L}\|_{2}\leq\sum_{u\in L}\lambda_{u}\sqrt{d_{T}(a_{L},u)}\leq\lambda_{L}\sqrt{\bar{\alpha}/m(L)}\text{.}$ A light terminal cell has $\lambda_{L}\leq m(L)/k\text{,}$ whence $\|e_{L}\|_{2}^{2}\leq\lambda_{L}^{2}\bar{\alpha}/m(L)\leq\lambda_{L}\bar{\alpha}/k\text{,}$ and summing over the light cells with $\sum_{L}\lambda_{L}\leq 1$ bounds their total contribution by $\bar{\alpha}/k\text{.}$ At most one terminal cell is heavy; it sits at level $J\text{,}$ where $m_{J}\geq k/2\text{,}$ and contributes $\|e_{L}\|_{2}^{2}\leq\lambda_{L}^{2}\bar{\alpha}/m_{J}\leq 2\bar{\alpha}/k\text{.}$ Adding the two bounds proves (1).</p>
</div>
<div id="S2a.p29" class="ltx_para">
<p id="S2a.p29.1" class="ltx_p"><em id="S2a.p29.1.1" class="ltx_emph ltx_font_italic">Part (2).</em> Each $Z_{L}$ has mean $\lambda_{L}$ and</p>
<table id="S2.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{Var}(Z_{L})\ \leq\ \Bigl(\frac{m(L)}{k}\Bigr)^{2}\frac{k\lambda_{L}}{m(L)}\ =\ \frac{\lambda_{L}m(L)}{k},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p29.2" class="ltx_p">while $\|q_{L}\|_{2}^{2}\leq 2\bar{\alpha}/m(L)$ by <a href="#S2.E1a" title="In S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.2.1</span></a>. The $Z_{L}$ are independent, so the cross terms vanish in expectation. With every sum below running over $L\in\mathcal{L}_{\mathrm{ex}}\text{,}$</p>
<table id="S2.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\Bigl\|\sum_{L}(Z_{L}-\lambda_{L})q_{L}\Bigr\|_{2}^{2}\ =\ \sum_{L}\operatorname{Var}(Z_{L})\,\|q_{L}\|_{2}^{2}\ \leq\ \frac{2\bar{\alpha}}{k}\sum_{L}\lambda_{L}\ \leq\ \frac{2\bar{\alpha}}{k}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p29.3" class="ltx_p">Also $\mathbb{E}W=\sum_{L}m(L)\,k\lambda_{L}/m(L)=k\sum_{L}\lambda_{L}\leq k\text{.}$ By Markov’s inequality $\mathbb{P}(W&gt;2k)\leq\tfrac{1}{2}\text{,}$ and the squared norm exceeds $8\bar{\alpha}/k$ with probability at most $\tfrac{1}{4}\text{,}$ so both bounds hold with probability at least $\tfrac{1}{4}\text{.}$</p>
</div>
<div id="S2a.p30" class="ltx_para">
<p id="S2a.p30.1" class="ltx_p"><em id="S2a.p30.1.1" class="ltx_emph ltx_font_italic">Part (3).</em> The skeleton $Q$ is supported on $U\subseteq A_{k}$ and each selected transfer on $\{a_{L},h(L)\}\text{;}$ the root of a level-$j$ cell lies in $R_{j}\subseteq A_{k}\text{,}$ so $\operatorname{supp}(z)\subseteq A_{k}\text{.}$ Since $Q$ is nonnegative with total mass $k$ and each selected transfer adds $2m(L)$ to the $\ell_{1}$ norm, $\|z\|_{1}\leq k+2W\leq 5k\text{.}$ The selected exit roots are distinct, being roots of distinct terminal cells, and $\widetilde{\omega}(a_{L})\leq\omega(a_{L})\leq m(L)$ because $a_{L}\in R_{j}$ with $m_{j}=m(L)\text{;}$ their charges therefore total at most $\sum_{L:\,Z_{L}\neq 0}m(L)=W\text{.}$
∎</p>
</div>
<div id="S2a.p31" class="ltx_para">
<p id="S2a.p31.1" class="ltx_p">Two explicit constants follow. The subtree $S$ has at most $5\bar{\alpha}k+1\leq 6\bar{\alpha}k$ vertices, by <a href="#S2.Thmlemma3a" title="Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.3</span></a>(<a href="#S2.I5.i2" title="Item 2 ‣ Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) and $\bar{\alpha}\geq 2\text{;}$ since $g_{0}$ and $\bar{g}_{0}$ differ by less than $1/k$ at every vertex and vanish outside $S\text{,}$ $\|g_{0}-\bar{g}_{0}\|_{2}^{2}&lt;6\bar{\alpha}k/k^{2}=6\bar{\alpha}/k\text{:}$ the display (3.5) holds with $C=6\text{.}$ Together with the collapse and exit bounds of <a href="#S2.Thmlemma4" title="Lemma S.2.4 (Collapse and exit estimates). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.4</span></a>, the error assembly of the main proof reads</p>
<table id="S2.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Bigl\|f-\frac{1}{k}\sum_{v}z_{v}p_{v}\Bigr\|_{2}^{2}\ \leq\ 3\Bigl(\frac{3\bar{\alpha}}{k}+\frac{6\bar{\alpha}}{k}+\frac{8\bar{\alpha}}{k}\Bigr)\ =\ \frac{51\,\bar{\alpha}}{k}\ =\ 51\,\overline{\delta}_{k}(T)\ \leq\ 102\,\delta_{k}(T),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2a.p31.2" class="ltx_p">the last step by Lemma 2.3, so part (1) of Proposition 3.1 holds with $C_{0}=102\text{.}$</p>
</div>
<div id="S2a.p32" class="ltx_para">
<p id="S2a.p32.1" class="ltx_p">It remains to prove the counting bound.</p>
</div>
<div id="S2.Thmlemma5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma5.2" class="ltx_text ltx_font_bold">Lemma S.2.5</span></span><span id="S2.Thmlemma5.3" class="ltx_text ltx_font_bold"> (Counting bound).</span></h6>
<div id="S2.Thmlemma5.p1" class="ltx_para">
<p id="S2.Thmlemma5.p1.1" class="ltx_p"><span id="S2.Thmlemma5.p1.1.1" class="ltx_text ltx_font_italic">The integer vectors $z$ supported on $A_{k}$ with $\sum_{v}z_{v}=k\text{,}$ $\Gamma(z)\leq 9k\text{,}$ and all flow states in $[0,3k]$ number at most $e^{45k}\text{.}$ In particular part (2) of Proposition 3.1 holds with $C_{1}=45\text{.}$</span></p>
</div>
</div>
<div id="S2a.p33" class="ltx_para">
<p id="S2a.p33.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S2a.p34" class="ltx_para">
<p id="S2a.p34.1" class="ltx_p">We bound the larger class defined by the support and code-length constraints alone. Each member $z$ determines its support, split into the free part $\operatorname{supp}(z)\cap R_{0}$ and the charged part $\operatorname{supp}(z)\setminus R_{0}\text{,}$ and its coefficient vector; we count the three in turn and multiply.</p>
</div>
<div id="S2a.p35" class="ltx_para">
<p id="S2a.p35.1" class="ltx_p"><em id="S2a.p35.1.1" class="ltx_emph ltx_font_italic">Free parts.</em> Any subset of $R_{0}$ can occur, and $|R_{0}|\leq ke^{m_{0}}=ek$ by <a href="#S2.Thmlemma1a" title="Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.1</span></a>(<a href="#S2.I1.i2a" title="Item 2 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>), so the free parts number at most $2^{ek}\leq e^{ek}\text{.}$</p>
</div>
<div id="S2a.p36" class="ltx_para">
<p id="S2a.p36.1" class="ltx_p"><em id="S2a.p36.1.1" class="ltx_emph ltx_font_italic">Charged parts.</em> Group the charged vertices by first appearance: $G_{j}:=\{v\in A_{k}\setminus R_{0}:\ \omega(v)=m_{j}\}$ satisfies $G_{j}\subseteq R_{j}\text{,}$ hence $|G_{j}|\leq 2ke^{m_{j}}$ by <a href="#S2.Thmlemma1a" title="Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.1</span></a>(<a href="#S2.I1.i3a" title="Item 3 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), for $1\leq j\leq J\text{.}$ The groups partition $A_{k}\setminus R_{0}\text{,}$ so a charged part is the disjoint union of its intersections with them, and one with $q_{j}$ elements of $G_{j}$ carries activation charge $\sum_{j}m_{j}q_{j}\leq\Gamma(z)\leq 9k\text{.}$ Inserting the factor $e^{2(9k-\sum_{j}m_{j}q_{j})}\geq 1$ and then dropping the charge constraint,</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S2.EGx2"></span><span class="paper-eq-anchor" id="S2.Ex14"></span><span class="paper-eq-anchor" id="S2.Ex15"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\#\{\text{charged parts}\}\ \leq\ e^{18k}\prod_{j=1}^{J}\ \sum_{q\geq 0}\binom{|G_{j}|}{q}\,e^{-2m_{j}q}\space &amp; \displaystyle=\ e^{18k}\prod_{j=1}^{J}\bigl(1+e^{-2m_{j}}\bigr)^{|G_{j}|} \\
 &amp; \displaystyle\leq\ e^{18k}\exp\Bigl(2k\sum_{j\geq 1}e^{-m_{j}}\Bigr)\ \leq\ e^{19k},
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S2a.p36.2" class="ltx_p">using $\log(1+x)\leq x\text{,}$ $|G_{j}|e^{-2m_{j}}\leq 2ke^{-m_{j}}\text{,}$ and $\sum_{j\geq 1}e^{-2^{j}}&lt;\tfrac{1}{6}\text{.}$</p>
</div>
<div id="S2a.p37" class="ltx_para">
<p id="S2a.p37.1" class="ltx_p"><em id="S2a.p37.1.1" class="ltx_emph ltx_font_italic">Coefficients.</em> Every charged support vertex carries charge at least $1\text{,}$ so a support has at most $ek+9k\leq 12k$ vertices. On a fixed support of size $d\text{,}$ the map $z\mapsto(z^{+},z^{-})$ is injective into the nonnegative integer vectors on $2d$ coordinates with total at most $9k\text{,}$ since $\|z\|_{1}\leq\Gamma(z)\leq 9k\text{;}$ these number $\binom{9k+2d}{2d}\leq 2^{9k+2d}\leq 2^{33k}\leq e^{23k}\text{.}$</p>
</div>
<div id="S2a.p38" class="ltx_para">
<p id="S2a.p38.1" class="ltx_p">Multiplying the three counts bounds the class by $e^{(e+19+23)k}\leq e^{45k}\text{.}$
∎</p>
</div>
<div id="S2a.p39" class="ltx_para">
<p id="S2a.p39.1" class="ltx_p">The facts quoted in the main proof are now all in place, and Proposition 3.1 is proved.</p>
</div>
</section>
<section id="S3a" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-packing-lower-bound-1"><span class="ltx_tag ltx_tag_section">S.3 </span>The Packing Lower Bound</h2>

<div id="S3a.p1" class="ltx_para">
<p id="S3a.p1.1" class="ltx_p">This section completes the lower-bound half of Section 3.2. Lemmas 3.2 and 3.3, whose proofs were sketched there, are proved in full first, with the constants of the latter fixed. Two self-contained lemmas follow: the additivity of Bayes risks across coordinate-disjoint blocks, and the edge-disjoint grouping of a separated vertex set. The section then completes the proofs of Propositions 3.4 and 3.5, and finally the deferred cases of Theorem 1 and Proposition 1.</p>
</div>
<div id="S3a.p2" class="ltx_para">
<p id="S3a.p2.1" class="ltx_p"><em class="ltx_title_proof">Proof of Lemma 3.2.</em></p>
</div>
<div id="S3a.p3" class="ltx_para">
<p id="S3a.p3.1" class="ltx_p">Write $\mathcal{P}:=\{p_{u}:u\in\mathsf{V}\}$ and $\varepsilon:=\sqrt{r}/3\text{,}$ and fix a maximal $\varepsilon$-separated subset of $\mathcal{P}\text{;}$ by maximality, every point of $\mathcal{P}$ lies within Euclidean distance $\varepsilon$ of the subset. By Lemma 2.2(1), the vertices indexing the subset have pairwise tree distances at least $\varepsilon^{2}=r/9\text{,}$ so it suffices to bound their number below by $N^{\uparrow}_{T}(r)\text{.}$</p>
</div>
<div id="S3a.p4" class="ltx_para">
<p id="S3a.p4.1" class="ltx_p">Consider the ball of radius $\varepsilon$ around one point of the subset, let $C$ be the set of vertices whose indicators it contains, and let $a$ be the deepest common ancestor of $C\text{.}$ Fix $u\in C$ with $u\neq a$ and let $c$ be the child of $a$ on the path toward $u\text{.}$ Not all of $C$ lies in the subtree $T_{c}\text{,}$ since $c$ would then be a common ancestor of $C$ deeper than $a\text{;}$ fix $v\in C\setminus T_{c}\text{.}$ The meet $u\wedge v$ is at least as deep as $a\text{,}$ the latter being a common ancestor of $u$ and $v\text{;}$ and it is not deeper, since an ancestor of $u$ strictly below $a$ lies in $T_{c}\text{,}$ and $u\wedge v\in T_{c}$ would force $v\in T_{c}\text{.}$ Hence $u\wedge v=a\text{,}$ so the path from $u$ to $v$ passes through $a\text{,}$ and by Lemma 2.2(1),</p>
<table id="S3.Ex1a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{T}(a,u)\ \leq\ d_{T}(u,v)\ =\ \|p_{u}-p_{v}\|_{2}^{2}\ \leq\ (2\varepsilon)^{2}\ =\ \tfrac{4}{9}\,r\ &lt;\ r,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p4.2" class="ltx_p">the indicators $p_{u}$ and $p_{v}$ lying in one ball of radius $\varepsilon\text{.}$ The bound holds trivially at $u=a\text{,}$ so $a$ ancestor-covers every vertex of $C$ within distance $r\text{.}$ Every vertex of $T$ lies in the captured set of some ball, so collecting one such ancestor per ball yields an ancestor $r$-net, of size at most the number of balls; the number of balls is the size of the separated subset, and every ancestor $r$-net has at least $N^{\uparrow}_{T}(r)$ elements, which proves the bound.
∎</p>
</div>
<div id="S3a.p5" class="ltx_para">
<p id="S3a.p5.1" class="ltx_p">Two facts about Gaussian shifts are used without further comment <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib36" title="" class="ltx_ref">Tsybakov, 2009</a>)</cite>. The Kullback–Leibler divergence between $N(\theta,\sigma^{2}I_{N})$ and $N(\theta^{\prime},\sigma^{2}I_{N})$ is $\|\theta-\theta^{\prime}\|_{2}^{2}/(2\sigma^{2})\text{.}$ Fano’s inequality in its pairwise form states that if a label is uniform on $M\geq 2$ hypotheses whose data laws satisfy $\max_{i,j}\operatorname{KL}(P_{i},P_{j})\leq\kappa\text{,}$ then every decoder based on the data errs with probability at least $1-(\kappa+\log 2)/\log M\text{.}$</p>
</div>
<div id="S3a.p6" class="ltx_para">
<p id="S3a.p6.1" class="ltx_p"><em class="ltx_title_proof">Proof of Lemma 3.3.</em></p>
</div>
<div id="S3a.p7" class="ltx_para">
<p id="S3a.p7.1" class="ltx_p">Fix $\eta:=\tfrac{1}{10}\text{,}$ the constant of the main-text sketch, and shrink each block into its information budget:</p>
<table id="S3.Ex2a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau_{j}^{2}\ :=\ \min\Bigl\{1,\ \frac{\eta\,\sigma^{2}h_{j}}{D_{j}^{2}}\Bigr\},\qquad\widetilde{\mu}_{\mathbf{a}}\ :=\ \mu_{0}+\sum_{j}\tau_{j}g_{j}(a_{j}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p7.2" class="ltx_p">so that $\tau_{j}\in[0,1]$ and, by hypothesis (1), the shrunken family lies in $K\text{.}$ Place the uniform product prior on $\mathbf{a}\text{.}$ Since the family lies in $K\text{,}$ the minimax risk over $K$ dominates the Bayes risk of this prior, and it suffices to bound the latter for an arbitrary estimator $\widehat{\mu}=\widehat{\mu}(Y)\text{.}$</p>
</div>
<div id="S3a.p8" class="ltx_para">
<p id="S3a.p8.1" class="ltx_p"><em id="S3a.p8.1.1" class="ltx_emph ltx_font_italic">Separation.</em> Let $\widehat{\mathbf{a}}$ index a member of the shrunken family nearest to $\widehat{\mu}\text{,}$ ties broken by a fixed order, so that $\|\widehat{\mu}-\widetilde{\mu}_{\mathbf{a}}\|_{2}\geq\tfrac{1}{2}\|\widetilde{\mu}_{\widehat{\mathbf{a}}}-\widetilde{\mu}_{\mathbf{a}}\|_{2}$ by the triangle inequality, and write $\Delta_{j}:=g_{j}(\widehat{a}_{j})-g_{j}(a_{j})\text{,}$ blocks with $\Delta_{j}=0$ dropped. With $\rho_{ij}:=|\langle\Delta_{i},\Delta_{j}\rangle|/(\|\Delta_{i}\|_{2}\|\Delta_{j}\|_{2})\text{,}$ hypothesis (3) gives $\sum_{j\neq i}\rho_{ij}\leq\gamma$ for every $i\text{,}$ and</p>
<table id="S3.Ex3a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Bigl\|\sum_{j}\tau_{j}\Delta_{j}\Bigr\|_{2}^{2}\ \geq\ \sum_{j}\tau_{j}^{2}\|\Delta_{j}\|_{2}^{2}-\sum_{i\neq j}\rho_{ij}\,\tau_{i}\|\Delta_{i}\|_{2}\,\tau_{j}\|\Delta_{j}\|_{2}\ \geq\ (1-\gamma)\sum_{j}\tau_{j}^{2}\|\Delta_{j}\|_{2}^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p8.2" class="ltx_p">the last step by $xy\leq\tfrac{1}{2}(x^{2}+y^{2})$ and the row sums. Since $\|\Delta_{j}\|_{2}\geq d_{j}$ whenever $\widehat{a}_{j}\neq a_{j}\text{,}$ pathwise</p>
<table id="S3.Ex4a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|\widehat{\mu}-\widetilde{\mu}_{\mathbf{a}}\|_{2}^{2}\ \geq\ \frac{1-\gamma}{4}\sum_{j}\tau_{j}^{2}d_{j}^{2}\,\mathbf{1}\{\widehat{a}_{j}\neq a_{j}\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S3a.p9" class="ltx_para">
<p id="S3a.p9.1" class="ltx_p"><em id="S3a.p9.1.1" class="ltx_emph ltx_font_italic">Per-block error.</em> Fix $j$ and condition on the other labels $\mathbf{a}_{-j}\text{.}$ Under the product prior, $a_{j}$ remains uniform on $\mathcal{A}_{j}\text{,}$ and subtracting the known vector $\mu_{0}+\sum_{i\neq j}\tau_{i}g_{i}(a_{i})$ from $Y$ reduces the conditional problem to testing the finite Gaussian family $\{\tau_{j}g_{j}(a):a\in\mathcal{A}_{j}\}\text{,}$ whose pairwise Kullback–Leibler divergences are at most $\tau_{j}^{2}D_{j}^{2}/(2\sigma^{2})\leq\eta h_{j}/2\text{.}$ If $|\mathcal{A}_{j}|\geq 3\text{,}$ Fano’s inequality gives every decoder error probability at least $1-\eta/2-\log 2/\log|\mathcal{A}_{j}|\geq 1-\tfrac{1}{20}-\log 2/\log 3&gt;\tfrac{1}{4}\text{.}$ If $|\mathcal{A}_{j}|=2\text{,}$ then $D_{j}=d_{j}$ and the two means are at distance $\tau_{j}D_{j}\leq\sigma\sqrt{\eta\log 2}\text{;}$ the likelihood-ratio test is optimal and projects the data onto the difference of the means; its two conditional errors are equal, and the Bayes error is</p>
<table id="S3.Ex5a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Phi_{\mathcal{N}}\Bigl(-\frac{\tau_{j}D_{j}}{2\sigma}\Bigr)\ \geq\ \frac{1}{2}-\frac{\sqrt{\eta\log 2}}{2\sqrt{2\pi}}\ &gt;\ \frac{1}{4},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p9.2" class="ltx_p">where $\Phi_{\mathcal{N}}$ is the standard normal distribution function, whose density is at most $1/\sqrt{2\pi}\text{.}$ In either case, every decoder of $a_{j}$ that is measurable in $Y$ is, conditionally on $\mathbf{a}_{-j}\text{,}$ a decoder of the reduced problem, so $\mathbb{P}(\widehat{a}_{j}\neq a_{j})\geq\tfrac{1}{4}\text{.}$</p>
</div>
<div id="S3a.p10" class="ltx_para">
<p id="S3a.p10.1" class="ltx_p"><em id="S3a.p10.1.1" class="ltx_emph ltx_font_italic">Assembly.</em> Taking expectations in the separation bound,</p>
<table id="S3.Ex6a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\|\widehat{\mu}-\widetilde{\mu}_{\mathbf{a}}\|_{2}^{2}\ \geq\ \frac{1-\gamma}{4}\sum_{j}\tau_{j}^{2}d_{j}^{2}\,\mathbb{P}(\widehat{a}_{j}\neq a_{j})\ \geq\ \frac{1-\gamma}{16}\sum_{j}\tau_{j}^{2}d_{j}^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p10.2" class="ltx_p">and by the definition of $\tau_{j}$ and hypothesis (2),</p>
<table id="S3.Ex7a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau_{j}^{2}d_{j}^{2}\ =\ \min\Bigl\{d_{j}^{2},\ \eta\,\sigma^{2}h_{j}\,\frac{d_{j}^{2}}{D_{j}^{2}}\Bigr\}\ \geq\ \min\Bigl\{d_{j}^{2},\ \frac{\eta}{A}\,\sigma^{2}h_{j}\Bigr\}\ \geq\ \frac{\eta}{A}\,\min\bigl\{d_{j}^{2},\ \sigma^{2}h_{j}\bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p10.3" class="ltx_p">so the Bayes risk of the prior is at least $c_{A}(1-\gamma)\sum_{j}\min\{d_{j}^{2},\sigma^{2}h_{j}\}$ with $c_{A}:=\eta/(16A)=1/(160A)\text{.}$</p>
</div>
<div id="S3a.p11" class="ltx_para">
<p id="S3a.p11.1" class="ltx_p"><em id="S3a.p11.1.1" class="ltx_emph ltx_font_italic">The restricted loss.</em> When every contrast is supported in the coordinate set $S\text{,}$ choose $\widehat{\mathbf{a}}$ nearest to $\widehat{\mu}$ in the norm restricted to $S\text{.}$ The differences $(\widetilde{\mu}_{\widehat{\mathbf{a}}}-\widetilde{\mu}_{\mathbf{a}})|_{S}=\sum_{j}\tau_{j}\Delta_{j}$ are unchanged, since the contrasts live in $S\text{,}$ so the separation bound holds for $\|(\widehat{\mu}-\widetilde{\mu}_{\mathbf{a}})|_{S}\|_{2}^{2}\text{;}$ and the per-block bound applies to any decoder measurable in the full data $Y\text{,}$ in particular to this one. The assembly is identical.
∎</p>
</div>
<div id="S3a.p12" class="ltx_para">
<p id="S3a.p12.1" class="ltx_p">The assembly across groups in Proposition 3.4 rests on the fact that coordinate-disjoint blocks contribute additively to the Bayes risk.</p>
</div>
<div id="S3.Thmlemma1a" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma1a.2" class="ltx_text ltx_font_bold">Lemma S.3.1</span></span><span id="S3.Thmlemma1a.3" class="ltx_text ltx_font_bold"> (Bayes risks add across disjoint blocks).</span></h6>
<div id="S3.Thmlemma1a.p1" class="ltx_para">
<p id="S3.Thmlemma1a.p1.1" class="ltx_p"><span id="S3.Thmlemma1a.p1.1.1" class="ltx_text ltx_font_italic">Let</span></p>
<table id="S3.Ex8a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mu_{\boldsymbol{\theta}}\ =\ \mu_{0}+\sum_{i=1}^{m}h_{i}(\theta_{i}),\qquad\boldsymbol{\theta}=(\theta_{1},\dots,\theta_{m}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.Thmlemma1a.p1.2" class="ltx_p"><span id="S3.Thmlemma1a.p1.2.1" class="ltx_text ltx_font_italic">where the $\theta_{i}$ are independent under a product prior and, for each $i\text{,}$ every contrast $h_{i}(\theta_{i})-h_{i}(\theta_{i}^{\prime})$ is supported in a coordinate set $S_{i}\text{,}$ the sets $S_{1},\dots,S_{m}$ pairwise disjoint. In the model $Y=\mu_{\boldsymbol{\theta}}+\sigma Z\text{,}$ $Z\sim N(0,I_{N})\text{,}$ the Bayes risk of estimating $\mu_{\boldsymbol{\theta}}$ in squared loss is at least the sum over $i$ of the Bayes risks of the isolated problems: observe $Y_{S_{i}}\text{,}$ which up to a fixed additive vector is $h_{i}(\theta_{i})|_{S_{i}}+\sigma Z_{S_{i}}\text{,}$ and estimate $\mu_{\boldsymbol{\theta}}|_{S_{i}}$ under the $i$-th marginal prior.</span></p>
</div>
</div>
<div id="S3a.p13" class="ltx_para">
<p id="S3a.p13.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S3a.p14" class="ltx_para">
<p id="S3a.p14.1" class="ltx_p">The squared loss dominates the sum of its restrictions to the disjoint sets: $\|\widehat{\mu}-\mu_{\boldsymbol{\theta}}\|_{2}^{2}\geq\sum_{i}\|(\widehat{\mu}-\mu_{\boldsymbol{\theta}})|_{S_{i}}\|_{2}^{2}\text{.}$ Fix $i\text{.}$ For $\ell\neq i$ the restriction $h_{\ell}(\theta_{\ell})|_{S_{i}}$ does not depend on $\theta_{\ell}\text{:}$ two values of $\theta_{\ell}$ differ on $S_{i}$ by a contrast of block $\ell$ restricted to $S_{i}\text{,}$ which vanishes because those contrasts are supported in $S_{\ell}\text{,}$ disjoint from $S_{i}\text{.}$ Hence $\mu_{\boldsymbol{\theta}}|_{S_{i}}=c_{i}+h_{i}(\theta_{i})|_{S_{i}}$ for a fixed vector $c_{i}\text{,}$ and $Y_{S_{i}}$ is distributed as in the isolated problem. Moreover $Y_{S_{i}^{c}}$ is a function of $(\boldsymbol{\theta}_{-i},Z_{S_{i}^{c}})\text{,}$ which is independent of $(\theta_{i},Z_{S_{i}})$ under the product prior, so $Y_{S_{i}^{c}}$ is independent of the pair $(\theta_{i},Y_{S_{i}})$ and the conditional law of $\mu_{\boldsymbol{\theta}}|_{S_{i}}$ given $Y$ equals its conditional law given $Y_{S_{i}}\text{.}$ The Bayes-optimal estimate of $\mu_{\boldsymbol{\theta}}|_{S_{i}}\text{,}$ its posterior mean, is therefore a function of $Y_{S_{i}}$ alone, and $\mathbb{E}\|(\widehat{\mu}-\mu_{\boldsymbol{\theta}})|_{S_{i}}\|_{2}^{2}$ is at least the isolated Bayes risk for every estimator $\widehat{\mu}\text{.}$ Summing over $i$ completes the proof.
∎</p>
</div>
<div id="S3a.p15" class="ltx_para">
<p id="S3a.p15.1" class="ltx_p">The next lemma produces the edge-disjoint groups of the main-text sketch, with explicit comparison constants.</p>
</div>
<div id="S3.Thmlemma2a" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma2a.2" class="ltx_text ltx_font_bold">Lemma S.3.2</span></span><span id="S3.Thmlemma2a.3" class="ltx_text ltx_font_bold"> (Edge-disjoint grouping).</span></h6>
<div id="S3.Thmlemma2a.p1" class="ltx_para">
<p id="S3.Thmlemma2a.p1.1" class="ltx_p"><span id="S3.Thmlemma2a.p1.1.1" class="ltx_text ltx_font_italic">Let $U\subseteq\mathsf{V}$ consist of $M\geq 2$ vertices and let $q$ be an integer with $1\leq q\leq M/2\text{.}$ There are connected subtrees $\mathcal{C}_{1},\dots,\mathcal{C}_{q^{\prime}}$ of $T$ with pairwise disjoint edge sets, and pairwise disjoint sets $U_{i}\subseteq U\cap\mathcal{C}_{i}\text{,}$ such that</span></p>
<table id="S3.Ex9a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{q}{4}\ \leq\ q^{\prime}\ \leq\ 6q,\qquad\frac{M}{6q}\ \leq\ |U_{i}|\ \leq\ \frac{M}{q}\quad\text{and}\quad|U_{i}|\ \geq\ 2\qquad\text{for every }i.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S3a.p16" class="ltx_para">
<p id="S3a.p16.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S3a.p17" class="ltx_para">
<p id="S3a.p17.1" class="ltx_p">Call the members of $U$ <em id="S3a.p17.1.1" class="ltx_emph ltx_font_italic">marks</em>. Work in the minimal subtree of $T$ spanning $U\text{,}$ rooted by the orientation inherited from $T\text{,}$ and set $L:=\max\{2,\lfloor M/(4q)\rfloor\}\text{.}$</p>
</div>
<div id="S3a.p18" class="ltx_para">
<p id="S3a.p18.1" class="ltx_p"><em id="S3a.p18.1.1" class="ltx_emph ltx_font_italic">The procedure.</em> Process the vertices in postorder, distinguishing each mark’s <em id="S3a.p18.1.2" class="ltx_emph ltx_font_italic">token</em>, which will be assigned to at most one group, from the vertices and edges that only provide connectivity. Each vertex $v$ receives a collection of <em id="S3a.p18.1.3" class="ltx_emph ltx_font_italic">items</em>, each a connected subgraph containing $v$ together with the unassigned tokens it carries: for every child $c$ of $v\text{,}$ the residual passed up from $c\text{,}$ extended by the edge $(v,c)\text{;}$ and, if $v$ is a mark, the one-point item $\{v\}$ carrying the token of $v\text{.}$ Insert the items into an open bin one at a time; whenever the bin first carries at least $L$ tokens, seal it: its subgraphs unite into a component, connected through $v\text{,}$ and its tokens, now permanently assigned, form the component’s mark set. After the last item, pass the union of the open bin and the bare vertex $\{v\}\text{,}$ carrying the bin’s tokens, upward as the residual of $v\text{.}$ At the root, discard the final residual.</p>
</div>
<div id="S3a.p19" class="ltx_para">
<p id="S3a.p19.1" class="ltx_p"><em id="S3a.p19.1.1" class="ltx_emph ltx_font_italic">The invariant.</em> Sealed components and residuals are connected, being unions of items that share the vertex at which they formed. A residual carries fewer than $L$ tokens, its bin having never reached $L\text{;}$ consequently every item carries fewer than $L$ tokens, the one-point items because $L\geq 2\text{,}$ and a component seals with at least $L$ but fewer than $2L$ tokens. Each token is assigned at most once, so the mark sets $U_{i}$ are pairwise disjoint; and a token’s vertex belongs to every subgraph that carries it, so $U_{i}\subseteq U\cap\mathcal{C}_{i}\text{.}$ Finally, each edge of the spanning subtree enters the process in exactly one item and thereafter stays inside whichever bin, component, or residual that item joined; the components are therefore pairwise edge-disjoint.</p>
</div>
<div id="S3a.p20" class="ltx_para">
<p id="S3a.p20.1" class="ltx_p"><em id="S3a.p20.1.1" class="ltx_emph ltx_font_italic">Counting.</em> Let $q^{\prime}$ be the number of sealed components; by the invariant, $|U_{i}|\in[L,2L)$ for each. Every token is either assigned at some sealing or sits in the final, discarded residual, which carries fewer than $L\text{;}$ hence</p>
<table id="S3.Ex10a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$q^{\prime}L\ \leq\ M\ &lt;\ 2Lq^{\prime}+L.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p20.2" class="ltx_p">If $M\geq 12q\text{,}$ then $L=\lfloor M/(4q)\rfloor\geq 3$ and $M/(6q)\leq L\leq M/(4q)\text{,}$ since $\lfloor x\rfloor\geq x-1\geq\tfrac{2}{3}x$ for $x\geq 3\text{;}$ hence $q^{\prime}\leq M/L\leq 6q$ and $q^{\prime}&gt;M/(2L)-\tfrac{1}{2}\geq 2q-\tfrac{1}{2}\text{,}$ so $q^{\prime}\geq 2q\geq q\text{,}$ while $|U_{i}|\in[L,2L)\subseteq[M/(6q),\,M/(2q)]\text{.}$ If $M&lt;12q\text{,}$ then $L=2\text{:}$ every item then carries at most one token, so components seal with exactly two, and $|U_{i}|=2$ lies in $[M/(6q),M/q]$ because $2q\leq M&lt;12q\text{.}$ For $M\geq 4$ the count gives $q^{\prime}\leq M/2\leq 6q$ and $q^{\prime}&gt;(M-2)/4\geq M/8\geq q/4\text{;}$ for $M\in\{2,3\}\text{,}$ necessarily $q=1\text{,}$ and the procedure seals exactly one component: fewer than $4$ tokens admit at most one, and at least one seals because all unassigned tokens funnel into the bins at the root.
∎</p>
</div>
<div id="S3a.p21" class="ltx_para">
<p id="S3a.p21.1" class="ltx_p"><em class="ltx_title_proof">Completion of the proof of Proposition 3.4.</em></p>
</div>
<div id="S3a.p22" class="ltx_para">
<p id="S3a.p22.1" class="ltx_p"><a href="#S3.Thmlemma2a" title="Lemma S.3.2 (Edge-disjoint grouping). ‣ S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.3.2</span></a>, applied with the parameter $q$ of the proposition, supplies the groups of the main-text sketch, with $q/4\leq q^{\prime}\leq 6q$ and $M/(6q)\leq M_{i}\leq M/q\text{;}$ every group receives the budget $a=V/q^{\prime}\text{.}$ Fix a group, with marked set $U_{i}$ of size $M_{i}\geq 2\text{,}$ and adopt the objects of the sketch: the radii $r_{\ell}=16^{\ell}r\text{,}$ the nested maximal separated subsets $N_{\ell}\text{,}$ the descent chain with its node weights and child counts $m_{\ell}\text{,}$ the retained levels $I\text{,}$ the alphabets $\mathcal{A}_{\ell}\text{,}$ and the masses $a_{\ell}$ with their normalizer $S\text{.}$ We verify the claims quoted there and assemble.</p>
</div>
<div id="S3a.p23" class="ltx_para">
<p id="S3a.p23.1" class="ltx_p"><em id="S3a.p23.1.1" class="ltx_emph ltx_font_italic">The hierarchy and its entropy.</em> Maximality of $N_{\ell}$ inside $N_{\ell-1}$ means that every point of $N_{\ell-1}$ lies within $r_{\ell}$ of a point of $N_{\ell}\text{,}$ so parents can be assigned, each point of $N_{\ell}$ to itself; and once $r_{\ell}$ exceeds the diameter of $U_{i}$ an $r_{\ell}$-separated subset is a single point: the hierarchy has a top. The weight of a node is at most its number of children times the largest weight of a child, so descending along children of maximal weight from the top, whose weight is $M_{i}\text{,}$ to a leaf, whose weight is one, gives $M_{i}\leq\prod_{\ell}m_{\ell}\text{,}$ that is, $\sum_{\ell}\log m_{\ell}\geq\log M_{i}\text{.}$ Levels with $m_{\ell}=1$ contribute zero to this sum, and among the four residue classes modulo four of the remaining levels one carries at least a quarter of it; the retained class $I$ therefore has $H=\sum_{\ell\in I}h_{\ell}\geq\tfrac{1}{4}\log M_{i}\text{.}$</p>
</div>
<div id="S3a.p24" class="ltx_para">
<p id="S3a.p24.1" class="ltx_p"><em id="S3a.p24.1.1" class="ltx_emph ltx_font_italic">Separations and aspect.</em> Distinct children $u\neq v$ of the chain node at level $\ell$ lie in $N_{\ell-1}\text{,}$ so $d_{T}(u,v)\geq r_{\ell-1}\text{;}$ both lie within $r_{\ell}$ of their parent, so $d_{T}(u,v)\leq 2r_{\ell}=32\,r_{\ell-1}\text{.}$ By Lemma 2.2(1), the contrasts $\Delta=a_{\ell}(p_{u}-p_{v})$ then satisfy $a_{\ell}^{2}r_{\ell-1}\leq\|\Delta\|_{2}^{2}\leq 32\,a_{\ell}^{2}r_{\ell-1}\text{,}$ so $d_{\ell}^{2}\geq a_{\ell}^{2}r_{\ell-1}$ and $D_{\ell}^{2}\leq 32\,a_{\ell}^{2}r_{\ell-1}\leq 32\,d_{\ell}^{2}\text{:}$ hypothesis (2) of Lemma 3.3 holds with $A=32\text{.}$</p>
</div>
<div id="S3a.p25" class="ltx_para">
<p id="S3a.p25.1" class="ltx_p"><em id="S3a.p25.1.1" class="ltx_emph ltx_font_italic">Overlap.</em> For $\ell&lt;\ell^{\prime}$ in $I\text{,}$ a contrast $\Delta_{\ell}$ has entries in $[-a_{\ell},a_{\ell}]$ and support of size $d_{T}(u,v)\leq 32\,r_{\ell-1}\text{,}$ by Lemma 2.2(2), so $|\langle\Delta_{\ell},\Delta_{\ell^{\prime}}\rangle|\leq 32\,r_{\ell-1}a_{\ell}a_{\ell^{\prime}}\text{,}$ and with the norm lower bounds just proved the normalized entry is at most $32\sqrt{r_{\ell-1}/r_{\ell^{\prime}-1}}=32\cdot 4^{-(\ell^{\prime}-\ell)}\text{.}$ Retained levels differ by at least four, so every row of the normalized Gram matrix sums to at most</p>
<table id="S3.Ex11a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$2\sum_{t\geq 1}32\cdot 4^{-4t}\ =\ \frac{64}{255}\ =:\ \gamma\ &lt;\ 1:$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p25.2" class="ltx_p">hypothesis (3) of Lemma 3.3 holds with this $\gamma\text{.}$</p>
</div>
<div id="S3a.p26" class="ltx_para">
<p id="S3a.p26.1" class="ltx_p"><em id="S3a.p26.1.1" class="ltx_emph ltx_font_italic">Legality and scalability.</em> With the reference points $u_{\ell}^{0}\in\mathcal{A}_{\ell}$ and $\mu_{0}:=\sum_{\ell\in I}a_{\ell}p_{u_{\ell}^{0}}\text{,}$ a blockwise-scaled member of the group family is</p>
<table id="S3.Ex12a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mu_{0}+\sum_{\ell\in I}\tau_{\ell}\,a_{\ell}\bigl(p_{u_{\ell}}-p_{u_{\ell}^{0}}\bigr)\ =\ \sum_{\ell\in I}a_{\ell}\bigl[(1-\tau_{\ell})\,p_{u_{\ell}^{0}}+\tau_{\ell}\,p_{u_{\ell}}\bigr],$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p26.2" class="ltx_p">a leak combination with nonnegative coefficients of total mass $\sum_{\ell\in I}a_{\ell}=a\text{;}$ hypothesis (1) of Lemma 3.3 holds with $K$ the convex set of all such mass-$a$ combinations.</p>
</div>
<div id="S3a.p27" class="ltx_para">
<p id="S3a.p27.1" class="ltx_p"><em id="S3a.p27.1.1" class="ltx_emph ltx_font_italic">The allocation.</em> Since $a_{\ell}^{2}r_{\ell-1}=a^{2}h_{\ell}/S^{2}\text{,}$</p>
<table id="S3.Ex13a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{\ell\in I}\min\bigl\{a_{\ell}^{2}r_{\ell-1},\ \sigma^{2}h_{\ell}\bigr\}\ =\ \sum_{\ell\in I}h_{\ell}\,\min\Bigl\{\frac{a^{2}}{S^{2}},\ \sigma^{2}\Bigr\}\ =\ H\,\min\Bigl\{\frac{a^{2}}{S^{2}},\ \sigma^{2}\Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p27.2" class="ltx_p">By the Cauchy–Schwarz inequality, $S^{2}\leq H\sum_{\ell\in I}r_{\ell-1}^{-1}\text{,}$ and the radii grow geometrically, so $\sum_{\ell\in I}r_{\ell-1}^{-1}\leq r^{-1}\sum_{i\geq 0}16^{-i}=16/(15r)\leq 2/r\text{;}$ hence $a^{2}/S^{2}\geq a^{2}r/(2H)$ and</p>
<table id="S3.Ex14a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$H\,\min\Bigl\{\frac{a^{2}}{S^{2}},\ \sigma^{2}\Bigr\}\ \geq\ \min\Bigl\{\frac{a^{2}r}{2},\ \sigma^{2}H\Bigr\}\ \geq\ \frac{1}{4}\,\min\bigl\{a^{2}r,\ \sigma^{2}\log M_{i}\bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p27.3" class="ltx_p">using $H\geq\tfrac{1}{4}\log M_{i}\text{.}$</p>
</div>
<div id="S3a.p28" class="ltx_para">
<p id="S3a.p28.1" class="ltx_p"><em id="S3a.p28.1.1" class="ltx_emph ltx_font_italic">Assembly.</em> The contrasts of the group join members of $U_{i}\subseteq\mathcal{C}_{i}\text{,}$ and the connecting paths run inside the connected subtree $\mathcal{C}_{i}\text{,}$ so all group contrasts are supported in the set $S_{i}$ of lower endpoints of the edges of $\mathcal{C}_{i}$ (Lemma 2.2(2)). Lemma 3.3, in its restricted-loss form with $A=32$ and $\gamma=64/255\text{,}$ therefore bounds the Bayes risk of the shrunken group family, for every estimator measurable in the full data, below by</p>
<table id="S3.Ex15a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$c_{A}(1-\gamma)\sum_{\ell\in I}\min\bigl\{d_{\ell}^{2},\sigma^{2}h_{\ell}\bigr\}\ \geq\ c^{\prime}\,\min\bigl\{a^{2}r,\ \sigma^{2}\log M_{i}\bigr\},\qquad c^{\prime}:=\frac{c_{A}(1-\gamma)}{4},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p28.2" class="ltx_p">by the aspect and allocation bounds above. Sums of one shrunken member per group are legal points of $\mathcal{F}_{V}(T)\text{,}$ as verified in the main body; the sets $S_{i}$ are pairwise disjoint, the $E(\mathcal{C}_{i})$ being disjoint and distinct edges having distinct lower endpoints; and the prior is a product across groups. <a href="#S3.Thmlemma1a" title="Lemma S.3.1 (Bayes risks add across disjoint blocks). ‣ S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.3.1</span></a> therefore bounds the joint Bayes risk below by the sum of the isolated group risks, and each isolated problem is, after subtracting its fixed vector, the group problem observed through $Y_{S_{i}}$ alone, so its Bayes risk also dominates the displayed bound. Hence</p>
<table id="S3.Ex16a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(V,\sigma)\ \geq\ c^{\prime}\sum_{i=1}^{q^{\prime}}\min\bigl\{a^{2}r,\ \sigma^{2}\log M_{i}\bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p28.3" class="ltx_p">Finally, $a=V/q^{\prime}\geq V/(6q)\text{,}$ and $\log M_{i}\geq\tfrac{1}{7}\log(eM/q)\text{:}$ if $M/q\geq 36\text{,}$ then with $x:=\log(M/q)\text{,}$ $\log M_{i}\geq\log(M/(6q))=x-\log 6$ and $5(x-\log 6)-(1+x)=4x-5\log 6-1\geq 4\log 36-5\log 6-1=3\log 6-1&gt;0\text{,}$ so the ratio to $\log(eM/q)=1+x$ is at least $\tfrac{1}{5}\text{;}$ if $M/q&lt;36\text{,}$ then $\log M_{i}\geq\log 2$ and $\log(eM/q)&lt;1+\log 36\text{,}$ and $7\log 2&gt;4.8&gt;1+\log 36\text{.}$ Therefore</p>
<table id="S3.Ex17a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(V,\sigma)\ \geq\ \frac{q^{\prime}c^{\prime}}{36}\,\min\Bigl\{\frac{V^{2}r}{q^{2}},\ \sigma^{2}\log\frac{eM}{q}\Bigr\}\ \geq\ \frac{c^{\prime}}{144}\,\min\Bigl\{\frac{V^{2}r}{q},\ \sigma^{2}q\log\frac{eM}{q}\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p28.4" class="ltx_p">which is the claim.
∎</p>
</div>
<div id="S3a.p29" class="ltx_para">
<p id="S3a.p29.1" class="ltx_p">The reduction of Proposition 3.5 rests on a scalar matching of the free parameter $q$ to the profile; the constant $8$ below is the one priced into $A_{0}=18\cdot 8=144\text{.}$</p>
</div>
<div id="S3.Thmlemma3a" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma3a.2" class="ltx_text ltx_font_bold">Lemma S.3.3</span></span><span id="S3.Thmlemma3a.3" class="ltx_text ltx_font_bold"> (Scalar matching).</span></h6>
<div id="S3.Thmlemma3a.p1" class="ltx_para">
<p id="S3.Thmlemma3a.p1.1" class="ltx_p"><span id="S3.Thmlemma3a.p1.1.1" class="ltx_text ltx_font_italic">Let $k\geq 1$ and $M&gt;k$ be integers, let $r&gt;0\text{,}$ and set $L:=\log(M/k)&gt;0\text{.}$ If</span></p>
<table id="S3.Ex18a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}r\,\min\Bigl\{1,\ \frac{L}{k}\Bigr\}\ \geq\ 8\,\sigma^{2}k,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.Thmlemma3a.p1.2" class="ltx_p"><span id="S3.Thmlemma3a.p1.2.1" class="ltx_text ltx_font_italic">then some integer $1\leq q\leq M/2\text{,}$ comparable to $\max\{1,\ k/(1+L)\}$ within universal factors, satisfies</span></p>
<table id="S3.Ex19a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\min\Bigl\{\frac{V^{2}r}{q},\ \sigma^{2}q\log\frac{eM}{q}\Bigr\}\ \geq\ \frac{\sigma^{2}k}{7}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S3a.p30" class="ltx_para">
<p id="S3a.p30.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S3a.p31" class="ltx_para">
<p id="S3a.p31.1" class="ltx_p">Write $B:=1+L$ and note $M\geq 2\text{.}$ There are three cases.</p>
</div>
<div id="S3a.p32" class="ltx_para">
<p id="S3a.p32.1" class="ltx_p"><em id="S3a.p32.1.1" class="ltx_emph ltx_font_italic">Case $L\geq k\text{.}$</em> Take $q:=1\text{,}$ which equals $\max\{1,k/B\}$ since $k/B&lt;1\text{.}$ The hypothesis reads $V^{2}r\geq 8\sigma^{2}k\text{,}$ and $\sigma^{2}\log(eM)=\sigma^{2}(1+\log M)\geq\sigma^{2}(1+L)\geq\sigma^{2}k\text{,}$ so both branches are at least $\sigma^{2}k\text{.}$</p>
</div>
<div id="S3a.p33" class="ltx_para">
<p id="S3a.p33.1" class="ltx_p"><em id="S3a.p33.1.1" class="ltx_emph ltx_font_italic">Case $L&lt;k$ and $M\geq 8k/B\text{.}$</em> Take $q:=\max\{1,\lfloor k/B\rfloor\}\text{.}$ Then $k/(2B)\leq q\leq 2k/B\text{:}$ if $k\geq B$ this is $\lfloor x\rfloor\in[x/2,x]$ at $x=k/B\geq 1\text{;}$ if $k&lt;B\text{,}$ then $q=1\text{,}$ and $k/(2B)&lt;\tfrac{1}{2}&lt;1\leq 2k/B$ because $B=1+L&lt;1+k\leq 2k\text{.}$ Also $q\leq 2k/B\leq M/4&lt;M/2$ by the case hypothesis. The hypothesis of the lemma reads $V^{2}rL/k\geq 8\sigma^{2}k\text{,}$ so</p>
<table id="S3.Ex20a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{V^{2}r}{q}\ \geq\ \frac{B}{2k}\,V^{2}r\ \geq\ \frac{L}{2k}\,V^{2}r\ \geq\ 4\,\sigma^{2}k.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p33.2" class="ltx_p">For the entropy branch, $M=ke^{L}$ and $q\leq 2k/B$ give $eM/q\geq\tfrac{e}{2}\,Be^{L}\text{,}$ so</p>
<table id="S3.Ex21a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log\frac{eM}{q}\ \geq\ 1+L+\log B-\log 2\ \geq\ 0.3\,B,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p33.3" class="ltx_p">since $0.7(1+L)+\log(1+L)\geq 0.7&gt;\log 2\text{;}$ hence $\sigma^{2}q\log(eM/q)\geq\sigma^{2}\,\tfrac{k}{2B}\cdot 0.3B=0.15\,\sigma^{2}k\text{.}$</p>
</div>
<div id="S3a.p34" class="ltx_para">
<p id="S3a.p34.1" class="ltx_p"><em id="S3a.p34.1.1" class="ltx_emph ltx_font_italic">Case $L&lt;k$ and $M&lt;8k/B\text{.}$</em> Take $q:=\lfloor M/2\rfloor\text{,}$ so $M/3\leq q\leq M/2\text{;}$ and $q$ is comparable to $\max\{1,k/B\}\text{,}$ since $k&lt;M&lt;8k/B$ forces $B&lt;8\text{,}$ whence $q\geq(M-1)/2\geq k/2$ and $q&lt;4k/B\leq 4k\text{.}$ The entropy branch has $\log(eM/q)\geq\log(2e)&gt;1\text{,}$ so $\sigma^{2}q\log(eM/q)\geq\sigma^{2}M/3&gt;\sigma^{2}k/3\text{;}$ and the mass branch, using $k/M&gt;B/8$ and $B&gt;L\text{,}$</p>
<table id="S3.Ex22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{V^{2}r}{q}\ \geq\ \frac{2V^{2}r}{M}\ =\ 2\,\frac{V^{2}rL}{k}\cdot\frac{k}{LM}\ \geq\ 16\,\sigma^{2}k\cdot\frac{B}{8L}\ \geq\ 2\,\sigma^{2}k.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p34.2" class="ltx_p">In every case the minimum is at least $0.15\,\sigma^{2}k\geq\sigma^{2}k/7\text{.}$
∎</p>
</div>
<div id="S3a.p35" class="ltx_para">
<p id="S3a.p35.1" class="ltx_p"><em class="ltx_title_proof">Completion of the proof of Proposition 3.5.</em></p>
</div>
<div id="S3a.p36" class="ltx_para">
<p id="S3a.p36.1" class="ltx_p">The main text reduces the proposition to the following situation: an integer $k\geq 1\text{,}$ and $M\geq N^{\uparrow}_{T}(r)&gt;k$ vertices with pairwise tree distances at least $r^{\prime}:=r/9\text{,}$ where</p>
<table id="S3.Ex23" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}r^{\prime}\,\min\Bigl\{1,\ \frac{1}{k}\Bigl[\log\frac{M}{k}\Bigr]_{+}\Bigr\}\ \geq\ \frac{1}{18}\,V^{2}\delta_{k}(T)\ \geq\ \frac{A_{0}}{18}\,\sigma^{2}k\ =\ 8\,\sigma^{2}k:$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p36.2" class="ltx_p">the term at $(r^{\prime},M)$ is at least one ninth of the term at $(r,N^{\uparrow}_{T}(r))\text{,}$ since $r^{\prime}=r/9$ and enlarging the count only increases the positive part. With $L:=\log(M/k)&gt;0$ this is the hypothesis of <a href="#S3.Thmlemma3a" title="Lemma S.3.3 (Scalar matching). ‣ S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.3.3</span></a>. Its conclusion returns an integer $1\leq q\leq M/2\text{,}$ comparable to $\max\{1,k/(1+\log(M/k))\}$ as asserted in the main body, with $\min\{V^{2}r^{\prime}/q,\ \sigma^{2}q\log(eM/q)\}\geq\sigma^{2}k/7\text{.}$ Proposition 3.4, applied to the $M$ separated vertices with this $q\text{,}$ gives $R^{*}_{T}(V,\sigma)\geq(c/7)\,\sigma^{2}k$ with $c$ the constant of that proposition, which proves Proposition 3.5.
∎</p>
</div>
<div id="S3a.p37" class="ltx_para">
<p id="S3a.p37.1" class="ltx_p">Section 3.3 assembles the two halves. We next record its two-point bound, the deferred comparisons from three of the four cases, and the fixed-point conclusion. First, the generic bound (3.6) rests on the oracle inequality for least squares over a finite set of candidates. The inequality is classical, and belongs to the Gaussian model selection theory of <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib6" title="" class="ltx_ref">Birgé and Massart (2001)</a></cite> and <cite class="ltx_cite ltx_citemacro_citet"><a href="#bib.bib38" title="" class="ltx_ref">Massart (2007)</a></cite>; we give the short proof so that its constants are explicit.</p>
</div>
<div id="S3.Thmlemma4a" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma4a.2" class="ltx_text ltx_font_bold">Lemma S.3.4</span></span><span id="S3.Thmlemma4a.3" class="ltx_text ltx_font_bold"> (Finite-class least squares).</span></h6>
<div id="S3.Thmlemma4a.p1" class="ltx_para">
<p id="S3.Thmlemma4a.p1.1" class="ltx_p"><span id="S3.Thmlemma4a.p1.1.1" class="ltx_text ltx_font_italic">Let $Y=\mu+\sigma Z$ with $Z\sim N(0,I_{n})$ and $\mu\in\mathbb{R}^{n}\text{,}$ let $\mathcal{N}\subset\mathbb{R}^{n}$ be finite and nonempty, and let $\widehat{f}$ minimize $\|Y-f\|_{2}^{2}$ over $f\in\mathcal{N}\text{,}$ ties broken by a fixed rule. Then</span></p>
<table id="S3.Ex24" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}_{\mu}\bigl\|\widehat{f}-\mu\bigr\|_{2}^{2}\ \leq\ 4\min_{f\in\mathcal{N}}\|f-\mu\|_{2}^{2}\ +\ 12\,\sigma^{2}\bigl(1+\log|\mathcal{N}|\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S3a.p38" class="ltx_para">
<p id="S3a.p38.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S3a.p39" class="ltx_para">
<p id="S3a.p39.1" class="ltx_p">Let $f^{\star}$ attain the minimum and $a:=\|f^{\star}-\mu\|_{2}\text{.}$ If $|\mathcal{N}|=1$ then $\widehat{f}=f^{\star}$ and the claim is immediate, so assume $N:=|\mathcal{N}|\geq 2\text{.}$ Optimality of $\widehat{f}$ and $Y-f=(\mu-f)+\sigma Z$ give</p>
<table id="S3.Ex25" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|\mu-\widehat{f}\|_{2}^{2}+2\sigma\langle Z,\mu-\widehat{f}\rangle\ \leq\ a^{2}+2\sigma\langle Z,\mu-f^{\star}\rangle,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p39.2" class="ltx_p">that is, $\|\mu-\widehat{f}\|_{2}^{2}\leq a^{2}+2\sigma\langle Z,\widehat{f}-f^{\star}\rangle\text{.}$ Writing $u_{f}:=(f-f^{\star})/\|f-f^{\star}\|_{2}$ for $f\neq f^{\star}$ and $G:=\bigl[\max_{f\neq f^{\star}}\langle Z,u_{f}\rangle\bigr]_{+}\text{,}$ we get $\langle Z,\widehat{f}-f^{\star}\rangle\leq\|\widehat{f}-f^{\star}\|_{2}\,G\text{,}$ whence, with $x:=\|\widehat{f}-\mu\|_{2}$ and the triangle inequality $\|\widehat{f}-f^{\star}\|_{2}\leq x+a\text{,}$</p>
<table id="S3.Ex26" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$x^{2}\ \leq\ a^{2}+2\sigma Gx+2\sigma Ga\ \leq\ a^{2}+\Bigl(\tfrac{x^{2}}{2}+2\sigma^{2}G^{2}\Bigr)+\bigl(a^{2}+\sigma^{2}G^{2}\bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p39.3" class="ltx_p">so $x^{2}\leq 4a^{2}+6\sigma^{2}G^{2}\text{.}$ Each $\langle Z,u_{f}\rangle$ is standard normal, so $\mathbb{P}(G&gt;s)\leq\min\{1,Ne^{-s^{2}/2}\}$ and, splitting the integral $\mathbb{E}G^{2}=\int_{0}^{\infty}2s\,\mathbb{P}(G&gt;s)\,ds$ at $s_{0}:=\sqrt{2\log N}\text{,}$</p>
<table id="S3.Ex27" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}G^{2}\ \leq\ s_{0}^{2}+N\int_{s_{0}}^{\infty}2s\,e^{-s^{2}/2}\,ds\ =\ 2\log N+2.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p39.4" class="ltx_p">Combining the two displays proves the lemma.
∎</p>
</div>
<div id="S3a.p40" class="ltx_para">
<p id="S3a.p40.1" class="ltx_p"><em class="ltx_title_proof">Completion of Theorem 1 and Proposition 1.</em></p>
</div>
<div id="S3a.p41" class="ltx_para">
<p id="S3a.p41.1" class="ltx_p">For the two-point bound, pick $u,w$ at tree distance $H_{T}\text{.}$ The segment from $Vp_{u}$ to $Vp_{w}$ lies in $\mathcal{F}_{V}(T)$ and has length $V\sqrt{H_{T}}$ by Lemma 2.2(1), so it contains two points at distance</p>
<table id="S3.Ex28" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\varrho\ :=\ \min\bigl\{V\sqrt{H_{T}},\ \sigma\bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p41.2" class="ltx_p">Testing one against the other is a one-dimensional Gaussian shift of size $\varrho/\sigma\leq 1\text{,}$ so under the uniform prior on the pair every test errs with probability at least a universal constant. For any estimator, decoding the nearer of the two points errs only when the squared loss is at least $\varrho^{2}/4\text{;}$ hence the maximum of the two risks is at least $c\varrho^{2}\text{,}$ which is the display (3.8).</p>
</div>
<div id="S3a.p42" class="ltx_para">
<p id="S3a.p42.1" class="ltx_p"><em id="S3a.p42.1.1" class="ltx_emph ltx_font_italic">Case $n&lt;C_{\star}\text{.}$</em> By (3.8) and $\sigma^{2}\geq\sigma^{2}n/C_{\star}\text{,}$</p>
<table id="S3.Ex29" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}\ \geq\ c\min\{V^{2}H_{T},\sigma^{2}\}\ \geq\ \frac{c}{C_{\star}}\min\{V^{2}H_{T},\ \sigma^{2}n\}\ \geq\ \frac{c}{C_{\star}}\bigl(\rho_{T}\wedge V^{2}H_{T}\wedge\sigma^{2}n\bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p42.2" class="ltx_p">which is (I) and the lower half of (II); the upper half follows from (3.6), since $\rho_{T}\wedge V^{2}H_{T}\wedge\sigma^{2}n\leq C_{\star}\min\{V^{2}H_{T},\sigma^{2}\}\text{.}$</p>
</div>
<div id="S3a.p43" class="ltx_para">
<p id="S3a.p43.1" class="ltx_p"><em id="S3a.p43.1.1" class="ltx_emph ltx_font_italic">Case $k_{0}=1$ with $n\geq C_{\star}\text{.}$</em> The main text bounds $\rho_{T}\leq(A_{0}/\log 2)\,\sigma^{2}$ there, so</p>
<table id="S3.Ex30" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\rho_{T}\wedge V^{2}H_{T}\wedge\sigma^{2}n\ \leq\ \rho_{T}\ \leq\ C\min\{\sigma^{2},\ V^{2}H_{T}\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3a.p43.2" class="ltx_p">using $\rho_{T}\leq V^{2}h_{T}\leq V^{2}H_{T}$ for the second branch; with (3.8) this gives (I). For (II), $\min\{V^{2}H_{T},\sigma^{2}k_{0}\}=\min\{V^{2}H_{T},\sigma^{2}\}\text{,}$ whose lower half is (3.8) and whose upper half is $R^{*}_{T}\leq C\rho_{T}\wedge CV^{2}H_{T}\leq C^{\prime}\min\{\sigma^{2},V^{2}H_{T}\}$ by (3.6).</p>
</div>
<div id="S3a.p44" class="ltx_para">
<p id="S3a.p44.1" class="ltx_p"><em id="S3a.p44.1.1" class="ltx_emph ltx_font_italic">Case $k_{0}=K+1$ with $n\geq C_{\star}\text{.}$</em> Here $K=\lfloor n/C_{\star}\rfloor\geq n/(2C_{\star})\text{,}$ so $\sigma^{2}k_{0}=\sigma^{2}(K+1)$ lies between $\sigma^{2}n/(2C_{\star})$ and $2\sigma^{2}n/C_{\star}\text{,}$ while $V^{2}H_{T}\geq V^{2}\delta_{K}&gt;A_{0}\sigma^{2}K\geq\sigma^{2}k_{0}/2\text{.}$ Hence $\min\{V^{2}H_{T},\sigma^{2}k_{0}\}\asymp\sigma^{2}n\text{,}$ bounded below by the profile-to-risk lower bound proved in the main body and above by (3.6) through the branch $\sigma^{2}n\text{.}$</p>
</div>
<div id="S3a.p45" class="ltx_para">
<p id="S3a.p45.1" class="ltx_p"><em id="S3a.p45.1.1" class="ltx_emph ltx_font_italic">The fixed point.</em> In the interior case $2\leq k_{0}\leq K\text{,}$ the bound (3.6) gives $\rho_{T}\geq\rho_{T}\wedge V^{2}H_{T}\wedge\sigma^{2}n\geq R^{*}_{T}/C\text{,}$ so (3.9) and (3.10) pin the fixed point itself: $c\,\sigma^{2}k_{0}\leq\rho_{T}\leq C\,\sigma^{2}k_{0}\text{.}$
∎</p>
</div>
</section>
<section id="S4a" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="benchmark-and-broom-profiles"><span class="ltx_tag ltx_tag_section">S.4 </span>Benchmark and Broom Profiles</h2>

<div id="S4a.p1" class="ltx_para">
<p id="S4a.p1.1" class="ltx_p">This section proves Corollaries 1, 2, and 3, together with the broom profile bounds (5.8) and the remaining computations deferred from the broom lower bound of Section 5: the objective cap, the probability of the forcing event, the broom’s covering counts, and the crossing that pins its minimax rate. By Theorem 1 the minimax risk is $\min\{V^{2}H_{T},\sigma^{2}k_{0}\}$ up to universal constants, so each corollary reduces to pinning the covering counts and the profile with explicit constants, localizing $k_{0}\text{,}$ and identifying the active branch in every parameter regime. Throughout, $K:=\lfloor n/C_{\star}\rfloor$ with $C_{\star}=e^{2}\text{;}$ the dimension clause of (1.5) holds at $K+1\text{,}$ so $1\leq k_{0}\leq K+1$ on every tree. In the corollary proofs, $W:=V/\sigma\text{.}$</p>
</div>
<div id="S4a.p2" class="ltx_para">
<p id="S4a.p2.1" class="ltx_p">On the path, ancestor covering is interval covering, and the exact counts it yields reduce the profile to one scalar optimization.</p>
</div>
<div id="S4.Thmlemma1a" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmlemma1a.2" class="ltx_text ltx_font_bold">Lemma S.4.1</span></span><span id="S4.Thmlemma1a.3" class="ltx_text ltx_font_bold"> (Path profile).</span></h6>
<div id="S4.Thmlemma1a.p1" class="ltx_para">
<p id="S4.Thmlemma1a.p1.1" class="ltx_p"><span id="S4.Thmlemma1a.p1.1.1" class="ltx_text ltx_font_italic">Let $P_{L}$ be the path with $L\geq 1$ edges, rooted at one endpoint, so that $n=L+1$ and $h_{P_{L}}=H_{P_{L}}=L\text{.}$ For integers $0\leq q&lt;L\text{,}$</span></p>
<table id="S4.Ex1a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N^{\uparrow}_{T}(q)\ =\ \Bigl\lceil\frac{L+1}{q+1}\Bigr\rceil.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.Thmlemma1a.p1.2" class="ltx_p"><span id="S4.Thmlemma1a.p1.2.1" class="ltx_text ltx_font_italic">Moreover</span></p>
<table id="S4.Ex2a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{k}(P_{L})\ \leq\ \frac{2(L+1)}{ek}\quad\text{for every }k\geq 1,\qquad\alpha_{k}(P_{L})\ \geq\ \frac{L+1}{2ek}\quad\text{for }1\leq k\leq\frac{L+1}{e^{2}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4a.p3" class="ltx_para">
<p id="S4a.p3.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S4a.p4" class="ltx_para">
<p id="S4a.p4.1" class="ltx_p">Index the vertices by depth $0,\dots,L\text{.}$ The ancestors of $u$ are $0,\dots,u\text{,}$ so a center $a$ covers exactly the vertices $a,\dots,\min\{a+q,L\}\text{:}$ ancestor $q$-nets are coverings of $L+1$ points by blocks of $q+1$ consecutive integers anchored at their left endpoints. The centers $j(q+1)\text{,}$ $0\leq j\leq\lfloor L/(q+1)\rfloor\text{,}$ form such a covering, and there are $\lfloor L/(q+1)\rfloor+1=\lceil(L+1)/(q+1)\rceil$ of them; no net is smaller, because each center covers at most $q+1$ of the $L+1$ vertices and net sizes are integers.</p>
</div>
<div id="S4a.p5" class="ltx_para">
<p id="S4a.p5.1" class="ltx_p"><em id="S4a.p5.1.1" class="ltx_emph ltx_font_italic">Upper bound.</em> Consider a radius $q$ whose term in the discrete formula (2.3) is nonzero, so that $N^{\uparrow}_{T}(q)&gt;k\geq 1\text{;}$ then $\lceil(L+1)/(q+1)\rceil\geq 2$ forces $(L+1)/(q+1)&gt;1\text{,}$ whence $N^{\uparrow}_{T}(q)&lt;(L+1)/(q+1)+1&lt;2(L+1)/(q+1)\text{.}$ With $y:=q+1$ and $A:=2(L+1)/k\text{,}$ the term is therefore at most</p>
<table id="S4.Ex3a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$y\,\log\frac{A}{y}\ \leq\ \sup_{y&gt;0}\ y\log\frac{A}{y}\ =\ \frac{A}{e}\ =\ \frac{2(L+1)}{ek},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p5.2" class="ltx_p">the supremum being attained at $y=A/e\text{.}$</p>
</div>
<div id="S4a.p6" class="ltx_para">
<p id="S4a.p6.1" class="ltx_p"><em id="S4a.p6.1.1" class="ltx_emph ltx_font_italic">Lower bound.</em> Set $x:=(L+1)/(ek)$ and $y:=\lfloor x\rfloor\text{.}$ The hypothesis $k\leq(L+1)/e^{2}$ gives $x\geq e&gt;2\text{,}$ so $y\geq x-1\geq x/2\text{;}$ and $y\leq x\leq(L+1)/e\leq L\text{,}$ so $q:=y-1$ is an admissible radius. Then $N^{\uparrow}_{T}(q)=\lceil(L+1)/y\rceil\geq(L+1)/y\geq ek\text{,}$ so $[\log(N^{\uparrow}_{T}(q)/k)]_{+}\geq 1$ and the term at $q$ is at least $y\min\{k,1\}=y\geq(L+1)/(2ek)\text{.}$
∎</p>
</div>
<div id="S4a.p7" class="ltx_para">
<p id="S4a.p7.1" class="ltx_p"><em class="ltx_title_proof">Proof of Corollary 1.</em></p>
</div>
<div id="S4a.p8" class="ltx_para">
<p id="S4a.p8.1" class="ltx_p">By Theorem 1 and $H_{P_{L}}=L\text{,}$ $R^{*}_{P_{L}}(V,\sigma)\asymp\min\{V^{2}L,\sigma^{2}k_{0}\}\text{;}$ write</p>
<table id="S4.Ex4a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$F\ :=\ \min\bigl\{V^{2}L,\ \ V^{2/3}\sigma^{4/3}L^{1/3},\ \ \sigma^{2}(L+1)\bigr\}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p8.2" class="ltx_p">for the right side of Corollary 1. Since its middle branch is the geometric interpolation $(V^{2}L)^{1/3}(\sigma^{2})^{2/3}\text{,}$ every branch of $F\text{,}$ and hence $F$ itself, dominates $\min\{V^{2}L,\sigma^{2}\}\text{.}$ Here $K=\lfloor(L+1)/e^{2}\rfloor\text{,}$ and there are three cases.</p>
</div>
<div id="S4a.p9" class="ltx_para">
<p id="S4a.p9.1" class="ltx_p"><em id="S4a.p9.1.1" class="ltx_emph ltx_font_italic">Case $k_{0}=1\text{.}$</em> Here $\min\{V^{2}L,\sigma^{2}k_{0}\}=\min\{V^{2}L,\sigma^{2}\}\text{,}$ which $F$ dominates; and since $F\leq V^{2}L\text{,}$ the matching upper bound needs an argument only when $\sigma^{2}&lt;V^{2}L\text{.}$ By (1.5), $k_{0}=1$ means $L+1&lt;e^{2}$ or $V^{2}\delta_{1}\leq A_{0}\sigma^{2}\text{.}$ In the first case $F\leq\sigma^{2}(L+1)&lt;e^{2}\sigma^{2}\text{.}$ Otherwise $L+1\geq e^{2}\text{,}$ so <a href="#S4.Thmlemma1a" title="Lemma S.4.1 (Path profile). ‣ S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.4.1</span></a> applies at $k=1$ and gives $\delta_{1}=\alpha_{1}\geq(L+1)/(2e)\text{,}$ whence $F\leq V^{2}L\leq 2e\,V^{2}\delta_{1}\leq 2eA_{0}\sigma^{2}\text{.}$</p>
</div>
<div id="S4a.p10" class="ltx_para">
<p id="S4a.p10.1" class="ltx_p"><em id="S4a.p10.1.1" class="ltx_emph ltx_font_italic">Case $2\leq k_{0}\leq K\text{.}$</em> By minimality no clause of (1.5) holds below $k_{0}\text{,}$ while at $k_{0}$ the crossing clause holds, the dimension clause being silent there. <a href="#S4.Thmlemma1a" title="Lemma S.4.1 (Path profile). ‣ S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.4.1</span></a> is available on all of $[1,K]\text{,}$ since $K\leq(L+1)/e^{2}\text{,}$ and with</p>
<table id="S4.Ex5a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\kappa\ :=\ \Bigl(\frac{V^{2}(L+1)}{eA_{0}\sigma^{2}}\Bigr)^{1/3}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p10.2" class="ltx_p">the crossing inequalities at $k_{0}$ and $k_{0}-1$ read</p>
<table id="S4.Ex6a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{V^{2}(L+1)}{2e\,k_{0}^{2}}\ \leq\ V^{2}\delta_{k_{0}}\ \leq\ A_{0}\sigma^{2}k_{0},\qquad A_{0}\sigma^{2}(k_{0}-1)\ &lt;\ V^{2}\delta_{k_{0}-1}\ \leq\ \frac{2V^{2}(L+1)}{e\,(k_{0}-1)^{2}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p10.3" class="ltx_p">that is, $k_{0}^{3}\geq\kappa^{3}/2$ and $(k_{0}-1)^{3}&lt;2\kappa^{3}\text{;}$ since $k_{0}\geq 2$ gives $k_{0}\leq 2(k_{0}-1)\text{,}$</p>
<table id="S4.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$2^{-1/3}\,\kappa\ \leq\ k_{0}\ \leq\ 2^{4/3}\,\kappa.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p10.4" class="ltx_p">Hence $\sigma^{2}k_{0}\asymp\sigma^{2}\kappa\asymp V^{2/3}\sigma^{4/3}L^{1/3}\text{,}$ the middle branch of $F\text{,}$ using $L\leq L+1\leq 2L\text{.}$ That branch is the least of the three up to constants: failure of the crossing clause at $k=1$ gives $A_{0}\sigma^{2}&lt;V^{2}\delta_{1}\leq 4V^{2}L/e\text{,}$ so $\sigma^{2}\leq CV^{2}L$ and the middle branch is at most $(V^{2}L)^{1/3}(CV^{2}L)^{2/3}=C^{2/3}V^{2}L\text{;}$ and it is $\asymp\sigma^{2}k_{0}\leq\sigma^{2}K\leq\sigma^{2}(L+1)\text{.}$ Therefore $F\asymp\sigma^{2}k_{0}\text{,}$ and the same middle-branch bound gives $\sigma^{2}k_{0}\leq CV^{2}L\text{,}$ so $\min\{V^{2}L,\sigma^{2}k_{0}\}\asymp\sigma^{2}k_{0}$ as well.</p>
</div>
<div id="S4a.p11" class="ltx_para">
<p id="S4a.p11.1" class="ltx_p"><em id="S4a.p11.1.1" class="ltx_emph ltx_font_italic">Case $k_{0}=K+1\geq 2\text{.}$</em> Then $K\geq 1\text{,}$ so $L+1\geq e^{2}\text{,}$ and no clause fired on $[1,K]\text{;}$ at $k=K\text{,}$</p>
<table id="S4.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$A_{0}\sigma^{2}K\ &lt;\ V^{2}\delta_{K}\ \leq\ \frac{2V^{2}(L+1)}{eK^{2}},\quad\text{so}\quad V^{2}(L+1)\ &gt;\ \frac{eA_{0}}{2}\,\sigma^{2}K^{3}\ \geq\ \frac{A_{0}}{16e^{5}}\,\sigma^{2}(L+1)^{3},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p11.2" class="ltx_p">using $K\geq(L+1)/(2e^{2})\text{,}$ which holds because $\lfloor x\rfloor\geq x/2$ for $x\geq 1\text{.}$ Hence $V^{2}\geq c\,\sigma^{2}(L+1)^{2}$ with $c:=A_{0}/(16e^{5})\text{,}$ and both remaining branches of $F$ dominate the third: $V^{2}L\geq\tfrac{1}{2}V^{2}(L+1)\geq\tfrac{c}{2}\,\sigma^{2}(L+1)^{3}\geq\tfrac{c}{2}\,\sigma^{2}(L+1)\text{,}$ and $(V^{2}L)^{1/3}\sigma^{4/3}\geq(\tfrac{c}{2})^{1/3}\sigma^{2}(L+1)\text{.}$ Therefore $F\asymp\sigma^{2}(L+1)\text{.}$ On the other side, $(L+1)/e^{2}&lt;K+1\leq 2(L+1)/e^{2}$ gives $\sigma^{2}k_{0}\asymp\sigma^{2}(L+1)\text{,}$ and $\min\{V^{2}L,\sigma^{2}k_{0}\}\asymp\sigma^{2}(L+1)$ as well, by $V^{2}L\geq\tfrac{c}{2}\,\sigma^{2}(L+1)\text{.}$ The three cases are exhaustive.
∎</p>
</div>
<div id="S4a.p12" class="ltx_para">
<p id="S4a.p12.1" class="ltx_p">On the star, $h_{S_{m}}=1\text{,}$ so only the count $N^{\uparrow}_{T}(0)=m+1$ remains; the profile is exact by Remark 2.1, splitting into a capped and a logarithmic phase, and the case analysis tracks which phase meets the crossing.</p>
</div>
<div id="S4a.p13" class="ltx_para">
<p id="S4a.p13.1" class="ltx_p"><em class="ltx_title_proof">Proof of Corollary 2.</em></p>
</div>
<div id="S4a.p14" class="ltx_para">
<p id="S4a.p14.1" class="ltx_p">By Theorem 1 and $H_{S_{m}}=2\text{,}$ $R^{*}_{S_{m}}(V,\sigma)\asymp\min\{V^{2},\sigma^{2}k_{0}\}$ after absorbing the factor two; here $n=m+1\text{.}$ By Remark 2.1,</p>
<table id="S4.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{k}\ =\ \min\{k,\ \ell(k)\},\qquad\ell(x)\ :=\ \Bigl[\log\frac{m+1}{x}\Bigr]_{+}\quad(x&gt;0),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p14.2" class="ltx_p">and since $k$ grows while $\ell(k)$ does not, the set $\{k\geq 1:k\leq\ell(k)\}$ is an initial segment of the integers; it contains $1\text{,}$ because $\ell(1)=\log(m+1)&gt;1\text{,}$ and is finite, because $\ell$ vanishes beyond $m+1\text{.}$ With $\bar{k}$ its largest element, the profile has two phases:</p>
<table id="S4.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}\delta_{k}\ =\ \sigma^{2}W^{2}\ \ (k\leq\bar{k}),\qquad V^{2}\delta_{k}\ =\ \sigma^{2}W^{2}\,\frac{\ell(k)}{k}\ \ (k&gt;\bar{k}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p14.3" class="ltx_p">Write</p>
<table id="S4.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Lambda\ :=\ 1+\bigl[\log(m/W)\bigr]_{+},\qquad F\ :=\ \min\bigl\{V^{2},\ \sigma^{2}W\sqrt{\Lambda},\ \sigma^{2}m\bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p14.4" class="ltx_p">so that $F$ is the right side of Corollary 2.</p>
</div>
<div id="S4a.p15" class="ltx_para">
<p id="S4a.p15.1" class="ltx_p"><em id="S4a.p15.1.1" class="ltx_emph ltx_font_italic">Bounded stars.</em> For any universal $m_{0}$ the corollary holds for $m\leq m_{0}$ with constants depending only on $m_{0}\text{:}$ from $1\leq k_{0}\leq K+1\leq m_{0}\text{,}$ $\min\{V^{2},\sigma^{2}k_{0}\}\asymp\min\{V^{2},\sigma^{2}\}\text{,}$ while $F\leq\min\{V^{2},\sigma^{2}m\}\leq m_{0}\min\{V^{2},\sigma^{2}\}$ and every branch of $F$ dominates $\min\{V^{2},\sigma^{2}\}\text{,}$ the middle one because $\sigma^{2}W\sqrt{\Lambda}\geq\sigma V\geq\min\{V^{2},\sigma^{2}\}\text{.}$ Now fix a universal $m_{0}$ with the following four properties for every $m\geq m_{0}$ (one may take $m_{0}=\lceil e^{10}\rceil$): (a) $\bar{k}\geq\tfrac{1}{2}\log(m+1)\text{;}$ (b) $\bar{k}+1\leq K\text{;}$ (c) $\log(m/w)\geq\tfrac{1}{2}(1+\log m)$ whenever $1\leq w\leq\sqrt{A_{0}\log(m+1)}\text{;}$ (d) $m\geq 4e^{4}(1+\log m)\text{.}$ Property (a) holds because $k^{\prime}:=\lceil\tfrac{1}{2}\log(m+1)\rceil$ satisfies $k^{\prime}+\log k^{\prime}\leq\log(m+1)$ once $m$ is large, so that $k^{\prime}\leq\ell(k^{\prime})\text{;}$ (b) and (d) compare linear with logarithmic growth; (c) is worst at $w=\sqrt{A_{0}\log(m+1)}\text{,}$ where it reads $\tfrac{1}{2}\log m\geq\tfrac{1}{2}+\tfrac{1}{2}\log(A_{0}\log(m+1))\text{.}$ We also use, unconditionally, $\bar{k}\leq\ell(\bar{k})\leq\log(m+1)\text{.}$ Assume $m\geq m_{0}\text{;}$ there are four cases in $W\text{.}$</p>
</div>
<div id="S4a.p16" class="ltx_para">
<p id="S4a.p16.1" class="ltx_p"><em id="S4a.p16.1.1" class="ltx_emph ltx_font_italic">Case $W^{2}\leq A_{0}\text{.}$</em> Since $\bar{k}\geq 1\text{,}$ the capped phase gives $V^{2}\delta_{1}=\sigma^{2}W^{2}\leq A_{0}\sigma^{2}\text{:}$ the crossing clause fires at once and $k_{0}=1\text{.}$ Then $\min\{V^{2},\sigma^{2}k_{0}\}\in[V^{2}/A_{0},\,V^{2}]\text{.}$ And $F\asymp V^{2}\text{:}$ it is at most $V^{2}\text{,}$ while $\sigma^{2}W\sqrt{\Lambda}\geq\sigma^{2}W\geq V^{2}/\sqrt{A_{0}}$ and $\sigma^{2}m\geq 2\sigma^{2}\geq 2V^{2}/A_{0}\text{.}$</p>
</div>
<div id="S4a.p17" class="ltx_para">
<p id="S4a.p17.1" class="ltx_p"><em id="S4a.p17.1.1" class="ltx_emph ltx_font_italic">Case $A_{0}&lt;W^{2}\leq A_{0}\bar{k}\text{.}$</em> Every integer $k&lt;W^{2}/A_{0}$ has $k&lt;\bar{k}\text{,}$ so the capped phase gives $V^{2}\delta_{k}=\sigma^{2}W^{2}&gt;A_{0}\sigma^{2}k\text{,}$ and $k&lt;\bar{k}\leq K$ keeps the dimension clause silent: no clause fires below $W^{2}/A_{0}\text{.}$ At $k_{1}:=\lceil W^{2}/A_{0}\rceil\text{,}$ which is at most $\bar{k}\leq K$ because $W^{2}/A_{0}\leq\bar{k}$ and $\bar{k}$ is an integer, the bound $\delta_{k_{1}}\leq 1$ gives $V^{2}\delta_{k_{1}}\leq\sigma^{2}W^{2}\leq A_{0}\sigma^{2}k_{1}\text{.}$ Hence</p>
<table id="S4.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$k_{0}\ =\ \Bigl\lceil\frac{W^{2}}{A_{0}}\Bigr\rceil\ \in\ \Bigl[\frac{W^{2}}{A_{0}},\ \frac{2W^{2}}{A_{0}}\Bigr],\qquad\sigma^{2}k_{0}\ \asymp\ V^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p17.2" class="ltx_p">so $\min\{V^{2},\sigma^{2}k_{0}\}\asymp V^{2}\text{.}$ For $F\asymp V^{2}\text{:}$ the case hypothesis and $\bar{k}\leq\log(m+1)$ give $W\leq\sqrt{A_{0}\log(m+1)}\text{,}$ so property (c) yields $\Lambda\geq\tfrac{1}{2}(1+\log m)$ and</p>
<table id="S4.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sigma^{2}W\sqrt{\Lambda}\ \geq\ V^{2}\,\frac{\sqrt{\Lambda}}{W}\ \geq\ V^{2}\,\frac{\sqrt{(1+\log m)/2}}{\sqrt{A_{0}(1+\log m)}}\ =\ \frac{V^{2}}{\sqrt{2A_{0}}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p17.3" class="ltx_p">the denominator by $\log(m+1)\leq 1+\log m\text{.}$ Also $\sigma^{2}m\geq\sigma^{2}W^{2}=V^{2}\text{,}$ since property (d) gives $m\geq A_{0}\log(m+1)\geq W^{2}\text{.}$</p>
</div>
<div id="S4a.p18" class="ltx_para">
<p id="S4a.p18.1" class="ltx_p"><em id="S4a.p18.1.1" class="ltx_emph ltx_font_italic">Case $W^{2}&gt;A_{0}\bar{k}$ and $W&lt;m\text{.}$</em> Now $W&gt;\sqrt{A_{0}}$ and $\log(m/W)&gt;0\text{,}$ so $\Lambda=1+\log(m/W)\text{.}$ Set</p>
<table id="S4.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\kappa\ :=\ W\sqrt{\Lambda},\qquad c_{1}\ :=\ \frac{1}{2\sqrt{A_{0}}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p18.2" class="ltx_p"><em id="S4a.p18.2.1" class="ltx_emph ltx_font_italic">No crossing below $c_{1}\kappa\text{:}$</em> fix an integer $k\leq\min\{c_{1}\kappa,K\}\text{,}$ so that the dimension clause is silent at $k\text{.}$ If $k\leq\bar{k}\text{,}$ the capped phase and the case hypothesis give $V^{2}\delta_{k}=\sigma^{2}W^{2}&gt;A_{0}\sigma^{2}\bar{k}\geq A_{0}\sigma^{2}k\text{.}$ If $\bar{k}&lt;k\leq c_{1}\kappa\text{,}$ monotonicity of $\ell$ gives</p>
<table id="S4.Ex15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\ell(k)\ \geq\ \ell(c_{1}\kappa)\ \geq\ \log\frac{m}{c_{1}W\sqrt{\Lambda}}\ =\ (\Lambda-1)+\log(2\sqrt{A_{0}})-\tfrac{1}{2}\log\Lambda\ \geq\ \frac{\Lambda}{4}+1,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p18.3" class="ltx_p">the last step because $\log(2\sqrt{A_{0}})=\log 24&gt;3$ and $\tfrac{3}{4}\Lambda+1\geq\tfrac{1}{2}\log\Lambda$ for every $\Lambda\geq 1\text{;}$ hence, using $A_{0}c_{1}^{2}=\tfrac{1}{4}\text{,}$</p>
<table id="S4.Ex16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}\delta_{k}\ =\ \sigma^{2}\,\frac{W^{2}\ell(k)}{k}\ &gt;\ \sigma^{2}\,\frac{W^{2}\Lambda}{4k}\ =\ A_{0}\sigma^{2}\,\frac{(c_{1}\kappa)^{2}}{k}\ \geq\ A_{0}\sigma^{2}k.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p18.4" class="ltx_p">So no clause fires at $k\text{,}$ and $k_{0}&gt;\min\{c_{1}\kappa,K\}\text{.}$ <em id="S4a.p18.4.1" class="ltx_emph ltx_font_italic">Crossing by $\lceil\kappa\rceil\text{:}$</em> if $\lceil\kappa\rceil\leq K\text{,}$ then $k_{1}:=\lceil\kappa\rceil$ has</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S4.EGx3"></span><span class="paper-eq-anchor" id="S4.Ex17"></span><span class="paper-eq-anchor" id="S4.Ex18"></span><div class="paper-eqgroup-body">$$\begin{gathered}
\displaystyle\ell(k_{1})\ \leq\ \Bigl[\log\frac{2m}{\kappa}\Bigr]_{+}\ \leq\ \log 2+(\Lambda-1)-\tfrac{1}{2}\log\Lambda\ &lt;\ \Lambda, \\
\displaystyle V^{2}\delta_{k_{1}}\ \leq\ \sigma^{2}\,\frac{W^{2}\Lambda}{k_{1}}\ \leq\ \sigma^{2}\kappa\ \leq\ A_{0}\sigma^{2}k_{1},
\end{gathered}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S4a.p18.5" class="ltx_p">so the crossing clause fires by $k_{1}$ and $k_{0}\leq\lceil\kappa\rceil\text{.}$</p>
</div>
<div id="S4a.p19" class="ltx_para">
<p id="S4a.p19.1" class="ltx_p">If $\kappa\leq K\text{:}$ then $c_{1}\kappa&lt;k_{0}\leq\lceil\kappa\rceil\leq 2\kappa\text{,}$ using $\kappa\geq W&gt;1\text{,}$ so $\sigma^{2}k_{0}\asymp\sigma^{2}\kappa=\sigma^{2}W\sqrt{\Lambda}\text{,}$ the middle branch of $F\text{.}$ Moreover, by property (a) and the case hypothesis,</p>
<table id="S4.Ex19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Lambda\ \leq\ 1+\log m\ \leq\ 1+2\bar{k}\ &lt;\ 1+\frac{2W^{2}}{A_{0}}\ \leq\ \frac{3W^{2}}{A_{0}},\qquad\text{so}\qquad\sigma^{2}\kappa\ \leq\ \sqrt{\tfrac{3}{A_{0}}}\,V^{2}\ \leq\ \tfrac{1}{6}\,V^{2}:$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p19.2" class="ltx_p">hence $\min\{V^{2},\sigma^{2}k_{0}\}\asymp\sigma^{2}\kappa\text{,}$ and $F\asymp\sigma^{2}\kappa$ as well: the first branch is at least $6\sigma^{2}\kappa\text{,}$ and the third is at least the second because $\kappa\leq K\leq m\text{.}$ If $\kappa&gt;K\text{:}$ then $k_{0}&gt;\min\{c_{1}\kappa,K\}\geq c_{1}K$ and $k_{0}\leq K+1\leq 2K\text{,}$ so $\sigma^{2}k_{0}\asymp\sigma^{2}K\asymp\sigma^{2}m\text{,}$ using $K\geq(m+1)/(2e^{2})\text{.}$ Also $V^{2}&gt;\sigma^{2}m\text{:}$ squaring $W\sqrt{\Lambda}=\kappa&gt;K\geq m/(2e^{2})$ gives</p>
<table id="S4.Ex20" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}\ =\ \sigma^{2}W^{2}\ &gt;\ \frac{\sigma^{2}m^{2}}{4e^{4}\Lambda}\ \geq\ \sigma^{2}m,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p19.3" class="ltx_p">by property (d) and $\Lambda\leq 1+\log m\text{.}$ Hence $\min\{V^{2},\sigma^{2}k_{0}\}\asymp\sigma^{2}m\text{,}$ and $F\asymp\sigma^{2}m\text{:}$ its first branch exceeds $\sigma^{2}m\text{,}$ and its second is $\sigma^{2}\kappa&gt;\sigma^{2}K\geq\sigma^{2}m/(2e^{2})\text{.}$</p>
</div>
<div id="S4a.p20" class="ltx_para">
<p id="S4a.p20.1" class="ltx_p"><em id="S4a.p20.1.1" class="ltx_emph ltx_font_italic">Case $W\geq m\text{.}$</em> Then $\Lambda=1$ and $F=\sigma^{2}\min\{W^{2},W,m\}=\sigma^{2}m\text{.}$ For every integer $k\leq K\text{,}$</p>
<table id="S4.Ex21" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\ell(k)\ \geq\ \ell(K)\ =\ \log\frac{m+1}{K}\ \geq\ \log C_{\star}\ =\ 2,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p20.2" class="ltx_p">so $\min\{k,\ell(k)\}\geq 1$ and $V^{2}\delta_{k}\geq\sigma^{2}W^{2}/k&gt;A_{0}\sigma^{2}k$ whenever $k&lt;W/\sqrt{A_{0}}\text{:}$ no clause fires below $\min\{W/\sqrt{A_{0}},\,K+1\}\geq m/12\text{,}$ the first entry because $W\geq m$ and $\sqrt{A_{0}}=12\text{,}$ the second because $K+1&gt;(m+1)/e^{2}$ and $e^{2}&lt;12\text{.}$ Hence $m/12\leq k_{0}\leq K+1\leq m$ and $\sigma^{2}k_{0}\asymp\sigma^{2}m\text{.}$ Since $V^{2}=\sigma^{2}W^{2}\geq\sigma^{2}m^{2}\geq\sigma^{2}m\text{,}$ also $\min\{V^{2},\sigma^{2}k_{0}\}\asymp\sigma^{2}m\asymp F\text{.}$</p>
</div>
<div id="S4a.p21" class="ltx_para">
<p id="S4a.p21.1" class="ltx_p">The four cases cover $m\geq m_{0}\text{:}$ if $W\geq m$ the fourth applies, and otherwise $W^{2}\leq A_{0}\text{,}$ $A_{0}&lt;W^{2}\leq A_{0}\bar{k}\text{,}$ and $W^{2}&gt;A_{0}\bar{k}$ partition the range.
∎</p>
</div>
<div id="S4a.p22" class="ltx_para">
<p id="S4a.p22.1" class="ltx_p">On the complete binary tree the covering counts decay exponentially in the radius. Radius therefore trades against entropy linearly, and the profile is governed by $\log(n/k)\text{:}$ quadratic in that logarithm when the budget exceeds it, and truncated at the budget otherwise.</p>
</div>
<div id="S4.Thmlemma2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmlemma2.2" class="ltx_text ltx_font_bold">Lemma S.4.2</span></span><span id="S4.Thmlemma2.3" class="ltx_text ltx_font_bold"> (Binary profile).</span></h6>
<div id="S4.Thmlemma2.p1" class="ltx_para">
<p id="S4.Thmlemma2.p1.1" class="ltx_p"><span id="S4.Thmlemma2.p1.1.1" class="ltx_text ltx_font_italic">Let $B_{h}$ be the complete binary tree of height $h\geq 1\text{,}$ with $n=2^{h+1}-1$ vertices, $h_{B_{h}}=h\text{,}$ and $H_{B_{h}}=2h\text{.}$ For integers $0\leq q&lt;h\text{,}$</span></p>
<table id="S4.Ex22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$2^{h-q}\ \leq\ N^{\uparrow}_{T}(q)\ \leq\ 3\cdot 2^{h-q},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.Thmlemma2.p1.2" class="ltx_p"><span id="S4.Thmlemma2.p1.2.1" class="ltx_text ltx_font_italic">and for every integer $1\leq k\leq n/C_{\star}\text{,}$ with $\beta:=\log(n/k)\text{,}$ which is at least $2$ in this range,</span></p>
<table id="S4.Ex23" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$c_{B}\,\beta\min\{k,\beta\}\ \leq\ \alpha_{k}(B_{h})\ \leq\ C_{B}\,\beta\min\{k,\beta\},\qquad c_{B}:=\frac{1}{8\log 2},\quad C_{B}:=3.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4a.p23" class="ltx_para">
<p id="S4a.p23.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S4a.p24" class="ltx_para">
<p id="S4a.p24.1" class="ltx_p"><em id="S4a.p24.1.1" class="ltx_emph ltx_font_italic">Covering counts.</em> An ancestor of a depth-$h$ leaf within distance $q$ has depth at least $h-q\text{,}$ and a vertex at depth $d\geq h-q$ has $2^{h-d}\leq 2^{q}$ leaf descendants; covering all $2^{h}$ leaves therefore needs at least $2^{h-q}$ centers. Conversely, let $R$ consist of the root together with every vertex whose depth is of the form $D_{j}:=h-q-j(q+1)\geq 0\text{,}$ $j\geq 0\text{.}$ A selected vertex covers exactly the depths $D_{j},\dots,D_{j}+q$ of its subtree; consecutive selected depths differ by $q+1\text{,}$ so the covered bands tile $\{D_{j^{*}},\dots,h\}\text{,}$ where $D_{j^{*}}$ is the smallest selected depth, and $D_{j^{*}}\leq q\text{,}$ since otherwise $D_{j^{*}}-(q+1)\geq 0$ would be selected as well; the root covers the depths below $D_{j^{*}}\text{.}$ Hence $R$ is an ancestor $q$-net, of size</p>
<table id="S4.Ex24" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$1+\sum_{j:\,D_{j}\geq 0}2^{D_{j}}\ \leq\ 1+2^{h-q}\sum_{j\geq 0}2^{-j(q+1)}\ \leq\ 1+2\cdot 2^{h-q}\ \leq\ 3\cdot 2^{h-q}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S4a.p25" class="ltx_para">
<p id="S4a.p25.1" class="ltx_p"><em id="S4a.p25.1.1" class="ltx_emph ltx_font_italic">Profile, upper bound.</em> Since $2^{h+1}=n+1$ and $\log(n+1)\leq\log n+\tfrac{1}{3}$ for $n\geq 3\text{,}$ every integer $0\leq q&lt;h$ has, with $y:=q+1\text{,}$</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S4.EGx4"></span><span class="paper-eq-anchor" id="S4.Ex25"></span><span class="paper-eq-anchor" id="S4.Ex26"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\log\frac{N^{\uparrow}_{T}(q)}{k}\space &amp; \displaystyle\leq\ (h-q)\log 2+\log 3-\log k \\
 &amp; \displaystyle=\ \log(n+1)+\log 3-\log k-y\log 2\ \leq\ \beta+\tfrac{3}{2}-y\log 2,
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S4a.p25.2" class="ltx_p">and $\beta+\tfrac{3}{2}\leq\tfrac{7}{4}\beta$ because $\beta\geq 2\text{.}$ Substituting $u:=y\log 2$ in the discrete formula (2.3) and writing $B:=\tfrac{7}{4}\beta\text{,}$</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S4.EGx5"></span><span class="paper-eq-anchor" id="S4.Ex27"></span><span class="paper-eq-anchor" id="S4.Ex28"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\alpha_{k}(B_{h})\ \leq\ \frac{1}{\log 2}\,\sup_{u&gt;0}\ u\,\min\bigl\{k,\ (B-u)_{+}\bigr\}\space &amp; \displaystyle\leq\ \frac{1}{\log 2}\,B\,\min\Bigl\{\frac{B}{4},\ k\Bigr\} \\
 &amp; \displaystyle\leq\ \frac{7}{4\log 2}\,\beta\min\{k,\beta\}\ \leq\ C_{B}\,\beta\min\{k,\beta\}:
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S4a.p25.3" class="ltx_p">if $k\geq B/4$ the supremum is at most $\sup_{u}u(B-u)_{+}=B^{2}/4\text{,}$ while if $k&lt;B/4$ the product is at most $uk\leq(B-k)k$ for $u\leq B-k\text{,}$ and at most $u(B-u)_{+}\leq(B-k)k$ beyond, since $u(B-u)_{+}$ is nonincreasing past $B/2&lt;B-k\text{.}$</p>
</div>
<div id="S4a.p26" class="ltx_para">
<p id="S4a.p26.1" class="ltx_p"><em id="S4a.p26.1.1" class="ltx_emph ltx_font_italic">Profile, lower bound.</em> Set $y:=\lfloor\beta/(2\log 2)\rfloor\text{.}$ From $\beta\geq 2\text{:}$ $\beta/(2\log 2)\geq 1/\log 2&gt;1\text{,}$ so $y\geq 1$ and, halving, $y\geq\beta/(4\log 2)\text{;}$ and $y\leq\beta/(2\log 2)\leq\log n/(2\log 2)\leq(h+1)/2\leq h\text{,}$ so $q:=y-1$ is an admissible radius. At this radius,</p>
<table id="S4.Ex29" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log\frac{N^{\uparrow}_{T}(q)}{k}\ \geq\ (h-q)\log 2-\log k\ =\ \log(n+1)-\log k-y\log 2\ \geq\ \beta-\frac{\beta}{2}\ =\ \frac{\beta}{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p26.2" class="ltx_p">so, using $\min\{k,\beta/2\}\geq\tfrac{1}{2}\min\{k,\beta\}\text{,}$ the term at $q$ is at least</p>
<table id="S4.Ex30" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$y\,\min\Bigl\{k,\ \frac{\beta}{2}\Bigr\}\ \geq\ \frac{\beta}{4\log 2}\cdot\frac{\min\{k,\beta\}}{2}\ =\ c_{B}\,\beta\min\{k,\beta\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S4a.p27" class="ltx_para">
<p id="S4a.p27.1" class="ltx_p"><em class="ltx_title_proof">Proof of Corollary 3.</em></p>
</div>
<div id="S4a.p28" class="ltx_para">
<p id="S4a.p28.1" class="ltx_p">By Theorem 1 and $H_{B_{h}}=2h\text{,}$ $R^{*}_{B_{h}}(V,\sigma)\asymp\min\{V^{2}h,\sigma^{2}k_{0}\}$ after absorbing the factor two. Write $\beta(k):=\log(n/k)\text{,}$ as in <a href="#S4.Thmlemma2" title="Lemma S.4.2 (Binary profile). ‣ S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.4.2</span></a>, and</p>
<table id="S4.Ex31" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Lambda\ :=\ 1+\bigl[\log(n/W)\bigr]_{+},\qquad F\ :=\ \sigma^{2}\min\bigl\{W^{2}h,\ W\Lambda,\ n\bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p28.2" class="ltx_p">the right side of Corollary 3.</p>
</div>
<div id="S4a.p29" class="ltx_para">
<p id="S4a.p29.1" class="ltx_p"><em id="S4a.p29.1.1" class="ltx_emph ltx_font_italic">Bounded trees.</em> For any universal $n_{0}$ the corollary holds for $n\leq n_{0}$ with constants depending only on $n_{0}\text{:}$ from $1\leq k_{0}\leq K+1\leq n_{0}\text{,}$ $\min\{V^{2}h,\sigma^{2}k_{0}\}\asymp\min\{V^{2}h,\sigma^{2}\}\text{,}$ while $F\leq\min\{V^{2}h,\sigma^{2}n\}\leq n_{0}\min\{V^{2}h,\sigma^{2}\}$ and every branch of $F$ dominates $\min\{V^{2}h,\sigma^{2}\}\text{;}$ for the middle branch, when $W\leq 1$ this is $\sigma^{2}W\Lambda\geq\log 2\cdot\sigma^{2}W^{2}h\text{,}$ using $W\geq W^{2}$ and $\Lambda\geq 1+\log n\geq h\log 2\text{,}$ and when $W&gt;1$ it is $\sigma^{2}W\Lambda\geq\sigma^{2}\text{.}$ Now fix a universal $n_{0}$ (one may take $n_{0}=2^{7}$) such that for every $n\geq n_{0}\text{:}$ $h\leq K\text{,}$ $n\leq 2e^{2}K\text{,}$ and $\log h\leq\tfrac{\log 2}{2}\,h\text{.}$ Assume $n\geq n_{0}\text{.}$</p>
</div>
<div id="S4a.p30" class="ltx_para">
<p id="S4a.p30.1" class="ltx_p"><em id="S4a.p30.1.1" class="ltx_emph ltx_font_italic">The diameter regime $W\leq 1\text{.}$</em> We claim $k_{0}\geq c\,W^{2}h$ with $c:=c_{B}\log 2/(4A_{0})\text{.}$ This is trivial when $cW^{2}h&lt;1\text{;}$ otherwise fix an integer $k\leq cW^{2}h\leq ch\text{.}$ Then</p>
<table id="S4.Ex32" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\beta(k)\ \geq\ \log\frac{2^{h}}{h}\ =\ h\log 2-\log h\ \geq\ \frac{\log 2}{2}\,h\ \geq\ k,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p30.2" class="ltx_p">the last step because $c\leq\log 2/2\text{;}$ so <a href="#S4.Thmlemma2" title="Lemma S.4.2 (Binary profile). ‣ S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.4.2</span></a> gives</p>
<table id="S4.Ex33" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}\delta_{k}\ \geq\ c_{B}\,\sigma^{2}W^{2}\beta(k)\ \geq\ \frac{c_{B}\log 2}{2}\,\sigma^{2}W^{2}h\ &gt;\ A_{0}\sigma^{2}\,cW^{2}h\ \geq\ A_{0}\sigma^{2}k,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p30.3" class="ltx_p">and the dimension clause is silent at $k\leq h\leq K\text{:}$ no clause fires at any $k\leq cW^{2}h\text{,}$ proving the claim. In either case $\sigma^{2}k_{0}\geq c\,V^{2}h\text{,}$ so</p>
<table id="S4.Ex34" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\min\{V^{2}h,\ \sigma^{2}k_{0}\}\ \asymp\ V^{2}h.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p30.4" class="ltx_p">And $F\asymp V^{2}h\text{:}$ its first branch is $V^{2}h\text{;}$ its middle branch dominates $\log 2\cdot V^{2}h$ as above; and $\sigma^{2}n\geq\sigma^{2}h\geq V^{2}h\text{.}$ This proves the corollary for $W\leq 1\text{.}$</p>
</div>
<div id="S4a.p31" class="ltx_para">
<p id="S4a.p31.1" class="ltx_p"><em id="S4a.p31.1.1" class="ltx_emph ltx_font_italic">The entropy and dimension regimes $W&gt;1\text{.}$</em> Put $\kappa:=W\Lambda\geq 1\text{.}$ First, if $\lceil\kappa\rceil\leq K\text{,}$ the crossing clause fires by $k_{1}:=\lceil\kappa\rceil\text{:}$ there $W\leq k_{1}\leq K\leq n\text{,}$ so $\beta(k_{1})\leq\log(n/W)\leq\Lambda\text{,}$ and <a href="#S4.Thmlemma2" title="Lemma S.4.2 (Binary profile). ‣ S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.4.2</span></a> gives</p>
<table id="S4.Ex35" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}\delta_{k_{1}}\ \leq\ C_{B}\,\sigma^{2}\,\frac{W^{2}\beta(k_{1})^{2}}{k_{1}}\ \leq\ C_{B}\,\sigma^{2}\,\frac{W^{2}\Lambda^{2}}{\kappa}\ =\ C_{B}\,\sigma^{2}\kappa\ \leq\ A_{0}\sigma^{2}k_{1};$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p31.2" class="ltx_p">hence $k_{0}\leq\lceil\kappa\rceil$ whenever $\lceil\kappa\rceil\leq K\text{.}$ Second, with $c:=c_{B}/(8A_{0})\text{,}$ no clause fires at any integer $k\leq\min\{c\kappa,K\}\text{.}$ The dimension clause is silent since $k\leq K\text{.}$ For the crossing clause, note first that $\beta(k)\geq\Lambda/4\text{:}$ if $W\geq n$ this reads $\beta(k)\geq 2&gt;\tfrac{1}{4}=\Lambda/4\text{,}$ and if $W&lt;n\text{,}$ then $k\leq cW\Lambda$ with $c\leq 1$ gives</p>
<table id="S4.Ex36" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\beta(k)\ \geq\ \log\frac{n}{W\Lambda}\ =\ (\Lambda-1)-\log\Lambda\ \geq\ \frac{\Lambda}{4}\quad(\Lambda\geq 3),\qquad\beta(k)\ \geq\ 2\ \geq\ \frac{3}{4}\ &gt;\ \frac{\Lambda}{4}\quad(\Lambda&lt;3),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p31.3" class="ltx_p">the first branch because $\tfrac{3}{4}\Lambda\geq 1+\log\Lambda$ for $\Lambda\geq 3\text{.}$ Now split on $\min\{k,\beta(k)\}\text{.}$ If $k\leq\beta(k)\text{,}$ then, using $k\leq cW\Lambda\leq cW^{2}\Lambda$ and $A_{0}c=c_{B}/8\text{,}$</p>
<table id="S4.Ex37" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}\delta_{k}\ \geq\ c_{B}\,\sigma^{2}W^{2}\beta(k)\ \geq\ \frac{c_{B}}{4}\,\sigma^{2}W^{2}\Lambda\ &gt;\ A_{0}\sigma^{2}\,cW^{2}\Lambda\ \geq\ A_{0}\sigma^{2}k.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p31.4" class="ltx_p">If $k&gt;\beta(k)\text{,}$ then</p>
<table id="S4.Ex38" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V^{2}\delta_{k}\ \geq\ c_{B}\,\sigma^{2}\,\frac{W^{2}\beta(k)^{2}}{k}\ \geq\ \frac{c_{B}}{16}\,\sigma^{2}\,\frac{\kappa^{2}}{k}\ &gt;\ A_{0}\sigma^{2}k,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p31.5" class="ltx_p">the last step because $k\leq c\kappa$ and $c=c_{B}/(8A_{0})&lt;\sqrt{c_{B}}/(4\sqrt{A_{0}})\text{,}$ so that $k^{2}\leq c^{2}\kappa^{2}&lt;\tfrac{c_{B}}{16A_{0}}\kappa^{2}\text{.}$ Hence $k_{0}&gt;\min\{c\kappa,K\}\text{.}$</p>
</div>
<div id="S4a.p32" class="ltx_para">
<p id="S4a.p32.1" class="ltx_p">Combining the two tests: if $\kappa\leq K\text{,}$ then $c\kappa&lt;k_{0}\leq\lceil\kappa\rceil\leq 2\kappa\text{,}$ so $\sigma^{2}k_{0}\asymp\sigma^{2}\kappa=\sigma^{2}\min\{W\Lambda,n\}\text{,}$ using $\kappa\leq K\leq n\text{;}$ if $\kappa&gt;K\text{,}$ then $k_{0}&gt;\min\{c\kappa,K\}\geq cK$ and $k_{0}\leq K+1\leq 2K\text{,}$ so $\sigma^{2}k_{0}\asymp\sigma^{2}K\asymp\sigma^{2}n\asymp\sigma^{2}\min\{W\Lambda,n\}\text{,}$ using $n\leq 2e^{2}K\text{.}$ In both regimes</p>
<table id="S4.Ex39" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sigma^{2}k_{0}\ \asymp\ \sigma^{2}\min\{W\Lambda,\ n\},\quad\text{hence}\quad\min\{V^{2}h,\ \sigma^{2}k_{0}\}\ \asymp\ \sigma^{2}\min\{W^{2}h,\ W\Lambda,\ n\}\ =\ F,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p32.2" class="ltx_p">which proves the corollary for $W&gt;1\text{.}$
∎</p>
</div>
<div id="S4a.p33" class="ltx_para">
<p id="S4a.p33.1" class="ltx_p">It remains to prove the profile bounds (5.8) for the broom $T_{L}$ of Section 5, the handle $o=v_{0},\dots,v_{L}$ with $m$ leaf children at $v_{L}\text{,}$ so that $h_{T_{L}}=L+1\text{.}$ Its ancestor-covering numbers were computed in (5.7) there: $N^{\uparrow}_{T}(0)=n\text{,}$ and $N^{\uparrow}_{T}(q)=\lceil(L+2)/(q+1)\rceil$ for integers $1\leq q\leq L\text{.}$</p>
</div>
<div id="S4.Thmlemma3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmlemma3.2" class="ltx_text ltx_font_bold">Lemma S.4.3</span></span><span id="S4.Thmlemma3.3" class="ltx_text ltx_font_bold"> (Broom profile).</span></h6>
<div id="S4.Thmlemma3.p1" class="ltx_para">
<p id="S4.Thmlemma3.p1.1" class="ltx_p"><span id="S4.Thmlemma3.p1.1.1" class="ltx_text ltx_font_italic">For the broom $T_{L}$ with $L\geq 1$ and every integer $k\geq 1\text{,}$</span></p>
<table id="S4.Ex40" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\delta_{k}(T_{L})\ \leq\ \max\Bigl\{1,\ \frac{2(L+2)}{ek^{2}}\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.Thmlemma3.p1.2" class="ltx_p"><span id="S4.Thmlemma3.p1.2.1" class="ltx_text ltx_font_italic">and whenever $k\leq(L+2)/(2e)\text{,}$</span></p>
<table id="S4.Ex41" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\delta_{k}(T_{L})\ \geq\ \frac{L+2}{2ek^{2}}\,.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4a.p34" class="ltx_para">
<p id="S4a.p34.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S4a.p35" class="ltx_para">
<p id="S4a.p35.1" class="ltx_p">By the discrete formula (2.3), with $h_{T_{L}}=L+1\text{,}$</p>
<table id="S4.Ex42" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{k}(T_{L})\ =\ \max_{0\leq q\leq L}\ (q+1)\,\min\Bigl\{k,\ \Bigl[\log\frac{N^{\uparrow}_{T}(q)}{k}\Bigr]_{+}\Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S4a.p36" class="ltx_para">
<p id="S4a.p36.1" class="ltx_p"><em id="S4a.p36.1.1" class="ltx_emph ltx_font_italic">Upper bound.</em> The term at $q=0$ is at most $k$ and contributes at most $1$ to $\delta_{k}=\alpha_{k}/k\text{.}$ Consider $1\leq q\leq L$ with a nonvanishing term and put $y:=q+1\text{.}$ Then $\lceil(L+2)/y\rceil&gt;k\text{,}$ hence $(L+2)/y&gt;k\text{,}$ since a real number at most the integer $k$ has ceiling at most $k\text{;}$ consequently</p>
<table id="S4.Ex43" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N^{\uparrow}_{T}(q)\ &lt;\ \frac{L+2}{y}+1\ &lt;\ \frac{2(L+2)}{y}\,,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p36.2" class="ltx_p">and the term is at most</p>
<table id="S4.Ex44" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$y\,\log\frac{2(L+2)}{ky}\ \leq\ \sup_{u&gt;0}\ u\log\frac{A}{u}\ =\ \frac{A}{e}\,,\qquad A:=\frac{2(L+2)}{k}\,,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p36.3" class="ltx_p">the supremum attained at $u=A/e\text{.}$ Hence $\alpha_{k}\leq\max\{k,\ 2(L+2)/(ek)\}\text{,}$ and dividing by $k$ proves the upper bound.</p>
</div>
<div id="S4a.p37" class="ltx_para">
<p id="S4a.p37.1" class="ltx_p"><em id="S4a.p37.1.1" class="ltx_emph ltx_font_italic">Lower bound.</em> Set $x:=(L+2)/(ek)\text{,}$ at least $2$ in the stated range, and $y:=\lfloor x\rfloor\text{,}$ so that $y\geq 2$ and $y&gt;x-1\geq x/2\text{.}$ The radius $q:=y-1$ lies in $[1,L]\text{:}$ $q\geq 1$ since $y\geq 2\text{,}$ and $q\leq L$ since $y\leq x\leq(L+2)/e&lt;L+1$ for every $L\geq 1\text{.}$ Then</p>
<table id="S4.Ex45" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N^{\uparrow}_{T}(q)\ =\ \Bigl\lceil\frac{L+2}{y}\Bigr\rceil\ \geq\ \frac{L+2}{y}\ \geq\ \frac{L+2}{x}\ =\ ek,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p37.2" class="ltx_p">so $[\log(N^{\uparrow}_{T}(q)/k)]_{+}\geq 1\text{,}$ and the term at $q$ is at least $y\cdot\min\{k,1\}=y\geq x/2\text{.}$ Hence $\alpha_{k}\geq(L+2)/(2ek)\text{,}$ and dividing by $k$ proves the lower bound.
∎</p>
</div>
<div id="S4a.p38" class="ltx_para">
<p id="S4a.p38.1" class="ltx_p">Four computations from the lower-bound proof of Theorem 5 remain, in the notation fixed there: $V=L^{1/4}\text{,}$ $\sigma=1\text{,}$ $m\geq e^{20L^{5/2}}\text{,}$ and the statistics $W=\sum_{j=1}^{L}Z_{v_{j}}\text{,}$ $Q=\sum_{j=1}^{L}[Z_{v_{j}}]_{+}^{2}\text{,}$ $M=\max_{1\leq i\leq m}Z_{w_{i}}\text{.}$</p>
</div>
<div id="S4a.p39" class="ltx_para">
<p id="S4a.p39.1" class="ltx_p"><em id="S4a.p39.1.1" class="ltx_emph ltx_font_italic">The covering counts (5.7).</em> For the lower bound, the root-to-leaf path $v_{0},\dots,v_{L},w_{1}$ has $L+2$ vertices; an ancestor center on it covers at most $j+1$ consecutive ones, and a center at any other leaf covers none of them, so $N^{\uparrow}_{T}(j)\geq\lceil(L+2)/(j+1)\rceil\text{.}$ For the upper bound, the single center $v_{L+1-j}$ covers $v_{L+1-j},\dots,v_{L}$ together with every leaf, each at distance exactly $j\text{,}$ and $\lceil(L-j+1)/(j+1)\rceil$ further centers along the prefix $v_{0},\dots,v_{L-j}$ complete an ancestor $j$-net; the total is $1+\lceil(L-j+1)/(j+1)\rceil=\lceil(L+2)/(j+1)\rceil\text{.}$</p>
</div>
<div id="S4a.p40" class="ltx_para">
<p id="S4a.p40.1" class="ltx_p"><em id="S4a.p40.1.1" class="ltx_emph ltx_font_italic">The cap (5.3).</em> For $h_{j}\geq 0$ the handle term obeys $2Z_{v_{j}}h_{j}-h_{j}^{2}\leq[Z_{v_{j}}]_{+}^{2}\text{:}$ the left side is nonpositive when $Z_{v_{j}}\leq 0\text{,}$ and equals $Z_{v_{j}}^{2}-(h_{j}-Z_{v_{j}})^{2}$ otherwise. The leaf part is at most $2M\sum_{i}\ell_{i}\leq 2Mh_{L}\leq MV$ by (5.1), the last step because the case under consideration has $h_{L}\leq V/2\text{.}$</p>
</div>
<div id="S4a.p41" class="ltx_para">
<p id="S4a.p41.1" class="ltx_p"><em id="S4a.p41.1.1" class="ltx_emph ltx_font_italic">The forcing event $E=\{W\geq-2\sqrt{L}\}\cap\{Q\leq 2L\}\cap\{M\geq 4L^{5/4}\}$ has probability at least $\tfrac{3}{8}\text{.}$</em> On $E\text{,}$</p>
<table id="S4.Ex46" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(L+1)V-2W+\frac{Q}{V}\ \leq\ L^{5/4}+L^{1/4}+4L^{1/2}+2L^{3/4}\ &lt;\ 4L^{5/4}\ \leq\ M,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p41.2" class="ltx_p">the middle inequality being equivalent to $L^{-1}+4L^{-3/4}+2L^{-1/2}&lt;3\text{,}$ whose left side is decreasing in $L$ and below $3$ at $L=4\text{;}$ so the forcing inequality (5.4) holds on $E\text{.}$ Since $W\sim N(0,L)\text{,}$ Markov’s inequality applied to $W^{2}$ gives $\mathbb{P}(W&lt;-2\sqrt{L})\leq\tfrac{1}{4}\text{;}$ since $\mathbb{E}Q=L/2\text{,}$ by $\mathbb{E}[Z_{v_{j}}]_{+}^{2}=\tfrac{1}{2}\text{,}$ the same inequality gives $\mathbb{P}(Q&gt;2L)\leq\tfrac{1}{4}\text{;}$ hence $\mathbb{P}\{W\geq-2\sqrt{L},\ Q\leq 2L\}\geq\tfrac{1}{2}\text{.}$ For the leaves, set $t:=4L^{5/4}$ and integrate the standard normal density, decreasing on $[t,t+t^{-1}]\text{,}$ over that interval:</p>
<table id="S4.Ex47" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{P}\bigl(Z_{w_{1}}\geq t\bigr)\ \geq\ \frac{1}{t\sqrt{2\pi}}\,e^{-(t+t^{-1})^{2}/2}\ \geq\ c_{G}\,L^{-5/4}\,e^{-8L^{5/2}},\qquad c_{G}:=\frac{e^{-33/32}}{4\sqrt{2\pi}}\ ,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p41.3" class="ltx_p">the exponent being $\tfrac{1}{2}t^{2}+1+\tfrac{1}{2}t^{-2}\leq 8L^{5/2}+\tfrac{33}{32}$ by $t^{2}=16L^{5/2}\geq 16\text{.}$ Multiplying by $m\geq e^{20L^{5/2}}\text{,}$</p>
<table id="S4.Ex48" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$m\,\mathbb{P}\bigl(Z_{w_{1}}\geq t\bigr)\ \geq\ c_{G}\,L^{-5/4}\,e^{12L^{5/2}}\ \geq\ \log 4,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4a.p41.4" class="ltx_p">the middle expression being increasing in $L$ and, at $L=1\text{,}$ equal to $c_{G}e^{12}\geq e^{12-33/32-3}\geq e^{7}\text{,}$ using $4\sqrt{2\pi}\leq e^{3}\text{.}$ The leaves are independent of one another, so $\mathbb{P}(M&lt;t)=(1-\mathbb{P}(Z_{w_{1}}\geq t))^{m}\leq e^{-m\mathbb{P}(Z_{w_{1}}\geq t)}\leq\tfrac{1}{4}\text{,}$ and independent of the handle, whence $\mathbb{P}(E)\geq\tfrac{1}{2}\cdot\tfrac{3}{4}=\tfrac{3}{8}\text{.}$</p>
</div>
<div id="S4a.p42" class="ltx_para">
<p id="S4a.p42.1" class="ltx_p"><em id="S4a.p42.1.1" class="ltx_emph ltx_font_italic">The crossing index satisfies $k_{0}\asymp\sqrt{L}\text{.}$</em> Set $\kappa:=(V^{2}(L+2)/(2eA_{0}))^{1/3}\text{,}$ which is $\asymp\sqrt{L}$ since $V^{2}=\sqrt{L}\text{.}$ Every integer $k&lt;\kappa$ lies in the lower-bound range of <a href="#S4.Thmlemma3" title="Lemma S.4.3 (Broom profile). ‣ S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.4.3</span></a>: $(2e)^{2}\sqrt{L}\leq A_{0}(L+2)^{2}$ gives $\kappa\leq(L+2)/(2e)\text{,}$ and there $V^{2}\delta_{k}\geq V^{2}(L+2)/(2ek^{2})&gt;A_{0}k\text{,}$ the strict inequality being $k^{3}&lt;\kappa^{3}$ rearranged, while $n\geq e^{20L^{5/2}}$ keeps the dimension clause of (1.5) silent; hence $k_{0}\geq\kappa\text{.}$ At $k_{+}:=\lceil 4^{1/3}\kappa\rceil$ the upper bound of <a href="#S4.Thmlemma3" title="Lemma S.4.3 (Broom profile). ‣ S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.4.3</span></a> gives $V^{2}\delta_{k_{+}}\leq\max\{V^{2},2V^{2}(L+2)/(ek_{+}^{2})\}\leq A_{0}k_{+}\text{,}$ the first branch since $A_{0}k_{+}\geq A_{0}^{2/3}(2/e)^{1/3}\sqrt{L}\geq V^{2}$ and the second since $k_{+}^{3}\geq 4\kappa^{3}\text{;}$ so the crossing fires by $k_{+}$ and $\kappa\leq k_{0}\leq\lceil 4^{1/3}\kappa\rceil\text{,}$ whence $k_{0}\asymp\sqrt{L}\text{.}$ Finally $\kappa\leq(L+2)/(2e)$ gives $k_{0}\leq\lceil 4^{1/3}\kappa\rceil\leq L+3\leq\sqrt{L}\,(L+1)=V^{2}H_{T_{L}}\text{,}$ so the minimum in Theorem 1 is the information branch and $R^{*}_{T_{L}}(L^{1/4},1)\asymp k_{0}\asymp\sqrt{L}\text{.}$</p>
</div>
</section>
<section id="S5a" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="exact-evaluation-of-the-aggregate"><span class="ltx_tag ltx_tag_section">S.5 </span>Exact Evaluation of the Aggregate</h2>

<div id="S5a.p1" class="ltx_para">
<p id="S5a.p1.1" class="ltx_p">This section proves the statements deferred from Sections 4.1 and 4.2: the bound on the normalizing sum of the prior, the completion of the proof of Lemma 4.1, the risk of the three elementary branches of (4.3), the correctness and cost of the exact evaluation of the aggregate (4.2), and the batched evaluation behind the instance sentence of Section 4.2, including the softly linear evaluation on stars.</p>
</div>
<div id="S5a.p2" class="ltx_para">
<p id="S5a.p2.1" class="ltx_p">Throughout, $K:=\lfloor n/C_{\star}\rfloor\text{;}$ except in the treatment of the elementary branches, $k$ is an integer with $2\leq k\leq K\text{.}$ The active support $A_{k}\text{,}$ the charges $\widetilde{\omega}\text{,}$ the code length $\Gamma\text{,}$ and the level weights $m_{j}=2^{j}$ for $0\leq j\leq J$ are those of Section 3.1; $\mathcal{X}_{k}$ is the class (4.1) of integer states of Section 4.1; and, as in Section 4.2 there, $\varphi_{v}(x)=e^{-(Y_{v}-bx)^{2}/(4\sigma^{2})}$ with the shorthand $b:=V/k\text{.}$</p>
</div>
<div id="S5.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma S.5.1</span></span><span id="S5.Thmlemma1.3" class="ltx_text ltx_font_bold"> (Normalizing sum).</span></h6>
<div id="S5.Thmlemma1.p1" class="ltx_para">
<p id="S5.Thmlemma1.p1.1" class="ltx_p"><span id="S5.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">For every integer $2\leq k\leq K\text{,}$</span></p>
<table id="S5.Ex1a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{x\in\mathcal{X}_{k}}e^{-2\Gamma(x)}\ \leq\ e^{k}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S5a.p3" class="ltx_para">
<p id="S5a.p3.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S5a.p4" class="ltx_para">
<p id="S5a.p4.1" class="ltx_p">The map $x\mapsto z$ is injective on state vectors, since the subtree sums $x_{v}=\sum_{u\succeq v}z_{u}$ recover $x\text{,}$ and $\Gamma(x)$ depends only on $z\text{.}$ Dropping the constraints $x_{o}=k$ and $0\leq x_{v}\leq 3k$ therefore bounds the sum by a product over the support:</p>
<table id="S5.Ex2a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{x\in\mathcal{X}_{k}}e^{-2\Gamma(x)}\ \leq\ \sum_{z\in\mathbb{Z}^{A_{k}}}\prod_{v\in A_{k}}e^{-2(|z_{v}|+\widetilde{\omega}(v)\mathbf{1}\{z_{v}\neq 0\})}\ =\ \prod_{v\in A_{k}}\Bigl(1+\tfrac{2}{e^{2}-1}\,e^{-2\widetilde{\omega}(v)}\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p4.2" class="ltx_p">the factor at $v$ being $1+e^{-2\widetilde{\omega}(v)}\cdot 2\sum_{t\geq 1}e^{-2t}\text{,}$ with $2\sum_{t\geq 1}e^{-2t}=\tfrac{2}{e^{2}-1}\text{.}$ The free level $R_{0}\text{,}$ where $\widetilde{\omega}=0\text{,}$ has $|R_{0}|\leq ke^{m_{0}}=ek$ vertices by <a href="#S2.Thmlemma1a" title="Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.1</span></a>(<a href="#S2.I1.i2a" title="Item 2 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>), and $\log(1+\tfrac{2}{e^{2}-1})\leq\tfrac{3}{10}\text{,}$ so it contributes at most $\tfrac{3}{10}ek&lt;0.82\,k$ to the logarithm. The charged vertices split into the groups $G_{j}:=\{v\in A_{k}\setminus R_{0}:\ \omega(v)=m_{j}\}\subseteq R_{j}\text{,}$ $1\leq j\leq J\text{,}$ with $|G_{j}|\leq 2ke^{m_{j}}$ by <a href="#S2.Thmlemma1a" title="Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.1</span></a>(<a href="#S2.I1.i3a" title="Item 3 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>); since $\log(1+y)\leq y\text{,}$ their contribution is at most</p>
<table id="S5.Ex3a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{j\geq 1}2ke^{m_{j}}\cdot\frac{2}{e^{2}-1}\,e^{-2m_{j}}\ =\ \frac{4k}{e^{2}-1}\sum_{j\geq 1}e^{-2^{j}}\ \leq\ \frac{4k}{e^{2}-1}\cdot 0.16\ &lt;\ 0.11\,k,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p4.3" class="ltx_p">using $\sum_{j\geq 1}e^{-2^{j}}&lt;e^{-2}+e^{-4}+2e^{-8}&lt;0.16\text{.}$ The logarithm of the product is below $0.93\,k\text{.}$
∎</p>
</div>
<div id="S5a.p5" class="ltx_para">
<p id="S5a.p5.1" class="ltx_p">In the setting of Lemma 4.1, write</p>
<table id="S5.Ex4a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{Z}(y)\ :=\ \sum_{g\in F}\pi_{g}\,e^{-\|y-g\|_{2}^{2}/(4\sigma^{2})}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p5.2" class="ltx_p">for the normalizing sum of the weights, positive and smooth on $\mathbb{R}^{N}\text{.}$</p>
</div>
<div id="S5a.p6" class="ltx_para">
<p id="S5a.p6.1" class="ltx_p"><em class="ltx_title_proof">Completion of the proof of Lemma 4.1.</em></p>
</div>
<div id="S5a.p7" class="ltx_para">
<p id="S5a.p7.1" class="ltx_p"><em id="S5a.p7.1.1" class="ltx_emph ltx_font_italic">The Jacobian.</em> The logarithm of a weight is $\log\pi_{f}-\|y-f\|_{2}^{2}/(4\sigma^{2})-\log\mathcal{Z}(y)\text{;}$ differentiating it in $y_{i}$ gives</p>
<table id="S5.Ex5a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{\partial\log\widehat{\pi}_{f}}{\partial y_{i}}\ =\ -\frac{y_{i}-f_{i}}{2\sigma^{2}}+\sum_{g\in F}\widehat{\pi}_{g}(y)\,\frac{y_{i}-g_{i}}{2\sigma^{2}}\ =\ \frac{f_{i}-\widehat{f}_{i}(y)}{2\sigma^{2}}\ ,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p7.2" class="ltx_p">that is, $\partial\widehat{\pi}_{f}/\partial y_{i}=\widehat{\pi}_{f}\,(f_{i}-\widehat{f}_{i})/(2\sigma^{2})\text{.}$ Multiplying by $f_{j}$ and summing over $f\text{,}$</p>
<table id="S5.Ex6a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{\partial\widehat{f}_{j}}{\partial y_{i}}\ =\ \frac{1}{2\sigma^{2}}\Bigl(\sum_{f\in F}\widehat{\pi}_{f}\,f_{i}f_{j}-\widehat{f}_{i}\,\widehat{f}_{j}\Bigr)\ =\ \frac{1}{2\sigma^{2}}\operatorname{Cov}_{\widehat{\pi}(y)}(f_{i},f_{j}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p7.3" class="ltx_p">the Jacobian identity of the main-text sketch; taking $i=j$ and summing,</p>
<table id="S5.E1a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$2\sigma^{2}\operatorname{div}\widehat{f}_{\pi}(y)\ =\ \operatorname{tr}\operatorname{Cov}_{\widehat{\pi}(y)}(f)\ =\ \sum_{f\in F}\widehat{\pi}_{f}(y)\,\bigl\|f-\widehat{f}_{\pi}(y)\bigr\|_{2}^{2}\ \geq\ 0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.1)</span></td></tr></tbody>
</table>
</div>
<div id="S5a.p8" class="ltx_para">
<p id="S5a.p8.1" class="ltx_p"><em id="S5a.p8.1.1" class="ltx_emph ltx_font_italic">The domain of Stein’s identity.</em> The aggregate takes values in the convex hull of the finite set $F\text{,}$ so it is bounded; its partial derivatives are posterior covariances of coordinates of $F\text{,}$ bounded uniformly in $y\text{;}$ and both are smooth, since $\mathcal{Z}&gt;0$ everywhere. For such a map, Stein’s identity <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib35" title="" class="ltx_ref">Stein, 1981</a>)</cite> gives</p>
<table id="S5.Ex7a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}_{\mu}\bigl\|\widehat{f}_{\pi}(Y)-\mu\bigr\|_{2}^{2}\ =\ \mathbb{E}\bigl\|\widehat{f}_{\pi}(Y)-Y\bigr\|_{2}^{2}+2\sigma^{2}\,\mathbb{E}\operatorname{div}\widehat{f}_{\pi}(Y)\ -\ N\sigma^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S5a.p9" class="ltx_para">
<p id="S5a.p9.1" class="ltx_p"><em id="S5a.p9.1.1" class="ltx_emph ltx_font_italic">The cancellation.</em> At fixed $y\text{,}$ expanding $\|y-f\|_{2}^{2}$ around $\widehat{f}_{\pi}(y)$ and averaging under $\widehat{\pi}(y)$ kills the cross term, since $\sum_{f}\widehat{\pi}_{f}\,(f-\widehat{f}_{\pi})=0\text{:}$</p>
<table id="S5.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{f\in F}\widehat{\pi}_{f}(y)\,\|y-f\|_{2}^{2}\ =\ \bigl\|y-\widehat{f}_{\pi}(y)\bigr\|_{2}^{2}+\sum_{f\in F}\widehat{\pi}_{f}(y)\,\bigl\|f-\widehat{f}_{\pi}(y)\bigr\|_{2}^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p9.2" class="ltx_p">The last sum is $2\sigma^{2}\operatorname{div}\widehat{f}_{\pi}(y)$ by <a href="#S5.E1a" title="In S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.1</span></a>, so substituting the expansion into Stein’s identity cancels the divergence terms and leaves the risk identity of the main-text sketch.</p>
</div>
<div id="S5a.p10" class="ltx_para">
<p id="S5a.p10.1" class="ltx_p"><em id="S5a.p10.1.1" class="ltx_emph ltx_font_italic">The variational bound.</em> The relative entropy of probability vectors on $F$ is $\operatorname{KL}(\rho\,\|\,\pi):=\sum_{f}\rho_{f}\log(\rho_{f}/\pi_{f})\text{,}$ with $0\log 0:=0\text{.}$ For any such $\rho\text{,}$ inserting the definition of $\widehat{\pi}(y)$ gives the identity</p>
<table id="S5.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{f\in F}\rho_{f}\,\|y-f\|_{2}^{2}+4\sigma^{2}\operatorname{KL}(\rho\,\|\,\pi)\ =\ 4\sigma^{2}\operatorname{KL}\bigl(\rho\,\|\,\widehat{\pi}(y)\bigr)\ -\ 4\sigma^{2}\log\mathcal{Z}(y),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p10.2" class="ltx_p">so the left side is minimized exactly at $\rho=\widehat{\pi}(y)\text{.}$ Comparing the minimizer with the point mass at $f_{0}\text{,}$ and dropping the nonnegative divergence $\operatorname{KL}(\widehat{\pi}(y)\,\|\,\pi)$ from the minimum,</p>
<table id="S5.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{f\in F}\widehat{\pi}_{f}(y)\,\|y-f\|_{2}^{2}\ \leq\ \|y-f_{0}\|_{2}^{2}+4\sigma^{2}\log\frac{1}{\pi_{f_{0}}}\ ,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p10.3" class="ltx_p">the pathwise bound of the main body, whose expectation completes the proof there.
∎</p>
</div>
<div id="S5a.p11" class="ltx_para">
<p id="S5a.p11.1" class="ltx_p">The elementary branches of (4.3) are next. Their analysis rests on two facts: the root-corrected observation matches $\mu(o)=V$ exactly, and $Vp_{o}$ is within $V\sqrt{h_{T}}$ of every body point.</p>
</div>
<div id="S5.Thmlemma2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmlemma2.2" class="ltx_text ltx_font_bold">Lemma S.5.2</span></span><span id="S5.Thmlemma2.3" class="ltx_text ltx_font_bold"> (Elementary branches).</span></h6>
<div id="S5.Thmlemma2.p1" class="ltx_para">
<p id="S5.Thmlemma2.p1.1" class="ltx_p"><span id="S5.Thmlemma2.p1.1.1" class="ltx_text ltx_font_italic">Write $k:=k_{\mathrm{alg}}(T,V,\sigma)\text{.}$ In each of the three elementary branches of (4.3),</span></p>
<table id="S5.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sup_{\mu\in\mathcal{F}_{V}(T)}\mathbb{E}_{\mu}\|\widehat{\mu}-\mu\|_{2}^{2}\ \leq\ C\min\{V^{2}H_{T},\ \sigma^{2}k\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S5a.p12" class="ltx_para">
<p id="S5a.p12.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S5a.p13" class="ltx_para">
<p id="S5a.p13.1" class="ltx_p">For every $\mu=\sum_{u}\lambda_{u}\,Vp_{u}\in\mathcal{F}_{V}(T)\text{,}$ convexity of the norm and Lemma 2.2 give $\|\mu-Vp_{o}\|_{2}\leq\max_{u}\|Vp_{u}-Vp_{o}\|_{2}=V\sqrt{h_{T}}\text{.}$</p>
</div>
<div id="S5a.p14" class="ltx_para">
<p id="S5a.p14.1" class="ltx_p"><em id="S5a.p14.1.1" class="ltx_emph ltx_font_italic">Diameter branch ($V^{2}H_{T}\leq\sigma^{2}k$).</em> The estimator is the constant $Vp_{o}\text{,}$ so its risk is at most $V^{2}h_{T}\leq V^{2}H_{T}\text{,}$ which is the minimum under the branch condition.</p>
</div>
<div id="S5a.p15" class="ltx_para">
<p id="S5a.p15.1" class="ltx_p"><em id="S5a.p15.1.1" class="ltx_emph ltx_font_italic">Dimension branch ($V^{2}H_{T}&gt;\sigma^{2}k$ and $k&gt;K$).</em> Since $k\leq K+1$ always, $k=K+1\text{,}$ and $K=\lfloor n/C_{\star}\rfloor$ gives $n&lt;C_{\star}(K+1)=C_{\star}k\text{.}$ The root coordinate of $\widetilde{Y}$ is exact, so</p>
<table id="S5.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}_{\mu}\|\widetilde{Y}-\mu\|_{2}^{2}\ =\ (n-1)\,\sigma^{2}\ &lt;\ C_{\star}\,\sigma^{2}k,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p15.2" class="ltx_p">and the minimum is $\sigma^{2}k$ under the branch condition.</p>
</div>
<div id="S5a.p16" class="ltx_para">
<p id="S5a.p16.1" class="ltx_p"><em id="S5a.p16.1.1" class="ltx_emph ltx_font_italic">First-budget branch ($V^{2}H_{T}&gt;\sigma^{2}k$ and $k=1\leq K$).</em> Here $n\geq C_{\star}\text{,}$ so $n\geq 2\text{,}$ and, as in Section 3.3, every ancestor $r$-net with $r&lt;h_{T}$ has at least two elements: the root lies in every net and covers no deepest vertex. Hence $N^{\uparrow}_{T}(r)\geq 2$ for all $r&lt;h_{T}\text{,}$ and letting $r\uparrow h_{T}$ in (1.4) gives $\alpha_{1}\geq h_{T}\log 2\text{.}$ The dimension clause of (2.2) is silent at $k=1\text{,}$ since $1\leq K\text{,}$ so the surrogate crossing clause fired there, $V^{2}\overline{\delta}_{1}\leq 2A_{0}\sigma^{2}\text{,}$ and with Lemma 2.3,</p>
<table id="S5.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sup_{\mu}\|\mu-Vp_{o}\|_{2}^{2}\ \leq\ V^{2}h_{T}\ \leq\ \frac{V^{2}\alpha_{1}}{\log 2}\ =\ \frac{V^{2}\delta_{1}}{\log 2}\ \leq\ \frac{V^{2}\overline{\delta}_{1}}{\log 2}\ \leq\ \frac{2A_{0}}{\log 2}\,\sigma^{2};$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p16.2" class="ltx_p">the minimum is $\sigma^{2}$ under the branch condition.
∎</p>
</div>
<div id="S5a.p17" class="ltx_para">
<p id="S5a.p17.1" class="ltx_p">The rest of the section evaluates the interior branch. Fix $2\leq k\leq K$ and collect the prior into local kernels: for $z\in\mathbb{Z}$ put</p>
<table id="S5.E2a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\kappa_{v}(z)\ :=\ \begin{cases}1,&amp;z=0,\\ e^{-2\widetilde{\omega}(v)}\,e^{-2|z|},&amp;z\neq 0\ \text{and}\ v\in A_{k},\\ 0,&amp;z\neq 0\ \text{and}\ v\notin A_{k}.\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.2)</span></td></tr></tbody>
</table>
<p id="S5a.p17.2" class="ltx_p">For a state vector $x\in\{0,\dots,3k\}^{\mathsf{V}}$ with leaks $z_{v}=x_{v}-\sum_{c\in\operatorname{ch}(v)}x_{c}\text{,}$ the product $\prod_{v}\kappa_{v}(z_{v})$ equals $e^{-2\Gamma(x)}$ when the leaks vanish off $A_{k}$ and is zero otherwise. The denominator of (4.2) is therefore the total <em id="S5a.p17.2.1" class="ltx_emph ltx_font_italic">weight</em> $\prod_{v}\kappa_{v}(z_{v})\,\varphi_{v}(x_{v})$ of all state vectors with $x_{o}=k\text{,}$ and it is positive: the vector with $x_{o}=k$ and all other states zero has its one leak at the root, where $\widetilde{\omega}(o)=0$ because $o\in R_{0}\text{,}$ so its weight is $e^{-2k}\varphi_{o}(k)\prod_{v\neq o}\varphi_{v}(0)&gt;0\text{.}$ In the same terms, the coefficients of the message (4.5) are</p>
<table id="S5.E3a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$P_{v}[x]\ =\ \sum_{\begin{subarray}{c}x^{\prime}\in\{0,\dots,3k\}^{T_{v}}\\ x^{\prime}_{v}=x\end{subarray}}\ \prod_{w\in T_{v}}\kappa_{w}(z^{\prime}_{w})\,\varphi_{w}(x^{\prime}_{w}),\qquad z^{\prime}_{w}:=x^{\prime}_{w}-\textstyle\sum_{c\in\operatorname{ch}(w)}x^{\prime}_{c},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.3)</span></td></tr></tbody>
</table>
<p id="S5a.p17.3" class="ltx_p">the leaks computed within $T_{v}\text{.}$</p>
</div>
<div id="S5a.p18" class="ltx_para">
<p id="S5a.p18.1" class="ltx_p">Messages are polynomials of degree at most $3k\text{,}$ but the product of many children’s messages is not, and its degree must not be allowed to grow with their number. The device is a pair representation: a polynomial $F(\zeta)=\sum_{i\geq 0}F[i]\zeta^{i}$ with nonnegative coefficients is carried as its truncation $F_{0}(\zeta):=\sum_{i\leq 3k}F[i]\zeta^{i}$ together with its <em id="S5a.p18.1.1" class="ltx_emph ltx_font_italic">tail</em></p>
<table id="S5.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau_{F}\ :=\ \sum_{i&gt;3k}F[i]\,e^{-2(i-3k)},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p18.2" class="ltx_p">the evaluation of the high part at $e^{-2}\text{,}$ shifted to the cap. Messages have zero tail; tails arise along partial products of messages and stay scalars.</p>
</div>
<div id="S5.Thmlemma3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmlemma3.2" class="ltx_text ltx_font_bold">Lemma S.5.3</span></span><span id="S5.Thmlemma3.3" class="ltx_text ltx_font_bold"> (Product of pairs).</span></h6>
<div id="S5.Thmlemma3.p1" class="ltx_para">
<p id="S5.Thmlemma3.p1.1" class="ltx_p"><span id="S5.Thmlemma3.p1.1.1" class="ltx_text ltx_font_italic">Let $F,G$ be polynomials with nonnegative coefficients, of arbitrary degrees, given by their pairs. Then $(FG)_{0}$ is the truncation of $F_{0}G_{0}\text{,}$ and</span></p>
<table id="S5.E4a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau_{FG}\ =\ \sum_{q=3k+1}^{6k}[\zeta^{q}](F_{0}G_{0})\,e^{-2(q-3k)}\ +\ F_{0}(e^{-2})\,\tau_{G}\ +\ \tau_{F}\,G_{0}(e^{-2})\ +\ e^{-6k}\,\tau_{F}\,\tau_{G}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.4)</span></td></tr></tbody>
</table>
<p id="S5.Thmlemma3.p1.2" class="ltx_p"><span id="S5.Thmlemma3.p1.2.1" class="ltx_text ltx_font_italic">The pair of $FG$ is therefore computable from the pairs of $F$ and $G$ by one multiplication of two polynomials of degree at most $3k$ and $O(k)$ further operations.</span></p>
</div>
</div>
<div id="S5a.p19" class="ltx_para">
<p id="S5a.p19.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S5a.p20" class="ltx_para">
<p id="S5a.p20.1" class="ltx_p">For $q\leq 3k\text{,}$ $[\zeta^{q}](FG)=\sum_{i+j=q}F[i]G[j]$ involves only indices $i,j\leq 3k\text{,}$ which gives the truncation claim. In $\tau_{FG}=\sum_{i+j&gt;3k}F[i]G[j]e^{-2(i+j-3k)}\text{,}$ partition the index pairs according to whether $i\leq 3k$ and whether $j\leq 3k\text{.}$ The low–low pairs give the first term of <a href="#S5.E4a" title="In Lemma S.5.3 (Product of pairs). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.4</span></a>. The low–high pairs factor as $\sum_{i\leq 3k}F[i]e^{-2i}\cdot\sum_{j&gt;3k}G[j]e^{-2(j-3k)}=F_{0}(e^{-2})\tau_{G}\text{,}$ the high–low pairs symmetrically, and the high–high pairs as $e^{-6k}\tau_{F}\tau_{G}\text{,}$ since $e^{-2(i+j-3k)}=e^{-2(i-3k)}e^{-2(j-3k)}e^{-6k}\text{.}$ For the cost: the single multiplication $F_{0}G_{0}$ yields all coefficients through degree $6k\text{,}$ and every remaining ingredient of <a href="#S5.E4a" title="In Lemma S.5.3 (Product of pairs). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.4</span></a>, including the evaluations $F_{0}(e^{-2})$ and $G_{0}(e^{-2})\text{,}$ is $O(k)$ arithmetic on them.
∎</p>
</div>
<div id="S5a.p21" class="ltx_para">
<p id="S5a.p21.1" class="ltx_p">The recursion of Section 4.2 now takes its precise form. At each vertex the children’s messages are merged pairwise in the pair representation, and one local pass applies the observation weight and the prior kernel.</p>
</div>
<div id="S5.Thmlemma4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmlemma4.2" class="ltx_text ltx_font_bold">Lemma S.5.4</span></span><span id="S5.Thmlemma4.3" class="ltx_text ltx_font_bold"> (Message recursion).</span></h6>
<div id="S5.Thmlemma4.p1" class="ltx_para">
<p id="S5.Thmlemma4.p1.1" class="ltx_p"><span id="S5.Thmlemma4.p1.1.1" class="ltx_text ltx_font_italic">For $v\in\mathsf{V}$ let $Q_{v}(\zeta):=\prod_{c\in\operatorname{ch}(v)}P_{c}(\zeta)\text{,}$ an empty product being $1\text{,}$ with coefficients $Q_{v}[s]$ and tail $\tau_{v}\text{,}$ and set</span></p>
<table id="S5.Ex15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\psi^{-}_{x}\ :=\ \sum_{0\leq s&lt;x}e^{-2(x-s)}\,Q_{v}[s],\qquad\psi^{+}_{x}\ :=\ \sum_{s&gt;x}e^{-2(s-x)}\,Q_{v}[s]\qquad(0\leq x\leq 3k).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.Thmlemma4.p1.2" class="ltx_p"><span id="S5.Thmlemma4.p1.2.1" class="ltx_text ltx_font_italic">Then</span></p>
<table id="S5.E5a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$P_{v}[x]\ =\ \begin{cases}\varphi_{v}(x)\,Q_{v}[x],&amp;v\notin A_{k},\\[2.0pt] \varphi_{v}(x)\,\bigl(Q_{v}[x]+e^{-2\widetilde{\omega}(v)}(\psi^{-}_{x}+\psi^{+}_{x})\bigr),&amp;v\in A_{k},\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.5)</span></td></tr></tbody>
</table>
<p id="S5.Thmlemma4.p1.3" class="ltx_p"><span id="S5.Thmlemma4.p1.3.1" class="ltx_text ltx_font_italic">and the two sums obey the linear recurrences</span></p>
<table id="S5.E6a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\psi^{-}_{0}=0,\quad\psi^{-}_{x}=e^{-2}\bigl(Q_{v}[x-1]+\psi^{-}_{x-1}\bigr);\qquad\psi^{+}_{3k}=\tau_{v},\quad\psi^{+}_{x}=e^{-2}\bigl(Q_{v}[x+1]+\psi^{+}_{x+1}\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.6)</span></td></tr></tbody>
</table>
<p id="S5.Thmlemma4.p1.4" class="ltx_p"><span id="S5.Thmlemma4.p1.4.1" class="ltx_text ltx_font_italic">In particular the pair of $P_{v}$ is computed from the pairs of the
children’s messages by $(|\operatorname{ch}(v)|-1)_{+}$ products of pairs and $O(k)$
further operations, and $P_{o}[k]$ is the denominator of (4.2).</span></p>
</div>
</div>
<div id="S5a.p22" class="ltx_para">
<p id="S5a.p22.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S5a.p23" class="ltx_para">
<p id="S5a.p23.1" class="ltx_p">Assignments on the subtrees of distinct children are independent,
and weights multiply, so $Q_{v}[s]$ is the total weight of the
assignments on the child subtrees whose states at the children sum
to $s\text{;}$ here $s$ ranges over all of $\{0,1,\dots\}\text{,}$ and the pair of
$Q_{v}$ is assembled by <a href="#S5.Thmlemma3" title="Lemma S.5.3 (Product of pairs). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.3</span></a>. A state $x$ at $v$
completes such a family to an assignment on $T_{v}$ with local weight
$\varphi_{v}(x)\kappa_{v}(x-s)\text{,}$ so by <a href="#S5.E3a" title="In S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.3</span></a></p>
<table id="S5.Ex16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$P_{v}[x]\ =\ \varphi_{v}(x)\sum_{s\geq 0}\kappa_{v}(x-s)\,Q_{v}[s].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p23.2" class="ltx_p">If $v\notin A_{k}\text{,}$ the kernel forces $s=x\leq 3k\text{,}$ which is <a href="#S5.E5a" title="In Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.5</span></a>; child sums beyond $3k$ contribute nothing. If $v\in A_{k}\text{,}$ the kernel splits the sum at $s=x$ into $Q_{v}[x]+e^{-2\widetilde{\omega}(v)}(\psi^{-}_{x}+\psi^{+}_{x})$ with</p>
<table id="S5.Ex17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\psi^{+}_{x}\ =\ \sum_{x&lt;s\leq 3k}e^{-2(s-x)}Q_{v}[s]\ +\ e^{-2(3k-x)}\,\tau_{v},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p23.3" class="ltx_p">the high child sums entering exactly through the tail. The recurrences <a href="#S5.E6a" title="In Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.6</span></a> are immediate from the definitions; the seed $\psi^{+}_{3k}=\tau_{v}$ is the identity just displayed at $x=3k\text{.}$ Both passes cost $O(k)\text{,}$ as does applying <a href="#S5.E5a" title="In Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.5</span></a>, and the leaf base case ($Q_{v}\equiv 1$) is contained in the general one. At the root, <a href="#S5.E3a" title="In S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.3</span></a> with $x=k$ sums the weights of all state vectors with $x_{o}=k\text{,}$ which is the denominator of (4.2).
∎</p>
</div>
<div id="S5a.p24" class="ltx_para">
<p id="S5a.p24.1" class="ltx_p">The pruning and the chain compression described in Section 4.2 modify this recursion; neither changes the posterior.</p>
</div>
<div id="S5.Thmlemma5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmlemma5.2" class="ltx_text ltx_font_bold">Lemma S.5.5</span></span><span id="S5.Thmlemma5.3" class="ltx_text ltx_font_bold"> (Pruning and compression).</span></h6>
<div id="S5.Thmlemma5.p1" class="ltx_para">
<ol id="S5.I6" class="ltx_enumerate">
<li id="S5.I6.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S5.I6.i1.p1" class="ltx_para">
<p id="S5.I6.i1.p1.1" class="ltx_p"><span id="S5.I6.i1.p1.1.1" class="ltx_text ltx_font_italic">If </span>$T_{w}\cap A_{k}=\varnothing$<span id="S5.I6.i1.p1.1.2" class="ltx_text ltx_font_italic">, then every
state vector of nonzero weight vanishes on </span>$T_{w}$<span id="S5.I6.i1.p1.1.3" class="ltx_text ltx_font_italic">, and the subtree
contributes the factor </span>$\prod_{u\in T_{w}}\varphi_{u}(0)$<span id="S5.I6.i1.p1.1.4" class="ltx_text ltx_font_italic"> to every
weight; dropping it, and every other factor common to all
assignments, changes no posterior quantity. The estimator satisfies
</span>$\widehat{\mu}_{k}(u)=0$<span id="S5.I6.i1.p1.1.5" class="ltx_text ltx_font_italic"> for </span>$u\in T_{w}$<span id="S5.I6.i1.p1.1.6" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
<li id="S5.I6.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S5.I6.i2.p1" class="ltx_para">
<p id="S5.I6.i2.p1.1" class="ltx_p"><span id="S5.I6.i2.p1.1.1" class="ltx_text ltx_font_italic">Let </span>$\mathcal{C}$<span id="S5.I6.i2.p1.1.2" class="ltx_text ltx_font_italic"> be a maximal chain of
vertices not in </span>$A_{k}$<span id="S5.I6.i2.p1.1.3" class="ltx_text ltx_font_italic">, each having exactly one child whose subtree
meets </span>$A_{k}$<span id="S5.I6.i2.p1.1.4" class="ltx_text ltx_font_italic"> and each, except the lowest, followed in </span>$\mathcal{C}$<span id="S5.I6.i2.p1.1.5" class="ltx_text ltx_font_italic"> by
that child; write </span>$c_{\mathcal{C}}$<span id="S5.I6.i2.p1.1.6" class="ltx_text ltx_font_italic"> for that child of the lowest
vertex of </span>$\mathcal{C}$<span id="S5.I6.i2.p1.1.7" class="ltx_text ltx_font_italic">. Every state vector of nonzero weight is constant on
</span>$\mathcal{C}\cup\{c_{\mathcal{C}}\}$<span id="S5.I6.i2.p1.1.8" class="ltx_text ltx_font_italic">, and the chain contributes, after
the
state-independent factor
</span>$\exp(-\sum_{w\in\mathcal{C}}Y_{w}^{2}/(4\sigma^{2}))$<span id="S5.I6.i2.p1.1.9" class="ltx_text ltx_font_italic"> is dropped, the
diagonal kernel</span></p>
<table id="S5.E7a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$x\ \longmapsto\ \exp\Bigl(\frac{b\,x}{2\sigma^{2}}\sum_{w\in\mathcal{C}}Y_{w}\ -\ \frac{|\mathcal{C}|\,b^{2}x^{2}}{4\sigma^{2}}\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.7)</span></td></tr></tbody>
</table>
<p id="S5.I6.i2.p1.2" class="ltx_p"><span id="S5.I6.i2.p1.2.1" class="ltx_text ltx_font_italic">generated in </span>$O(k)$<span id="S5.I6.i2.p1.2.2" class="ltx_text ltx_font_italic"> operations from </span>$|\mathcal{C}|$<span id="S5.I6.i2.p1.2.3" class="ltx_text ltx_font_italic"> and
</span>$\sum_{w\in\mathcal{C}}Y_{w}$<span id="S5.I6.i2.p1.2.4" class="ltx_text ltx_font_italic">. The estimator satisfies
</span>$\widehat{\mu}_{k}(w)=\widehat{\mu}_{k}(c_{\mathcal{C}})$<span id="S5.I6.i2.p1.2.5" class="ltx_text ltx_font_italic"> for
</span>$w\in\mathcal{C}$<span id="S5.I6.i2.p1.2.6" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S5a.p25" class="ltx_para">
<p id="S5a.p25.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S5a.p26" class="ltx_para">
<p id="S5a.p26.1" class="ltx_p">For (<a href="#S5.I6.i1" title="Item 1 ‣ Lemma S.5.5 (Pruning and compression). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>): on $T_{w}$ all kernels force $z\equiv 0\text{,}$ so leaf-up induction gives $x\equiv 0$ on $T_{w}$ for every assignment of nonzero weight; the surviving factor is $\prod_{u\in T_{w}}\kappa_{u}(0)\varphi_{u}(0)$ as claimed. A factor common to every assignment multiplies numerator and denominator of each posterior expectation alike. Since $x_{u}=0$ with posterior probability one, $\widehat{\mu}_{k}(u)=b\,\mathbb{E}_{Y}[x_{u}]=0\text{.}$</p>
</div>
<div id="S5a.p27" class="ltx_para">
<p id="S5a.p27.1" class="ltx_p">For (<a href="#S5.I6.i2" title="Item 2 ‣ Lemma S.5.5 (Pruning and compression). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>): a vertex $w\in\mathcal{C}$ has $z_{w}=0$ and all of its child subtrees off the chain disjoint from $A_{k}\text{,}$ hence carrying state zero, so $x_{w}$ equals the state of its unique child toward $A_{k}\text{;}$ iterating down the chain, all these states equal $x_{c_{\mathcal{C}}}=:x\text{.}$ The chain’s likelihood factor is $\prod_{w\in\mathcal{C}}\varphi_{w}(x)\text{,}$ and expanding the exponent,</p>
<table id="S5.Ex18" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$-\sum_{w\in\mathcal{C}}\frac{(Y_{w}-bx)^{2}}{4\sigma^{2}}\ =\ -\sum_{w\in\mathcal{C}}\frac{Y_{w}^{2}}{4\sigma^{2}}\ +\ \frac{bx}{2\sigma^{2}}\sum_{w\in\mathcal{C}}Y_{w}\ -\ \frac{|\mathcal{C}|\,b^{2}x^{2}}{4\sigma^{2}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p27.2" class="ltx_p">which is <a href="#S5.E7a" title="In Item 2 ‣ Lemma S.5.5 (Pruning and compression). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.7</span></a> after the constant is dropped. Pathwise equality of the states gives $\mathbb{E}_{Y}[x_{w}]=\mathbb{E}_{Y}[x_{c_{\mathcal{C}}}]\text{,}$ hence the coordinate claim.
∎</p>
</div>
<div id="S5a.p28" class="ltx_para">
<p id="S5a.p28.1" class="ltx_p">The forward computation of $P_{o}[k]$ is a straight-line program in the $n(3k+1)$ inputs $\varphi_{v}(x)$ whose gates are polynomial multiplications with their tail formulas <a href="#S5.E4a" title="In Lemma S.5.3 (Product of pairs). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.4</span></a>, the linear recurrences <a href="#S5.E6a" title="In Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.6</span></a>, and the coordinatewise products <a href="#S5.E5a" title="In Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.5</span></a>. The reverse sweep differentiates it.</p>
</div>
<div id="S5.Thmlemma6" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmlemma6.2" class="ltx_text ltx_font_bold">Lemma S.5.6</span></span><span id="S5.Thmlemma6.3" class="ltx_text ltx_font_bold"> (Reverse sweep).</span></h6>
<div id="S5.Thmlemma6.p1" class="ltx_para">
<p id="S5.Thmlemma6.p1.1" class="ltx_p"><span id="S5.Thmlemma6.p1.1.1" class="ltx_text ltx_font_italic">All $n(3k+1)$ partial derivatives $\partial P_{o}[k]/\partial\varphi_{v}(x)$ are computable in $O(1)$ times the cost of the forward computation, and</span></p>
<table id="S5.E8a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{\mu}_{k}(v)\ =\ b\sum_{x=0}^{3k}x\cdot\frac{\varphi_{v}(x)}{P_{o}[k]}\,\frac{\partial P_{o}[k]}{\partial\varphi_{v}(x)},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.8)</span></td></tr></tbody>
</table>
<p id="S5.Thmlemma6.p1.2" class="ltx_p"><span id="S5.Thmlemma6.p1.2.1" class="ltx_text ltx_font_italic">which is the display (4.6).</span></p>
</div>
</div>
<div id="S5a.p29" class="ltx_para">
<p id="S5a.p29.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S5a.p30" class="ltx_para">
<p id="S5a.p30.1" class="ltx_p">By <a href="#S5.E3a" title="In S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.3</span></a> at the root, $P_{o}[k]$ is a sum of monomials, one per state vector $x^{\prime}$ with $x^{\prime}_{o}=k\text{,}$ each containing the input $\varphi_{v}(x^{\prime}_{v})$ exactly once and otherwise only kernel constants and inputs at other vertices. Hence $\varphi_{v}(x)\,\partial P_{o}[k]/\partial\varphi_{v}(x)$ is the total weight of the state vectors with $x^{\prime}_{v}=x\text{,}$ so the ratio in <a href="#S5.E8a" title="In Lemma S.5.6 (Reverse sweep). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.8</span></a> is the posterior probability of $\{x_{v}=x\}$ and the sum is $b\,\mathbb{E}_{Y}[x_{v}]=\widehat{\mu}_{k}(v)\text{.}$</p>
</div>
<div id="S5a.p31" class="ltx_para">
<p id="S5a.p31.1" class="ltx_p">For the cost, propagate the derivatives of $P_{o}[k]$ with respect to every intermediate quantity backward through the program, from the output to the inputs. By the chain rule, the derivative with respect to a quantity is assembled from the derivatives with respect to the quantities that consume it, so one backward pass over the acyclic program suffices; each gate is handled by the transpose of its linearization, at the cost of the gate itself. For a product of pairs, the derivative with respect to a coefficient of one factor is a correlation with the other,</p>
<table id="S5.E9a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{\partial P_{o}[k]}{\partial F_{0}[i]}\ =\ \sum_{j=0}^{3k}\frac{\partial P_{o}[k]}{\partial\,[\zeta^{i+j}](F_{0}G_{0})}\ G_{0}[j]\qquad(0\leq i\leq 3k),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.9)</span></td></tr></tbody>
</table>
<p id="S5a.p31.2" class="ltx_p">one multiplication of polynomials of degree at most $6k$ after reversing the coefficient order, plus the $O(k)$ coordinatewise contributions of <a href="#S5.E4a" title="In Lemma S.5.3 (Product of pairs). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.4</span></a> through its low coefficients, its evaluations, and its tails. The transposed recurrences <a href="#S5.E6a" title="In Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.6</span></a> run in the opposite direction in $O(k)\text{,}$ and the coordinatewise products <a href="#S5.E5a" title="In Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.5</span></a> are differentiated in $O(k)\text{.}$ Every gate’s transpose therefore costs the order of the gate, and the sweep visits each gate once.
∎</p>
</div>
<div id="S5a.p32" class="ltx_para">
<p id="S5a.p32.1" class="ltx_p"><em id="S5a.p32.1.1" class="ltx_emph ltx_font_italic">The operation count of Theorem 2.</em> Computing $k_{\mathrm{alg}}$ costs $O(n\log(n+1))$ operations by Lemma 2.3; the nets $S_{j}$ at the $J+1=O(\log(k+1))$ dyadic radii cost $O(n)$ each by <a href="#S1.Thmlemma1" title="Lemma S.1.1. ‣ S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.1.1</span></a>, and the charges $\widetilde{\omega}$ one further pass. In the interior branch, the forward computation performs, over the whole tree, fewer than $n$ products of pairs, each $O(k\log(k+1))$ by <a href="#S5.Thmlemma3" title="Lemma S.5.3 (Product of pairs). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.3</span></a> and the multiplication model of Section 2.1, and $O(k)$ local work at each vertex (<a href="#S5.Thmlemma4" title="Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.4</span></a>); the reverse sweep matches this cost (<a href="#S5.Thmlemma6" title="Lemma S.5.6 (Reverse sweep). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.6</span></a>); and assembling <a href="#S5.E8a" title="In Lemma S.5.6 (Reverse sweep). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.8</span></a> at every vertex costs $O(nk)\text{.}$ Pruning and compression (<a href="#S5.Thmlemma5" title="Lemma S.5.5 (Pruning and compression). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.5</span></a>) only remove work. The elementary branches cost $O(n)$ beyond the preprocessing. Every tie break (child orders, the greedy of <a href="#S1.Thmlemma1" title="Lemma S.1.1. ‣ S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.1.1</span></a>, the merge order) is fixed, so the whole map $(T,V,\sigma,Y)\mapsto\widehat{\mu}$ is deterministic, and the total is</p>
<table id="S5.Ex19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$O\bigl(n\log(n+1)+nk\log(k+1)\bigr)\ \leq\ O\bigl(n^{2}\log(n+1)\bigr)$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p32.2" class="ltx_p">operations, since $k\leq K+1\leq n\text{:}$ the count claimed in Theorem 2, whose proof is now complete.</p>
</div>
<div id="S5a.p33" class="ltx_para">
<p id="S5a.p33.1" class="ltx_p">The remaining two lemmas support the instance sentence of Section 4.2. Sibling messages that are dilations of a common polynomial multiply in batch: the mechanism is that logarithms turn the product into power sums of the dilation parameters. Two standard consequences of fast multiplication are used <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib39" title="" class="ltx_ref">von zur Gathen and Gerhard, 2013</a>)</cite>: Newton iteration computes truncated inverses and logarithms of power series with constant term $1\text{,}$ and exponentials of those with constant term $0\text{,}$ at the cost of $O(1)$ multiplications of the same degree; and a degree-$D$ polynomial is evaluated at $d$ points in $O((D+d)\log^{2}(D+d))$ operations by a product tree.</p>
</div>
<div id="S5.Thmlemma7" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmlemma7.2" class="ltx_text ltx_font_bold">Lemma S.5.7</span></span><span id="S5.Thmlemma7.3" class="ltx_text ltx_font_bold"> (Batched dilations).</span></h6>
<div id="S5.Thmlemma7.p1" class="ltx_para">
<p id="S5.Thmlemma7.p1.1" class="ltx_p"><span id="S5.Thmlemma7.p1.1.1" class="ltx_text ltx_font_italic">Let $F$ be a polynomial of degree at most $3k$ with $F[0]=1\text{,}$ and let $\xi_{1},\dots,\xi_{d}&gt;0\text{.}$ In $O((k+d)\log^{2}(k+d))$ operations one can compute</span></p>
<ol id="S5.I9" class="ltx_enumerate">
<li id="S5.I9.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S5.I9.i1.p1" class="ltx_para">
<p id="S5.I9.i1.p1.1" class="ltx_p"><span id="S5.I9.i1.p1.1.1" class="ltx_text ltx_font_italic">the truncation of
</span>$\prod_{i=1}^{d}F(\xi_{i}\zeta)$<span id="S5.I9.i1.p1.1.2" class="ltx_text ltx_font_italic"> modulo </span>$\zeta^{3k+1}$<span id="S5.I9.i1.p1.1.3" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S5.I9.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S5.I9.i2.p1" class="ltx_para">
<p id="S5.I9.i2.p1.1" class="ltx_p"><span id="S5.I9.i2.p1.1.1" class="ltx_text ltx_font_italic">the values </span>$F(e^{-2}\xi_{i})$<span id="S5.I9.i2.p1.1.2" class="ltx_text ltx_font_italic"> and
</span>$F^{\prime}(e^{-2}\xi_{i})$<span id="S5.I9.i2.p1.1.3" class="ltx_text ltx_font_italic"> for all </span>$i\leq d$<span id="S5.I9.i2.p1.1.4" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S5.I9.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S5.I9.i3.p1" class="ltx_para">
<p id="S5.I9.i3.p1.1" class="ltx_p"><span id="S5.I9.i3.p1.1.1" class="ltx_text ltx_font_italic">for any given </span>$y_{0},\dots,y_{3k}$<span id="S5.I9.i3.p1.1.2" class="ltx_text ltx_font_italic">, the
values
</span>$\ \xi_{i}\,\dfrac{\partial}{\partial\xi_{i}}\displaystyle\sum_{s=0}^{3k}y_{s}\,[\zeta^{s}]\prod_{j=1}^{d}F(\xi_{j}\zeta)\space$<span id="S5.I9.i3.p1.1.3" class="ltx_text ltx_font_italic">
for all </span>$i\leq d$<span id="S5.I9.i3.p1.1.4" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S5a.p34" class="ltx_para">
<p id="S5a.p34.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S5a.p35" class="ltx_para">
<p id="S5a.p35.1" class="ltx_p">Write $g(\zeta):=\log F(\zeta)=\sum_{m=1}^{3k}g_{m}\zeta^{m}$ modulo $\zeta^{3k+1}\text{,}$ computable by Newton iteration since $F[0]=1\text{,}$ and let $t_{m}:=\sum_{i\leq d}\xi_{i}^{m}$ be the power sums. Then, modulo $\zeta^{3k+1}\text{,}$</p>
<table id="S5.E10a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\prod_{i=1}^{d}F(\xi_{i}\zeta)\ =\ \exp\Bigl(\sum_{m=1}^{3k}g_{m}\,t_{m}\,\zeta^{m}\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.10)</span></td></tr></tbody>
</table>
<p id="S5a.p35.2" class="ltx_p">because $\log F(\xi_{i}\zeta)=\sum_{m}g_{m}\xi_{i}^{m}\zeta^{m}$ and the logarithms add. The power sums come from the auxiliary polynomial $N(\zeta):=\prod_{i\leq d}(1-\xi_{i}\zeta)\text{,}$ built by a product tree, through the logarithmic-derivative identity $-\zeta N^{\prime}(\zeta)/N(\zeta)=\sum_{m\geq 1}t_{m}\zeta^{m}\text{,}$ one derivative, one truncated inversion, and one multiplication; the exponential in <a href="#S5.E10a" title="In S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.10</span></a> is one more Newton iteration. This proves (<a href="#S5.I9.i1" title="Item 1 ‣ Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>), and (<a href="#S5.I9.i2" title="Item 2 ‣ Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) is multipoint evaluation of $F$ and $F^{\prime}$ at the points $e^{-2}\xi_{i}\text{.}$ For (<a href="#S5.I9.i3" title="Item 3 ‣ Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), write $P:=\exp(H)$ with $H:=\sum_{m}g_{m}t_{m}\zeta^{m}\text{;}$ then $dP=P\,dH\text{,}$ so the displayed quantity, as a function of the $t_{m}\text{,}$ has</p>
<table id="S5.Ex20" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{\partial}{\partial t_{m}}\sum_{s\leq 3k}y_{s}\,[\zeta^{s}]P\ =\ g_{m}\sum_{s=m}^{3k}y_{s}\,[\zeta^{s-m}]P,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p35.3" class="ltx_p">one correlation as in <a href="#S5.E9a" title="In S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.9</span></a>; and since $\xi_{i}\,\partial t_{m}/\partial\xi_{i}=m\,\xi_{i}^{m}\text{,}$ the value carried by the dilation parameter $\xi_{i}$ is the evaluation at $\xi_{i}$ of the polynomial $\sum_{m=1}^{3k}m\,g_{m}\bigl(\sum_{s\geq m}y_{s}[\zeta^{s-m}]P\bigr)\,\zeta^{m}\text{,}$ a second multipoint evaluation. Every step is a product tree, a truncated inversion, a logarithm or exponential, a correlation, or a multipoint evaluation at degree $O(k+d)\text{,}$ each within the stated bound.
∎</p>
</div>
<div id="S5a.p36" class="ltx_para">
<p id="S5a.p36.1" class="ltx_p">On the star, either the active support collapses to the root or every leaf message is a dilation of one template; in both cases the evaluation is softly linear.</p>
</div>
<div id="S5.Thmlemma8" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmlemma8.2" class="ltx_text ltx_font_bold">Lemma S.5.8</span></span><span id="S5.Thmlemma8.3" class="ltx_text ltx_font_bold"> (Stars).</span></h6>
<div id="S5.Thmlemma8.p1" class="ltx_para">
<p id="S5.Thmlemma8.p1.1" class="ltx_p"><span id="S5.Thmlemma8.p1.1.1" class="ltx_text ltx_font_italic">On the star $S_{m}$ with $m\geq 2$ leaves, the estimator (4.3) is computed in $O(n\log^{2}n)$ operations, $n=m+1\text{.}$</span></p>
</div>
</div>
<div id="S5a.p37" class="ltx_para">
<p id="S5a.p37.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S5a.p38" class="ltx_para">
<p id="S5a.p38.1" class="ltx_p">The preprocessing and the elementary branches cost $O(n\log(n+1))\text{,}$ so let the interior branch be selected, with budget $2\leq k\leq K$ and working scale $\bar{\alpha}=k\overline{\delta}_{k}\geq 2$ (<a href="#S2.Thmlemma1a" title="Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.1</span></a>(<a href="#S2.I1.i1a" title="Item 1 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>)). On the star, the minimum ancestor $r$-net with $r\geq 1$ is $\{o\}\text{,}$ a leaf being an ancestor only of itself, while at $r=0$ every vertex needs itself; so with $j_{0}:=\min\{j:\lfloor\bar{\alpha}/m_{j}\rfloor=0\}\text{,}$ understood as $j_{0}=J+1$ if no radius vanishes, the nets are $S_{j}=\{o\}$ for $j&lt;j_{0}$ and $S_{j}=\mathsf{V}$ for $j\geq j_{0}\text{,}$ and $j_{0}\geq 1$ because $\lfloor\bar{\alpha}\rfloor\geq 2\text{.}$</p>
</div>
<div id="S5a.p39" class="ltx_para">
<p id="S5a.p39.1" class="ltx_p">If $j_{0}=J+1\text{,}$ then $A_{k}=\{o\}\text{:}$ the only state vector with nonzero weight has $x_{o}=k$ and all leaf states zero, the posterior is a point mass, and $\widehat{\mu}_{k}=\tfrac{V}{k}\,x=Vp_{o}$ is written in $O(n)\text{.}$</p>
</div>
<div id="S5a.p40" class="ltx_para">
<p id="S5a.p40.1" class="ltx_p">If $j_{0}\leq J\text{,}$ then $A_{k}=\mathsf{V}$ and every leaf carries the same charge $\widetilde{\omega}=m_{j_{0}}\text{.}$ Factor the local weight of leaf $v$ at state $x$ as $\varphi_{v}(x)=e^{-Y_{v}^{2}/(4\sigma^{2})}\,e^{-b^{2}x^{2}/(4\sigma^{2})}\,\xi_{v}^{x}$ with $\xi_{v}:=e^{bY_{v}/(2\sigma^{2})}\text{;}$ the first factor is common to every assignment and is dropped. By <a href="#S5.Thmlemma4" title="Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.4</span></a>, the message of leaf $v$ is then $F(\xi_{v}\zeta)$ for the common template</p>
<table id="S5.Ex21" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$F(\zeta)\ :=\ 1\ +\ e^{-2m_{j_{0}}}\sum_{x=1}^{3k}e^{-2x}\,e^{-b^{2}x^{2}/(4\sigma^{2})}\,\zeta^{x},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p40.2" class="ltx_p">and the child product of the root is $Q_{o}(\zeta)=\prod_{v}F(\xi_{v}\zeta)\text{.}$ <a href="#S5.Thmlemma7" title="Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.7</span></a>(<a href="#S5.I9.i1" title="Item 1 ‣ Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>) gives its truncation, <a href="#S5.Thmlemma7" title="Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.7</span></a>(<a href="#S5.I9.i2" title="Item 2 ‣ Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) gives $Q_{o}(e^{-2})=\prod_{v}F(e^{-2}\xi_{v})\text{,}$ and the tail follows as</p>
<table id="S5.Ex22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau_{o}\ =\ e^{6k}\Bigl(\,Q_{o}(e^{-2})-\sum_{s=0}^{3k}Q_{o}[s]\,e^{-2s}\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p40.3" class="ltx_p">exactly, from the definition of the tail. The root pass of <a href="#S5.Thmlemma4" title="Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.4</span></a> then yields $P_{o}[k]$ in $O(k)$ operations.</p>
</div>
<div id="S5a.p41" class="ltx_para">
<p id="S5a.p41.1" class="ltx_p">For the marginals, $P_{o}[k]$ is a linear function of $(Q_{o}[0],\dots,Q_{o}[3k],\tau_{o})$ by <a href="#S5.E5a" title="In Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.5</span></a> and <a href="#S5.E6a" title="In Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.5.6</span></a>, with coefficients computable in $O(k)\text{;}$ and every assignment’s weight carries the factor $\xi_{v}^{x_{v}}\text{,}$ so Euler differentiation gives</p>
<table id="S5.E11a" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}_{Y}[x_{v}]\ =\ \frac{\xi_{v}}{P_{o}[k]}\,\frac{\partial P_{o}[k]}{\partial\xi_{v}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.5.11)</span></td></tr></tbody>
</table>
<p id="S5a.p41.2" class="ltx_p">The derivative splits along the linear form: the low coefficients contribute one instance of <a href="#S5.Thmlemma7" title="Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.7</span></a>(<a href="#S5.I9.i3" title="Item 3 ‣ Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), with weights that combine the direct coefficients of the linear form and the term $-e^{6k-2s}$ that $Q_{o}[s]$ inherits from $\tau_{o}\text{,}$ while $Q_{o}(e^{-2})$ contributes</p>
<table id="S5.Ex23" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\xi_{v}\,\frac{\partial Q_{o}(e^{-2})}{\partial\xi_{v}}\ =\ Q_{o}(e^{-2})\cdot\frac{e^{-2}\xi_{v}\,F^{\prime}(e^{-2}\xi_{v})}{F(e^{-2}\xi_{v})}\ ,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5a.p41.3" class="ltx_p">an $O(1)$ combination of the values from <a href="#S5.Thmlemma7" title="Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.7</span></a>(<a href="#S5.I9.i2" title="Item 2 ‣ Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>), whose denominators are positive because $F$ has positive constant term and nonnegative coefficients. Then $\widehat{\mu}_{k}(v)=b\,\mathbb{E}_{Y}[x_{v}]$ at every leaf and $\widehat{\mu}_{k}(o)=V\text{.}$ All steps beyond the preprocessing cost $O((k+m)\log^{2}(k+m))\text{,}$ and $k\leq K&lt;n$ makes this $O(n\log^{2}n)\text{.}$
∎</p>
</div>
<div id="S5a.p42" class="ltx_para">
<p id="S5a.p42.1" class="ltx_p">Together, <a href="#S5.Thmlemma7" title="Lemma S.5.7 (Batched dilations). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemmas</span> <span class="ltx_text ltx_ref_tag">S.5.7</span></a> and <a href="#S5.Thmlemma8" title="Lemma S.5.8 (Stars). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">S.5.8</span></a> verify the instance sentence of Section 4.2: a group of sibling messages agreeing up to a dilation of the variable multiplies in batch, and on stars the entire evaluation is softly linear in $n\text{.}$</p>
</div>
</section>
<section id="S6" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="adaptation-1"><span class="ltx_tag ltx_tag_section">S.6 </span>Adaptation</h2>

<div id="S6.p1" class="ltx_para">
<p id="S6.p1.1" class="ltx_p">This section proves the statements deferred from Section 4.3: the selection oracle (4.8), in the weighted and random-penalty form stated there; the scale calculus for the minimax risk; the subspace approximation (4.7); the enumeration of admissible supports; the assembly of the sufficiency half of Theorem 3, including its running time; the difference statistics of Theorem 4 with their contamination bound, the concentration of the noise estimate, and the moment bookkeeping; and the noise-estimation ceiling stated at the end of Section 4.3. Throughout, $K:=\lfloor n/C_{\star}\rfloor$ and dyadic integers are powers of two; the selection constant of (4.8) is instantiated as $C_{2}:=128\text{.}$ The standard Gaussian tail bound $\mathbb{P}\bigl(N(0,\tau^{2})\geq t\bigr)\leq e^{-t^{2}/(2\tau^{2})}\text{,}$ valid for $t\geq 0\text{,}$ is used without further comment.</p>
</div>
<div id="S6.p2" class="ltx_para">
<p id="S6.p2.1" class="ltx_p">The selection engine comes first. The lemma below is the oracle promised with (4.8): the noise may have unequal, even zero, coordinate variances, which is how conditioning on the root observation will enter, and the penalties may be random as long as they are bracketed on an event, which is how the estimated noise scale will enter.</p>
</div>
<div id="S6.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma S.6.1</span></span><span id="S6.Thmlemma1.3" class="ltx_text ltx_font_bold"> (Weighted affine selection).</span></h6>
<div id="S6.Thmlemma1.p1" class="ltx_para">
<p id="S6.Thmlemma1.p1.1" class="ltx_p"><span id="S6.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">Let $Y=\theta+Z\in\mathbb{R}^{N}\text{,}$ where $\theta\in\mathbb{R}^{N}$ and $Z$ is a centered Gaussian vector with independent coordinates whose variances are at most $\sigma^{2}\text{,}$ some possibly zero. Let $\mathcal{M}$ be a countable collection of affine models $m=c_{m}+W_{m}\subseteq\mathbb{R}^{N}\text{,}$ each $W_{m}$ a linear subspace of finite dimension $D_{m}\text{,}$ with weights $\Delta_{m}\geq 0$ such that $\sum_{m\in\mathcal{M}}e^{-\Delta_{m}}\leq 1\text{.}$ Let $\widehat{\theta}$ minimize $\|Y-\nu\|_{2}^{2}+\operatorname{pen}(m)$ over $m\in\mathcal{M}$ and $\nu\in m\text{,}$ and over a full model whose fit is $\nu=Y$ itself. The penalties are nonnegative, possibly random, and such that the minimum defining $\widehat{\theta}$ is attained, as it is in particular for finite $\mathcal{M}\text{.}$ Suppose that on an event $E\text{,}$ for a constant $\bar{\kappa}\geq 32\text{,}$</span></p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S6.EGx6"></span><span class="paper-eq-anchor" id="S6.Ex1"></span><span class="paper-eq-anchor" id="S6.Ex2"></span><div class="paper-eqgroup-body">$$\begin{gathered}
\displaystyle 32\,\sigma^{2}(D_{m}+\Delta_{m})\ \leq\ \operatorname{pen}(m)\ \leq\ \bar{\kappa}\,\sigma^{2}(D_{m}+\Delta_{m})\qquad\text{for every }m\in\mathcal{M}, \\
\displaystyle 32\,\sigma^{2}N\ \leq\ \operatorname{pen}(\mathrm{full})\ \leq\ \bar{\kappa}\,\sigma^{2}N.
\end{gathered}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S6.Thmlemma1.p1.2" class="ltx_p"><span id="S6.Thmlemma1.p1.2.1" class="ltx_text ltx_font_italic">Then</span></p>
<table id="S6.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl[\|\widehat{\theta}-\theta\|_{2}^{2}\,\mathbf{1}_{E}\bigr]\ \leq\ C_{\bar{\kappa}}\Bigl(\min\Bigl\{\ \inf_{m\in\mathcal{M}}\bigl(\operatorname{dist}^{2}(\theta,m)+\sigma^{2}(D_{m}+\Delta_{m}+1)\bigr),\ \ \sigma^{2}N\ \Bigr\}\ +\ \sigma^{2}\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.Thmlemma1.p1.3" class="ltx_p"><span id="S6.Thmlemma1.p1.3.1" class="ltx_text ltx_font_italic">where $C_{\bar{\kappa}}$ depends only on $\bar{\kappa}\text{.}$</span></p>
</div>
</div>
<div id="S6.p3" class="ltx_para">
<p id="S6.p3.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S6.p4" class="ltx_para">
<p id="S6.p4.1" class="ltx_p">The selected model is compared with one fixed model through the basic inequality of penalized least squares; a single Kraft-weighted deviation variable controls the Gaussian fluctuations over the whole collection, and the full model is handled by its own comparison.</p>
</div>
<div id="S6.p5" class="ltx_para">
<p id="S6.p5.1" class="ltx_p"><em id="S6.p5.1.1" class="ltx_emph ltx_font_italic">A projection bound.</em> Let $U\subseteq\mathbb{R}^{N}$ be a fixed subspace of dimension $d$ and $P_{U}$ the orthogonal projection onto it. For an orthonormal basis $u_{1},\dots,u_{d}$ of $U\text{,}$ the vector $(\langle Z,u_{i}\rangle)_{i\leq d}$ is centered Gaussian with covariance $\Sigma\preceq\sigma^{2}I_{d}\text{:}$ its quadratic form at $a\in\mathbb{R}^{d}$ is $\operatorname{Var}\langle Z,\sum_{i}a_{i}u_{i}\rangle\leq\sigma^{2}\|\sum_{i}a_{i}u_{i}\|_{2}^{2}=\sigma^{2}\|a\|_{2}^{2}\text{.}$ For a centered Gaussian $g$ of variance $\tau^{2}\leq\sigma^{2}\text{,}$ direct integration gives $\mathbb{E}e^{g^{2}/(4\sigma^{2})}=(1-\tau^{2}/(2\sigma^{2}))^{-1/2}\leq\sqrt{2}\text{,}$ the case $\tau^{2}=0$ included; diagonalizing $\Sigma$ and multiplying over the independent coordinates,</p>
<table id="S6.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\,e^{\|P_{U}Z\|_{2}^{2}/(4\sigma^{2})}\ \leq\ 2^{d/2};$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p5.2" class="ltx_p">hence, by Markov’s inequality and $2^{1/2}\leq e\text{,}$ for every $t\geq 0\text{,}$</p>
<table id="S6.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{P}\bigl(\|P_{U}Z\|_{2}^{2}\geq 4\sigma^{2}(d+t)\bigr)\ \leq\ 2^{d/2}\,e^{-d-t}\ \leq\ e^{-t}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S6.p6" class="ltx_para">
<p id="S6.p6.1" class="ltx_p"><em id="S6.p6.1.1" class="ltx_emph ltx_font_italic">The deviation variable.</em> Fix a comparison model $m_{0}\in\mathcal{M}$ and let $f_{0}\in m_{0}$ attain $a:=\operatorname{dist}(\theta,m_{0})\text{,}$ the metric projection of $\theta$ onto the closed affine set $m_{0}\text{.}$ For $m\in\mathcal{M}$ put</p>
<table id="S6.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$U_{m}\ :=\ W_{m}+W_{m_{0}}+\operatorname{span}(c_{m}-f_{0}),\qquad d_{m}\ :=\ \dim U_{m}\ \leq\ D_{m}+D_{m_{0}}+1,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p6.2" class="ltx_p">so that every $\nu=c_{m}+w\in m$ has $\nu-f_{0}=(c_{m}-f_{0})+w\in U_{m}\text{,}$ and define</p>
<table id="S6.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Z^{*}\ :=\ \sup_{m\in\mathcal{M}}\ \Bigl[\frac{\|P_{U_{m}}Z\|_{2}^{2}}{4\sigma^{2}}-(d_{m}+\Delta_{m})\Bigr]_{+}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p6.3" class="ltx_p">By the projection bound and a union bound, $\mathbb{P}(Z^{*}&gt;t)\leq\sum_{m}e^{-\Delta_{m}-t}\leq e^{-t}\text{,}$ so $\mathbb{E}Z^{*}=\int_{0}^{\infty}\mathbb{P}(Z^{*}&gt;t)\,dt\leq 1\text{;}$ and by its definition, $\|P_{U_{m}}Z\|_{2}^{2}\leq 4\sigma^{2}(d_{m}+\Delta_{m}+Z^{*})$ for every $m$ simultaneously.</p>
</div>
<div id="S6.p7" class="ltx_para">
<p id="S6.p7.1" class="ltx_p"><em id="S6.p7.1.1" class="ltx_emph ltx_font_italic">A model is selected.</em> Suppose the minimum is attained at some $\widehat{m}\in\mathcal{M}$ with fit $\widehat{\theta}\in\widehat{m}\text{,}$ and write $d:=\widehat{\theta}-\theta\text{.}$ Expanding the basic inequality against $(m_{0},f_{0})\text{,}$ $\|Y-\widehat{\theta}\|_{2}^{2}+\operatorname{pen}(\widehat{m})\leq\|Y-f_{0}\|_{2}^{2}+\operatorname{pen}(m_{0})\text{,}$ at $Y=\theta+Z$ and combining the two cross terms into $2\langle Z,\widehat{\theta}-f_{0}\rangle$ gives</p>
<table id="S6.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|d\|_{2}^{2}\ \leq\ a^{2}+2\langle Z,\widehat{\theta}-f_{0}\rangle-\operatorname{pen}(\widehat{m})+\operatorname{pen}(m_{0}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p7.2" class="ltx_p">Since $\widehat{\theta}-f_{0}\in U_{\widehat{m}}\text{,}$ the inequality $2xy\leq\tfrac{1}{4}x^{2}+4y^{2}$ and the deviation variable give</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S6.EGx7"></span><span class="paper-eq-anchor" id="S6.Ex9"></span><span class="paper-eq-anchor" id="S6.Ex10"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle 2\langle Z,\widehat{\theta}-f_{0}\rangle\ =\ 2\bigl\langle P_{U_{\widehat{m}}}Z,\ \widehat{\theta}-f_{0}\bigr\rangle\space &amp; \displaystyle\leq\ \tfrac{1}{4}\|\widehat{\theta}-f_{0}\|_{2}^{2}+4\,\|P_{U_{\widehat{m}}}Z\|_{2}^{2} \\
 &amp; \displaystyle\leq\ \tfrac{1}{4}\bigl(\|d\|_{2}+a\bigr)^{2}+16\sigma^{2}\bigl(d_{\widehat{m}}+\Delta_{\widehat{m}}+Z^{*}\bigr).
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S6.p7.3" class="ltx_p">By $d_{\widehat{m}}\leq D_{\widehat{m}}+D_{m_{0}}+1\text{,}$ the last term splits into $16\sigma^{2}(D_{\widehat{m}}+\Delta_{\widehat{m}})+16\sigma^{2}(D_{m_{0}}+1)+16\sigma^{2}Z^{*}\text{,}$ and on $E$ the penalty dominates its first piece: $\operatorname{pen}(\widehat{m})\geq 32\sigma^{2}(D_{\widehat{m}}+\Delta_{\widehat{m}})\text{.}$ Together with $\tfrac{1}{4}(\|d\|_{2}+a)^{2}\leq\tfrac{1}{2}\|d\|_{2}^{2}+\tfrac{1}{2}a^{2}\text{,}$ the expansion rearranges to</p>
<table id="S6.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|d\|_{2}^{2}\ \leq\ 3a^{2}+2\operatorname{pen}(m_{0})+32\sigma^{2}(D_{m_{0}}+1)+32\sigma^{2}Z^{*}\qquad\text{on }E\cap\{\text{a model is selected}\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.1)</span></td></tr></tbody>
</table>
</div>
<div id="S6.p8" class="ltx_para">
<p id="S6.p8.1" class="ltx_p"><em id="S6.p8.1.1" class="ltx_emph ltx_font_italic">The full model is selected.</em> Then $\widehat{\theta}=Y$ and $\|d\|_{2}^{2}=\|Z\|_{2}^{2}\text{,}$ while the full model’s own residual vanishes, so the basic inequality against $(m_{0},f_{0})$ reads $\operatorname{pen}(\mathrm{full})\leq\|Y-f_{0}\|_{2}^{2}+\operatorname{pen}(m_{0})\leq 2a^{2}+2\|Z\|_{2}^{2}+\operatorname{pen}(m_{0})\text{;}$ on $E$ this gives $32\sigma^{2}N\leq 2a^{2}+2\|Z\|_{2}^{2}+\operatorname{pen}(m_{0})\text{.}$ On the event $\{\|Z\|_{2}^{2}\leq 2\sigma^{2}N\}\text{,}$ where $2\|Z\|_{2}^{2}\leq 4\sigma^{2}N\text{,}$ the preceding two inequalities force $28\sigma^{2}N\leq 2a^{2}+\operatorname{pen}(m_{0})\text{,}$ hence $\|Z\|_{2}^{2}\leq 2\sigma^{2}N\leq\tfrac{1}{14}\bigl(2a^{2}+\operatorname{pen}(m_{0})\bigr)\text{.}$ On the complement, the projection bound at $U=\mathbb{R}^{N}$ gives $\mathbb{P}(\|Z\|_{2}^{2}&gt;2\sigma^{2}N)\leq 2^{N/2}e^{-N/2}\leq e^{-N/8}\text{;}$ moreover $\mathbb{E}\|Z\|_{2}^{4}=\sum_{i}\mathbb{E}Z_{i}^{4}+\sum_{i\neq j}\mathbb{E}Z_{i}^{2}\,\mathbb{E}Z_{j}^{2}\leq 3\sigma^{4}N+\sigma^{4}N(N-1)\leq 3\sigma^{4}N^{2}\text{,}$ the coordinates being independent with fourth moments at most $3\sigma^{4}\text{,}$ so the Cauchy–Schwarz inequality gives</p>
<table id="S6.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl[\|Z\|_{2}^{2}\,\mathbf{1}\{\|Z\|_{2}^{2}&gt;2\sigma^{2}N\}\bigr]\ \leq\ \sqrt{3}\,\sigma^{2}N\,e^{-N/16}\ \leq\ C\sigma^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p8.2" class="ltx_p">the map $N\mapsto Ne^{-N/16}$ being bounded.</p>
</div>
<div id="S6.p9" class="ltx_para">
<p id="S6.p9.1" class="ltx_p"><em id="S6.p9.1.1" class="ltx_emph ltx_font_italic">Assembly.</em> Combining <a href="#S6.E1" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> with the two estimates of the full-model case and using $\mathbb{E}Z^{*}\leq 1$ and the bracketing of $\operatorname{pen}(m_{0})$ on $E\text{,}$</p>
<table id="S6.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl[\|\widehat{\theta}-\theta\|_{2}^{2}\,\mathbf{1}_{E}\bigr]\ \leq\ C\bigl(a^{2}+\bar{\kappa}\,\sigma^{2}(D_{m_{0}}+\Delta_{m_{0}}+1)\bigr)+C\sigma^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p9.2" class="ltx_p">and taking the infimum over $m_{0}$ gives the first branch of the minimum. For the second branch, compare with the full model instead: if the full model is selected, then $\mathbb{E}[\|d\|_{2}^{2}\,\mathbf{1}_{E}]\leq\mathbb{E}\|Z\|_{2}^{2}\leq\sigma^{2}N\text{;}$ if some $\widehat{m}$ is selected, the basic inequality against the full model gives $\|Y-\widehat{\theta}\|_{2}^{2}\leq\operatorname{pen}(\mathrm{full})\leq\bar{\kappa}\sigma^{2}N$ on $E\text{,}$ so $\|d\|_{2}^{2}\leq 2\|Y-\widehat{\theta}\|_{2}^{2}+2\|Z\|_{2}^{2}$ has expectation at most $(2\bar{\kappa}+2)\sigma^{2}N$ there. Taking the minimum of the two comparisons completes the proof.
∎</p>
</div>
<div id="S6.p10" class="ltx_para">
<p id="S6.p10.1" class="ltx_p">Three features are used below. The penalties may be random, only their bracketing on $E$ entering the argument. The coordinate variances may differ and may vanish. And a point $\nu$ is the affine model $\{\nu\}$ with $D_{m}=0\text{,}$ whose oracle value reads $\|\theta-\nu\|_{2}^{2}+\sigma^{2}(\Delta_{\{\nu\}}+1)\text{;}$ we write $w(\nu)$ for the weight of a point model. The display (4.8) is the deterministic special case: penalties $C_{2}\sigma^{2}(\dim m+\Delta_{m})$ and $C_{2}\sigma^{2}N$ satisfy the bracketing with $E$ the whole probability space and $\bar{\kappa}=C_{2}\text{.}$</p>
</div>
<div id="S6.p11" class="ltx_para">
<p id="S6.p11.1" class="ltx_p">The coverage argument will replace the unknown amplitude by a grid value and the unknown noise level by a rounded estimate. The next lemma prices both substitutions.</p>
</div>
<div id="S6.Thmlemma2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmlemma2.2" class="ltx_text ltx_font_bold">Lemma S.6.2</span></span><span id="S6.Thmlemma2.3" class="ltx_text ltx_font_bold"> (Scale calculus).</span></h6>
<div id="S6.Thmlemma2.p1" class="ltx_para">
<p id="S6.Thmlemma2.p1.1" class="ltx_p"><span id="S6.Thmlemma2.p1.1.1" class="ltx_text ltx_font_italic">For every finite rooted tree, $R^{*}_{T}(V,\sigma)$ is nondecreasing in $V$ and in $\sigma\text{,}$ and for every $c\geq 1\text{,}$</span></p>
<table id="S6.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(cV,\sigma)\ \leq\ c^{2}\,R^{*}_{T}(V,\sigma),\qquad R^{*}_{T}(V,c\sigma)\ \leq\ c^{2}\,R^{*}_{T}(V,\sigma).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S6.p12" class="ltx_para">
<p id="S6.p12.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S6.p13" class="ltx_para">
<p id="S6.p13.1" class="ltx_p"><em id="S6.p13.1.1" class="ltx_emph ltx_font_italic">Monotonicity in $V\text{.}$</em> Let $V\leq V^{\prime}\text{.}$ The translation $\iota(\mu):=\mu+(V^{\prime}-V)p_{o}$ adds $V^{\prime}-V$ to the leak at the root and changes no other leak, so it maps $\mathcal{F}_{V}(T)$ into $\mathcal{F}_{V^{\prime}}(T)$ by Lemma 2.1. Given any estimator $\widehat{\mu}^{\prime}\text{,}$ define $\widehat{\mu}(Y):=\widehat{\mu}^{\prime}\bigl(Y+(V^{\prime}-V)p_{o}\bigr)-(V^{\prime}-V)p_{o}\text{.}$ Under $\mu\in\mathcal{F}_{V}(T)\text{,}$ the shifted data $Y+(V^{\prime}-V)p_{o}$ are distributed as an observation of $\iota(\mu)\text{,}$ and $\|\widehat{\mu}-\mu\|_{2}=\|\widehat{\mu}^{\prime}(Y+(V^{\prime}-V)p_{o})-\iota(\mu)\|_{2}\text{,}$ so the risk of $\widehat{\mu}$ at $\mu$ equals the risk of $\widehat{\mu}^{\prime}$ at $\iota(\mu)\in\mathcal{F}_{V^{\prime}}(T)\text{.}$ Taking the supremum over $\mu$ and then the infimum over $\widehat{\mu}^{\prime}$ gives $R^{*}_{T}(V,\sigma)\leq R^{*}_{T}(V^{\prime},\sigma)\text{.}$</p>
</div>
<div id="S6.p14" class="ltx_para">
<p id="S6.p14.1" class="ltx_p"><em id="S6.p14.1.1" class="ltx_emph ltx_font_italic">Monotonicity in $\sigma\text{.}$</em> Let $\sigma\leq\sigma^{\prime}$ and let $W\sim N(0,(\sigma^{\prime 2}-\sigma^{2})I_{n})$ be independent of the data. For any estimator $\widehat{\mu}^{\prime}\text{,}$ the randomized procedure $\widehat{\mu}^{\prime}(Y+W)$ has, at every $\mu\text{,}$ the risk of $\widehat{\mu}^{\prime}$ under noise level $\sigma^{\prime}\text{;}$ replacing it by its average $\widehat{\mu}(Y):=\mathbb{E}_{W}\widehat{\mu}^{\prime}(Y+W)$ only lowers the squared-error risk, by Jensen’s inequality conditionally on $Y\text{,}$ and produces a deterministic estimator. Hence $R^{*}_{T}(V,\sigma)\leq R^{*}_{T}(V,\sigma^{\prime})\text{.}$</p>
</div>
<div id="S6.p15" class="ltx_para">
<p id="S6.p15.1" class="ltx_p"><em id="S6.p15.1.1" class="ltx_emph ltx_font_italic">The quadratic bounds.</em> Scaling the observation, the parameter, and the estimator by $a&gt;0$ turns the experiment at $(V,\sigma)$ into the experiment at $(aV,a\sigma)\text{,}$ since $\mathcal{F}_{aV}(T)=a\,\mathcal{F}_{V}(T)\text{;}$ the squared error scales by $a^{2}\text{,}$ so</p>
<table id="S6.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(aV,a\sigma)\ =\ a^{2}\,R^{*}_{T}(V,\sigma)\qquad(a&gt;0).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p15.2" class="ltx_p">For $c\geq 1\text{,}$ combining this exact identity with the monotonicity just proved gives</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S6.Ex15"></span><span class="paper-eq-anchor" id="S6.Ex15X"></span><span class="paper-eq-anchor" id="S6.Ex15Xa"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle R^{*}_{T}(cV,\sigma) &amp; \displaystyle=\ c^{2}R^{*}_{T}(V,\sigma/c)\ \leq\ c^{2}R^{*}_{T}(V,\sigma), \\
\displaystyle R^{*}_{T}(V,c\sigma) &amp; \displaystyle=\ c^{2}R^{*}_{T}(V/c,\sigma)\ \leq\ c^{2}R^{*}_{T}(V,\sigma),
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S6.p15.3" class="ltx_p">using $\sigma/c\leq\sigma$ and $V/c\leq V\text{.}$
∎</p>
</div>
<div id="S6.p16" class="ltx_para">
<p id="S6.p16.1" class="ltx_p">Two consequences are used repeatedly. First, for every amplitude $v&gt;0$ and every working scale $s\in[\sigma/2,4\sigma]\text{,}$ monotonicity and the quadratic bound at $c=4$ give</p>
<table id="S6.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{*}_{T}(v,s)\ \leq\ R^{*}_{T}(v,4\sigma)\ \leq\ 16\,R^{*}_{T}(v,\sigma).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.2)</span></td></tr></tbody>
</table>
<p id="S6.p16.2" class="ltx_p">Second, $k_{\mathrm{alg}}(T,v,s)\leq k_{0}(T,v,s)$ by Lemma 2.3(3), and the middle term below is at most $CR^{*}_{T}(v,s)$ by Theorem 1 at $(v,s)\text{,}$ so <a href="#S6.E2" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.2</span></a> gives</p>
<table id="S6.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\min\bigl\{v^{2}H_{T},\ s^{2}k_{\mathrm{alg}}(T,v,s)\bigr\}\ \leq\ \min\bigl\{v^{2}H_{T},\ s^{2}k_{0}(T,v,s)\bigr\}\ \leq\ C\,R^{*}_{T}(v,\sigma),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.3)</span></td></tr></tbody>
</table>
<p id="S6.p16.3" class="ltx_p">valid for all $v&gt;0$ and $s\in[\sigma/2,4\sigma]\text{.}$</p>
</div>
<div id="S6.p17" class="ltx_para">
<p id="S6.p17.1" class="ltx_p">The amplitude-free half of the candidate system rests on the subspace approximation (4.7), verified next with an explicit constant.</p>
</div>
<div id="S6.Thmlemma3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmlemma3.2" class="ltx_text ltx_font_bold">Lemma S.6.3</span></span><span id="S6.Thmlemma3.3" class="ltx_text ltx_font_bold"> (Subspace approximation).</span></h6>
<div id="S6.Thmlemma3.p1" class="ltx_para">
<p id="S6.Thmlemma3.p1.1" class="ltx_p"><span id="S6.Thmlemma3.p1.1.1" class="ltx_text ltx_font_italic">For every $\mu\in\mathcal{F}_{V}(T)$ and every integer $2\leq k\leq n/C_{\star}$ there is an admissible support $S$ with</span></p>
<table id="S6.Ex16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{dist}^{2}\bigl(\mu,\ \mathcal{V}_{k,S}\bigr)\ \leq\ 22\,V^{2}\overline{\delta}_{k}(T).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S6.p18" class="ltx_para">
<p id="S6.p18.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S6.p19" class="ltx_para">
<p id="S6.p19.1" class="ltx_p">Run the proof of Proposition 3.1 on the normalized signal $f:=\mu/V\text{,}$ retaining its objects: the terminal cells $L$ with masses $\lambda_{L}$ and exits $q_{L}\text{;}$ the collapse $g$ with $\|f-g\|_{2}^{2}\leq 3\bar{\alpha}/k$ by (3.4); the skeleton $g_{0}=\sum_{h\in U}b_{h}\,p_{h}\text{,}$ supported on the set $U$ consisting of $R_{0}$ and the heavy roots, with $g=g_{0}+\sum_{L}\lambda_{L}q_{L}\text{;}$ and the exit sampling, fixed at a realization with $W\leq 2k$ and $\|\sum_{L}(Z_{L}-\lambda_{L})q_{L}\|_{2}^{2}\leq 8\bar{\alpha}/k\text{.}$ Keep the skeleton unrounded and set</p>
<table id="S6.Ex17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\nu\ :=\ g_{0}+\sum_{L}Z_{L}q_{L},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p19.2" class="ltx_p">a real linear combination of $\{p_{v}:\ v\in U\cup\{a_{L}:Z_{L}\neq 0\}\}\text{.}$ The set $S:=\bigl(U\cup\{a_{L}:Z_{L}\neq 0\}\bigr)\setminus R_{0}$ is admissible: the heavy roots carry total activation charge below $2k$ by <a href="#S2.Thmlemma3a" title="Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.3</span></a>(3); the selected exit roots are pairwise distinct with $\widetilde{\omega}(a_{L})\leq m(L)\text{,}$ so their charges total at most $W\leq 2k\text{;}$ and a union is charged at most the sum of its parts. Hence $\sum_{v\in S}\widetilde{\omega}(v)\leq 4k\text{.}$ Since $\nu\in\mathcal{V}_{k,S}$ and $f-\nu=(f-g)+\sum_{L}(\lambda_{L}-Z_{L})q_{L}\text{,}$</p>
<table id="S6.Ex18" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{dist}^{2}\bigl(f,\ \mathcal{V}_{k,S}\bigr)\ \leq\ \|f-\nu\|_{2}^{2}\ \leq\ 2\,\frac{3\bar{\alpha}}{k}+2\,\frac{8\bar{\alpha}}{k}\ =\ 22\,\frac{\bar{\alpha}}{k}\ =\ 22\,\overline{\delta}_{k}(T).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p19.3" class="ltx_p">Restoring the amplitude multiplies the squared distance by $V^{2}\text{.}$
∎</p>
</div>
<div id="S6.p20" class="ltx_para">
<p id="S6.p20.1" class="ltx_p">Selecting over the capped subspaces requires listing them; this is the enumeration claim of Section 4.3.</p>
</div>
<div id="S6.Thmlemma4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmlemma4.2" class="ltx_text ltx_font_bold">Lemma S.6.4</span></span><span id="S6.Thmlemma4.3" class="ltx_text ltx_font_bold"> (Support enumeration).</span></h6>
<div id="S6.Thmlemma4.p1" class="ltx_para">
<p id="S6.Thmlemma4.p1.1" class="ltx_p"><span id="S6.Thmlemma4.p1.1.1" class="ltx_text ltx_font_italic">For every integer $2\leq k\leq n/C_{\star}\text{,}$ the admissible supports at budget $k$ number at most $e^{C_{1}k}\text{,}$ and they can be listed in $O(|A_{k}|\,e^{C_{1}k})$ operations.</span></p>
</div>
</div>
<div id="S6.p21" class="ltx_para">
<p id="S6.p21.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S6.p22" class="ltx_para">
<p id="S6.p22.1" class="ltx_p">An admissible support is a subset of $A_{k}\setminus R_{0}$ of total activation charge at most $4k\leq 9k\text{,}$ hence one of the charged parts counted in the proof of <a href="#S2.Thmlemma5" title="Lemma S.2.5 (Counting bound). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.5</span></a>, where the generating-function estimate bounds their number by $e^{19k}\leq e^{C_{1}k}\text{.}$ To enumerate, fix a linear order on $A_{k}\setminus R_{0}$ and run a depth-first search over subsets that appends only higher-indexed vertices and recurses only while the accumulated charge remains at most $4k\text{.}$ Every node visited by the search is an admissible support, every admissible support is visited exactly once, along the insertion order of its elements, and testing all extensions of a visited support costs $O(|A_{k}|)$ operations.
∎</p>
</div>
<div id="S6.p23" class="ltx_para">
<p id="S6.p23.1" class="ltx_p"><em id="S6.p23.1.1" class="ltx_emph ltx_font_italic">The candidate system.</em> The estimator of Theorem 3 is the penalized selection of <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> over the candidates described in Section 4.3, which we now fix precisely. The system is parameterized by a working scale $s\text{,}$ equal to $\sigma$ in Theorem 3 and to the rounded noise estimate in Theorem 4. Fix a universal threshold $n_{\star}$ such that</p>
<table id="S6.Ex19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Bigl\lfloor\frac{\log n}{2C_{1}}\Bigr\rfloor\ \geq\ 2\qquad\text{and}\qquad\Bigl\lfloor\frac{\log n}{2C_{1}}\Bigr\rfloor\ \leq\ \Bigl\lfloor\frac{n}{C_{\star}}\Bigr\rfloor\qquad\text{for every }n\geq n_{\star}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p23.2" class="ltx_p">For $n&lt;n_{\star}$ the estimator returns $Y\text{,}$ whose risk $n\sigma^{2}\leq n_{\star}\sigma^{2}$ is absorbed by the additive $\sigma^{2}$ after enlarging the universal constant; assume $n\geq n_{\star}$ from here on, and set $k^{\star}:=\lfloor\log n/(2C_{1})\rfloor\text{,}$ so that $2\leq k^{\star}\leq K\text{.}$ Write</p>
<table id="S6.Ex20" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$v_{i}:=(Y_{o})_{+}+2^{i}s\ \ (0\leq i\leq J^{+}),\qquad v^{-}_{j}:=2^{-j}s\ \ (1\leq j\leq J^{-}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p23.3" class="ltx_p">with $J^{+}=J^{-}:=\lceil\log_{2}(n+1)\rceil+2\text{,}$ for the root-anchored and the low-amplitude grids. Throughout, $\mathcal{X}_{k}$ is the class (4.1) of integer states of Section 4.1. The candidates are:</p>
<ul id="S6.I5" class="ltx_itemize">
<li id="S6.I5.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S6.I5.i1.p1" class="ltx_para">
<p id="S6.I5.i1.p1.1" class="ltx_p">the subspaces $\mathcal{V}_{k,S}$ for dyadic $2\leq k\leq k^{\star}$
and admissible $S\text{,}$ with weights $\Delta_{k,S}:=(C_{1}+1)k\text{,}$ together
with $\operatorname{span}(p_{o})$ at weight $1\text{;}$</p>
</div></li>
<li id="S6.I5.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S6.I5.i2.p1" class="ltx_para">
<p id="S6.I5.i2.p1.1" class="ltx_p">the point models $\nu_{i,k,x}:=(v_{i}/k)\,x$ for $x\in\mathcal{X}_{k}$ and dyadic $2\leq k\leq K\text{,}$ at weights
$w(\nu_{i,k,x}):=2\Gamma(x)+k+i+\log_{2}k+4\text{,}$ and the root points
$\nu^{0}_{i}:=v_{i}\,p_{o}$ at weights $i+4\text{;}$ their low-amplitude
counterparts $\nu^{-}_{j,k,x}:=(v^{-}_{j}/k)\,x$ at weights
$2\Gamma(x)+k+2\log(1+j)+\log_{2}k+4\text{,}$ and $\nu^{0-}_{j}:=v^{-}_{j}\,p_{o}$ at
weights $2\log(1+j)+4\text{;}$</p>
</div></li>
<li id="S6.I5.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S6.I5.i3.p1" class="ltx_para">
<p id="S6.I5.i3.p1.1" class="ltx_p">the full model.</p>
</div></li>
</ul>
<p id="S6.p23.4" class="ltx_p">The penalties are $\operatorname{pen}(m):=C_{2}s^{2}(D_{m}+\Delta_{m})$ for the affine and point models, with $\Delta_{m}$ the weight just listed, and $\operatorname{pen}(\mathrm{full}):=C_{2}s^{2}n\text{.}$ The supports $A_{k}\text{,}$ the charges $\widetilde{\omega}\text{,}$ and hence $\Gamma$ and $\mathcal{X}_{k}$ depend only on $(T,k)$ (Proposition 3.1); a grid index enters only through its amplitude and its weight, and all tie breaks are fixed, so the system and its penalties are deterministic given $(Y_{o},s)\text{.}$</p>
</div>
<div id="S6.p24" class="ltx_para">
<p id="S6.p24.1" class="ltx_p">The weights are Kraft-summable with room to spare. For the subspaces, <a href="#S6.Thmlemma4" title="Lemma S.6.4 (Support enumeration). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.4</span></a> gives</p>
<table id="S6.Ex21" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{\begin{subarray}{c}k\ \mathrm{dyadic}\\ 2\leq k\leq k^{\star}\end{subarray}}\ \sum_{S\ \mathrm{admissible}}e^{-(C_{1}+1)k}\ +\ e^{-1}\ \leq\ \sum_{\begin{subarray}{c}k\ \mathrm{dyadic}\\ k\geq 2\end{subarray}}e^{-k}+e^{-1}\ &lt;\ 0.16+0.37\ =\ 0.53.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p24.2" class="ltx_p">For the grid family, <a href="#S5.Thmlemma1" title="Lemma S.5.1 (Normalizing sum). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.1</span></a> gives $\sum_{x\in\mathcal{X}_{k}}e^{-2\Gamma(x)-k}\leq 1$ for every dyadic $k=2^{\ell}\text{,}$ so, once the price of the grid index is factored out, each amplitude contributes at most $1$ from its root candidate and $\sum_{\ell\geq 1}e^{-\ell}$ from its flow candidates, and</p>
<table id="S6.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{\text{grid models}}e^{-w}\ \leq\ \Bigl(\sum_{i\geq 0}e^{-i-4}+\sum_{j\geq 1}\frac{e^{-4}}{(1+j)^{2}}\Bigr)\Bigl(1+\sum_{\ell\geq 1}e^{-\ell}\Bigr)\\ =\ e^{-4}\Bigl(\frac{e}{e-1}+\frac{\pi^{2}}{6}-1\Bigr)\frac{e}{e-1}\ &lt;\ \frac{1}{8}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.4)</span></td></tr></tbody>
</table>
<p id="S6.p24.3" class="ltx_p">The total is below $1\text{,}$ as <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> requires.</p>
</div>
<div id="S6.p25" class="ltx_para">
<p id="S6.p25.1" class="ltx_p">The root-anchored grid is finite, and the truth can exceed its top value only after a downward root-noise fluctuation of order $n\text{.}$ The next lemma quantifies both halves of this statement; its event $\mathcal{E}_{+}$ is the one announced in Section 4.3.</p>
</div>
<div id="S6.Thmlemma5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmlemma5.2" class="ltx_text ltx_font_bold">Lemma S.6.5</span></span><span id="S6.Thmlemma5.3" class="ltx_text ltx_font_bold"> (Anchor event).</span></h6>
<div id="S6.Thmlemma5.p1" class="ltx_para">
<p id="S6.Thmlemma5.p1.1" class="ltx_p"><span id="S6.Thmlemma5.p1.1.1" class="ltx_text ltx_font_italic">Let $s\in[\sigma/2,4\sigma]\text{,}$ extend the anchored grid to $v_{i}=(Y_{o})_{+}+2^{i}s$ for all integers $i\geq 0\text{,}$ and set</span></p>
<table id="S6.Ex22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$i^{*}\ :=\ \min\{i\geq 0:\ v_{i}\geq V\},\qquad\mathcal{E}_{+}\ :=\ \{i^{*}\leq J^{+}\},\qquad Z_{o}\ :=\ Z(o).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.Thmlemma5.p1.2" class="ltx_p"><span id="S6.Thmlemma5.p1.2.1" class="ltx_text ltx_font_italic">Then:</span></p>
<ol id="S6.I6" class="ltx_enumerate">
<li id="S6.I6.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S6.I6.i1.p1" class="ltx_para">
<p id="S6.I6.i1.p1.1" class="ltx_p"><span id="S6.I6.i1.p1.1.1" class="ltx_text ltx_font_italic">pointwise,
</span>$2^{i^{*}}s\leq 2s+2\sigma|Z_{o}|$<span id="S6.I6.i1.p1.1.2" class="ltx_text ltx_font_italic">, and consequently</span></p>
<table id="S6.Ex23" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$i^{*}\leq 1+\log_{2}\bigl(1+2|Z_{o}|\bigr),\qquad v_{i^{*}}\leq V+2s+3\sigma|Z_{o}|,\qquad 0\ \leq\ v_{i^{*}}-Y_{o}\ \leq\ 2s+3\sigma|Z_{o}|,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.I6.i1.p1.2" class="ltx_p"><span id="S6.I6.i1.p1.2.1" class="ltx_text ltx_font_italic">and in expectation
</span>$\mathbb{E}\bigl[\sigma^{2}(1+i^{*})+(Y_{o}-v_{i^{*}})^{2}\bigr]\leq C\sigma^{2}$<span id="S6.I6.i1.p1.2.2" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S6.I6.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S6.I6.i2.p1" class="ltx_para">
<p id="S6.I6.i2.p1.1" class="ltx_p">$\mathcal{E}_{+}^{\,c}\subseteq\{Z_{o}&lt;-2(n+1)\}$<span id="S6.I6.i2.p1.1.1" class="ltx_text ltx_font_italic">;</span></p>
</div></li>
<li id="S6.I6.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S6.I6.i3.p1" class="ltx_para">
<p id="S6.I6.i3.p1.1" class="ltx_p"><span id="S6.I6.i3.p1.1.1" class="ltx_text ltx_font_italic">every penalized selection of this section,
the full model carrying penalty </span>$C_{2}s^{2}n$<span id="S6.I6.i3.p1.1.2" class="ltx_text ltx_font_italic"> and all penalties being
nonnegative, satisfies pathwise
</span>$\|\widehat{\mu}-\mu\|_{2}^{2}\leq 2C_{2}s^{2}n+2\sigma^{2}\|Z\|_{2}^{2}$<span id="S6.I6.i3.p1.1.3" class="ltx_text ltx_font_italic">, and therefore
</span>$\mathbb{E}\bigl[\|\widehat{\mu}-\mu\|_{2}^{2}\,\mathbf{1}_{\mathcal{E}_{+}^{c}}\bigr]\leq C\sigma^{2}$<span id="S6.I6.i3.p1.1.4" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S6.p26" class="ltx_para">
<p id="S6.p26.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S6.p27" class="ltx_para">
<p id="S6.p27.1" class="ltx_p"><em id="S6.p27.1.1" class="ltx_emph ltx_font_italic">Part (1).</em> Since $Y_{o}=V+\sigma Z_{o}$ and $(Y_{o})_{+}\geq Y_{o}\text{,}$</p>
<table id="S6.Ex24" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V-(Y_{o})_{+}\ \leq\ (V-Y_{o})_{+}\ =\ (-\sigma Z_{o})_{+}\ \leq\ \sigma|Z_{o}|.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p27.2" class="ltx_p">If $\sigma|Z_{o}|\leq s\text{,}$ then $v_{0}=(Y_{o})_{+}+s\geq V-\sigma|Z_{o}|+s\geq V\text{,}$ so $i^{*}=0$ and $2^{i^{*}}s=s\text{.}$ If $\sigma|Z_{o}|&gt;s$ and $i^{*}\geq 1\text{,}$ minimality gives $v_{i^{*}-1}&lt;V\text{,}$ that is, $2^{i^{*}-1}s&lt;V-(Y_{o})_{+}\leq\sigma|Z_{o}|\text{,}$ so $2^{i^{*}}s&lt;2\sigma|Z_{o}|\text{;}$ and if $\sigma|Z_{o}|&gt;s$ and $i^{*}=0\text{,}$ then $2^{i^{*}}s=s&lt;2\sigma|Z_{o}|\text{.}$ In every case $2^{i^{*}}s\leq 2s+2\sigma|Z_{o}|\text{,}$ and $i^{*}$ is finite, the grid values increasing to infinity. Dividing by $s\geq\sigma/2$ gives $2^{i^{*}}\leq 2+4|Z_{o}|=2(1+2|Z_{o}|)\text{,}$ which is the bound on $i^{*}\text{.}$ Next, $(Y_{o})_{+}\leq V+\sigma|Z_{o}|\text{,}$ since $Y_{o}\leq V+\sigma|Z_{o}|$ and $0\leq V\text{,}$ so $v_{i^{*}}=(Y_{o})_{+}+2^{i^{*}}s\leq V+\sigma|Z_{o}|+2s+2\sigma|Z_{o}|\text{.}$ For the last pointwise claim, $v_{i^{*}}\geq Y_{o}$ because $(Y_{o})_{+}\geq Y_{o}\text{,}$ and</p>
<table id="S6.Ex25" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$v_{i^{*}}-Y_{o}\ =\ \bigl((Y_{o})_{+}-Y_{o}\bigr)+2^{i^{*}}s\ \leq\ (-Y_{o})_{+}+2s+2\sigma|Z_{o}|\ \leq\ 2s+3\sigma|Z_{o}|,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p27.3" class="ltx_p">since $-Y_{o}=-V-\sigma Z_{o}\leq\sigma|Z_{o}|\text{.}$ In expectation, $\mathbb{E}\,i^{*}\leq 1+\log_{2}(1+2\,\mathbb{E}|Z_{o}|)\leq 3$ by concavity of $t\mapsto\log_{2}(1+2t)$ and $\mathbb{E}|Z_{o}|\leq 1\text{,}$ while $\mathbb{E}(Y_{o}-v_{i^{*}})^{2}\leq 2(2s)^{2}+18\sigma^{2}\mathbb{E}Z_{o}^{2}\leq 146\sigma^{2}\text{,}$ using $s\leq 4\sigma\text{.}$</p>
</div>
<div id="S6.p28" class="ltx_para">
<p id="S6.p28.1" class="ltx_p"><em id="S6.p28.1.1" class="ltx_emph ltx_font_italic">Part (2).</em> On $\mathcal{E}_{+}^{\,c}\text{,}$ $i^{*}&gt;J^{+}\text{,}$ so $v_{J^{+}}&lt;V$ and</p>
<table id="S6.Ex26" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(-\sigma Z_{o})_{+}\ \geq\ V-(Y_{o})_{+}\ &gt;\ 2^{J^{+}}s\ \geq\ 4(n+1)\cdot\frac{\sigma}{2}\ =\ 2(n+1)\,\sigma,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p28.2" class="ltx_p">using $2^{J^{+}}\geq 2^{\log_{2}(n+1)+2}=4(n+1)$ and $s\geq\sigma/2\text{;}$ the positive part is positive here, so it equals $-\sigma Z_{o}\text{,}$ and $Z_{o}&lt;-2(n+1)\text{.}$</p>
</div>
<div id="S6.p29" class="ltx_para">
<p id="S6.p29.1" class="ltx_p"><em id="S6.p29.1.1" class="ltx_emph ltx_font_italic">Part (3).</em> The selected criterion value is at most the full model’s, whose fit is $Y$ itself, so $\|Y-\widehat{\mu}\|_{2}^{2}\leq\|Y-\widehat{\mu}\|_{2}^{2}+\operatorname{pen}(\widehat{m})\leq\operatorname{pen}(\mathrm{full})=C_{2}s^{2}n\text{,}$ and $\|\widehat{\mu}-\mu\|_{2}^{2}\leq 2\|\widehat{\mu}-Y\|_{2}^{2}+2\|Y-\mu\|_{2}^{2}\leq 2C_{2}s^{2}n+2\sigma^{2}\|Z\|_{2}^{2}\text{.}$ Put $a:=2(n+1)\text{.}$ By part (<a href="#S6.I6.i2" title="Item 2 ‣ Lemma S.6.5 (Anchor event). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) and the independence of $Z_{o}$ from the nonroot coordinates,</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S6.EGx8"></span><span class="paper-eq-anchor" id="S6.Ex27"></span><span class="paper-eq-anchor" id="S6.Ex28"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\mathbb{E}\bigl[\|Z\|_{2}^{2}\,\mathbf{1}_{\mathcal{E}_{+}^{c}}\bigr]\space &amp; \displaystyle\leq\ (n-1)\,\mathbb{P}(Z_{o}&lt;-a)+\mathbb{E}\bigl[Z_{o}^{2}\,\mathbf{1}\{Z_{o}&lt;-a\}\bigr] \\
 &amp; \displaystyle\leq\ (n-1)\,e^{-a^{2}/2}+a\,\phi_{\mathcal{N}}(a)+\Phi_{\mathcal{N}}(-a)\ \leq\ C,
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S6.p29.2" class="ltx_p">where $\phi_{\mathcal{N}}$ is the standard normal density, the middle step by the Gaussian tail bound and one integration by parts. With $s^{2}\leq 16\sigma^{2}$ and $n\,e^{-a^{2}/2}\leq C\text{,}$ the pathwise bound integrates to $\mathbb{E}[\|\widehat{\mu}-\mu\|_{2}^{2}\mathbf{1}_{\mathcal{E}_{+}^{c}}]\leq C\sigma^{2}\text{.}$
∎</p>
</div>
<div id="S6.p30" class="ltx_para">
<p id="S6.p30.1" class="ltx_p">With the anchor in place, some grid candidate always sits close to the truth at a price the selection can afford. The lemma is stated conditionally on the root observation, matching the conditional analysis of the selection to come.</p>
</div>
<div id="S6.Thmlemma6" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmlemma6.2" class="ltx_text ltx_font_bold">Lemma S.6.6</span></span><span id="S6.Thmlemma6.3" class="ltx_text ltx_font_bold"> (Grid coverage).</span></h6>
<div id="S6.Thmlemma6.p1" class="ltx_para">
<p id="S6.Thmlemma6.p1.1" class="ltx_p"><span id="S6.Thmlemma6.p1.1.1" class="ltx_text ltx_font_italic">Condition on $Y_{o}=y_{0}\text{,}$ let $s\in[\sigma/2,4\sigma]\text{,}$ suppose $\mathcal{E}_{+}$ holds, and write $v:=v_{i^{*}}\text{,}$ $k^{\prime}:=k_{\mathrm{alg}}(T,v,s)\text{,}$ and $\widetilde{\theta}:=(y_{0},\mu_{-o})\text{.}$ Let $\mathfrak{O}$ be the minimum, over the point models of the candidate system and the full model, of the oracle values of <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> at mean $\widetilde{\theta}\text{:}$</span></p>
<table id="S6.Ex29" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathfrak{O}\ :=\ \min\Bigl\{\ \inf_{\nu}\bigl(\|\widetilde{\theta}-\nu\|_{2}^{2}+\sigma^{2}(w(\nu)+1)\bigr),\ \ \sigma^{2}n\ \Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.Thmlemma6.p1.2" class="ltx_p"><span id="S6.Thmlemma6.p1.2.1" class="ltx_text ltx_font_italic">Then, for every realization,</span></p>
<table id="S6.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathfrak{O}\ \leq\ C\Bigl(R^{*}_{T}(v,\sigma)+(y_{0}-v)^{2}+\sigma^{2}(1+i^{*})\Bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.5)</span></td></tr></tbody>
</table>
<p id="S6.Thmlemma6.p1.3" class="ltx_p"><span id="S6.Thmlemma6.p1.3.1" class="ltx_text ltx_font_italic">If moreover $V&lt;s/2\text{,}$ set $j^{*}:=\lfloor\log_{2}(s/V)\rfloor\geq 1\text{,}$ so that $v^{-}_{j^{*}}\in[V,2V]\text{;}$ if $j^{*}\leq J^{-}\text{,}$ then also</span></p>
<table id="S6.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathfrak{O}\ \leq\ C\Bigl(R^{*}_{T}\bigl(v^{-}_{j^{*}},\sigma\bigr)+\bigl(y_{0}-v^{-}_{j^{*}}\bigr)^{2}+\sigma^{2}\bigl(1+\log(1+j^{*})\bigr)\Bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.6)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S6.p31" class="ltx_para">
<p id="S6.p31.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S6.p32" class="ltx_para">
<p id="S6.p32.1" class="ltx_p">Every candidate of anchored index $i^{*}$ has root coordinate exactly $v\text{:}$ the flow candidates because their root state is $k\text{,}$ so $\nu_{i^{*},k,x}(o)=(v/k)\,k=v\text{,}$ and the root candidates trivially. Since $v\geq V\text{,}$ the translate $\mu^{\prime}:=\mu+(v-V)p_{o}$ lies in $\mathcal{F}_{v}(T)$ by Lemma 2.1 and agrees with $\mu$ off the root, with $\mu^{\prime}(o)=v\text{;}$ hence, for every such candidate $\nu\text{,}$</p>
<table id="S6.E7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|\widetilde{\theta}-\nu\|_{2}^{2}\ =\ (y_{0}-v)^{2}+\|\mu^{\prime}-\nu\|_{2}^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.7)</span></td></tr></tbody>
</table>
<p id="S6.p32.2" class="ltx_p">Let $k_{\max}$ be the largest dyadic integer at most $K\text{,}$ defined when $K\geq 2\text{,}$ so that $2k_{\max}&gt;K\text{.}$ There are three exhaustive cases.</p>
</div>
<div id="S6.p33" class="ltx_para">
<p id="S6.p33.1" class="ltx_p"><em id="S6.p33.1.1" class="ltx_emph ltx_font_italic">Case (a): $s^{2}k^{\prime}\leq v^{2}H_{T}\text{,}$ $K\geq 2\text{,}$ and $k^{\prime}\leq k_{\max}\text{.}$</em> Choose the smallest dyadic $k\geq\max\{k^{\prime},2\}\text{;}$ then $k\leq 2k^{\prime}$ and $k\leq k_{\max}\leq K\text{,}$ since $k_{\max}$ is itself a dyadic integer at least $\max\{k^{\prime},2\}\text{.}$ Proposition 3.1(1), applied to $\mu^{\prime}\in\mathcal{F}_{v}(T)$ at budget $k$ and taken with the explicit constant of its error assembly in <a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>, supplies $x^{\star}\in\mathcal{X}_{k}$ with $\Gamma(x^{\star})\leq 9k$ and</p>
<table id="S6.Ex30" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|\mu^{\prime}-\nu_{i^{*},k,x^{\star}}\|_{2}^{2}\ \leq\ 51\,v^{2}\overline{\delta}_{k}(T)\ \leq\ 51\,v^{2}\overline{\delta}_{k^{\prime}}(T)\ \leq\ 102\,A_{0}\,s^{2}k^{\prime},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p33.2" class="ltx_p">the second step by the monotonicity of $\overline{\delta}$ (Lemma 2.3(3)) and $k\geq k^{\prime}\text{,}$ the third because the dimension clause of (2.2) is silent at $k^{\prime}\leq K\text{,}$ so its surrogate crossing clause fired there: $v^{2}\overline{\delta}_{k^{\prime}}\leq 2A_{0}s^{2}k^{\prime}\text{.}$ The weight obeys</p>
<table id="S6.Ex31" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$w(\nu_{i^{*},k,x^{\star}})\ =\ 2\Gamma(x^{\star})+k+i^{*}+\log_{2}k+4\ \leq\ 19k+i^{*}+\log_{2}k+4\ \leq\ C(k^{\prime}+i^{*}+1).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p33.3" class="ltx_p">By the case hypothesis and <a href="#S6.E3" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.3</span></a>, $s^{2}k^{\prime}=\min\{v^{2}H_{T},s^{2}k^{\prime}\}\leq CR^{*}_{T}(v,\sigma)\text{,}$ and $\sigma^{2}k^{\prime}\leq 4s^{2}k^{\prime}\text{;}$ with <a href="#S6.E7" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.7</span></a>, the candidate’s oracle value is therefore at most $(y_{0}-v)^{2}+CR^{*}_{T}(v,\sigma)+C\sigma^{2}(1+i^{*})\text{,}$ which is <a href="#S6.E5" title="In Lemma S.6.6 (Grid coverage). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>.</p>
</div>
<div id="S6.p34" class="ltx_para">
<p id="S6.p34.1" class="ltx_p"><em id="S6.p34.1.1" class="ltx_emph ltx_font_italic">Case (b): $v^{2}H_{T}&lt;s^{2}k^{\prime}\text{.}$</em> Take the root candidate $\nu^{0}_{i^{*}}\text{,}$ whose nonroot coordinates vanish. By <a href="#S6.E7" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.7</span></a> and the convexity bound $\|\mu-Vp_{o}\|_{2}\leq V\sqrt{h_{T}}$ established in the proof of <a href="#S5.Thmlemma2" title="Lemma S.5.2 (Elementary branches). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.2</span></a>,</p>
<table id="S6.Ex32" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|\widetilde{\theta}-\nu^{0}_{i^{*}}\|_{2}^{2}\ =\ (y_{0}-v)^{2}+\|\mu-Vp_{o}\|_{2}^{2}\ \leq\ (y_{0}-v)^{2}+V^{2}h_{T},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p34.2" class="ltx_p">and $V^{2}h_{T}\leq v^{2}H_{T}=\min\{v^{2}H_{T},s^{2}k^{\prime}\}\leq CR^{*}_{T}(v,\sigma)$ by <a href="#S6.E3" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.3</span></a>. The weight is $i^{*}+4\text{,}$ so the oracle value is at most $(y_{0}-v)^{2}+CR^{*}_{T}(v,\sigma)+\sigma^{2}(i^{*}+5)\text{.}$</p>
</div>
<div id="S6.p35" class="ltx_para">
<p id="S6.p35.1" class="ltx_p"><em id="S6.p35.1.1" class="ltx_emph ltx_font_italic">Case (c): $s^{2}k^{\prime}\leq v^{2}H_{T}\text{,}$ and $K\leq 1$ or $k^{\prime}&gt;k_{\max}\text{.}$</em> If $K\geq 2$ and $k^{\prime}&gt;k_{\max}\text{,}$ then $K&lt;2k_{\max}&lt;2k^{\prime}$ and $n&lt;C_{\star}(K+1)\leq 2C_{\star}K&lt;4C_{\star}k^{\prime}\text{,}$ so</p>
<table id="S6.Ex33" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sigma^{2}n\ \leq\ 4s^{2}n\ &lt;\ 16\,C_{\star}\,s^{2}k^{\prime}\ \leq\ C\,R^{*}_{T}(v,\sigma)$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p35.2" class="ltx_p">by the case hypothesis and <a href="#S6.E3" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.3</span></a>: the full-model branch of $\mathfrak{O}$ qualifies. If $K\leq 1\text{,}$ then $n&lt;2C_{\star}\text{,}$ and $\sigma^{2}n\leq 2C_{\star}\sigma^{2}$ is absorbed by the term $\sigma^{2}(1+i^{*})$ of <a href="#S6.E5" title="In Lemma S.6.6 (Grid coverage). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>.</p>
</div>
<div id="S6.p36" class="ltx_para">
<p id="S6.p36.1" class="ltx_p"><em id="S6.p36.1.1" class="ltx_emph ltx_font_italic">The low-amplitude bound.</em> Let $V&lt;s/2$ and $j^{*}\leq J^{-}\text{.}$ From $2^{j^{*}}\leq s/V&lt;2^{j^{*}+1}\text{,}$ the amplitude $v^{-}_{j^{*}}=2^{-j^{*}}s$ lies in $[V,2V)\text{,}$ the translate $\mu+(v^{-}_{j^{*}}-V)p_{o}$ lies in $\mathcal{F}_{v^{-}_{j^{*}}}(T)$ and agrees with $\mu$ off the root, and every candidate of low-amplitude index $j^{*}$ has root coordinate exactly $v^{-}_{j^{*}}\text{,}$ so <a href="#S6.E7" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.7</span></a> holds with $v^{-}_{j^{*}}$ in place of $v\text{.}$ The three cases above run verbatim at the amplitude $v^{-}_{j^{*}}$ and its crossing index $k_{\mathrm{alg}}(T,v^{-}_{j^{*}},s)\text{,}$ the weight contributions $i^{*}+\log_{2}k+4$ and $i^{*}+4$ replaced by $2\log(1+j^{*})+\log_{2}k+4$ and $2\log(1+j^{*})+4\text{;}$ they yield <a href="#S6.E6" title="In Lemma S.6.6 (Grid coverage). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.6</span></a>.
∎</p>
</div>
<div id="S6.p37" class="ltx_para">
<p id="S6.p37.1" class="ltx_p">One computational ingredient remains before the assembly: the inner minimization of the selection criterion over an integer-state class. It is the min-plus analogue of the evaluation of <a href="#S5.Thmlemma4" title="Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.4</span></a>, on the same one-dimensional state and with its own overflow scalar.</p>
</div>
<div id="S6.Thmlemma7" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmlemma7.2" class="ltx_text ltx_font_bold">Lemma S.6.7</span></span><span id="S6.Thmlemma7.3" class="ltx_text ltx_font_bold"> (Min-plus evaluation).</span></h6>
<div id="S6.Thmlemma7.p1" class="ltx_para">
<p id="S6.Thmlemma7.p1.1" class="ltx_p"><span id="S6.Thmlemma7.p1.1.1" class="ltx_text ltx_font_italic">Fix an amplitude $v&gt;0\text{,}$ a dyadic budget $2\leq k\leq K\text{,}$ and a constant $c\geq 0\text{.}$ The minimum</span></p>
<table id="S6.Ex34" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$m_{v,k}\ :=\ \min_{x\in\mathcal{X}_{k}}\Bigl[\bigl\|Y-\tfrac{v}{k}\,x\bigr\|_{2}^{2}+c\,\Gamma(x)\Bigr]$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.Thmlemma7.p1.2" class="ltx_p"><span id="S6.Thmlemma7.p1.2.1" class="ltx_text ltx_font_italic">and one minimizer are computable exactly in $O(nk^{2})$ operations.</span></p>
</div>
</div>
<div id="S6.p38" class="ltx_para">
<p id="S6.p38.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S6.p39" class="ltx_para">
<p id="S6.p39.1" class="ltx_p">Write $b:=v/k$ and $D:=3k\text{.}$ The class is nonempty: the state vector with $x_{o}=k$ and all other states zero belongs to $\mathcal{X}_{k}\text{,}$ its one leak sitting at the root. Losses and charges are vertex-additive, and the admissible completions on the subtrees of distinct children are independent given the state at their parent, so the minimum is computed by a postorder dynamic program over one state per vertex.</p>
</div>
<div id="S6.p40" class="ltx_para">
<p id="S6.p40.1" class="ltx_p">As in <a href="#S5.Thmlemma5" title="Lemma S.5.5 (Pruning and compression). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.5</span></a>, every $x\in\mathcal{X}_{k}$ vanishes on a subtree disjoint from $A_{k}\text{,}$ so such a subtree contributes one state-independent constant, the sum of $Y_{w}^{2}$ over its vertices, to every candidate; and a maximal chain of vertices off $A_{k}$ with a single child subtree meeting $A_{k}$ carries one common state. Call the tree obtained by pruning the zero subtrees and contracting these chains the <em id="S6.p40.1.1" class="ltx_emph ltx_font_italic">reduced tree</em>. The cost of such a chain is the explicit quadratic $x\mapsto\sum_{u}(Y_{u}-bx)^{2}$ in the state $x$ at the reduced-tree vertex below it, generated in $O(k)$ operations from the chain’s length, sum, and sum of squares. Unlike its sum-product counterpart, the min-plus recursion retains these additive constants: the values $m_{v,k}$ of different candidates are later compared, so nothing may be dropped. The reduction partitions the vertices: each vertex $u$ of the reduced tree owns itself, the suppressed chain entering it, and the zero subtrees pruned at $u$ or along that chain. Write $\widehat{T}_{u}$ for the union of the blocks owned by $u$ and by its descendants in the reduced tree, so that $\widehat{T}_{o}=\mathsf{V}\text{,}$ and define at each such $u$ the table</p>
<table id="S6.Ex35" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$m_{u}(x)\ :=\ \min\Bigl\{\sum_{w\in\widehat{T}_{u}}(Y_{w}-bx^{\prime}_{w})^{2}+c\,\Gamma\bigl(z^{\prime}|_{\widehat{T}_{u}}\bigr)\Bigr\}\qquad(0\leq x\leq D),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p40.2" class="ltx_p">the minimum over the state vectors $x^{\prime}\in\{0,\dots,D\}^{\widehat{T}_{u}}$ with $x^{\prime}_{u}=x$ whose leaks $z^{\prime}$ vanish off $A_{k}\text{.}$</p>
</div>
<div id="S6.p41" class="ltx_para">
<p id="S6.p41.1" class="ltx_p"><em id="S6.p41.1.1" class="ltx_emph ltx_font_italic">Overflow.</em> Child states are individually at most $D\text{,}$ but their sum is not. A partial min-plus product of child tables, with conceptual value $A(t)$ at child sum $t\geq 0\text{,}$ is carried as its truncation $A(0),\dots,A(D)$ together with the overflow scalar</p>
<table id="S6.Ex36" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau_{A}\ :=\ \min_{t&gt;D}\ \bigl\{A(t)+c\,(t-D)\bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p41.2" class="ltx_p">the minimum of an empty set being $+\infty\text{.}$ For the min-plus convolution of two partial products, $H(q)=\min_{i+j=q}\{A(i)+B(j)\}\text{,}$ the values $H(0),\dots,H(D)$ cost $O(D^{2})$ directly, and partitioning the pairs $(i,j)$ with $i+j&gt;D$ according to whether each index exceeds $D$ gives the exact overflow</p>
<table id="S6.E8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau_{H}\ =\ \min\Bigl\{\min_{\begin{subarray}{c}0\leq i,j\leq D\\ i+j&gt;D\end{subarray}}\{A(i)+B(j)+c(i+j-D)\},\\ \tau_{A}+\min_{0\leq j\leq D}\{B(j)+cj\},\ \ \tau_{B}+\min_{0\leq i\leq D}\{A(i)+ci\},\ \ \tau_{A}+\tau_{B}+cD\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.8)</span></td></tr></tbody>
</table>
<p id="S6.p41.3" class="ltx_p">since $A(i)+c(i-D)$ ranges over the overflowed side: for instance, $i&gt;D$ and $j\leq D$ give $A(i)+B(j)+c(i+j-D)=[A(i)+c(i-D)]+[B(j)+cj]\text{,}$ minimized by the second block. Each merge therefore costs $O(D^{2})=O(k^{2})\text{,}$ and there are fewer than $n$ merges in the whole tree.</p>
</div>
<div id="S6.p42" class="ltx_para">
<p id="S6.p42.1" class="ltx_p"><em id="S6.p42.1.1" class="ltx_emph ltx_font_italic">The local step.</em> Let $(Q(0),\dots,Q(D),\tau_{Q})$ be the assembled child-sum table at $u\text{,}$ an empty product having $Q(0)=0\text{,}$ $Q(t)=+\infty$ for $t\geq 1\text{,}$ and $\tau_{Q}=+\infty\text{,}$ and let $\chi_{u}(x)$ be the cost of the rest of $u$’s own block: the quadratic cost of the suppressed chain entering $u\text{,}$ all of whose vertices carry the state $x\text{,}$ plus the constants of the block’s pruned subtrees, zero if the block is the singleton $\{u\}\text{.}$ If $u\notin A_{k}\text{,}$ conservation forces the child sum to equal $x\leq D\text{,}$ the overflow is irrelevant, and $m_{u}(x)=(Y_{u}-bx)^{2}+\chi_{u}(x)+Q(x)\text{.}$ If $u\in A_{k}\text{,}$ splitting on $z_{u}=0$ against $z_{u}\neq 0$ gives</p>
<table id="S6.Ex37" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$m_{u}(x)\ =\ (Y_{u}-bx)^{2}+\chi_{u}(x)+\min\Bigl\{Q(x),\ \ c\,\widetilde{\omega}(u)+\min_{t\geq 0}\bigl[Q(t)+c\,|x-t|\bigr]\Bigr\};$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p42.2" class="ltx_p">including $t=x$ in the charged branch only adds the option $Q(x)+c\widetilde{\omega}(u)\text{,}$ dominated by the first branch, so the split is exact. The inner minimum is a one-dimensional distance transform, the min-plus mirror of the recurrences in <a href="#S5.Thmlemma4" title="Lemma S.5.4 (Message recursion). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.4</span></a>: with</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S6.EGx9"></span><span class="paper-eq-anchor" id="S6.Ex38"></span><span class="paper-eq-anchor" id="S6.Ex39"></span><div class="paper-eqgroup-body">$$\begin{gathered}
\displaystyle F(0):=Q(0),\qquad F(x):=\min\{Q(x),\,F(x-1)+c\}; \\
\displaystyle B(D):=\min\{Q(D),\,\tau_{Q}\},\qquad B(x):=\min\{Q(x),\,B(x+1)+c\},
\end{gathered}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S6.p42.3" class="ltx_p">one has $F(x)=\min_{t\leq x}\{Q(t)+c(x-t)\}$ and $B(x)=\min_{t\geq x}\{Q(t)+c(t-x)\}\text{,}$ the seed at $D$ covering the overflowed sums because $\min_{t&gt;D}\{Q(t)+c(t-x)\}=\tau_{Q}+c(D-x)$ for $x\leq D\text{;}$ hence $\min_{t\geq 0}\{Q(t)+c|x-t|\}=\min\{F(x),B(x)\}\text{,}$ at cost $O(k)$ for the two passes. At the root, $x_{o}=k$ is pinned and $\widetilde{\omega}(o)=0\text{,}$ so $m_{v,k}$ is the local step evaluated at $x=k\text{.}$ Storing, at every minimum, an attaining index, an attaining block of <a href="#S6.E8" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.8</span></a>, and an attaining overflow sum, and backtracking from the root, recovers a minimizer $x\in\mathcal{X}_{k}\text{.}$ The total is $O(k^{2})$ per merge and $O(k)$ per vertex, hence $O(nk^{2})$ operations.
∎</p>
</div>
<div id="S6.p43" class="ltx_para">
<p id="S6.p43.1" class="ltx_p"><em class="ltx_title_proof">Completion of the proof of Theorem&nbsp;3, sufficiency.</em></p>
</div>
<div id="S6.p44" class="ltx_para">
<p id="S6.p44.1" class="ltx_p">The estimator is the penalized selection of <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> over the candidate system at working scale $s=\sigma\text{,}$ with penalties $C_{2}\sigma^{2}(D_{m}+\Delta_{m})$ and $C_{2}\sigma^{2}n\text{;}$ for $n&lt;n_{\star}$ it returns $Y\text{,}$ a case already absorbed. Condition on $Y_{o}=y_{0}\text{:}$ the candidate system is deterministic, the data decompose as $Y=\widetilde{\theta}+(0,\sigma Z_{-o})$ with $\widetilde{\theta}=(y_{0},\mu_{-o})\text{,}$ the noise being centered Gaussian with independent coordinates of variances at most $\sigma^{2}\text{,}$ the root variance zero, and the penalties are deterministic, so <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> applies conditionally with $E$ the whole space, $\bar{\kappa}=C_{2}\text{,}$ and $N=n\text{.}$ Since $\widetilde{\theta}-\mu=(Y_{o}-V)p_{o}\text{,}$ the pathwise root replacement</p>
<table id="S6.E9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|\widehat{\mu}-\mu\|_{2}^{2}\ \leq\ 2\,\|\widehat{\mu}-\widetilde{\theta}\|_{2}^{2}+2\,(Y_{o}-V)^{2},\qquad\mathbb{E}(Y_{o}-V)^{2}=\sigma^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.9)</span></td></tr></tbody>
</table>
<p id="S6.p44.2" class="ltx_p">converts conditional bounds on $\|\widehat{\mu}-\widetilde{\theta}\|_{2}^{2}$ into risk bounds. Write $k_{a}:=k_{\mathrm{alg}}(T,V,\sigma)$ and $r:=\min\{V^{2}H_{T},\sigma^{2}k_{a}\}\text{;}$ by Theorem 1 and the sandwich $k_{a}\leq k_{0}\leq 2k_{a}$ of Lemma 2.3(3), $r\asymp R^{*}_{T}(V,\sigma)\text{.}$ The anchor event $\mathcal{E}_{+}$ is determined by $Y_{o}\text{.}$ Its complement contributes at most $C\sigma^{2}$ to the risk, by <a href="#S6.Thmlemma5" title="Lemma S.6.5 (Anchor event). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>(3); on $\mathcal{E}_{+}\text{,}$ taking conditional expectations in <a href="#S6.E9" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.9</span></a> and applying <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> conditionally bounds the contribution by $C\,\mathbb{E}[\mathfrak{O}^{\prime}\,\mathbf{1}_{\mathcal{E}_{+}}]+C\sigma^{2}\text{,}$ where $\mathfrak{O}^{\prime}$ is the conditional oracle value of <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a>, the minimum over all candidates including the subspaces. It therefore suffices to prove</p>
<table id="S6.E10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl[\mathfrak{O}^{\prime}\,\mathbf{1}_{\mathcal{E}_{+}}\bigr]\ \leq\ C\,(r+\sigma^{2}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.10)</span></td></tr></tbody>
</table>
<p id="S6.p44.3" class="ltx_p">There are three exhaustive regimes; in the first two the bound is pointwise.</p>
</div>
<div id="S6.p45" class="ltx_para">
<p id="S6.p45.1" class="ltx_p"><em id="S6.p45.1.1" class="ltx_emph ltx_font_italic">Diameter regime: $V^{2}H_{T}\leq\sigma^{2}k_{a}\text{.}$</em> The model $\operatorname{span}(p_{o})$ contains $y_{0}p_{o}\text{,}$ and $\widetilde{\theta}-y_{0}p_{o}$ vanishes at the root and equals $\mu$ off it, so</p>
<table id="S6.Ex40" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{dist}^{2}\bigl(\widetilde{\theta},\operatorname{span}(p_{o})\bigr)\ \leq\ \|\mu-Vp_{o}\|_{2}^{2}\ \leq\ V^{2}h_{T}\ \leq\ r,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p45.2" class="ltx_p">by convexity as in <a href="#S5.Thmlemma2" title="Lemma S.5.2 (Elementary branches). ‣ S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.5.2</span></a>. Dimension and weight are one each, so $\mathfrak{O}^{\prime}\leq r+3\sigma^{2}\text{.}$</p>
</div>
<div id="S6.p46" class="ltx_para">
<p id="S6.p46.1" class="ltx_p"><em id="S6.p46.1.1" class="ltx_emph ltx_font_italic">Entropy regime with small crossing: $\sigma^{2}k_{a}&lt;V^{2}H_{T}$ and $k_{a}\leq k^{\star}/2\text{.}$</em> Choose the smallest dyadic $k\geq\max\{k_{a},2\}\text{,}$ so that $k\leq\max\{2k_{a},2\}\leq k^{\star}$ and $k\leq 4k_{a}\text{.}$ Since $k_{a}\leq k^{\star}/2\leq K/2\text{,}$ the dimension clause of (2.2) is silent at $k_{a}\text{,}$ so its surrogate crossing clause fired there: $V^{2}\overline{\delta}_{k_{a}}\leq 2A_{0}\sigma^{2}k_{a}\text{.}$ <a href="#S6.Thmlemma3" title="Lemma S.6.3 (Subspace approximation). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.3</span></a> at budget $k$ and the monotonicity of $\overline{\delta}$ (Lemma 2.3(3)) give an admissible $S$ with</p>
<table id="S6.Ex41" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{dist}^{2}\bigl(\mu,\ \mathcal{V}_{k,S}\bigr)\ \leq\ 22\,V^{2}\overline{\delta}_{k}\ \leq\ 22\,V^{2}\overline{\delta}_{k_{a}}\ \leq\ 44\,A_{0}\,\sigma^{2}k_{a}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p46.2" class="ltx_p">The root indicator $p_{o}$ lies in every profile subspace, $o$ being in $R_{0}\text{,}$ so translating an approximant of $\mu$ by $(y_{0}-V)p_{o}$ shows $\operatorname{dist}(\widetilde{\theta},\mathcal{V}_{k,S})\leq\operatorname{dist}(\mu,\mathcal{V}_{k,S})\text{.}$ With $\dim\mathcal{V}_{k,S}\leq|R_{0}|+|S|\leq(e+4)k$ and $\Delta_{k,S}=(C_{1}+1)k\text{,}$ the oracle value of this subspace is at most $44A_{0}\sigma^{2}k_{a}+C\sigma^{2}k\leq C\sigma^{2}k_{a}=Cr\text{.}$</p>
</div>
<div id="S6.p47" class="ltx_para">
<p id="S6.p47.1" class="ltx_p"><em id="S6.p47.1.1" class="ltx_emph ltx_font_italic">Entropy regime with large crossing: $\sigma^{2}k_{a}&lt;V^{2}H_{T}$ and $k_{a}&gt;k^{\star}/2\text{.}$</em> Suppose first $V\geq\sigma/2\text{.}$ On $\mathcal{E}_{+}\text{,}$ <a href="#S6.Thmlemma5" title="Lemma S.6.5 (Anchor event). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>(1) with $s=\sigma$ and $\sigma/V\leq 2$ gives, pointwise,</p>
<table id="S6.Ex42" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{v_{i^{*}}}{V}\ \leq\ 1+\frac{2\sigma}{V}+\frac{3\sigma|Z_{o}|}{V}\ \leq\ 5+6|Z_{o}|,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p47.2" class="ltx_p">so <a href="#S6.Thmlemma2" title="Lemma S.6.2 (Scale calculus). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.2</span></a>, at the factor $c=v_{i^{*}}/V\geq 1\text{,}$ gives $R^{*}_{T}(v_{i^{*}},\sigma)\leq(5+6|Z_{o}|)^{2}R^{*}_{T}(V,\sigma)$ pointwise, of expectation at most $CR^{*}_{T}(V,\sigma)\text{.}$ Since $\mathfrak{O}^{\prime}\leq\mathfrak{O}\text{,}$ the infimum running over more candidates, <a href="#S6.E5" title="In Lemma S.6.6 (Grid coverage). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a> and <a href="#S6.Thmlemma5" title="Lemma S.6.5 (Anchor event). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>(1) together prove <a href="#S6.E10" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.10</span></a> in this regime. Suppose now $V&lt;\sigma/2\text{.}$ The regime inequality and $H_{T}&lt;n$ give $\sigma^{2}k_{a}&lt;V^{2}H_{T}\leq V^{2}n\text{,}$ so $\sigma/V&lt;\sqrt{n/k_{a}}\leq\sqrt{n}$ and $j^{*}=\lfloor\log_{2}(\sigma/V)\rfloor$ satisfies $1\leq j^{*}\leq\tfrac{1}{2}\log_{2}n\leq J^{-}\text{.}$ The low-amplitude bound <a href="#S6.E6" title="In Lemma S.6.6 (Grid coverage). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.6</span></a> applies, and its three terms are handled in turn: $v^{-}_{j^{*}}\in[V,2V]$ and <a href="#S6.Thmlemma2" title="Lemma S.6.2 (Scale calculus). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.2</span></a> give $R^{*}_{T}(v^{-}_{j^{*}},\sigma)\leq 4R^{*}_{T}(V,\sigma)\text{;}$ the amplitude $v^{-}_{j^{*}}=2^{-j^{*}}\sigma$ is deterministic, so</p>
<table id="S6.Ex43" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl(Y_{o}-v^{-}_{j^{*}}\bigr)^{2}\ \leq\ 2\sigma^{2}\,\mathbb{E}Z_{o}^{2}+2\bigl(V-v^{-}_{j^{*}}\bigr)^{2}\ \leq\ 2\sigma^{2}+2V^{2}\ \leq\ 3\sigma^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p47.3" class="ltx_p">using $|V-v^{-}_{j^{*}}|\leq V&lt;\sigma/2\text{;}$ and, since $\log(1+t)\leq t$ and $k_{a}&gt;k^{\star}/2\geq\log n/(8C_{1})$ for $n\geq n_{\star}\text{,}$</p>
<table id="S6.Ex44" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sigma^{2}\log(1+j^{*})\ \leq\ \sigma^{2}\,\frac{\log_{2}n}{2}\ \leq\ C\,\sigma^{2}k_{a}\ =\ C\,r.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p47.4" class="ltx_p">This proves <a href="#S6.E10" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.10</span></a> in every regime, hence the risk bound of Theorem 3.</p>
</div>
<div id="S6.p48" class="ltx_para">
<p id="S6.p48.1" class="ltx_p"><em id="S6.p48.1.1" class="ltx_emph ltx_font_italic">Running time.</em> The dyadic budgets $k\leq k^{\star}$ carry $\sum_{k}e^{C_{1}k}\leq 2e^{C_{1}k^{\star}}\leq 2\sqrt{n}$ admissible supports in total, the terms of the sum growing at least geometrically; by <a href="#S6.Thmlemma4" title="Lemma S.6.4 (Support enumeration). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.4</span></a> they are listed in $O(n\sqrt{n})$ operations. One $O(n\log n)$ preprocessing pass stores every vertex’s $2^{j}$-th ancestor for $j\leq\lceil\log_{2}n\rceil$ and every root-path sum of $Y\text{;}$ lifting the deeper endpoint and then both endpoints finds the deepest common ancestor of any pair in $O(\log n)$ operations, and, by the ancestor count recorded with Lemma 2.2, $\langle p_{u},p_{w}\rangle=\operatorname{depth}(u\wedge w)+1\text{,}$ while $\langle Y,p_{u}\rangle$ is the stored root-path sum at $u\text{.}$ Forming and solving the normal equations of one subspace, of dimension $O(\log n)\text{,}$ therefore costs $O(\log^{3}n)$ operations after the preprocessing, and the subspace half costs $O(n^{3/2})$ in total, up to logarithmic factors. The grid half has $O(\log n)$ amplitudes, $O(\log n)$ budgets, and, for each pair, one run of <a href="#S6.Thmlemma7" title="Lemma S.6.7 (Min-plus evaluation). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.7</span></a> with $c=2C_{2}\sigma^{2}\text{:}$ the remaining weight $C_{2}\sigma^{2}(k+i+\log_{2}k+4)$ of a flow candidate is constant across $x\in\mathcal{X}_{k}\text{,}$ so the penalized criterion is minimized by the returned minimizer. With $k\leq n\text{,}$ the grid half costs $O(n^{3}\log^{2}n)$ operations, a conservative bound, and the final comparison across all candidates is dominated by it. All tie breaks are fixed, so the estimator is a deterministic function of $(T,\sigma,Y)\text{,}$ computable in polynomial time.
∎</p>
</div>
<div id="S6.p49" class="ltx_para">
<p id="S6.p49.1" class="ltx_p">It remains to remove the noise level; the difference statistics and their contamination bound come first. Write $\operatorname{hc}(u)$ for the size-heavy child of an internal vertex $u\text{,}$ fixed in Section 4.3, pair the children of each branching vertex by a fixed rule, one child left unpaired when their number is odd, and take</p>
<table id="S6.E11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$X_{u}\ :=\ Y_{u}-Y_{\operatorname{hc}(u)}\ \ (u\ \text{internal}),\qquad X_{c,c^{\prime}}\ :=\ Y_{c}-Y_{c^{\prime}}\ \ (\{c,c^{\prime}\}\ \text{a pair of children}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.11)</span></td></tr></tbody>
</table>
<p id="S6.p49.2" class="ltx_p">at least $(n-1)/2$ statistics in all, each a Gaussian of variance $2\sigma^{2}$ around a signal difference. For every $\varepsilon&gt;0\text{,}$ the contamination bound announced in the main body reads</p>
<table id="S6.E12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\#\bigl\{u:\ \mathbb{E}X_{u}\geq\varepsilon\sigma\bigr\}\ +\ \#\bigl\{\{c,c^{\prime}\}:\ |\mathbb{E}X_{c,c^{\prime}}|\geq\varepsilon\sigma\bigr\}\ \leq\ \frac{V\,w_{T}}{\varepsilon\sigma}\ .$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.12)</span></td></tr></tbody>
</table>
</div>
<div id="S6.p50" class="ltx_para">
<p id="S6.p50.1" class="ltx_p"><em class="ltx_title_proof">Proof of <a class="ltx_ref" href="#S6.E12">(S.6.12)</a>.</em></p>
</div>
<div id="S6.p51" class="ltx_para">
<p id="S6.p51.1" class="ltx_p">Fix $\varepsilon&gt;0\text{.}$ Both counts rest on the identity, valid for every vertex set $B$ by the subtree sums of Lemma 2.1,</p>
<table id="S6.E13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{a\in B}\mu(a)\ =\ \sum_{a\in B}\ \sum_{u:\,u\succeq a}s_{u}\ =\ \sum_{u\in\mathsf{V}}s_{u}\,\#\{a\in B:\ a\preceq u\}\ ;$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.13)</span></td></tr></tbody>
</table>
<p id="S6.p51.2" class="ltx_p">when every root path meets $B$ in at most $w$ vertices, the count on the right is at most $w\text{,}$ and the leaks total $V\text{,}$ so $\sum_{a\in B}\mu(a)\leq Vw\text{.}$</p>
</div>
<div id="S6.p52" class="ltx_para">
<p id="S6.p52.1" class="ltx_p"><em id="S6.p52.1.1" class="ltx_emph ltx_font_italic">Heavy differences.</em> Every internal vertex carries exactly one heavy edge, and every vertex is the size-heavy child of at most one vertex, its parent, so the heavy edges partition $\mathsf{V}$ into vertex-disjoint paths; the <em id="S6.p52.1.2" class="ltx_emph ltx_font_italic">top</em> of such a path is the root or the lower endpoint of a light edge. The flow form of Lemma 2.1 makes every mean $\mathbb{E}X_{u}=\mu(u)-\mu(\operatorname{hc}(u))$ nonnegative, and along one heavy path the means telescope to $\mu(\mathrm{top})-\mu(\mathrm{bottom})\leq\mu(\mathrm{top})\text{.}$ A root path contains at most $w_{\mathrm{lt}}$ tops, one for the root and one per light edge it crosses, so <a href="#S6.E13" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.13</span></a>, applied to the set of tops, gives</p>
<table id="S6.Ex45" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\varepsilon\sigma\,\#\bigl\{u:\ \mathbb{E}X_{u}\geq\varepsilon\sigma\bigr\}\ \leq\ \sum_{u\ \mathrm{internal}}\mathbb{E}X_{u}\ \leq\ \sum_{\mathrm{tops}\ a}\mu(a)\ \leq\ V\,w_{\mathrm{lt}}\ .$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S6.p53" class="ltx_para">
<p id="S6.p53.1" class="ltx_p"><em id="S6.p53.1.1" class="ltx_emph ltx_font_italic">Sibling pairs.</em> The coordinates $\mu(c)$ of the children of a branching vertex $u$ are nonnegative, so a pair with $|\mathbb{E}X_{c,c^{\prime}}|=|\mu(c)-\mu(c^{\prime})|\geq\varepsilon\sigma$ contains a child whose coordinate is at least $\varepsilon\sigma\text{;}$ such children number at most $\mu(u)/(\varepsilon\sigma)\text{,}$ since $\sum_{c\in\operatorname{ch}(u)}\mu(c)\leq\mu(u)\text{,}$ and distinct pairs contain distinct children. Summing over the branching vertices, of which a root path contains at most $w_{\mathrm{br}}\text{,}$ and applying <a href="#S6.E13" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.13</span></a> to their set,</p>
<table id="S6.Ex46" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\#\bigl\{\{c,c^{\prime}\}:\ |\mathbb{E}X_{c,c^{\prime}}|\geq\varepsilon\sigma\bigr\}\ \leq\ \frac{1}{\varepsilon\sigma}\sum_{u\ \mathrm{branching}}\mu(u)\ \leq\ \frac{V\,w_{\mathrm{br}}}{\varepsilon\sigma}\ .$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p53.2" class="ltx_p">Adding the two displays gives <a href="#S6.E12" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.12</span></a>, the width being $w_{T}=w_{\mathrm{lt}}+w_{\mathrm{br}}\text{.}$
∎</p>
</div>
<div id="S6.p54" class="ltx_para">
<p id="S6.p54.1" class="ltx_p">The statistic family <a href="#S6.E11" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.11</span></a> has at least $(n-1)/2$ members: an internal vertex with $g$ children contributes the difference along its heavy edge together with $\lfloor g/2\rfloor$ sibling pairs, $1+\lfloor g/2\rfloor\geq(g+1)/2\text{,}$ and the child counts of the internal vertices sum to $n-1\text{.}$ Each vertex $u$ enters at most three statistics: its own difference $X_{u}$ when internal, the difference $X_{\operatorname{pa}(u)}$ when it is the size-heavy child of its parent, and at most one pair. Scan the family in a fixed order and retain every statistic both of whose coordinates are unused by the statistics retained so far: a retained statistic blocks at most four others, two through each coordinate, so at least a fifth of the family is retained. This produces a deterministic subfamily, relabeled $X_{1},\dots,X_{N}\text{,}$ with $N\geq(n-1)/10$ and pairwise disjoint coordinate pairs; the $X_{i}$ are therefore independent, with $X_{i}-\mathbb{E}X_{i}\sim N(0,2\sigma^{2})\text{.}$</p>
</div>
<div id="S6.Thmlemma8" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmlemma8.2" class="ltx_text ltx_font_bold">Lemma S.6.8</span></span><span id="S6.Thmlemma8.3" class="ltx_text ltx_font_bold"> (Noise estimate).</span></h6>
<div id="S6.Thmlemma8.p1" class="ltx_para">
<p id="S6.Thmlemma8.p1.1" class="ltx_p"><span id="S6.Thmlemma8.p1.1.1" class="ltx_text ltx_font_italic">Let $n\geq 2\text{,}$ write $\operatorname{med}\{|X_{1}|,\dots,|X_{N}|\}$ for the $\lceil N/2\rceil$-th smallest of the absolute values, and set</span></p>
<table id="S6.Ex47" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{\sigma}\ :=\ \frac{\operatorname{med}\{|X_{1}|,\dots,|X_{N}|\}}{\sqrt{2}\,\Phi_{\mathcal{N}}^{-1}(3/4)},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.Thmlemma8.p1.2" class="ltx_p"><span id="S6.Thmlemma8.p1.2.1" class="ltx_text ltx_font_italic">the denominator being the median of $|N(0,2)|\text{,}$ with $\Phi_{\mathcal{N}}$ the standard normal distribution function. If $V\,w_{T}\leq\sigma n/1280\text{,}$ then</span></p>
<table id="S6.Ex48" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{P}\bigl(\widehat{\sigma}\in[\sigma/2,\ 2\sigma]\bigr)\ \geq\ 1-2e^{-c(n-1)}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.Thmlemma8.p1.3" class="ltx_p"><span id="S6.Thmlemma8.p1.3.1" class="ltx_text ltx_font_italic">with a universal $c&gt;0\text{.}$</span></p>
</div>
</div>
<div id="S6.p55" class="ltx_para">
<p id="S6.p55.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S6.p56" class="ltx_para">
<p id="S6.p56.1" class="ltx_p">Call $X_{i}$ <em id="S6.p56.1.1" class="ltx_emph ltx_font_italic">clean</em> when $|\mathbb{E}X_{i}|\leq\sigma/8\text{.}$ The contamination count <a href="#S6.E12" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.12</span></a> at $\varepsilon=1/8\text{,}$ applied to the full family and hence to the subfamily, bounds the number of statistics that are not clean by $8Vw_{T}/\sigma\leq n/160\leq N/8\text{,}$ the last step because $N\geq(n-1)/10\geq n/20$ for $n\geq 2\text{.}$ A clean statistic satisfies, for every $t\geq 0\text{,}$</p>
<table id="S6.Ex49" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{P}\bigl(|X_{i}|\leq t\bigr)\ \leq\ \mathbb{P}\Bigl(|N(0,2)|\leq\frac{t}{\sigma}+\frac{1}{8}\Bigr),\qquad\mathbb{P}\bigl(|X_{i}|&gt;t\bigr)\ \leq\ \mathbb{P}\Bigl(|N(0,2)|&gt;\frac{t}{\sigma}-\frac{1}{8}\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p56.2" class="ltx_p">and two numerical evaluations of the standard normal distribution function give</p>
<table id="S6.Ex50" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{P}\bigl(|N(0,2)|\leq 0.625\bigr)\ &lt;\ 0.35\ &lt;\ \tfrac{3}{8},\qquad\mathbb{P}\bigl(|N(0,2)|&gt;1.675\bigr)\ &lt;\ 0.24\ &lt;\ \tfrac{3}{8}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p56.3" class="ltx_p">If $\operatorname{med}|X|&lt;\sigma/2\text{,}$ at least $\lceil N/2\rceil$ of the absolute values are below $\sigma/2\text{,}$ of which at least $N/2-N/8=3N/8$ belong to clean statistics, and each clean statistic falls below $\sigma/2$ with probability less than $0.35\text{.}$ If $\operatorname{med}|X|&gt;9\sigma/5\text{,}$ at least $N-\lceil N/2\rceil+1\geq N/2$ of the absolute values exceed $9\sigma/5\text{,}$ at least $3N/8$ of them clean, each clean statistic exceeding $9\sigma/5$ with probability less than $0.24\text{.}$ In either case, a count of at most $N$ independent indicators, each of success probability at most a fixed $p&lt;3/8\text{,}$ must reach $3N/8\text{.}$ For $\lambda&gt;0\text{,}$ Markov’s inequality applied to the exponential of $\lambda$ times this count bounds the probability by $[e^{-3\lambda/8}(1-p+pe^{\lambda})]^{N}\text{,}$ each missing indicator only lowering the moment generating function below the factor $1-p+pe^{\lambda}&gt;1\text{;}$ the bracket equals $1$ at $\lambda=0$ with derivative $p-\tfrac{3}{8}&lt;0\text{,}$ so a fixed small $\lambda$ makes it $e^{-c}&lt;1\text{,}$ and each probability is at most $e^{-cN}\leq e^{-c(n-1)/10}\text{;}$ renaming $c\text{,}$ the two events together have probability at most $2e^{-c(n-1)}\text{,}$ the claimed exceptional probability. On the complement of the two events, $\operatorname{med}|X|\in[\sigma/2,\,9\sigma/5]\text{;}$ since $\Phi_{\mathcal{N}}(0.6718)&lt;\tfrac{3}{4}&lt;\Phi_{\mathcal{N}}(0.6788)$ by a numerical evaluation, the denominator $\sqrt{2}\,\Phi_{\mathcal{N}}^{-1}(3/4)$ lies in $(0.95,\,0.96)\text{,}$ and</p>
<table id="S6.Ex51" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{\sigma}\ \in\ \Bigl[\frac{\sigma/2}{0.96},\ \frac{9\sigma/5}{0.95}\Bigr]\ \subseteq\ [\sigma/2,\ 2\sigma].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S6.p57" class="ltx_para">
<p id="S6.p57.1" class="ltx_p"><em class="ltx_title_proof">Completion of the proof of Theorem&nbsp;4.</em></p>
</div>
<div id="S6.p58" class="ltx_para">
<p id="S6.p58.1" class="ltx_p">For $n&lt;n_{\star}$ return $Y\text{,}$ whose risk $n\sigma^{2}\leq n_{\star}\sigma^{2}$ is absorbed as before; assume $n\geq n_{\star}\text{.}$ The estimator computes $\widehat{\sigma}\text{;}$ on the null event $\{\widehat{\sigma}=0\}$ it returns $Y\text{,}$ and otherwise it rounds upward to $\widetilde{\sigma}:=2^{\lceil\log_{2}\widehat{\sigma}\rceil}$ and runs the selection of Theorem 3 at working scale $s=\widetilde{\sigma}\text{,}$ with the weight of every subspace and point model increased by two and the penalties built from these shifted weights at scale $\widetilde{\sigma}\text{.}$ The estimator depends only on $(T,Y)\text{,}$ and its running time adds $O(n\log n)$ for the statistics and the median to the polynomial cost already accounted. We prove the risk bound with $c=1/1280$ in the regime condition.</p>
</div>
<div id="S6.p59" class="ltx_para">
<p id="S6.p59.1" class="ltx_p">Let $\widehat{E}:=\{\widehat{\sigma}\in[\sigma/2,2\sigma]\}\text{,}$ so that $\mathbb{P}(\widehat{E}^{c})\leq 2e^{-c(n-1)}$ by <a href="#S6.Thmlemma8" title="Lemma S.6.8 (Noise estimate). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.8</span></a> under the regime condition. On $\widehat{E}\text{,}$ the rounding gives $\widetilde{\sigma}\in[\sigma/2,4\sigma]\text{,}$ and $\widetilde{\sigma}$ is a power of two in that interval, hence takes at most four values determined by $\sigma\text{.}$</p>
</div>
<div id="S6.p60" class="ltx_para">
<p id="S6.p60.1" class="ltx_p"><em id="S6.p60.1.1" class="ltx_emph ltx_font_italic">On $\widehat{E}\text{.}$</em> Condition on $Y_{o}=y_{0}\text{.}$ The realized candidate-and-penalty system is one of the four deterministic systems indexed by the possible values of $\widetilde{\sigma}\text{;}$ the subspace candidates are common to all four, while the grids differ. The penalties satisfy the bracketing of <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> with respect to the true $\sigma$ on $\widehat{E}\text{:}$ with shifted weights $\Delta_{m}+2\text{,}$ since $\widetilde{\sigma}^{2}\in[\sigma^{2}/4,16\sigma^{2}]$ and $C_{2}/4=32\text{,}$</p>
<table id="S6.Ex52" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$32\,\sigma^{2}(D_{m}+\Delta_{m}+2)\ \leq\ C_{2}\widetilde{\sigma}^{2}(D_{m}+\Delta_{m}+2)\ \leq\ 16C_{2}\,\sigma^{2}(D_{m}+\Delta_{m}+2),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p60.2" class="ltx_p">and likewise for the full model, so $E=\widehat{E}$ and $\bar{\kappa}=16C_{2}\text{.}$ The proof of <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> is repeated with one change: the deviation variable is the supremum over the four systems, each paired with its own comparison model. The weight shift by two keeps the combined Kraft sum below one, since $4e^{-2}\bigl(0.53+\tfrac{1}{8}\bigr)&lt;1$ by <a href="#S6.E4" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.4</span></a> and the subspace sum, so the expectation of the deviation variable is still at most one; the basic inequality is unchanged, the selected and the comparison model both lying in the realized subsystem. The conditional oracle bound of <a href="#S6.Thmlemma1" title="Lemma S.6.1 (Weighted affine selection). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.1</span></a> therefore holds on $\widehat{E}$ for the realized system.</p>
</div>
<div id="S6.p61" class="ltx_para">
<p id="S6.p61.1" class="ltx_p">Coverage now runs as in the completion of Theorem 3, at the realized scale $s=\widetilde{\sigma}\in[\sigma/2,4\sigma]\text{,}$ with $k_{a}(s):=k_{\mathrm{alg}}(T,V,s)$ and $r_{s}:=\min\{V^{2}H_{T},s^{2}k_{a}(s)\}\text{;}$ by <a href="#S6.E3" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.3</span></a>, $r_{s}\leq CR^{*}_{T}(V,\sigma)$ uniformly over the four values, and the weight shift adds $2\sigma^{2}$ to every oracle value, absorbed by the additive term. In the diameter regime, the pointwise bound through $\operatorname{span}(p_{o})$ is unchanged. In the entropy regime with $k_{a}(s)\leq k^{\star}/2\text{,}$ the surrogate crossing at scale $s$ gives $V^{2}\overline{\delta}_{k_{a}(s)}\leq 2A_{0}s^{2}k_{a}(s)\text{,}$ and the subspace bound reads $22V^{2}\overline{\delta}_{k}\leq 44A_{0}s^{2}k_{a}(s)\leq Cr_{s}\text{.}$ In the entropy regime with $k_{a}(s)&gt;k^{\star}/2\text{:}$ for $V\geq s/2\text{,}$ <a href="#S6.Thmlemma5" title="Lemma S.6.5 (Anchor event). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>(1) gives, pointwise,</p>
<table id="S6.Ex53" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{v_{i^{*}}}{V}\ \leq\ 1+\frac{2s}{V}+\frac{3\sigma|Z_{o}|}{V}\ \leq\ 5+12\,|Z_{o}|,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p61.2" class="ltx_p">using $s/V\leq 2$ and $\sigma\leq 2s\text{,}$ so <a href="#S6.E5" title="In Lemma S.6.6 (Grid coverage). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>, <a href="#S6.Thmlemma2" title="Lemma S.6.2 (Scale calculus). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.2</span></a>, and <a href="#S6.Thmlemma5" title="Lemma S.6.5 (Anchor event). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>(1) give the bound $C(R^{*}_{T}(V,\sigma)+\sigma^{2})$ in expectation as before. For $V&lt;s/2\text{,}$ the index $j^{*}=\lfloor\log_{2}(s/V)\rfloor$ again lies in $\{1,\dots,J^{-}\}\text{,}$ since $s^{2}k_{a}(s)&lt;V^{2}H_{T}\leq V^{2}n\text{;}$ the amplitude $v^{-}_{j^{*}}=2^{-j^{*}}\widetilde{\sigma}$ now depends on the data through $\widetilde{\sigma}\text{,}$ so no independence from $Z_{o}$ is available, and the root-coordinate term of <a href="#S6.E6" title="In Lemma S.6.6 (Grid coverage). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.6</span></a> is bounded pathwise on $\widehat{E}$ instead:</p>
<table id="S6.Ex54" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\bigl(Y_{o}-v^{-}_{j^{*}}\bigr)^{2}\ \leq\ 2\sigma^{2}Z_{o}^{2}+2\bigl(V-v^{-}_{j^{*}}\bigr)^{2}\ \leq\ 2\sigma^{2}Z_{o}^{2}+2V^{2}\ \leq\ 2\sigma^{2}Z_{o}^{2}+8\sigma^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p61.3" class="ltx_p">using $v^{-}_{j^{*}}\in[V,2V]$ and $V&lt;s/2\leq 2\sigma\text{,}$ of expectation $O(\sigma^{2})\text{;}$ the weight term $\sigma^{2}\log(1+j^{*})\leq C\sigma^{2}k_{a}(s)=Cr_{s}$ as before. Finally, for every realized $s$ the omitted-anchor event is contained in $\{Z_{o}&lt;-2(n+1)\}$ by <a href="#S6.Thmlemma5" title="Lemma S.6.5 (Anchor event). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>(2), and <a href="#S6.Thmlemma5" title="Lemma S.6.5 (Anchor event). ‣ S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.6.5</span></a>(3) with $s^{2}\leq 16\sigma^{2}$ bounds its loss contribution by $C\sigma^{2}\text{.}$ Splitting along the realized anchor event and applying the pathwise root replacement <a href="#S6.E9" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.9</span></a> on it, as in the completion of Theorem 3, gives $\mathbb{E}[\|\widehat{\mu}-\mu\|_{2}^{2}\,\mathbf{1}_{\widehat{E}}]\leq C(R^{*}_{T}(V,\sigma)+\sigma^{2})\text{.}$</p>
</div>
<div id="S6.p62" class="ltx_para">
<p id="S6.p62.1" class="ltx_p"><em id="S6.p62.1.1" class="ltx_emph ltx_font_italic">Off $\widehat{E}\text{.}$</em> On $\{\widehat{\sigma}=0\}$ the loss is $\sigma^{2}\|Z\|_{2}^{2}\text{.}$ On $\{\widehat{\sigma}&gt;0\}\cap\widehat{E}^{c}\text{,}$ compare the selected criterion with $\operatorname{span}(p_{o})\text{,}$ of dimension one and shifted weight three:</p>
<table id="S6.Ex55" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|Y-\widehat{\mu}\|_{2}^{2}\ \leq\ \bigl\|Y-P_{\operatorname{span}(p_{o})}Y\bigr\|_{2}^{2}+4C_{2}\widetilde{\sigma}^{2}\ \leq\ \|Y\|_{2}^{2}+4C_{2}\widetilde{\sigma}^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p62.2" class="ltx_p">so $\|\widehat{\mu}-\mu\|_{2}\leq\|\widehat{\mu}-Y\|_{2}+\|Y-\mu\|_{2}\leq 2\|Y\|_{2}+\|\mu\|_{2}+2\sqrt{C_{2}}\,\widetilde{\sigma}\text{.}$ Pathwise, $\widetilde{\sigma}\leq 2\widehat{\sigma}\leq 3\operatorname{med}|X|\leq 3\max_{i}|X_{i}|\leq 6\|Y\|_{\infty}\leq 6\|Y\|_{2}\text{,}$ each $X_{i}$ being a difference of two coordinates of $Y\text{,}$ so all losses off $\widehat{E}$ obey $\|\widehat{\mu}-\mu\|_{2}\leq C(\|Y\|_{2}+\|\mu\|_{2})\text{.}$ For the moments: $\mu(u)\leq V$ at every vertex and $\sum_{u}\mu(u)=\sum_{x}s_{x}(\operatorname{depth}(x)+1)\leq Vn$ by Lemma 2.1, so $\|\mu\|_{2}^{2}\leq V^{2}n\text{;}$ $\mathbb{E}\|Z\|_{2}^{4}\leq 3n^{2}$ gives $\mathbb{E}\|Y\|_{2}^{4}\leq 8(\|\mu\|_{2}^{4}+\sigma^{4}\mathbb{E}\|Z\|_{2}^{4})\leq 8(V^{4}n^{2}+3\sigma^{4}n^{2})\text{;}$ and the regime condition with $w_{T}\geq 1$ gives $V\leq\sigma n/1280\text{,}$ hence $V^{4}n^{2}\leq\sigma^{4}n^{6}\text{.}$ The squared loss therefore has second moment at most $C\sigma^{4}n^{6}$ off $\widehat{E}\text{,}$ and the Cauchy–Schwarz inequality gives</p>
<table id="S6.Ex56" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl[\|\widehat{\mu}-\mu\|_{2}^{2}\,\mathbf{1}_{\widehat{E}^{c}}\bigr]\ \leq\ \bigl(C\sigma^{4}n^{6}\bigr)^{1/2}\bigl(2e^{-c(n-1)}\bigr)^{1/2}\ \leq\ C\sigma^{2}n^{3}e^{-c(n-1)/2}\ \leq\ C\sigma^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p62.3" class="ltx_p">Adding the two contributions proves Theorem 4.
∎</p>
</div>
<div id="S6.p63" class="ltx_para">
<p id="S6.p63.1" class="ltx_p">The width of the benchmark families is read off the definition in Section 4.3. A path has no light edge and no branching vertex, so $w_{T}=1\text{.}$ On the complete binary tree of height $h\text{,}$ every internal vertex has one light child edge, and a root-to-leaf path may cross a light edge and a branching vertex at each of its $h$ internal levels, so $w_{T}=(1+h)+h=2h+1\text{.}$ On a star with $m\geq 2$ leaves, and on the broom of Theorem 5, a root-to-leaf path crosses at most one light edge and one branching vertex, so $w_{T}\leq 3\text{.}$</p>
</div>
<div id="S6.p64" class="ltx_para">
<p id="S6.p64.1" class="ltx_p">The regime of Theorem 4 cannot be removed entirely by a better noise estimate. The following converse, promised at the end of Section 4.3, shows that once budgets of order $\sigma n\sqrt{\log n}$ are admitted, no estimator lands strictly within a factor $\sqrt{2}$ of the noise level, uniformly, on any tree.</p>
</div>
<div id="S6.Thmlemma9" class="ltx_theorem ltx_theorem_prop">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmlemma9.2" class="ltx_text ltx_font_bold">Proposition S.6.9</span></span><span id="S6.Thmlemma9.3" class="ltx_text ltx_font_bold"> (Noise-estimation ceiling).</span></h6>
<div id="S6.Thmlemma9.p1" class="ltx_para">
<p id="S6.Thmlemma9.p1.1" class="ltx_p"><span id="S6.Thmlemma9.p1.1.1" class="ltx_text ltx_font_italic">For every finite rooted tree and every $\sigma&gt;0\text{,}$ put
$\lambda_{n}:=\log\bigl(4(n+1)\bigr)$ and
$V_{1}:=6\,\sigma n\sqrt{\lambda_{n}}\text{.}$ In the model $Y=\mu+sZ\text{,}$
$Z\sim N(0,I_{n})\text{,}$ where $\mu$ is a monotone flow of root value at
most $V_{1}\text{,}$ that is, $\mu\in\bigcup_{0\leq V^{\prime}\leq V_{1}}\mathcal{F}_{V^{\prime}}(T)$ with $\mathcal{F}_{0}(T):=\{0\}\text{,}$ and $s\in\{\sigma,2\sigma\}\text{,}$ every estimator
$\widehat{s}=\widehat{s}(Y)$ satisfies</span></p>
<table id="S6.Ex57" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sup_{(\mu,s)}\ \mathbb{P}_{\mu,s}\Bigl(\widehat{s}\notin\bigl(s/\sqrt{2},\ \sqrt{2}\,s\bigr)\Bigr)\ \geq\ \frac{3}{8},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.Thmlemma9.p1.2" class="ltx_p"><span id="S6.Thmlemma9.p1.2.1" class="ltx_text ltx_font_italic">the supremum running over the admitted pairs. The same
bound holds for randomized estimators, by averaging over their
internal randomness.</span></p>
</div>
</div>
<div id="S6.p65" class="ltx_para">
<p id="S6.p65.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S6.p66" class="ltx_para">
<p id="S6.p66.1" class="ltx_p">The mechanism is a scale mixture: doubling the noise of a Gaussian shift is a random perturbation of its mean, and a signal whose flow inequalities all carry enough slack absorbs the perturbation without leaving the cone.</p>
</div>
<div id="S6.p67" class="ltx_para">
<p id="S6.p67.1" class="ltx_p"><em id="S6.p67.1.1" class="ltx_emph ltx_font_italic">Step 1: the mixture identity.</em> In one coordinate, with $a:=3\sigma^{2}$ and $b:=\sigma^{2}\text{,}$ the exponent of the convolution integrand of $N(0,a)$ and $N(0,b)$ completes the square as</p>
<table id="S6.Ex58" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{w^{2}}{2a}+\frac{(y-w)^{2}}{2b}\ =\ \frac{a+b}{2ab}\Bigl(w-\frac{ay}{a+b}\Bigr)^{2}+\frac{y^{2}}{2(a+b)}\ ,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p67.2" class="ltx_p">and integrating out $w$ leaves a Gaussian integral at variance $ab/(a+b)\text{;}$ the normalizers combine into that of $N(0,a+b)\text{,}$ so the convolution is $N(0,4\sigma^{2})\text{.}$ Coordinates being independent, with $\gamma:=N(0,3\sigma^{2}I_{n})$ and any fixed $\mu_{0}\in\mathbb{R}^{n}\text{,}$</p>
<table id="S6.E14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N\bigl(\mu_{0},\,4\sigma^{2}I_{n}\bigr)\ =\ \int N\bigl(\mu_{0}+w,\ \sigma^{2}I_{n}\bigr)\,d\gamma(w):$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.6.14)</span></td></tr></tbody>
</table>
<p id="S6.p67.3" class="ltx_p">the law of $Y$ at signal $\mu_{0}$ and noise $2\sigma$ is a $\gamma$-mixture of laws at noise $\sigma$ and shifted signals.</p>
</div>
<div id="S6.p68" class="ltx_para">
<p id="S6.p68.1" class="ltx_p"><em id="S6.p68.1.1" class="ltx_emph ltx_font_italic">Step 2: a signal with slack.</em> Define $\mu_{0}$ through its leaks,</p>
<table id="S6.Ex59" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$s_{v}\ :=\ \sigma\sqrt{6\,(1+|\operatorname{ch}(v)|)\,\lambda_{n}}\qquad(v\in\mathsf{V}),\qquad V_{0}\ :=\ \sum_{v}s_{v},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p68.2" class="ltx_p">so that $\mu_{0}\in\mathcal{F}_{V_{0}}(T)$ by Lemma 2.1. The Cauchy–Schwarz inequality and $\sum_{v}(1+|\operatorname{ch}(v)|)=n+(n-1)\leq 2n$ give $V_{0}\leq\sigma\sqrt{6\lambda_{n}}\,\sqrt{n}\,\sqrt{2n}=\sigma n\sqrt{12\lambda_{n}}\leq V_{1}\text{,}$ so $\mu_{0}$ is admitted. Define the legality event</p>
<table id="S6.Ex60" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$A\ :=\ \Bigl\{w\in\mathbb{R}^{\mathsf{V}}:\ w_{v}-\textstyle\sum_{c\in\operatorname{ch}(v)}w_{c}\ \geq\ -s_{v}\ \text{ for all }v\in\mathsf{V}\Bigr\}\ \cap\ \bigl\{w_{o}\leq\sigma\sqrt{6\lambda_{n}}\bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p68.3" class="ltx_p">The leak map is linear, so on $A$ the leak of $\mu_{0}+w$ at $v$ is $s_{v}+(w_{v}-\sum_{c}w_{c})\geq 0\text{:}$ the shifted signal is a monotone flow, of root value</p>
<table id="S6.Ex61" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V_{0}+w_{o}\ \leq\ \sigma n\sqrt{12\lambda_{n}}+\sigma\sqrt{6\lambda_{n}}\ \leq\ \bigl(\sqrt{12}+\sqrt{6}\bigr)\,\sigma n\sqrt{\lambda_{n}}\ \leq\ V_{1},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p68.4" class="ltx_p">hence admitted. Under $\gamma\text{,}$ the constraint at $v$ fails when a centered Gaussian of variance $3\sigma^{2}(1+|\operatorname{ch}(v)|)$ exceeds $s_{v}\text{,}$ and the root cap fails when a centered Gaussian of variance $3\sigma^{2}$ exceeds $\sigma\sqrt{6\lambda_{n}}\text{;}$ by the Gaussian tail bound each failure has probability at most $e^{-\lambda_{n}}\text{,}$ so</p>
<table id="S6.Ex62" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\gamma(A^{c})\ \leq\ (n+1)\,e^{-\lambda_{n}}\ =\ \frac{1}{4}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S6.p69" class="ltx_para">
<p id="S6.p69.1" class="ltx_p"><em id="S6.p69.1.1" class="ltx_emph ltx_font_italic">Step 3: two inseparable hypotheses.</em> Let $P:=N(\mu_{0},4\sigma^{2}I_{n})\text{,}$ the law of $Y$ at the admitted pair $(\mu_{0},2\sigma)\text{,}$ and let</p>
<table id="S6.Ex63" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Q_{A}\ :=\ \frac{1}{\gamma(A)}\int_{A}N\bigl(\mu_{0}+w,\ \sigma^{2}I_{n}\bigr)\,d\gamma(w),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p69.2" class="ltx_p">a mixture of laws at admitted pairs with noise level $\sigma\text{.}$ Splitting <a href="#S6.E14" title="In S.6 Adaptation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.6.14</span></a> over $A$ and $A^{c}$ gives $P=\gamma(A)Q_{A}+\gamma(A^{c})Q_{A^{c}}\text{,}$ so every event $B$ satisfies</p>
<table id="S6.Ex64" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\bigl|P(B)-Q_{A}(B)\bigr|\ =\ \gamma(A^{c})\,\bigl|Q_{A^{c}}(B)-Q_{A}(B)\bigr|\ \leq\ \frac{1}{4}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.p69.3" class="ltx_p">Given $\widehat{s}\text{,}$ let $B:=\{\widehat{s}&lt;\sqrt{2}\,\sigma\}\text{.}$ Then $Q_{A}(B^{c})+P(B)=1-[Q_{A}(B)-P(B)]\geq\tfrac{3}{4}\text{,}$ so at least one term is at least $\tfrac{3}{8}\text{.}$ If $P(B)\geq\tfrac{3}{8}\text{:}$ at $(\mu_{0},2\sigma)$ the event $B$ reads $\{\widehat{s}&lt;s/\sqrt{2}\}\text{,}$ outside the window. If $Q_{A}(B^{c})\geq\tfrac{3}{8}\text{:}$ a mixture average is at least $\tfrac{3}{8}\text{,}$ so some $w\in A$ has $\mathbb{P}_{\mu_{0}+w,\,\sigma}(B^{c})\geq\tfrac{3}{8}\text{,}$ and at $(\mu_{0}+w,\sigma)$ the event $B^{c}$ reads $\{\widehat{s}\geq\sqrt{2}\,s\}\text{,}$ outside the window. A randomized estimator is handled by averaging the display over its internal randomness.
∎</p>
</div>
<div id="S6.p70" class="ltx_para">
<p id="S6.p70.1" class="ltx_p">The statements deferred from Section 4.3 are now all in place.</p>
</div>
</section>
<section id="S7" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-universal-upper-bound-for-least-squares"><span class="ltx_tag ltx_tag_section">S.7 </span>The Universal Upper Bound for Least Squares</h2>

<div id="S7.p1" class="ltx_para">
<p id="S7.p1.1" class="ltx_p">This section proves the upper bound of Theorem 5, following the three blocks sketched in Section 5: the localized projection principle (<a href="#S7.Thmlemma1" title="Lemma S.7.1 (Localized projection). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.1</span></a>), the truth-localized width bound (5.10) (<a href="#S7.Thmlemma4" title="Lemma S.7.4 (Truth-localized width). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.4</span></a>), which rests on a noise-compatible choice of centers in the coded cover (<a href="#S7.Thmlemma3" title="Lemma S.7.3 (Noise-compatible centers). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.3</span></a>), and the closure of the exponent, for which <a href="#S7.Thmlemma5" title="Lemma S.7.5 (Height floor). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.5</span></a> supplies the height branch. The capped order-statistics bound of <a href="#S7.Thmlemma2" title="Lemma S.7.2 (Capped order statistics). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.2</span></a> does the repeated work inside <a href="#S7.Thmlemma3" title="Lemma S.7.3 (Noise-compatible centers). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.3</span></a>.</p>
</div>
<div id="S7.p2" class="ltx_para">
<p id="S7.p2.1" class="ltx_p">Throughout, $Z\sim N(0,I_{n})$ is the noise, $\ell_{n}:=1+\log(en)\text{,}$ and, for an integer $2\leq k\leq n/C_{\star}\text{,}$ the construction of Proposition 3.1 is in force with the notation and of <a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>: the working scale $\bar{\alpha}=k\overline{\delta}_{k}(T)\text{,}$ the nets $R_{j}$ with level weights $m_{j}=2^{j}$ and deepest-ancestor maps $a_{j}(\cdot)\text{,}$ and, for a signal $f\in\mathcal{F}_{1}(T)\text{,}$ the terminal cells $L$ with masses $\lambda_{L}$ and levels $m(L)\text{,}$ the collapse $g\text{,}$ the skeleton $g_{0}$ supported on $U\text{,}$ its rounding $\bar{g}_{0}\text{,}$ the exits $q_{L}\text{,}$ and the sampling variables $Z_{L}$ with selection weight $W\text{,}$ a notation fixed in the proof of Proposition 3.1; the unsubscripted $Z$ is always the noise. Root coordinates never contribute: every point of $\mathcal{F}_{V}(T)$ has root coordinate $V\text{,}$ so every difference below vanishes there. The Gaussian tail bound $\mathbb{P}(N(0,\tau^{2})\geq u)\leq e^{-u^{2}/(2\tau^{2})}\text{,}$ valid for $u\geq 0\text{,}$ and Gaussian concentration for Lipschitz functions <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib40" title="" class="ltx_ref">Borell, 1975</a>; <a href="#bib.bib41" title="" class="ltx_ref">Cirel’son et al., 1976</a>)</cite>, namely $\mathbb{P}\bigl(F(Z)\geq\mathbb{E}F(Z)+u\bigr)\leq e^{-u^{2}/(2\Lambda^{2})}$ for $\Lambda$-Lipschitz $F:\mathbb{R}^{n}\to\mathbb{R}\text{,}$ are used without further comment.</p>
</div>
<div id="S7.p3" class="ltx_para">
<p id="S7.p3.1" class="ltx_p">The first lemma turns a bound on the localized Gaussian width into a risk bound for the projection. It is the fixed-point principle of Chatterjee’s analysis of least squares <cite class="ltx_cite ltx_citemacro_citep">(<a href="#bib.bib14" title="" class="ltx_ref">Chatterjee, 2014</a>)</cite>, in the form quoted in Section 5; nothing in it refers to trees.</p>
</div>
<div id="S7.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S7.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma S.7.1</span></span><span id="S7.Thmlemma1.3" class="ltx_text ltx_font_bold"> (Localized projection).</span></h6>
<div id="S7.Thmlemma1.p1" class="ltx_para">
<p id="S7.Thmlemma1.p1.1" class="ltx_p"><span id="S7.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">Let $C\subseteq\mathbb{R}^{N}$ be compact and convex, let $\mu\in C\text{,}$ let $Y=\mu+\sigma Z$ with $Z\sim N(0,I_{N})\text{,}$ and let $\widehat{\mu}:=\Pi_{C}(Y)$ be the Euclidean projection of $Y$ onto $C\text{.}$ Suppose that $t\geq\sigma$ and that for every $s\geq t$</span></p>
<table id="S7.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sigma\,\mathbb{E}\,\sup\bigl\{\langle Z,x-\mu\rangle:\ x\in C,\ \|x-\mu\|_{2}\leq s\bigr\}\ \leq\ \frac{s^{2}}{4}\,.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.1)</span></td></tr></tbody>
</table>
<p id="S7.Thmlemma1.p1.2" class="ltx_p"><span id="S7.Thmlemma1.p1.2.1" class="ltx_text ltx_font_italic">Then $\mathbb{E}\|\widehat{\mu}-\mu\|_{2}^{2}\leq 33\,t^{2}\text{.}$</span></p>
</div>
</div>
<div id="S7.p4" class="ltx_para">
<p id="S7.p4.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S7.p5" class="ltx_para">
<p id="S7.p5.1" class="ltx_p">Write $\widehat{z}:=\widehat{\mu}-\mu$ and, for $s&gt;0\text{,}$ let $X_{s}$ denote the supremum in <a href="#S7.E1" title="In Lemma S.7.1 (Localized projection). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.1</span></a>, so that the hypothesis reads $\mathbb{E}X_{s}\leq s^{2}/(4\sigma)$ for $s\geq t\text{.}$ The projection is the nearest point of $C$ and $\mu\in C\text{,}$ so $\|Y-\widehat{\mu}\|_{2}^{2}\leq\|Y-\mu\|_{2}^{2}\text{;}$ expanding both sides at $Y=\mu+\sigma Z$ and cancelling $\sigma^{2}\|Z\|_{2}^{2}$ gives</p>
<table id="S7.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|\widehat{z}\|_{2}^{2}\ \leq\ 2\sigma\,\langle Z,\widehat{z}\rangle.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.2)</span></td></tr></tbody>
</table>
<p id="S7.p5.2" class="ltx_p">Fix $s\geq t$ and suppose $\|\widehat{z}\|_{2}\geq s\text{.}$ The point $\mu+s\widehat{z}/\|\widehat{z}\|_{2}$ lies in $C$ by convexity, on the segment from $\mu$ to $\widehat{\mu}\text{,}$ and within distance $s$ of $\mu\text{,}$ so</p>
<table id="S7.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$X_{s}\ \geq\ \frac{s}{\|\widehat{z}\|_{2}}\,\langle Z,\widehat{z}\rangle\ \geq\ \frac{s\,\|\widehat{z}\|_{2}}{2\sigma}\ \geq\ \frac{s^{2}}{2\sigma}\,,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p5.3" class="ltx_p">the middle inequality by <a href="#S7.E2" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.2</span></a>. As a function of $Z$ the supremum $X_{s}$ is $s$-Lipschitz, being a maximum of linear functionals with gradients of norm at most $s\text{,}$ so concentration and $\mathbb{E}X_{s}\leq s^{2}/(4\sigma)$ give</p>
<table id="S7.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{P}\bigl(\|\widehat{z}\|_{2}\geq s\bigr)\ \leq\ \mathbb{P}\Bigl(X_{s}\geq\mathbb{E}X_{s}+\frac{s^{2}}{4\sigma}\Bigr)\ \leq\ \exp\Bigl(-\frac{(s^{2}/4\sigma)^{2}}{2s^{2}}\Bigr)\ =\ e^{-s^{2}/(32\sigma^{2})}\qquad(s\geq t).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p5.4" class="ltx_p">The layer-cake formula integrates the tail:</p>
<table id="S7.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\|\widehat{z}\|_{2}^{2}\ \leq\ t^{2}+\int_{t}^{\infty}2s\,e^{-s^{2}/(32\sigma^{2})}\,ds\ =\ t^{2}+32\sigma^{2}e^{-t^{2}/(32\sigma^{2})}\ \leq\ t^{2}+32\sigma^{2}\ \leq\ 33\,t^{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p5.5" class="ltx_p">the last step by $t\geq\sigma\text{.}$
∎</p>
</div>
<div id="S7.p6" class="ltx_para">
<p id="S7.p6.1" class="ltx_p">For $C=\mathcal{F}_{V}(T)$ the expectation in <a href="#S7.E1" title="In Lemma S.7.1 (Localized projection). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.1</span></a> is the localized width $w_{\mu}(s)$ of Section 5, and the lemma is the principle stated there. Bounding $w_{\mu}$ requires expected maxima of many correlated Gaussian terms whose weights are capped individually and in total; the next lemma is the tool. For $a\in(0,1]$ and $y\in\mathbb{R}^{M}$ define</p>
<table id="S7.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathfrak{M}_{a}(y)\ :=\ \sup\Bigl\{\,\sum_{i=1}^{M}w_{i}y_{i}:\ 0\leq w_{i}\leq a\ \text{ for all }i,\ \ \sum_{i=1}^{M}w_{i}\leq 1\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.3)</span></td></tr></tbody>
</table>
<p id="S7.p6.2" class="ltx_p">the largest weighted sum under a cap on each weight and on the total.</p>
</div>
<div id="S7.Thmlemma2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S7.Thmlemma2.2" class="ltx_text ltx_font_bold">Lemma S.7.2</span></span><span id="S7.Thmlemma2.3" class="ltx_text ltx_font_bold"> (Capped order statistics).</span></h6>
<div id="S7.Thmlemma2.p1" class="ltx_para">
<p id="S7.Thmlemma2.p1.1" class="ltx_p"><span id="S7.Thmlemma2.p1.1.1" class="ltx_text ltx_font_italic">Let $G_{1},\dots,G_{M}$ be jointly Gaussian, each centered with variance at most $\tau^{2}\text{,}$ not necessarily independent, and let $a\in(0,1]\text{.}$ Then</span></p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S7.EGx10"></span><span class="paper-eq-anchor" id="S7.Ex4"></span><span class="paper-eq-anchor" id="S7.Ex5"></span><div class="paper-eqgroup-body">$$\begin{gathered}
\displaystyle\mathbb{E}\,\mathfrak{M}_{a}(G_{1},\dots,G_{M})\ \leq\ C\tau\sqrt{1+[\log(Ma)]_{+}}\,, \\
\displaystyle\mathbb{E}\,\mathfrak{M}_{a}\bigl(G_{1}^{2},\dots,G_{M}^{2}\bigr)\ \leq\ C\tau^{2}\bigl(1+[\log(Ma)]_{+}\bigr).
\end{gathered}$$</div><div class="paper-eqgroup-no"></div></div>

</div>
</div>
<div id="S7.p7" class="ltx_para">
<p id="S7.p7.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S7.p8" class="ltx_para">
<p id="S7.p8.1" class="ltx_p">Write $G_{(1)}^{+}\geq G_{(2)}^{+}\geq\cdots$ for the decreasing rearrangement of the positive parts $[G_{i}]_{+}$ and $Q_{(1)}\geq Q_{(2)}\geq\cdots$ for that of the squares $G_{i}^{2}\text{,}$ and set $q:=\min\{\lceil 1/a\rceil,M\}\text{.}$</p>
</div>
<div id="S7.p9" class="ltx_para">
<p id="S7.p9.1" class="ltx_p"><em id="S7.p9.1.1" class="ltx_emph ltx_font_italic">Reduction to order statistics.</em> A feasible weight vector puts total weight at most $1\text{,}$ each entry at most $a\text{,}$ and gains nothing from coordinates where $G_{i}&lt;0\text{;}$ moving weight from a smaller to a larger positive coordinate only increases the sum, so the supremum is attained by filling the largest positive coordinates to capacity $a\text{,}$ with at most one fractional entry. Since $aq\geq 1$ when $q=\lceil 1/a\rceil\text{,}$ while all $M$ coordinates are already covered when $q=M\text{,}$</p>
<table id="S7.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathfrak{M}_{a}(G)\ \leq\ a\sum_{j\leq q}G_{(j)}^{+},\qquad\mathfrak{M}_{a}(G_{1}^{2},\dots,G_{M}^{2})\ \leq\ a\sum_{j\leq q}Q_{(j)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.4)</span></td></tr></tbody>
</table>
</div>
<div id="S7.p10" class="ltx_para">
<p id="S7.p10.1" class="ltx_p"><em id="S7.p10.1.1" class="ltx_emph ltx_font_italic">Tails of the order statistics.</em> If $G_{(j)}^{+}\geq u$ for some $u&gt;0\text{,}$ at least $j$ of the $G_{i}$ are at least $u\text{;}$ Markov’s inequality applied to the count, whose mean is at most $Me^{-u^{2}/(2\tau^{2})}$ by the Gaussian tail bound, gives</p>
<table id="S7.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{P}\bigl(G_{(j)}^{+}\geq u\bigr)\ \leq\ \min\Bigl\{1,\ \frac{M}{j}\,e^{-u^{2}/(2\tau^{2})}\Bigr\},\qquad\mathbb{P}\bigl(Q_{(j)}\geq u^{2}\bigr)\ \leq\ \min\Bigl\{1,\ \frac{2M}{j}\,e^{-u^{2}/(2\tau^{2})}\Bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p10.2" class="ltx_p">the second by the same argument applied to $|G_{i}|\text{.}$ Splitting the first tail at $u_{j}\text{,}$ where $u_{j}^{2}:=2\tau^{2}\log(eM/j)\text{,}$ gives</p>
<table id="S7.p10.3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$\mathbb{E}\,G_{(j)}^{+}\ \leq\ u_{j}+\frac{M}{j}\int_{u_{j}}^{\infty}e^{-u^{2}/(2\tau^{2})}\,du\\ \leq\ u_{j}+\frac{M}{j}\cdot\frac{\tau^{2}}{u_{j}}\,e^{-u_{j}^{2}/(2\tau^{2})}\ =\ u_{j}+\frac{\tau^{2}}{e\,u_{j}}\ \leq\ C\tau\sqrt{\log\frac{eM}{j}}\,,$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p10.4" class="ltx_p">where the integrand is at most $(u/u_{j})\,e^{-u^{2}/(2\tau^{2})}\text{.}$ Splitting the second tail at $2\tau^{2}\log(2eM/j)$ gives</p>
<table id="S7.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\,Q_{(j)}\ \leq\ 2\tau^{2}\log\frac{2eM}{j}+\frac{2\tau^{2}}{e}\ \leq\ C\tau^{2}\log\frac{eM}{j}\,.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S7.p11" class="ltx_para">
<p id="S7.p11.1" class="ltx_p"><em id="S7.p11.1.1" class="ltx_emph ltx_font_italic">Summation.</em> Summing the first bound over $j\leq q$ and applying the Cauchy–Schwarz inequality to the average,</p>
<table id="S7.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$a\sum_{j\leq q}\mathbb{E}\,G_{(j)}^{+}\ \leq\ Ca\tau\,q\,\Bigl(\frac{1}{q}\sum_{j\leq q}\log\frac{eM}{j}\Bigr)^{1/2}\ \leq\ Ca\tau\,q\sqrt{2+\log(M/q)}\,,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p11.2" class="ltx_p">using $\sum_{j\leq q}\log(eM/j)=q\log(eM)-\log q!\leq q\bigl(2+\log(M/q)\bigr)\text{,}$ by $\log q!\geq q\log q-q\text{.}$ Now $aq\leq a\lceil 1/a\rceil\leq 1+a\leq 2\text{;}$ and either $q=\lceil 1/a\rceil\text{,}$ in which case $M/q\leq Ma\text{,}$ or $q=M\text{,}$ in which case $\log(M/q)=0\text{.}$ In both cases the right side is at most $C\tau\sqrt{1+[\log(Ma)]_{+}}\text{,}$ which with <a href="#S7.E4" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.4</span></a> proves the first claim. The second is identical with $\tau^{2}\log(eM/j)$ in place of $\tau\sqrt{\log(eM/j)}\text{,}$ without the Cauchy–Schwarz step.
∎</p>
</div>
<div id="S7.p12" class="ltx_para">
<p id="S7.p12.1" class="ltx_p">The heart of the matter is the next lemma: for each signal and noise realization, take the best accurate member of the coded cover; the resulting pairing with the noise, maximized over the body, is small in expectation. Its proof prices the three residuals of the construction separately, and only the last one, the sampled exits, needs the noise-dependent choice.</p>
</div>
<div id="S7.Thmlemma3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S7.Thmlemma3.2" class="ltx_text ltx_font_bold">Lemma S.7.3</span></span><span id="S7.Thmlemma3.3" class="ltx_text ltx_font_bold"> (Noise-compatible centers).</span></h6>
<div id="S7.Thmlemma3.p1" class="ltx_para">
<p id="S7.Thmlemma3.p1.1" class="ltx_p"><span id="S7.Thmlemma3.p1.1.1" class="ltx_text ltx_font_italic">Fix an integer $2\leq k\leq n/C_{\star}$ and let $\mathcal{D}_{k}$ be the coded cover at amplitude $V=1\text{.}$ For $f\in\mathcal{F}_{1}(T)$ and a noise realization $Z$ set</span></p>
<table id="S7.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathfrak{r}_{Z}(f)\ :=\ \inf\Bigl\{\langle Z,\ f-\nu\rangle:\ \nu\in\mathcal{D}_{k},\ \|f-\nu\|_{2}^{2}\leq 51\,\overline{\delta}_{k}(T)\Bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.5)</span></td></tr></tbody>
</table>
<p id="S7.Thmlemma3.p1.2" class="ltx_p"><span id="S7.Thmlemma3.p1.2.1" class="ltx_text ltx_font_italic">The infimum runs over a nonempty set for every $f$ and every $Z\text{,}$ and</span></p>
<table id="S7.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\,\sup_{f\in\mathcal{F}_{1}(T)}\mathfrak{r}_{Z}(f)\ \leq\ C\Bigl[\sqrt{\bar{\alpha}}\,\log(2+\ell_{n})+\sqrt{\overline{\delta}_{k}(T)\,\ell_{n}}\,\Bigr].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.6)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S7.p13" class="ltx_para">
<p id="S7.p13.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S7.p14" class="ltx_para">
<p id="S7.p14.1" class="ltx_p">Fix $f$ and run the proof of Proposition 3.1 on it, retaining its objects. Each realization of the sampling defines the candidate $\nu:=\bar{g}_{0}+\sum_{L}Z_{L}q_{L}\text{,}$ and the error decomposes as there:</p>
<table id="S7.E7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$f-\nu\ =\ (f-g)\ +\ (g_{0}-\bar{g}_{0})\ +\ \sum_{L}(\lambda_{L}-Z_{L})\,q_{L}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.7)</span></td></tr></tbody>
</table>
<p id="S7.p14.2" class="ltx_p">On the sampling event of that proof, call it $A\text{,}$ of probability at least $\tfrac{1}{4}\text{,}$ where $W\leq 2k$ and $\|\sum_{L}(Z_{L}-\lambda_{L})q_{L}\|_{2}^{2}\leq 8\bar{\alpha}/k\text{,}$ the candidate lies in $\mathcal{D}_{k}\text{,}$ and the three residuals assemble, as in <a href="#S2a" title="S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">S.2</span></a>, to $\|f-\nu\|_{2}^{2}\leq 3(3+6+8)\bar{\alpha}/k=51\,\overline{\delta}_{k}(T)\text{:}$ the feasible set of <a href="#S7.E5" title="In Lemma S.7.3 (Noise-compatible centers). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.5</span></a> is nonempty, for every $f$ and irrespective of $Z\text{.}$ Pairing <a href="#S7.E7" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.7</span></a> with the noise and taking on $A$ the realization that minimizes the third term,</p>
<table id="S7.E8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathfrak{r}_{Z}(f)\ \leq\ \langle Z,f-g\rangle+\langle Z,g_{0}-\bar{g}_{0}\rangle+\min_{A}\,\Bigl\langle Z,\sum_{L}(\lambda_{L}-Z_{L})q_{L}\Bigr\rangle.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.8)</span></td></tr></tbody>
</table>
<p id="S7.p14.3" class="ltx_p">The three terms are bounded uniformly over $f$ in turn; the first carries the main contribution, the second is a union bound over few subspaces, and the third is where choosing the center after the noise pays.</p>
</div>
<div id="S7.p15" class="ltx_para">
<p id="S7.p15.1" class="ltx_p"><em id="S7.p15.1.1" class="ltx_emph ltx_font_italic">The collapse residual.</em> Let $\tau(u)$ be the level of the terminal cell containing $u\text{,}$ so that $g=\sum_{u}\lambda_{u}\,p_{a_{\tau(u)}(u)}$ and the difference telescopes through the levels:</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S7.EGx11"></span><span class="paper-eq-anchor" id="S7.Ex9"></span><span class="paper-eq-anchor" id="S7.Ex10"></span><div class="paper-eqgroup-body">$$\begin{gathered}
\displaystyle f-g\ =\ \sum_{u}\lambda_{u}\bigl(p_{u}-p_{a_{\tau(u)}(u)}\bigr), \\
\displaystyle p_{u}-p_{a_{\tau(u)}(u)}\ =\ \sum_{j=\tau(u)}^{J-1}\bigl(p_{a_{j+1}(u)}-p_{a_{j}(u)}\bigr)+\bigl(p_{u}-p_{a_{J}(u)}\bigr).
\end{gathered}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="S7.p15.2" class="ltx_p">Fix a level $j&lt;J$ and group the contributions by the level-$(j{+}1)$ root: by <a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i3a" title="Item 3 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), $a_{j}(u)=a_{j}(b)$ whenever $a_{j+1}(u)=b\text{,}$ so the level-$j$ increment of every $u$ in the group of $b$ is the same vector $p_{b}-p_{a_{j}(b)}\text{,}$ of squared norm at most $d_{T}(a_{j}(b),b)\leq\bar{\alpha}/m_{j}$ by <a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i4" title="Item 4 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>). The group mass</p>
<table id="S7.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lambda_{b}\ :=\ \sum\bigl\{\lambda_{u}:\ a_{j+1}(u)=b,\ \tau(u)\leq j\bigr\}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p15.3" class="ltx_p">is capped: each member of the group lies in the level-$(j{+}1)$ cell of $b$ and in its own terminal cell, which is coarser and hence contains that whole cell; two terminal cells with a common vertex coincide, the terminal cells being a partition, so the group shares one terminal cell, stopped at a level at most $j&lt;J$ and hence light, whence $\lambda_{b}\leq m_{j}/k$ by the monotonicity of the level weights. The group masses are nonnegative and total at most one, each $\lambda_{u}$ entering at most one group, so, with $M_{j}\leq\min\{n,\,|R_{j+1}|\}\leq\min\{n,\,2ke^{2m_{j}}\}$ possible groups (<a href="#S2.Thmlemma1a" title="Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.1</span></a>(<a href="#S2.I1.i3a" title="Item 3 ‣ Lemma S.2.1 (Scale floor and net sizes). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>)),</p>
<table id="S7.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\,\sup_{f}\,\sum_{b}\lambda_{b}\,\langle Z,p_{b}-p_{a_{j}(b)}\rangle\leq\mathbb{E}\,\mathfrak{M}_{m_{j}/k}\Bigl(\bigl(\langle Z,p_{b}-p_{a_{j}(b)}\rangle\bigr)_{b}\Bigr)\leq C\sqrt{\bar{\alpha}}\,\min\bigl\{1,\sqrt{\ell_{n}/m_{j}}\bigr\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p15.4" class="ltx_p">by <a href="#S7.Thmlemma2" title="Lemma S.7.2 (Capped order statistics). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.2</span></a> with variance bound $\bar{\alpha}/m_{j}$ and cap $m_{j}/k\text{:}$ its logarithmic factor $1+[\log(M_{j}m_{j}/k)]_{+}$ is at most $\min\{5m_{j},\,\ell_{n}\}\text{,}$ being at most $1+\log 2+\log m_{j}+2m_{j}\leq 5m_{j}$ from $M_{j}m_{j}/k\leq 2m_{j}e^{2m_{j}}\text{,}$ and at most $1+\log n\leq\ell_{n}$ from $M_{j}m_{j}/k\leq n\text{.}$ Summing the dyadic levels: those with $m_{j}\leq\ell_{n}$ number at most $C\log(2+\ell_{n})$ and contribute $C\sqrt{\bar{\alpha}}$ each, while over the rest $\sqrt{\ell_{n}/m_{j}}$ is geometrically decaying from below one, and sums to a constant. The final increments $p_{u}-p_{a_{J}(u)}$ number at most $n$ and have squared norms at most $\bar{\alpha}/m_{J}\leq 2\overline{\delta}_{k}(T)\text{,}$ and their mass-weighted sum is a feasible value of $\mathfrak{M}_{1}\text{;}$ so <a href="#S7.Thmlemma2" title="Lemma S.7.2 (Capped order statistics). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.2</span></a> with cap $1$ and variance bound $2\overline{\delta}_{k}(T)$ bounds its expected supremum by $C\sqrt{\overline{\delta}_{k}(T)}\,\sqrt{1+\log n}\leq C\sqrt{\overline{\delta}_{k}(T)\,\ell_{n}}\text{.}$ Altogether</p>
<table id="S7.E9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\,\sup_{f}\ \langle Z,\ f-g\rangle\ \leq\ C\Bigl[\sqrt{\bar{\alpha}}\,\log(2+\ell_{n})+\sqrt{\overline{\delta}_{k}(T)\,\ell_{n}}\,\Bigr].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.9)</span></td></tr></tbody>
</table>
</div>
<div id="S7.p16" class="ltx_para">
<p id="S7.p16.1" class="ltx_p"><em id="S7.p16.1.1" class="ltx_emph ltx_font_italic">The rounding residual.</em> The difference $g_{0}-\bar{g}_{0}$ has squared norm at most $6\bar{\alpha}/k\text{,}$ by the constant recorded after <a href="#S2.Thmlemma3a" title="Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.3</span></a>, and lies in the span of $\{p_{h}:h\in U\}\text{.}$ The set $U\setminus R_{0}$ consists of heavy roots, of total activation charge below $2k$ by <a href="#S2.Thmlemma3a" title="Lemma S.2.3 (The heavy structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.3</span></a>(3); it is therefore one of the charged parts counted in the proof of <a href="#S2.Thmlemma5" title="Lemma S.2.5 (Counting bound). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.5</span></a>, so at most $e^{19k}$ sets $U\text{,}$ hence at most $e^{19k}$ subspaces $V_{U}:=\operatorname{span}\{p_{h}:h\in U\}\text{,}$ occur as $f$ varies. Each has dimension $|U|\leq|R_{0}|+k\leq ek+k\leq 4k\text{,}$ since a heavy root outside $R_{0}$ carries charge at least $m_{1}=2\text{.}$ For any fixed $U\text{,}$</p>
<table id="S7.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sup\bigl\{\langle Z,z\rangle:\ z\in V_{U},\ \|z\|_{2}^{2}\leq 6\bar{\alpha}/k\bigr\}\ =\ \sqrt{6\bar{\alpha}/k}\,\bigl\|P_{V_{U}}Z\bigr\|_{2},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p16.2" class="ltx_p">and $\|P_{V_{U}}Z\|_{2}$ is a $1$-Lipschitz function of $Z$ with mean at most $\sqrt{\dim V_{U}}\leq 2\sqrt{k}\text{.}$ Concentration and a union bound give, for $u\geq 0\text{,}$ $\mathbb{P}(\max_{U}\|P_{V_{U}}Z\|_{2}\geq 2\sqrt{k}+\sqrt{38k}+u)\leq e^{19k}e^{-(\sqrt{38k}+u)^{2}/2}\leq e^{-u^{2}/2}\text{,}$ so $\mathbb{E}\max_{U}\|P_{V_{U}}Z\|_{2}\leq 2\sqrt{k}+\sqrt{38k}+2\leq C\sqrt{k}$ and</p>
<table id="S7.E10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\,\sup_{f}\ \langle Z,\ g_{0}-\bar{g}_{0}\rangle\ \leq\ \sqrt{6\bar{\alpha}/k}\cdot C\sqrt{k}\ =\ C\sqrt{\bar{\alpha}}\,.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.10)</span></td></tr></tbody>
</table>
</div>
<div id="S7.p17" class="ltx_para">
<p id="S7.p17.1" class="ltx_p"><em id="S7.p17.1.1" class="ltx_emph ltx_font_italic">The exit pairing.</em> Condition on $Z$ and on $f\text{,}$ so that only the sampling is random, and write $X:=\langle Z,\sum_{L}(\lambda_{L}-Z_{L})q_{L}\rangle\text{.}$ The sampling variables are independent with $\mathbb{E}Z_{L}=\lambda_{L}$ and $\operatorname{Var}(Z_{L})\leq\lambda_{L}m(L)/k\text{,}$ so $X$ is centered with</p>
<table id="S7.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\,X^{2}\ =\ \sum_{L}\operatorname{Var}(Z_{L})\,\langle Z,q_{L}\rangle^{2}\ \leq\ \sum_{L}\lambda_{L}\,\frac{m(L)}{k}\,\langle Z,q_{L}\rangle^{2}\ =:\ S_{f}(Z)^{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p17.2" class="ltx_p">Centeredness and the Cauchy–Schwarz inequality give</p>
<table id="S7.Ex15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\bigl[X\ \big|\ A\bigr]\ =\ -\frac{\mathbb{E}\bigl[X\,\mathbf{1}_{A^{c}}\bigr]}{\mathbb{P}(A)}\ \leq\ \frac{(\mathbb{E}X^{2})^{1/2}\,\mathbb{P}(A^{c})^{1/2}}{\mathbb{P}(A)}\ \leq\ 4\,S_{f}(Z),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p17.3" class="ltx_p">and some realization in $A$ is no larger than this conditional expectation. Hence the third term of <a href="#S7.E8" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.8</span></a> is at most $4S_{f}(Z)\text{,}$ and it remains to prove</p>
<table id="S7.E11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\,\sup_{f}\ S_{f}(Z)^{2}\ \leq\ C\bar{\alpha},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.11)</span></td></tr></tbody>
</table>
<p id="S7.p17.4" class="ltx_p">which gives $\mathbb{E}\sup_{f}S_{f}(Z)\leq\sqrt{\mathbb{E}\sup_{f}S_{f}(Z)^{2}}\leq C\sqrt{\bar{\alpha}}$ by Jensen’s inequality. An exit $q_{L}$ is determined by the root $a_{L}$ of its cell: its other endpoint is the root of the parent cell (<a href="#S2.Thmlemma2a" title="Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.2.2</span></a>(<a href="#S2.I3.i3a" title="Item 3 ‣ Lemma S.2.2 (Cell structure). ‣ S.2 The Coded Cover ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>)), so at level $m$ the possible exits number at most $\min\{n,2ke^{m}\}\text{,}$ with $\|q_{L}\|_{2}^{2}\leq 2\bar{\alpha}/m$ by the parent cell’s radius. Split $S_{f}(Z)^{2}$ by levels. At a level $m\leq\ell_{n}\text{,}$ the weights $\lambda_{L}\leq m/k$ are again capped with total at most one, so <a href="#S7.Thmlemma2" title="Lemma S.7.2 (Capped order statistics). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.2</span></a>, applied to the squares with variance bound $2\bar{\alpha}/m$ and cap $m/k\text{,}$ bounds the expected supremum of the level’s sum by $C(2\bar{\alpha}/m)\bigl(1+[\log(2me^{m})]_{+}\bigr)\leq C\bar{\alpha}\text{,}$ since $1+\log(2me^{m})\leq 4m\text{;}$ with the prefactor $m/k$ the level contributes $C\bar{\alpha}\,m/k\text{,}$ and the dyadic sum over $m&lt;k$ is at most $C\bar{\alpha}\text{.}$ At the levels $m&gt;\ell_{n}\text{,}$ the prefactor obeys $m/k\leq 1$ and the weights total at most one, so the combined contribution is a feasible value of $\mathfrak{M}_{1}$ over the possible exits at these levels, at most $n(1+\log_{2}k)$ vectors of variance at most $2\bar{\alpha}/\ell_{n}\text{;}$ <a href="#S7.Thmlemma2" title="Lemma S.7.2 (Capped order statistics). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.2</span></a> with cap $1\text{,}$ applied to the squares, bounds its expectation by $C(\bar{\alpha}/\ell_{n})\bigl(1+\log(n(1+\log_{2}k))\bigr)\leq C\bar{\alpha}\text{,}$ since $1+\log\bigl(n(1+\log_{2}k)\bigr)\leq 2\ell_{n}\text{.}$ This proves <a href="#S7.E11" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.11</span></a>.</p>
</div>
<div id="S7.p18" class="ltx_para">
<p id="S7.p18.1" class="ltx_p">Combining <a href="#S7.E8" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.8</span></a> with <a href="#S7.E9" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">S.7.9</span></a>, <a href="#S7.E10" title="Equation S.7.10 ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">S.7.10</span></a> and <a href="#S7.E11" title="Equation S.7.11 ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">S.7.11</span></a>,</p>
<table id="S7.Ex16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\,\sup_{f}\mathfrak{r}_{Z}(f)\ \leq\ C\Bigl[\sqrt{\bar{\alpha}}\,\log(2+\ell_{n})+\sqrt{\overline{\delta}_{k}(T)\,\ell_{n}}\,\Bigr]+C\sqrt{\bar{\alpha}}+4\,C\sqrt{\bar{\alpha}}\,,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p18.2" class="ltx_p">and $\sqrt{\bar{\alpha}}\leq\sqrt{\bar{\alpha}}\log(2+\ell_{n})$ absorbs the last two terms into the first.
∎</p>
</div>
<div id="S7.p19" class="ltx_para">
<p id="S7.p19.1" class="ltx_p">The width bound follows by recentering the local ball at a deterministic member of the cover.</p>
</div>
<div id="S7.Thmlemma4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S7.Thmlemma4.2" class="ltx_text ltx_font_bold">Lemma S.7.4</span></span><span id="S7.Thmlemma4.3" class="ltx_text ltx_font_bold"> (Truth-localized width).</span></h6>
<div id="S7.Thmlemma4.p1" class="ltx_para">
<p id="S7.Thmlemma4.p1.1" class="ltx_p"><span id="S7.Thmlemma4.p1.1.1" class="ltx_text ltx_font_italic">For every integer $2\leq k\leq n/C_{\star}\text{,}$ every $\mu\in\mathcal{F}_{V}(T)\text{,}$ and every $t&gt;0\text{,}$</span></p>
<table id="S7.Ex17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$w_{\mu}(t)\ \leq\ C\,\bigl(t+V\sqrt{\overline{\delta}_{k}(T)}\,\bigr)\sqrt{k}\ +\ C\,V\Bigl[\sqrt{k\overline{\delta}_{k}(T)}\,\log(2+\ell_{n})+\sqrt{\overline{\delta}_{k}(T)\,\ell_{n}}\,\Bigr],$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.Thmlemma4.p1.2" class="ltx_p"><span id="S7.Thmlemma4.p1.2.1" class="ltx_text ltx_font_italic">with $w_{\mu}$ the localized Gaussian width defined in Section 5; this is the display (5.10) there.</span></p>
</div>
</div>
<div id="S7.p20" class="ltx_para">
<p id="S7.p20.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S7.p21" class="ltx_para">
<p id="S7.p21.1" class="ltx_p">Abbreviate $\overline{\delta}:=\overline{\delta}_{k}(T)\text{.}$ Amplitudes rescale: for $\theta\in\mathcal{F}_{V}(T)$ the normalized signal $\theta/V$ lies in $\mathcal{F}_{1}(T)\text{,}$ and multiplying a member of the unit-amplitude cover by $V$ gives a member of $\mathcal{D}_{k}$ at amplitude $V\text{.}$ The feasible set of <a href="#S7.E5" title="In Lemma S.7.3 (Noise-compatible centers). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.5</span></a> does not depend on $Z$ and is never empty, so fix $\nu_{\mu}\text{,}$ $V$ times one of its members at $\mu/V\text{:}$ then $\|\mu-\nu_{\mu}\|_{2}\leq V\sqrt{51\overline{\delta}}$ and $\nu_{\mu}$ is deterministic. For each $\theta$ with $\|\theta-\mu\|_{2}\leq t$ and each realization of $Z\text{,}$ let $\nu_{\theta}$ be $V$ times a minimizer of <a href="#S7.E5" title="In Lemma S.7.3 (Noise-compatible centers). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.5</span></a> at $\theta/V\text{,}$ so that $\|\theta-\nu_{\theta}\|_{2}\leq V\sqrt{51\overline{\delta}}$ and $\langle Z,\theta-\nu_{\theta}\rangle=V\,\mathfrak{r}_{Z}(\theta/V)\text{.}$ Decompose</p>
<table id="S7.Ex18" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\langle Z,\ \theta-\mu\rangle\ =\ \langle Z,\ \nu_{\theta}-\nu_{\mu}\rangle+\langle Z,\ \theta-\nu_{\theta}\rangle-\langle Z,\ \mu-\nu_{\mu}\rangle.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p21.2" class="ltx_p">The last term does not depend on $\theta$ and has expectation zero, $\nu_{\mu}$ being deterministic, so it drops from the expected supremum. The middle term is at most $V\sup_{f\in\mathcal{F}_{1}(T)}\mathfrak{r}_{Z}(f)\text{,}$ whose expectation <a href="#S7.Thmlemma3" title="Lemma S.7.3 (Noise-compatible centers). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.3</span></a> bounds by the second group of the claim. For the first term, the triangle inequality confines every center met to a deterministic ball:</p>
<table id="S7.Ex19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\|\nu_{\theta}-\nu_{\mu}\|_{2}\ \leq\ \|\nu_{\theta}-\theta\|_{2}+\|\theta-\mu\|_{2}+\|\mu-\nu_{\mu}\|_{2}\ \leq\ t+2V\sqrt{51\overline{\delta}}\ =:\ \rho,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p21.3" class="ltx_p">so the first term is at most the maximum of $\langle Z,\nu-\nu_{\mu}\rangle$ over $\{\nu\in\mathcal{D}_{k}:\|\nu-\nu_{\mu}\|_{2}\leq\rho\}\text{,}$ a fixed set of at most $e^{C_{1}k}$ centered Gaussians of standard deviation at most $\rho\text{.}$ The maximum is a feasible value of $\mathfrak{M}_{1}\text{,}$ so <a href="#S7.Thmlemma2" title="Lemma S.7.2 (Capped order statistics). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.2</span></a> with cap $1$ bounds its expectation by $C\rho\sqrt{1+C_{1}k}\leq C(t+V\sqrt{\overline{\delta}}\,)\sqrt{k}\text{,}$ the first group of the claim.
∎</p>
</div>
<div id="S7.p22" class="ltx_para">
<p id="S7.p22.1" class="ltx_p">The second comparison branch of Section 5 rests on the profile remembering the height of the tree.</p>
</div>
<div id="S7.Thmlemma5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S7.Thmlemma5.2" class="ltx_text ltx_font_bold">Lemma S.7.5</span></span><span id="S7.Thmlemma5.3" class="ltx_text ltx_font_bold"> (Height floor).</span></h6>
<div id="S7.Thmlemma5.p1" class="ltx_para">
<p id="S7.Thmlemma5.p1.1" class="ltx_p"><span id="S7.Thmlemma5.p1.1.1" class="ltx_text ltx_font_italic">For every finite rooted tree and every integer $1\leq k\leq n/C_{\star}\text{,}$</span></p>
<table id="S7.Ex20" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\delta_{k}(T)\ \geq\ \frac{\log 2}{8}\cdot\frac{H_{T}}{k^{2}}\,.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S7.p23" class="ltx_para">
<p id="S7.p23.1" class="ltx_p"><em class="ltx_title_proof">Proof.</em></p>
</div>
<div id="S7.p24" class="ltx_para">
<p id="S7.p24.1" class="ltx_p">Write $h:=h_{T}\text{,}$ so that $H_{T}\leq 2h\text{,}$ and fix a root-to-leaf path with $h$ edges; every ancestor of a vertex of the path lies on the path, so ancestor covering restricted to it is interval covering of its $h+1$ vertices, as on the path of <a href="#S4.Thmlemma1a" title="Lemma S.4.1 (Path profile). ‣ S.4 Benchmark and Broom Profiles ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.4.1</span></a>.</p>
</div>
<div id="S7.p25" class="ltx_para">
<p id="S7.p25.1" class="ltx_p">If $h\geq 4k\text{,}$ set $q:=\lfloor h/(2k)\rfloor-1\geq 1\text{.}$ A center covers at most $q+1$ consecutive path vertices, so</p>
<table id="S7.Ex21" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N^{\uparrow}_{T}(q)\ \geq\ \frac{h+1}{q+1}\ =\ \frac{h+1}{\lfloor h/(2k)\rfloor}\ \geq\ 2k,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p25.2" class="ltx_p">whence $[\log(N^{\uparrow}_{T}(q)/k)]_{+}\geq\log 2$ and the term of the discrete formula (2.3) at $q$ is at least $(q+1)\log 2\text{.}$ Since $q+1=\lfloor h/(2k)\rfloor&gt;h/(2k)-1\geq h/(4k)\text{,}$</p>
<table id="S7.Ex22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\delta_{k}\ \geq\ \frac{(q+1)\log 2}{k}\ \geq\ \frac{h\log 2}{4k^{2}}\ \geq\ \frac{H_{T}\log 2}{8k^{2}}\,.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S7.p26" class="ltx_para">
<p id="S7.p26.1" class="ltx_p">If $h&lt;4k\text{,}$ the term of (2.3) at $q=0$ is $\min\{k,[\log(n/k)]_{+}\}\geq\min\{k,2\}\geq 1\text{,}$ since $n/k\geq C_{\star}=e^{2}\text{;}$ hence $\delta_{k}\geq 1/k&gt;H_{T}\log 2/(8k^{2})\text{,}$ using $H_{T}\leq 2h&lt;8k$ and $\log 2&lt;1\text{.}$
∎</p>
</div>
<div id="S7.p27" class="ltx_para">
<p id="S7.p27.1" class="ltx_p">The blocks are in place, and it remains to assemble them along the case analysis of Section 5.</p>
</div>
<div id="S7.p28" class="ltx_para">
<p id="S7.p28.1" class="ltx_p"><em class="ltx_title_proof">Completion of Theorem&nbsp;5, upper bound.</em></p>
</div>
<div id="S7.p29" class="ltx_para">
<p id="S7.p29.1" class="ltx_p">The skeleton, the meeting of the two branches at $k_{0}=\ell_{n}^{1/5}\text{,}$ and the resulting bound $C(1+\log(en))^{2/5}$ are in Section 5; deferred here are the fixed-point verification behind (5.11), the height branch (5.12), and the endpoint cases.</p>
</div>
<div id="S7.p30" class="ltx_para">
<p id="S7.p30.1" class="ltx_p"><em id="S7.p30.1.1" class="ltx_emph ltx_font_italic">The interior case: the width branch <span id="S7.p30.1.1.1" class="ltx_text ltx_font_upright">(5.11)</span>.</em> Let $2\leq k_{0}\leq K:=\lfloor n/C_{\star}\rfloor\text{,}$ so that the crossing clause fired at $k_{0}\text{:}$ $V^{2}\delta_{k_{0}}\leq A_{0}\sigma^{2}k_{0}\text{,}$ and $R^{*}_{T}\asymp\sigma^{2}k_{0}$ by the interior case of Section 3.3. Lemma 2.3 gives $\overline{\delta}_{k_{0}}\leq 2\delta_{k_{0}}\text{,}$ so</p>
<table id="S7.Ex23" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$V\sqrt{\overline{\delta}_{k_{0}}}\ \leq\ \sqrt{2A_{0}}\,\sigma\sqrt{k_{0}}\,,\qquad V\sqrt{k_{0}\overline{\delta}_{k_{0}}}\ \leq\ \sqrt{2A_{0}}\,\sigma\,k_{0}\,,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p30.2" class="ltx_p">and <a href="#S7.Thmlemma4" title="Lemma S.7.4 (Truth-localized width). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.4</span></a> at $k=k_{0}$ yields, for every $s&gt;0\text{,}$</p>
<table id="S7.Ex24" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$w_{\mu}(s)\ \leq\ Cs\sqrt{k_{0}}\ +\ C\sigma B,\qquad B\ :=\ k_{0}\log(2+\ell_{n})+\sqrt{k_{0}\,\ell_{n}}\,,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p30.3" class="ltx_p">with one universal constant $C\text{,}$ uniformly over $\mu\in\mathcal{F}_{V}(T)\text{:}$ the term $CV\sqrt{\overline{\delta}_{k_{0}}}\,\sqrt{k_{0}}\leq C^{\prime}\sigma k_{0}$ from the first group, and both terms of the second group after the two displayed substitutions, are absorbed into $C\sigma B\text{,}$ since $k_{0}\leq B/\log 2\text{.}$ Set $t^{2}:=C_{\mathrm{loc}}\sigma^{2}B$ with $C_{\mathrm{loc}}:=64C^{2}/\log 2+8C+1\text{.}$ Then $t\geq\sigma\text{,}$ since $B\geq k_{0}\log 2\geq 2\log 2&gt;1\text{;}$ and for every $s\geq t\text{,}$</p>
<table id="S7.Ex25" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sigma\,w_{\mu}(s)\ \leq\ C\sigma s\sqrt{k_{0}}+C\sigma^{2}B\ \leq\ \frac{s^{2}}{8}+\frac{s^{2}}{8}\ =\ \frac{s^{2}}{4}\,,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p30.4" class="ltx_p">the first term because $s\geq t\geq\sqrt{C_{\mathrm{loc}}k_{0}\log 2}\,\sigma\geq 8C\sigma\sqrt{k_{0}}\text{,}$ and the second because $C\sigma^{2}B=Ct^{2}/C_{\mathrm{loc}}\leq t^{2}/8\leq s^{2}/8\text{.}$ <a href="#S7.Thmlemma1" title="Lemma S.7.1 (Localized projection). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.1</span></a> applies at every $\mu$ and gives</p>
<table id="S7.Ex26" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{\mathrm{worst}}_{\mathrm{LSE}}(T,V,\sigma)\ \leq\ 33\,t^{2}\ =\ 33\,C_{\mathrm{loc}}\,\sigma^{2}\bigl[k_{0}\log(2+\ell_{n})+\sqrt{k_{0}\,\ell_{n}}\,\bigr];$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p30.5" class="ltx_p">dividing by $R^{*}_{T}\asymp\sigma^{2}k_{0}$ proves (5.11).</p>
</div>
<div id="S7.p31" class="ltx_para">
<p id="S7.p31.1" class="ltx_p"><em id="S7.p31.1.1" class="ltx_emph ltx_font_italic">The interior case: the height branch <span id="S7.p31.1.1.1" class="ltx_text ltx_font_upright">(5.12)</span>.</em> Still for $2\leq k_{0}\leq K\text{,}$ <a href="#S7.Thmlemma5" title="Lemma S.7.5 (Height floor). ‣ S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">S.7.5</span></a> applies at $k_{0}$ and combines with the crossing:</p>
<table id="S7.Ex27" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{\log 2}{8}\cdot\frac{V^{2}H_{T}}{k_{0}^{2}}\ \leq\ V^{2}\delta_{k_{0}}\ \leq\ A_{0}\sigma^{2}k_{0},\qquad\text{so}\qquad V^{2}H_{T}\ \leq\ \frac{8A_{0}}{\log 2}\,\sigma^{2}k_{0}^{3}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S7.p31.2" class="ltx_p">Both $\mu$ and its projection lie in the body, so $\|\widehat{\mu}_{\mathrm{LSE}}-\mu\|_{2}^{2}\leq\operatorname{diam}^{2}\mathcal{F}_{V}(T)=V^{2}H_{T}$ pathwise, and dividing by $R^{*}_{T}\asymp\sigma^{2}k_{0}$ proves (5.12).</p>
</div>
<div id="S7.p32" class="ltx_para">
<p id="S7.p32.1" class="ltx_p"><em id="S7.p32.1.1" class="ltx_emph ltx_font_italic">The endpoints.</em> The projection onto a convex set is a contraction, so $\|\widehat{\mu}_{\mathrm{LSE}}-\mu\|_{2}=\|\Pi_{\mathcal{F}_{V}(T)}(Y)-\Pi_{\mathcal{F}_{V}(T)}(\mu)\|_{2}\leq\|Y-\mu\|_{2}$ and $R^{\mathrm{worst}}_{\mathrm{LSE}}\leq\sigma^{2}n$ always; together with the diameter,</p>
<table id="S7.E12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{\mathrm{worst}}_{\mathrm{LSE}}(T,V,\sigma)\ \leq\ \min\bigl\{V^{2}H_{T},\ \sigma^{2}n\bigr\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(S.7.12)</span></td></tr></tbody>
</table>
<p id="S7.p32.2" class="ltx_p">If $k_{0}=K+1$ with $n\geq C_{\star}\text{,}$ the dimension case of Section 3.3 gives $R^{*}_{T}\asymp\sigma^{2}n\text{,}$ and <a href="#S7.E12" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.12</span></a> bounds the ratio by a constant. If $k_{0}=1\text{,}$ the two-point bound (3.8) gives $R^{*}_{T}\geq c\min\{V^{2}H_{T},\sigma^{2}\}$ for $n\geq 2\text{,}$ and there are two subcases. When $n&lt;C_{\star}\text{,}$ the right side of <a href="#S7.E12" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.12</span></a> is at most $C_{\star}\min\{V^{2}H_{T},\sigma^{2}\}\text{:}$ its second branch is $\sigma^{2}n\leq C_{\star}\sigma^{2}\text{,}$ and its first is unchanged. When the crossing clause fired at $k=1\text{,}$ the second case of Section 3.3 gives $V^{2}H_{T}\leq 2V^{2}h_{T}\leq(2A_{0}/\log 2)\,\sigma^{2}\text{,}$ so the right side of <a href="#S7.E12" title="In S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">S.7.12</span></a> is again at most $C\min\{V^{2}H_{T},\sigma^{2}\}\text{:}$ if $V^{2}H_{T}\leq\sigma^{2}$ it equals the first branch, and otherwise it is at most $C\sigma^{2}\text{.}$ In both subcases $R^{\mathrm{worst}}_{\mathrm{LSE}}\leq C\,R^{*}_{T}\text{.}$ The three cases are exhaustive: $k_{0}=K+1$ with $n&lt;C_{\star}$ means $K=0$ and $k_{0}=1\text{,}$ which the last case covers. Together with the two interior branches and the case analysis of Section 5, the upper bound of Theorem 5 is proved; with the lower bound established there, so is the theorem.
∎</p>
</div>
<div class="ltx_pagination ltx_role_newpage"></div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography" id="references">References</h2>

<ul id="bib.L1" class="ltx_biblist">
<li id="bib.bib8" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Abowd <span class="ltx_text ltx_bib_etal">et al.</span> (2022)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">J. M. Abowd, R. Ashmead, R. Cumings-Menon, <span class="ltx_text ltx_bib_etal">et al.</span></span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The 2020 Census disclosure avoidance system TopDown algorithm</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Harv. Data Sci. Rev.</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">Special Issue 2</span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.p2.1" title="1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span></li>
<li id="bib.bib31" class="ltx_bibitem ltx_bib_misc"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Aolaritei <span class="ltx_text ltx_bib_etal">et al.</span> (2025)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">L. Aolaritei, M. I. Jordan, R. Pathak, and A. Ulichney</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Revisiting mean estimation over $\ell_{p}$ balls: is the MLE optimal?</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2506.10354</span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p3.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib32" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Barron and Cover (1991)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. R. Barron and T. M. Cover</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Minimum complexity density estimation</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">IEEE Trans. Inf. Theory</span> <span class="ltx_text ltx_bib_volume">37</span> (<span class="ltx_text ltx_bib_number">4</span>), <span class="ltx_text ltx_bib_pages">pp. 1034–1054</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib20" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Bellec (2018)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. C. Bellec</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Sharp oracle inequalities for least squares estimators in shape restricted regression</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">46</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 745–780</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p1.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib10" class="ltx_bibitem ltx_bib_misc"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Benabbas <span class="ltx_text ltx_bib_etal">et al.</span> (2011)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Benabbas, H. C. Lee, J. Oren, and Y. Ye</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Efficient sum-based hierarchical smoothing under $\ell_{1}$-norm</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:1108.1751</span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p1.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib6" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Birgé and Massart (2001)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">L. Birgé and P. Massart</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Gaussian model selection</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">J. Eur. Math. Soc.</span> <span class="ltx_text ltx_bib_volume">3</span> (<span class="ltx_text ltx_bib_number">3</span>), <span class="ltx_text ltx_bib_pages">pp. 203–268</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p5.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.p1.1" title="1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S3a.p37.1" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.3</span></a>,
<a href="#S4.SS3.p5.1" title="4.3 Adaptation ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4.3</span></a>.
</span></li>
<li id="bib.bib40" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Borell (1975)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">C. Borell</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The Brunn-Minkowski inequality in Gauss space</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Invent. Math.</span> <span class="ltx_text ltx_bib_volume">30</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 207–216</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S7.p2.1" title="S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.7</span></a>.
</span></li>
<li id="bib.bib37" class="ltx_bibitem ltx_bib_book"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Boucheron <span class="ltx_text ltx_bib_etal">et al.</span> (2013)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Boucheron, G. Lugosi, and P. Massart</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Concentration inequalities: a nonasymptotic theory of independence</span>.
</span>
<span class="ltx_bibblock"> <span class="ltx_text ltx_bib_publisher">Oxford University Press</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S4.SS1.p6.1" title="4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4.1</span></a>.
</span></li>
<li id="bib.bib4" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Chatterjee <span class="ltx_text ltx_bib_etal">et al.</span> (2015)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Chatterjee, A. Guntuboyina, and B. Sen</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">On risk bounds in isotonic and other shape restricted regression problems</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">43</span> (<span class="ltx_text ltx_bib_number">4</span>), <span class="ltx_text ltx_bib_pages">pp. 1774–1800</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p1.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1.1" title="1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span></li>
<li id="bib.bib1" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Chatterjee and Lafferty (2018)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Chatterjee and J. Lafferty</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Denoising flows on trees</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">IEEE Trans. Inf. Theory</span> <span class="ltx_text ltx_bib_volume">64</span> (<span class="ltx_text ltx_bib_number">3</span>), <span class="ltx_text ltx_bib_pages">pp. 1767–1783</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p1.3" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS1.p5.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS1.p6.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS1.p7.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS2.p2.1" title="1.2 Technical Overview ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.2</span></a>,
<a href="#S1.SS2.p3.1" title="1.2 Technical Overview ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.2</span></a>,
<a href="#S1.SS3.p1.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p2.1" title="1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1a.p1.1" title="S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.1</span></a>,
<a href="#S1a.p26.1" title="S.1 The Profile Toolkit ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.1</span></a>,
<a href="#S2.SS1.p3.1" title="2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§2.1</span></a>.
</span></li>
<li id="bib.bib14" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Chatterjee (2014)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Chatterjee</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">A new perspective on least squares under convex constraint</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">42</span> (<span class="ltx_text ltx_bib_number">6</span>), <span class="ltx_text ltx_bib_pages">pp. 2340–2381</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p8.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS2.p7.1" title="1.2 Technical Overview ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.2</span></a>,
<a href="#S1.SS3.p3.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S5.p13.2" title="5 The Suboptimality of Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§5</span></a>,
<a href="#S7.p3.1" title="S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.7</span></a>.
</span></li>
<li id="bib.bib41" class="ltx_bibitem ltx_bib_incollection"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Cirel’son <span class="ltx_text ltx_bib_etal">et al.</span> (1976)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">B. S. Cirel’son, I. A. Ibragimov, and V. N. Sudakov</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Norms of Gaussian sample functions</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">Proceedings of the Third Japan-USSR Symposium on Probability Theory</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_series">Lecture Notes in Mathematics</span>, Vol. <span class="ltx_text ltx_bib_volume">550</span>, <span class="ltx_text ltx_bib_pages">pp. 20–41</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S7.p2.1" title="S.7 The Universal Upper Bound for Least Squares ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.7</span></a>.
</span></li>
<li id="bib.bib26" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Dalalyan and Tsybakov (2008)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. S. Dalalyan and A. B. Tsybakov</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Aggregation by exponential weighting, sharp PAC-Bayesian bounds and sparsity</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Mach. Learn.</span> <span class="ltx_text ltx_bib_volume">72</span>, <span class="ltx_text ltx_bib_pages">pp. 39–61</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib30" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Darwiche (2003)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Darwiche</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">A differential approach to inference in Bayesian networks</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">J. ACM</span> <span class="ltx_text ltx_bib_volume">50</span> (<span class="ltx_text ltx_bib_number">3</span>), <span class="ltx_text ltx_bib_pages">pp. 280–305</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib5" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Donoho and Johnstone (1994)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">D. L. Donoho and I. M. Johnstone</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Minimax risk over $\ell_{p}$-balls for $\ell_{q}$-error</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Probab. Theory Related Fields</span> <span class="ltx_text ltx_bib_volume">99</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 277–303</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p5.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.p1.1" title="1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span></li>
<li id="bib.bib28" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Giraud (2008)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">C. Giraud</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Mixing least-squares estimators when the variance is unknown</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Bernoulli</span> <span class="ltx_text ltx_bib_volume">14</span> (<span class="ltx_text ltx_bib_number">4</span>), <span class="ltx_text ltx_bib_pages">pp. 1089–1107</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib9" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Graham <span class="ltx_text ltx_bib_etal">et al.</span> (1982)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. L. Graham, P. B. Kessler, and M. K. McKusick</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Gprof: a call graph execution profiler</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">SIGPLAN Not.</span> <span class="ltx_text ltx_bib_volume">17</span> (<span class="ltx_text ltx_bib_number">6</span>), <span class="ltx_text ltx_bib_pages">pp. 120–126</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.p2.1" title="1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span></li>
<li id="bib.bib24" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Guntuboyina and Sen (2018)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Guntuboyina and B. Sen</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Nonparametric shape-restricted regression</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Statist. Sci.</span> <span class="ltx_text ltx_bib_volume">33</span> (<span class="ltx_text ltx_bib_number">4</span>), <span class="ltx_text ltx_bib_pages">pp. 568–594</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p1.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib17" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Han <span class="ltx_text ltx_bib_etal">et al.</span> (2019)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">Q. Han, T. Wang, S. Chatterjee, and R. J. Samworth</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Isotonic regression in general dimensions</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">47</span> (<span class="ltx_text ltx_bib_number">5</span>), <span class="ltx_text ltx_bib_pages">pp. 2440–2471</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p1.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib7" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Hay <span class="ltx_text ltx_bib_etal">et al.</span> (2010)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Hay, V. Rastogi, G. Miklau, and D. Suciu</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Boosting the accuracy of differentially private histograms through consistency</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Proc. VLDB Endow.</span> <span class="ltx_text ltx_bib_volume">3</span> (<span class="ltx_text ltx_bib_number">1</span>), <span class="ltx_text ltx_bib_pages">pp. 1021–1032</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.p2.1" title="1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span></li>
<li id="bib.bib15" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Kur <span class="ltx_text ltx_bib_etal">et al.</span> (2024)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">G. Kur, F. Gao, A. Guntuboyina, and B. Sen</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Convex regression in multidimensions: suboptimality of least squares estimators</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">52</span> (<span class="ltx_text ltx_bib_number">6</span>), <span class="ltx_text ltx_bib_pages">pp. 2791–2815</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p8.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS3.p3.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib18" class="ltx_bibitem ltx_bib_inproceedings"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Kyng <span class="ltx_text ltx_bib_etal">et al.</span> (2015)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">R. Kyng, A. Rao, and S. Sachdeva</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Fast, provable algorithms for isotonic regression in all $\ell_{p}$-norms</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">Adv. Neural Inf. Process. Syst. 28</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages">pp. 2719–2727</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib25" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Leung and Barron (2006)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">G. Leung and A. R. Barron</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Information theory and mixing least-squares regressions</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">IEEE Trans. Inf. Theory</span> <span class="ltx_text ltx_bib_volume">52</span> (<span class="ltx_text ltx_bib_number">8</span>), <span class="ltx_text ltx_bib_pages">pp. 3396–3410</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S4.SS1.p4.1" title="4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4.1</span></a>.
</span></li>
<li id="bib.bib21" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Lifshits and Linde (2011a)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Lifshits and W. Linde</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Compactness properties of weighted summation operators on trees</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Studia Math.</span> <span class="ltx_text ltx_bib_volume">202</span> (<span class="ltx_text ltx_bib_number">1</span>), <span class="ltx_text ltx_bib_pages">pp. 17–47</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p2.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib22" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Lifshits and Linde (2011b)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Lifshits and W. Linde</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Compactness properties of weighted summation operators on trees—the critical case</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Studia Math.</span> <span class="ltx_text ltx_bib_volume">206</span> (<span class="ltx_text ltx_bib_number">1</span>), <span class="ltx_text ltx_bib_pages">pp. 75–96</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p2.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib23" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Luss and Rosset (2017)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">R. Luss and S. Rosset</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Bounded isotonic regression</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Electron. J. Stat.</span> <span class="ltx_text ltx_bib_volume">11</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 4488–4514</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p1.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib38" class="ltx_bibitem ltx_bib_book"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Massart (2007)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. Massart</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Concentration inequalities and model selection</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_series">Lecture Notes in Mathematics</span>, Vol. <span class="ltx_text ltx_bib_volume">1896</span>,  <span class="ltx_text ltx_bib_publisher">Springer</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S3a.p37.1" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.3</span></a>.
</span></li>
<li id="bib.bib12" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Neykov (2023)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Neykov</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">On the minimax rate of the Gaussian sequence model under bounded convex constraints</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">IEEE Trans. Inf. Theory</span> <span class="ltx_text ltx_bib_volume">69</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 1244–1260</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p4.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS3.p2.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p3.1" title="1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span></li>
<li id="bib.bib34" class="ltx_bibitem ltx_bib_misc"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Neykov (2026)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Neykov</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Fast near-optimal estimation over symmetric norm balls</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2606.01554</span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib13" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Prasadan and Neykov (2025)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Prasadan and M. Neykov</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Some facts about the optimality of the LSE in the Gaussian sequence model with convex constraint</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">IEEE Trans. Inf. Theory</span> <span class="ltx_text ltx_bib_volume">71</span> (<span class="ltx_text ltx_bib_number">11</span>), <span class="ltx_text ltx_bib_pages">pp. 8928–8958</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p3.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib27" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Rigollet and Tsybakov (2011)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. Rigollet and A. B. Tsybakov</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Exponential screening and optimal rates of sparse estimation</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">39</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 731–771</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib33" class="ltx_bibitem ltx_bib_book"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Robertson <span class="ltx_text ltx_bib_etal">et al.</span> (1988)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">T. Robertson, F. T. Wright, and R. L. Dykstra</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Order restricted statistical inference</span>.
</span>
<span class="ltx_bibblock"> <span class="ltx_text ltx_bib_publisher">Wiley</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib35" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Stein (1981)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">C. M. Stein</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Estimation of the mean of a multivariate normal distribution</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">9</span> (<span class="ltx_text ltx_bib_number">6</span>), <span class="ltx_text ltx_bib_pages">pp. 1135–1151</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S4.SS1.p6.1" title="4.1 Aggregation over Integer States ‣ 4 Efficient and Adaptive Estimation ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4.1</span></a>,
<a href="#S5a.p8.1" title="S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.5</span></a>.
</span></li>
<li id="bib.bib36" class="ltx_bibitem ltx_bib_book"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Tsybakov (2009)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. B. Tsybakov</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Introduction to nonparametric estimation</span>.
</span>
<span class="ltx_bibblock"> <span class="ltx_text ltx_bib_publisher">Springer</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S3.SS2.p6.1" title="3.2 The Packing Lower Bound ‣ 3 The Rate Formula ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§3.2</span></a>,
<a href="#S3a.p5.1" title="S.3 The Packing Lower Bound ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.3</span></a>.
</span></li>
<li id="bib.bib16" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Vaškevičius and Zhivotovskiy (2023)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">T. Vaškevičius and N. Zhivotovskiy</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Suboptimality of constrained least squares and improvements via non-linear predictors</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Bernoulli</span> <span class="ltx_text ltx_bib_volume">29</span> (<span class="ltx_text ltx_bib_number">1</span>), <span class="ltx_text ltx_bib_pages">pp. 473–495</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p3.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib39" class="ltx_bibitem ltx_bib_book"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">von zur Gathen and Gerhard (2013)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">J. von zur Gathen and J. Gerhard</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Modern computer algebra</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_edition">3rd edition</span>,  <span class="ltx_text ltx_bib_publisher">Cambridge Univ. Press</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S2.SS1.p1.1" title="2.1 The Flow Polytope ‣ 2 The Flow Polytope and the Ancestor Profile ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§2.1</span></a>,
<a href="#S5a.p33.1" title="S.5 Exact Evaluation of the Aggregate ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§S.5</span></a>.
</span></li>
<li id="bib.bib19" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Wei <span class="ltx_text ltx_bib_etal">et al.</span> (2019)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">Y. Wei, M. J. Wainwright, and A. Guntuboyina</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The geometry of hypothesis testing over convex cones: generalized likelihood ratio tests and minimax radii</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">47</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 994–1024</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p2.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib29" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Willems <span class="ltx_text ltx_bib_etal">et al.</span> (1995)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">F. M. J. Willems, Y. M. Shtarkov, and T. J. Tjalkens</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The context-tree weighting method: basic properties</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">IEEE Trans. Inf. Theory</span> <span class="ltx_text ltx_bib_volume">41</span> (<span class="ltx_text ltx_bib_number">3</span>), <span class="ltx_text ltx_bib_pages">pp. 653–664</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p4.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib11" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Yang and Barron (1999)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">Y. Yang and A. Barron</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Information-theoretic determination of minimax rates of convergence</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">27</span> (<span class="ltx_text ltx_bib_number">5</span>), <span class="ltx_text ltx_bib_pages">pp. 1564–1599</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p4.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS3.p2.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
<li id="bib.bib2" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Zhang (2002)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">C. Zhang</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Risk bounds in isotonic regression</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">30</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 528–555</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p5.1" title="1.1 Our Results ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS3.p1.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1.1" title="1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span></li>
<li id="bib.bib3" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_author-year ltx_role_refnum ltx_tag_bibitem">Zhang (2013)</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">L. Zhang</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Nearly optimal minimax estimator for high-dimensional sparse linear regression</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Statist.</span> <span class="ltx_text ltx_bib_volume">41</span> (<span class="ltx_text ltx_bib_number">4</span>), <span class="ltx_text ltx_bib_pages">pp. 2149–2175</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p3.1" title="1.3 Related Work ‣ 1 Introduction ‣ The Minimax Rate of Denoising Flows on Trees" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span></li>
</ul>
</section>
</article>
