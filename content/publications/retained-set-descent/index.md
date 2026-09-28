---
title: "Retained-Set Descent for Diagonal Ramsey Numbers"

authors:
  - Zhipeng Lu
  - me

# arXiv v1 submission date.
date: 2026-09-13

publication_types: ["manuscript"]
publication: "*Preprint*, arXiv:2609.14525"
publication_short: "Preprint"

abstract: |
  We study how far a fixed Ramsey upper bound can be improved by descending through
  blue neighborhoods in one vertex set while keeping a second set fixed. A weighted
  inequality in the two set sizes determines when the descent can stop. For the source
  bound specified here, the infimum diagonal exponent over all finite derivations lies
  in $[1.305,\,1.307]$. A finite derivation gives $R(k,k)\le3.69507^k$ for all
  sufficiently large $k$; a concave polygon proves the lower bound for every finite
  depth. We also characterize the infimum as a greatest fixed point and show that
  every larger exponent has a finite derivation valid uniformly for nearby clique-size
  ratios.

tags:
  - Ramsey Theory
  - Extremal Combinatorics
  - Graph Theory

featured: false

links:
  - type: pdf
    url: paper.pdf
    label: Paper
  - type: code
    url: https://github.com/sichen-wang/diagonal-ramsey-numbers
  - type: preprint
    provider: arxiv
    id: 2609.14525
    label: arXiv
---

<article class="ltx_document ltx_authors_1line">




<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="introduction"><span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p id="S1.p1.1" class="ltx_p">Let $R(k,\ell)$ be the least integer $N$ such that every red–blue coloring of $K_{N}$ contains a red $K_{k}$ or a blue $K_{\ell}\text{.}$
Ramsey’s theorem <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx6" title="" class="ltx_ref">Ram</a>]</cite> guarantees that these numbers are finite.
The Erdős–Szekeres recurrence <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx4" title="" class="ltx_ref">ES</a>]</cite> gives $R(k,\ell)\leq\binom{k+\ell-2}{k-1}\text{,}$ and hence $R(k,k)\leq 4^{k}\text{.}$
In the other direction, Erdős’s random-coloring argument <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx3" title="" class="ltx_ref">Er</a>]</cite> gives a lower bound of order $k2^{k/2}\text{;}$ Spencer <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx8" title="" class="ltx_ref">Spe</a>]</cite> improved its leading constant using the Lovász local lemma.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p id="S1.p2.1" class="ltx_p">Thomason <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">Tho</a>]</cite> improved the classical upper bound by a polynomial factor using quasirandomness: a coloring close to the inductive bound must have degrees and small-subgraph counts close to those of a random coloring.
Conlon <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx2" title="" class="ltx_ref">Con</a>]</cite> developed this approach to obtain $R(k,k)\leq 4^{k}\exp(-c(\log k)^{2}/\log\log k)\text{.}$
Sah <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx7" title="" class="ltx_ref">Sah</a>]</cite> strengthened the estimate to $R(k,k)\leq 4^{k}\exp(-c(\log k)^{2})\text{.}$
Each bound holds for a suitable absolute constant $c&gt;0$ and all sufficiently large $k\text{.}$
These results gave successively larger subexponential improvements while retaining exponential base $4\text{.}$</p>
</div>
<div id="S1.p3" class="ltx_para">
<p id="S1.p3.1" class="ltx_p">Campos, Griffiths, Morris, and Sahasrabudhe <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx1" title="" class="ltx_ref">CGMS</a>]</cite> obtained the first improvement in the exponential base, proving $R(k,k)\leq(4-\varepsilon)^{k}$ for an absolute $\varepsilon&gt;0$ and all sufficiently large $k\text{.}$
Their book algorithm works with two vertex sets and controls the red density between them.
Gupta, Ndiaye, Norin, and Wei <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx5" title="" class="ltx_ref">GNNW</a>]</cite> replaced this algorithm by a candidate induction, obtained stronger off-diagonal estimates, and optimized the resulting parameters to give $R(k,k)\leq 3.8^{k+o(k)}\text{.}$
Their candidate induction and reuse of improved Ramsey bounds in this optimization are the starting points of our work.</p>
</div>
<div id="S1.p4" class="ltx_para">
<p id="S1.p4.1" class="ltx_p">We improve the diagonal bound to $3.69507^{k}$ for all sufficiently large $k\text{.}$
Our descent applies density bounds inside a vertex set $X$ while keeping a second set $Y$ fixed for a final inequality in $|X|^{w}|Y|\text{,}$ with $w&gt;0\text{.}$
Each resulting bound can be used inside $X$ in a later descent.
We also ask how small an exponent finitely many such repetitions can give from a fixed initial bound.</p>
</div>
<div id="S1.p5" class="ltx_para">
<p id="S1.p5.1" class="ltx_p">We call this initial bound the <em id="S1.p5.1.1" class="ltx_emph ltx_font_italic">source</em>.
It has the form $\log R(a,b)\leq af(b/a)+o(a)$ for integers $1\leq b\leq a\text{,}$ where $f$ is a fixed concave function on $[0,1]$ and the error is uniform in $b\text{.}$
<a href="#S2" title="2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a> specifies $f\text{,}$ and <a href="#A2" title="Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">B</span></a> proves the bound.</p>
</div>
<div id="S1.p6" class="ltx_para">
<p id="S1.p6.1" class="ltx_p">A <em id="S1.p6.1.1" class="ltx_emph ltx_font_italic">conditional bound</em> at density $p\in(0,1)$ and ratio $s\in(0,1]$ applies to colorings with at least a fraction $p$ of their edges red.
An exponent $z$ means that, for some fixed $C\geq 1$ and all sufficiently large $k\text{,}$ order at least $C\mathrm{e}^{zk}$ guarantees a red $K_{k}$ or a blue $K_{\lfloor sk\rfloor}\text{.}$
We use families of such bounds on closed intervals of $s\text{,}$ with continuous exponents and common constants and thresholds.</p>
</div>
<div id="S1.p7" class="ltx_para">
<p id="S1.p7.1" class="ltx_p">Starting from the conditional bounds supplied by the source, we apply the descent rule using bounds proved at earlier steps.
We may also restrict ratio intervals, increase a density threshold or an exponent, and combine bounds at the same density on a finite closed cover of a ratio interval.
A <em id="S1.p7.1.1" class="ltx_emph ltx_font_italic">finite proof</em> uses only finitely many of these operations; <a href="#S4.Thmlemma1" title="Definition 4.1 (Finite Proof). ‣ 4 The Optimum over Finite Proofs ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Definition</span> <span class="ltx_text ltx_ref_tag">4.1</span></a> gives the precise rules.</p>
</div>
<div id="S1.p8" class="ltx_para">
<p id="S1.p8.1" class="ltx_p">Let $U_{\rm fin}(p,s)$ be the infimum of the exponents obtained at density $p$ and ratio $s$ by such finite proofs.
In the diagonal case $(p,s)=(1/2,1)\text{,}$ we construct a finite proof with rational exponent $z_{+}$ and a rational lower bound $z_{-}$ for all finite proofs.
Their exact values are given in <a href="#S6" title="6 The Diagonal Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6</span></a>.</p>
</div>
<div id="Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem1.2" class="ltx_text ltx_font_bold">Theorem 1</span></span><span id="Thmtheorem1.3" class="ltx_text ltx_font_bold">.</span></h6>
<div id="Thmtheorem1.p1" class="ltx_para">
<p id="Thmtheorem1.p1.1" class="ltx_p"><span id="Thmtheorem1.p1.1.1" class="ltx_text ltx_font_italic">For this source and these finite proof rules,</span></p>
<table id="S1.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$1.305&lt;z_{-}\leq U_{\rm fin}(1/2,1)\leq z_{+}&lt;1.307.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1)</span></td></tr></tbody>
</table>
<p id="Thmtheorem1.p1.2" class="ltx_p"><span id="Thmtheorem1.p1.2.1" class="ltx_text ltx_font_italic">The exponent $z_{+}$ has a finite proof.
For all sufficiently large integers $k\text{,}$</span></p>
<table id="S1.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R(k,k)\leq\left\lceil 150003\exp(z_{+}k)\right\rceil,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(2)</span></td></tr></tbody>
</table>
<p id="Thmtheorem1.p1.3" class="ltx_p"><span id="Thmtheorem1.p1.3.1" class="ltx_text ltx_font_italic">and hence $R(k,k)\leq 3.69507^{k}\text{.}$</span></p>
</div>
</div>
<div id="S1.p9" class="ltx_para">
<p id="S1.p9.1" class="ltx_p">For the Ramsey bound, choose the denser color as red and apply the conditional bound at $(p,s)=(1/2,1)\text{.}$</p>
</div>
<section id="S1.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="proof-outline"><span class="ltx_tag ltx_tag_subsection">1.1 </span>Proof Outline</h3>

<div id="S1.SS1.p1" class="ltx_para">
<p id="S1.SS1.p1.1" class="ltx_p">We use disjoint sets $X,Y\text{,}$ keeping $Y$ fixed and requiring each vertex of $X$ to have at least a fixed positive fraction of $Y$ as red neighbors.
The red target $k$ and the blue target $\ell$ in $Y$ stay fixed while the blue target $t$ in $X$ decreases.
When $X$ is large enough for a conditional bound at density $q\text{,}$ we either finish at red density at least $q$ or descend to a blue neighborhood of size greater than $(1-q)(|X|-1)\text{.}$
Restricting $X$ to this neighborhood preserves its red degrees into $Y$ and reduces $t$ by one: a blue $K_{t-1}$ there extends through the chosen vertex.</p>
</div>
<div id="S1.SS1.p2" class="ltx_para">
<p id="S1.SS1.p2.1" class="ltx_p">Write the required size of $X$ at $s=t/k$ as $\exp(kg(s))\text{,}$ with $g$ piecewise affine.
On a cell of slope $d\text{,}$ the threshold falls by a factor $\mathrm{e}^{-d}$ per step, so we take $d&gt;-\log(1-q)$ to allow for the neighborhood loss.
The profile $g$ must also exceed the exponents of the bounds used inside $X\text{.}$
With slopes and calls fixed, optimizing its vertical shift under these conditions and the initial and terminal inequalities gives the cost in <a href="#S3.E12" title="In 3.1 The Cost of a Descent ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">12</span></a>.</p>
</div>
<div id="S1.SS1.p3" class="ltx_para">
<p id="S1.SS1.p3.1" class="ltx_p">Reusing these bounds and iterating from the source gives a decreasing sequence of exponents whose limit is a greatest fixed point (<a href="#Thmtheorem3" title="Theorem 3 (Finite Proofs and Preserved Lower Bounds). ‣ 4 The Optimum over Finite Proofs ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3</span></a>).
Strict inequalities persist on neighborhoods of ratios; compactness selects finitely many neighborhoods and hence a common finite depth for a whole descent.
Hence every exponent strictly above the limit has a finite proof, uniformly near its target ratio.</p>
</div>
<div id="S1.SS1.p4" class="ltx_para">
<p id="S1.SS1.p4.1" class="ltx_p">For the lower bound, a concave polygon $F$ assigns exponent $F(s)$ at densities up to $1-\mathrm{e}^{-d}$ on a segment of slope $d\text{.}$
Where a descent using bounds that respect this estimate has $g&lt;F\text{,}$ its call density must exceed $1-\mathrm{e}^{-d}\text{,}$ forcing the slope of $g$ above $d\text{.}$
Thus $g-F$ decreases as the descent moves to smaller ratios.
We choose $F$ so that the terminal weighted inequality cannot hold below it.
The supporting-line formula reduces this requirement to one-variable inequalities at its vertices (<a href="#Thmtheorem4" title="Theorem 4 (Finite Polygon Criterion). ‣ 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4</span></a>); the certificates in <a href="#S6" title="6 The Diagonal Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6</span></a> complete the proof of <a href="#Thmtheorem1" title="Theorem 1. ‣ 1 Introduction ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a>.</p>
</div>
<div id="S1.SS1.p5" class="ltx_para">
<p id="S1.SS1.p5.1" class="ltx_p">The Lean 4 formalization and the Python code for exact certificate checks are available in the accompanying repository.<span id="footnote1" class="ltx_note ltx_role_footnote"><sup class="ltx_note_mark">1</sup><span class="ltx_note_outer"><span class="ltx_note_content"><sup class="ltx_note_mark">1</sup>
              <span class="ltx_tag ltx_tag_note">1</span>
              
              
              
              
              
              
              
            <a href="https://github.com/sichen-wang/diagonal-ramsey-numbers" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://github.com/sichen-wang/diagonal-ramsey-numbers</a></span></span></span></p>
</div>
</section>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="source-bounds"><span class="ltx_tag ltx_tag_section">2 </span>Source Bounds</h2>

<div id="S2.p1" class="ltx_para">
<p id="S2.p1.1" class="ltx_p">We now describe the source function and express its bound through pairs $(x,y)\text{.}$
These pairs supply the weighted inequality and the initial conditional bounds used in the descent.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p id="S2.p2.1" class="ltx_p">All logarithms are natural. Let</p>
<table id="S2.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$h(s)=(1+s)\log(1+s)-s\log s,\qquad h(0)=0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.p2.2" class="ltx_p">The classical Ramsey bound gives $\log R(k,\ell)\leq kh(\ell/k)$ for $1\leq\ell\leq k$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx4" title="" class="ltx_ref">ES</a>]</cite>.</p>
</div>
<div id="S2.p3" class="ltx_para">
<p id="S2.p3.1" class="ltx_p">Our fixed source is</p>
<table id="S2.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$f(s)=h(s)+s\mathrm{e}^{-s}P(s)\qquad(0\leq s\leq 1),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3)</span></td></tr></tbody>
</table>
<p id="S2.p3.2" class="ltx_p">where the piecewise cubic $P$ is specified by the rational partition points, values, and derivatives in <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">data/source.json</span>.
This source satisfies</p>
<table id="S2.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log R(a,b)\leq af(b/a)+o(a)\qquad(1\leq b\leq a),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4)</span></td></tr></tbody>
</table>
<p id="S2.p3.3" class="ltx_p">with an error uniform in $b\text{.}$
<a href="#A2" title="Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">B</span></a> proves this bound and the properties of $f$ used below.</p>
</div>
<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="source-pairs-and-supporting-lines"><span class="ltx_tag ltx_tag_subsection">2.1 </span>Source Pairs and Supporting Lines</h3>

<div id="S2.SS1.p1" class="ltx_para">
<p id="S2.SS1.p1.1" class="ltx_p">The weighted inequality uses bounds of the form $R(a,b)\leq x^{-a}y^{-b}\text{.}$
We say that $(x,y)\in(0,1)^{2}$ is an <em id="S2.SS1.p1.1.1" class="ltx_emph ltx_font_italic">admissible Ramsey pair</em> if this bound holds for all sufficiently large $a+b\text{.}$
Color symmetry in <a href="#S2.E4" title="In 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4</span></a> leads to the extension</p>
<table id="S2.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{f}(t)=\begin{cases}f(t),&amp;0\leq t\leq 1,\\ tf(1/t),&amp;t\geq 1.\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.SS1.p1.2" class="ltx_p">The source exponent for arbitrary positive targets $a,b$ is then $b\widehat{f}(a/b)\text{.}$
We call $(x,y)\in(0,1)^{2}$ a <em id="S2.SS1.p1.2.1" class="ltx_emph ltx_font_italic">source pair</em> if
$b\widehat{f}(a/b)\leq-a\log x-b\log y$ for all $a,b&gt;0\text{,}$ and write $\mathcal{B}_{f}$ for their set.
Every interior point of $\mathcal{B}_{f}$ is admissible: choose a slightly larger pair still in $\mathcal{B}_{f}$ and apply <a href="#S2.E4" title="In 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4</span></a> with color symmetry.
The resulting error is $o(a+b)\text{,}$ which the strict coordinate gaps absorb.</p>
</div>
<div id="S2.SS1.p2" class="ltx_para">
<p id="S2.SS1.p2.1" class="ltx_p">Supporting lines give a convenient description of these pairs.
The source verification shows that $f$ is continuous on $[0,1]$ and is $C^{1}$ on $(0,1]\text{,}$ where it is strictly concave and increasing.
It also gives $f(0)=0$ and $2f^{\prime}(1)&gt;f(1)\text{.}$
It follows that $\widehat{f}$ is increasing and concave.
On each smooth piece with $t&gt;1\text{,}$ $\widehat{f}^{\prime\prime}(t)=t^{-3}f^{\prime\prime}(1/t)&lt;0\text{;}$ its first derivative is continuous at the reflected source partition points. At $t=1\text{,}$ the derivative drops from $f^{\prime}(1)$ to $f(1)-f^{\prime}(1)\text{.}$
Strict concavity and $f(0)=0$ give $f(s)-sf^{\prime}(s)&gt;0\text{,}$ so the reflected branch is increasing.
The expression in <a href="#S2.E3" title="In 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3</span></a> gives $\widehat{f}^{\prime}(0+)=\infty\text{,}$ $\widehat{f}^{\prime}(\infty)=0\text{,}$ and $\widehat{f}(t)/t\to 0$ as $t\to\infty\text{.}$</p>
</div>
<div id="S2.SS1.p3" class="ltx_para">
<p id="S2.SS1.p3.1" class="ltx_p">For $A&gt;0\text{,}$ define the intercept of the supporting line with slope $A$ by</p>
<table id="S2.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$b(A)=\sup_{t\geq 0}\{\widehat{f}(t)-At\},\qquad\widehat{f}(t)=\inf_{A&gt;0}\{At+b(A)\}\quad(t&gt;0).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5)</span></td></tr></tbody>
</table>
<p id="S2.SS1.p3.2" class="ltx_p">For fixed $A&gt;0\text{,}$ $\widehat{f}(t)-At\to-\infty$ as $t\to\infty\text{,}$ while $f(t)/t\to\infty$ as $t\downarrow 0$ makes this expression positive for small positive $t\text{.}$
By continuity, the supremum is positive and attained at some $t&gt;0\text{.}$
At each $t&gt;0\text{,}$ concavity supplies a supporting slope $A&gt;0\text{:}$ use the derivative, or any slope between the one-sided derivatives at $t=1\text{.}$
For this slope $b(A)=\widehat{f}(t)-At\text{,}$ proving the second identity.</p>
</div>
<div id="S2.SS1.p4" class="ltx_para">
<p id="S2.SS1.p4.1" class="ltx_p">Writing $x=\mathrm{e}^{-A}$ and $y=\mathrm{e}^{-B}\text{,}$ the source-pair condition becomes $B\geq b(A)\text{,}$ so</p>
<table id="S2.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{B}_{f}=\{(\mathrm{e}^{-A},\mathrm{e}^{-B}):A&gt;0,\ B\geq b(A)\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.SS1.p4.2" class="ltx_p">The finite convex function $b$ is continuous on $A&gt;0\text{,}$ so interior source pairs correspond to $B&gt;b(A)\text{.}$
Taking $(a,b)=(1,s)$ in the support inequality gives</p>
<table id="S2.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$A+sb(A)\geq f(s)\qquad(0&lt;s\leq 1).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(6)</span></td></tr></tbody>
</table>
</div>
</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-weighted-candidate-bound"><span class="ltx_tag ltx_tag_subsection">2.2 </span>The Weighted Candidate Bound</h3>

<div id="S2.SS2.p1" class="ltx_para">
<p id="S2.SS2.p1.1" class="ltx_p">Write $N_{\chi}(v)$ for the neighborhood of $v$ in color $\chi\in\{R,B\}$ and $\deg_{\chi}(v,Z)=|N_{\chi}(v)\cap Z|\text{.}$
For disjoint nonempty vertex sets $X,Y\text{,}$ let $e_{R}(X,Y)$ be the number of red edges between them and write $d_{R}(X,Y)=e_{R}(X,Y)/(|X||Y|)\text{.}$
Following <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx5" title="" class="ltx_ref">GNNW</a>]</cite>, a <em id="S2.SS2.p1.1.1" class="ltx_emph ltx_font_italic">candidate</em> is an ordered pair $(X,Y)$ of such sets.
We say that a candidate is <em id="S2.SS2.p1.1.2" class="ltx_emph ltx_font_italic">$(k,\ell,t)$-good</em> if $X\cup Y$ contains a red $K_{k}\text{,}$ or $X$ contains a blue $K_{t}\text{,}$ or $Y$ contains a blue $K_{\ell}\text{.}$
The target in the retained set $Y$ is $\ell\text{,}$ while the target $t$ in $X$ may decrease.</p>
</div>
<div id="S2.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma 2.1</span></span><span id="S2.Thmlemma1.3" class="ltx_text ltx_font_bold"> </span>(Weighted Candidate Bound)<span id="S2.Thmlemma1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmlemma1.p1" class="ltx_para">
<p id="S2.Thmlemma1.p1.1" class="ltx_p"><span id="S2.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">Fix $w&gt;0$ and $\mu,p,x,y\in(0,1)$ with $(x,y)\in\operatorname{int}\mathcal{B}_{f}$ and</span></p>
<table id="S2.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$x&lt;(1-\mu)^{w}p^{1/(1-\mu)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.Thmlemma1.p1.2" class="ltx_p"><span id="S2.Thmlemma1.p1.2.1" class="ltx_text ltx_font_italic">For all sufficiently large $\ell\text{,}$ uniformly in positive integers $k,t\text{,}$</span></p>
<table id="S2.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{R}(X,Y)\geq p,\qquad|X|^{w}|Y|\geq x^{-k}y^{-\ell}\mu^{-wt}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.Thmlemma1.p1.3" class="ltx_p"><span id="S2.Thmlemma1.p1.3.1" class="ltx_text ltx_font_italic">imply that $(X,Y)$ is $(k,\ell,t)$-good.</span></p>
</div>
</div>
<div id="S2.SS2.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS2.p2" class="ltx_para">
<p id="S2.SS2.p2.1" class="ltx_p"><span id="S2.SS2.p2.1.1" class="ltx_text">Choose a slightly larger pair $(\widehat{x},\widehat{y})$ still in $\operatorname{int}\mathcal{B}_{f}\text{.}$
Once $\ell$ is large, admissibility guarantees a red $K_{a}$ or a blue $K_{\ell}$ in every vertex set of size at least $\widehat{x}^{-a}\widehat{y}^{-\ell}\text{,}$ uniformly for $a\geq 1\text{.}$
Applying <a href="#A1.Thmlemma1" title="Lemma A.1 (Finite-Host Weighted Candidate Bound). ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">A.1</span></a> with $C=1$ proves the claim.
∎</span></p>
</div>
</div>
</section>
<section id="S2.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="conditional-bounds"><span class="ltx_tag ltx_tag_subsection">2.3 </span>Conditional Bounds</h3>

<div id="S2.SS3.p1" class="ltx_para">
<p id="S2.SS3.p1.1" class="ltx_p">To reuse a bound during a descent, we need it for an interval of blue-to-red target ratios, with a single size constant and a single threshold for $k\text{.}$</p>
</div>
<div id="S2.Thmlemma2" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma2.2" class="ltx_text ltx_font_bold">Definition 2.2</span></span><span id="S2.Thmlemma2.3" class="ltx_text ltx_font_bold"> </span>(Conditional Bound)<span id="S2.Thmlemma2.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmlemma2.p1" class="ltx_para">
<p id="S2.Thmlemma2.p1.1" class="ltx_p">For $p\in(0,1)\text{,}$ a compact interval $I\subset(0,1]\text{,}$ and a continuous function $L:I\to(0,\infty)\text{,}$ we say that the <em id="S2.Thmlemma2.p1.1.1" class="ltx_emph ltx_font_italic">conditional bound</em> $\mathsf{D}(p,L,I)$ holds if some $C\geq 1,K$ have the following property uniformly for $r\in I$ and integers $k\geq K\text{:}$
a coloring of red density at least $p$ and order at least $C\mathrm{e}^{kL(r)}$ contains a red $K_{k}$ or a blue $K_{\lfloor rk\rfloor}\text{.}$
We choose $K$ so that all blue targets are positive.
For a constant exponent $z\text{,}$ the notation $\mathsf{D}(p,z,I)$ means $L\equiv z\text{.}$</p>
</div>
</div>
<div id="S2.SS3.p2" class="ltx_para">
<p id="S2.SS3.p2.1" class="ltx_p">We call $(w,\mu,x,y)$ a <em id="S2.SS3.p2.1.1" class="ltx_emph ltx_font_italic">strict control at density $p$</em> when it satisfies the parameter conditions of <a href="#S2.Thmlemma1" title="Lemma 2.1 (Weighted Candidate Bound). ‣ 2.2 The Weighted Candidate Bound ‣ 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>.
Write $A=-\log x\text{,}$ $B=-\log y\text{,}$ and $\beta=-\log\mu\text{.}$
Apply the weighted candidate bound with $t=\ell$ to a balanced partition whose red cross-density is at least $p\text{;}$ such a partition exists by averaging.
Both set sizes are a constant fraction of the graph’s order, so the corresponding exponent is</p>
<table id="S2.E7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$L(r)=\frac{A+rB+wr\beta}{1+w}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(7)</span></td></tr></tbody>
</table>
<p id="S2.SS3.p2.2" class="ltx_p">Choose $y_{1}&gt;y$ with $(x,y_{1})\in\operatorname{int}\mathcal{B}_{f}\text{.}$
For $\ell=\lfloor rk\rfloor$ and a host of order $N\geq\mathrm{e}^{kL(r)}\text{,}$ the partition satisfies</p>
<table id="S2.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$|X|^{w}|Y|\geq\frac{x^{-k}y^{-\ell}\mu^{-w\ell}}{3^{w+1}}\geq x^{-k}y_{1}^{-\ell}\mu^{-w\ell}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.SS3.p2.3" class="ltx_p">The first inequality uses $kr\geq\ell$ and $B+w\beta&gt;0\text{;}$ the second holds once $(y_{1}/y)^{\ell}\geq 3^{w+1}\text{.}$
Applying <a href="#S2.Thmlemma1" title="Lemma 2.1 (Weighted Candidate Bound). ‣ 2.2 The Weighted Candidate Bound ‣ 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a> at $(x,y_{1})$ proves $\mathsf{D}(p,L,I)$ with $C=1$ on every compact $I\subset(0,1]\text{.}$
The threshold is uniform in $r\in I\text{,}$ since $\ell\geq k\min I-1\text{.}$
These <em id="S2.SS3.p2.3.1" class="ltx_emph ltx_font_italic">weighted source bounds</em> are the starting points of our finite derivations, and we call them <em id="S2.SS3.p2.3.2" class="ltx_emph ltx_font_italic">source leaves</em>.</p>
</div>
</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="retained-set-descent-and-its-cost"><span class="ltx_tag ltx_tag_section">3 </span>Retained-Set Descent and Its Cost</h2>

<div id="S3.p1" class="ltx_para">
<p id="S3.p1.1" class="ltx_p">We now allow the conditional bound used in $X$ to change as its blue target decreases.
Throughout the descent we keep $\deg_{R}(v,Y)\geq\pi|Y|$ for every $v\in X\text{,}$ for a fixed $\pi\in(0,1)\text{.}$
This gives cross-density at least $\pi$ after every restriction of $X\text{.}$
A positive function $g(s)$ specifies the required size $\exp(kg(s))$ of $X$ at target $t=sk\text{.}$
To use a bound $\mathsf{D}(q,L,I)\text{,}$ we require $g&gt;L$ to absorb its size constant; the slope condition below absorbs the loss in a blue-neighborhood step.</p>
</div>
<div id="S3.Thmlemma1" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmlemma1.2" class="ltx_text ltx_font_bold">Definition 3.1</span></span><span id="S3.Thmlemma1.3" class="ltx_text ltx_font_bold"> </span>(Route)<span id="S3.Thmlemma1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S3.Thmlemma1.p1" class="ltx_para">
<p id="S3.Thmlemma1.p1.1" class="ltx_p">A <em id="S3.Thmlemma1.p1.1.1" class="ltx_emph ltx_font_italic">route</em> consists of a partition
$0&lt;\theta=u_{0}&lt;\cdots&lt;u_{m}=\lambda\leq 1$ and, on each closed cell $J_{j}=[u_{j-1},u_{j}]\text{,}$ a proved call $\mathsf{D}(q_{j},L_{j},I_{j})$ with $J_{j}\subseteq I_{j}\text{.}$
It also specifies slopes</p>
<table id="S3.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{j}&gt;c(q_{j}):=-\log(1-q_{j})$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.Thmlemma1.p1.2" class="ltx_p">and a continuous positive function $g\text{,}$ constant on $[0,\theta]$ and affine with slope $d_{j}$ on $J_{j}\text{,}$ such that $g&gt;L_{j}$ on every closed cell.</p>
</div>
</div>
<div id="S3.p2" class="ltx_para">
<p id="S3.p2.1" class="ltx_p">The descent starts at ratio $\lambda$ and stops at $\theta\text{.}$
Write $d(t)$ for the piecewise constant slope on $[\theta,\lambda]\text{,}$ taking the right-hand slope at $\theta$ and internal partition points and the left-hand slope at $\lambda\text{.}$</p>
</div>
<div id="Thmtheorem2" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem2.2" class="ltx_text ltx_font_bold">Theorem 2</span></span><span id="Thmtheorem2.3" class="ltx_text ltx_font_bold"> </span>(Retained-Set Rule)<span id="Thmtheorem2.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="Thmtheorem2.p1" class="ltx_para">
<p id="Thmtheorem2.p1.1" class="ltx_p"><span id="Thmtheorem2.p1.1.1" class="ltx_text ltx_font_italic">Fix a route as above, an outer density $p\text{,}$ and a row density $0&lt;\pi&lt;p&lt;1\text{.}$
Choose a strict control at density $\pi$ as the route’s <em id="Thmtheorem2.p1.1.1.1" class="ltx_emph ltx_font_upright">terminal parameters</em>.
If</span></p>
<table id="S3.E8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$z&gt;g(\lambda),\qquad z+wg(\theta)&gt;A+\lambda B+w\theta\beta,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(8)</span></td></tr></tbody>
</table>
<p id="Thmtheorem2.p1.2" class="ltx_p"><span id="Thmtheorem2.p1.2.1" class="ltx_text ltx_font_italic">then $\mathsf{D}(p,z,\{\lambda\})$ holds with</span></p>
<table id="S3.E9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C=\frac{3(1-\pi)}{p-\pi}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(9)</span></td></tr></tbody>
</table>
<p id="Thmtheorem2.p1.3" class="ltx_p"><span id="Thmtheorem2.p1.3.1" class="ltx_text ltx_font_italic">The conclusion is uniform over truncations and vertical shifts of one fixed route when the new endpoint, output exponent, and shift depend continuously on a parameter in a compact set; the stopping ratio, slopes, densities, calls, and terminal controls stay fixed.
At endpoint $r\text{,}$ retain the closed cells $[u_{j-1},\min\{u_{j},r\}]$ with $u_{j-1}&lt;r$ and require positive uniform margins in $g&gt;L_{j}$ and in <a href="#S3.E8" title="In Theorem 2 (Retained-Set Rule). ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">8</span></a>.
Such a family may include $r=\theta\text{,}$ with no internal calls.</span></p>
</div>
</div>
<div id="S3.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.p3" class="ltx_para">
<p id="S3.p3.1" class="ltx_p"><span id="S3.p3.1.1" class="ltx_text">If $\lambda=\theta\text{,}$ the size tests give</span></p>
<table id="S3.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(1+w)z&gt;z+wg(\theta)&gt;A+\theta B+w\theta\beta.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.p3.2" class="ltx_p"><span id="S3.p3.2.1" class="ltx_text">The source leaf at density $\pi$ proves the conclusion at density $p&gt;\pi\text{,}$ with constant $1\leq C\text{.}$</span></p>
</div>
<div id="S3.p4" class="ltx_para">
<p id="S3.p4.1" class="ltx_p"><span id="S3.p4.1.1" class="ltx_text">Suppose $\theta&lt;\lambda\text{,}$ and take a graph of red density at least $p$ and order $N\geq C\mathrm{e}^{kz}\text{.}$
Averaging gives a balanced partition $X_{0},Y$ with cross-density at least $p$ and both parts of size at least $N/3\text{.}$
Keep in $X_{0}$ only the vertices with at least $\pi|Y|$ red neighbors in $Y\text{.}$
The surviving set $X$ satisfies</span></p>
<table id="S3.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(p-\pi)|X_{0}||Y|\leq e_{R}(X,Y)-\pi|X||Y|\leq(1-\pi)|X||Y|.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.p4.2" class="ltx_p"><span id="S3.p4.2.1" class="ltx_text">The choice of $C$ gives $|X|,|Y|\geq\mathrm{e}^{kz}\text{.}$
Every nonempty subset of $X$ has red cross-density at least $\pi$ with this fixed $Y\text{.}$</span></p>
</div>
<div id="S3.p5" class="ltx_para">
<p id="S3.p5.1" class="ltx_p"><span id="S3.p5.1.1" class="ltx_text">Put $n_{0}=\lfloor\theta k\rfloor$ and $\ell=\lfloor\lambda k\rfloor\text{,}$ taking $k$ large enough that $n_{0}\geq 1\text{.}$
To track the loss, define for integers $0\leq t\leq\ell$</span></p>
<table id="S3.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Gamma_{k}(t)=kg(\theta)+\sum_{j=n_{0}+1}^{t}d(j/k)\quad(t&gt;n_{0}),\qquad\Gamma_{k}(t)=kg(\theta)\quad(0\leq t\leq n_{0}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.p5.2" class="ltx_p"><span id="S3.p5.2.1" class="ltx_text">For $V=d_{1}+\sum_{j&lt;m}|d_{j+1}-d_{j}|\text{,}$</span></p>
<table id="S3.E10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Gamma_{k}(t)-\Gamma_{k}(t-1)=d(t/k)\quad(t&gt;n_{0}),\qquad|\Gamma_{k}(t)-kg(t/k)|\leq V.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(10)</span></td></tr></tbody>
</table>
<p id="S3.p5.3" class="ltx_p"><span id="S3.p5.3.1" class="ltx_text">For the second bound, express $d$ as its initial step at $\theta$ and its subsequent jumps.
For each unit step, the mesh count differs from $k$ times its integral by at most one, even when a jump lies on the mesh.
Summing the absolute jump sizes gives $V\text{.}$</span></p>
</div>
<div id="S3.p6" class="ltx_para">
<p id="S3.p6.1" class="ltx_p"><span id="S3.p6.1.1" class="ltx_text">Let $C_{j}$ be the call constants and put</span></p>
<table id="S3.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\delta=\min_{j}\min_{J_{j}}(g-L_{j})&gt;0,\qquad\eta=\min_{j}(1-q_{j}-\mathrm{e}^{-d_{j}})&gt;0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.p6.2" class="ltx_p"><span id="S3.p6.2.1" class="ltx_text">Choose $k$ so that $k\delta&gt;V+\max_{j}\log C_{j}$ and $\eta\mathrm{e}^{kg(\theta)}&gt;1\text{,}$ and so that all call and candidate thresholds hold.
We prove by induction on $t=1,\ldots,\ell$ that $(Z,Y)$ is $(k,\ell,t)$-good whenever $Z\subseteq X$ and $|Z|\geq\mathrm{e}^{\Gamma_{k}(t)}\text{.}$</span></p>
</div>
<div id="S3.p7" class="ltx_para">
<p id="S3.p7.1" class="ltx_p"><span id="S3.p7.1.1" class="ltx_text">For $t\leq n_{0}\text{,}$ the terminal test gives</span></p>
<table id="S3.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log(|Z|^{w}|Y|)\geq k[wg(\theta)+z]&gt;k(A+\lambda B+w\theta\beta)\geq kA+\ell B+wt\beta.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.p7.2" class="ltx_p"><span id="S3.p7.2.1" class="ltx_text">Since $d_{R}(Z,Y)\geq\pi\text{,}$ <a href="#S2.Thmlemma1" title="Lemma 2.1 (Weighted Candidate Bound). ‣ 2.2 The Weighted Candidate Bound ‣ 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a> applies.</span></p>
</div>
<div id="S3.p8" class="ltx_para">
<p id="S3.p8.1" class="ltx_p"><span id="S3.p8.1.1" class="ltx_text">For $t&gt;n_{0}\text{,}$ put $s=t/k$ and use the cell with assigned slope $d_{j}\text{.}$
If the red density in $Z$ is at least $q_{j}\text{,}$ then
$\log|Z|\geq kg(s)-V&gt;kL_{j}(s)+\log C_{j}\text{.}$
The call gives a red $K_{k}$ or a blue $K_{t}\text{.}$
Otherwise some vertex has a blue neighborhood $Z^{\prime}\subseteq Z$ with</span></p>
<table id="S3.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$|Z^{\prime}|&gt;(\mathrm{e}^{-d_{j}}+\eta)(|Z|-1)&gt;\mathrm{e}^{-d_{j}}|Z|\geq\mathrm{e}^{\Gamma_{k}(t-1)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.p8.2" class="ltx_p"><span id="S3.p8.2.1" class="ltx_text">The middle inequality follows from $\eta|Z|&gt;1$ and $\mathrm{e}^{-d_{j}}+\eta&lt;1\text{.}$
Induction applies to $(Z^{\prime},Y)\text{.}$
A blue $K_{t-1}$ extends through the chosen vertex; either of the other two outcomes already proves the claim.</span></p>
</div>
<div id="S3.p9" class="ltx_para">
<p id="S3.p9.1" class="ltx_p"><span id="S3.p9.1.1" class="ltx_text">Finally, <a href="#S3.E10" title="In Proof. ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">10</span></a> and the endpoint test give
$\Gamma_{k}(\ell)\leq kg(\lambda)+V&lt;kz$ for large $k\text{.}$
The claim therefore applies to $Z=X$ at $t=\ell\text{.}$</span></p>
</div>
<div id="S3.p10" class="ltx_para">
<p id="S3.p10.1" class="ltx_p"><span id="S3.p10.1.1" class="ltx_text">For uniformity, take the minimum stopping height and the minima of the strict gaps over the compact parameter set, and the maxima of the finitely many call thresholds.
The same $V$ bounds every truncated profile, since truncation only removes slope jumps.
These choices give a common threshold for $k\text{;}$ at $\lambda=\theta$ use the fixed source control as above.
∎</span></p>
</div>
</div>
<section id="S3.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-cost-of-a-descent"><span class="ltx_tag ltx_tag_subsection">3.1 </span>The Cost of a Descent</h3>

<div id="S3.SS1.p1" class="ltx_para">
<p id="S3.SS1.p1.1" class="ltx_p">Fix the partition, calls, slopes, and terminal controls, and vary the vertical position of $g\text{.}$
Put</p>
<table id="S3.E11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$S(s)=\int_{s}^{\lambda}d(t)\,dt,\qquad M=\max_{j}\max_{s\in J_{j}}\{L_{j}(s)+S(s)\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(11)</span></td></tr></tbody>
</table>
<p id="S3.SS1.p1.2" class="ltx_p">The quantity $S(s)$ is the cumulative logarithmic loss in descending from $\lambda$ to $s\text{.}$
Every $g$ with the specified slopes has the form $g(s)=H-S(s)$ on $[\theta,\lambda]\text{.}$
The internal conditions are exactly $H&gt;M\text{;}$ they also make $g$ positive, since $M\geq L_{1}(\theta)+S(\theta)&gt;S(\theta)\text{.}$
The conditions in <a href="#S3.E8" title="In Theorem 2 (Retained-Set Rule). ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">8</span></a> now read</p>
<table id="S3.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$H&lt;z,\qquad wH+z&gt;A+\lambda B+w\theta\beta+wS(\theta).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS1.p1.3" class="ltx_p">There is such an $H&gt;M$ exactly when</p>
<table id="S3.E12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$z&gt;Z:=\max\left\{M,\frac{A+\lambda B+w\theta\beta+wS(\theta)}{1+w}\right\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(12)</span></td></tr></tbody>
</table>
<p id="S3.SS1.p1.4" class="ltx_p">Necessity follows from $z&gt;H&gt;M$ and $(1+w)z&gt;z+wH\text{.}$
Conversely, if $z&gt;Z\text{,}$ choose $H&lt;z$ sufficiently close to $z$ to satisfy both inequalities.
Thus $Z$ is the infimum output exponent over these vertical positions.
The term $M$ accounts for every internal call together with the loss needed to reach it; the other term is the least exponent compatible with the weighted terminal inequality.</p>
</div>
<div id="S3.SS1.p2" class="ltx_para">
<p id="S3.SS1.p2.1" class="ltx_p">For one call $\mathsf{D}(q,L,[\theta,\lambda])$ with affine $L\text{,}$ choose a slope $d&gt;c(q)\text{.}$
Here $S(s)=d(\lambda-s)\text{,}$ so $L+S$ is affine and its maximum occurs at an endpoint.
Substitution in <a href="#S3.E12" title="In 3.1 The Cost of a Descent ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">12</span></a> gives</p>
<table id="S3.Ex15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Z=\max\left\{L(\lambda),\ L(\theta)+d(\lambda-\theta),\ \frac{A+\lambda B+w\theta\beta+wd(\lambda-\theta)}{1+w}\right\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS1.p2.2" class="ltx_p">The first two terms require enough vertices to use the call at both ends of the interval; the second includes all the loss incurred before reaching $\theta\text{.}$
The third requires enough vertices to apply the weighted bound at $\theta\text{.}$
Every $z&gt;Z$ therefore gives a new conditional bound at $\lambda\text{.}$</p>
</div>
</section>
<section id="S3.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="reuse-on-an-interval"><span class="ltx_tag ltx_tag_subsection">3.2 </span>Reuse on an Interval</h3>

<div id="S3.SS2.p1" class="ltx_para">
<p id="S3.SS2.p1.1" class="ltx_p">To obtain bounds at smaller target ratios, keep the same calls and terminal controls.
For $\theta\leq r\leq\lambda\text{,}$ restrict the profile $g$ to $[0,r]$ and allow a nonnegative vertical shift.
Such a shift preserves the inequalities $g&gt;L_{j}\text{.}$
The resulting infimum is</p>
<table id="S3.E13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E(r)=\max\left\{g(r),\frac{A+rB+w\{\theta\beta+g(r)-g(\theta)\}}{1+w}\right\},\qquad\theta\leq r\leq\lambda.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(13)</span></td></tr></tbody>
</table>
<p id="S3.SS2.p1.2" class="ltx_p">For every $\varepsilon&gt;0\text{,}$ the whole family $\mathsf{D}(p,E+\varepsilon,[\theta,\lambda])$ holds with the constant in <a href="#S3.E9" title="In Theorem 2 (Retained-Set Rule). ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">9</span></a>.
To check strictness uniformly, use the shift
$H_{r}=E(r)-g(r)+\varepsilon/2$ and output $z_{r}=E(r)+\varepsilon\text{.}$
The endpoint gap is $\varepsilon/2\text{,}$ and</p>
<table id="S3.Ex16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$z_{r}+w[g(\theta)+H_{r}]-A-rB-w\theta\beta\geq(1+w/2)\varepsilon.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS2.p1.3" class="ltx_p"><a href="#Thmtheorem2" title="Theorem 2 (Retained-Set Rule). ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> applies uniformly.</p>
</div>
<div id="S3.SS2.p2" class="ltx_para">
<p id="S3.SS2.p2.1" class="ltx_p">A source leaf is affine, and $E$ is the maximum of two affine functions on each affine piece of $g\text{.}$
When a new route uses one of these bounds as a call, refine its cell at the partition points of the called profile.
On each resulting piece, adding the affine loss $S$ preserves convexity.
The maximum in <a href="#S3.E11" title="In 3.1 The Cost of a Descent ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">11</span></a> is therefore attained at an endpoint of a call cell or a partition point of the called profile inside that cell.</p>
</div>
</section>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-optimum-over-finite-proofs"><span class="ltx_tag ltx_tag_section">4 </span>The Optimum over Finite Proofs</h2>

<div id="S4.p1" class="ltx_para">
<p id="S4.p1.1" class="ltx_p">We keep the source $\mathcal{B}_{f}$ fixed and minimize over all finite repetitions of the retained-set rule.</p>
</div>
<div id="S4.Thmlemma1" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmlemma1.2" class="ltx_text ltx_font_bold">Definition 4.1</span></span><span id="S4.Thmlemma1.3" class="ltx_text ltx_font_bold"> </span>(Finite Proof)<span id="S4.Thmlemma1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmlemma1.p1" class="ltx_para">
<p id="S4.Thmlemma1.p1.1" class="ltx_p">A <em id="S4.Thmlemma1.p1.1.1" class="ltx_emph ltx_font_italic">finite proof</em> is a finite derivation of conditional bounds using the following rules:</p>
<ol id="S4.I1" class="ltx_enumerate">
<li id="S4.I1.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S4.I1.i1.p1" class="ltx_para">
<p id="S4.I1.i1.p1.1" class="ltx_p">Start with a weighted source bound from <a href="#S2.E7" title="In 2.3 Conditional Bounds ‣ 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">7</span></a>.</p>
</div></li>
<li id="S4.I1.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S4.I1.i2.p1" class="ltx_para">
<p id="S4.I1.i2.p1.1" class="ltx_p">Apply <a href="#Thmtheorem2" title="Theorem 2 (Retained-Set Rule). ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> with previously derived conditional bounds as its calls, including its uniform families.</p>
</div></li>
<li id="S4.I1.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S4.I1.i3.p1" class="ltx_para">
<p id="S4.I1.i3.p1.1" class="ltx_p">Restrict to a closed ratio interval, increase the density, or increase the continuous exponent function pointwise.</p>
</div></li>
<li id="S4.I1.i4" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">4.</span> 
<div id="S4.I1.i4.p1" class="ltx_para">
<p id="S4.I1.i4.p1.1" class="ltx_p">Combine finitely many bounds: on a finite closed cover of a compact ratio interval, use a continuous output that dominates a proved family at the same density on each cover interval.</p>
</div></li>
</ol>
</div>
</div>
<div id="S4.p2" class="ltx_para">
<p id="S4.p2.1" class="ltx_p">Taking the maximum of the constants and thresholds validates the last rule.
Let $U_{\rm fin}(p,s)$ be the infimum of the exponents obtained at $(p,s)$ by these finite proofs.</p>
</div>
<div id="S4.p3" class="ltx_para">
<p id="S4.p3.1" class="ltx_p">To compare these proofs across all finite depths, first let $U_{0}(p,s)$ be the infimum over source leaves alone.
It is finite: take $w=1\text{,}$ $\mu=1/2\text{,}$ $A&gt;\log 2-2\log p\text{,}$ and $B&gt;b(A)\text{.}$
These strict controls give $0\leq U_{0}(p,s)&lt;\infty\text{.}$</p>
</div>
<div id="S4.p4" class="ltx_para">
<p id="S4.p4.1" class="ltx_p">To treat all possible descents at once, let $u(p,s)$ specify the required exponent for a call at $(p,s)\text{.}$
Order these functions pointwise and consider the complete lattice
$\mathcal{L}=\{u:(0,1)\times(0,1]\to\mathbb{R}:0\leq u\leq U_{0}\}\text{.}$</p>
</div>
<div id="S4.p5" class="ltx_para">
<p id="S4.p5.1" class="ltx_p">Define $T(u)(p,\lambda)$ as the infimum of $U_{0}(p,\lambda)$ and all $z&gt;0$ admitted by the following data:
a finite partition $0&lt;\theta=u_{0}&lt;\cdots&lt;u_{m}=\lambda\text{,}$ densities $q_{j}\in(0,1)\text{,}$ slopes $d_{j}&gt;c(q_{j})\text{,}$ and a continuous positive function $g\text{,}$ affine with slope $d_{j}$ on each $J_{j}$ and constant on $[0,\theta]\text{,}$ such that</p>
<table id="S4.E14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$g(s)&gt;u(q_{j},s)\qquad(s\in J_{j}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(14)</span></td></tr></tbody>
</table>
<p id="S4.p5.2" class="ltx_p">The terminal parameters form a strict control at some row density $0&lt;\pi&lt;p$ and satisfy <a href="#S3.E8" title="In Theorem 2 (Retained-Set Rule). ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">8</span></a>.
All data are finite and fixed before $k$ is chosen.</p>
</div>
<div id="S4.p6" class="ltx_para">
<p id="S4.p6.1" class="ltx_p">The operator is monotone: decreasing the internal requirements can only add feasible routes.
Its output is nonincreasing in the outer density $p\text{,}$ since any leaf or route valid at $p$ remains valid at a larger density.
Set</p>
<table id="S4.Ex17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$U_{n+1}=T(U_{n}),\qquad U_{\infty}=\inf_{n\geq 0}U_{n}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S4.p7" class="ltx_para">
<p id="S4.p7.1" class="ltx_p">We say that $v\in\mathcal{L}$ is a <em id="S4.p7.1.1" class="ltx_emph ltx_font_italic">lower bound preserved by the rules</em> if $v\leq T(v)\text{.}$
In standard order terminology, such a function is a <em id="S4.p7.1.2" class="ltx_emph ltx_font_italic">post-fixed point</em> of $T\text{.}$
Equivalently, every leaf and every route using internal requirements $v$ has output at least $v\text{.}$
Here a proof on a relative neighborhood of $s$ means a conditional bound on a compact ratio interval containing that neighborhood.</p>
</div>
<div id="Thmtheorem3" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem3.2" class="ltx_text ltx_font_bold">Theorem 3</span></span><span id="Thmtheorem3.3" class="ltx_text ltx_font_bold"> </span>(Finite Proofs and Preserved Lower Bounds)<span id="Thmtheorem3.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="Thmtheorem3.p1" class="ltx_para">
<p id="Thmtheorem3.p1.1" class="ltx_p"><span id="Thmtheorem3.p1.1.1" class="ltx_text ltx_font_italic">The sequence $U_{n}$ decreases to the greatest fixed point $U_{\infty}$ of $T$ in $\mathcal{L}\text{,}$ and</span></p>
<table id="S4.E15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$U_{\rm fin}(p,s)=U_{\infty}(p,s)=\sup_{\begin{subarray}{c}v\in\mathcal{L}\\ v\leq T(v)\end{subarray}}v(p,s).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(15)</span></td></tr></tbody>
</table>
<p id="Thmtheorem3.p1.2" class="ltx_p"><span id="Thmtheorem3.p1.2.1" class="ltx_text ltx_font_italic">Every $z&gt;U_{\infty}(p,s)$ has a finite proof with constant output $z$ on a relative neighborhood of $s\text{,}$ with uniform constants.</span></p>
</div>
</div>
<div id="S4.p8" class="ltx_para">
<p id="S4.p8.1" class="ltx_p">The order comparison is the classical greatest-fixed-point principle <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx9" title="" class="ltx_ref">Tarski</a>, Theorem 1]</cite>.
Strict inequalities and compactness also identify the limit with finite conditional proofs, including the uniformity required for their reuse.</p>
</div>
<div id="S4.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.p9" class="ltx_para">
<p id="S4.p9.1" class="ltx_p"><span id="S4.p9.1.1" class="ltx_text">Since $T(U_{0})\leq U_{0}\text{,}$ monotonicity gives $U_{n+1}\leq U_{n}\text{.}$
By induction on $n\text{,}$ we prove both that each ratio section $U_{n}(p,\cdot)$ is upper semicontinuous and that every $z&gt;U_{n}(p,s)$ has a finite proof with constant output $z$ on a relative neighborhood of $s\text{.}$
Upper semicontinuity means that a strict inequality $U_{n}(p,s)&lt;a$ persists near $s\text{.}$
At level zero, both conclusions follow by choosing a continuous source leaf strictly below $z\text{.}$</span></p>
</div>
<div id="S4.p10" class="ltx_para">
<p id="S4.p10.1" class="ltx_p"><span id="S4.p10.1.1" class="ltx_text">Suppose the claim holds at level $n\text{,}$ and let $z&gt;U_{n+1}(p,\lambda)\text{.}$
Choose a leaf or a formal route against $U_{n}$ with output $z^{\prime}&lt;z\text{.}$
A leaf again gives both conclusions by continuity.
For a route, truncate or extend its last affine cell, keeping the density and slope.
Upper semicontinuity preserves $g&gt;U_{n}(q_{m},\cdot)$ near $\lambda\text{,}$ and the strict endpoint and terminal tests persist by continuity.
Thus the same output $z^{\prime}$ is feasible for nearby endpoints, proving $U_{n+1}(p,r)&lt;z$ there.</span></p>
</div>
<div id="S4.p11" class="ltx_para">
<p id="S4.p11.1" class="ltx_p"><span id="S4.p11.1.1" class="ltx_text">Choose a compact interval of endpoints within this range that contains a relative neighborhood of $\lambda\text{.}$
To replace the formal calls by finite proofs, consider the call cells up to the largest endpoint in this neighborhood.
At each point $s$ of a cell with density $q_{j}\text{,}$ choose</span></p>
<table id="S4.Ex18" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$U_{n}(q_{j},s)&lt;z_{s}&lt;g(s).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.p11.2" class="ltx_p"><span id="S4.p11.2.1" class="ltx_text">The induction hypothesis gives a finite proof with constant output $z_{s}$ near $s\text{.}$
Shrink this neighborhood until $z_{s}&lt;g$ throughout.
Compactness gives a finite subcover of each cell.
Subdivide into closed subcells contained in these neighborhoods and use the corresponding proofs, with the original density and slope.
The calls and their strict inequalities also hold at every shared endpoint.
There are finitely many subcells, so their positive gaps have a common positive lower bound.
The uniform part of <a href="#Thmtheorem2" title="Theorem 2 (Retained-Set Rule). ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> now gives a finite proof with constant output $z$ on the chosen endpoint neighborhood.
This completes the induction.</span></p>
</div>
<div id="S4.p12" class="ltx_para">
<p id="S4.p12.1" class="ltx_p"><span id="S4.p12.1.1" class="ltx_text">We next show that $U_{\infty}$ is fixed.
Monotonicity gives $T(U_{\infty})\leq U_{n+1}$ for every $n\text{,}$ hence $T(U_{\infty})\leq U_{\infty}\text{.}$
For the reverse inequality, take a route feasible against $U_{\infty}\text{.}$
On each closed cell $J_{j}\text{,}$ the sets</span></p>
<table id="S4.Ex19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$O_{n}=\{s\in J_{j}:U_{n}(q_{j},s)&lt;g(s)\}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.p12.2" class="ltx_p"><span id="S4.p12.2.1" class="ltx_text">are relatively open, increase with $n\text{,}$ and cover $J_{j}\text{.}$
Compactness and nesting give a common $N$ with $O_{N}=J_{j}$ on every cell.
The route is therefore feasible against $U_{N}\text{,}$ so its output is at least $U_{N+1}\geq U_{\infty}\text{.}$
The leaf alternative is also at least $U_{\infty}\text{.}$
Taking infima gives $T(U_{\infty})=U_{\infty}\text{.}$</span></p>
</div>
<div id="S4.p13" class="ltx_para">
<p id="S4.p13.1" class="ltx_p"><span id="S4.p13.1.1" class="ltx_text">If $v\in\mathcal{L}$ and $v\leq T(v)\text{,}$ then $v\leq U_{0}$ and</span></p>
<table id="S4.Ex20" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$v\leq U_{n}\quad\Longrightarrow\quad v\leq T(v)\leq T(U_{n})=U_{n+1}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.p13.2" class="ltx_p"><span id="S4.p13.2.1" class="ltx_text">Hence $v\leq U_{\infty}\text{.}$
As $U_{\infty}$ is itself fixed, it is the greatest post-fixed point.</span></p>
</div>
<div id="S4.p14" class="ltx_para">
<p id="S4.p14.1" class="ltx_p"><span id="S4.p14.1.1" class="ltx_text">Every finite proof has output at least $U_{\infty}\text{,}$ by induction through its rules.
This holds for leaves since $U_{0}\geq U_{\infty}\text{.}$
A route whose calls are at least $U_{\infty}$ is feasible against $U_{\infty}\text{,}$ so its output is at least $T(U_{\infty})=U_{\infty}\text{.}$
The case $\lambda=\theta$ reduces to a leaf.
Restriction, increasing the exponent, and finite patching preserve the comparison.
Increasing the density does too, since $U_{\infty}$ is nonincreasing in that density.
Thus $U_{\rm fin}\geq U_{\infty}\text{.}$</span></p>
</div>
<div id="S4.p15" class="ltx_para">
<p id="S4.p15.1" class="ltx_p"><span id="S4.p15.1.1" class="ltx_text">Conversely, every $z&gt;U_{\infty}(p,s)$ exceeds $U_{n}(p,s)$ for some finite $n\text{.}$
The local proof constructed above gives $U_{\rm fin}\leq U_{\infty}$ and the claimed uniformity.
∎</span></p>
</div>
</div>
</section>
<section id="S5" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="concave-lower-bounds"><span class="ltx_tag ltx_tag_section">5 </span>Concave Lower Bounds</h2>

<div id="S5.p1" class="ltx_para">
<p id="S5.p1.1" class="ltx_p">We construct a function $v\leq T(v)\text{,}$ giving the lower estimate by <a href="#Thmtheorem3" title="Theorem 3 (Finite Proofs and Preserved Lower Bounds). ‣ 4 The Optimum over Finite Proofs ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3</span></a>.
Its exponent will be a <em id="S5.p1.1.1" class="ltx_emph ltx_font_italic">concave polygon</em>: a continuous piecewise affine concave function $F:[0,1]\to\mathbb{R}\text{.}$
Write its partition points and values as</p>
<table id="S5.Ex21" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$0=s_{0}&lt;s_{1}&lt;\cdots&lt;s_{N}=1,\qquad F_{i}=F(s_{i}),\qquad F_{0}=0,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.p1.2" class="ltx_p">and suppose the slopes $d_{i}=(F_{i}-F_{i-1})/(s_{i}-s_{i-1})$ satisfy
$d_{1}\geq\cdots\geq d_{N}&gt;0\text{.}$
A call at density $q&gt;1-\mathrm{e}^{-d_{i}}$ requires a route slope greater than $c(q)&gt;d_{i}\text{.}$
This relation suggests using $1-\mathrm{e}^{-d_{i}}$ as the density up to which $F$ gives a lower bound.
Define</p>
<table id="S5.Ex22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p_{F}(s)=1-\mathrm{e}^{-d_{i}}\quad(s_{i-1}&lt;s\leq s_{i}),\qquad v_{F}(p,s)=\begin{cases}F(s),&amp;p\leq p_{F}(s),\\ 0,&amp;p&gt;p_{F}(s).\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.p1.3" class="ltx_p">At each $s_{i}&gt;0\text{,}$ $p_{F}$ uses the slope of the segment ending there.</p>
</div>
<div id="S5.Thmlemma1" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmlemma1.2" class="ltx_text ltx_font_bold">Proposition 5.1</span></span><span id="S5.Thmlemma1.3" class="ltx_text ltx_font_bold"> </span>(A Preserved Lower Bound)<span id="S5.Thmlemma1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmlemma1.p1" class="ltx_para">
<p id="S5.Thmlemma1.p1.1" class="ltx_p"><span id="S5.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">Suppose every strict terminal control of row density at most $p_{F}(\lambda)$ satisfies</span></p>
<table id="S5.E16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$F(\lambda)+wF(\theta)\leq A+\lambda B+w\theta\beta\qquad(0\leq\theta\leq\lambda\leq 1,\ \lambda&gt;0).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(16)</span></td></tr></tbody>
</table>
<p id="S5.Thmlemma1.p1.2" class="ltx_p"><span id="S5.Thmlemma1.p1.2.1" class="ltx_text ltx_font_italic">Then $v_{F}\leq U_{\infty}\text{.}$
If $d_{N}\geq\log 2\text{,}$ in particular $F(1)\leq U_{\infty}(1/2,1)\text{.}$</span></p>
</div>
</div>
<div id="S5.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.p2" class="ltx_para">
<p id="S5.p2.1" class="ltx_p"><span id="S5.p2.1.1" class="ltx_text">Taking $\theta=\lambda$ in <a href="#S5.E16" title="In Proposition 5.1 (A Preserved Lower Bound). ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">16</span></a> shows that every source leaf at density $p\leq p_{F}(\lambda)$ has exponent at least $F(\lambda)\text{.}$
Thus $0\leq v_{F}\leq U_{0}\text{.}$</span></p>
</div>
<div id="S5.p3" class="ltx_para">
<p id="S5.p3.1" class="ltx_p"><span id="S5.p3.1.1" class="ltx_text">Consider a route feasible against $v_{F}$ at density $p\leq p_{F}(\lambda)\text{,}$ with output $z&lt;F(\lambda)\text{.}$
Its endpoint satisfies $g(\lambda)&lt;F(\lambda)\text{.}$
Refine the call partition at the points $s_{i}\text{.}$
On a resulting cell $[a,b]\text{,}$ let $\ell_{j}$ and $d_{i}$ be the slopes of $g$ and $F\text{.}$
If $g(b)&lt;F(b)\text{,}$ the closed call condition forces $q_{j}&gt;p_{F}(b)=1-\mathrm{e}^{-d_{i}}\text{,}$ since $p_{F}$ uses the left slope at $b\text{.}$
Consequently $\ell_{j}&gt;c(q_{j})&gt;d_{i}\text{,}$ and</span></p>
<table id="S5.Ex23" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$g(a)-F(a)=g(b)-F(b)-(\ell_{j}-d_{i})(b-a)&lt;0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.p3.2" class="ltx_p"><span id="S5.p3.2.1" class="ltx_text">Starting at $\lambda$ and applying this implication backward through the finite partition gives $g(\theta)&lt;F(\theta)\text{.}$
The row density satisfies $\pi&lt;p\leq p_{F}(\lambda)\text{,}$ so <a href="#S5.E16" title="In Proposition 5.1 (A Preserved Lower Bound). ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">16</span></a> now contradicts
$z+wg(\theta)&gt;A+\lambda B+w\theta\beta\text{.}$
Every route and leaf therefore has output at least $v_{F}\text{,}$ giving $v_{F}\leq T(v_{F})\text{.}$
Apply <a href="#Thmtheorem3" title="Theorem 3 (Finite Proofs and Preserved Lower Bounds). ‣ 4 The Optimum over Finite Proofs ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3</span></a>; the final assertion follows from $p_{F}(1)\geq 1/2\text{.}$
∎</span></p>
</div>
</div>
<section id="S5.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="elimination-of-the-terminal-controls"><span class="ltx_tag ltx_tag_subsection">5.1 </span>Elimination of the Terminal Controls</h3>

<div id="S5.SS1.p1" class="ltx_para">
<p id="S5.SS1.p1.1" class="ltx_p">At each positive partition point, we maximize over the stopping ratio and combine the terminal inequalities with the supporting-line formula.
This gives a test in the single parameter $\mu\text{.}$
For $0&lt;\mu&lt;1\text{,}$ write $\tau=-\log(1-\mu)$ and $\beta=-\log\mu\text{,}$ and define</p>
<table id="S5.E17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Psi(\lambda,z,\kappa,\mu)=\frac{1-\mu}{\kappa}\left[z-\lambda\widehat{f}\!\left(\frac{1-\kappa}{\lambda}\right)\right],\qquad\lambda&gt;0,\quad 0&lt;\kappa&lt;1.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(17)</span></td></tr></tbody>
</table>
</div>
<div id="Thmtheorem4" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem4.2" class="ltx_text ltx_font_bold">Theorem 4</span></span><span id="Thmtheorem4.3" class="ltx_text ltx_font_bold"> </span>(Finite Polygon Criterion)<span id="Thmtheorem4.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="Thmtheorem4.p1" class="ltx_para">
<p id="Thmtheorem4.p1.1" class="ltx_p"><span id="Thmtheorem4.p1.1.1" class="ltx_text ltx_font_italic">Suppose $F$ is as above and</span></p>
<table id="S5.E18" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$0&lt;F_{i}&lt;\min\{f(s_{i}),h(s_{i})\}\qquad(1\leq i\leq N).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(18)</span></td></tr></tbody>
</table>
<p id="Thmtheorem4.p1.2" class="ltx_p"><span id="Thmtheorem4.p1.2.1" class="ltx_text ltx_font_italic">For each $\mu\in(0,1)$ define</span></p>
<table id="S5.E19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D_{i}(\beta)=\max_{0\leq j\leq i}(F_{j}-s_{j}\beta),\qquad\kappa_{i}=D_{i}(\beta)/\tau,\qquad P_{i}=-\log(1-\mathrm{e}^{-d_{i}}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(19)</span></td></tr></tbody>
</table>
<p id="Thmtheorem4.p1.3" class="ltx_p"><span id="Thmtheorem4.p1.3.1" class="ltx_text ltx_font_italic">If, for every $i$ and every $\mu$ with $D_{i}(\beta)&gt;0\text{,}$</span></p>
<table id="S5.E20" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Psi(s_{i},F_{i},\kappa_{i},\mu)\leq P_{i},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(20)</span></td></tr></tbody>
</table>
<p id="Thmtheorem4.p1.4" class="ltx_p"><span id="Thmtheorem4.p1.4.1" class="ltx_text ltx_font_italic">then $v_{F}\leq U_{\infty}\text{.}$</span></p>
</div>
</div>
<div id="S5.SS1.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS1.p2" class="ltx_para">
<p id="S5.SS1.p2.1" class="ltx_p"><span id="S5.SS1.p2.1.1" class="ltx_text">At endpoint $s_{i}\text{,}$ the function $F(\theta)-\theta\beta$ is affine between consecutive partition points, so</span></p>
<table id="S5.Ex24" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\max_{0\leq\theta\leq s_{i}}\{F(\theta)-\theta\beta\}=D_{i}(\beta).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS1.p2.2" class="ltx_p"><span id="S5.SS1.p2.2.1" class="ltx_text">Concavity of $h$ and <a href="#S5.E18" title="In Theorem 4 (Finite Polygon Criterion). ‣ 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">18</span></a> put $F(\theta)$ strictly below $h(\theta)$ for $\theta&gt;0\text{.}$
The minimum of $\tau+\theta\beta$ over $0&lt;\mu&lt;1$ occurs at $\mu=\theta/(1+\theta)$ and equals $h(\theta)\text{.}$
Thus</span></p>
<table id="S5.Ex25" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$F(\theta)&lt;h(\theta)\leq\tau+\theta\beta\qquad(\theta&gt;0).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS1.p2.3" class="ltx_p"><span id="S5.SS1.p2.3.1" class="ltx_text">The term at $\theta=0$ is zero, so $0\leq D_{i}(\beta)&lt;\tau\text{.}$</span></p>
</div>
<div id="S5.SS1.p3" class="ltx_para">
<p id="S5.SS1.p3.1" class="ltx_p"><span id="S5.SS1.p3.1.1" class="ltx_text">Fix a strict control at row density $\pi\leq 1-\mathrm{e}^{-d_{i}}$ and put $P_{\pi}=-\log\pi\geq P_{i}\text{.}$
If the terminal inequality fails at $\lambda=s_{i}$ for some stopping ratio, then</span></p>
<table id="S5.Ex26" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$wD_{i}&gt;A+s_{i}B-F_{i}&gt;0,\qquad A&gt;w\tau+\frac{P_{\pi}}{1-\mu}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS1.p3.2" class="ltx_p"><span id="S5.SS1.p3.2.1" class="ltx_text">Here $A+s_{i}B-F_{i}&gt;0$ because $A+s_{i}B\geq f(s_{i})&gt;F_{i}\text{.}$
In particular $0&lt;\kappa_{i}=D_{i}/\tau&lt;1\text{.}$
Multiplying the second inequality by $\kappa_{i}$ and using the first gives</span></p>
<table id="S5.Ex27" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(1-\kappa_{i})A+s_{i}B&lt;F_{i}-\frac{\kappa_{i}P_{\pi}}{1-\mu}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS1.p3.3" class="ltx_p"><span id="S5.SS1.p3.3.1" class="ltx_text">Since $B&gt;b(A)\text{,}$ the supporting-line formula <a href="#S2.E5" title="In 2.1 Source Pairs and Supporting Lines ‣ 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">5</span></a> gives</span></p>
<table id="S5.Ex28" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$s_{i}\widehat{f}\!\left(\frac{1-\kappa_{i}}{s_{i}}\right)\leq(1-\kappa_{i})A+s_{i}B.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS1.p3.4" class="ltx_p"><span id="S5.SS1.p3.4.1" class="ltx_text">Combining these inequalities yields
$P_{\pi}&lt;\Psi(s_{i},F_{i},\kappa_{i},\mu)\leq P_{i}\text{,}$ a contradiction.
Thus <a href="#S5.E16" title="In Proposition 5.1 (A Preserved Lower Bound). ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">16</span></a> holds for every stopping ratio at each positive partition point.</span></p>
</div>
<div id="S5.SS1.p4" class="ltx_para">
<p id="S5.SS1.p4.1" class="ltx_p"><span id="S5.SS1.p4.1.1" class="ltx_text">Now fix controls at row density at most $1-\mathrm{e}^{-d_{i}}$ and let $\lambda\in[s_{i-1},s_{i}]\text{.}$
Since $F$ is affine on this interval,</span></p>
<table id="S5.Ex29" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\max_{0\leq\theta\leq\lambda}\{F(\theta)-\theta\beta\}=\max\{D_{i-1}(\beta),\ F(\lambda)-\lambda\beta\},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS1.p4.2" class="ltx_p"><span id="S5.SS1.p4.2.1" class="ltx_text">where $D_{0}=0\text{.}$
The largest terminal difference over all stopping ratios is therefore</span></p>
<table id="S5.Ex30" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$F(\lambda)-A-\lambda B+w\max\{D_{i-1}(\beta),\ F(\lambda)-\lambda\beta\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS1.p4.3" class="ltx_p"><span id="S5.SS1.p4.3.1" class="ltx_text">This is convex in $\lambda\text{,}$ being affine plus a positive multiple of a maximum of two affine functions.
It is nonpositive at $s_{i}$ by the inequality already proved there.
The same holds at $s_{i-1}&gt;0$ because the left slope of $F$ there is at least $d_{i}\text{;}$ at zero the value is $-A&lt;0\text{.}$
Convexity gives <a href="#S5.E16" title="In Proposition 5.1 (A Preserved Lower Bound). ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">16</span></a> throughout the interval.
Apply <a href="#S5.Thmlemma1" title="Proposition 5.1 (A Preserved Lower Bound). ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>.
∎</span></p>
</div>
</div>
</section>
<section id="S5.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-full-control-interval"><span class="ltx_tag ltx_tag_subsection">5.2 </span>The Full Control Interval</h3>

<div id="S5.SS2.p1" class="ltx_para">
<p id="S5.SS2.p1.1" class="ltx_p">For the supplied polygon, the remaining variable is $\tau\in(0,\infty)\text{,}$ with
$\mu=1-\mathrm{e}^{-\tau}$ and $\beta(\tau)=-\log(1-\mathrm{e}^{-\tau})\text{.}$
We verify the criterion analytically near zero and infinity, leaving a compact interval for the finite computation.
Let $L=1/10$ and $H=10\text{.}$
The supplied data satisfy</p>
<table id="S5.E21" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\beta(L)&gt;d_{1},\qquad\beta(H)&lt;F_{N}/2,\qquad F_{N}&lt;H,\qquad 2H\mathrm{e}^{-H}&lt;P_{1}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(21)</span></td></tr></tbody>
</table>
<p id="S5.SS2.p1.2" class="ltx_p">For $\tau\leq L\text{,}$ concavity gives $F_{j}\leq d_{1}s_{j}&lt;\beta s_{j}$ for $j&gt;0\text{,}$ so $D_{i}=0\text{.}$
For $\tau\geq H\text{,}$ concavity gives $F_{i}/s_{i}\geq F_{N}$ and hence
$D_{i}\geq F_{i}-s_{i}\beta\geq F_{i}/2\text{.}$
Also $D_{i}\leq F_{N}&lt;\tau\text{.}$
The source term in <a href="#S5.E17" title="In 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">17</span></a> is nonnegative, so</p>
<table id="S5.Ex31" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Psi(s_{i},F_{i},\kappa_{i},\mu)\leq\mathrm{e}^{-\tau}\frac{F_{i}\tau}{D_{i}}\leq 2\tau\mathrm{e}^{-\tau}\leq 2H\mathrm{e}^{-H}&lt;P_{1}\leq P_{i}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS2.p1.3" class="ltx_p">Thus only the closed interval $[L,H]$ requires subdivision.</p>
</div>
<div id="S5.SS2.p2" class="ltx_para">
<p id="S5.SS2.p2.1" class="ltx_p">On each control cell, outward interval arithmetic first encloses $\beta\text{.}$
The function $D_{i}$ is nonincreasing in $\beta\text{,}$ so its two endpoint evaluations enclose the finite maximum in <a href="#S5.E19" title="In Theorem 4 (Finite Polygon Criterion). ‣ 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">19</span></a>.
The source $\widehat{f}$ increases, so its endpoint values enclose the source term in <a href="#S5.E17" title="In 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">17</span></a>.
A cell is accepted if it proves $D_{i}=0$ throughout, or a nonpositive numerator in <a href="#S5.E17" title="In 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">17</span></a> wherever $D_{i}&gt;0\text{.}$
Points with $D_{i}=0$ already satisfy the terminal condition, since $F_{i}&lt;A+s_{i}B\text{.}$
Otherwise the checker requires a positive lower bound for $\kappa_{i}$ before division, and accepts the cell only if it proves $P_{i}-\Psi&gt;0\text{.}$
All other cells are subdivided.
The checker verifies an exact closed cover of $[L,H]$ for every positive partition point.
<a href="#Thmtheorem4" title="Theorem 4 (Finite Polygon Criterion). ‣ 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4</span></a> then covers all weights, source supports, stopping ratios, endpoint ratios, and finite depths.</p>
</div>
</section>
</section>
<section id="S6" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-diagonal-bounds"><span class="ltx_tag ltx_tag_section">6 </span>The Diagonal Bounds</h2>

<div id="S6.p1" class="ltx_para">
<p id="S6.p1.1" class="ltx_p">We now evaluate the two sides of <a href="#S4.E15" title="In Theorem 3 (Finite Proofs and Preserved Lower Bounds). ‣ 4 The Optimum over Finite Proofs ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">15</span></a>.
The repository specifies the source, a finite upper proof, and a rational lower polygon, with the following complete interval covers.</p>
<table id="S6.p1.2" class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr id="S6.p1.2.1" class="ltx_tr">
<th id="S6.p1.2.1.1" class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_th_row ltx_border_tt">Construction</th>
<th id="S6.p1.2.1.2" class="ltx_td ltx_align_right ltx_th ltx_th_column ltx_border_tt">Size</th>
<th id="S6.p1.2.1.3" class="ltx_td ltx_align_right ltx_th ltx_th_column ltx_border_tt">Checked Cells</th></tr>
</thead>
<tbody class="ltx_tbody">
<tr id="S6.p1.2.2" class="ltx_tr">
<th id="S6.p1.2.2.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">Source profile</th>
<td id="S6.p1.2.2.2" class="ltx_td ltx_align_right ltx_border_t">2,279 cubic pieces</td>
<td id="S6.p1.2.2.3" class="ltx_td ltx_align_right ltx_border_t">12,319</td></tr>
<tr id="S6.p1.2.3" class="ltx_tr">
<th id="S6.p1.2.3.1" class="ltx_td ltx_align_left ltx_th ltx_th_row">Upper proof</th>
<td id="S6.p1.2.3.2" class="ltx_td ltx_align_right">2,932 routes; depth 27</td>
<td id="S6.p1.2.3.3" class="ltx_td ltx_align_right">1,065,279</td></tr>
<tr id="S6.p1.2.4" class="ltx_tr">
<th id="S6.p1.2.4.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb">Lower polygon</th>
<td id="S6.p1.2.4.2" class="ltx_td ltx_align_right ltx_border_bb">2,048 affine pieces</td>
<td id="S6.p1.2.4.3" class="ltx_td ltx_align_right ltx_border_bb">853,082</td></tr>
</tbody>
</table>
</div>
<div id="S6.p2" class="ltx_para">
<p id="S6.p2.1" class="ltx_p">The source inequalities are evaluated at 224 fractional binary bits, and the upper and lower inequalities at both 224 and 320 bits.
An independent integer-prefix computation reproduces every route height and loss from the checked primitive enclosures.
The repository contains the four rational inputs in <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">data/</span>, the Python certificate checker in <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">proof/</span>, and the Lean formalization in <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">lean/</span>.
The Python checker uses only the standard library. Running <span id="S6.p2.1.1" class="ltx_text ltx_font_typewriter">python proof/replay.py --workers 16</span> from the repository root writes the results and input and code hashes to <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">proof/build/replay/</span>.
The root <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">README.md</span> gives the build and reproduction instructions for both projects.</p>
</div>
<section id="S6.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="exact-interval-arithmetic"><span class="ltx_tag ltx_tag_subsection">6.1 </span>Exact Interval Arithmetic</h3>

<div id="S6.SS1.p1" class="ltx_para">
<p id="S6.SS1.p1.1" class="ltx_p">Transcendental quantities are enclosed by intervals whose endpoints are integers divided by a fixed power of two. Rational inputs and arithmetic operations are rounded outward. For logarithms, reduce to $y\in[1,2]$ and put $u=(y-1)/(y+1)\in[0,1/3]\text{.}$ Then</p>
<table id="S6.E22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log y=2\sum_{j=0}^{m-1}\frac{u^{2j+1}}{2j+1}+E_{m},\qquad 0\leq E_{m}\leq\frac{3u^{2m+1}}{2m+1}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(22)</span></td></tr></tbody>
</table>
<p id="S6.SS1.p1.2" class="ltx_p">The tail is at most $2u^{2m+1}/((2m+1)(1-u^{2}))\text{.}$ The same formula encloses $\log 2$ for reversing the scaling.</p>
</div>
<div id="S6.SS1.p2" class="ltx_para">
<p id="S6.SS1.p2.1" class="ltx_p">For the exponential, put $S_{m}(z)=\sum_{j=0}^{m}z^{j}/j!$ for integers $m\geq 0\text{.}$
Successive terms after degree $m$ have ratio at most $z/(m+2)\text{,}$ so a geometric sum gives</p>
<table id="S6.E23" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$S_{m}(z)&lt;\mathrm{e}^{z}\leq S_{m}(z)+\frac{z^{m+1}}{(m+1)!}\frac{1}{1-z/(m+2)}\qquad(0&lt;z&lt;m+2).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(23)</span></td></tr></tbody>
</table>
<p id="S6.SS1.p2.2" class="ltx_p">At zero the sum is exact.
The interval backend reduces a nonnegative argument to $0\leq y\leq 1/8\text{,}$ where this tail is at most $2y^{m+1}/(m+1)!\text{.}$
Repeated squaring reverses the scaling; negative arguments use outward reciprocals.
A logarithm or division is accepted only after its domain is checked.
For the final exponential bound, a separate rational calculation applies <a href="#S6.E23" title="In 6.1 Exact Interval Arithmetic ‣ 6 The Diagonal Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">23</span></a> directly with $m=140$ and compares the upper enclosure with $3.69507\text{.}$</p>
</div>
</section>
<section id="S6.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="a-finite-upper-proof"><span class="ltx_tag ltx_tag_subsection">6.2 </span>A Finite Upper Proof</h3>

<div id="S6.SS2.p1" class="ltx_para">
<p id="S6.SS2.p1.1" class="ltx_p">The file <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">data/upper.json</span> contains an ordered list of routes.
A call names either a weighted source bound or an earlier route with a terminal control.
All 2,932 routes are reachable from the root.
The density, height, and output margins are all $10^{-12}\text{;}$ rounding is upward to multiples of $10^{-12}\text{.}$
The source pairs use the inward factor $1-10^{-9}\text{,}$ and we put $\rho=1-2\cdot 10^{-5}\text{.}$</p>
</div>
<div id="S6.SS2.p2" class="ltx_para">
<p id="S6.SS2.p2.1" class="ltx_p">For each control, let $\pi$ be its leaf density when it defines a source bound, and $\rho p$ when it ends a route at outer density $p\text{.}$
The checker computes</p>
<table id="S6.Ex32" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$x_{\rm cap}=(1-\mu)^{w}\pi^{1/(1-\mu)}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS2.p2.2" class="ltx_p">and an explicit boundary pair $(\xi,\zeta)$ with $\xi\geq x_{\rm cap}\text{.}$
It uses $x=(1-10^{-9})x_{\rm cap}$ and $y=(1-10^{-9})\zeta\text{.}$
Both coordinates are strictly below a supporting pair, and $x&lt;x_{\rm cap}\text{,}$ so the control is strict.
Source supports are given explicitly in the data and checked by interval inequalities.
For a source leaf, the coefficients $A/(1+w)$ and $(B+w\beta)/(1+w)$ are rounded upward, giving a rational affine upper bound for <a href="#S2.E7" title="In 2.3 Conditional Bounds ‣ 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">7</span></a>.</p>
</div>
<div id="S6.SS2.p3" class="ltx_para">
<p id="S6.SS2.p3.1" class="ltx_p">For a reused child with stored profile $g$ and stopping ratio $\theta\text{,}$ upward enclosures of its terminal parameters give rational coefficients</p>
<table id="S6.Ex33" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$a^{+}\geq\frac{A+w\theta\beta}{1+w},\qquad b^{+}\geq\frac{B}{1+w},\qquad t^{+}\geq\frac{w}{1+w}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS2.p3.2" class="ltx_p">Its called family is</p>
<table id="S6.Ex34" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\max\{g(s),\ a^{+}+b^{+}s+t^{+}(g(s)-g(\theta))\}+10^{-12}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS2.p3.3" class="ltx_p">This dominates <a href="#S3.E13" title="In 3.2 Reuse on an Interval ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">13</span></a> with a strict allowance; rounding $t^{+}$ upward is valid because $g(s)-g(\theta)\geq 0\text{.}$</p>
</div>
<div id="S6.SS2.p4" class="ltx_para">
<p id="S6.SS2.p4.1" class="ltx_p">With these calls established, the parent route can be evaluated.
Each slope is an upward-rounded enclosure of $c(q_{j})+10^{-12}\text{,}$ so the sums defining $S$ are rational.
The endpoint rule in <a href="#S3.E11" title="In 3.1 The Cost of a Descent ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">11</span></a> gives $M$ by checking the parent cell endpoints and the child profiles’ partition points inside each cell.
With $Q=10^{12}\text{,}$ the parent stores</p>
<table id="S6.Ex35" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$H=\frac{\lceil Q(M+10^{-12})\rceil}{Q},\qquad g=H-S.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS2.p4.2" class="ltx_p">The checker also verifies the full partitions, density implications, child-domain containment, and strict ordering of child indices.
Induction through the ordered list and <a href="#Thmtheorem2" title="Theorem 2 (Retained-Set Rule). ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">2</span></a> prove all its conditional families.</p>
</div>
<div id="S6.SS2.p5" class="ltx_para">
<p id="S6.SS2.p5.1" class="ltx_p">The root has</p>
<table id="S6.Ex36" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p=\tfrac{1}{2},\qquad\pi=\tfrac{1}{2}-10^{-5},\qquad\theta=\tfrac{1}{4},\qquad\lambda=1,\qquad w=1,\qquad\mu=\tfrac{1}{4}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS2.p5.2" class="ltx_p">It has 65 cells and uses the left source support in <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">data/upper.json</span>, at $t\approx 0.383\text{.}$
Exact reconstruction gives $g(1)&gt;1.3\text{,}$ while the second term in <a href="#S3.E13" title="In 3.2 Reuse on an Interval ‣ 3 Retained-Set Descent and Its Cost ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">13</span></a> is less than $1.2\text{.}$
Adding the output margin yields the constant conditional exponent</p>
<table id="S6.Ex37" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$z_{+}=g(1)+10^{-12}=\frac{1306998938417}{10^{12}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS2.p5.3" class="ltx_p">Thus $U_{\infty}(1/2,1)\leq z_{+}\text{.}$</p>
</div>
</section>
<section id="S6.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-lower-polygon"><span class="ltx_tag ltx_tag_subsection">6.3 </span>The Lower Polygon</h3>

<div id="S6.SS3.p1" class="ltx_para">
<p id="S6.SS3.p1.1" class="ltx_p">The file <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">data/lower.json</span> specifies the 2,049 rational partition points and values of $F\text{.}$
Exact rational comparisons establish positive decreasing slopes and $F(0)=0\text{.}$
Interval comparisons establish <a href="#S5.E18" title="In Theorem 4 (Finite Polygon Criterion). ‣ 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">18</span></a>, the tail bounds in <a href="#S5.E21" title="In 5.2 The Full Control Interval ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">21</span></a>, and $d_{N}&gt;\log 2\text{.}$
The 853,082 closed control cells verify <a href="#S5.E20" title="In Theorem 4 (Finite Polygon Criterion). ‣ 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">20</span></a>.
<a href="#Thmtheorem4" title="Theorem 4 (Finite Polygon Criterion). ‣ 5.1 Elimination of the Terminal Controls ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4</span></a> and <a href="#S5.Thmlemma1" title="Proposition 5.1 (A Preserved Lower Bound). ‣ 5 Concave Lower Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> therefore give</p>
<table id="S6.Ex38" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$z_{-}:=F(1)=\frac{1305460275532}{10^{12}}\leq U_{\infty}(1/2,1).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S6.SS3.p2" class="ltx_para">
<p id="S6.SS3.p2.1" class="ltx_p">The resulting interval for the finite-proof optimum has width less than $0.0016\text{.}$</p>
</div>
<div id="S6.SS3.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#Thmtheorem1" title="Theorem 1. ‣ 1 Introduction ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a>.</h6>
<div id="S6.SS3.p3" class="ltx_para">
<p id="S6.SS3.p3.1" class="ltx_p"><span id="S6.SS3.p3.1.1" class="ltx_text">The finite upper proof and the preserved polygon give <a href="#S1.E1" title="In Theorem 1. ‣ 1 Introduction ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1</span></a> by <a href="#Thmtheorem3" title="Theorem 3 (Finite Proofs and Preserved Lower Bounds). ‣ 4 The Optimum over Finite Proofs ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3</span></a>.
In an arbitrary two-coloring, interchange the colors so that red has density at least $1/2$ and apply the root conditional bound.
Its constant is</span></p>
<table id="S6.Ex39" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{3(1-\pi)}{1/2-\pi}=150003,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS3.p3.2" class="ltx_p"><span id="S6.SS3.p3.2.1" class="ltx_text">which proves <a href="#S1.E2" title="In Theorem 1. ‣ 1 Introduction ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2</span></a>.
An independent rational Taylor enclosure gives $\mathrm{e}^{z_{+}}&lt;3.69507\text{.}$
This strict gap absorbs the fixed factor and the ceiling for sufficiently large $k\text{.}$
∎</span></p>
</div>
</div>
<div class="ltx_pagination ltx_role_newpage"></div>
</section>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography" id="references">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bibx1" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[CGMS]</span>
<span class="ltx_bibblock"> M. Campos, S. Griffiths, R. Morris, and J. Sahasrabudhe, An exponential improvement for diagonal Ramsey, <em id="bib.bibx1.2" class="ltx_emph ltx_font_italic">Annals of Mathematics</em> <span id="bib.bibx1.3" class="ltx_text ltx_font_bold">203</span> (2026), no. 3, 869–932. <a href="https://doi.org/10.4007/annals.2026.203.3.4" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://doi.org/10.4007/annals.2026.203.3.4</a>.

</span></li>
      
<li id="bib.bibx2" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Con]</span>
<span class="ltx_bibblock"> D. Conlon, A new upper bound for diagonal Ramsey numbers, <em id="bib.bibx2.2" class="ltx_emph ltx_font_italic">Annals of Mathematics</em> <span id="bib.bibx2.3" class="ltx_text ltx_font_bold">170</span> (2009), no. 2, 941–960. <a href="https://doi.org/10.4007/annals.2009.170.941" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://doi.org/10.4007/annals.2009.170.941</a>.

</span></li>
      
<li id="bib.bibx3" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Er]</span>
<span class="ltx_bibblock"> P. Erdős, Some remarks on the theory of graphs, <em id="bib.bibx3.2" class="ltx_emph ltx_font_italic">Bulletin of the American Mathematical Society</em> <span id="bib.bibx3.3" class="ltx_text ltx_font_bold">53</span> (1947), 292–294. <a href="https://doi.org/10.1090/S0002-9904-1947-08785-1" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://doi.org/10.1090/S0002-9904-1947-08785-1</a>.

</span></li>
      
<li id="bib.bibx4" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[ES]</span>
<span class="ltx_bibblock"> P. Erdős and G. Szekeres, A combinatorial problem in geometry, <em id="bib.bibx4.2" class="ltx_emph ltx_font_italic">Compositio Mathematica</em> <span id="bib.bibx4.3" class="ltx_text ltx_font_bold">2</span> (1935), 463–470. <a href="https://www.numdam.org/item/CM_1935__2__463_0/" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://www.numdam.org/item/CM_1935__2__463_0/</a>.

</span></li>
      
<li id="bib.bibx5" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[GNNW]</span>
<span class="ltx_bibblock"> P. Gupta, Ndiamé Ndiaye, S. Norin, and L. Wei, <em id="bib.bibx5.2" class="ltx_emph ltx_font_italic">Optimizing the CGMS upper bound on Ramsey numbers</em>, arXiv:2407.19026v2, revised 29 August 2026. <a href="https://arxiv.org/abs/2407.19026v2" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://arxiv.org/abs/2407.19026v2</a>.

</span></li>
      
<li id="bib.bibx6" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Ram]</span>
<span class="ltx_bibblock"> F. P. Ramsey, On a problem of formal logic, <em id="bib.bibx6.2" class="ltx_emph ltx_font_italic">Proceedings of the London Mathematical Society</em> (2) <span id="bib.bibx6.3" class="ltx_text ltx_font_bold">30</span> (1930), 264–286. <a href="https://doi.org/10.1112/plms/s2-30.1.264" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://doi.org/10.1112/plms/s2-30.1.264</a>.

</span></li>
      
<li id="bib.bibx7" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Sah]</span>
<span class="ltx_bibblock"> A. Sah, Diagonal Ramsey via effective quasirandomness, <em id="bib.bibx7.2" class="ltx_emph ltx_font_italic">Duke Mathematical Journal</em> <span id="bib.bibx7.3" class="ltx_text ltx_font_bold">172</span> (2023), no. 3, 545–567. <a href="https://doi.org/10.1215/00127094-2022-0048" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://doi.org/10.1215/00127094-2022-0048</a>.

</span></li>
      
<li id="bib.bibx8" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Spe]</span>
<span class="ltx_bibblock"> J. Spencer, Ramsey’s theorem—a new lower bound, <em id="bib.bibx8.2" class="ltx_emph ltx_font_italic">Journal of Combinatorial Theory, Series A</em> <span id="bib.bibx8.3" class="ltx_text ltx_font_bold">18</span> (1975), 108–115. <a href="https://doi.org/10.1016/0097-3165(75)90071-0" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://doi.org/10.1016/0097-3165(75)90071-0</a>.

</span></li>
      
<li id="bib.bibx9" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Tarski]</span>
<span class="ltx_bibblock"> A. Tarski, A lattice-theoretical fixpoint theorem and its applications, <em id="bib.bibx9.2" class="ltx_emph ltx_font_italic">Pacific Journal of Mathematics</em> <span id="bib.bibx9.3" class="ltx_text ltx_font_bold">5</span> (1955), 285–309. <a href="https://msp.org/pjm/1955/5-2/pjm-v5-n2-p11-s.pdf" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://msp.org/pjm/1955/5-2/pjm-v5-n2-p11-s.pdf</a>.

</span></li>
      
<li id="bib.bibx10" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Tho]</span>
<span class="ltx_bibblock"> A. Thomason, An upper bound for some Ramsey numbers, <em id="bib.bibx10.2" class="ltx_emph ltx_font_italic">Journal of Graph Theory</em> <span id="bib.bibx10.3" class="ltx_text ltx_font_bold">12</span> (1988), no. 4, 509–517. <a href="https://doi.org/10.1002/jgt.3190120406" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://doi.org/10.1002/jgt.3190120406</a>.

</span></li>
    
</ul>
</section>
<div class="ltx_pagination ltx_role_newpage"></div>
<section id="A1" class="ltx_appendix">
<h2 class="ltx_title ltx_title_appendix" id="the-finite-host-weighted-inequality"><span class="ltx_tag ltx_tag_appendix">Appendix A </span>The Finite-Host Weighted Inequality</h2>

<div id="A1.p1" class="ltx_para">
<p id="A1.p1.1" class="ltx_p">We prove the estimate used in <a href="#S2.Thmlemma1" title="Lemma 2.1 (Weighted Candidate Bound). ‣ 2.2 The Weighted Candidate Bound ‣ 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>.
Its stopping assumption concerns only proper subsets of the host.
This lets the same estimate prove the source bound by a smallest-counterexample argument in <a href="#A2" title="Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">B</span></a>.</p>
</div>
<div id="A1.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="A1.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma A.1</span></span><span id="A1.Thmlemma1.3" class="ltx_text ltx_font_bold"> </span>(Finite-Host Weighted Candidate Bound)<span id="A1.Thmlemma1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="A1.Thmlemma1.p1" class="ltx_para">
<p id="A1.Thmlemma1.p1.1" class="ltx_p"><span id="A1.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">Fix $w&gt;0$ and parameters in $(0,1)$ satisfying</span></p>
<table id="A1.Ex40" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$x_{0}&lt;\widehat{x},\qquad y_{0}&lt;\widehat{y},\qquad x_{0}&lt;(1-\mu_{0})^{w}p^{1/(1-\mu_{0})}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.Thmlemma1.p1.2" class="ltx_p"><span id="A1.Thmlemma1.p1.2.1" class="ltx_text ltx_font_italic">There is $L_{0}\text{,}$ depending only on these parameters, with the following property, uniformly in $C\geq 1$ and the finite host coloring $H\text{.}$ Fix $\ell\geq L_{0}\text{,}$ and suppose that for every integer $a\geq 1\text{,}$ every proper subset $Z\subsetneq V(H)$ of size</span></p>
<table id="A1.E24" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$|Z|\geq C\widehat{x}^{-a}\widehat{y}^{-\ell}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(24)</span></td></tr></tbody>
</table>
<p id="A1.Thmlemma1.p1.3" class="ltx_p"><span id="A1.Thmlemma1.p1.3.1" class="ltx_text ltx_font_italic">contains a red $K_{a}$ or a blue $K_{\ell}\text{.}$ Then, for all $k,t\geq 1\text{,}$ every candidate in $H$ satisfying</span></p>
<table id="A1.E25" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{R}(X,Y)\geq p,\qquad|X|^{w}|Y|\geq C^{w+1}x_{0}^{-k}y_{0}^{-\ell}\mu_{0}^{-wt}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(25)</span></td></tr></tbody>
</table>
<p id="A1.Thmlemma1.p1.4" class="ltx_p"><span id="A1.Thmlemma1.p1.4.1" class="ltx_text ltx_font_italic">is $(k,\ell,t)$-good.</span></p>
</div>
</div>
<div id="A1.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="A1.p2" class="ltx_para">
<p id="A1.p2.1" class="ltx_p"><span id="A1.p2.1.1" class="ltx_text">We adapt the candidate induction of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx5" title="" class="ltx_ref">GNNW</a>, Lemma 12]</cite> to unequal weights. After removing rows with too few red neighbors, we either pass to a common blue neighborhood or choose a vertex whose red or blue child satisfies the induction hypothesis. A power of the excess red density controls the size loss in these steps.</span></p>
</div>
<div id="A1.p3" class="ltx_para">
<p id="A1.p3.1" class="ltx_p"><span id="A1.p3.1.1" class="ltx_text">Choose a fixed integer $r&gt;\max\{1,w\}$ so large that $p^{1/r}&gt;\mu_{0}$ and</span></p>
<table id="A1.Ex41" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$x_{0}&lt;(p^{1/r}-\mu_{0})^{r}(1-\mu_{0})^{w-r}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p3.2" class="ltx_p"><span id="A1.p3.2.1" class="ltx_text">The logarithm of the right side tends to $w\log(1-\mu_{0})+\log p/(1-\mu_{0})\text{.}$ The function</span></p>
<table id="A1.Ex42" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$x_{0}^{1/r}(1-q)^{1-w/r}+\mu_{0}^{w/r}q^{1-w/r}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p3.3" class="ltx_p"><span id="A1.p3.3.1" class="ltx_text">increases until $q=\mu_{0}/(\mu_{0}+x_{0}^{1/w})&gt;\mu_{0}\text{,}$ and is less than $p^{1/r}$ at $q=\mu_{0}\text{.}$ By continuity choose</span></p>
<table id="A1.Ex43" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$x_{0}&lt;x&lt;\widehat{x},\quad y_{0}&lt;y&lt;\widehat{y},\quad\mu_{0}&lt;\mu&lt;\beta&lt;1,\quad 0&lt;\delta&lt;p/2,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p3.4" class="ltx_p"><span id="A1.p3.4.1" class="ltx_text">and $\gamma&gt;0$ so that, with $\bar{p}=p-\delta\text{,}$</span></p>
<table id="A1.E26" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\max_{0\leq q\leq\beta}\{x^{1/r}(1-q)^{1-w/r}+\mu^{w/r}q^{1-w/r}\}\leq(1-\gamma)\bar{p}^{1/r}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(26)</span></td></tr></tbody>
</table>
<p id="A1.p3.5" class="ltx_p"><span id="A1.p3.5.1" class="ltx_text">All these choices precede $C,H,k,\ell,t\text{.}$</span></p>
</div>
<div id="A1.p4" class="ltx_para">
<p id="A1.p4.1" class="ltx_p"><span id="A1.p4.1.1" class="ltx_text">Put $n=k+t\text{,}$ $\delta_{n}=\delta/n\text{,}$ and induct on $n\text{,}$ for fixed sufficiently large $\ell\text{,}$ using the stronger hypothesis</span></p>
<table id="A1.E27" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{R}(X,Y)\geq p-\delta_{n},\qquad Q_{n}=(d_{R}(X,Y)-p+\delta_{n})^{r}|X|^{w}|Y|\geq C^{w+1}x^{-k}y^{-\ell}\mu^{-wt}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(27)</span></td></tr></tbody>
</table>
<p id="A1.p4.2" class="ltx_p"><span id="A1.p4.2.1" class="ltx_text">After canceling $C^{w+1}\text{,}$ the conditions in <a href="#A1.E25" title="In Lemma A.1 (Finite-Host Weighted Candidate Bound). ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">25</span></a> imply this once $\ell$ is large, uniformly in $k,t\text{,}$ because</span></p>
<table id="A1.Ex44" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(\delta/n)^{r}(x/x_{0})^{k}(y/y_{0})^{\ell}(\mu/\mu_{0})^{wt}\geq 1.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p4.3" class="ltx_p"><span id="A1.p4.3.1" class="ltx_text">The factors involving $k,t$ grow exponentially in $n\text{,}$ so their ratio to $n^{r}$ has a positive infimum; increasing $\ell$ makes the inequality hold. If $k=1$ or $t=1\text{,}$ any vertex of $X$ suffices. Henceforth $k,t\geq 2\text{,}$ and the density excess lies in $(0,1)\text{.}$</span></p>
</div>
<div id="A1.p5" class="ltx_para">
<p id="A1.p5.1" class="ltx_p"><em id="A1.p5.1.1" class="ltx_emph ltx_font_italic">Regularize and stop if $Y$ is large.</em><span id="A1.p5.1.2" class="ltx_text">
Delete rows of red degree less than $(p-\delta_{n})|Y|\text{.}$ The excess edge count $E=e_{R}(X,Y)-(p-\delta_{n})|X||Y|$ increases, and</span></p>
<table id="A1.Ex45" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Q_{n}=E^{r}|X|^{w-r}|Y|^{1-r}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p5.2" class="ltx_p"><span id="A1.p5.2.1" class="ltx_text">does not decrease, since $r&gt;w\text{.}$ Positive excess prevents deletion of the last row. Every nonempty $T\subseteq X$ now has $d_{R}(T,Y)\geq p-\delta_{n}\text{.}$
If $|Y|\geq C\widehat{x}^{-k}\widehat{y}^{-\ell}\text{,}$ apply the stopping assumption with $a=k\text{;}$ $Y$ is proper because $X\neq\varnothing\text{.}$ Otherwise $Q_{n}\leq|X|^{w}|Y|$ implies</span></p>
<table id="A1.E28" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$|X|^{w}&gt;C^{w}(\widehat{x}/x)^{k}(\widehat{y}/y)^{\ell}\mu^{-wt},\qquad|X|\geq C\exp(c(k+\ell+t))$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(28)</span></td></tr></tbody>
</table>
<p id="A1.p5.3" class="ltx_p"><span id="A1.p5.3.1" class="ltx_text">for a fixed $c&gt;0\text{.}$</span></p>
</div>
<div id="A1.p6" class="ltx_para">
<p id="A1.p6.1" class="ltx_p"><em id="A1.p6.1.1" class="ltx_emph ltx_font_italic">Find a common blue neighborhood or a suitable vertex.</em><span id="A1.p6.1.2" class="ltx_text">
Define</span></p>
<table id="A1.Ex46" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$b=\left\lceil\frac{2r\log n+r\log(1/\delta)+w\log 2}{w\log(\beta/\mu)}\right\rceil,\qquad m=\lceil 10\beta^{-1}b^{2}\rceil,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p6.2" class="ltx_p"><span id="A1.p6.2.1" class="ltx_text">and $W=\{v\in X:\deg_{B}(v,X)\geq\beta|X|\}\text{.}$ Put $\xi_{n}=\delta/(2n^{2})\text{.}$
We choose $L_{0}$ once so that</span></p>
<table id="A1.Ex47" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$|X|\geq 5m^{2},\qquad R(k,m)&lt;\bar{p}\xi_{n}|X|,\qquad\frac{2n^{2}}{\delta|X|}&lt;\gamma.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p6.3" class="ltx_p"><span id="A1.p6.3.1" class="ltx_text">To justify a uniform choice, note that $b=O(\log n)\text{,}$ $m=O((\log n)^{2})\text{,}$ and
$R(k,m)\leq\binom{k+m-2}{m-1}\leq k^{m-1}\text{;}$ the last inequality counts nondecreasing tuples in $\{1,\ldots,k\}^{m-1}\text{.}$
The logarithm of each required lower bound on $|X|$ is therefore $O((\log n)^{3})\text{.}$
Subtracting $cn$ leaves a function bounded above in $n\text{,}$ so <a href="#A1.E28" title="In Proof. ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">28</span></a> supplies all three bounds for one $L_{0}\text{,}$ independently of $C\geq 1,k,t\text{.}$
We use the common-neighborhood averaging argument of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx5" title="" class="ltx_ref">GNNW</a>, Lemma 9]</cite>.
When $|W|\geq R(k,m)\text{,}$ either a red $K_{k}$ finishes the proof, or $W$ contains a blue $m$-clique $U\text{.}$ Put $N_{X}=|X|\text{.}$ The blue density $\sigma$ between $U$ and $X\setminus U$ satisfies</span></p>
<table id="A1.Ex48" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sigma\geq\frac{\beta N_{X}-m}{N_{X}-m}=\beta-\frac{(1-\beta)m}{N_{X}-m}\geq\beta-\frac{1}{4m}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p6.4" class="ltx_p"><span id="A1.p6.4.1" class="ltx_text">Choose a uniform $b$-subset of $U\text{,}$ and let $T$ be its common blue neighborhood in $X\setminus U\text{.}$ Convexity of the piecewise-linear extension of $j\mapsto\binom{j}{b}$ on nonnegative integers gives</span></p>
<table id="A1.Ex49" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}|T|\geq(N_{X}-m)\frac{\binom{\lfloor\sigma m\rfloor}{b}}{\binom{m}{b}}\geq(N_{X}-m)(\sigma-b/m)^{b}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p6.5" class="ltx_p"><span id="A1.p6.5.1" class="ltx_text">The second inequality follows factor by factor from the binomial product. Since $m\geq 10\beta^{-1}b^{2}\text{,}$</span></p>
<table id="A1.Ex50" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sigma-b/m\geq\beta\left(1-\frac{1}{8b}\right)&gt;0,\qquad N_{X}-m\geq\frac{4}{5}N_{X}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p6.6" class="ltx_p"><span id="A1.p6.6.1" class="ltx_text">Bernoulli’s inequality gives $\mathbb{E}|T|\geq(7/10)\beta^{b}N_{X}\text{.}$ Thus some blue $b$-clique $S\subseteq U$ has a disjoint common blue neighborhood $T$ with $|T|\geq\beta^{b}|X|/2\text{.}$</span></p>
</div>
<div id="A1.p7" class="ltx_para">
<p id="A1.p7.1" class="ltx_p"><span id="A1.p7.1.1" class="ltx_text">If $b\geq t\text{,}$ then $S$ already contains the required blue clique. For $b&lt;t\text{,}$ we have</span></p>
<table id="A1.Ex51" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\delta_{n-b}-\delta_{n}\geq\delta/n^{2},\qquad Q_{n-b}(T,Y)\geq(\delta/n^{2})^{r}2^{-w}\beta^{wb}|X|^{w}|Y|\geq C^{w+1}x^{-k}y^{-\ell}\mu^{-w(t-b)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p7.2" class="ltx_p"><span id="A1.p7.2.1" class="ltx_text">The last inequality uses $Q_{n}\leq|X|^{w}|Y|$ and $(\beta/\mu)^{wb}\geq 2^{w}(n^{2}/\delta)^{r}\text{,}$ which follows from the choice of $b\text{.}$ Induction applies; a blue $K_{t-b}$ in $T$ joins $S$ to form a blue $K_{t}\text{,}$ and either of the other two outcomes already suffices.</span></p>
</div>
<div id="A1.p8" class="ltx_para">
<p id="A1.p8.1" class="ltx_p"><span id="A1.p8.1.1" class="ltx_text">We may now assume $|W|&lt;R(k,m)&lt;\bar{p}\xi_{n}|X|\text{.}$ Put $Y_{v}=N_{R}(v)\cap Y\text{,}$ $d=d_{R}(X,Y)\text{,}$ and $E_{0}=e_{R}(X,Y)\text{.}$ Row regularization gives $|Y_{v}|\geq\bar{p}|Y|&gt;0$ for every $v\in X\text{.}$ Counting by vertices in $Y$ and applying Cauchy–Schwarz gives</span></p>
<table id="A1.Ex52" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{v\in X}d_{R}(X,Y_{v})|Y_{v}|=\frac{1}{|X|}\sum_{y\in Y}\deg_{R}(y,X)^{2}\geq dE_{0}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p8.2" class="ltx_p"><span id="A1.p8.2.1" class="ltx_text">Removing the terms indexed by $W$ loses at most $|W||Y|\text{,}$ so</span></p>
<table id="A1.Ex53" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{v\notin W}d_{R}(X,Y_{v})|Y_{v}|\geq dE_{0}-|W||Y|&gt;(d-\xi_{n})E_{0}\geq(d-\xi_{n})\sum_{v\notin W}|Y_{v}|.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p8.3" class="ltx_p"><span id="A1.p8.3.1" class="ltx_text">Here $E_{0}\geq\bar{p}|X||Y|$ and $d-\xi_{n}&gt;0\text{.}$ Hence some $v\notin W$ satisfies $d_{R}(X,Y_{v})\geq d-\xi_{n}\text{.}$</span></p>
</div>
<div id="A1.p9" class="ltx_para">
<p id="A1.p9.1" class="ltx_p"><em id="A1.p9.1.1" class="ltx_emph ltx_font_italic">Pass to a red or blue child.</em><span id="A1.p9.1.2" class="ltx_text">
Set $Y^{\prime}=Y_{v}\text{,}$ $X_{R}=N_{R}(v)\cap X\text{,}$ $X_{B}=N_{B}(v)\cap X\text{,}$ and</span></p>
<table id="A1.Ex54" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$a=|X_{R}|/|X|,\quad q=|X_{B}|/|X|,\quad\alpha=d_{R}(X,Y^{\prime})-p+\delta_{n-1}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p9.2" class="ltx_p"><span id="A1.p9.2.1" class="ltx_text">Then $a+q\leq 1\text{,}$ $q\leq\beta\text{,}$ and $\alpha\geq d-p+\delta_{n}+\delta/(2n^{2})&gt;0\text{.}$
For $\chi\in\{R,B\}\text{,}$ set $\alpha_{\chi}=d_{R}(X_{\chi},Y^{\prime})-p+\delta_{n-1}$ when $X_{\chi}\neq\varnothing\text{,}$ and set $\alpha_{\chi}=0$ otherwise. Write $u_{+}=\max\{u,0\}$ and</span></p>
<table id="A1.Ex55" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Q_{\chi}=(\alpha_{\chi})_{+}^{r}|X_{\chi}|^{w}|Y^{\prime}|.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p9.3" class="ltx_p"><span id="A1.p9.3.1" class="ltx_text">Splitting $X$ into its two children and the root gives</span></p>
<table id="A1.E29" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$1\leq a\frac{(\alpha_{R})_{+}}{\alpha}+q\frac{(\alpha_{B})_{+}}{\alpha}+\frac{1}{\alpha|X|}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(29)</span></td></tr></tbody>
</table>
<p id="A1.p9.4" class="ltx_p"><span id="A1.p9.4.1" class="ltx_text">The root’s contribution is $(1-p+\delta_{n-1})/(\alpha|X|)\leq 1/(\alpha|X|)\text{.}$
We claim that</span></p>
<table id="A1.Ex56" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Q_{R}\geq xQ_{n}\qquad\text{or}\qquad Q_{B}\geq\mu^{w}Q_{n}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p9.5" class="ltx_p"><span id="A1.p9.5.1" class="ltx_text">If both inequalities failed, then $Q_{n}\leq\alpha^{r}|X|^{w}|Y|\text{,}$ $|Y^{\prime}|\geq\bar{p}|Y|\text{,}$ and <a href="#A1.E29" title="In Proof. ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">29</span></a> would give</span></p>
<table id="A1.Ex57" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$1\leq\bar{p}^{-1/r}\{x^{1/r}a^{1-w/r}+\mu^{w/r}q^{1-w/r}\}+\frac{1}{\alpha|X|}\leq 1-\gamma+\frac{2n^{2}}{\delta|X|}&lt;1.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A1.p9.6" class="ltx_p"><span id="A1.p9.6.1" class="ltx_text">The second inequality uses $a\leq 1-q$ and <a href="#A1.E26" title="In Proof. ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">26</span></a>; the last is one of our three size bounds.
Thus one child has a positive value of $Q_{n-1}$ meeting <a href="#A1.E27" title="In Proof. ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">27</span></a>, with $k$ reduced by one in the red child or $t$ reduced by one in the blue child. Induction applies. The root extends a red $K_{k-1}$ in $X_{R}\cup Y^{\prime}\text{,}$ or a blue $K_{t-1}$ in $X_{B}\text{,}$ respectively. Every other good outcome already gives a required clique.
∎</span></p>
</div>
</div>
<div id="A1.Thmlemma2" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="A1.Thmlemma2.2" class="ltx_text ltx_font_bold">Corollary A.2</span></span><span id="A1.Thmlemma2.3" class="ltx_text ltx_font_bold"> </span>(Local Density Bound)<span id="A1.Thmlemma2.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="A1.Thmlemma2.p1" class="ltx_para">
<p id="A1.Thmlemma2.p1.1" class="ltx_p"><span id="A1.Thmlemma2.p1.1.1" class="ltx_text ltx_font_italic">Under the stopping assumption of <a href="#A1.Thmlemma1" title="Lemma A.1 (Finite-Host Weighted Candidate Bound). ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">A.1</span></a>, fix $w&gt;0$ and $\mu,p,x,y\in(0,1)$ with
$x&lt;\widehat{x}\text{,}$ $y&lt;\widehat{y}\text{,}$ and $x&lt;(1-\mu)^{w}p^{1/(1-\mu)}\text{.}$
If a host has red density at least $p$ and order</span></p>
<table id="A1.E30" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N\geq Cx^{-k/(w+1)}(y\mu^{w})^{-\ell/(w+1)},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(30)</span></td></tr></tbody>
</table>
<p id="A1.Thmlemma2.p1.2" class="ltx_p"><span id="A1.Thmlemma2.p1.2.1" class="ltx_text ltx_font_italic">then it contains a red $K_{k}$ or a blue $K_{\ell}$ for all sufficiently large $\ell\text{,}$ with a threshold independent of $C\geq 1$ and $k\text{.}$</span></p>
</div>
</div>
<div id="A1.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="A1.p10" class="ltx_para">
<p id="A1.p10.1" class="ltx_p"><span id="A1.p10.1.1" class="ltx_text">Choose $y&lt;y_{1}&lt;\widehat{y}\text{.}$
A uniformly chosen balanced partition has expected cross-density equal to the host density, so some disjoint $X,Y\text{,}$ each of size at least $N/3\text{,}$ satisfy $d_{R}(X,Y)\geq p\text{.}$
For large $\ell\text{,}$ $(y_{1}/y)^{\ell}\geq 3^{w+1}\text{.}$
The order bound therefore supplies <a href="#A1.E25" title="In Lemma A.1 (Finite-Host Weighted Candidate Bound). ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">25</span></a> at $(x,y_{1})$ with $t=\ell\text{,}$ and <a href="#A1.Thmlemma1" title="Lemma A.1 (Finite-Host Weighted Candidate Bound). ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">A.1</span></a> applies.
∎</span></p>
</div>
</div>
</section>
<section id="A2" class="ltx_appendix">
<h2 class="ltx_title ltx_title_appendix" id="admissibility-of-the-source"><span class="ltx_tag ltx_tag_appendix">Appendix B </span>Admissibility of the Source</h2>

<div id="A2.p1" class="ltx_para">
<p id="A2.p1.1" class="ltx_p">We first give a criterion for a concave Ramsey profile, then verify it for the specified function $f\text{.}$
For a continuous $F$ on $[0,1]$ with $F(0)=0\text{,}$ define</p>
<table id="A2.Ex58" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{F}(a,b)=\max(a,b)F\!\left(\frac{\min(a,b)}{\max(a,b)}\right),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<table id="A2.Ex59" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{B}_{F}=\{(x,y)\in(0,1)^{2}:G_{F}(a,b)\leq-a\log x-b\log y\text{ for all }a,b&gt;0\}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.p1.2" class="ltx_p">Thus $\mathcal{B}_{F}$ consists of the exponential bounds that dominate the profile in both coordinates.
For $F=f\text{,}$ this agrees with the source pairs in <a href="#S2" title="2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a>, since $G_{f}(a,b)=b\widehat{f}(a/b)\text{.}$
In the source criterion, $X,Y$ denote scalar support parameters.</p>
</div>
<div id="A2.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="A2.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma B.1</span></span><span id="A2.Thmlemma1.3" class="ltx_text ltx_font_bold"> </span>(Source Criterion)<span id="A2.Thmlemma1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="A2.Thmlemma1.p1" class="ltx_para">
<p id="A2.Thmlemma1.p1.1" class="ltx_p"><span id="A2.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">Suppose $F$ is continuous on $[0,1]\text{,}$ $F(0)=0\text{,}$ is $C^{1}$ and concave on $(0,1]\text{,}$ and has $F^{\prime}&gt;0\text{.}$ If for every $s\in(0,1]$ there are $w&gt;0\text{,}$ $\mu,Y\in(0,1)$ with</span></p>
<table id="A2.Ex60" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p_{0}(s)=1-\mathrm{e}^{-F^{\prime}(s)},\quad X=(1-\mu)^{w}p_{0}(s)^{1/(1-\mu)},\quad(X,Y)\in\mathcal{B}_{F},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.Thmlemma1.p1.2" class="ltx_p"><span id="A2.Thmlemma1.p1.2.1" class="ltx_text ltx_font_italic">and</span></p>
<table id="A2.E31" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(w+1)F(s)+\log X+s\log Y+ws\log\mu&gt;0,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(31)</span></td></tr></tbody>
</table>
<p id="A2.Thmlemma1.p1.3" class="ltx_p"><span id="A2.Thmlemma1.p1.3.1" class="ltx_text ltx_font_italic">then, for every $\varepsilon&gt;0\text{,}$ some $C_{\varepsilon}\geq 1$ satisfies</span></p>
<table id="A2.E32" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R(a,b)\leq\left\lceil C_{\varepsilon}\exp\bigl(G_{F}(a,b)+\varepsilon(a+b)\bigr)\right\rceil\qquad(a,b\in\mathbb{Z}_{\geq 1}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(32)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="A2.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="A2.p2" class="ltx_para">
<p id="A2.p2.1" class="ltx_p"><span id="A2.p2.1.1" class="ltx_text">Fix $\varepsilon&gt;0\text{.}$ We first choose finitely many local bounds, then apply one of them to a smallest counterexample.
Since $F(0)=0$ and $F^{\prime}&gt;0\text{,}$ we have $F\geq 0\text{.}$
Choose $0&lt;\alpha&lt;1$ with $h(\alpha)&lt;\varepsilon/2\text{;}$ the classical bound will handle smaller ratios.
At each $s_{0}\in[\alpha,1]\text{,}$ choose $w,\mu,X,Y$ as in the hypothesis and put $\bar{x}=\mathrm{e}^{-\varepsilon}X\text{,}$ $\bar{y}=\mathrm{e}^{-\varepsilon}Y\text{.}$
Scaling the controls this way and replacing $F(s_{0})$ by $F(s_{0})+\varepsilon(1+s_{0})$ increases the slack by $w\varepsilon(1+s_{0})\text{.}$
We may therefore choose</span></p>
<table id="A2.Ex61" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$0&lt;x&lt;\widehat{x}&lt;\bar{x},\qquad 0&lt;y&lt;\widehat{y}&lt;\bar{y},\qquad 0&lt;p&lt;p_{0}(s_{0}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.p2.2" class="ltx_p"><span id="A2.p2.2.1" class="ltx_text">close enough to $(\bar{x},\bar{y},p_{0}(s_{0}))$ that $x&lt;(1-\mu)^{w}p^{1/(1-\mu)}$ and</span></p>
<table id="A2.Ex62" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$H(t):=-\frac{\log x+t\log(y\mu^{w})}{w+1},\qquad H(s_{0})&lt;F(s_{0})+\varepsilon(1+s_{0}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.p2.3" class="ltx_p"><span id="A2.p2.3.1" class="ltx_text">Continuity gives a neighborhood on which this inequality holds and $p_{0}(s)&gt;p+2\eta_{s_{0}}$ for some $\eta_{s_{0}}&gt;0\text{.}$
A finite subcover gives $\eta&gt;0$ and a common threshold $L\geq 2$ for <a href="#A1.Thmlemma2" title="Corollary A.2 (Local Density Bound). ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">A.2</span></a>, both independent of $C\text{.}$
At every $s\in[\alpha,1]\text{,}$ one selected local bound satisfies $H(s)&lt;F(s)+\varepsilon(1+s)$ and $p_{0}(s)&gt;p+2\eta\text{.}$
Every selected pair also satisfies</span></p>
<table id="A2.E33" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$-a\log\widehat{x}-b\log\widehat{y}\geq G_{F}(a,b)+\varepsilon(a+b)\qquad(a,b&gt;0),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(33)</span></td></tr></tbody>
</table>
<p id="A2.p2.4" class="ltx_p"><span id="A2.p2.4.1" class="ltx_text">by the support condition and the scaling by $\mathrm{e}^{-\varepsilon}\text{.}$</span></p>
</div>
<div id="A2.p3" class="ltx_para">
<p id="A2.p3.1" class="ltx_p"><span id="A2.p3.1.1" class="ltx_text">Choose an integer $K$ with $\alpha K\geq L\text{,}$ and then $C\geq\max\{3,2/\eta,4^{K}\}\text{.}$ Suppose there is a coloring with no required clique at an integer order</span></p>
<table id="A2.Ex63" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N\geq C\exp\bigl(G_{F}(a,b)+\varepsilon(a+b)\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.p3.2" class="ltx_p"><span id="A2.p3.2.1" class="ltx_text">Choose one of smallest order among all parameter pairs and colorings. Interchange the colors if needed and write its targets as $k\geq\ell\text{.}$ The classical bound <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx4" title="" class="ltx_ref">ES</a>]</cite> excludes $k&lt;K\text{.}$ It also excludes $\ell/k\leq\alpha\text{,}$ since</span></p>
<table id="A2.Ex64" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log R(k,\ell)\leq kh(\ell/k)\leq kh(\alpha)&lt;\varepsilon k/2\leq kF(\ell/k)+\varepsilon(k+\ell)+\log C.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.p3.3" class="ltx_p"><span id="A2.p3.3.1" class="ltx_text">Thus $s=\ell/k\in[\alpha,1]$ and $\ell\geq L\text{.}$</span></p>
</div>
<div id="A2.p4" class="ltx_para">
<p id="A2.p4.1" class="ltx_p"><span id="A2.p4.1.1" class="ltx_text">For every integer $a\geq 1\text{,}$ minimality and <a href="#A2.E33" title="In Proof. ‣ Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">33</span></a> give a red $K_{a}$ or a blue $K_{\ell}$ in each proper subset satisfying <a href="#A1.E24" title="In Lemma A.1 (Finite-Host Weighted Candidate Bound). ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">24</span></a>.
Thus the stopping assumption of <a href="#A1.Thmlemma2" title="Corollary A.2 (Local Density Bound). ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">A.2</span></a> holds for the local bound selected at $s\text{.}$
If the host’s red density is at least $p_{0}(s)-\eta&gt;p\text{,}$ then $N&gt;C\mathrm{e}^{kH(s)}\text{,}$ and <a href="#A1.Thmlemma2" title="Corollary A.2 (Local Density Bound). ‣ Appendix A The Finite-Host Weighted Inequality ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">A.2</span></a> gives a required clique.</span></p>
</div>
<div id="A2.p5" class="ltx_para">
<p id="A2.p5.1" class="ltx_p"><span id="A2.p5.1.1" class="ltx_text">Otherwise its blue density exceeds $q=\mathrm{e}^{-F^{\prime}(s)}+\eta&lt;1\text{.}$ A blue neighborhood $Z$ has size at least $q(N-1)&gt;N\mathrm{e}^{-F^{\prime}(s)}\text{,}$ since $N\eta&gt;1\text{.}$ Concavity gives</span></p>
<table id="A2.Ex65" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$k\bigl(F(s)-F(s-1/k)\bigr)\geq F^{\prime}(s).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.p5.2" class="ltx_p"><span id="A2.p5.2.1" class="ltx_text">Consequently</span></p>
<table id="A2.Ex66" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$|Z|&gt;N\mathrm{e}^{-F^{\prime}(s)}\geq\mathrm{e}^{\varepsilon}C\exp\bigl(kF(s-1/k)+\varepsilon(k+\ell-1)\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.p5.3" class="ltx_p"><span id="A2.p5.3.1" class="ltx_text">The proper subset $Z$ therefore has order above the proposed $(k,\ell-1)$ threshold. Minimality gives a red $K_{k}$ or a blue $K_{\ell-1}\text{;}$ in the latter case, add the chosen vertex. Either outcome contradicts the choice of the host.</span></p>
</div>
<div id="A2.p6" class="ltx_para">
<p id="A2.p6.1" class="ltx_p"><span id="A2.p6.1.1" class="ltx_text">Hence <a href="#A2.E32" title="In Lemma B.1 (Source Criterion). ‣ Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">32</span></a> holds. For $1\leq b\leq a\text{,}$ its logarithm is at most $aF(b/a)+2\varepsilon a+\log(2C_{\varepsilon})\text{.}$ Since $\varepsilon$ is arbitrary, the error is uniform in $b\text{.}$
∎</span></p>
</div>
</div>
<section id="A2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-piecewise-cubic-profile"><span class="ltx_tag ltx_tag_subsection">B.1 </span>The Piecewise Cubic Profile</h3>

<div id="A2.SS1.p1" class="ltx_para">
<p id="A2.SS1.p1.1" class="ltx_p">We now verify the criterion for $f$ in <a href="#S2.E3" title="In 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">3</span></a>. The function $P$ has 2,279 rational cubic pieces.
The file <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">data/source.json</span> gives the rational partition points, values, and derivatives of $P\text{.}$ On a cell $[a,b]\text{,}$ set $u=t-a\text{,}$ $\delta=b-a\text{,}$ and $\Delta=P(b)-P(a)\text{.}$ Its exact polynomial is</p>
<table id="A2.Ex67" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$P(a+u)=P(a)+P^{\prime}(a)u+\frac{3\Delta/\delta-2P^{\prime}(a)-P^{\prime}(b)}{\delta}u^{2}+\frac{P^{\prime}(a)+P^{\prime}(b)-2\Delta/\delta}{\delta^{2}}u^{3}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.SS1.p1.2" class="ltx_p">Exact endpoint identities ensure that $P$ is globally $C^{1}\text{.}$ For $t&gt;0$ in the interior of a piece, with $j(t)=t\mathrm{e}^{-t}P(t)\text{,}$</p>
<table id="A2.Ex68" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$j^{\prime\prime}(t)=\mathrm{e}^{-t}\bigl((t-2)P+(2-2t)P^{\prime}+tP^{\prime\prime}\bigr),\qquad f^{\prime\prime}(t)=-\frac{1}{t(1+t)}+j^{\prime\prime}(t).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.SS1.p1.3" class="ltx_p">The cover in <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">data/source_cells.json</span> proves $1-t(1+t)j^{\prime\prime}(t)&gt;0$ on each closed piece, using that piece’s endpoint derivatives, together with $f^{\prime}(1)&gt;0$ and $2f^{\prime}(1)&gt;f(1)\text{.}$
Consequently $f(0)=0\text{,}$ $f$ is continuous on $[0,1]\text{,}$ $C^{1}$ on $(0,1]\text{,}$ strictly concave and increasing.</p>
</div>
<div id="A2.SS1.p2" class="ltx_para">
<p id="A2.SS1.p2.1" class="ltx_p">To describe the boundary of $\mathcal{B}_{f}\text{,}$ put $x_{f}(t)=\mathrm{e}^{-f^{\prime}(t)}$ and $y_{f}(t)=\mathrm{e}^{tf^{\prime}(t)-f(t)}\text{.}$
Their endpoint limits are</p>
<table id="A2.Ex69" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$x_{f}(t)=\frac{t}{1+t}\mathrm{e}^{-j^{\prime}(t)}\longrightarrow 0,\qquad y_{f}(t)=\frac{1}{1+t}\mathrm{e}^{tj^{\prime}(t)-j(t)}\longrightarrow 1.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="A2.SS1.p3" class="ltx_para">
<p id="A2.SS1.p3.1" class="ltx_p">Strict concavity makes $x_{f}$ increasing and $y_{f}$ decreasing.
Also $x_{f}(t)&lt;y_{f}(t)\text{:}$ the function $(1+t)f^{\prime}(t)-f(t)$ decreases to its positive value at $t=1\text{.}$
Writing $x_{1}=x_{f}(1)$ and $y_{1}=y_{f}(1)\text{,}$ the upper boundary is</p>
<table id="A2.E34" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Y_{f}(x)=\begin{cases}y_{f}(t),&amp;0&lt;x&lt;x_{1},\quad x_{f}(t)=x,\\ \mathrm{e}^{-f(1)}/x,&amp;x_{1}\leq x\leq y_{1},\\ x_{f}(t),&amp;y_{1}&lt;x&lt;1,\quad y_{f}(t)=x.\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(34)</span></td></tr></tbody>
</table>
<p id="A2.SS1.p3.2" class="ltx_p">These are the supporting lines of $\widehat{f}$ on its two smooth branches and at its corner.
Thus $b(A)=-\log Y_{f}(\mathrm{e}^{-A})\text{.}$</p>
</div>
</section>
<section id="A2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-source-inequalities"><span class="ltx_tag ltx_tag_subsection">B.2 </span>The Source Inequalities</h3>

<div id="A2.SS2.p1" class="ltx_para">
<p id="A2.SS2.p1.1" class="ltx_p">The file <span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter ltx_ref_self">data/source_cells.json</span> supplies a cover of 12,319 closed cells and rational controls $r,w&gt;0$ on each cell.
Set $\mu=tr\text{,}$ take $X$ as in <a href="#A2.Thmlemma1" title="Lemma B.1 (Source Criterion). ‣ Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">B.1</span></a>, and choose $Y=Y_{f}(X)\text{.}$
With $\Delta_{f}$ denoting the left side of <a href="#A2.E31" title="In Lemma B.1 (Source Criterion). ‣ Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">31</span></a>, the cell inequalities give</p>
<table id="A2.Ex70" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Delta_{f}(t)/t&gt;10^{-8}\qquad(0&lt;t\leq 1).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.SS2.p1.2" class="ltx_p">The cell inequalities also establish $0&lt;\mu,p_{0}&lt;1$ for positive $t\text{.}$ Since <a href="#A2.Thmlemma1" title="Lemma B.1 (Source Criterion). ‣ Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">B.1</span></a> requires controls at each ratio, they may be chosen separately on each cell.</p>
</div>
<div id="A2.SS2.p2" class="ltx_para">
<p id="A2.SS2.p2.1" class="ltx_p">Near zero, we cancel the logarithmic terms before evaluating the slack. Define</p>
<table id="A2.Ex71" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$L_{+}(u)=\frac{\log(1+u)}{u},\qquad L_{-}(u)=\frac{-\log(1-u)}{u},\qquad L_{+}(0)=L_{-}(0)=1,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<table id="A2.Ex72" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$U=(1+t)L_{+}(t)+\mathrm{e}^{-t}P(t),\quad u=\frac{\mathrm{e}^{-j^{\prime}(t)}}{1+t},\quad V=wrL_{-}(tr)+\frac{uL_{-}(tu)}{1-tr},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<table id="A2.Ex73" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$J(s)=L_{+}(s)+s\mathrm{e}^{-s}(P(s)-P^{\prime}(s)).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.SS2.p2.2" class="ltx_p">Then $f(t)/t=-\log t+U$ and $\log X=-tV\text{.}$
On the right supporting branch, write $X=y_{f}(t\sigma)\text{,}$ $Y=x_{f}(t\sigma)\text{.}$
Here $\log Y=\log t+\log\sigma-\log(1+t\sigma)-j^{\prime}(t\sigma)$ and $\log\mu=\log t+\log r\text{.}$
The terms in $\log t$ cancel in the normalized slack, giving</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="A2.EGx1"></span><span class="paper-eq-anchor" id="A2.Ex74"></span><span class="paper-eq-anchor" id="A2.Ex75"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\sigma J(t\sigma) &amp; \displaystyle=V, \\
\displaystyle\Delta_{f}(t)/t &amp; \displaystyle=(w+1)U-V+\log\sigma-\log(1+t\sigma)-j^{\prime}(t\sigma)+w\log r.
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p id="A2.SS2.p2.3" class="ltx_p">As $t\downarrow 0\text{,}$ $X\to 1$ implies $t\sigma\to 0\text{,}$ since $y_{f}$ is strictly decreasing with limit 1 only at zero. Thus $\sigma J(t\sigma)=V$ and $J(0)=1$ give the continuous extension $\sigma(0)=V(0)=wr+\mathrm{e}^{-P(0)}&gt;0\text{.}$ On each cell near zero, the checker verifies the branch, a positive bracket for $\sigma\text{,}$ and $t\sigma\leq 1\text{.}$ The root is unique: $\sigma\mapsto\sigma J(t\sigma)=-\log y_{f}(t\sigma)/t$ is strictly increasing for $t&gt;0\text{,}$ and is the identity at zero.</p>
</div>
<div id="A2.SS2.p3" class="ltx_para">
<p id="A2.SS2.p3.1" class="ltx_p">The verifier evaluates complete finite polynomial expansions. Source inverse brackets are accepted only after outward-rounded endpoint inequalities prove them. When $t$ and $t\sigma(t)$ lie in the interiors of source pieces, possibly different ones,</p>
<table id="A2.Ex76" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sigma^{\prime}=\frac{V^{\prime}-\sigma^{2}J^{\prime}(t\sigma)}{J(t\sigma)+t\sigma J^{\prime}(t\sigma)},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.SS2.p3.2" class="ltx_p">with a checked positive denominator. The integral representations</p>
<table id="A2.Ex77" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$L_{+}(u)=\int_{0}^{1}\frac{da}{1+ua},\qquad L_{-}(u)=\int_{0}^{1}\frac{da}{1-ua}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="A2.SS2.p3.3" class="ltx_p">give endpoint enclosures for these functions and their derivatives, including at zero. Away from zero, the function $u\mapsto\log Y_{f}(\mathrm{e}^{u})\text{,}$ with $u&lt;0\text{,}$ has derivative $-s\text{,}$ $-1\text{,}$ or $-1/s$ on the three branches of <a href="#A2.E34" title="In B.1 The Piecewise Cubic Profile ‣ Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">34</span></a>, where $s$ is the supporting parameter. These derivatives agree at the branch junctions.</p>
</div>
<div id="A2.SS2.p4" class="ltx_para">
<p id="A2.SS2.p4.1" class="ltx_p">Together with <a href="#S6.E22" title="In 6.1 Exact Interval Arithmetic ‣ 6 The Diagonal Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">22</span></a> and <a href="#S6.E23" title="Equation 23 ‣ 6.1 Exact Interval Arithmetic ‣ 6 The Diagonal Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">23</span></a>, these identities enclose each slack and its derivative. An enclosure at the cell center plus the derivative interval times the displacement encloses the slack throughout the cell. When a cell crosses a source partition point, enclosures from every adjoining piece are combined. The continuous compositions are locally Lipschitz, and the stated derivative bounds hold almost everywhere; integrating those bounds justifies the same enclosure across a junction. The complete cover verifies the hypotheses of <a href="#A2.Thmlemma1" title="Lemma B.1 (Source Criterion). ‣ Appendix B Admissibility of the Source ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">B.1</span></a>, which gives <a href="#S2.E4" title="In 2 Source Bounds ‣ Retained-Set Descent for Diagonal Ramsey Numbers" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">4</span></a> with an error uniform in $b\text{.}$</p>
</div>
</section>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Zhipeng Lu and Sichen Wang"></div>
<div class="ltx_rdf" about="" property="dcterms:subject" content="Finite Ramsey proofs, their greatest fixed point, and rigorous upper and lower bounds"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="Retained-Set Descent for Diagonal Ramsey Numbers"></div>

</article>
