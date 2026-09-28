---
title: "On Completion Times under Memoryless Catastrophe"

authors:
  - me
  - Zhipeng Lu

# arXiv v1 submission date.
date: 2026-09-15

publication_types: ["manuscript"]
publication: "*Preprint*, arXiv:2609.16566"
publication_short: "Preprint"

abstract: |
  We study the completion time of a task subject to independent reset (catastrophe) at
  each step. The completion-time PGF depends on the base-process PGF through an affine
  relation, and we exploit this structure systematically. Our main result shows that,
  among age-based catastrophe mechanisms, geometric-tail catastrophe is exactly the
  class that yields uniform affine PGF structure; in continuous time, the
  characterization sharpens to Poisson resetting. We establish a sharp two-sided
  Kolmogorov bound of order $p+|\alpha|$ for the exponential approximation
  $d_K(T/E[T], \mathrm{Exp}(1))$, thereby closing a logarithmic gap. Applications to
  the coupon collector with reset coupons reveal a discontinuous Gumbel-to-Exponential
  transition under resetting, while a multi-phase model exhibits a
  Gaussian-to-exponential transition with exponential convergence rate.

tags:
  - Stochastic Processes
  - Stochastic Resetting
  - Completion Times

featured: false

links:
  - type: pdf
    url: paper.pdf
    label: Paper
  - type: preprint
    provider: arxiv
    id: 2609.16566
    label: arXiv
---

<article class="ltx_document ltx_authors_1line">




<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="introduction"><span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<section id="S1.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="motivation"><span class="ltx_tag ltx_tag_subsection">1.1 </span>Motivation</h3>

<div id="S1.SS1.p1" class="ltx_para">
<p id="S1.SS1.p1.1" class="ltx_p">Stochastic processes subject to catastrophe undergo the total loss of accumulated progress at random intervals, necessitating a complete restart from the initial state. This abstraction of a base task disrupted by total resets arises across several disciplines:</p>
<ul id="S1.I1" class="ltx_itemize">
<li id="S1.I1.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S1.I1.i1.p1" class="ltx_para">
<p id="S1.I1.i1.p1.1" class="ltx_p">Randomized algorithms restarted upon timeout, where <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib29" title="" class="ltx_ref">29</a>]</cite> showed that a universal restart strategy is near-optimal up to a logarithmic factor;</p>
</div></li>
<li id="S1.I1.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S1.I1.i2.p1" class="ltx_para">
<p id="S1.I1.i2.p1.1" class="ltx_p"><em id="S1.I1.i2.p1.1.1" class="ltx_emph ltx_font_italic">Queueing systems</em> flushed by disasters, initiated by the disaster models of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib5" title="" class="ltx_ref">5</a>]</cite> and developed through the negative-customer framework of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib20" title="" class="ltx_ref">20</a>]</cite>;</p>
</div></li>
<li id="S1.I1.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S1.I1.i3.p1" class="ltx_para">
<p id="S1.I1.i3.p1.1" class="ltx_p"><em id="S1.I1.i3.p1.1.1" class="ltx_emph ltx_font_italic">Diffusive search</em> under stochastic resetting, where <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib15" title="" class="ltx_ref">16</a>]</cite> demonstrated that Poisson resetting of a Brownian particle produces a nonequilibrium steady state with finite mean first-passage time—launching a now-extensive literature surveyed in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib16" title="" class="ltx_ref">15</a>]</cite>.</p>
</div></li>
</ul>
</div>
<div id="S1.SS1.p2" class="ltx_para">
<p id="S1.SS1.p2.1" class="ltx_p">For such a process that must complete a task, its completion time, denoted by $T\text{,}$ depends on two ingredients: the base task (how long without catastrophe?) and the catastrophe mechanism (when does reset strike?). Much of the existing literature studies the first ingredient—optimizing restart timing for a given task <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib37" title="" class="ltx_ref">37</a>, <a href="#bib.bib33" title="" class="ltx_ref">33</a>, <a href="#bib.bib8" title="" class="ltx_ref">8</a>]</cite>. We ask a complementary question about the second:</p>
</div>
<div id="S1.SS1.p3" class="ltx_para">
<blockquote id="S1.SS1.p3.1" class="ltx_quote">
<p id="S1.SS1.p3.1.1" class="ltx_p"><em id="S1.SS1.p3.1.1.1" class="ltx_emph ltx_font_italic">What algebraic structure does the catastrophe mechanism impose on the probability generating function of $T\text{,}$ and what are the consequences for moments, limit laws, and convergence rates?</em></p>
</blockquote>
</div>
<div id="S1.SS1.p4" class="ltx_para">
<p id="S1.SS1.p4.1" class="ltx_p">The question has a clear theoretical lineage. The probability generating function (PGF) formula for completion under geometric restart was derived independently by <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib4" title="" class="ltx_ref">4</a>]</cite> and <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib19" title="" class="ltx_ref">19</a>]</cite>. Both observed the striking fact that $E[T]$ depends on the base process only through a single PGF evaluation—Flynn and Pilyugin called this “wonderful.” This is, in retrospect, the $k=1$ shadow of a deeper phenomenon. Meanwhile, in branching process theory, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib1" title="" class="ltx_ref">1</a>]</cite> and <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib38" title="" class="ltx_ref">38</a>]</cite> exploited the fact that geometric compounding inherently produces linear fractional (Möbius) PGFs; in the catastrophe/restart context, this connection has not been made. Our work identifies the algebraic mechanism underlying these observations—<em id="S1.SS1.p4.1.1" class="ltx_emph ltx_font_italic">affine PGF structure</em>—and develops it into a systematic theory: a derivative reduction principle, a characterization theorem, an exponential limit with explicit Laplace expansion, sharp two-sided convergence rates, and a continuous-time counterpart that sharpens the characterization to full Poisson resetting.</p>
</div>
</section>
<section id="S1.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="setup-and-the-pgf-formula"><span class="ltx_tag ltx_tag_subsection">1.2 </span>Setup and the PGF Formula</h3>

<div id="S1.SS2.p1" class="ltx_para">
<p id="S1.SS2.p1.1" class="ltx_p">Throughout, $T_{0}$ is a positive-integer-valued, almost surely finite random variable (the base completion time). Catastrophe occurs independently at each step with probability $q\in(0,1)\text{.}$
For an integer-valued random variable $X\text{,}$ write $G_{X}$ for its probability generating function.
We set</p>
<table id="S1.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$s=1-q,\qquad g=G_{T_{0}},\qquad p=g(s),\qquad D_{k}=g^{(k)}(s).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1.SS2.p1.2" class="ltx_p">We write $\operatorname{Exp}(\lambda)$ for the exponential distribution with rate $\lambda&gt;0$ (density $\lambda e^{-\lambda x}\text{,}$ $x\geq 0\text{;}$ mean $1/\lambda$). In particular, $\operatorname{Exp}(1)$ denotes the standard exponential (mean $1$). The attempt decomposition</p>
<table id="S1.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$T=\sum_{i=1}^{N}A_{i}+B,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1)</span></td></tr></tbody>
</table>
<p id="S1.SS2.p1.3" class="ltx_p">with $N\sim\mathrm{Geom}_{0}(p)$ counting failed attempts, $A_{i}$ i.i.d. failed-attempt lengths, and $B$ the successful-attempt length, is classical (see §<a href="#S2.SS1" title="2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.1</span></a> for a self-contained derivation).
The success probability $p=g(s)\text{,}$ a single PGF evaluation, is the simplest instance of what we call <em id="S1.SS2.p1.3.1" class="ltx_emph ltx_font_italic">proportional single-point sufficiency</em>.</p>
</div>
<div id="S1.SS2.p2" class="ltx_para">
<p id="S1.SS2.p2.1" class="ltx_p">The PGF of $T$ then takes the form (Theorem <a href="#S2.Thmtheorem2" title="Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a>)</p>
<table id="S1.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{T}(w)\;=\;\frac{g(u)(1-u)}{1-w+qw\,g(u)},\qquad u=ws.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(2)</span></td></tr></tbody>
</table>
<p id="S1.SS2.p2.2" class="ltx_p">This formula was obtained independently by <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib19" title="" class="ltx_ref">19</a>]</cite> and <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib4" title="" class="ltx_ref">4</a>]</cite>. Our contribution begins with the observation that (<a href="#S1.E2" title="In 1.2 Setup and the PGF Formula ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) is <em id="S1.SS2.p2.2.1" class="ltx_emph ltx_font_italic">affine in $g(u)$</em>:</p>
<table id="S1.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\underbrace{(1-u)}_{\alpha_{N}(w)}\cdot g(u)+\underbrace{0}_{\beta_{N}(w)}\quad\Big/\quad\underbrace{qw}_{\alpha_{D}(w)}\cdot g(u)+\underbrace{(1-w)}_{\beta_{D}(w)},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3)</span></td></tr></tbody>
</table>
<p id="S1.SS2.p2.3" class="ltx_p">where the argument $u=ws$ is <em id="S1.SS2.p2.3.1" class="ltx_emph ltx_font_italic">linear</em> in $w\text{.}$ Since $\beta_{N}(1)=0=\beta_{D}(1)\text{,}$ the probability axiom $G_{T}(1)=1$ forces</p>
<table id="S1.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{N}(1)=\alpha_{D}(1)=q.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4)</span></td></tr></tbody>
</table>
</div>
<div id="S1.SS2.p3" class="ltx_para">
<p id="S1.SS2.p3.1" class="ltx_p">This coefficient equality is the organizing algebraic mechanism behind the derivative reduction principle and the subsequent approximation theory.</p>
</div>
</section>
<section id="S1.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="main-results"><span class="ltx_tag ltx_tag_subsection">1.3 </span>Main Results</h3>

<div id="S1.SS3.p1" class="ltx_para">
<p id="S1.SS3.p1.1" class="ltx_p">We state our principal results in order: the coefficient equality (<a href="#S1.E4" title="In 1.2 Setup and the PGF Formula ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>) drives the derivative reduction principle (Theorem <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Derivative reduction principle). ‣ 1.3 Main Results ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1.1</span></a>), which in turn underpins the Laplace expansion (Theorem <a href="#S1.Thmtheorem3" title="Theorem 1.3 (Laplace expansion). ‣ 1.3 Main Results ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1.3</span></a>) and the sharp rate (Theorem <a href="#S1.Thmtheorem4" title="Theorem 1.4 (Sharp Kolmogorov bound). ‣ 1.3 Main Results ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1.4</span></a>). The characterization (Theorem <a href="#S1.Thmtheorem2" title="Theorem 1.2 (Characterization). ‣ 1.3 Main Results ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1.2</span></a>) closes the loop by showing that affine structure is not merely sufficient but also <em id="S1.SS3.p1.1.1" class="ltx_emph ltx_font_italic">necessary</em> within the class of age-based catastrophe mechanisms.</p>
</div>
<div id="S1.SS3.p2" class="ltx_para ltx_noindent">
<p id="S1.SS3.p2.1" class="ltx_p"><span id="S1.SS3.p2.1.1" class="ltx_text ltx_font_bold">I. Derivative reduction principle.</span>
The coefficient equality (<a href="#S1.E4" title="In 1.2 Setup and the PGF Formula ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>) propagates through the Leibniz rule to produce an exact cancellation at every moment level.</p>
</div>
<div id="S1.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S1.Thmtheorem1.2" class="ltx_text ltx_font_bold">Theorem 1.1</span></span><span id="S1.Thmtheorem1.3" class="ltx_text ltx_font_bold"> </span>(Derivative reduction principle)<span id="S1.Thmtheorem1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S1.Thmtheorem1.p1" class="ltx_para">
<p id="S1.Thmtheorem1.p1.1" class="ltx_p"><span id="S1.Thmtheorem1.p1.1.1" class="ltx_text ltx_font_italic">Define $\Delta_{k}=N^{(k)}(1)-D^{(k)}(1)\text{,}$ where $N$ and $D$ are the numerator and denominator of (<a href="#S1.E2" title="In 1.2 Setup and the PGF Formula ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>). Then</span></p>
<table id="S1.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Delta_{k}=\begin{cases}1-p,&amp;k=1,\\ -k\,s^{k-1}\,D_{k-1},&amp;k\geq 2.\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1.Thmtheorem1.p1.2" class="ltx_p"><span id="S1.Thmtheorem1.p1.2.1" class="ltx_text ltx_font_italic">In particular, $\Delta_{k}$ does not contain $D_{k}=g^{(k)}(s)\text{.}$ Consequently, the $k$-th factorial moment of $T$ depends on the $(k{-}1)$-jet $\{g(s),g^{\prime}(s),\ldots,g^{(k-1)}(s)\}\text{,}$ never on $g^{(k)}(s)\text{.}$</span></p>
</div>
</div>
<div id="S1.SS3.p3" class="ltx_para">
<p id="S1.SS3.p3.1" class="ltx_p">For details, see Theorem <a href="#S2.Thmtheorem6" title="Theorem 2.6 (Derivative reduction principle). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.6</span></a> and its proof. The theorem reveals a <em id="S1.SS3.p3.1.1" class="ltx_emph ltx_font_italic">strict complexity staircase</em>: each moment level requires exactly one new derivative of the base PGF. For base processes with unbounded support, the staircase is tight—no further reduction is possible (Proposition <a href="#S2.Thmtheorem10" title="Proposition 2.10 (Tightness of the staircase). ‣ 2.3 Moment Recursion and the Complexity Staircase ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.10</span></a>). In the coupon collector application (§<a href="#S6" title="6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>), this staircase is realized by the finite harmonic sums $H^{(k-1)}=\sum_{j=m+1}^{n+m}j^{-(k-1)}\text{,}$ so that the $k$-th moment introduces one new harmonic statistic that cannot be eliminated from the present recursion using lower-order data.</p>
</div>
<div id="S1.SS3.p4" class="ltx_para">
<p id="S1.SS3.p4.1" class="ltx_p">The cancellation rests on affine dependence on $g(u)\text{,}$ a linear shift $u=ws\text{,}$ and coefficient matching at the normalization point; see Lemma <a href="#S2.Thmtheorem7" title="Lemma 2.7 (Affine-ratio recursion). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.7</span></a>. This raises a natural question: is their conjunction <em id="S1.SS3.p4.1.1" class="ltx_emph ltx_font_italic">characteristic</em> of some identifiable class of catastrophe mechanisms?</p>
</div>
<div id="S1.SS3.p5" class="ltx_para ltx_noindent">
<p id="S1.SS3.p5.1" class="ltx_p"><span id="S1.SS3.p5.1.1" class="ltx_text ltx_font_bold">II. Characterization of geometric-tail catastrophe.</span>
The answer is yes. Consider a general age-based catastrophe mechanism with hazard sequence $(h_{t})_{t\geq 1}\text{,}$ $h_{t}\in(0,1)\text{,}$ and survival function $S(t)=\prod_{i=1}^{t}(1-h_{i})\text{.}$ We say the mechanism has <em id="S1.SS3.p5.1.2" class="ltx_emph ltx_font_italic">geometric tail</em> if there exist $a\in(0,1)$ and $q\in(0,1)$ such that $h_{1}=1-a$ and $h_{t}=q$ for all $t\geq 2\text{;}$ equivalently, $S(t)=a\,s^{t-1}$ for $t\geq 1\text{.}$ The special case $a=s$ recovers full memorylessness.</p>
</div>
<div id="S1.Thmtheorem2" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S1.Thmtheorem2.2" class="ltx_text ltx_font_bold">Theorem 1.2</span></span><span id="S1.Thmtheorem2.3" class="ltx_text ltx_font_bold"> </span>(Characterization)<span id="S1.Thmtheorem2.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S1.Thmtheorem2.p1" class="ltx_para">
<p id="S1.Thmtheorem2.p1.1" class="ltx_p"><span id="S1.Thmtheorem2.p1.1.1" class="ltx_text ltx_font_italic">Among age-based catastrophe mechanisms with hazard rates $h_{t}\in(0,1)\text{,}$ the following are equivalent:</span></p>
<ol id="S1.I2" class="ltx_enumerate">
<li id="S1.I2.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(A)</span> 
<div id="S1.I2.i1.p1" class="ltx_para">
<p id="S1.I2.i1.p1.1" class="ltx_p"><span id="S1.I2.i1.p1.1.1" class="ltx_text ltx_font_italic">Geometric-tail catastrophe: </span>$S(t)=a\,s^{t-1}$<span id="S1.I2.i1.p1.1.2" class="ltx_text ltx_font_italic"> for </span>$t\geq 1$<span id="S1.I2.i1.p1.1.3" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
<li id="S1.I2.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(B)</span> 
<div id="S1.I2.i2.p1" class="ltx_para">
<p id="S1.I2.i2.p1.1" class="ltx_p"><span id="S1.I2.i2.p1.1.1" class="ltx_text ltx_font_italic">Uniform affine PGF structure (Definition </span><a href="#S2.Thmtheorem4" title="Definition 2.4 (Uniform affine PGF structure). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref ltx_font_italic"><span class="ltx_text ltx_ref_tag">2.4</span></a><span id="S1.I2.i2.p1.1.2" class="ltx_text ltx_font_italic">).</span></p>
</div></li>
<li id="S1.I2.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(C)</span> 
<div id="S1.I2.i3.p1" class="ltx_para">
<p id="S1.I2.i3.p1.1" class="ltx_p"><span id="S1.I2.i3.p1.1.1" class="ltx_text ltx_font_italic">Derivative reduction: there exists </span>$z_{0}\in(0,1)$<span id="S1.I2.i3.p1.1.2" class="ltx_text ltx_font_italic"> such that for every </span>$k\geq 1$<span id="S1.I2.i3.p1.1.3" class="ltx_text ltx_font_italic"> and every finitely-supported </span>$T_{0}$<span id="S1.I2.i3.p1.1.4" class="ltx_text ltx_font_italic">, the </span>$k$<span id="S1.I2.i3.p1.1.5" class="ltx_text ltx_font_italic">-th factorial moment of </span>$T$<span id="S1.I2.i3.p1.1.6" class="ltx_text ltx_font_italic"> depends on </span>$T_{0}$<span id="S1.I2.i3.p1.1.7" class="ltx_text ltx_font_italic"> only through </span>$\{g^{(j)}(z_{0})\}_{j=0}^{k-1}$<span id="S1.I2.i3.p1.1.8" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
<li id="S1.I2.i4" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(D)</span> 
<div id="S1.I2.i4.p1" class="ltx_para">
<p id="S1.I2.i4.p1.1" class="ltx_p"><span id="S1.I2.i4.p1.1.1" class="ltx_text ltx_font_italic">Proportional single-point sufficiency: </span>$p=\lambda\,g(z_{0})$<span id="S1.I2.i4.p1.1.2" class="ltx_text ltx_font_italic"> for some </span>$z_{0}\in(0,1)$<span id="S1.I2.i4.p1.1.3" class="ltx_text ltx_font_italic">, </span>$\lambda&gt;0$<span id="S1.I2.i4.p1.1.4" class="ltx_text ltx_font_italic">, and all finitely-supported </span>$T_{0}$<span id="S1.I2.i4.p1.1.5" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
<p id="S1.Thmtheorem2.p1.2" class="ltx_p"><span id="S1.Thmtheorem2.p1.2.1" class="ltx_text ltx_font_italic">Full memorylessness ($h_{t}\equiv q$) is further equivalent to $\lambda=1$ (Corollary <a href="#S3.Thmtheorem8" title="Corollary 3.8 (Full memorylessness). ‣ 3.4 From Geometric Tail to Full Memorylessness ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.8</span></a>).</span></p>
</div>
</div>
<div id="S1.SS3.p6" class="ltx_para">
<p id="S1.SS3.p6.1" class="ltx_p">For details, see Theorem <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Characterization). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a>. The hardest implication (C)$\Rightarrow$(A) uses only the $k=1$ case and proceeds by a Möbius rigidity argument (§<a href="#S3.SS3" title="3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.3</span></a>). The gap between geometric-tail and full memorylessness is exactly one degree of freedom—the first-step hazard $h_{1}\text{.}$ In continuous time, this gap closes entirely (Theorem <a href="#S5.Thmtheorem7" title="Theorem 5.7 (Continuous-time characterization). ‣ 5.4 Characterization: Affine Laplace Structure Is Poisson ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.7</span></a>); see <span id="S1.SS3.p6.1.1" class="ltx_text ltx_font_bold">VI</span> below.</p>
</div>
<div id="S1.SS3.p7" class="ltx_para ltx_noindent">
<p id="S1.SS3.p7.1" class="ltx_p"><span id="S1.SS3.p7.1.1" class="ltx_text ltx_font_bold">III. Exponential limit and the Laplace expansion.</span>
The attempt decomposition (<a href="#S1.E1" title="In 1.2 Setup and the PGF Formula ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>) expresses $T$ as a geometric sum plus a perturbation. Rényi’s classical theorem <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib36" title="" class="ltx_ref">36</a>]</cite> asserts that normalized geometric sums converge to the exponential distribution. The coefficient equality (<a href="#S1.E4" title="In 1.2 Setup and the PGF Formula ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>) sharpens this into a quantitative expansion.</p>
</div>
<div id="S1.Thmtheorem3" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S1.Thmtheorem3.2" class="ltx_text ltx_font_bold">Theorem 1.3</span></span><span id="S1.Thmtheorem3.3" class="ltx_text ltx_font_bold"> </span>(Laplace expansion)<span id="S1.Thmtheorem3.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S1.Thmtheorem3.p1" class="ltx_para">
<p id="S1.Thmtheorem3.p1.1" class="ltx_p"><span id="S1.Thmtheorem3.p1.1.1" class="ltx_text ltx_font_italic">Fix $q\in(0,1)\text{.}$ Let $W=T/E[T]$ and define</span></p>
<table id="S1.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha=\frac{s(p-qD_{1})}{1-p},\qquad\beta=\frac{1-qp-qsD_{1}}{1-p}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1.Thmtheorem3.p1.2" class="ltx_p"><span id="S1.Thmtheorem3.p1.2.1" class="ltx_text ltx_font_italic">Then $1+\alpha-\beta=0$ as an algebraic identity. For $p$ sufficiently small and $\theta&gt;0$ satisfying $\theta pq/(1-p)\leq\epsilon_{0}\text{,}$</span></p>
<table id="S1.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[e^{-\theta W}]-\frac{1}{1+\theta}\;=\;\frac{\alpha\,\theta^{2}}{(1+\theta)^{2}}\;+\;O\!\left(\frac{|\alpha|^{2}\,\theta^{3}}{(1+\theta)^{3}}\right)\;+\;O\!\left(\frac{p\,\theta^{2}}{1+\theta}\right),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S1.Thmtheorem3.p1.3" class="ltx_p"><span id="S1.Thmtheorem3.p1.3.1" class="ltx_text ltx_font_italic">with implicit constants depending only on $q\text{.}$ In particular, $T/E[T]\xrightarrow{d}\mathrm{Exp}(1)$ as $p\to 0\text{.}$</span></p>
</div>
</div>
<div id="S1.SS3.p8" class="ltx_para">
<p id="S1.SS3.p8.1" class="ltx_p">See Theorem <a href="#S4.Thmtheorem4" title="Theorem 4.4 (Laplace expansion). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.4</span></a> for details. The identity $1+\alpha-\beta=0$ ensures that the first-order term in $\theta$ vanishes exactly—an algebraic consequence of the coefficient match (<a href="#S1.E4" title="In 1.2 Setup and the PGF Formula ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>), not an asymptotic cancellation. The parameter $\alpha$ measures the deviation of the successful attempt from a geometric target (§<a href="#S4.SS1" title="4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.1</span></a>).</p>
</div>
<div id="S1.SS3.p9" class="ltx_para ltx_noindent">
<p id="S1.SS3.p9.1" class="ltx_p"><span id="S1.SS3.p9.1.1" class="ltx_text ltx_font_bold">IV. Sharp two-sided Kolmogorov bound.</span>
Converting the Laplace expansion to Kolmogorov distance via the smoothing inequality yields $d_{K}=O(|\alpha|\log(1/|\alpha|))$—a logarithmic artifact. The following theorem eliminates this loss.</p>
</div>
<div id="S1.Thmtheorem4" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S1.Thmtheorem4.2" class="ltx_text ltx_font_bold">Theorem 1.4</span></span><span id="S1.Thmtheorem4.3" class="ltx_text ltx_font_bold"> </span>(Sharp Kolmogorov bound)<span id="S1.Thmtheorem4.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S1.Thmtheorem4.p1" class="ltx_para">
<p id="S1.Thmtheorem4.p1.1" class="ltx_p"><span id="S1.Thmtheorem4.p1.1.1" class="ltx_text ltx_font_italic">There exist constants $c_{A},C_{A},\delta_{A}&gt;0$ depending only on $q$ such that, for $p+|\alpha|\leq\delta_{A}\text{,}$</span></p>
<table id="S1.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$c_{A}\,(p+|\alpha|)\;\leq\;d_{K}\!\left(\frac{T}{E[T]},\,\mathrm{Exp}(1)\right)\;\leq\;C_{A}\,(p+|\alpha|).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S1.SS3.p10" class="ltx_para">
<p id="S1.SS3.p10.1" class="ltx_p">See Theorem <a href="#S4.Thmtheorem15" title="Theorem 4.15 (Two-sided bound). ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.15</span></a> for details. The template $p+|\alpha|$ reflects two independent error sources: a <em id="S1.SS3.p10.1.1" class="ltx_emph ltx_font_italic">lattice error</em> $\Theta(p)$ from the integrality of the attempt count, and a <em id="S1.SS3.p10.1.2" class="ltx_emph ltx_font_italic">perturbation error</em> $\Theta(|\alpha|)$ from the successful attempt’s length mismatch. The $p$-term is irreducible, as shown by Proposition <a href="#S4.Thmtheorem16" title="Proposition 4.16 (Counterexample: 𝑝 cannot be dropped). ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.16</span></a>; the
$|\alpha|$-term is forced by the Laplace-transform lower bound and is dominant in the CCP regime. The upper bound rests on a Bridge Theorem (Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a>) that decomposes the approximation via Brown’s quantitative Rényi theorem (<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib6" title="" class="ltx_ref">6</a>]</cite>); the lower bound combines a lattice argument with evaluation of the Laplace expansion.</p>
</div>
<div id="S1.SS3.p11" class="ltx_para ltx_noindent">
<p id="S1.SS3.p11.1" class="ltx_p"><span id="S1.SS3.p11.1.1" class="ltx_text ltx_font_bold">V. CCP specialization and phase transition.</span>
We instantiate the theory to the coupon collector problem with $m$ reset coupons among $n+m$ types (§<a href="#S6" title="6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>). The specialization yields:</p>
<ul id="S1.I3" class="ltx_itemize">
<li id="S1.I3.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S1.I3.i1.p1" class="ltx_para">
<p id="S1.I3.i1.p1.1" class="ltx_p">Closed-form expressions for $E[T]$ and $\operatorname{Var}(T)\text{,}$ together with an explicit harmonic realization of the DRP staircase for higher moments (§<a href="#S6.SS3" title="6.3 Moments ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.3</span></a>);</p>
</div></li>
<li id="S1.I3.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S1.I3.i2.p1" class="ltx_para">
<p id="S1.I3.i2.p1.1" class="ltx_p">The CCP-specific bound $d_{K}\in[1-o(1),\,2+o(1)]\cdot|\alpha|$ with $|\alpha|\sim m!\,m\ln n/n^{m}$ (Theorem <a href="#S6.Thmtheorem4" title="Theorem 6.4 (CCP sharp bound). ‣ 6.4 Phase Transition and Sharp Kolmogorov Bound ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.4</span></a>), closing the logarithmic gap left by the smoothing approach;</p>
</div></li>
<li id="S1.I3.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S1.I3.i3.p1" class="ltx_para">
<p id="S1.I3.i3.p1.1" class="ltx_p">A <em id="S1.I3.i3.p1.1.1" class="ltx_emph ltx_font_italic">discontinuous Gumbel-to-Exponential phase transition</em> at $m=0\to m\geq 1\text{:}$ one reset coupon suffices to replace extreme-value waiting ($(T_{0}-n\ln n)/n\xrightarrow{d}\text{Gumbel}$) by geometric waiting ($T/E[T]\to$ Exponential).</p>
</div></li>
</ul>
</div>
<div id="S1.SS3.p12" class="ltx_para ltx_noindent">
<p id="S1.SS3.p12.1" class="ltx_p"><span id="S1.SS3.p12.1.1" class="ltx_text ltx_font_bold">VI. Continuous-time sharpening.</span>
Replacing PGFs by Laplace transforms and the multiplicative shift $u=ws$ by an additive shift $\sigma=\lambda+r\text{,}$ the entire discrete theory carries over to continuous time (§<a href="#S5" title="5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5</span></a>), with one qualitative sharpening and one quantitative simplification.</p>
</div>
<div id="S1.SS3.p13" class="ltx_para">
<p id="S1.SS3.p13.1" class="ltx_p">The <em id="S1.SS3.p13.1.1" class="ltx_emph ltx_font_italic">sharpening</em>: the geometric-tail gap of Theorem <a href="#S1.Thmtheorem2" title="Theorem 1.2 (Characterization). ‣ 1.3 Main Results ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1.2</span></a> closes. Among continuous-time age-based catastrophe mechanisms, affine Laplace structure characterizes <em id="S1.SS3.p13.1.2" class="ltx_emph ltx_font_italic">full</em> Poisson resetting—constant hazard everywhere, with no residual first-step degree of freedom (Theorem <a href="#S5.Thmtheorem7" title="Theorem 5.7 (Continuous-time characterization). ‣ 5.4 Characterization: Affine Laplace Structure Is Poisson ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.7</span></a>). The mechanism is twofold: point masses $T_{0}=\delta_{x}$ with continuous $x$ determine the function $\psi$ on all of $(0,1)\text{,}$ and the relation $F=\rho\,S+c$ is <em id="S1.SS3.p13.1.3" class="ltx_emph ltx_font_italic">differentiated</em> rather than <em id="S1.SS3.p13.1.4" class="ltx_emph ltx_font_italic">differenced</em>, constraining the hazard rate at every point.</p>
</div>
<div id="S1.SS3.p14" class="ltx_para">
<p id="S1.SS3.p14.1" class="ltx_p">The <em id="S1.SS3.p14.1.1" class="ltx_emph ltx_font_italic">simplification</em> is conditional rather than unconditional: In continuous time, the lattice error disappears. In the regime $|\alpha|\gg p\text{,}$ the sharp template reduces to $|\alpha|\text{;}$ when $\alpha$ is small, a residual $O(p)$ term may remain. In the Brownian first-passage model of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib15" title="" class="ltx_ref">16</a>]</cite>, this yields $d_{\mathrm{K}}\!\left(\frac{T}{E[T]},\,\operatorname{Exp}(1)\right)\in[1-o(1),\,2+o(1)]\cdot|\alpha|$ (§<a href="#S5.SS6" title="5.6 Worked Example: Brownian First Passage ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.6</span></a>).</p>
</div>
</section>
<section id="S1.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="architecture-of-the-paper"><span class="ltx_tag ltx_tag_subsection">1.4 </span>Architecture of the Paper</h3>

<div id="S1.SS4.p1" class="ltx_para">
<p id="S1.SS4.p1.1" class="ltx_p">The paper is organized as follows. §<a href="#S2" title="2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a> derives the PGF formula, identifies the affine structure, and establishes the coefficient equality. §<a href="#S2.SS2" title="2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a> proves the derivative reduction principle and the moment recursion. §<a href="#S3" title="3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a> establishes the characterization theorem via a Möbius rigidity argument. §<a href="#S4" title="4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a> develops the exponential approximation: the Laplace expansion, the Bridge Theorem, and the sharp two-sided Kolmogorov bound $d_{K}\asymp p+|\alpha|\text{,}$ including a counterexample showing that neither term is redundant. §<a href="#S5" title="5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5</span></a> presents the continuous-time counterpart—replacing PGFs by Laplace transforms and the multiplicative shift by an additive one—and shows that the geometric-tail gap closes: affine Laplace structure characterizes full Poisson resetting. §<a href="#S6" title="6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a> and §<a href="#S7" title="7 Application: Multi-Phase Task with Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a> instantiate the theory to two structurally contrasting applications: the coupon collector with reset coupons, which produces a harmonic moment staircase and a Gumbel-to-Exponential phase transition, and a multi-phase task under catastrophe, which produces an algebraic staircase and a Gaussian-to-exponential transition with exponentially fast convergence. §<a href="#S8" title="8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8</span></a> discusses related work, and §<a href="#S9" title="9 Further Directions ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a> outlines further directions.</p>
</div>
</section>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="completion-time-under-memoryless-catastrophe"><span class="ltx_tag ltx_tag_section">2 </span>Completion Time under Memoryless Catastrophe</h2>

<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="model-and-pgf-formula"><span class="ltx_tag ltx_tag_subsection">2.1 </span>Model and PGF Formula</h3>

<div id="S2.SS1.p1" class="ltx_para">
<p id="S2.SS1.p1.1" class="ltx_p">Let $T_{0}$ be a positive-integer-valued, almost surely finite random variable, called the <em id="S2.SS1.p1.1.1" class="ltx_emph ltx_font_italic">base completion time</em>, with $\pi_{j}=P(T_{0}=j)$ for $j\geq 1$ and PGF $g(z)=G_{T_{0}}(z)=\sum_{k\geq 0}P(T_{0}=k)\,z^{k}$ for $|z|\leq 1\text{.}$</p>
</div>
<div id="S2.Thmtheorem1" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem1.2" class="ltx_text ltx_font_bold">Definition 2.1</span></span><span id="S2.Thmtheorem1.3" class="ltx_text ltx_font_bold"> </span>(Memoryless catastrophe)<span id="S2.Thmtheorem1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem1.p1" class="ltx_para">
<p id="S2.Thmtheorem1.p1.1" class="ltx_p">Fix $q\in(0,1)$ and set $s=1-q\text{.}$ At each step, independently of everything else, a catastrophe occurs with probability $q\text{.}$ If the process survives (probability $s$), the base task may advance; if a catastrophe occurs and the base task has not yet completed, all accumulated progress is destroyed and the process restarts from scratch. The process terminates at the first step where it survives the catastrophe and the base task completes.</p>
</div>
</div>
<div id="S2.SS1.p2" class="ltx_para">
<p id="S2.SS1.p2.1" class="ltx_p">A maximal run of steps uninterrupted by catastrophe is called an <em id="S2.SS1.p2.1.1" class="ltx_emph ltx_font_italic">attempt</em>. Each attempt begins from the empty state and either <em id="S2.SS1.p2.1.2" class="ltx_emph ltx_font_italic">succeeds</em> (the base task completes) or <em id="S2.SS1.p2.1.3" class="ltx_emph ltx_font_italic">fails</em> (terminated by catastrophe). Since the base task completes at step $t$ with no prior catastrophe with probability $s^{t}\,\pi_{t}$ (independence), the success probability is</p>
<table id="S2.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p\;=\;\sum_{t\geq 1}s^{t}\,\pi_{t}\;=\;g(s)\;\in\;(0,1).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5)</span></td></tr></tbody>
</table>
<p id="S2.SS1.p2.2" class="ltx_p">Successive attempts are independent (each restarts from the empty state), so the number of failed attempts before the first success is $N\sim\mathrm{Geom}_{0}(p)\text{.}$<span id="footnote1" class="ltx_note ltx_role_footnote"><sup class="ltx_note_mark">1</sup><span class="ltx_note_outer"><span class="ltx_note_content"><sup class="ltx_note_mark">1</sup>
              <span class="ltx_tag ltx_tag_note">1</span>
              
              
              
            We write $\mathrm{Geom}_{0}(p)$ for the distribution on $\{0,1,2,\ldots\}$ with $P(N=k)=(1-p)^{k}p$ (failure count), and $\mathrm{Geom}_{1}(p)=\mathrm{Geom}_{0}(p)+1$ for the trial count.</span></span></span></p>
</div>
<div id="S2.SS1.p3" class="ltx_para">
<p id="S2.SS1.p3.1" class="ltx_p">Denote by $A$ the length of a generic failed attempt, by $B$ the length of the successful attempt, and let $A_{1},A_{2},\ldots$ be i.i.d. copies of $A\text{.}$ The total completion time decomposes as</p>
<table id="S2.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$T\;=\;\sum_{i=1}^{N}A_{i}\;+\;B,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(6)</span></td></tr></tbody>
</table>
<p id="S2.SS1.p3.2" class="ltx_p">where $N\text{,}$ $(A_{i})_{i\geq 1}\text{,}$ and $B$ are mutually independent. Standard conditioning (Bayes’ rule on the success/failure event) yields the PGFs</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S2.EGx1"></span><span class="paper-eq-anchor" id="S2.E7"></span><span class="paper-eq-anchor" id="S2.E8"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle G_{B}(w) &amp; \displaystyle=\frac{g(ws)}{p}, \\[4pt]
\displaystyle G_{A}(w) &amp; \displaystyle=\frac{qw\bigl(1-g(ws)\bigr)}{(1-p)(1-ws)},
\end{aligned}$$</div><div class="paper-eqgroup-no paper-eqgroup-no-rows"><span class="paper-eqgroup-number">(7)</span><span class="paper-eqgroup-number">(8)</span></div></div>

<p id="S2.SS1.p3.3" class="ltx_p">where (<a href="#S2.E8" title="In 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8</span></a>) uses the identity $\sum_{j\geq 0}z^{j}P(T_{0}&gt;j)=(1-g(z))/(1-z)\text{.}$ Combining these with the geometric-sum PGF $E[G_{A}(w)^{N}]=p/(1-(1-p)G_{A}(w))$ gives the following.</p>
</div>
<div id="S2.Thmtheorem2" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem2.2" class="ltx_text ltx_font_bold">Theorem 2.2</span></span><span id="S2.Thmtheorem2.3" class="ltx_text ltx_font_bold"> </span>(PGF formula)<span id="S2.Thmtheorem2.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem2.p1" class="ltx_para">
<p id="S2.Thmtheorem2.p1.1" class="ltx_p"><span id="S2.Thmtheorem2.p1.1.1" class="ltx_text ltx_font_italic">Under memoryless catastrophe with rate $q\text{,}$ the PGF of the completion time is</span></p>
<table id="S2.E9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{T}(w)\;=\;\frac{g(u)(1-u)}{1-w+qw\,g(u)},\qquad u=ws.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(9)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S2.SS1.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS1.p4" class="ltx_para">
<p id="S2.SS1.p4.1" class="ltx_p"><span id="S2.SS1.p4.1.1" class="ltx_text">By (<a href="#S2.E6" title="In 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>) and mutual independence, $G_{T}=G_{B}\cdot E[G_{A}^{N}]\text{.}$ Substituting (<a href="#S2.E7" title="In 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a>) and (<a href="#S2.E8" title="In 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8</span></a>):</span></p>
<table id="S2.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{T}(w)=\frac{g(u)}{p}\cdot\frac{p}{1-\dfrac{qw(1-g(u))}{1-u}}=\frac{g(u)(1-u)}{(1-u)-qw(1-g(u))}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.SS1.p4.2" class="ltx_p"><span id="S2.SS1.p4.2.1" class="ltx_text">The denominator simplifies: $(1-ws)-qw+qw\,g(u)=1-w(s+q)+qw\,g(u)=1-w+qw\,g(u)\text{,}$ using $s+q=1\text{.}$
∎</span></p>
</div>
</div>
<div id="S2.Thmtheorem3" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem3.2" class="ltx_text ltx_font_bold">Corollary 2.3</span></span><span id="S2.Thmtheorem3.3" class="ltx_text ltx_font_bold"> </span>(Expected completion time)<span id="S2.Thmtheorem3.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem3.p1" class="ltx_para">
<p id="S2.Thmtheorem3.p1.1" class="ltx_p">$\displaystyle E[T]=\frac{1-p}{qp}$<span id="S2.Thmtheorem3.p1.1.1" class="ltx_text ltx_font_italic">.</span></p>
</div>
</div>
<div id="S2.SS1.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS1.p5" class="ltx_para">
<p id="S2.SS1.p5.1" class="ltx_p"><span id="S2.SS1.p5.1.1" class="ltx_text">Differentiating (<a href="#S2.E9" title="In Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a>): $G_{T}(w)-1=(1-w)(g(u)-1)/(1-w+qwg(u))$ (using $1-u-qw=1-w$), so $E[T]=\lim_{w\to 1}(G_{T}(w)-1)/(w-1)=(1-p)/(qp)\text{.}$
∎</span></p>
</div>
</div>
</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="affine-structure-and-the-derivative-reduction-principle"><span class="ltx_tag ltx_tag_subsection">2.2 </span>Affine Structure and the Derivative Reduction Principle</h3>

<div id="S2.SS2.p1" class="ltx_para">
<p id="S2.SS2.p1.1" class="ltx_p">We now identify the structural property of (<a href="#S2.E9" title="In Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a>) that drives all subsequent results.</p>
</div>
<div id="S2.Thmtheorem4" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem4.2" class="ltx_text ltx_font_bold">Definition 2.4</span></span><span id="S2.Thmtheorem4.3" class="ltx_text ltx_font_bold"> </span>(Uniform affine PGF structure)<span id="S2.Thmtheorem4.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem4.p1" class="ltx_para">
<p id="S2.Thmtheorem4.p1.1" class="ltx_p">A catastrophe mechanism has uniform affine PGF structure if there exist functions
$a(w),b(w),c(w),d(w)\text{,}$ analytic in a neighborhood of $w=1\text{,}$ depending only on the mechanism
(not on the base process $T_{0}$), and a linear function $u(w)$ with $u(1)\in(0,1)\text{,}$ such that for all base processes $T_{0}\text{,}$</p>
<table id="S2.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{T}(w)=\frac{a(w)\,g(u(w))+b(w)}{c(w)\,g(u(w))+d(w)},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.Thmtheorem4.p1.2" class="ltx_p">with $a$ and $c$ not identically zero, and the non-degeneracy condition $c(1)\,g(u(1))+d(1)\neq 0$ for all admissible $g\text{.}$<span id="footnote2" class="ltx_note ltx_role_footnote"><sup class="ltx_note_mark">2</sup><span class="ltx_note_outer"><span class="ltx_note_content"><sup class="ltx_note_mark">2</sup>
                <span class="ltx_tag ltx_tag_note">2</span>
                
                
                
              Non-degeneracy excludes pathological representations obtained by multiplying numerator and denominator by a factor vanishing at $w=1\text{,}$ which would create a $0/0$ indeterminacy and invalidate the coefficient-matching argument.</span></span></span></p>
</div>
</div>
<div id="S2.Thmtheorem5" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem5.2" class="ltx_text ltx_font_bold">Proposition 2.5</span></span><span id="S2.Thmtheorem5.3" class="ltx_text ltx_font_bold"> </span>(Affine structure and coefficient equality)<span id="S2.Thmtheorem5.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem5.p1" class="ltx_para">
<p id="S2.Thmtheorem5.p1.1" class="ltx_p"><span id="S2.Thmtheorem5.p1.1.1" class="ltx_text ltx_font_italic">The PGF formula (<a href="#S2.E9" title="In Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a>) exhibits uniform affine structure with</span></p>
<table id="S2.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$a(w)=1-u,\quad b(w)=0,\quad c(w)=qw,\quad d(w)=1-w,\quad u(w)=ws.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.Thmtheorem5.p1.2" class="ltx_p"><span id="S2.Thmtheorem5.p1.2.1" class="ltx_text ltx_font_italic">Writing $N(w)=a(w)\,g(u)+b(w)$ and $D(w)=c(w)\,g(u)+d(w)$ for the numerator and denominator, the normalization $G_{T}(1)=1$ forces</span></p>
<table id="S2.E10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{N}(1)\;:=\;a(1)\;=\;q\;=\;c(1)\;=:\;\alpha_{D}(1).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(10)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S2.SS2.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS2.p2" class="ltx_para">
<p id="S2.SS2.p2.1" class="ltx_p"><span id="S2.SS2.p2.1.1" class="ltx_text">Immediate from (<a href="#S2.E9" title="In Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a>): at $w=1\text{,}$ $b(1)=0=d(1)\text{,}$ so $G_{T}(1)=1$ gives $a(1)\,g(s)=c(1)\,g(s)$ and $a(1)=c(1)$ (since $g(s)=p&gt;0$); since $a(1)=1-s=q\text{,}$ the result follows.
∎</span></p>
</div>
</div>
<div id="S2.SS2.p3" class="ltx_para">
<p id="S2.SS2.p3.1" class="ltx_p">The coefficient equality (<a href="#S2.E10" title="In Proposition 2.5 (Affine structure and coefficient equality). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">10</span></a>) is a direct consequence of the probability axiom $G_{T}(1)=1$ applied to the affine form. Together with the linearity of $u(w)=ws$ and the affine dependence on $g(u)\text{,}$ it produces an exact derivative cancellation at every moment level.</p>
</div>
<div id="S2.SS2.p4" class="ltx_para">
<p id="S2.SS2.p4.1" class="ltx_p">The PGF formula expresses $G_{T}(w)=N(w)/D(w)\text{,}$ where</p>
<table id="S2.E11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N(w)=(1-u)\,g(u),\qquad D(w)=(1-w)+qw\,g(u),\qquad u=ws.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(11)</span></td></tr></tbody>
</table>
<p id="S2.SS2.p4.2" class="ltx_p">The $k$-th factorial moment is $\eta_{k}=G_{T}^{(k)}(1)\text{.}$ Since $u=ws$ is linear, $\frac{d^{j}}{dw^{j}}g(ws)=s^{j}g^{(j)}(ws)$ with no Faà di Bruno corrections. Writing $D_{j}=g^{(j)}(s)\text{,}$ one might expect $\eta_{k}$ to depend on the full $k$-jet $\{D_{0},\ldots,D_{k}\}\text{.}$ The following theorem shows that $D_{k}$ cancels exactly.</p>
</div>
<div id="S2.Thmtheorem6" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem6.2" class="ltx_text ltx_font_bold">Theorem 2.6</span></span><span id="S2.Thmtheorem6.3" class="ltx_text ltx_font_bold"> </span>(Derivative reduction principle)<span id="S2.Thmtheorem6.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem6.p1" class="ltx_para">
<p id="S2.Thmtheorem6.p1.1" class="ltx_p"><span id="S2.Thmtheorem6.p1.1.1" class="ltx_text ltx_font_italic">Define $\Delta_{k}=N^{(k)}(1)-D^{(k)}(1)$ for $k\geq 1\text{.}$ Then</span></p>
<table id="S2.E12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Delta_{k}=\begin{cases}1-p,&amp;k=1,\\[3.0pt] -k\,s^{k-1}\,D_{k-1},&amp;k\geq 2.\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(12)</span></td></tr></tbody>
</table>
<p id="S2.Thmtheorem6.p1.2" class="ltx_p"><span id="S2.Thmtheorem6.p1.2.1" class="ltx_text ltx_font_italic">In particular, $\Delta_{k}$ does not contain $D_{k}=g^{(k)}(s)\text{.}$</span></p>
</div>
</div>
<div id="S2.SS2.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS2.p5" class="ltx_para">
<p id="S2.SS2.p5.1" class="ltx_p"><span id="S2.SS2.p5.1.1" class="ltx_text">We compute $N^{(k)}(1)$ and $D^{(k)}(1)$ separately via the Leibniz rule, then subtract.</span></p>
</div>
<div id="S2.SS2.p6" class="ltx_para ltx_noindent">
<p id="S2.SS2.p6.1" class="ltx_p"><em id="S2.SS2.p6.1.1" class="ltx_emph ltx_font_italic">Case $k\geq 2\text{.}$</em> 
Write $N(w)=f_{1}(w)\cdot g(ws)$ with $f_{1}(w)=1-ws\text{.}$ Since $f_{1}(1)=q\text{,}$ $f_{1}^{\prime}(w)=-s\text{,}$ and $f_{1}^{(j)}=0$ for $j\geq 2\text{,}$ the Leibniz rule gives</p>
<table id="S2.E13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N^{(k)}(1)=q\,s^{k}D_{k}-k\,s^{k}D_{k-1}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(13)</span></td></tr></tbody>
</table>
<p id="S2.SS2.p6.2" class="ltx_p">Similarly, $D(w)=(1-w)+f_{2}(w)\cdot g(ws)$ with $f_{2}(w)=qw\text{.}$ For $k\geq 2\text{,}$ $\frac{d^{k}}{dw^{k}}(1-w)=0\text{.}$ Since $f_{2}(1)=q\text{,}$ $f_{2}^{\prime}(w)=q\text{,}$ and $f_{2}^{(j)}=0$ for $j\geq 2\text{:}$</p>
<table id="S2.E14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D^{(k)}(1)=q\,s^{k}D_{k}+k\,q\,s^{k-1}D_{k-1}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(14)</span></td></tr></tbody>
</table>
<p id="S2.SS2.p6.3" class="ltx_p">Subtracting (<a href="#S2.E14" title="In Proof. ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">14</span></a>) from (<a href="#S2.E13" title="In Proof. ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">13</span></a>):</p>
<table id="S2.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Delta_{k}=\underbrace{(q\,s^{k}-q\,s^{k})}_{=0}\,D_{k}+\bigl(-k\,s^{k}-k\,q\,s^{k-1}\bigr)\,D_{k-1}=-k\,s^{k-1}(s+q)\,D_{k-1}=-k\,s^{k-1}D_{k-1},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.SS2.p6.4" class="ltx_p">where the last step uses $s+q=1\text{.}$ The $D_{k}$-terms cancel because they enter $N^{(k)}(1)$ and $D^{(k)}(1)$ with the same coefficient $q\,s^{k}$—precisely the coefficient equality (<a href="#S2.E10" title="In Proposition 2.5 (Affine structure and coefficient equality). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">10</span></a>).</p>
</div>
<div id="S2.SS2.p7" class="ltx_para ltx_noindent">
<p id="S2.SS2.p7.1" class="ltx_p"><em id="S2.SS2.p7.1.1" class="ltx_emph ltx_font_italic">Case $k=1\text{.}$</em> 
Direct computation: $N^{\prime}(1)=-sp+qsD_{1}\text{,}$ $D^{\prime}(1)=-1+qp+qsD_{1}\text{.}$ Hence</p>
<table id="S2.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Delta_{1}=(-sp+qsD_{1})-(-1+qp+qsD_{1})=1-p(s+q)=1-p.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S2.SS2.p8" class="ltx_para">
<p id="S2.SS2.p8.1" class="ltx_p">The next lemma extracts the cancellation mechanism behind Theorem <a href="#S2.Thmtheorem6" title="Theorem 2.6 (Derivative reduction principle). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.6</span></a>.</p>
</div>
<div id="S2.Thmtheorem7" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem7.2" class="ltx_text ltx_font_bold">Lemma 2.7</span></span><span id="S2.Thmtheorem7.3" class="ltx_text ltx_font_bold"> </span>(Affine-ratio recursion)<span id="S2.Thmtheorem7.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem7.p1" class="ltx_para">
<p id="S2.Thmtheorem7.p1.1" class="ltx_p"><span id="S2.Thmtheorem7.p1.1.1" class="ltx_text ltx_font_italic">Let</span></p>
<table id="S2.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R(z)=\frac{a(z)h(u(z))+b(z)}{c(z)h(u(z))+d(z)},\qquad u(z)=u_{0}+\kappa(z-z_{*}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.Thmtheorem7.p1.2" class="ltx_p"><span id="S2.Thmtheorem7.p1.2.1" class="ltx_text ltx_font_italic">where $a,b,c,d$ are $C^{\infty}$ near $z_{*}\text{,}$ and $a(z_{*})=c(z_{*}),b(z_{*})=d(z_{*}),D(z_{*}):=c(z_{*})h(u_{0})+d(z_{*})\neq 0\text{.}$
Set</span></p>
<table id="S2.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N(z)=a(z)h(u(z))+b(z),\qquad D(z)=c(z)h(u(z))+d(z).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.Thmtheorem7.p1.3" class="ltx_p"><span id="S2.Thmtheorem7.p1.3.1" class="ltx_text ltx_font_italic">Then, for every $k\geq 1\text{,}$ $\Delta_{k}:=N^{(k)}(z_{*})-D^{(k)}(z_{*})$ depends only on $h(u_{0}),h^{\prime}(u_{0}),\dots,h^{(k-1)}(u_{0})\text{,}$ and</span></p>
<table id="S2.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$R^{(k)}(z_{*})=\frac{1}{D(z_{*})}\left(\Delta_{k}-\sum_{j=1}^{k-1}\binom{k}{j}D^{(j)}(z_{*})R^{(k-j)}(z_{*})\right).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.Thmtheorem7.p1.4" class="ltx_p"><span id="S2.Thmtheorem7.p1.4.1" class="ltx_text ltx_font_italic">Consequently, $R^{(k)}(z_{*})$ depends only on the $(k-1)$-jet of $h$ at $u_{0}\text{.}$</span></p>
</div>
</div>
<div id="S2.SS2.4" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS2.p9" class="ltx_para">
<p id="S2.SS2.p9.1" class="ltx_p"><span id="S2.SS2.p9.1.1" class="ltx_text">Since $u$ is linear, $(h\circ u)^{(k)}(z_{*})=\kappa^{k}h^{(k)}(u_{0})$ and no Faà di Bruno terms appear. Hence the coefficient of $h^{(k)}(u_{0})$ in $N^{(k)}(z_{*})$ is $a(z_{*})\kappa^{k}\text{,}$ while in $D^{(k)}(z_{*})$ it is $c(z_{*})\kappa^{k}\text{;}$ these agree by $a(z_{*})=c(z_{*})\text{,}$ so $\Delta_{k}$ contains no $h^{(k)}(u_{0})\text{.}$ Differentiating the identity $D(z)R(z)=N(z)$ $k$ times at $z=z_{*}$ and isolating the $j=0$ and $j=k$ terms gives the displayed recursion.
∎</span></p>
</div>
</div>
</section>
<section id="S2.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="moment-recursion-and-the-complexity-staircase"><span class="ltx_tag ltx_tag_subsection">2.3 </span>Moment Recursion and the Complexity Staircase</h3>

<div id="S2.Thmtheorem8" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem8.2" class="ltx_text ltx_font_bold">Corollary 2.8</span></span><span id="S2.Thmtheorem8.3" class="ltx_text ltx_font_bold"> </span>(Moment recursion)<span id="S2.Thmtheorem8.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem8.p1" class="ltx_para">
<p id="S2.Thmtheorem8.p1.1" class="ltx_p"><span id="S2.Thmtheorem8.p1.1.1" class="ltx_text ltx_font_italic">The factorial moments of $T$ satisfy $\eta_{0}=1$ and, for $k\geq 1\text{,}$</span></p>
<table id="S2.E15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\eta_{k}=\frac{1}{pq}\left(\Delta_{k}-\sum_{j=1}^{k-1}\binom{k}{j}D^{(j)}(1)\,\eta_{k-j}\right),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(15)</span></td></tr></tbody>
</table>
<p id="S2.Thmtheorem8.p1.2" class="ltx_p"><span id="S2.Thmtheorem8.p1.2.1" class="ltx_text ltx_font_italic">where $D^{(j)}(1)$ is the $j$-th derivative of $D(w)=(1-w)+qw\,g(ws)$ at $w=1\text{.}$ Since $\Delta_{k}$ involves at most $D_{k-1}$ (Theorem <a href="#S2.Thmtheorem6" title="Theorem 2.6 (Derivative reduction principle). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.6</span></a>) and $D^{(j)}(1)$ involves at most $D_{j}$ for $j\leq k-1$ (by (<a href="#S2.E14" title="In Proof. ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">14</span></a>)), induction on $k$ confirms: $\eta_{k}$ depends on the $(k{-}1)$-jet $\{D_{0},D_{1},\ldots,D_{k-1}\}\text{,}$ never on $D_{k}\text{.}$</span></p>
</div>
</div>
<div id="S2.SS3.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS3.p1" class="ltx_para">
<p id="S2.SS3.p1.1" class="ltx_p"><span id="S2.SS3.p1.1.1" class="ltx_text">Apply the Leibniz rule to $D\cdot G_{T}=N$ at $w=1\text{,}$ separate the $j=0$ and $j=k$ terms, and use $\Delta_{k}=N^{(k)}(1)-D^{(k)}(1)$ to cancel $D^{(k)}(1)\text{.}$
∎</span></p>
</div>
</div>
<div id="S2.SS3.p2" class="ltx_para">
<p id="S2.SS3.p2.1" class="ltx_p">The low-order derivatives of $D$ at $w=1$ are:</p>
<table id="S2.E16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D(1)=qp,\qquad D^{\prime}(1)=-1+qp+qsD_{1},\qquad D^{\prime\prime}(1)=2qsD_{1}+qs^{2}D_{2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(16)</span></td></tr></tbody>
</table>
</div>
<div id="S2.Thmtheorem9" class="ltx_theorem ltx_theorem_example">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem9.2" class="ltx_text ltx_font_bold">Example 2.9</span></span><span id="S2.Thmtheorem9.3" class="ltx_text ltx_font_bold"> </span>(First two moments)<span id="S2.Thmtheorem9.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem9.p1" class="ltx_para">
<p id="S2.Thmtheorem9.p1.1" class="ltx_p">From (<a href="#S2.E15" title="In Corollary 2.8 (Moment recursion). ‣ 2.3 Moment Recursion and the Complexity Staircase ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">15</span></a>) with $k=1\text{:}$ $\eta_{1}=(1-p)/(pq)\text{,}$ recovering Corollary <a href="#S2.Thmtheorem3" title="Corollary 2.3 (Expected completion time). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.3</span></a>. With $k=2\text{:}$ $\eta_{2}=\frac{1}{pq}(-2sD_{1}-2D^{\prime}(1)\,\eta_{1})\text{.}$ The variance $\operatorname{Var}(T)=\eta_{2}+\eta_{1}-\eta_{1}^{2}$ simplifies to</p>
<table id="S2.E17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{Var}(T)=\frac{(1-p)(1+ps)-2qsD_{1}}{p^{2}q^{2}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(17)</span></td></tr></tbody>
</table>
<p id="S2.Thmtheorem9.p1.2" class="ltx_p">which depends on $p=D_{0}$ and $D_{1}=g^{\prime}(s)$ but not on $D_{2}$—exactly as the DRP predicts.</p>
</div>
</div>
<div id="S2.SS3.p3" class="ltx_para">
<p id="S2.SS3.p3.1" class="ltx_p">The DRP asserts that each moment level requires at most $D_{k-1}\text{.}$ The following shows that, for base processes with sufficiently rich structure, it requires <em id="S2.SS3.p3.1.1" class="ltx_emph ltx_font_italic">exactly</em> $D_{k-1}\text{.}$</p>
</div>
<div id="S2.Thmtheorem10" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmtheorem10.2" class="ltx_text ltx_font_bold">Proposition 2.10</span></span><span id="S2.Thmtheorem10.3" class="ltx_text ltx_font_bold"> </span>(Tightness of the staircase)<span id="S2.Thmtheorem10.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmtheorem10.p1" class="ltx_para">
<p id="S2.Thmtheorem10.p1.1" class="ltx_p"><span id="S2.Thmtheorem10.p1.1.1" class="ltx_text ltx_font_italic">For $k\geq 2\text{,}$ the total coefficient of $D_{k-1}$ in $\eta_{k}$ is $-ks^{k-1}/(p^{2}q)\neq 0\text{,}$ provided $D_{k-1}\neq 0\text{.}$ The latter holds whenever $P(T_{0}\geq k)&gt;0\text{.}$ In particular, for base processes with unbounded support, every moment level introduces exactly one new derivative of $g\text{.}$</span></p>
</div>
</div>
<div id="S2.SS3.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS3.p4" class="ltx_para">
<p id="S2.SS3.p4.1" class="ltx_p"><span id="S2.SS3.p4.1.1" class="ltx_text">By Theorem <a href="#S2.Thmtheorem6" title="Theorem 2.6 (Derivative reduction principle). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.6</span></a>, $\Delta_{k}=-ks^{k-1}D_{k-1}$ for $k\geq 2\text{.}$ By induction, $\eta_{k-j}$ for $j\geq 1$ depends on $\{D_{0},\ldots,D_{k-j-1}\}\text{,}$ so $D_{k-1}$ enters the sum in (<a href="#S2.E15" title="In Corollary 2.8 (Moment recursion). ‣ 2.3 Moment Recursion and the Complexity Staircase ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">15</span></a>) only through the $j=k-1$ term $D^{(k-1)}(1)\,\eta_{1}\text{,}$ where $D^{(k-1)}(1)$ contains $D_{k-1}$ with coefficient $qs^{k-1}\text{.}$ Combining: the total coefficient of $D_{k-1}$ in $\eta_{k}$ is $\frac{1}{pq}(-ks^{k-1}-k\,qs^{k-1}\,\eta_{1})=\frac{-ks^{k-1}}{pq}(1+q\eta_{1})=\frac{-ks^{k-1}}{p^{2}q}\text{,}$ using $\eta_{1}=(1-p)/(pq)\text{.}$</span></p>
</div>
<div id="S2.SS3.p5" class="ltx_para">
<p id="S2.SS3.p5.1" class="ltx_p"><span id="S2.SS3.p5.1.1" class="ltx_text">For the second claim: $g^{(k-1)}(s)=\sum_{t\geq k}\frac{t!}{(t-k+1)!}\pi_{t}s^{t-k+1}&gt;0$ whenever some $\pi_{t}&gt;0$ for $t\geq k\text{.}$
∎</span></p>
</div>
</div>
<div id="S2.SS3.p6" class="ltx_para">
<p id="S2.SS3.p6.1" class="ltx_p">Together, Theorem <a href="#S2.Thmtheorem6" title="Theorem 2.6 (Derivative reduction principle). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.6</span></a> and Proposition <a href="#S2.Thmtheorem10" title="Proposition 2.10 (Tightness of the staircase). ‣ 2.3 Moment Recursion and the Complexity Staircase ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.10</span></a> establish a sharp complexity staircase: for base processes with unbounded support, each moment of $T$ introduces exactly one new derivative of $g\text{,}$ and this staircase collapses only when $T_{0}$ has bounded support.</p>
</div>
</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="characterization-of-geometric-tail-catastrophe"><span class="ltx_tag ltx_tag_section">3 </span>Characterization of Geometric-Tail Catastrophe</h2>

<div id="S3.p1" class="ltx_para">
<p id="S3.p1.1" class="ltx_p">§<a href="#S2" title="2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a> established a chain of implications under memoryless catastrophe:</p>
<table id="S3.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\text{memoryless catastrophe}\;\Longrightarrow\;\text{affine PGF structure}\;\Longrightarrow\;\text{derivative reduction (DRP)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.p1.2" class="ltx_p">A natural question arises: <em id="S3.p1.2.1" class="ltx_emph ltx_font_italic">is memoryless catastrophe the only mechanism producing these properties, or do they hold more broadly?</em> This section answers the question precisely. The answer is that affine PGF structure—and hence the DRP—characterizes a slightly larger class, which we call <em id="S3.p1.2.2" class="ltx_emph ltx_font_italic">geometric-tail catastrophe</em>: mechanisms whose hazard rate is constant from the second step onward, with the first-step hazard left free. Full memorylessness is the unique member of this class satisfying an additional algebraic condition ($p=g(s)$ rather than $p\propto g(s)$).</p>
</div>
<div id="S3.p2" class="ltx_para">
<p id="S3.p2.1" class="ltx_p">To state and prove this characterization, we first extend the framework of §<a href="#S2" title="2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a> to general age-based catastrophe mechanisms.</p>
</div>
<section id="S3.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="general-hazard-framework"><span class="ltx_tag ltx_tag_subsection">3.1 </span>General Hazard Framework</h3>

<div id="S3.Thmtheorem1" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem1.2" class="ltx_text ltx_font_bold">Definition 3.1</span></span><span id="S3.Thmtheorem1.3" class="ltx_text ltx_font_bold"> </span>(Age-based catastrophe mechanism)<span id="S3.Thmtheorem1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S3.Thmtheorem1.p1" class="ltx_para">
<p id="S3.Thmtheorem1.p1.1" class="ltx_p">An <em id="S3.Thmtheorem1.p1.1.1" class="ltx_emph ltx_font_italic">age-based catastrophe mechanism</em> is specified by a hazard sequence $(h_{t})_{t\geq 1}$ with $h_{t}\in(0,1)$ for all $t\text{.}$ Here $h_{t}$ is the conditional probability of catastrophe at step $t\text{,}$ given that no catastrophe has occurred in steps $1,\ldots,t-1\text{.}$ The associated <em id="S3.Thmtheorem1.p1.1.2" class="ltx_emph ltx_font_italic">survival function</em> is</p>
<table id="S3.E18" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$S(0)=1,\qquad S(t)=\prod_{i=1}^{t}(1-h_{i}),\quad t\geq 1.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(18)</span></td></tr></tbody>
</table>
<p id="S3.Thmtheorem1.p1.2" class="ltx_p">Thus $S(t)$ is the probability of surviving $t$ consecutive steps without catastrophe. The requirement $h_{t}\in(0,1)$ ensures $S(t)&gt;0$ for all $t$ (every step has a positive probability of both survival and catastrophe).</p>
</div>
</div>
<div id="S3.SS1.p1" class="ltx_para">
<p id="S3.SS1.p1.1" class="ltx_p">Note that memoryless catastrophe (Definition <a href="#S2.Thmtheorem1" title="Definition 2.1 (Memoryless catastrophe). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.1</span></a>) is the special case $h_{t}\equiv q\text{,}$ giving $S(t)=s^{t}\text{.}$ The attempt decomposition (<a href="#S2.E6" title="In 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>) remains valid under any age-based mechanism: each attempt starts from the empty state, so successive attempts are i.i.d. The success probability generalizes from $p=g(s)$ to</p>
<table id="S3.E19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p=\sum_{t\geq 1}S(t)\,\pi_{t},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(19)</span></td></tr></tbody>
</table>
<p id="S3.SS1.p1.2" class="ltx_p">which is no longer a PGF evaluation unless $S(t)$ is exponential in $t\text{.}$ The expected completion time generalizes from Theorem <a href="#S2.Thmtheorem2" title="Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a> as follows.</p>
</div>
<div id="S3.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem2.2" class="ltx_text ltx_font_bold">Lemma 3.2</span></span><span id="S3.Thmtheorem2.3" class="ltx_text ltx_font_bold"> </span>(Expected attempt length)<span id="S3.Thmtheorem2.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S3.Thmtheorem2.p1" class="ltx_para">
<p id="S3.Thmtheorem2.p1.1" class="ltx_p"><span id="S3.Thmtheorem2.p1.1.1" class="ltx_text ltx_font_italic">Under an age-based mechanism with survival function $S\text{,}$ the expected length of a single attempt (regardless of outcome) satisfies</span></p>
<table id="S3.E20" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[\ell]=\sum_{j\geq 1}F(j)\,\pi_{j},\qquad F(j)=\sum_{t=0}^{j-1}S(t).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(20)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S3.SS1.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS1.p2" class="ltx_para">
<p id="S3.SS1.p2.1" class="ltx_p"><span id="S3.SS1.p2.1.1" class="ltx_text">Condition on $T_{0}=j\text{:}$ step $t\leq j$ is reached with probability $S(t-1)\text{.}$
∎</span></p>
</div>
</div>
<div id="S3.Thmtheorem3" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem3.2" class="ltx_text ltx_font_bold">Proposition 3.3</span></span><span id="S3.Thmtheorem3.3" class="ltx_text ltx_font_bold"> </span>(General expected completion time)<span id="S3.Thmtheorem3.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S3.Thmtheorem3.p1" class="ltx_para">
<p id="S3.Thmtheorem3.p1.1" class="ltx_p"><span id="S3.Thmtheorem3.p1.1.1" class="ltx_text ltx_font_italic">Assume $E[\ell]=\sum_{j\geq 1}F(j)\pi_{j}&lt;\infty\text{.}$ Then</span></p>
<table id="S3.E21" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[T]=\frac{E[\ell]}{p}=\frac{\sum_{j\geq 1}F(j)\pi_{j}}{\sum_{j\geq 1}S(j)\pi_{j}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(21)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S3.SS1.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS1.p3" class="ltx_para">
<p id="S3.SS1.p3.1" class="ltx_p"><span id="S3.SS1.p3.1.1" class="ltx_text">The pairs $(\ell_{i},\mathrm{outcome}_{i})$ are i.i.d., and $M=N+1\sim\operatorname{Geom}_{1}(p)$ is a stopping time. Since $E[\ell]&lt;\infty\text{,}$ Wald’s identity applies and gives $E[T]=E[\ell]\cdot E[M]=\frac{E[\ell]}{p}\text{.}$
∎</span></p>
</div>
</div>
<div id="S3.SS1.p4" class="ltx_para">
<p id="S3.SS1.p4.1" class="ltx_p">Formula (<a href="#S3.E21" title="In Proposition 3.3 (General expected completion time). ‣ 3.1 General Hazard Framework ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">21</span></a>) expresses $E[T]$ as a ratio of two linear functionals of the base distribution $(\pi_{j})_{j\geq 1}\text{.}$ In the memoryless case, $S(t)=s^{t}$ makes the denominator $p=g(s)$—a PGF evaluation—and $E[T]$ depends on $T_{0}$ only through this single number. For a general mechanism, $E[T]$ depends on the full interaction between $(\pi_{j})$ and $S\text{.}$</p>
</div>
</section>
<section id="S3.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="geometric-tail-catastrophe"><span class="ltx_tag ltx_tag_subsection">3.2 </span>Geometric-Tail Catastrophe</h3>

<div id="S3.Thmtheorem4" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem4.2" class="ltx_text ltx_font_bold">Definition 3.4</span></span><span id="S3.Thmtheorem4.3" class="ltx_text ltx_font_bold"> </span>(Geometric-tail catastrophe)<span id="S3.Thmtheorem4.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S3.Thmtheorem4.p1" class="ltx_para">
<p id="S3.Thmtheorem4.p1.1" class="ltx_p">A hazard sequence $(h_{t})_{t\geq 1}$ has <em id="S3.Thmtheorem4.p1.1.1" class="ltx_emph ltx_font_italic">geometric tail</em> if there exist $a\in(0,1)$ and $q\in(0,1)$ such that</p>
<table id="S3.Ex15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$h_{1}=1-a,\qquad h_{t}=q\quad\text{for all }t\geq 2.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.Thmtheorem4.p1.2" class="ltx_p">Equivalently, $S(t)=a\,s^{t-1}$ for $t\geq 1\text{,}$ where $s=1-q\text{.}$ The parameter $a=S(1)=1-h_{1}$ is the first-step survival probability. The special case $a=s$ (i.e., $h_{1}=q$) recovers memoryless catastrophe.</p>
</div>
</div>
<div id="S3.SS2.p1" class="ltx_para">
<p id="S3.SS2.p1.1" class="ltx_p">The geometric-tail class has one degree of freedom beyond full memorylessness: the first-step hazard $h_{1}$ may differ from $q\text{.}$ The next proposition shows that every member of this class produces a PGF with affine structure, establishing the forward direction of the characterization.</p>
</div>
<div id="S3.Thmtheorem5" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem5.2" class="ltx_text ltx_font_bold">Proposition 3.5</span></span><span id="S3.Thmtheorem5.3" class="ltx_text ltx_font_bold"> </span>(Geometric-tail PGF formula)<span id="S3.Thmtheorem5.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S3.Thmtheorem5.p1" class="ltx_para">
<p id="S3.Thmtheorem5.p1.1" class="ltx_p"><span id="S3.Thmtheorem5.p1.1.1" class="ltx_text ltx_font_italic">Under geometric-tail catastrophe with parameters $(a,q)\text{,}$ the success probability is $p=(a/s)\,g(s)$ and the completion-time PGF is</span></p>
<table id="S3.E22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{T}(w)=\frac{a(1-u)\,g(u)}{s(1-w)(1-w(s-a))+aqw\,g(u)},\qquad u=ws.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(22)</span></td></tr></tbody>
</table>
<p id="S3.Thmtheorem5.p1.2" class="ltx_p"><span id="S3.Thmtheorem5.p1.2.1" class="ltx_text ltx_font_italic">This exhibits uniform affine PGF structure (Definition <a href="#S2.Thmtheorem4" title="Definition 2.4 (Uniform affine PGF structure). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.4</span></a>) with coefficient equality $\alpha_{N}(1)=\alpha_{D}(1)=aq\text{.}$ Setting $a=s$ recovers the memoryless formula (<a href="#S2.E9" title="In Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a>).</span></p>
</div>
</div>
<div id="S3.SS2.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS2.p2" class="ltx_para">
<p id="S3.SS2.p2.1" class="ltx_p"><span id="S3.SS2.p2.1.1" class="ltx_text">Since $S(t)=as^{t-1}\text{,}$ the success probability is $p=(a/s)\,g(s)$ and the successful-attempt PGF is $G_{B}(w)=a\,g(u)/(ps)\text{,}$ where $u=ws\text{.}$</span></p>
</div>
<div id="S3.SS2.p3" class="ltx_para">
<p id="S3.SS2.p3.1" class="ltx_p"><span id="S3.SS2.p3.1.1" class="ltx_text">For the failed-attempt PGF, note that the only departure from the memoryless calculation (§<a href="#S2" title="2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) is the first-step hazard $h_{1}=1-a\neq q\text{.}$ Splitting accordingly:</span></p>
<table id="S3.Ex16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(1-p)\,G_{A}(w)=w(1-a)+\frac{aqw}{s}\sum_{j\geq 1}u^{j}\,P(T_{0}&gt;j).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS2.p3.2" class="ltx_p"><span id="S3.SS2.p3.2.1" class="ltx_text">The identity $\sum_{j\geq 1}u^{j}P(T_{0}&gt;j)=(u-g(u))/(1-u)$ (used in §<a href="#S2" title="2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>) gives</span></p>
<table id="S3.Ex17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(1-p)\,G_{A}(w)=w(1-a)+\frac{aqw(u-g(u))}{s(1-u)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS2.p3.3" class="ltx_p"><span id="S3.SS2.p3.3.1" class="ltx_text">Substituting into $G_{T}=p\,G_{B}/[1-(1-p)G_{A}]$ and clearing denominators, the denominator simplifies (using $s+q=1$ and $u=ws$) to $s(1-w)(1-w(s-a))+aqw\,g(u)\text{,}$ yielding (<a href="#S3.E22" title="In Proposition 3.5 (Geometric-tail PGF formula). ‣ 3.2 Geometric-Tail Catastrophe ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">22</span></a>). (Setting $a=s$ eliminates the $1-w(s-a)$ factor and recovers (<a href="#S2.E9" title="In Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a>).)</span></p>
</div>
<div id="S3.SS2.p4" class="ltx_para">
<p id="S3.SS2.p4.1" class="ltx_p"><span id="S3.SS2.p4.1.1" class="ltx_text">The $g(u)$-coefficients are $\alpha_{N}(w)=a(1-u)$ and $\alpha_{D}(w)=aqw\text{,}$ giving $\alpha_{N}(1)=\alpha_{D}(1)=aq\text{.}$ Since the numerator has no $g$-free term ($\beta_{N}\equiv 0$) and $\beta_{D}(1)=0\text{,}$ we obtain $G_{T}(1)=1\text{.}$ Non-degeneracy: $D(1)=aqg(s)=pqs&gt;0\text{.}$
∎</span></p>
</div>
</div>
<div id="S3.SS2.p5" class="ltx_para">
<p id="S3.SS2.p5.1" class="ltx_p">Since the geometric-tail PGF has the same affine-ratio form, the same linear shift $u=ws\text{,}$ and coefficient matching at $w=1\text{,}$ Lemma <a href="#S2.Thmtheorem7" title="Lemma 2.7 (Affine-ratio recursion). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.7</span></a> applies verbatim. Hence the DRP holds for geometric-tail mechanisms, with $\alpha_{N}(1)=\alpha_{D}(1)=aq$ replacing $q\text{.}$</p>
</div>
</section>
<section id="S3.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-characterization-theorem"><span class="ltx_tag ltx_tag_subsection">3.3 </span>The Characterization Theorem</h3>

<div id="S3.SS3.p1" class="ltx_para">
<p id="S3.SS3.p1.1" class="ltx_p">We now prove the converse: geometric-tail catastrophe is the <em id="S3.SS3.p1.1.1" class="ltx_emph ltx_font_italic">only</em> age-based mechanism producing affine PGF structure. The result takes the form of a four-way equivalence linking the survival function, the PGF structure, the derivative reduction property, and the success probability formula.</p>
</div>
<div id="S3.Thmtheorem6" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem6.2" class="ltx_text ltx_font_bold">Theorem 3.6</span></span><span id="S3.Thmtheorem6.3" class="ltx_text ltx_font_bold"> </span>(Characterization)<span id="S3.Thmtheorem6.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S3.Thmtheorem6.p1" class="ltx_para">
<p id="S3.Thmtheorem6.p1.1" class="ltx_p"><span id="S3.Thmtheorem6.p1.1.1" class="ltx_text ltx_font_italic">Among age-based catastrophe mechanisms (Definition <a href="#S3.Thmtheorem1" title="Definition 3.1 (Age-based catastrophe mechanism). ‣ 3.1 General Hazard Framework ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.1</span></a>), the following are equivalent:</span></p>
<ol id="S3.I1" class="ltx_enumerate">
<li id="S3.I1.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(A)</span> 
<div id="S3.I1.i1.p1" class="ltx_para">
<p id="S3.I1.i1.p1.1" class="ltx_p"><em id="S3.I1.i1.p1.1.1" class="ltx_emph">Geometric-tail catastrophe</em><span id="S3.I1.i1.p1.1.2" class="ltx_text ltx_font_italic">: </span>$S(t)=a\,s^{t-1}$<span id="S3.I1.i1.p1.1.3" class="ltx_text ltx_font_italic"> for </span>$t\geq 1$<span id="S3.I1.i1.p1.1.4" class="ltx_text ltx_font_italic"> (Definition </span><a href="#S3.Thmtheorem4" title="Definition 3.4 (Geometric-tail catastrophe). ‣ 3.2 Geometric-Tail Catastrophe ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref ltx_font_italic"><span class="ltx_text ltx_ref_tag">3.4</span></a><span id="S3.I1.i1.p1.1.5" class="ltx_text ltx_font_italic">).</span></p>
</div></li>
<li id="S3.I1.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(B)</span> 
<div id="S3.I1.i2.p1" class="ltx_para">
<p id="S3.I1.i2.p1.1" class="ltx_p"><em id="S3.I1.i2.p1.1.1" class="ltx_emph">Uniform affine PGF structure</em><span id="S3.I1.i2.p1.1.2" class="ltx_text ltx_font_italic">: Definition </span><a href="#S2.Thmtheorem4" title="Definition 2.4 (Uniform affine PGF structure). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref ltx_font_italic"><span class="ltx_text ltx_ref_tag">2.4</span></a><span id="S3.I1.i2.p1.1.3" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
<li id="S3.I1.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(C)</span> 
<div id="S3.I1.i3.p1" class="ltx_para">
<p id="S3.I1.i3.p1.1" class="ltx_p"><em id="S3.I1.i3.p1.1.1" class="ltx_emph">Derivative reduction</em><span id="S3.I1.i3.p1.1.2" class="ltx_text ltx_font_italic">: there exists </span>$z_{0}\in(0,1)$<span id="S3.I1.i3.p1.1.3" class="ltx_text ltx_font_italic"> such that for every </span>$k\geq 1$<span id="S3.I1.i3.p1.1.4" class="ltx_text ltx_font_italic"> and every finitely-supported </span>$T_{0}$<span id="S3.I1.i3.p1.1.5" class="ltx_text ltx_font_italic">, the </span>$k$<span id="S3.I1.i3.p1.1.6" class="ltx_text ltx_font_italic">-th factorial moment </span>$\eta_{k}$<span id="S3.I1.i3.p1.1.7" class="ltx_text ltx_font_italic"> depends on </span>$T_{0}$<span id="S3.I1.i3.p1.1.8" class="ltx_text ltx_font_italic"> only through </span>$\{g^{(j)}(z_{0})\}_{j=0}^{k-1}$<span id="S3.I1.i3.p1.1.9" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
<li id="S3.I1.i4" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(D)</span> 
<div id="S3.I1.i4.p1" class="ltx_para">
<p id="S3.I1.i4.p1.1" class="ltx_p"><em id="S3.I1.i4.p1.1.1" class="ltx_emph">Proportional single-point sufficiency</em><span id="S3.I1.i4.p1.1.2" class="ltx_text ltx_font_italic">: there exist </span>$z_{0}\in(0,1)$<span id="S3.I1.i4.p1.1.3" class="ltx_text ltx_font_italic"> and </span>$\lambda&gt;0$<span id="S3.I1.i4.p1.1.4" class="ltx_text ltx_font_italic"> such that </span>$p=\lambda\,g(z_{0})$<span id="S3.I1.i4.p1.1.5" class="ltx_text ltx_font_italic"> for all finitely-supported </span>$T_{0}$<span id="S3.I1.i4.p1.1.6" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S3.SS3.p2" class="ltx_para">
<p id="S3.SS3.p2.1" class="ltx_p">We prove the cycle (A)$\Rightarrow$(B)$\Rightarrow$(C)$\Rightarrow$(A), and independently prove (A)$\Leftrightarrow$(D). The implications (A)$\Rightarrow$(B) and (A)$\Rightarrow$(D) have been established; the substance lies in (C)$\Rightarrow$(A), which uses only the $k=1$ instance of (C) and proceeds by a Möbius rigidity argument.</p>
</div>
<div id="S3.SS3.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <span id="S3.SS3.2.1" class="ltx_text ltx_font_upright">(A)$\Rightarrow$(B)</span>.</h6>
<div id="S3.SS3.p3" class="ltx_para">
<p id="S3.SS3.p3.1" class="ltx_p"><span id="S3.SS3.p3.1.1" class="ltx_text">This is Proposition <a href="#S3.Thmtheorem5" title="Proposition 3.5 (Geometric-tail PGF formula). ‣ 3.2 Geometric-Tail Catastrophe ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.5</span></a>.
∎</span></p>
</div>
</div>
<div id="S3.SS3.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <span id="S3.SS3.3.1" class="ltx_text ltx_font_upright">(B)$\Rightarrow$(C)</span>.</h6>
<div id="S3.SS3.p4" class="ltx_para">
<p id="S3.SS3.p4.1" class="ltx_p"><span id="S3.SS3.p4.1.1" class="ltx_text">Suppose</span></p>
<table id="S3.Ex18" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{T}(w)=\frac{a(w)g(u(w))+b(w)}{c(w)g(u(w))+d(w)},\qquad u(1)=u_{1}\in(0,1),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS3.p4.2" class="ltx_p"><span id="S3.SS3.p4.2.1" class="ltx_text">with $u$ linear. From $G_{T}(1)=1$ for all finitely-supported $T_{0}\text{,}$ taking $T_{0}\equiv n$ and letting $n\to\infty$ gives $b(1)=d(1)\text{,}$ and then back-substitution gives $a(1)=c(1)\text{.}$ Since non-degeneracy yields $c(1)g(u_{1})+d(1)\neq 0\text{,}$ Lemma <a href="#S2.Thmtheorem7" title="Lemma 2.7 (Affine-ratio recursion). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.7</span></a> applies with $R=G_{T}\text{,}$ $h=g\text{,}$ $z_{*}=1\text{,}$ and $u_{0}=u_{1}\text{.}$ Therefore the $k$-th factorial moment $\eta_{k}=G_{T}^{(k)}(1)$ depends only on $\{g^{(j)}(u_{1})\}_{j=0}^{k-1}\text{.}$
∎</span></p>
</div>
</div>
<div id="S3.SS3.4" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <span id="S3.SS3.4.1" class="ltx_text ltx_font_upright">(C)$\Rightarrow$(A)</span>.</h6>
<div id="S3.SS3.p5" class="ltx_para">
<p id="S3.SS3.p5.1" class="ltx_p"><span id="S3.SS3.p5.1.1" class="ltx_text">We use only the $k=1$ case: $E[T]$ depends on $T_{0}$ only through $g(z_{0})$ for some $z_{0}\in(0,1)\text{.}$ By Proposition <a href="#S3.Thmtheorem3" title="Proposition 3.3 (General expected completion time). ‣ 3.1 General Hazard Framework ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.3</span></a>, there exists $\psi:(0,1)\to\mathbb{R}$ such that</span></p>
<table id="S3.E23" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{\sum_{j\geq 1}F(j)\,\pi_{j}}{\sum_{j\geq 1}S(j)\,\pi_{j}}=\psi\!\left(\sum_{j\geq 1}z_{0}^{j}\,\pi_{j}\right)\quad\text{for all finitely-supported }(\pi_{j}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(23)</span></td></tr></tbody>
</table>
</div>
<div id="S3.SS3.p6" class="ltx_para">
<p id="S3.SS3.p6.1" class="ltx_p"><em id="S3.SS3.p6.1.1" class="ltx_emph ltx_font_italic">Step 1: Point masses.</em><span id="S3.SS3.p6.1.2" class="ltx_text"> 
Taking $\pi=\delta_{j}$ gives $\psi(z_{0}^{j})=F(j)/S(j)=:f_{j}$ for each $j\geq 1\text{.}$</span></p>
</div>
<div id="S3.SS3.p7" class="ltx_para">
<p id="S3.SS3.p7.1" class="ltx_p"><em id="S3.SS3.p7.1.1" class="ltx_emph ltx_font_italic">Step 2: Two-point distributions force $\psi$ to be Möbius.</em><span id="S3.SS3.p7.1.2" class="ltx_text"> 
For $\pi_{a}=\alpha\text{,}$ $\pi_{b}=1-\alpha$ with $a&lt;b\text{,}$ set $v=\alpha z_{0}^{a}+(1-\alpha)z_{0}^{b}\text{.}$ Substituting into (<a href="#S3.E23" title="In Proof of (C)⇒(A). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">23</span></a>) and solving for $\alpha$ in terms of $v$ gives</span></p>
<table id="S3.E24" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\psi(v)=\frac{(F(a)-F(b))\,v+F(b)z_{0}^{a}-F(a)z_{0}^{b}}{(S(a)-S(b))\,v+S(b)z_{0}^{a}-S(a)z_{0}^{b}}=:M_{ab}(v)$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(24)</span></td></tr></tbody>
</table>
<p id="S3.SS3.p7.2" class="ltx_p"><span id="S3.SS3.p7.2.1" class="ltx_text">on $[z_{0}^{b},z_{0}^{a}]\text{.}$ This is a Möbius transformation of $v\text{.}$</span></p>
</div>
<div id="S3.SS3.p8" class="ltx_para">
<p id="S3.SS3.p8.1" class="ltx_p"><em id="S3.SS3.p8.1.1" class="ltx_emph ltx_font_italic">Step 3: Global consistency.</em><span id="S3.SS3.p8.1.2" class="ltx_text"> 
For $a&lt;c&lt;b\text{,}$ the Möbius transformations $M_{ab}$ and $M_{ac}$ agree on the interval $[z_{0}^{c},z_{0}^{a}]\text{,}$ which contains infinitely many points; since a non-degenerate Möbius transformation is determined by three values, $M_{ab}=M_{ac}$ as rational functions. For any two pairs $(a_{1},b_{1})\text{,}$ $(a_{2},b_{2})$ with $a_{i}&lt;b_{i}\text{,}$ setting $a^{*}=\min(a_{1},a_{2})\text{,}$ $b^{*}=\max(b_{1},b_{2})$ gives $[z_{0}^{b_{i}},z_{0}^{a_{i}}]\subset[z_{0}^{b^{*}},z_{0}^{a^{*}}]$ for each $i$ (since $z_{0}\in(0,1)$ makes $j\mapsto z_{0}^{j}$ decreasing), so $M_{a_{1}b_{1}}=M_{a^{*}b^{*}}=M_{a_{2}b_{2}}\text{.}$ Hence all $M_{ab}$ coincide with a single</span></p>
<table id="S3.E25" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\psi(v)=M(v)=\frac{Av+B}{Cv+D}\qquad\text{on }(0,z_{0}].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(25)</span></td></tr></tbody>
</table>
<p id="S3.SS3.p8.2" class="ltx_p"><span id="S3.SS3.p8.2.1" class="ltx_text">The denominator slope of each $M_{ab}$ is proportional to $S(a)-S(b)\neq 0$ (since $h_{t}\in(0,1)$ makes $S$ strictly decreasing), so $C\neq 0\text{.}$</span></p>
</div>
<div id="S3.SS3.p9" class="ltx_para">
<p id="S3.SS3.p9.1" class="ltx_p"><em id="S3.SS3.p9.1.1" class="ltx_emph ltx_font_italic">Step 4: Coefficient consistency forces $F=rS+c\text{.}$</em><span id="S3.SS3.p9.1.2" class="ltx_text"> 
Since $M_{ab}=M$ up to a common scalar, $A/C=(F(a)-F(b))/(S(a)-S(b))$ is constant across all $a\neq b\text{.}$ Denoting this constant by $r\text{,}$ we obtain $F(j)=rS(j)+c$ for all $j\geq 1\text{.}$</span></p>
</div>
<div id="S3.SS3.p10" class="ltx_para">
<p id="S3.SS3.p10.1" class="ltx_p"><em id="S3.SS3.p10.1.1" class="ltx_emph ltx_font_italic">Step 5: Differencing yields constant hazard from step $2$ onward.</em><span id="S3.SS3.p10.1.2" class="ltx_text"> 
From $F(j)=\sum_{t=0}^{j-1}S(t)\text{:}$ $F(j+1)-F(j)=S(j)\text{.}$ From $F=rS+c\text{:}$ $F(j+1)-F(j)=r(S(j+1)-S(j))=-rS(j)h_{j+1}\text{.}$ Equating and dividing by $S(j)&gt;0\text{:}$</span></p>
<table id="S3.Ex19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$h_{j+1}=-1/r\quad\text{for all }j\geq 1.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.SS3.p10.2" class="ltx_p"><span id="S3.SS3.p10.2.1" class="ltx_text">Hence $h_{t}=q:=-1/r$ for all $t\geq 2\text{,}$ with $r&lt;-1$ (since $q\in(0,1)$). Setting $a=S(1)\in(0,1)$ gives $S(t)=as^{t-1}$ for $t\geq 1\text{,}$ confirming geometric-tail catastrophe.
∎</span></p>
</div>
</div>
<div id="S3.SS3.5" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <span id="S3.SS3.5.1" class="ltx_text ltx_font_upright">(A)$\Rightarrow$(D)</span>.</h6>
<div id="S3.SS3.p11" class="ltx_para">
<p id="S3.SS3.p11.1" class="ltx_p"><span id="S3.SS3.p11.1.1" class="ltx_text">If $S(t)=as^{t-1}\text{,}$ then $p=\sum_{t\geq 1}as^{t-1}\pi_{t}=(a/s)\,g(s)\text{,}$ with $z_{0}=s$ and $\lambda=a/s&gt;0\text{.}$
∎</span></p>
</div>
</div>
<div id="S3.SS3.6" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <span id="S3.SS3.6.1" class="ltx_text ltx_font_upright">(D)$\Rightarrow$(A)</span>.</h6>
<div id="S3.SS3.p12" class="ltx_para">
<p id="S3.SS3.p12.1" class="ltx_p"><span id="S3.SS3.p12.1.1" class="ltx_text">The hypothesis $p=\lambda\,g(z_{0})$ for all finitely-supported $(\pi_{j})$ gives, upon taking $\pi=\delta_{t}\text{:}$ $S(t)=\lambda\,z_{0}^{t}$ for each $t\geq 1\text{.}$ Hence $h_{t}=1-S(t)/S(t-1)=1-z_{0}$ for all $t\geq 2\text{,}$ confirming geometric tail with $s=z_{0}\text{,}$ $q=1-z_{0}\text{,}$ and $a=\lambda z_{0}\text{.}$
∎</span></p>
</div>
</div>
<div id="S3.Thmtheorem7" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem7.2" class="ltx_text ltx_font_italic">Remark 3.7</span></span><span id="S3.Thmtheorem7.3" class="ltx_text ltx_font_italic"> </span>(Emphasis of the (C)$\Rightarrow$(A) argument)<span id="S3.Thmtheorem7.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S3.Thmtheorem7.p1" class="ltx_para">
<p id="S3.Thmtheorem7.p1.1" class="ltx_p">Only the $k=1$ instance of (C) is needed: the condition that $E[T]$ depends on $T_{0}$ through $g(z_{0})$ alone already forces geometric-tail catastrophe. The mechanism is Möbius rigidity: the ratio of two linear functionals of $(\pi_{j})$ equaling a function of a third forces that function to be linear fractional, and determination by three points propagates the local constraint globally. This is the same low-dimensionality phenomenon that drives the DRP—there, affine dependence on $g(u)$ forces the highest derivative to cancel; here, it forces the hazard sequence to stabilize.</p>
</div>
</div>
</section>
<section id="S3.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="from-geometric-tail-to-full-memorylessness"><span class="ltx_tag ltx_tag_subsection">3.4 </span>From Geometric Tail to Full Memorylessness</h3>

<div id="S3.SS4.p1" class="ltx_para">
<p id="S3.SS4.p1.1" class="ltx_p">The geometric-tail class has one free parameter ($a=S(1)$) beyond the catastrophe rate $q\text{.}$ The following corollary identifies the algebraic condition that pins down this parameter.</p>
</div>
<div id="S3.Thmtheorem8" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem8.2" class="ltx_text ltx_font_bold">Corollary 3.8</span></span><span id="S3.Thmtheorem8.3" class="ltx_text ltx_font_bold"> </span>(Full memorylessness)<span id="S3.Thmtheorem8.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S3.Thmtheorem8.p1" class="ltx_para">
<p id="S3.Thmtheorem8.p1.1" class="ltx_p"><span id="S3.Thmtheorem8.p1.1.1" class="ltx_text ltx_font_italic">Among geometric-tail mechanisms, full memorylessness ($h_{t}\equiv q$ for all $t\geq 1$) is equivalent to $\lambda=1$ in condition (D) of Theorem <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Characterization). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a>, i.e., the success probability is a literal PGF evaluation:</span></p>
<table id="S3.Ex20" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p=g(s).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S3.SS4.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS4.p2" class="ltx_para">
<p id="S3.SS4.p2.1" class="ltx_p"><span id="S3.SS4.p2.1.1" class="ltx_text">Geometric tail gives $p=(a/s)\,g(s)\text{,}$ so $\lambda=a/s\text{.}$ If $\lambda=1$ then $a=s\text{,}$ hence $h_{1}=1-a=1-s=q\text{,}$ giving full memorylessness. Conversely, memorylessness gives $a=s$ and $\lambda=1\text{.}$
∎</span></p>
</div>
</div>
<div id="S3.Thmtheorem9" class="ltx_theorem ltx_theorem_example">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem9.2" class="ltx_text ltx_font_bold">Example 3.9</span></span><span id="S3.Thmtheorem9.3" class="ltx_text ltx_font_bold"> </span>(Geometric-tail but not memoryless)<span id="S3.Thmtheorem9.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S3.Thmtheorem9.p1" class="ltx_para">
<p id="S3.Thmtheorem9.p1.1" class="ltx_p">Set $h_{1}=1/2$ and $h_{t}=1/4$ for $t\geq 2\text{,}$ so $a=1/2\text{,}$ $q=1/4\text{,}$ $s=3/4\text{.}$ Then $S(t)=(1/2)(3/4)^{t-1}$ and $p=(2/3)\,g(3/4)\text{.}$ Since $h_{1}=1/2\neq 1/4=q\text{,}$ this is not memoryless, yet it has uniform affine PGF structure by Proposition <a href="#S3.Thmtheorem5" title="Proposition 3.5 (Geometric-tail PGF formula). ‣ 3.2 Geometric-Tail Catastrophe ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.5</span></a>, with $\alpha_{N}(1)=\alpha_{D}(1)=aq=1/8\text{.}$ This confirms that affine PGF structure characterizes the geometric-tail class, not full memorylessness.</p>
</div>
</div>
<div id="S3.Thmtheorem10" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S3.Thmtheorem10.2" class="ltx_text ltx_font_italic">Remark 3.10</span></span><span id="S3.Thmtheorem10.3" class="ltx_text ltx_font_italic"> </span>(Proportionality is essential)<span id="S3.Thmtheorem10.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S3.Thmtheorem10.p1" class="ltx_para">
<p id="S3.Thmtheorem10.p1.1" class="ltx_p">Condition (D) requires $p=\lambda\,g(z_{0})$—proportionality, not merely functional dependence. If one weakens (D) to “$p=\varphi(g(z_{0}))$ for some function $\varphi\text{,}$” then two-point distributions force $\varphi$ to be affine: $\varphi(x)=\lambda x+\mu\text{.}$ When $\mu&gt;0\text{,}$ the resulting survival function $S(j)=\lambda z_{0}^{j}+\mu$ has $h_{j}\to 0$ as $j\to\infty\text{,}$ violating both (B) and (C). Thus proportionality ($\mu=0$) is necessary for the equivalence.</p>
</div>
</div>
</section>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="exponential-approximation"><span class="ltx_tag ltx_tag_section">4 </span>Exponential Approximation</h2>

<div id="S4.p1" class="ltx_para">
<p id="S4.p1.1" class="ltx_p">The attempt decomposition (Theorem <a href="#S2.Thmtheorem2" title="Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a>) writes $T=\sum_{i=1}^{N}A_{i}+B$ as a geometric sum plus a perturbation. A classical theorem of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib36" title="" class="ltx_ref">36</a>]</cite> establishes that normalized geometric sums converge to the exponential distribution; see <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib21" title="" class="ltx_ref">21</a>, <a href="#bib.bib25" title="" class="ltx_ref">25</a>]</cite> for comprehensive treatments. §<a href="#S2" title="2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a> revealed a specific algebraic structure—the coefficient equality $\alpha_{N}(1)=\alpha_{D}(1)$—governing the PGF of $T\text{.}$ We now show that this structure sharpens Rényi’s result into:</p>
<ol id="S4.I1" class="ltx_enumerate">
<li id="S4.I1.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(i)</span> 
<div id="S4.I1.i1.p1" class="ltx_para">
<p id="S4.I1.i1.p1.1" class="ltx_p">a quantitative Laplace expansion whose leading error is second-order (the first-order term vanishes as an algebraic identity, not an asymptotic cancellation), and</p>
</div></li>
<li id="S4.I1.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(ii)</span> 
<div id="S4.I1.i2.p1" class="ltx_para">
<p id="S4.I1.i2.p1.1" class="ltx_p">a sharp two-sided Kolmogorov bound $d_{K}(T/E[T],\operatorname{Exp}(1))\asymp p+|\alpha|$ that closes a logarithmic gap left by the smoothing inequality approach.</p>
</div></li>
</ol>
<p id="S4.p1.2" class="ltx_p">Both results hold for arbitrary base processes $T_{0}$ and are driven by the same coefficient equality.</p>
</div>
<section id="S4.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-perturbation-parameter"><span class="ltx_tag ltx_tag_subsection">4.1 </span>The Perturbation Parameter</h3>

<div id="S4.SS1.p1" class="ltx_para">
<p id="S4.SS1.p1.1" class="ltx_p">Recall the notation: $\mu=E[T]=(1-p)/(qp)\text{,}$ $b=E[B]\text{,}$ and write $W=T/\mu$ for the normalized completion time. From the decomposition (<a href="#S2.E6" title="In 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>), $W=U/\mu+B/\mu$ where $U=\sum_{i=1}^{N}A_{i}\text{.}$</p>
</div>
<div id="S4.Thmtheorem1" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem1.2" class="ltx_text ltx_font_bold">Definition 4.1</span></span><span id="S4.Thmtheorem1.3" class="ltx_text ltx_font_bold"> </span>(Perturbation parameters)<span id="S4.Thmtheorem1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem1.p1" class="ltx_para">
<p id="S4.Thmtheorem1.p1.1" class="ltx_p">Define</p>
<table id="S4.E26" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha=\frac{s(p-qD_{1})}{1-p},\qquad\beta=\frac{1-qp-qsD_{1}}{1-p},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(26)</span></td></tr></tbody>
</table>
<p id="S4.Thmtheorem1.p1.2" class="ltx_p">where $D_{1}=g^{\prime}(s)\text{.}$</p>
</div>
</div>
<div id="S4.Thmtheorem2" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem2.2" class="ltx_text ltx_font_bold">Proposition 4.2</span></span><span id="S4.Thmtheorem2.3" class="ltx_text ltx_font_bold"> </span>(Properties of the perturbation parameters)<span id="S4.Thmtheorem2.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem2.p1" class="ltx_para">
<p id="S4.Thmtheorem2.p1.1" class="ltx_p"><span id="S4.Thmtheorem2.p1.1.1" class="ltx_text"></span><span id="S4.Thmtheorem2.p1.1.2" class="ltx_text"></span></p>
<ol id="S4.I2" class="ltx_enumerate">
<li id="S4.I2.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(a)</span> 
<div id="S4.I2.i1.p1" class="ltx_para">
<p id="S4.I2.i1.p1.1" class="ltx_p"><em id="S4.I2.i1.p1.1.1" class="ltx_emph">Fundamental identity</em><span id="S4.I2.i1.p1.1.2" class="ltx_text ltx_font_italic">: </span>$1+\alpha-\beta=0$<span id="S4.I2.i1.p1.1.3" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
<li id="S4.I2.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(b)</span> 
<div id="S4.I2.i2.p1" class="ltx_para">
<p id="S4.I2.i2.p1.1" class="ltx_p"><em id="S4.I2.i2.p1.1.1" class="ltx_emph">Successful-attempt identity</em><span id="S4.I2.i2.p1.1.2" class="ltx_text ltx_font_italic">: </span>$b/\mu=sp/(1-p)-\alpha=qsD_{1}/(1-p)$<span id="S4.I2.i2.p1.1.3" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
<li id="S4.I2.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(c)</span> 
<div id="S4.I2.i3.p1" class="ltx_para">
<p id="S4.I2.i3.p1.1" class="ltx_p"><em id="S4.I2.i3.p1.1.1" class="ltx_emph">Vanishing rate</em><span id="S4.I2.i3.p1.1.2" class="ltx_text ltx_font_italic">: for fixed </span>$q\in(0,1)$<span id="S4.I2.i3.p1.1.3" class="ltx_text ltx_font_italic">, </span>$|\alpha|=O_{q}(p|\ln p|)$<span id="S4.I2.i3.p1.1.4" class="ltx_text ltx_font_italic"> as </span>$p\to 0$<span id="S4.I2.i3.p1.1.5" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S4.SS1.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS1.p2" class="ltx_para">
<p id="S4.SS1.p2.1" class="ltx_p"><span id="S4.SS1.p2.1.1" class="ltx_text">(a) $1+\alpha-\beta=1+[sp-qsD_{1}-1+qp+qsD_{1}]/(1-p)=1+(p-1)/(1-p)=0\text{,}$ noting that $s+q=1\text{.}$</span></p>
</div>
<div id="S4.SS1.p3" class="ltx_para">
<p id="S4.SS1.p3.1" class="ltx_p"><span id="S4.SS1.p3.1.1" class="ltx_text">(b) Differentiating $G_{B}(w)=g(ws)/p$ at $w=1$ gives $b=sD_{1}/p\text{,}$ so $b/\mu=qsD_{1}/(1-p)\text{.}$ The first equality follows from the definition of $\alpha\text{.}$</span></p>
</div>
<div id="S4.SS1.p4" class="ltx_para">
<p id="S4.SS1.p4.1" class="ltx_p"><span id="S4.SS1.p4.1.1" class="ltx_text">(c) Set $Y=s^{T_{0}}\in(0,1]\text{,}$ so $p=E[Y]$ and $qsD_{1}=qE[-Y\ln Y]/|\ln s|\text{.}$ Since $\varphi(x)=-x\ln x$ is concave, Jensen gives $E[-Y\ln Y]\leq-p\ln p\text{,}$ whence $qsD_{1}=O_{q}(p|\ln p|)\text{.}$ Both terms in $\alpha=(sp-qsD_{1})/(1-p)$ are therefore $O_{q}(p|\ln p|)\text{.}$
∎</span></p>
</div>
</div>
<div id="S4.SS1.p5" class="ltx_para">
<p id="S4.SS1.p5.1" class="ltx_p">Identity (a) is the Laplace-domain restatement of the coefficient equality (<a href="#S2.E10" title="In Proposition 2.5 (Affine structure and coefficient equality). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">10</span></a>): both arise from $s+q=1\text{.}$ Its consequence is that the first-order error in the exponential approximation vanishes exactly (Theorem <a href="#S4.Thmtheorem4" title="Theorem 4.4 (Laplace expansion). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.4</span></a>).</p>
</div>
<div id="S4.Thmtheorem3" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem3.2" class="ltx_text ltx_font_italic">Remark 4.3</span></span><span id="S4.Thmtheorem3.3" class="ltx_text ltx_font_italic"> </span>(Interpretation of $\alpha$)<span id="S4.Thmtheorem3.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S4.Thmtheorem3.p1" class="ltx_para">
<p id="S4.Thmtheorem3.p1.1" class="ltx_p">Identity (b) shows that $\alpha$ measures the deviation of the successful attempt from a “geometric target”: $\alpha=sp/(1-p)-b/\mu\text{.}$ If $\alpha=0\text{,}$ the rescaled successful attempt $B/\mu$ has exactly the expected length one would predict from a pure geometric model; if $\alpha\neq 0\text{,}$ $B$ is longer (when $\alpha&lt;0$) or shorter (when $\alpha&gt;0$) than this target. As we shall see, the Kolmogorov distance decomposes into two independent error sources: a lattice error $\Theta(p)$ from the integrality of the attempt count, and a perturbation error $\Theta(|\alpha|)$ from this mismatch.</p>
</div>
</div>
</section>
<section id="S4.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-laplace-expansion"><span class="ltx_tag ltx_tag_subsection">4.2 </span>The Laplace Expansion</h3>

<div id="S4.Thmtheorem4" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem4.2" class="ltx_text ltx_font_bold">Theorem 4.4</span></span><span id="S4.Thmtheorem4.3" class="ltx_text ltx_font_bold"> </span>(Laplace expansion)<span id="S4.Thmtheorem4.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem4.p1" class="ltx_para">
<p id="S4.Thmtheorem4.p1.1" class="ltx_p"><span id="S4.Thmtheorem4.p1.1.1" class="ltx_text ltx_font_italic">Fix $q\in(0,1)\text{.}$ There exist $p_{0}(q),\epsilon_{0}(q)&gt;0$ such that for all $p\leq p_{0}$ and $\theta&gt;0$ satisfying $\epsilon:=\theta pq/(1-p)\leq\epsilon_{0}\text{,}$</span></p>
<table id="S4.E27" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[e^{-\theta W}]-\frac{1}{1+\theta}=\frac{\alpha\,\theta^{2}}{(1+\theta)^{2}}+O\!\left(\frac{|\alpha|^{2}\,\theta^{3}}{(1+\theta)^{3}}\right)+O\!\left(\frac{p\,\theta^{2}}{1+\theta}\right),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(27)</span></td></tr></tbody>
</table>
<p id="S4.Thmtheorem4.p1.2" class="ltx_p"><span id="S4.Thmtheorem4.p1.2.1" class="ltx_text ltx_font_italic">with implicit constants depending only on $q\text{.}$</span></p>
</div>
</div>
<div id="S4.SS2.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS2.p1" class="ltx_para">
<p id="S4.SS2.p1.1" class="ltx_p"><span id="S4.SS2.p1.1.1" class="ltx_text">Set $\epsilon=\theta/\mu=\theta pq/(1-p)$ and $w=e^{-\epsilon}\text{.}$ Then $E[e^{-\theta W}]=G_{T}(w)\text{.}$ We expand the numerator $N(w)$ and denominator $D(w)$ of (<a href="#S2.E9" title="In Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a>) around $w=1\text{.}$</span></p>
</div>
<div id="S4.SS2.p2" class="ltx_para">
<p id="S4.SS2.p2.1" class="ltx_p"><span id="S4.SS2.p2.1.1" class="ltx_text">Using $w=1-\epsilon+O(\epsilon^{2})\text{,}$ $u=ws=s-s\epsilon+O(\epsilon^{2})\text{,}$ and $g(u)=p-sD_{1}\epsilon+O(\epsilon^{2})\text{:}$</span></p>
</div>
<div id="S4.SS2.p3" class="ltx_para">
<p id="S4.SS2.p3.1" class="ltx_p"><em id="S4.SS2.p3.1.1" class="ltx_emph ltx_font_italic">Numerator.</em><span id="S4.SS2.p3.1.2" class="ltx_text">  $g(u)(1-u)=(p-sD_{1}\epsilon+O(\epsilon^{2}))(q+s\epsilon+O(\epsilon^{2}))=pq+(ps-qsD_{1})\epsilon+O(\epsilon^{2})\text{.}$</span></p>
</div>
<div id="S4.SS2.p4" class="ltx_para">
<p id="S4.SS2.p4.1" class="ltx_p"><em id="S4.SS2.p4.1.1" class="ltx_emph ltx_font_italic">Denominator.</em><span id="S4.SS2.p4.1.2" class="ltx_text">  $1-w+qwg(u)=\epsilon+O(\epsilon^{2})+q(1-\epsilon+O(\epsilon^{2}))(p-sD_{1}\epsilon+O(\epsilon^{2}))=qp+(1-qp-qsD_{1})\epsilon+O(\epsilon^{2})\text{.}$</span></p>
</div>
<div id="S4.SS2.p5" class="ltx_para">
<p id="S4.SS2.p5.1" class="ltx_p"><span id="S4.SS2.p5.1.1" class="ltx_text">Dividing both by $pq$ and substituting $\epsilon=\theta pq/(1-p)\text{:}$</span></p>
<table id="S4.E28" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{T}(w)=\frac{1+\alpha\theta+R_{N}(\theta)}{1+\beta\theta+R_{D}(\theta)},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(28)</span></td></tr></tbody>
</table>
<p id="S4.SS2.p5.2" class="ltx_p"><span id="S4.SS2.p5.2.1" class="ltx_text">where $|R_{N}|,|R_{D}|=O(\theta^{2}p)$ (with implicit constants bounded for fixed $q\text{,}$ since $s^{k}D_{k}\leq\max_{t\geq 1}t^{k}s^{t}=(k/(e|\ln s|))^{k}$).</span></p>
</div>
<div id="S4.SS2.p6" class="ltx_para">
<p id="S4.SS2.p6.1" class="ltx_p"><span id="S4.SS2.p6.1.1" class="ltx_text">By Proposition <a href="#S4.Thmtheorem2" title="Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a> (<a href="#S4.I2.i1" title="item a ‣ Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">a</span></a>), $\beta=1+\alpha\text{.}$ Computing:</span></p>
<table id="S4.Ex21" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{1+\alpha\theta}{1+\beta\theta}-\frac{1}{1+\theta}=\frac{(1+\alpha-\beta)\theta+\alpha\theta^{2}}{(1+\beta\theta)(1+\theta)}=\frac{\alpha\theta^{2}}{(1+\beta\theta)(1+\theta)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.SS2.p6.2" class="ltx_p"><span id="S4.SS2.p6.2.1" class="ltx_text">Since $\beta=1+\alpha\text{:}$ $1/(1+\beta\theta)=1/((1+\theta)(1+\alpha\theta/(1+\theta)))\text{,}$ giving</span></p>
<table id="S4.Ex22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{\alpha\theta^{2}}{(1+\beta\theta)(1+\theta)}=\frac{\alpha\theta^{2}}{(1+\theta)^{2}}+O\!\left(\frac{|\alpha|^{2}\theta^{3}}{(1+\theta)^{3}}\right).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S4.SS2.p7" class="ltx_para">
<p id="S4.SS2.p7.1" class="ltx_p"><span id="S4.SS2.p7.1.1" class="ltx_text">It remains to bound the contribution of the remainders $R_{N},R_{D}$ to the ratio (<a href="#S4.E28" title="In Proof. ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">28</span></a>). Writing $G_{T}(w)-1/(1+\theta)$ and using $1+\alpha-\beta=0\text{,}$ the numerator becomes $\alpha\theta^{2}+(1+\theta)R_{N}-R_{D}\text{.}$ For the denominator: $1+\beta\theta+R_{D}=(1+\theta)(1+\alpha\theta/(1+\theta)+R_{D}/(1+\theta))\text{.}$ Taking $p_{0}$ small enough that $|\alpha|\leq 1/4$ and $\epsilon_{0}\leq q/4\text{,}$ the parenthetical factor is at least $1/2\text{,}$ so $|1+\beta\theta+R_{D}|\geq(1+\theta)/2\text{.}$ The numerator remainder satisfies $|(1+\theta)R_{N}-R_{D}|=O((1+\theta)\theta^{2}p)\text{,}$ giving a contribution $O(p\theta^{2}/(1+\theta))\text{.}$
∎</span></p>
</div>
</div>
<div id="S4.Thmtheorem5" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem5.2" class="ltx_text ltx_font_italic">Remark 4.5</span></span><span id="S4.Thmtheorem5.3" class="ltx_text ltx_font_italic"> </span>(Algebraic origin of the $\theta^{1}$ cancellation)<span id="S4.Thmtheorem5.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S4.Thmtheorem5.p1" class="ltx_para">
<p id="S4.Thmtheorem5.p1.1" class="ltx_p">The identity $1+\alpha-\beta=0$ is equivalent to $E[W]=1$ (matching first moments). Its algebraic root is $s+q=1\text{,}$ the same identity underlying the coefficient equality $\alpha_{N}(1)=\alpha_{D}(1)$ that drives the DRP. This is an exact algebraic identity, not an asymptotic cancellation—a structural guarantee that the exponential approximation begins at second order for any base process.</p>
</div>
</div>
<div id="S4.Thmtheorem6" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem6.2" class="ltx_text ltx_font_bold">Corollary 4.6</span></span><span id="S4.Thmtheorem6.3" class="ltx_text ltx_font_bold"> </span>(Exponential limit)<span id="S4.Thmtheorem6.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem6.p1" class="ltx_para">
<p id="S4.Thmtheorem6.p1.1" class="ltx_p"><span id="S4.Thmtheorem6.p1.1.1" class="ltx_text ltx_font_italic">Fix $q\in(0,1)\text{.}$ Under memoryless catastrophe with rate $q\text{,}$ $T/E[T]\xrightarrow{d}\operatorname{Exp}(1)$ as $p=g(s)\to 0\text{.}$</span></p>
</div>
</div>
<div id="S4.SS2.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS2.p8" class="ltx_para">
<p id="S4.SS2.p8.1" class="ltx_p"><span id="S4.SS2.p8.1.1" class="ltx_text">By Proposition <a href="#S4.Thmtheorem2" title="Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a> (<a href="#S4.I2.i3" title="item c ‣ Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">c</span></a>), $|\alpha|\to 0\text{.}$ For each fixed $\theta&gt;0\text{,}$ the condition $\epsilon=\theta pq/(1-p)\leq\epsilon_{0}$ is eventually satisfied, and both error terms in (<a href="#S4.E27" title="In Theorem 4.4 (Laplace expansion). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">27</span></a>) vanish. Hence $E[e^{-\theta W}]\to 1/(1+\theta)$ pointwise. Pointwise convergence of Laplace transforms on $(0,\infty)$ implies convergence in distribution <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib21" title="" class="ltx_ref">21</a>]</cite>.
∎</span></p>
</div>
</div>
<div id="S4.Thmtheorem7" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem7.2" class="ltx_text ltx_font_italic">Remark 4.7</span></span><span id="S4.Thmtheorem7.3" class="ltx_text ltx_font_italic"> </span>(Variable $q$ regime)<span id="S4.Thmtheorem7.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S4.Thmtheorem7.p1" class="ltx_para">
<p id="S4.Thmtheorem7.p1.1" class="ltx_p">Corollary <a href="#S4.Thmtheorem6" title="Corollary 4.6 (Exponential limit). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.6</span></a> assumes fixed $q\text{.}$ When $q\to 0$ simultaneously with $p\to 0$ (as in the CCP, where $q=m/(n+m)\to 0$), the implicit constants in (<a href="#S4.E27" title="In Theorem 4.4 (Laplace expansion). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">27</span></a>) may deteriorate. The convergence $T/E[T]\xrightarrow{d}\operatorname{Exp}(1)$ in such regimes follows instead from the Bridge Theorem below (Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a>), which requires only $p\to 0$ and uniform control of certain moment ratios of $A\text{.}$</p>
</div>
</div>
</section>
<section id="S4.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-bridge-theorem"><span class="ltx_tag ltx_tag_subsection">4.3 </span>The Bridge Theorem</h3>

<div id="S4.SS3.p1" class="ltx_para">
<p id="S4.SS3.p1.1" class="ltx_p">The Laplace expansion (Theorem <a href="#S4.Thmtheorem4" title="Theorem 4.4 (Laplace expansion). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.4</span></a>) gives pointwise control on the Laplace transform error. Converting to Kolmogorov distance $d_{\mathrm{K}}$ via the smoothing inequality (<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib25" title="" class="ltx_ref">25</a>]</cite>) yields</p>
<table id="S4.Ex23" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}\lesssim\int_{0}^{R}\frac{|\alpha|\theta}{(1+\theta)^{2}}\,d\theta+\frac{1}{R},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.SS3.p1.2" class="ltx_p">which evaluates to $O(|\alpha|\ln(1/|\alpha|))$ upon optimizing $R\text{.}$ The logarithmic factor arises because the integrand decays only as $|\alpha|/\theta$ for large $\theta\text{,}$ accumulating a logarithmic contribution absent from the pointwise bound.</p>
</div>
<div id="S4.SS3.p2" class="ltx_para">
<p id="S4.SS3.p2.1" class="ltx_p">We now develop a direct probabilistic approach that avoids this loss entirely. The key idea is to decompose the approximation into three steps, each handling one component of $W=U/\mu+B/\mu\text{.}$</p>
</div>
<div id="S4.Thmtheorem8" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem8.2" class="ltx_text ltx_font_bold">Lemma 4.8</span></span><span id="S4.Thmtheorem8.3" class="ltx_text ltx_font_bold"> </span>(Failed-attempt tail bound)<span id="S4.Thmtheorem8.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem8.p1" class="ltx_para">
<p id="S4.Thmtheorem8.p1.1" class="ltx_p"><span id="S4.Thmtheorem8.p1.1.1" class="ltx_text ltx_font_italic">Under memoryless catastrophe with rate $q\text{,}$ the failed-attempt length satisfies $P(A\geq t)\leq s^{t-1}$ for all $t\geq 1\text{.}$</span></p>
</div>
</div>
<div id="S4.SS3.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p3" class="ltx_para">
<p id="S4.SS3.p3.1" class="ltx_p"><span id="S4.SS3.p3.1.1" class="ltx_text">A failure at step $j$ requires survival through steps $1,\ldots,j-1$ (probability $s^{j-1}$), catastrophe at step $j$ (probability $q$), and $T_{0}\geq j\text{.}$ Hence</span></p>
<table id="S4.Ex24" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$P(A\geq t)=\frac{\sum_{j\geq t}q\,s^{j-1}P(T_{0}\geq j)}{1-p}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.SS3.p3.2" class="ltx_p"><span id="S4.SS3.p3.2.1" class="ltx_text">Factoring $s^{t-1}$ and using $P(T_{0}\geq t+k)\leq P(T_{0}\geq k+1)\text{:}$ the numerator is at most $s^{t-1}\sum_{k\geq 0}q\,s^{k}P(T_{0}\geq k+1)=s^{t-1}(1-p)\text{.}$
∎</span></p>
</div>
</div>
<div id="S4.Thmtheorem9" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem9.2" class="ltx_text ltx_font_bold">Lemma 4.9</span></span><span id="S4.Thmtheorem9.3" class="ltx_text ltx_font_bold"> </span>(Uniform moment-ratio control)<span id="S4.Thmtheorem9.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem9.p1" class="ltx_para">
<p id="S4.Thmtheorem9.p1.1" class="ltx_p"><span id="S4.Thmtheorem9.p1.1.1" class="ltx_text ltx_font_italic">Fix $q\in(0,1)\text{.}$ For any base process $T_{0}$ and any integer $k\geq 1\text{,}$</span></p>
<table id="S4.Ex25" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[A^{k}]\leq M_{k}(q):=\sum_{t\geq 1}k\,t^{k-1}\,s^{t-1}&lt;\infty,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.Thmtheorem9.p1.2" class="ltx_p"><span id="S4.Thmtheorem9.p1.2.1" class="ltx_text ltx_font_italic">and $E[A]\geq 1\text{.}$ Hence all moment ratios $E[A^{k}]/E[A]^{k}$ are bounded by constants depending only on $q\text{.}$</span></p>
</div>
</div>
<div id="S4.SS3.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p4" class="ltx_para">
<p id="S4.SS3.p4.1" class="ltx_p"><span id="S4.SS3.p4.1.1" class="ltx_text">The tail-sum formula $E[A^{k}]=\sum_{t\geq 1}[t^{k}-(t-1)^{k}]P(A\geq t)\text{,}$ combined with the mean value theorem bound $t^{k}-(t-1)^{k}\leq kt^{k-1}$ and Lemma <a href="#S4.Thmtheorem8" title="Lemma 4.8 (Failed-attempt tail bound). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.8</span></a>, gives $E[A^{k}]\leq\sum_{t\geq 1}kt^{k-1}s^{t-1}&lt;\infty\text{.}$ The bound $E[A]\geq 1$ is immediate since $A\geq 1\text{.}$
∎</span></p>
</div>
</div>
<div id="S4.Thmtheorem10" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem10.2" class="ltx_text ltx_font_bold">Lemma 4.10</span></span><span id="S4.Thmtheorem10.3" class="ltx_text ltx_font_bold"> </span>(Scaling perturbation)<span id="S4.Thmtheorem10.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem10.p1" class="ltx_para">
<p id="S4.Thmtheorem10.p1.1" class="ltx_p"><span id="S4.Thmtheorem10.p1.1.1" class="ltx_text ltx_font_italic">For any non-negative random variable $X$ and $r\in(0,1)\text{,}$</span></p>
<table id="S4.Ex26" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}(rX,\operatorname{Exp}(1))\leq d_{\mathrm{K}}(X,\operatorname{Exp}(1))+(1-r).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4.SS3.4" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p5" class="ltx_para">
<p id="S4.SS3.p5.1" class="ltx_p"><span id="S4.SS3.p5.1.1" class="ltx_text">Set $\varepsilon=d_{\mathrm{K}}(X,\operatorname{Exp}(1))$ and $F_{E}(x)=1-e^{-x}\text{.}$ For all $x\geq 0\text{:}$</span></p>
<table id="S4.Ex27" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$|P(rX\leq x)-F_{E}(x)|\leq\underbrace{|P(X\leq x/r)-F_{E}(x/r)|}_{\leq\,\varepsilon}+\underbrace{|F_{E}(x/r)-F_{E}(x)|}_{=\,e^{-x}-e^{-x/r}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.SS3.p5.2" class="ltx_p"><span id="S4.SS3.p5.2.1" class="ltx_text">The second term is non-negative (since $r&lt;1$) and maximized at $x^{*}=r\ln(1/r)/(1-r)\text{,}$ where it equals $(1-r)r^{r/(1-r)}\leq 1-r\text{.}$
∎</span></p>
</div>
</div>
<div id="S4.Thmtheorem11" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem11.2" class="ltx_text ltx_font_bold">Lemma 4.11</span></span><span id="S4.Thmtheorem11.3" class="ltx_text ltx_font_bold"> </span>(Additive perturbation)<span id="S4.Thmtheorem11.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem11.p1" class="ltx_para">
<p id="S4.Thmtheorem11.p1.1" class="ltx_p"><span id="S4.Thmtheorem11.p1.1.1" class="ltx_text ltx_font_italic">Let $X\geq 0$ and $Y\geq 0$ be independent. Then</span></p>
<table id="S4.Ex28" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}(X+Y,\operatorname{Exp}(1))\leq d_{\mathrm{K}}(X,\operatorname{Exp}(1))+E[Y].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4.SS3.5" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p6" class="ltx_para">
<p id="S4.SS3.p6.1" class="ltx_p"><span id="S4.SS3.p6.1.1" class="ltx_text">Set $\varepsilon=d_{\mathrm{K}}(X,\operatorname{Exp}(1))$ and $F_{E}(x)=1-e^{-x}\text{.}$</span></p>
</div>
<div id="S4.SS3.p7" class="ltx_para">
<p id="S4.SS3.p7.1" class="ltx_p"><em id="S4.SS3.p7.1.1" class="ltx_emph ltx_font_italic">Upper bound.</em><span id="S4.SS3.p7.1.2" class="ltx_text">  Since $Y\geq 0\text{,}$ $P(X+Y\leq x)\leq P(X\leq x)\leq F_{E}(x)+\varepsilon\text{.}$</span></p>
</div>
<div id="S4.SS3.p8" class="ltx_para">
<p id="S4.SS3.p8.1" class="ltx_p"><em id="S4.SS3.p8.1.1" class="ltx_emph ltx_font_italic">Lower bound.</em><span id="S4.SS3.p8.1.2" class="ltx_text">  We must show $F_{E}(x)-P(X+Y\leq x)\leq E[Y]+\varepsilon\text{.}$ Conditioning on $Y\text{:}$</span></p>
<table id="S4.Ex29" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$F_{E}(x)-P(X+Y\leq x)=E\bigl[\bigl(F_{E}(x)-F_{X}(x-Y)\bigr)\mathbf{1}_{\{Y\leq x\}}\bigr]+F_{E}(x)\,P(Y&gt;x).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S4.SS3.p8.2" class="ltx_p"><span id="S4.SS3.p8.2.1" class="ltx_text">For the first term, when $Y\leq x\text{,}$ $F_{E}(x)-F_{X}(x-Y)\leq\bigl[F_{E}(x)-F_{E}(x-Y)\bigr]+\varepsilon\leq Y+\varepsilon\text{,}$ using $|F_{E}^{\prime}|\leq 1\text{.}$ For the second term, $F_{E}(x)\,P(Y&gt;x)\leq xP(Y&gt;x)\leq E[Y\cdot\mathbf{1}_{\{Y&gt;x\}}]\text{.}$ Combining them gives</span></p>
<table id="S4.Ex30" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$F_{E}(x)-P(X+Y\leq x)\leq E[Y]+\varepsilon.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4.SS3.p9" class="ltx_para">
<p id="S4.SS3.p9.1" class="ltx_p">Rényi’s classical theorem (<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib36" title="" class="ltx_ref">36</a>]</cite>) asserts that normalized geometric sums converge in distribution to $\operatorname{Exp}(1)\text{.}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib6" title="" class="ltx_ref">6</a>]</cite> established the first explicit Kolmogorov-distance bound, showing that the rate is linear in the geometric parameter $p\text{.}$</p>
</div>
<div id="S4.Thmtheorem12" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem12.2" class="ltx_text ltx_font_bold">Theorem 4.12</span></span><span id="S4.Thmtheorem12.3" class="ltx_text ltx_font_bold"> </span>(Theorem 2.1 (ii), <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib6" title="" class="ltx_ref">6</a>]</cite>)<span id="S4.Thmtheorem12.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem12.p1" class="ltx_para">
<p id="S4.Thmtheorem12.p1.1" class="ltx_p"><span id="S4.Thmtheorem12.p1.1.1" class="ltx_text ltx_font_italic">Let $U=\sum_{i=1}^{N}X_{i}\text{,}$ $N\sim\operatorname{Geom}_{0}(p)\text{,}$ where $0&lt;p&lt;1\text{,}$ the $X_{i}$ are i.i.d. nonnegative random variables, $P(X_{1}=0)&lt;1\text{,}$ and $E[X_{1}^{2}]&lt;\infty\text{.}$ Set $\bar{p}:=1-p\text{,}$
$\rho_{2}:=\frac{E[X_{1}^{2}]}{E[X_{1}]^{2}}\text{.}$
Then</span></p>
<table id="S4.E29" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{K}\!\left(\frac{U}{E[U]},\,\operatorname{Exp}(1)\right)\leq p\max\!\left(\rho_{2},\frac{\rho_{2}}{2\bar{p}}\right).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(29)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S4.SS3.p10" class="ltx_para">
<p id="S4.SS3.p10.1" class="ltx_p">We can now state and prove the Bridge Theorem. The name reflects its role: it bridges the $O(p)$ exponential approximation of the pure geometric sum $U/\mu_{U}$ to the full completion time $W=T/\mu\text{.}$</p>
</div>
<div id="S4.Thmtheorem13" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem13.2" class="ltx_text ltx_font_bold">Theorem 4.13</span></span><span id="S4.Thmtheorem13.3" class="ltx_text ltx_font_bold"> </span>(Bridge Theorem)<span id="S4.Thmtheorem13.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem13.p1" class="ltx_para">
<p id="S4.Thmtheorem13.p1.1" class="ltx_p"><span id="S4.Thmtheorem13.p1.1.1" class="ltx_text ltx_font_italic">For $0&lt;p\leq 1/2\text{,}$</span></p>
<table id="S4.E30" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}(W,\operatorname{Exp}(1))\leq C_{1}\,p+2\,\frac{b}{\mu},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(30)</span></td></tr></tbody>
</table>
<p id="S4.Thmtheorem13.p1.2" class="ltx_p"><span id="S4.Thmtheorem13.p1.2.1" class="ltx_text ltx_font_italic">where $C_{1}&lt;\infty$ depends only on the distribution of $A$ (and is uniformly bounded over all base processes $T_{0}$ for fixed $q\text{,}$ by Lemma <a href="#S4.Thmtheorem9" title="Lemma 4.9 (Uniform moment-ratio control). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.9</span></a>).</span></p>
</div>
</div>
<div id="S4.SS3.6" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p11" class="ltx_para">
<p id="S4.SS3.p11.1" class="ltx_p"><span id="S4.SS3.p11.1.1" class="ltx_text">Set $\mu_{U}=E[U]=(1-p)E[A]/p$ and $r=\mu_{U}/\mu=1-b/\mu\in(0,1)\text{.}$</span></p>
</div>
<div id="S4.SS3.p12" class="ltx_para">
<p id="S4.SS3.p12.1" class="ltx_p"><em id="S4.SS3.p12.1.1" class="ltx_emph ltx_font_italic">Step 1: Geometric-convolution bound for $V=U/\mu_{U}\text{.}$</em><span id="S4.SS3.p12.1.2" class="ltx_text"> 
By Lemma <a href="#S4.Thmtheorem9" title="Lemma 4.9 (Uniform moment-ratio control). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.9</span></a>, $E[A^{k}]\leq M_{k}(q)&lt;\infty$ for all $k\geq 1\text{,}$ so Brown’s moment condition $E[A^{2}]&lt;\infty$ is satisfied and the moment ratios $\rho_{j}=E[A^{j}]/E[A]^{j}\leq M_{j}(q)/1=M_{j}(q)$ are uniformly bounded. Theorem <a href="#S4.Thmtheorem12" title="Theorem 4.12 (Theorem 2.1 (ii), []). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.12</span></a> applied with $X_{i}=A_{i}$ gives $d_{\mathrm{K}}(V,\operatorname{Exp}(1))\leq\rho_{2}(A)\,p\text{.}$ Since $\rho_{2}(A)=E[A^{2}]/E[A]^{2}\leq M_{2}(q)$ by Lemma <a href="#S4.Thmtheorem9" title="Lemma 4.9 (Uniform moment-ratio control). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.9</span></a>,
we may take $C_{1}=M_{2}(q)\text{,}$ and hence
$d_{\mathrm{K}}(V,\operatorname{Exp}(1))\leq C_{1}p\text{.}$</span></p>
</div>
<div id="S4.SS3.p13" class="ltx_para">
<p id="S4.SS3.p13.1" class="ltx_p"><em id="S4.SS3.p13.1.1" class="ltx_emph ltx_font_italic">Step 2: Scaling perturbation.</em><span id="S4.SS3.p13.1.2" class="ltx_text"> 
Since $U/\mu=rV$ with $r=1-b/\mu\text{,}$ Lemma <a href="#S4.Thmtheorem10" title="Lemma 4.10 (Scaling perturbation). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.10</span></a> gives $d_{\mathrm{K}}(U/\mu,\operatorname{Exp}(1))\leq C_{1}p+b/\mu\text{.}$</span></p>
</div>
<div id="S4.SS3.p14" class="ltx_para">
<p id="S4.SS3.p14.1" class="ltx_p"><em id="S4.SS3.p14.1.1" class="ltx_emph ltx_font_italic">Step 3: Additive perturbation.</em><span id="S4.SS3.p14.1.2" class="ltx_text"> 
Since $W=U/\mu+B/\mu$ and $U,B$ are independent (by mutual independence of $N\text{,}$ $(A_{i})\text{,}$ $B$ in (<a href="#S2.E6" title="In 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>)), Lemma <a href="#S4.Thmtheorem11" title="Lemma 4.11 (Additive perturbation). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.11</span></a> gives $d_{\mathrm{K}}(W,\operatorname{Exp}(1))\leq C_{1}p+b/\mu+E[B/\mu]=C_{1}p+2b/\mu\text{.}$ ∎</span></p>
</div>
</div>
<div id="S4.Thmtheorem14" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem14.2" class="ltx_text ltx_font_italic">Remark 4.14</span></span><span id="S4.Thmtheorem14.3" class="ltx_text ltx_font_italic"> </span>(Connection to the staircase)<span id="S4.Thmtheorem14.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S4.Thmtheorem14.p1" class="ltx_para">
<p id="S4.Thmtheorem14.p1.1" class="ltx_p">The explicit correction terms in the Bridge Theorem—$p=g(s)$ and $b/\mu=qsD_{1}/(1-p)$—involve only the $1$-jet $\{g(s),g^{\prime}(s)\}\text{,}$ matching the staircase level of $\operatorname{Var}(T)$ (<a href="#S2.E17" title="In Example 2.9 (First two moments). ‣ 2.3 Moment Recursion and the Complexity Staircase ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">17</span></a>). The Brown constant $C_{1}$ depends on the full distribution of $A$ (via moment ratios), so this staircase connection is more heuristic than exact.</p>
</div>
</div>
</section>
<section id="S4.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-sharp-two-sided-bound"><span class="ltx_tag ltx_tag_subsection">4.4 </span>The Sharp Two-Sided Bound</h3>

<div id="S4.SS4.p1" class="ltx_para">
<p id="S4.SS4.p1.1" class="ltx_p">We now combine the Laplace expansion (Theorem <a href="#S4.Thmtheorem4" title="Theorem 4.4 (Laplace expansion). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.4</span></a>) and the Bridge Theorem (Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a>) to obtain a sharp two-sided bound showing that $p+|\alpha|$ is the correct rate.</p>
</div>
<div id="S4.Thmtheorem15" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem15.2" class="ltx_text ltx_font_bold">Theorem 4.15</span></span><span id="S4.Thmtheorem15.3" class="ltx_text ltx_font_bold"> </span>(Two-sided bound)<span id="S4.Thmtheorem15.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem15.p1" class="ltx_para">
<p id="S4.Thmtheorem15.p1.1" class="ltx_p"><span id="S4.Thmtheorem15.p1.1.1" class="ltx_text ltx_font_italic">There exist constants $c_{A},C_{A},\delta_{A}&gt;0$ depending only on $q$ such that, for $p+|\alpha|\leq\delta_{A}\text{,}$</span></p>
<table id="S4.E31" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$c_{A}\,(p+|\alpha|)\leq d_{\mathrm{K}}\!\left(\frac{T}{E[T]},\,\operatorname{Exp}(1)\right)\leq C_{A}\,(p+|\alpha|).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(31)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S4.SS4.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of the upper bound.</h6>
<div id="S4.SS4.p2" class="ltx_para">
<p id="S4.SS4.p2.1" class="ltx_p"><span id="S4.SS4.p2.1.1" class="ltx_text">From Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a> and Proposition <a href="#S4.Thmtheorem2" title="Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a> (<a href="#S4.I2.i2" title="item b ‣ Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">b</span></a>): when $\alpha\leq 0\text{,}$ $b/\mu=|\alpha|+sp/(1-p)\text{;}$ when $\alpha&gt;0\text{,}$ $b/\mu=sp/(1-p)-\alpha\leq sp/(1-p)\text{.}$ In both cases, $2b/\mu\leq 2|\alpha|+2sp/(1-p)\text{.}$ Hence</span></p>
<table id="S4.Ex31" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}\leq C_{1}p+2|\alpha|+\frac{2sp}{1-p}\leq C_{A}(p+|\alpha|).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S4.SS4.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of the lower bound.</h6>
<div id="S4.SS4.p3" class="ltx_para">
<p id="S4.SS4.p3.1" class="ltx_p"><span id="S4.SS4.p3.1.1" class="ltx_text">We exhibit two independent error sources, each yielding a lower bound.</span></p>
</div>
<div id="S4.SS4.p4" class="ltx_para">
<p id="S4.SS4.p4.1" class="ltx_p"><em id="S4.SS4.p4.1.1" class="ltx_emph ltx_font_italic">Lower bound from discreteness.</em><span id="S4.SS4.p4.1.2" class="ltx_text"> 
Since $T\geq 1\text{,}$ $W=T/\mu\geq 1/\mu=pq/(1-p)\text{.}$ For $x=pq/(2(1-p))&lt;1/\mu\text{:}$ $P(W\leq x)=0\text{,}$ while $F_{E}(x)=1-e^{-x}\geq x/2=pq/(4(1-p))$ (using $1-e^{-t}\geq t/2$ for $t\in[0,1]$). Hence</span></p>
<table id="S4.E32" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}\geq\frac{pq}{4(1-p)}=\Omega(p).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(32)</span></td></tr></tbody>
</table>
</div>
<div id="S4.SS4.p5" class="ltx_para">
<p id="S4.SS4.p5.1" class="ltx_p"><em id="S4.SS4.p5.1.1" class="ltx_emph ltx_font_italic">Lower bound from the Laplace transform.</em><span id="S4.SS4.p5.1.2" class="ltx_text"> 
For any non-negative random variables $W,Z$ and any $\theta&gt;0\text{,}$ the integral representation $E[e^{-\theta X}]=\int_{0}^{\infty}\theta e^{-\theta x}(1-F_{X}(x))\,dx$ gives</span></p>
<table id="S4.E33" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}(W,Z)\geq|E[e^{-\theta W}]-E[e^{-\theta Z}]|.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(33)</span></td></tr></tbody>
</table>
<p id="S4.SS4.p5.2" class="ltx_p"><span id="S4.SS4.p5.2.1" class="ltx_text">Applying (<a href="#S4.E33" title="In Proof of the lower bound. ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">33</span></a>) with $Z\sim\operatorname{Exp}(1)$ and $\theta=1\text{:}$ for $p$ sufficiently small, Theorem <a href="#S4.Thmtheorem4" title="Theorem 4.4 (Laplace expansion). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.4</span></a> gives $|E[e^{-W}]-1/2|=|\alpha|/4+O(|\alpha|^{2})+O(p)\text{,}$ so</span></p>
<table id="S4.E34" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}\geq\frac{|\alpha|}{4}-O(|\alpha|^{2})-O(p)\geq c^{\prime}|\alpha|-c^{\prime\prime}p$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(34)</span></td></tr></tbody>
</table>
<p id="S4.SS4.p5.3" class="ltx_p"><span id="S4.SS4.p5.3.1" class="ltx_text">for suitable $c^{\prime},c^{\prime\prime}&gt;0\text{.}$</span></p>
</div>
<div id="S4.SS4.p6" class="ltx_para">
<p id="S4.SS4.p6.1" class="ltx_p"><em id="S4.SS4.p6.1.1" class="ltx_emph ltx_font_italic">Combining.</em><span id="S4.SS4.p6.1.2" class="ltx_text"> 
Set $K=2c^{\prime\prime}/c^{\prime}\text{.}$ Choose $\delta_{A}$ small enough that both (<a href="#S4.E32" title="In Proof of the lower bound. ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">32</span></a>) and (<a href="#S4.E34" title="In Proof of the lower bound. ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">34</span></a>) hold.</span></p>
</div>
<div id="S4.SS4.p7" class="ltx_para">
<p id="S4.SS4.p7.1" class="ltx_p"><em id="S4.SS4.p7.1.1" class="ltx_emph ltx_font_italic">Case 1</em><span id="S4.SS4.p7.1.2" class="ltx_text">: $|\alpha|\leq Kp\text{.}$ Then $p+|\alpha|\leq(1+K)p\text{.}$ From (<a href="#S4.E32" title="In Proof of the lower bound. ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">32</span></a>), $d_{\mathrm{K}}\geq qp/4\geq q(p+|\alpha|)/(4(1+K))\text{.}$</span></p>
</div>
<div id="S4.SS4.p8" class="ltx_para">
<p id="S4.SS4.p8.1" class="ltx_p"><em id="S4.SS4.p8.1.1" class="ltx_emph ltx_font_italic">Case 2</em><span id="S4.SS4.p8.1.2" class="ltx_text">: $|\alpha|&gt;Kp\text{.}$ Then $p+|\alpha|\leq(1+1/K)|\alpha|\text{.}$ From (<a href="#S4.E34" title="In Proof of the lower bound. ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">34</span></a>), $d_{\mathrm{K}}\geq c^{\prime}|\alpha|/2\geq c^{\prime}K(p+|\alpha|)/(2(K+1))\text{.}$</span></p>
</div>
<div id="S4.SS4.p9" class="ltx_para">
<p id="S4.SS4.p9.1" class="ltx_p"><span id="S4.SS4.p9.1.1" class="ltx_text">In both cases, $d_{\mathrm{K}}\geq c_{A}(p+|\alpha|)$ with $c_{A}=\min\{q/(4(1+K)),\;c^{\prime}K/(2(K+1))\}&gt;0\text{.}$
∎</span></p>
</div>
</div>
<div id="S4.SS4.p10" class="ltx_para">
<p id="S4.SS4.p10.1" class="ltx_p">The following counterexample shows that the $p$-term in the template $p+|\alpha|$ cannot be dropped.</p>
</div>
<div id="S4.Thmtheorem16" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem16.2" class="ltx_text ltx_font_bold">Proposition 4.16</span></span><span id="S4.Thmtheorem16.3" class="ltx_text ltx_font_bold"> </span>(Counterexample: $p$ cannot be dropped)<span id="S4.Thmtheorem16.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S4.Thmtheorem16.p1" class="ltx_para">
<p id="S4.Thmtheorem16.p1.1" class="ltx_p"><span id="S4.Thmtheorem16.p1.1.1" class="ltx_text ltx_font_italic">There exists a family of base processes $(T_{0}^{(\varepsilon)})_{\varepsilon\to 0}$ with $q=1/2$ such that $|\alpha_{\varepsilon}|=o(p_{\varepsilon})$ but $d_{\mathrm{K}}(W_{\varepsilon},\operatorname{Exp}(1))=\Theta(p_{\varepsilon})\text{.}$</span></p>
</div>
</div>
<div id="S4.SS4.4" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS4.p11" class="ltx_para">
<p id="S4.SS4.p11.1" class="ltx_p"><span id="S4.SS4.p11.1.1" class="ltx_text">Set $q=s=1/2$ and $P(T_{0}^{(\varepsilon)}=t)=\varepsilon\,\mathbf{1}_{t=1}+(1-\varepsilon)\,\mathbf{1}_{t=M_{\varepsilon}}$ where $M_{\varepsilon}=\lceil 3\log_{2}(1/\varepsilon)\rceil\text{.}$</span></p>
</div>
<div id="S4.SS4.p12" class="ltx_para">
<p id="S4.SS4.p12.1" class="ltx_p"><em id="S4.SS4.p12.1.1" class="ltx_emph ltx_font_italic">Claim 1</em><span id="S4.SS4.p12.1.2" class="ltx_text">: $|\alpha_{\varepsilon}|=o(p_{\varepsilon})\text{.}$ Since $2^{-M_{\varepsilon}}\leq\varepsilon^{3}\text{:}$ $p_{\varepsilon}=\varepsilon/2+O(\varepsilon^{3})$ and $qD_{1,\varepsilon}=\varepsilon/2+o(\varepsilon)=p_{\varepsilon}+o(p_{\varepsilon})\text{,}$ so $\alpha_{\varepsilon}=o(p_{\varepsilon})\text{.}$</span></p>
</div>
<div id="S4.SS4.p13" class="ltx_para">
<p id="S4.SS4.p13.1" class="ltx_p"><em id="S4.SS4.p13.1.1" class="ltx_emph ltx_font_italic">Claim 2</em><span id="S4.SS4.p13.1.2" class="ltx_text">: $d_{\mathrm{K}}=\Theta(p_{\varepsilon})\text{.}$ The event $\{T=1\}$ requires $T_{0}=1$ and no catastrophe: $P(T=1)=\varepsilon/2\text{.}$ At $x_{0}=1/E[T]\text{:}$ $P(W\leq x_{0})=P(T\leq 1)=p_{\varepsilon}+o(p_{\varepsilon})$ while $1-e^{-x_{0}}=p_{\varepsilon}/2+O(p_{\varepsilon}^{2})\text{.}$ Hence $d_{\mathrm{K}}\geq p_{\varepsilon}/2+o(p_{\varepsilon})\text{.}$ The upper bound $d_{\mathrm{K}}=O(p_{\varepsilon})$ follows from Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a> (since $|\alpha_{\varepsilon}|=o(p_{\varepsilon})$).
∎</span></p>
</div>
</div>
<div id="S4.Thmtheorem17" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S4.Thmtheorem17.2" class="ltx_text ltx_font_italic">Remark 4.17</span></span><span id="S4.Thmtheorem17.3" class="ltx_text ltx_font_italic"> </span>(Why $p+|\alpha|$ is the correct template)<span id="S4.Thmtheorem17.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S4.Thmtheorem17.p1" class="ltx_para">
<p id="S4.Thmtheorem17.p1.1" class="ltx_p">The two-sided bound decomposes the approximation error into two sources with distinct physical origins:</p>
<ul id="S4.I3" class="ltx_itemize">
<li id="S4.I3.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S4.I3.i1.p1" class="ltx_para">
<p id="S4.I3.i1.p1.1" class="ltx_p">The <em id="S4.I3.i1.p1.1.1" class="ltx_emph ltx_font_italic">$p$-term</em> reflects geometric discreteness: the attempt count is integer-valued, so $W$ takes values in $(1/\mu)\mathbb{Z}_{&gt;0}\text{,}$ creating CDF jumps that no continuous distribution can match.</p>
</div></li>
<li id="S4.I3.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">•</span> 
<div id="S4.I3.i2.p1" class="ltx_para">
<p id="S4.I3.i2.p1.1" class="ltx_p">The <em id="S4.I3.i2.p1.1.1" class="ltx_emph ltx_font_italic">$|\alpha|$-term</em> reflects the successful-attempt perturbation: $T$ is not a pure geometric sum but includes the final attempt $B\text{,}$ whose expected length may deviate from the rescaling target.</p>
</div></li>
</ul>
<p id="S4.Thmtheorem17.p1.2" class="ltx_p">The counterexample engineers near-cancellation of the perturbation ($\alpha\approx 0$) while preserving the irreducible lattice error, exposing the $\Theta(p)$ floor. In the CCP application (§<a href="#S6" title="6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>), the opposite regime prevails: $p\ll|\alpha|\text{,}$ so the perturbation term dominates.</p>
</div>
</div>
</section>
</section>
<section id="S5" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="continuous-time-theory"><span class="ltx_tag ltx_tag_section">5 </span>Continuous-Time Theory</h2>

<div id="S5.p1" class="ltx_para">
<p id="S5.p1.1" class="ltx_p">The discrete theory of §§<a href="#S2" title="2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>–<a href="#S4" title="4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a> rests on the affine dependence of $G_{T}$ on the base PGF $g$ at a linearly shifted argument. In continuous time, the same mechanism operates with PGFs replaced by Laplace transforms and the multiplicative shift $u=ws$ replaced by an additive shift $\sigma=\lambda+r\text{.}$ The entire theory carries over, with one notable sharpening: the geometric-tail gap of Theorem <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Characterization). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a> closes, and affine Laplace structure characterizes <em id="S5.p1.1.1" class="ltx_emph ltx_font_italic">full</em> Poisson resetting with no residual degree of freedom (Theorem <a href="#S5.Thmtheorem7" title="Theorem 5.7 (Continuous-time characterization). ‣ 5.4 Characterization: Affine Laplace Structure Is Poisson ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.7</span></a>).</p>
</div>
<section id="S5.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="setup"><span class="ltx_tag ltx_tag_subsection">5.1 </span>Setup</h3>

<div id="S5.SS1.p1" class="ltx_para">
<p id="S5.SS1.p1.1" class="ltx_p">Let $T_{0}$ be a positive, almost surely finite, continuous random variable with Laplace transform $\hat{f}_{0}(\lambda)=E[e^{-\lambda T_{0}}]\text{.}$ Catastrophe occurs via a Poisson process of rate $r&gt;0\text{,}$ independent of $T_{0}\text{.}$ The attempt decomposition (<a href="#S2.E6" title="In 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>) carries over with $N\sim\operatorname{Geom}_{0}(p)$ and</p>
<table id="S5.E35" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p=P(T_{0}&lt;\tau)=E[e^{-rT_{0}}]=\hat{f}_{0}(r),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(35)</span></td></tr></tbody>
</table>
<p id="S5.SS1.p1.2" class="ltx_p">where $\tau\sim\operatorname{Exp}(r)$ is the first catastrophe time. Under any age-based mechanism, catastrophe and $T_{0}$ are independent, so $p=P(T_{0}&lt;\tau)=E[S(T_{0})]\text{,}$ the continuous-time analog of (<a href="#S3.E19" title="In 3.1 General Hazard Framework ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">19</span></a>). More generally, for any continuous-time catastrophe mechanism with hazard rate $h:(0,\infty)\to(0,\infty)\text{,}$ the survival function $S(x)=\exp\bigl(-\int_{0}^{x}h(t)\,dt\bigr)$ gives the probability of no catastrophe before time $x\text{;}$ Poisson resetting is the special case $h\equiv r\text{,}$ i.e., $S(x)=e^{-rx}\text{.}$ We write $\hat{f}_{T}(\lambda)=E[e^{-\lambda T}]$ for the Laplace transform of the completion time.</p>
</div>
</section>
<section id="S5.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-laplace-transform-formula-and-affine-structure"><span class="ltx_tag ltx_tag_subsection">5.2 </span>The Laplace Transform Formula and Affine Structure</h3>

<div id="S5.SS2.p1" class="ltx_para">
<p id="S5.SS2.p1.1" class="ltx_p">The following is a standard consequence of the renewal structure under Poisson resetting (see, e.g., <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib16" title="" class="ltx_ref">15</a>, <a href="#bib.bib8" title="" class="ltx_ref">8</a>]</cite>). We state it to exhibit its affine structure, which has not been identified previously.</p>
</div>
<div id="S5.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem1.2" class="ltx_text ltx_font_bold">Theorem 5.1</span></span><span id="S5.Thmtheorem1.3" class="ltx_text ltx_font_bold"> </span>(Laplace transform under Poisson resetting)<span id="S5.Thmtheorem1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmtheorem1.p1" class="ltx_para">
<p id="S5.Thmtheorem1.p1.1" class="ltx_p"><span id="S5.Thmtheorem1.p1.1.1" class="ltx_text ltx_font_italic">For any base process $T_{0}$ under Poisson resetting at rate $r\text{,}$</span></p>
<table id="S5.E36" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\hat{f}_{T}(\lambda)=\frac{(\lambda+r)\,\hat{f}_{0}(\lambda+r)}{\lambda+r\,\hat{f}_{0}(\lambda+r)},\qquad\sigma:=\lambda+r.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(36)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S5.SS2.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS2.p2" class="ltx_para">
<p id="S5.SS2.p2.1" class="ltx_p"><span id="S5.SS2.p2.1.1" class="ltx_text">The successful-attempt Laplace transform is $\hat{f}_{B}(\lambda)=\hat{f}_{0}(\sigma)/p$ (tilting by $e^{-rT_{0}}/p$). For the failed attempt, $A=\tau\mid\tau&lt;T_{0}$ with $\tau\sim\operatorname{Exp}(r)$ independent of $T_{0}\text{:}$</span></p>
<table id="S5.Ex32" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(1-p)\,\hat{f}_{A}(\lambda)=E[e^{-\lambda\tau}\mathbf{1}_{\tau&lt;T_{0}}]=\frac{r(1-\hat{f}_{0}(\sigma))}{\sigma}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS2.p2.2" class="ltx_p"><span id="S5.SS2.p2.2.1" class="ltx_text">Composing via $\hat{f}_{T}=\hat{f}_{B}\cdot p/[1-(1-p)\hat{f}_{A}]\text{,}$ the denominator becomes $1-r(1-\hat{f}_{0}(\sigma))/\sigma=(\lambda+r\hat{f}_{0}(\sigma))/\sigma\text{,}$ using $\sigma-r=\lambda\text{,}$ which gives (<a href="#S5.E36" title="In Theorem 5.1 (Laplace transform under Poisson resetting). ‣ 5.2 The Laplace Transform Formula and Affine Structure ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">36</span></a>).</span></p>
</div>
<div id="S5.SS2.p3" class="ltx_para">
<p id="S5.SS2.p3.1" class="ltx_p"><span id="S5.SS2.p3.1.1" class="ltx_text">∎</span></p>
</div>
</div>
<div id="S5.Thmtheorem2" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem2.2" class="ltx_text ltx_font_bold">Corollary 5.2</span></span><span id="S5.Thmtheorem2.3" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmtheorem2.p1" class="ltx_para">
<p id="S5.Thmtheorem2.p1.1" class="ltx_p">$E[T]=(1-p)/(rp)$<span id="S5.Thmtheorem2.p1.1.1" class="ltx_text ltx_font_italic">, depending on $T_{0}$ only through $p=\hat{f}_{0}(r)\text{.}$</span></p>
</div>
</div>
<div id="S5.SS2.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS2.p4" class="ltx_para">
<p id="S5.SS2.p4.1" class="ltx_p"><span id="S5.SS2.p4.1.1" class="ltx_text">By the attempt decomposition, $E[T]=E[\ell]/p$ with $E[\ell]=(1-p)/r$ (the expected attempt length under $\operatorname{Exp}(r)$ catastrophe), giving $E[T]=(1-p)/(rp)\text{.}$
∎</span></p>
</div>
</div>
<div id="S5.SS2.p5" class="ltx_para">
<p id="S5.SS2.p5.1" class="ltx_p">As in the discrete case (§<a href="#S2.SS2" title="2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a>), formula (<a href="#S5.E36" title="In Theorem 5.1 (Laplace transform under Poisson resetting). ‣ 5.2 The Laplace Transform Formula and Affine Structure ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">36</span></a>) is affine in $\hat{f}_{0}(\sigma)$ with linear shift $\sigma=\lambda+r\text{:}$</p>
<table id="S5.E37" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N(\lambda)=\underbrace{\sigma}_{\alpha_{N}(\lambda)}\cdot\hat{f}_{0}(\sigma)+\underbrace{0}_{\beta_{N}(\lambda)},\qquad D(\lambda)=\underbrace{r}_{\alpha_{D}(\lambda)}\cdot\hat{f}_{0}(\sigma)+\underbrace{\lambda}_{\beta_{D}(\lambda)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(37)</span></td></tr></tbody>
</table>
<p id="S5.SS2.p5.2" class="ltx_p">At the normalization point $\lambda=0\text{:}$ $\beta_{N}(0)=0=\beta_{D}(0)\text{,}$ so $\hat{f}_{T}(0)=1$ forces</p>
<table id="S5.E38" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha_{N}(0)=\alpha_{D}(0)=r,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(38)</span></td></tr></tbody>
</table>
<p id="S5.SS2.p5.3" class="ltx_p">the continuous-time counterpart of (<a href="#S2.E10" title="In Proposition 2.5 (Affine structure and coefficient equality). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">10</span></a>). Since the transform has the same affine-ratio structure with linear shift and coefficient matching at $\lambda=0\text{,}$ Lemma <a href="#S2.Thmtheorem7" title="Lemma 2.7 (Affine-ratio recursion). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.7</span></a> applies in continuous time as well.</p>
</div>
</section>
<section id="S5.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="derivative-reduction"><span class="ltx_tag ltx_tag_subsection">5.3 </span>Derivative Reduction</h3>

<div id="S5.Thmtheorem3" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem3.2" class="ltx_text ltx_font_bold">Theorem 5.3</span></span><span id="S5.Thmtheorem3.3" class="ltx_text ltx_font_bold"> </span>(Continuous-time DRP)<span id="S5.Thmtheorem3.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmtheorem3.p1" class="ltx_para">
<p id="S5.Thmtheorem3.p1.1" class="ltx_p"><span id="S5.Thmtheorem3.p1.1.1" class="ltx_text ltx_font_italic">Define $D_{k}=\hat{f}_{0}^{(k)}(r)$ and $\Delta_{k}=N^{(k)}(0)-D^{(k)}(0)\text{.}$ For all $k\geq 1\text{,}$</span></p>
<table id="S5.E39" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Delta_{k}=\begin{cases}-(1-p),&amp;k=1,\\ k\,D_{k-1},&amp;k\geq 2.\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(39)</span></td></tr></tbody>
</table>
<p id="S5.Thmtheorem3.p1.2" class="ltx_p"><span id="S5.Thmtheorem3.p1.2.1" class="ltx_text ltx_font_italic">In particular, $\Delta_{k}$ does not contain $D_{k}\text{.}$</span></p>
</div>
</div>
<div id="S5.SS3.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS3.p1" class="ltx_para">
<p id="S5.SS3.p1.1" class="ltx_p"><span id="S5.SS3.p1.1.1" class="ltx_text">Since $N(\lambda)=(\lambda+r)\hat{f}_{0}(\lambda+r)$ and $\sigma=\lambda+r$ is linear ($\sigma^{\prime}=1$), the Leibniz rule gives $N^{(k)}(0)=rD_{k}+kD_{k-1}\text{.}$ For the denominator: $D^{(1)}(0)=1+rD_{1}$ and $D^{(k)}(0)=rD_{k}$ for $k\geq 2\text{.}$ Hence $\Delta_{k}=kD_{k-1}$ for $k\geq 2$ (the $D_{k}$ terms cancel because $\alpha_{N}(0)=\alpha_{D}(0)=r$), and $\Delta_{1}=(rD_{1}+p)-(1+rD_{1})=p-1\text{.}$
∎</span></p>
</div>
</div>
<div id="S5.Thmtheorem4" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem4.2" class="ltx_text ltx_font_italic">Remark 5.4</span></span><span id="S5.Thmtheorem4.3" class="ltx_text ltx_font_italic"> </span>(Comparison with the discrete DRP)<span id="S5.Thmtheorem4.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S5.Thmtheorem4.p1" class="ltx_para">
<p id="S5.Thmtheorem4.p1.1" class="ltx_p">The discrete formula $\Delta_{k}=-ks^{k-1}D_{k-1}$ (Theorem <a href="#S2.Thmtheorem6" title="Theorem 2.6 (Derivative reduction principle). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.6</span></a>) contains the factor $s^{k-1}$ from the multiplicative shift $u=ws$ (chain rule coefficient $s$). The continuous formula $\Delta_{k}=kD_{k-1}$ has no such factor because the additive shift $\sigma=\lambda+r$ has chain rule coefficient $1\text{.}$ The sign difference ($-k$ vs. $+k$) reflects opposite monotonicity conventions: $G_{T}^{\prime}(1)=E[T]&gt;0$ while $\hat{f}_{T}^{\prime}(0)=-E[T]&lt;0\text{.}$</p>
</div>
</div>
</section>
<section id="S5.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="characterization-affine-laplace-structure-is-poisson"><span class="ltx_tag ltx_tag_subsection">5.4 </span>Characterization: Affine Laplace Structure Is Poisson</h3>

<div id="S5.SS4.p1" class="ltx_para">
<p id="S5.SS4.p1.1" class="ltx_p">In discrete time, affine PGF structure characterizes geometric-tail catastrophe—constant hazard from the second step onward—leaving the first-step hazard $h_{1}$ as a free parameter (Theorem <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Characterization). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a>). In continuous time, this residual degree of freedom vanishes.</p>
</div>
<div id="S5.Thmtheorem5" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem5.2" class="ltx_text ltx_font_bold">Definition 5.5</span></span><span id="S5.Thmtheorem5.3" class="ltx_text ltx_font_bold"> </span>(Uniform affine Laplace structure)<span id="S5.Thmtheorem5.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmtheorem5.p1" class="ltx_para">
<p id="S5.Thmtheorem5.p1.1" class="ltx_p">A continuous-time catastrophe mechanism has <em id="S5.Thmtheorem5.p1.1.1" class="ltx_emph ltx_font_italic">uniform affine Laplace structure</em> if there exist functions $a(\lambda),b(\lambda),c(\lambda),d(\lambda)\text{,}$ analytic in a neighborhood of $\lambda=0\text{,}$ depending only on the mechanism and a linear function $\sigma(\lambda)=\lambda+r$ ($r&gt;0$), such that for all base processes $T_{0}\text{,}$</p>
<table id="S5.Ex33" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\hat{f}_{T}(\lambda)=\frac{a(\lambda)\,\hat{f}_{0}(\sigma)+b(\lambda)}{c(\lambda)\,\hat{f}_{0}(\sigma)+d(\lambda)},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.Thmtheorem5.p1.2" class="ltx_p">with $a,c$ not identically zero and $c(0)\hat{f}_{0}(r)+d(0)\neq 0$ for all admissible $\hat{f}_{0}\text{.}$</p>
</div>
</div>
<div id="S5.Thmtheorem6" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem6.2" class="ltx_text ltx_font_italic">Remark 5.6</span></span><span id="S5.Thmtheorem6.3" class="ltx_text ltx_font_italic"> </span>(Why the shift has unit slope)<span id="S5.Thmtheorem6.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S5.Thmtheorem6.p1" class="ltx_para">
<p id="S5.Thmtheorem6.p1.1" class="ltx_p">The restriction $\sigma(\lambda)=\lambda+r$ is not <em id="S5.Thmtheorem6.p1.1.1" class="ltx_emph ltx_font_italic">ad hoc</em>. Starting from a general linear shift $\sigma(\lambda)=a\lambda+b$ with $a,b&gt;0\text{,}$ the single-point sufficiency condition $p=\hat{f}_{0}(b)$ for all $T_{0}$ forces $S(x)=e^{-bx}$ (take $T_{0}=\delta_{x}$), identifying $b$ with the catastrophe rate $r\text{.}$ The Poisson catastrophe time then contributes a factor $e^{-rt}$ that combines with the Laplace kernel $e^{-\lambda t}$ into $e^{-(\lambda+r)t}\text{,}$ giving $a=1$ without further assumptions.</p>
</div>
</div>
<div id="S5.SS4.p2" class="ltx_para">
<p id="S5.SS4.p2.1" class="ltx_p">For the characterization result below, we temporarily enlarge the admissible
class of base laws: the quantifiers over $T_{0}$ range over all positive,
almost surely finite random variables, including point masses and two-point
mixtures. Continuity of $T_{0}$ is imposed only later, in the lattice-free
sharp-rate statement.</p>
</div>
<div id="S5.Thmtheorem7" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem7.2" class="ltx_text ltx_font_bold">Theorem 5.7</span></span><span id="S5.Thmtheorem7.3" class="ltx_text ltx_font_bold"> </span>(Continuous-time characterization)<span id="S5.Thmtheorem7.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmtheorem7.p1" class="ltx_para">
<p id="S5.Thmtheorem7.p1.1" class="ltx_p"><span id="S5.Thmtheorem7.p1.1.1" class="ltx_text ltx_font_italic">Among continuous-time age-based catastrophe mechanisms specified by a measurable, locally integrable hazard rate $h:(0,\infty)\to(0,\infty)$ (so that $S(x)=\exp(-\int_{0}^{x}h(t)\,dt)$ is well-defined, strictly decreasing, and absolutely continuous), the following are equivalent:</span></p>
<ol id="S5.I1" class="ltx_enumerate">
<li id="S5.I1.i1" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(a)</span> 
<div id="S5.I1.i1.p1" class="ltx_para">
<p id="S5.I1.i1.p1.1" class="ltx_p">$S(x)=e^{-rx}$<span id="S5.I1.i1.p1.1.1" class="ltx_text ltx_font_italic"> for all </span>$x&gt;0$<span id="S5.I1.i1.p1.1.2" class="ltx_text ltx_font_italic"> (Poisson resetting; equivalently,
</span>$h(t)=r$<span id="S5.I1.i1.p1.1.3" class="ltx_text ltx_font_italic"> for a.e. </span>$t&gt;0$<span id="S5.I1.i1.p1.1.4" class="ltx_text ltx_font_italic">).</span></p>
</div></li>
<li id="S5.I1.i2" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(b)</span> 
<div id="S5.I1.i2.p1" class="ltx_para">
<p id="S5.I1.i2.p1.1" class="ltx_p"><span id="S5.I1.i2.p1.1.1" class="ltx_text ltx_font_italic">Uniform affine Laplace structure (Definition </span><a href="#S5.Thmtheorem5" title="Definition 5.5 (Uniform affine Laplace structure). ‣ 5.4 Characterization: Affine Laplace Structure Is Poisson ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref ltx_font_italic"><span class="ltx_text ltx_ref_tag">5.5</span></a><span id="S5.I1.i2.p1.1.2" class="ltx_text ltx_font_italic">).</span></p>
</div></li>
<li id="S5.I1.i3" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(c)</span> 
<div id="S5.I1.i3.p1" class="ltx_para">
<p id="S5.I1.i3.p1.1" class="ltx_p"><span id="S5.I1.i3.p1.1.1" class="ltx_text ltx_font_italic">Derivative reduction: there exists </span>$r_{0}&gt;0$<span id="S5.I1.i3.p1.1.2" class="ltx_text ltx_font_italic"> such that for every
positive, almost surely finite </span>$T_{0}$<span id="S5.I1.i3.p1.1.3" class="ltx_text ltx_font_italic"> and every </span>$k\geq 1$<span id="S5.I1.i3.p1.1.4" class="ltx_text ltx_font_italic">, the </span>$k$<span id="S5.I1.i3.p1.1.5" class="ltx_text ltx_font_italic">-th
moment of </span>$T$<span id="S5.I1.i3.p1.1.6" class="ltx_text ltx_font_italic"> is determined by
</span>$\{\hat{f}_{0}^{(j)}(r_{0})\}_{j=0}^{k-1}$<span id="S5.I1.i3.p1.1.7" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
<li id="S5.I1.i4" class="ltx_item" style="list-style-type:none;"><span class="ltx_tag ltx_tag_item">(d)</span> 
<div id="S5.I1.i4.p1" class="ltx_para">
<p id="S5.I1.i4.p1.1" class="ltx_p"><span id="S5.I1.i4.p1.1.1" class="ltx_text ltx_font_italic">Single-point sufficiency: there exists </span>$r_{0}&gt;0$<span id="S5.I1.i4.p1.1.2" class="ltx_text ltx_font_italic"> such that
</span>$p=\hat{f}_{0}(r_{0})$<span id="S5.I1.i4.p1.1.3" class="ltx_text ltx_font_italic"> for every positive, almost surely finite </span>$T_{0}$<span id="S5.I1.i4.p1.1.4" class="ltx_text ltx_font_italic">.</span></p>
</div></li>
</ol>
</div>
</div>
<div id="S5.SS4.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS4.p3" class="ltx_para">
<p id="S5.SS4.p3.1" class="ltx_p"><span id="S5.SS4.p3.1.1" class="ltx_text">(a)$\Rightarrow$(b): Theorem <a href="#S5.Thmtheorem1" title="Theorem 5.1 (Laplace transform under Poisson resetting). ‣ 5.2 The Laplace Transform Formula and Affine Structure ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.1</span></a>.</span></p>
</div>
<div id="S5.SS4.p4" class="ltx_para">
<p id="S5.SS4.p4.1" class="ltx_p"><span id="S5.SS4.p4.1.1" class="ltx_text">(b)$\Rightarrow$(c): Suppose</span></p>
<table id="S5.Ex34" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\hat{f}_{T}(\lambda)=\frac{a(\lambda)\hat{f}_{0}(\sigma(\lambda))+b(\lambda)}{c(\lambda)\hat{f}_{0}(\sigma(\lambda))+d(\lambda)},\qquad\sigma(\lambda)=\lambda+r_{0}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p4.2" class="ltx_p"><span id="S5.SS4.p4.2.1" class="ltx_text">Applying $\hat{f}_{T}(0)=1$ to point masses $T_{0}=\delta_{x}$ and letting $x\to\infty$ gives $b(0)=d(0)\text{;}$ back-substitution yields $a(0)=c(0)\text{.}$ By non-degeneracy, Lemma <a href="#S2.Thmtheorem7" title="Lemma 2.7 (Affine-ratio recursion). ‣ 2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.7</span></a> applies with $R=\hat{f}_{T}\text{,}$ $h=\hat{f}_{0}\text{,}$ $z_{*}=0\text{,}$ and $u_{0}=r_{0}\text{.}$ Hence $\hat{f}_{T}^{(k)}(0)$ depends only on $\{\hat{f}_{0}^{(j)}(r_{0})\}_{j=0}^{k-1}\text{,}$ which is exactly the derivative-reduction property.</span></p>
</div>
<div id="S5.SS4.p5" class="ltx_para">
<p id="S5.SS4.p5.1" class="ltx_p"><span id="S5.SS4.p5.1.1" class="ltx_text">(a)$\Rightarrow$(d): By definition (<a href="#S5.E35" title="In 5.1 Setup ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">35</span></a>),</span></p>
<table id="S5.Ex35" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p=P(T_{0}&lt;\tau)=E[e^{-rT_{0}}]=\hat{f}_{0}(r).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
<div id="S5.SS4.p6" class="ltx_para">
<p id="S5.SS4.p6.1" class="ltx_p"><span id="S5.SS4.p6.1.1" class="ltx_text">(d)$\Rightarrow$(a): Under (d), for every positive, almost surely finite
$T_{0}$ we have</span></p>
<table id="S5.Ex36" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[S(T_{0})]=p=\hat{f}_{0}(r_{0})=E[e^{-r_{0}T_{0}}].$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p6.2" class="ltx_p"><span id="S5.SS4.p6.2.1" class="ltx_text">Taking $T_{0}=\delta_{x}$ gives $S(x)=e^{-r_{0}x}$ for every $x&gt;0\text{.}$</span></p>
</div>
<div id="S5.SS4.p7" class="ltx_para">
<p id="S5.SS4.p7.1" class="ltx_p"><span id="S5.SS4.p7.1.1" class="ltx_text">(c)$\Rightarrow$(a): We use only the $k=1$ case. Thus there exist
$r_{0}&gt;0$ and a function $\psi:(0,1)\to\mathbb{R}$ such that</span></p>
<table id="S5.Ex37" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[T]=\psi(\hat{f}_{0}(r_{0}))$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p7.2" class="ltx_p"><span id="S5.SS4.p7.2.1" class="ltx_text">for every positive, almost surely finite $T_{0}\text{.}$
For a general continuous-time age-based catastrophe mechanism,</span></p>
<table id="S5.Ex38" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p=E[S(T_{0})],\qquad E[\ell\,|\,T_{0}=x]=F(x):=\int_{0}^{x}S(t)\,dt,\qquad E[T]=\frac{E[\ell]}{p}=\frac{E[F(T_{0})]}{E[S(T_{0})]}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p7.3" class="ltx_p"><span id="S5.SS4.p7.3.1" class="ltx_text">Hence</span></p>
<table id="S5.E40" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{E[F(T_{0})]}{E[S(T_{0})]}=\psi\!\bigl(E[e^{-r_{0}T_{0}}]\bigr)$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(40)</span></td></tr></tbody>
</table>
<p id="S5.SS4.p7.4" class="ltx_p"><span id="S5.SS4.p7.4.1" class="ltx_text">for all positive, almost surely finite $T_{0}\text{.}$</span></p>
</div>
<div id="S5.SS4.p8" class="ltx_para">
<p id="S5.SS4.p8.1" class="ltx_p"><em id="S5.SS4.p8.1.1" class="ltx_emph ltx_font_italic">Step 1: point masses determine $\psi$ on $(0,1)\text{.}$</em><span id="S5.SS4.p8.1.2" class="ltx_text">
Taking $T_{0}=\delta_{x}$ in (<a href="#S5.E40" title="In Proof. ‣ 5.4 Characterization: Affine Laplace Structure Is Poisson ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">40</span></a>) gives</span></p>
<table id="S5.Ex39" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\psi(e^{-r_{0}x})=\frac{F(x)}{S(x)},\qquad x&gt;0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p8.2" class="ltx_p"><span id="S5.SS4.p8.2.1" class="ltx_text">Since $x\mapsto e^{-r_{0}x}$ is a bijection $(0,\infty)\to(0,1)\text{,}$ point
masses determine $\psi$ on all of $(0,1)\text{.}$</span></p>
</div>
<div id="S5.SS4.p9" class="ltx_para">
<p id="S5.SS4.p9.1" class="ltx_p"><em id="S5.SS4.p9.1.1" class="ltx_emph ltx_font_italic">Step 2: two-point laws force $\psi$ to be Möbius.</em><span id="S5.SS4.p9.1.2" class="ltx_text">
Take $T_{0}=\alpha\delta_{a}+(1-\alpha)\delta_{b}$ with $0&lt;a&lt;b\text{.}$ Writing</span></p>
<table id="S5.Ex40" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$v=\alpha e^{-r_{0}a}+(1-\alpha)e^{-r_{0}b}\in[e^{-r_{0}b},e^{-r_{0}a}],$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p9.2" class="ltx_p"><span id="S5.SS4.p9.2.1" class="ltx_text">equation (<a href="#S5.E40" title="In Proof. ‣ 5.4 Characterization: Affine Laplace Structure Is Poisson ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">40</span></a>) becomes</span></p>
<table id="S5.Ex41" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\psi(v)=\frac{\alpha F(a)+(1-\alpha)F(b)}{\alpha S(a)+(1-\alpha)S(b)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p9.3" class="ltx_p"><span id="S5.SS4.p9.3.1" class="ltx_text">Solving for $\alpha$ in terms of $v$ shows that the right-hand side is a
linear-fractional function of $v\text{,}$ namely</span></p>
<table id="S5.Ex42" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\psi(v)=\frac{(F(a)-F(b))\,v+F(b)e^{-r_{0}a}-F(a)e^{-r_{0}b}}{(S(a)-S(b))\,v+S(b)e^{-r_{0}a}-S(a)e^{-r_{0}b}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p9.4" class="ltx_p"><span id="S5.SS4.p9.4.1" class="ltx_text">Thus $\psi$ is Möbius on every interval
$[e^{-r_{0}b},e^{-r_{0}a}]\text{.}$</span></p>
</div>
<div id="S5.SS4.p10" class="ltx_para">
<p id="S5.SS4.p10.1" class="ltx_p"><em id="S5.SS4.p10.1.1" class="ltx_emph ltx_font_italic">Step 3: overlapping intervals glue the local Möbius maps globally.</em><span id="S5.SS4.p10.1.2" class="ltx_text">
Exactly as in Steps 2–4 of Theorem <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Characterization). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a>, the overlapping-interval
consistency argument shows that all these local Möbius maps coincide with a
single global one:</span></p>
<table id="S5.Ex43" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\psi(v)=\frac{Av+B}{Cv+D},\qquad v\in(0,1).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p10.2" class="ltx_p"><span id="S5.SS4.p10.2.1" class="ltx_text">Because $S$ is strictly decreasing, the denominator slope in the two-point
formula is nonzero, so the global denominator coefficient satisfies $C\neq 0\text{.}$</span></p>
</div>
<div id="S5.SS4.p11" class="ltx_para">
<p id="S5.SS4.p11.1" class="ltx_p"><em id="S5.SS4.p11.1.1" class="ltx_emph ltx_font_italic">Step 4: coefficient consistency forces $F=\rho S+c\text{.}$</em><span id="S5.SS4.p11.1.2" class="ltx_text">
Comparing the coefficients of $v$ in the two-point representation with the
global Möbius map shows that</span></p>
<table id="S5.Ex44" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{F(a)-F(b)}{S(a)-S(b)}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p11.2" class="ltx_p"><span id="S5.SS4.p11.2.1" class="ltx_text">is independent of the pair $(a,b)$ with $a\neq b\text{.}$ Denoting this constant by
$\rho\text{,}$ we obtain</span></p>
<table id="S5.Ex45" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$F(x)=\rho\,S(x)+c,\qquad x&gt;0$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p11.3" class="ltx_p"><span id="S5.SS4.p11.3.1" class="ltx_text">for some constant $c\text{.}$</span></p>
</div>
<div id="S5.SS4.p12" class="ltx_para">
<p id="S5.SS4.p12.1" class="ltx_p"><em id="S5.SS4.p12.1.1" class="ltx_emph ltx_font_italic">Step 5: differentiation yields constant hazard everywhere.</em><span id="S5.SS4.p12.1.2" class="ltx_text">
Since $F(x)=\int_{0}^{x}S(t)\,dt$ is absolutely continuous and
$F^{\prime}(x)=S(x)$ a.e., differentiating $F=\rho S+c$ gives</span></p>
<table id="S5.Ex46" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$S(x)=\rho\,S^{\prime}(x)\qquad\text{for a.e.\ }x&gt;0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p12.2" class="ltx_p"><span id="S5.SS4.p12.2.1" class="ltx_text">As $S^{\prime}(x)=-h(x)S(x)$ a.e. and $S(x)&gt;0\text{,}$ we conclude</span></p>
<table id="S5.Ex47" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$h(x)=-\frac{1}{\rho}=:r\qquad\text{for a.e.\ }x&gt;0.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS4.p12.3" class="ltx_p"><span id="S5.SS4.p12.3.1" class="ltx_text">Hence $S(x)=e^{-rx}$ for all $x&gt;0\text{,}$ which is exactly (a).
∎</span></p>
</div>
</div>
<div id="S5.Thmtheorem8" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem8.2" class="ltx_text ltx_font_italic">Remark 5.8</span></span><span id="S5.Thmtheorem8.3" class="ltx_text ltx_font_italic"> </span>(Why the geometric-tail gap closes)<span id="S5.Thmtheorem8.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S5.Thmtheorem8.p1" class="ltx_para">
<p id="S5.Thmtheorem8.p1.1" class="ltx_p">The geometric-tail gap of Theorem <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Characterization). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a> is a joint artifact of two discrete-time limitations: countable test points (requiring Möbius extension) and integer arithmetic (permitting only differencing). In continuous time, both limitations vanish simultaneously, forcing full Poisson resetting with no residual degree of freedom.</p>
</div>
</div>
</section>
<section id="S5.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="exponential-approximation-1"><span class="ltx_tag ltx_tag_subsection">5.5 </span>Exponential Approximation</h3>

<div id="S5.SS5.p1" class="ltx_para">
<p id="S5.SS5.p1.1" class="ltx_p">The exponential approximation theory of §<a href="#S4" title="4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a> has a continuous-time counterpart. Define the continuous-time perturbation parameters:</p>
<table id="S5.E41" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha=\frac{p+rD_{1}}{1-p},\qquad\beta=\frac{1+rD_{1}}{1-p},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(41)</span></td></tr></tbody>
</table>
<p id="S5.SS5.p1.2" class="ltx_p">where $D_{1}=\hat{f}_{0}^{\prime}(r)\text{.}$ Note that $D_{1}=-E[T_{0}e^{-rT_{0}}]&lt;0\text{,}$ so the sign conventions in the discrete and continuous perturbation parameters are consistent: both $\alpha$ vanish when $b/\mu$ matches the geometric target (Remark <a href="#S4.Thmtheorem3" title="Remark 4.3 (Interpretation of 𝛼). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.3</span></a>).
The fundamental identity</p>
<table id="S5.E42" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$1+\alpha-\beta=0$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(42)</span></td></tr></tbody>
</table>
<p id="S5.SS5.p1.3" class="ltx_p">holds by the same one-line computation as Proposition <a href="#S4.Thmtheorem2" title="Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a>(<a href="#S4.I2.i1" title="item a ‣ Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">a</span></a>), replacing $s+q=1$ by direct cancellation of $rD_{1}\text{.}$ Differentiating $\hat{f}_{B}(\lambda)=\hat{f}_{0}(\lambda+r)/p$ at $\lambda=0$ gives $b=-D_{1}/p\text{,}$ so</p>
<table id="S5.E43" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{b}{\mu}=\frac{-rD_{1}}{1-p}=\frac{p}{1-p}-\alpha,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(43)</span></td></tr></tbody>
</table>
<p id="S5.SS5.p1.4" class="ltx_p">the continuous-time analog of Proposition <a href="#S4.Thmtheorem2" title="Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a>(<a href="#S4.I2.i2" title="item b ‣ Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">b</span></a>).</p>
</div>
<div id="S5.Thmtheorem9" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem9.2" class="ltx_text ltx_font_bold">Theorem 5.9</span></span><span id="S5.Thmtheorem9.3" class="ltx_text ltx_font_bold"> </span>(Continuous-time Laplace expansion)<span id="S5.Thmtheorem9.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmtheorem9.p1" class="ltx_para">
<p id="S5.Thmtheorem9.p1.1" class="ltx_p"><span id="S5.Thmtheorem9.p1.1.1" class="ltx_text ltx_font_italic">Under Poisson resetting at rate $r\text{,}$ let $W=T/E[T]\text{.}$ For $\epsilon:=\theta rp/(1-p)\leq\epsilon_{0}\text{,}$</span></p>
<table id="S5.E44" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[e^{-\theta W}]-\frac{1}{1+\theta}=\frac{\alpha\,\theta^{2}}{(1+\theta)^{2}}+O\!\left(\frac{|\alpha|^{2}\,\theta^{3}}{(1+\theta)^{3}}\right)+O\!\left(\frac{p\,\theta^{2}}{1+\theta}\right),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(44)</span></td></tr></tbody>
</table>
<p id="S5.Thmtheorem9.p1.2" class="ltx_p"><span id="S5.Thmtheorem9.p1.2.1" class="ltx_text ltx_font_italic">with implicit constants depending on $|D_{1}|$ and $|D_{2}|\text{,}$ which satisfy $|D_{k}|=|\hat{f}_{0}^{(k)}(r)|=E[T_{0}^{k}e^{-rT_{0}}]\leq(k/(er))^{k}\text{.}$</span></p>
</div>
</div>
<div id="S5.SS5.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS5.p2" class="ltx_para">
<p id="S5.SS5.p2.1" class="ltx_p"><span id="S5.SS5.p2.1.1" class="ltx_text">Set $\mu=(1-p)/(rp)\text{,}$ $\epsilon=\theta/\mu\text{,}$ and expand $\hat{f}_{0}(r+\epsilon)=p+D_{1}\epsilon+O(\epsilon^{2})\text{.}$ Then $N(\epsilon)=(r+\epsilon)(p+D_{1}\epsilon+O(\epsilon^{2}))=rp+(p+rD_{1})\epsilon+O(\epsilon^{2})$ and $D(\epsilon)=\epsilon+r(p+D_{1}\epsilon+O(\epsilon^{2}))=rp+(1+rD_{1})\epsilon+O(\epsilon^{2})\text{.}$ Dividing by $rp$ and substituting $\epsilon=\theta rp/(1-p)$ yields the ratio $(1+\alpha\theta+R_{N})/(1+\beta\theta+R_{D})$ with $|R_{N}|,|R_{D}|=O(\theta^{2}p)\text{.}$ The identity $1+\alpha-\beta=0$ ensures the $\theta^{1}$-coefficient vanishes. The remainder analysis is identical to the proof of Theorem <a href="#S4.Thmtheorem4" title="Theorem 4.4 (Laplace expansion). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.4</span></a>.
∎</span></p>
</div>
</div>
<div id="S5.Thmtheorem10" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem10.2" class="ltx_text ltx_font_bold">Lemma 5.10</span></span><span id="S5.Thmtheorem10.3" class="ltx_text ltx_font_bold"> </span>(Continuous-time $\alpha\to 0$)<span id="S5.Thmtheorem10.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmtheorem10.p1" class="ltx_para">
<p id="S5.Thmtheorem10.p1.1" class="ltx_p"><span id="S5.Thmtheorem10.p1.1.1" class="ltx_text ltx_font_italic">For fixed $r&gt;0\text{,}$ $|\alpha|=O(p|\ln p|)$ as $p=\hat{f}_{0}(r)\to 0\text{.}$</span></p>
</div>
</div>
<div id="S5.SS5.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS5.p3" class="ltx_para">
<p id="S5.SS5.p3.1" class="ltx_p"><span id="S5.SS5.p3.1.1" class="ltx_text">Set $Y=e^{-rT_{0}}\in(0,1]\text{,}$ so $p=E[Y]$ and $rD_{1}=E[Y\ln Y]$ (since $Y\ln Y=-rT_{0}e^{-rT_{0}}$), giving $-rD_{1}=E[-Y\ln Y]\text{.}$ Since $\varphi(x)=-x\ln x$ is concave, Jensen’s inequality gives $E[-Y\ln Y]\leq-p\ln p\text{.}$ Hence $|p+rD_{1}|\leq p+E[-Y\ln Y]\leq p(1+|\ln p|)\text{,}$ so $|\alpha|=O(p|\ln p|)\text{.}$
∎</span></p>
</div>
</div>
<div id="S5.SS5.p4" class="ltx_para">
<p id="S5.SS5.p4.1" class="ltx_p">In continuous time, the lattice error that contributes the $\Theta(p)$ floor in the discrete two-sided bound (Theorem <a href="#S4.Thmtheorem15" title="Theorem 4.15 (Two-sided bound). ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.15</span></a>) disappears: when $T_{0}$ has a continuous distribution, so does $T\text{,}$ and the CDF of $W$ has no jumps. The sharp rate therefore reduces to $|\alpha|$ alone. The following lemma provides the necessary moment convergence for the Bridge Theorem.</p>
</div>
<div id="S5.Thmtheorem11" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem11.2" class="ltx_text ltx_font_bold">Lemma 5.11</span></span><span id="S5.Thmtheorem11.3" class="ltx_text ltx_font_bold"> </span>(Escape to infinity)<span id="S5.Thmtheorem11.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmtheorem11.p1" class="ltx_para">
<p id="S5.Thmtheorem11.p1.1" class="ltx_p"><span id="S5.Thmtheorem11.p1.1.1" class="ltx_text ltx_font_italic">Fix $r&gt;0\text{.}$ Let $(T_{0,n})$ be a sequence of positive random variables with $p_{n}=E[e^{-rT_{0,n}}]\to 0\text{.}$ Then $T_{0,n}\to\infty$ in probability. Consequently, for each fixed $t\geq 0\text{,}$ $P(A_{n}\geq t)\to e^{-rt}\text{,}$ and for each fixed integer $k\geq 1\text{,}$ $E[A_{n}^{k}]\to k!/r^{k}\text{.}$</span></p>
</div>
</div>
<div id="S5.SS5.4" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS5.p5" class="ltx_para">
<p id="S5.SS5.p5.1" class="ltx_p"><span id="S5.SS5.p5.1.1" class="ltx_text">For any fixed $x&gt;0\text{,}$ $p_{n}\geq e^{-rx}P(T_{0,n}\leq x)\text{,}$ so $P(T_{0,n}\leq x)\leq e^{rx}p_{n}\to 0\text{.}$</span></p>
</div>
<div id="S5.SS5.p6" class="ltx_para">
<p id="S5.SS5.p6.1" class="ltx_p"><span id="S5.SS5.p6.1.1" class="ltx_text">For the failed-attempt tail: since $\tau\sim\operatorname{Exp}(r)$ is independent of $T_{0,n}\text{,}$</span></p>
<table id="S5.Ex48" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$P(A_{n}\geq t)=\frac{P(\tau\geq t,\,\tau&lt;T_{0,n})}{1-p_{n}}=\frac{E[(e^{-rt}-e^{-rT_{0,n}})\mathbf{1}_{\{T_{0,n}&gt;t\}}]}{1-p_{n}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS5.p6.2" class="ltx_p"><span id="S5.SS5.p6.2.1" class="ltx_text">As $n\to\infty\text{:}$ $E[e^{-rT_{0,n}}\mathbf{1}_{\{T_{0,n}&gt;t\}}]\leq p_{n}\to 0$ and $P(T_{0,n}&gt;t)\to 1\text{,}$ so the numerator tends to $e^{-rt}$ and the denominator to $1\text{.}$</span></p>
</div>
<div id="S5.SS5.p7" class="ltx_para">
<p id="S5.SS5.p7.1" class="ltx_p"><span id="S5.SS5.p7.1.1" class="ltx_text">The uniform bound $P(A_{n}\geq t)\leq e^{-rt}/(1-p_{n})\leq 2e^{-rt}$ (for $p_{n}\leq 1/2$) provides a dominator for $t^{k-1}P(A_{n}\geq t)\text{,}$ so dominated convergence gives $E[A_{n}^{k}]=k\int_{0}^{\infty}t^{k-1}P(A_{n}\geq t)\,dt\to k!/r^{k}\text{.}$
∎</span></p>
</div>
</div>
<div id="S5.Thmtheorem12" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem12.2" class="ltx_text ltx_font_bold">Theorem 5.12</span></span><span id="S5.Thmtheorem12.3" class="ltx_text ltx_font_bold"> </span>(Continuous-time sharp bound)<span id="S5.Thmtheorem12.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S5.Thmtheorem12.p1" class="ltx_para">
<p id="S5.Thmtheorem12.p1.1" class="ltx_p"><span id="S5.Thmtheorem12.p1.1.1" class="ltx_text ltx_font_italic">Under Poisson resetting at rate $r\text{,}$ for $T_{0}$ with continuous distribution, and $|\alpha|/p\to\infty$ as $p\to 0\text{:}$</span></p>
<table id="S5.E45" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}\!\left(\frac{T}{E[T]},\,\operatorname{Exp}(1)\right)\in\bigl[1-o(1),\;2+o(1)\bigr]\cdot|\alpha|.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(45)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S5.SS5.5" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS5.p8" class="ltx_para">
<p id="S5.SS5.p8.1" class="ltx_p"><em id="S5.SS5.p8.1.1" class="ltx_emph ltx_font_italic">Upper bound.</em><span id="S5.SS5.p8.1.2" class="ltx_text"> 
The Bridge Theorem (Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a>) applies in continuous time: its three steps—Brown’s bound, scaling, and additive perturbation—require only that $N\sim\operatorname{Geom}_{0}(p)\text{,}$ the $A_{i}$ be i.i.d. positive with $E[A^{2}]&lt;\infty\text{,}$ and $B$ be independent of $U\text{;}$ none assumes integrality. The tail bound $P(A\geq t)\leq e^{-rt}/(1-p)$ from the proof of Lemma <a href="#S5.Thmtheorem11" title="Lemma 5.11 (Escape to infinity). ‣ 5.5 Exponential Approximation ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.11</span></a> gives $E[A^{k}]&lt;\infty$ for all $k\text{,}$ verifying Brown’s moment condition. By Lemma <a href="#S5.Thmtheorem11" title="Lemma 5.11 (Escape to infinity). ‣ 5.5 Exponential Approximation ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.11</span></a>, $\rho_{j}=E[A^{j}]/E[A]^{j}\to j!$ as $p\to 0\text{,}$ so the Brown constant $C_{1}=O(1)\text{.}$ By (<a href="#S5.E43" title="In 5.5 Exponential Approximation ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">43</span></a>), $2b/\mu\leq 2|\alpha|+2p/(1-p)\text{.}$ Hence $d_{\mathrm{K}}\leq C_{1}p+2|\alpha|+2p/(1-p)=(2+o(1))|\alpha|\text{,}$ using $p=o(|\alpha|)\text{.}$</span></p>
</div>
<div id="S5.SS5.p9" class="ltx_para">
<p id="S5.SS5.p9.1" class="ltx_p"><em id="S5.SS5.p9.1.1" class="ltx_emph ltx_font_italic">Lower bound.</em><span id="S5.SS5.p9.1.2" class="ltx_text"> 
Apply the Laplace expansion (Theorem <a href="#S5.Thmtheorem9" title="Theorem 5.9 (Continuous-time Laplace expansion). ‣ 5.5 Exponential Approximation ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.9</span></a>) with $\theta=\theta_{n}=(|\alpha|/(2p))^{1/2}\to\infty\text{.}$ The validity condition $\epsilon=\theta rp/(1-p)\to 0$ holds since $\epsilon=O(r\sqrt{p|\alpha|})\to 0$ by Lemma <a href="#S5.Thmtheorem10" title="Lemma 5.10 (Continuous-time 𝛼→0). ‣ 5.5 Exponential Approximation ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.10</span></a>. The error terms satisfy $p\theta^{2}/(1+\theta)\leq p\theta=\sqrt{p|\alpha|/2}=o(|\alpha|)$ and $|\alpha|^{2}\theta^{3}/(1+\theta)^{3}\leq|\alpha|^{2}=o(|\alpha|)\text{.}$ The leading term: $|\alpha|\theta^{2}/(1+\theta)^{2}=(1-o(1))|\alpha|$ since $\theta\to\infty\text{.}$ By (<a href="#S4.E33" title="In Proof of the lower bound. ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">33</span></a>), $d_{\mathrm{K}}\geq(1-o(1))|\alpha|\text{.}$
∎</span></p>
</div>
</div>
<div id="S5.Thmtheorem13" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S5.Thmtheorem13.2" class="ltx_text ltx_font_italic">Remark 5.13</span></span><span id="S5.Thmtheorem13.3" class="ltx_text ltx_font_italic"> </span>(Disappearance of the lattice error)<span id="S5.Thmtheorem13.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S5.Thmtheorem13.p1" class="ltx_para">
<p id="S5.Thmtheorem13.p1.1" class="ltx_p">In the discrete two-sided bound (Theorem <a href="#S4.Thmtheorem15" title="Theorem 4.15 (Two-sided bound). ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.15</span></a>), the template is $p+|\alpha|$ because $W$ takes values in $(1/\mu)\mathbb{Z}_{&gt;0}\text{,}$ creating an irreducible $\Omega(p)$ lattice error (Proposition <a href="#S4.Thmtheorem16" title="Proposition 4.16 (Counterexample: 𝑝 cannot be dropped). ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.16</span></a>). In continuous time, this error vanishes. When $|\alpha|/p\to\infty\text{,}$ the dominant error source is the successful-attempt perturbation encoded by $\alpha\text{;}$ when $\alpha\approx 0\text{,}$ a residual $O(p)$ error from higher-order terms persists.</p>
</div>
</div>
</section>
<section id="S5.SS6" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="worked-example-brownian-first-passage"><span class="ltx_tag ltx_tag_subsection">5.6 </span>Worked Example: Brownian First Passage</h3>

<div id="S5.SS6.p1" class="ltx_para">
<p id="S5.SS6.p1.1" class="ltx_p">To illustrate the continuous-time theory concretely, consider a Brownian particle starting at $x_{0}&gt;0$ with an absorbing barrier at the origin, subject to Poisson resetting at rate $r\text{.}$ This is the original model of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib15" title="" class="ltx_ref">16</a>]</cite>. The base first-passage time has Laplace transform $\hat{f}_{0}(\lambda)=e^{-x_{0}\sqrt{2\lambda}}\text{,}$ giving</p>
<table id="S5.Ex49" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p=e^{-x_{0}\sqrt{2r}},\qquad E[T]=\frac{e^{x_{0}\sqrt{2r}}-1}{r},\qquad D_{1}=-\frac{x_{0}}{\sqrt{2r}}\,e^{-x_{0}\sqrt{2r}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S5.SS6.p1.2" class="ltx_p">The perturbation parameter:</p>
<table id="S5.E46" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha=\frac{(1-x_{0}\sqrt{r/2})\,e^{-x_{0}\sqrt{2r}}}{1-e^{-x_{0}\sqrt{2r}}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(46)</span></td></tr></tbody>
</table>
<p id="S5.SS6.p1.3" class="ltx_p">As $x_{0}\sqrt{r}\to\infty\text{:}$ $|\alpha|\sim x_{0}\sqrt{r/2}\cdot p\text{,}$ so $|\alpha|/p\to\infty$—the perturbation term dominates, and Theorem <a href="#S5.Thmtheorem12" title="Theorem 5.12 (Continuous-time sharp bound). ‣ 5.5 Exponential Approximation ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.12</span></a> gives $d_{\mathrm{K}}\in[1-o(1),2+o(1)]\cdot|\alpha|\text{.}$</p>
</div>
<div id="S5.SS6.p2" class="ltx_para">
<p id="S5.SS6.p2.1" class="ltx_p">At the critical point $x_{0}\sqrt{r/2}=1\text{,}$ the perturbation parameter $\alpha$ vanishes exactly: the leading $\alpha\theta^{2}/(1+\theta)^{2}$ term in (<a href="#S5.E44" title="In Theorem 5.9 (Continuous-time Laplace expansion). ‣ 5.5 Exponential Approximation ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">44</span></a>) disappears, leaving only higher-order contributions. This does not imply distributional proximity to $\operatorname{Exp}(1)\text{:}$ at the critical point $p=e^{-2}$ is a fixed constant (not tending to zero), so the exponential limit theorem does not apply.</p>
</div>
</section>
<section id="S5.SS7" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="discretecontinuous-correspondence"><span class="ltx_tag ltx_tag_subsection">5.7 </span>Discrete–Continuous Correspondence</h3>

<div id="S5.SS7.p1" class="ltx_para">
<p id="S5.SS7.p1.1" class="ltx_p">Table <a href="#S5.T1" title="Table 1 ‣ 5.7 Discrete–Continuous Correspondence ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a> summarizes the parallel between the discrete and continuous theories. Every structural feature—affine form, coefficient matching, DRP, perturbation identity, Laplace expansion, sharp rate—carries over. The sole qualitative difference lies in the characterization’s scope and the sharp-rate template.</p>
</div>
<figure id="S5.T1" class="ltx_table">
<table id="S5.T1.2" class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr id="S5.T1.2.1" class="ltx_tr">
<th id="S5.T1.2.1.1" class="ltx_td ltx_th ltx_th_row ltx_border_tt" style="padding-top:1.15pt;padding-bottom:1.15pt;"></th>
<td id="S5.T1.2.1.2" class="ltx_td ltx_align_left ltx_border_tt" style="padding-top:1.15pt;padding-bottom:1.15pt;"><span id="S5.T1.2.1.2.1" class="ltx_text ltx_font_bold" style="font-size:90%;">Discrete time</span></td>
<td id="S5.T1.2.1.3" class="ltx_td ltx_align_left ltx_border_tt" style="padding-top:1.15pt;padding-bottom:1.15pt;"><span id="S5.T1.2.1.3.1" class="ltx_text ltx_font_bold" style="font-size:90%;">Continuous time</span></td></tr>
<tr id="S5.T1.2.2" class="ltx_tr">
<th id="S5.T1.2.2.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.2.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Transform</em></th>
<td id="S5.T1.2.2.2" class="ltx_td ltx_align_left ltx_border_t" style="padding-top:1.15pt;padding-bottom:1.15pt;"><span id="S5.T1.2.2.2.1" class="ltx_text" style="font-size:90%;">PGF $G_{T}(w)=E[w^{T}]$</span></td>
<td id="S5.T1.2.2.3" class="ltx_td ltx_align_left ltx_border_t" style="padding-top:1.15pt;padding-bottom:1.15pt;"><span id="S5.T1.2.2.3.1" class="ltx_text" style="font-size:90%;">Laplace $\hat{f}_{T}(\lambda)=E[e^{-\lambda T}]$</span></td></tr>
<tr id="S5.T1.2.3" class="ltx_tr">
<th id="S5.T1.2.3.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.3.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Normalization point</em></th>
<td id="S5.T1.2.3.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$w=1$</td>
<td id="S5.T1.2.3.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$\lambda=0$</td></tr>
<tr id="S5.T1.2.4" class="ltx_tr">
<th id="S5.T1.2.4.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.4.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Shift</em></th>
<td id="S5.T1.2.4.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$u=ws$<span id="S5.T1.2.4.2.1" class="ltx_text" style="font-size:90%;"> (multiplicative)</span></td>
<td id="S5.T1.2.4.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$\sigma=\lambda+r$<span id="S5.T1.2.4.3.1" class="ltx_text" style="font-size:90%;"> (additive)</span></td></tr>
<tr id="S5.T1.2.5" class="ltx_tr">
<th id="S5.T1.2.5.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.5.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Catastrophe parameter</em></th>
<td id="S5.T1.2.5.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$q\in(0,1)$</td>
<td id="S5.T1.2.5.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$r&gt;0$</td></tr>
<tr id="S5.T1.2.6" class="ltx_tr">
<th id="S5.T1.2.6.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.6.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Success probability</em></th>
<td id="S5.T1.2.6.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$p=g(s)$</td>
<td id="S5.T1.2.6.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$p=\hat{f}_{0}(r)$</td></tr>
<tr id="S5.T1.2.7" class="ltx_tr">
<th id="S5.T1.2.7.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.7.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">$E[T]$</em></th>
<td id="S5.T1.2.7.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$(1-p)/(qp)$</td>
<td id="S5.T1.2.7.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$(1-p)/(rp)$</td></tr>
<tr id="S5.T1.2.8" class="ltx_tr">
<th id="S5.T1.2.8.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.8.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Coefficient match</em></th>
<td id="S5.T1.2.8.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$\alpha_{N}(1)=\alpha_{D}(1)=q$</td>
<td id="S5.T1.2.8.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$\alpha_{N}(0)=\alpha_{D}(0)=r$</td></tr>
<tr id="S5.T1.2.9" class="ltx_tr">
<th id="S5.T1.2.9.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.9.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">DRP ($k\geq 2$)</em></th>
<td id="S5.T1.2.9.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$\Delta_{k}=-ks^{k-1}D_{k-1}$</td>
<td id="S5.T1.2.9.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$\Delta_{k}=kD_{k-1}$</td></tr>
<tr id="S5.T1.2.10" class="ltx_tr">
<th id="S5.T1.2.10.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.10.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Perturbation $\alpha$</em></th>
<td id="S5.T1.2.10.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$s(p-qD_{1})/(1-p)$</td>
<td id="S5.T1.2.10.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$(p+rD_{1})/(1-p)$</td></tr>
<tr id="S5.T1.2.11" class="ltx_tr">
<th id="S5.T1.2.11.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.11.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Fundamental identity</em></th>
<td id="S5.T1.2.11.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$1+\alpha-\beta=0$</td>
<td id="S5.T1.2.11.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$1+\alpha-\beta=0$</td></tr>
<tr id="S5.T1.2.12" class="ltx_tr">
<th id="S5.T1.2.12.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.12.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Laplace expansion</em></th>
<td id="S5.T1.2.12.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$\alpha\theta^{2}/(1+\theta)^{2}+\text{h.o.t.}$</td>
<td id="S5.T1.2.12.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$\alpha\theta^{2}/(1+\theta)^{2}+\text{h.o.t.}$</td></tr>
<tr id="S5.T1.2.13" class="ltx_tr">
<th id="S5.T1.2.13.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.13.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Bridge Theorem</em></th>
<td id="S5.T1.2.13.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$d_{\mathrm{K}}\leq C_{1}p+2b/\mu$</td>
<td id="S5.T1.2.13.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$d_{\mathrm{K}}\leq C_{1}p+2b/\mu$</td></tr>
<tr id="S5.T1.2.14" class="ltx_tr">
<th id="S5.T1.2.14.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.14.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Sharp-rate template</em></th>
<td id="S5.T1.2.14.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$p+|\alpha|$</td>
<td id="S5.T1.2.14.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;">$|\alpha|$<span id="S5.T1.2.14.3.1" class="ltx_text" style="font-size:90%;"> (no lattice error)</span></td></tr>
<tr id="S5.T1.2.15" class="ltx_tr">
<th id="S5.T1.2.15.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.15.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Characterizes</em></th>
<td id="S5.T1.2.15.2" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;"><span id="S5.T1.2.15.2.1" class="ltx_text" style="font-size:90%;">geometric tail</span></td>
<td id="S5.T1.2.15.3" class="ltx_td ltx_align_left" style="padding-top:1.15pt;padding-bottom:1.15pt;"><span id="S5.T1.2.15.3.1" class="ltx_text" style="font-size:90%;">Poisson (full memoryless)</span></td></tr>
<tr id="S5.T1.2.16" class="ltx_tr">
<th id="S5.T1.2.16.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb" style="padding-top:1.15pt;padding-bottom:1.15pt;"><em id="S5.T1.2.16.1.1" class="ltx_emph ltx_font_italic" style="font-size:90%;">Gap</em></th>
<td id="S5.T1.2.16.2" class="ltx_td ltx_align_left ltx_border_bb" style="padding-top:1.15pt;padding-bottom:1.15pt;">$h_{1}$<span id="S5.T1.2.16.2.1" class="ltx_text" style="font-size:90%;"> free</span></td>
<td id="S5.T1.2.16.3" class="ltx_td ltx_align_left ltx_border_bb" style="padding-top:1.15pt;padding-bottom:1.15pt;"><span id="S5.T1.2.16.3.1" class="ltx_text" style="font-size:90%;">none</span></td></tr>
</tbody>
</table>
<figcaption class="ltx_caption ltx_centering" style="font-size:90%;"><span class="ltx_tag ltx_tag_table">Table 1: </span>Discrete–continuous correspondence. The two theories share every structural feature. The characterization sharpens in continuous time (the geometric-tail gap closes, Remark <a href="#S5.Thmtheorem8" title="Remark 5.8 (Why the geometric-tail gap closes). ‣ 5.4 Characterization: Affine Laplace Structure Is Poisson ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.8</span></a>), and the sharp-rate template simplifies (the lattice error vanishes for continuous $T_{0}\text{,}$ Remark <a href="#S5.Thmtheorem13" title="Remark 5.13 (Disappearance of the lattice error). ‣ 5.5 Exponential Approximation ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.13</span></a>).</figcaption>
</figure>
</section>
</section>
<section id="S6" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="application-coupon-collector-with-reset"><span class="ltx_tag ltx_tag_section">6 </span>Application: Coupon Collector with Reset</h2>

<div id="S6.p1" class="ltx_para">
<p id="S6.p1.1" class="ltx_p">The general theory of §§<a href="#S2" title="2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>–<a href="#S4" title="4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a> applies to any base process $T_{0}\text{.}$ We now instantiate it to the coupon collector problem with reset, obtaining closed-form moments, a sharp Kolmogorov bound that closes the logarithmic gap, and a discontinuous phase transition in the limit law. The pattern throughout is: compute CCP-specific quantities ($p\text{,}$ $D_{1}\text{,}$ $D_{2}\text{,}$ $\alpha$), then substitute into general formulas. The sole exception is the lower bound in the sharp Kolmogorov estimate (§<a href="#S6.SS4" title="6.4 Phase Transition and Sharp Kolmogorov Bound ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.4</span></a>), which requires a product-structure argument specific to the CCP.</p>
</div>
<section id="S6.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="model"><span class="ltx_tag ltx_tag_subsection">6.1 </span>Model</h3>

<div id="S6.SS1.p1" class="ltx_para">
<p id="S6.SS1.p1.1" class="ltx_p">A deck contains $n+m$ coupon types: types $1,\ldots,n$ are <em id="S6.SS1.p1.1.1" class="ltx_emph ltx_font_italic">standard</em>, and types $n+1,\ldots,n+m$ are <em id="S6.SS1.p1.1.2" class="ltx_emph ltx_font_italic">reset</em>. At each step, one type is drawn uniformly at random with replacement. Standard draws accumulate; any reset draw erases all collected coupons. The game ends when all $n$ standard types have been collected. This is the framework of §<a href="#S2.SS1" title="2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.1</span></a> with $T_{0}$ the classical coupon collector completion time and</p>
<table id="S6.Ex50" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$q=\frac{m}{n+m},\qquad s=\frac{n}{n+m}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS1.p1.2" class="ltx_p">A closely related model was studied by <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib24" title="" class="ltx_ref">24</a>]</cite>, who derived expected values via Markov chain methods; our contribution is the distributional theory.</p>
</div>
<div id="S6.SS1.p2" class="ltx_para">
<p id="S6.SS1.p2.1" class="ltx_p"><span id="S6.SS1.p2.1.1" class="ltx_text ltx_font_bold">Notation.</span>  $C=\binom{n+m}{n}\text{;}$  $H=\sum_{j=m+1}^{n+m}1/j=H_{n+m}-H_{m}\text{;}$  $H^{(r)}=\sum_{j=m+1}^{n+m}1/j^{r}=H^{(r)}_{n+m}-H^{(r)}_{m}\text{.}$</p>
</div>
</section>
<section id="S6.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="specialization-of-the-pgf-data"><span class="ltx_tag ltx_tag_subsection">6.2 </span>Specialization of the PGF Data</h3>

<div id="S6.SS2.p1" class="ltx_para">
<p id="S6.SS2.p1.1" class="ltx_p">The classical CCP has $T_{0}=X_{1}+\cdots+X_{n}$ with $X_{k}\sim\operatorname{Geom}_{1}((n{-}k{+}1)/n)$ independent, giving</p>
<table id="S6.E47" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$g(z)=\prod_{k=1}^{n}\frac{(n{-}k{+}1)z/n}{1-(k{-}1)z/n}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(47)</span></td></tr></tbody>
</table>
<p id="S6.SS2.p1.2" class="ltx_p">The general theory requires three inputs: $p=g(s)\text{,}$ $D_{1}=g^{\prime}(s)\text{,}$ and $D_{2}=g^{\prime\prime}(s)\text{.}$</p>
</div>
<div id="S6.Thmtheorem1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmtheorem1.2" class="ltx_text ltx_font_bold">Lemma 6.1</span></span><span id="S6.Thmtheorem1.3" class="ltx_text ltx_font_bold"> </span>(Success probability)<span id="S6.Thmtheorem1.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S6.Thmtheorem1.p1" class="ltx_para">
<p id="S6.Thmtheorem1.p1.1" class="ltx_p">$p=g(s)=1/C=1/\binom{n+m}{n}$<span id="S6.Thmtheorem1.p1.1.1" class="ltx_text ltx_font_italic">.</span></p>
</div>
</div>
<div id="S6.SS2.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS2.p2" class="ltx_para">
<p id="S6.SS2.p2.1" class="ltx_p"><em id="S6.SS2.p2.1.1" class="ltx_emph ltx_font_italic">Algebraic.</em><span id="S6.SS2.p2.1.2" class="ltx_text">  At $z=s=n/(n+m)\text{,}$ each factor of (<a href="#S6.E47" title="In 6.2 Specialization of the PGF Data ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">47</span></a>) evaluates to $(n{-}k{+}1)/(n{+}m{-}k{+}1)\text{.}$ The product telescopes: $\prod_{k=1}^{n}(n{-}k{+}1)/(n{+}m{-}k{+}1)=n!\,m!/(n{+}m)!=1/C\text{.}$</span></p>
</div>
<div id="S6.SS2.p3" class="ltx_para">
<p id="S6.SS2.p3.1" class="ltx_p"><em id="S6.SS2.p3.1.1" class="ltx_emph ltx_font_italic">Combinatorial.</em><span id="S6.SS2.p3.1.2" class="ltx_text">  An attempt succeeds if and only if all $n$ standard types appear before any reset type in the first-appearance permutation. By symmetry of i.i.d. uniform draws, this probability is $n!\,m!/(n+m)!=1/C\text{.}$
∎</span></p>
</div>
</div>
<div id="S6.SS2.p4" class="ltx_para">
<p id="S6.SS2.p4.1" class="ltx_p">The derivatives are computed by logarithmic differentiation, exploiting the product structure $\log g=\sum_{k=1}^{n}\log G_{X_{k}}\text{.}$</p>
</div>
<div id="S6.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmtheorem2.2" class="ltx_text ltx_font_bold">Lemma 6.2</span></span><span id="S6.Thmtheorem2.3" class="ltx_text ltx_font_bold"> </span>(PGF derivatives at $z=s$)<span id="S6.Thmtheorem2.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S6.Thmtheorem2.p1" class="ltx_para">
<table id="S6.E48" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D_{1}=g^{\prime}(s)=\frac{(n+m)^{2}\,H}{n\,C},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(48)</span></td></tr></tbody>
</table>
<table id="S6.E49" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D_{2}=g^{\prime\prime}(s)=\frac{(n+m)^{3}}{n^{2}\,C}\bigl((n+m)(H^{2}+H^{(2)})-2H\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(49)</span></td></tr></tbody>
</table>
<p id="S6.Thmtheorem2.p1.1" class="ltx_p"><span id="S6.Thmtheorem2.p1.1.1" class="ltx_text ltx_font_italic">More generally, the $r$-th logarithmic derivative of $g$ at $z=s$ is a polynomial in $H,H^{(2)},\ldots,H^{(r)}$ with rational coefficients in $(n,m)\text{.}$</span></p>
</div>
</div>
<div id="S6.SS2.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof sketch.</h6>
<div id="S6.SS2.p5" class="ltx_para">
<p id="S6.SS2.p5.1" class="ltx_p"><span id="S6.SS2.p5.1.1" class="ltx_text">Write $r_{k}(z)=G^{\prime}_{X_{k}}(z)/G_{X_{k}}(z)=1/(z\varphi_{k}(z))$ with $\varphi_{k}(z)=1-(k{-}1)z/n\text{.}$ At $z=s\text{:}$ $\varphi_{k}(s)=(n{+}m{-}k{+}1)/(n{+}m)\text{,}$ so $r_{k}(s)=(n{+}m)^{2}/(n(n{+}m{-}k{+}1))\text{.}$ Setting $j=n{+}m{-}k{+}1\text{:}$</span></p>
<table id="S6.Ex51" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(\log g)^{\prime}(s)=\sum_{k=1}^{n}r_{k}(s)=\frac{(n+m)^{2}}{n}\sum_{j=m+1}^{n+m}\frac{1}{j}=\frac{(n+m)^{2}\,H}{n}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS2.p5.2" class="ltx_p"><span id="S6.SS2.p5.2.1" class="ltx_text">Then $D_{1}=g(s)\cdot(\log g)^{\prime}(s)\text{.}$ The second derivative follows from $g^{\prime\prime}=g[(\log g)^{\prime\prime}+((\log g)^{\prime})^{2}]$ and an analogous computation of $(\log g)^{\prime\prime}(s)\text{,}$ which introduces $H^{(2)}$ via the partial fractions of $r^{\prime}_{k}(s)\text{.}$
∎</span></p>
</div>
</div>
<div id="S6.SS2.p6" class="ltx_para">
<p id="S6.SS2.p6.1" class="ltx_p">The pattern is transparent: the $r$-th logarithmic derivative introduces $H^{(r)}$ because each differentiation of $r_{k}(z)=1/(z\varphi_{k}(z))$ adds one power of $1/\varphi_{k}(s)=(n{+}m)/j\text{,}$ and summing over $k$ produces $\sum j^{-r}\text{.}$</p>
</div>
</section>
<section id="S6.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="moments"><span class="ltx_tag ltx_tag_subsection">6.3 </span>Moments</h3>

<div id="S6.SS3.p1" class="ltx_para">
<p id="S6.SS3.p1.1" class="ltx_p">Substituting the CCP data $(p,q,D_{1})$ into the general formulas of §<a href="#S2.SS2" title="2.2 Affine Structure and the Derivative Reduction Principle ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a> gives closed-form first two moments:</p>
<table id="S6.E50" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[T]=\frac{n+m}{m}(C-1),\qquad\operatorname{Var}(T)=\frac{n+m}{m^{2}}\bigl((C-1)((n{+}m)C+n)-2m(n{+}m)CH\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(50)</span></td></tr></tbody>
</table>
<p id="S6.SS3.p1.2" class="ltx_p">For $m=1\text{:}$ $E[T]=n(n+1)\text{.}$ For fixed $m$ as $n\to\infty\text{:}$ $E[T]\sim n^{m+1}/(m\cdot m!)\text{.}$ The variance involves both $p=1/C$ and $D_{1}$—but not $D_{2}$—exactly as the DRP guarantees. Higher moments follow analogously from the recursion (<a href="#S2.E15" title="In Corollary 2.8 (Moment recursion). ‣ 2.3 Moment Recursion and the Complexity Staircase ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">15</span></a>). In particular, the third centered moment is the first level at which $D_{2}\text{,}$ and hence $H^{(2)}\text{,}$ enters; more generally, the $k$-th centered moment first involves the new harmonic statistic $H^{(k-1)}\text{.}$</p>
</div>
<div id="S6.SS3.p2" class="ltx_para">
<p id="S6.SS3.p2.1" class="ltx_p">The staircase of §<a href="#S2.SS3" title="2.3 Moment Recursion and the Complexity Staircase ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.3</span></a> takes a particularly illuminating form:</p>
<table id="S6.SS3.p2.2" class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr id="S6.SS3.p2.2.1" class="ltx_tr">
<th id="S6.SS3.p2.2.1.1" class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_border_tt"><span id="S6.SS3.p2.2.1.1.1" class="ltx_text ltx_font_bold">Moment of $T$</span></th>
<th id="S6.SS3.p2.2.1.2" class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span id="S6.SS3.p2.2.1.2.1" class="ltx_text ltx_font_bold">New input (DRP)</span></th>
<th id="S6.SS3.p2.2.1.3" class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span id="S6.SS3.p2.2.1.3.1" class="ltx_text ltx_font_bold">CCP realization</span></th>
<th id="S6.SS3.p2.2.1.4" class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span id="S6.SS3.p2.2.1.4.1" class="ltx_text ltx_font_bold">Origin</span></th></tr>
</thead>
<tbody class="ltx_tbody">
<tr id="S6.SS3.p2.2.2" class="ltx_tr">
<td id="S6.SS3.p2.2.2.1" class="ltx_td ltx_align_left ltx_border_t" style="padding-bottom: 2.0pt;">$E[T]$</td>
<td id="S6.SS3.p2.2.2.2" class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom: 2.0pt;">$g(s)$</td>
<td id="S6.SS3.p2.2.2.3" class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom: 2.0pt;">$C=\binom{n+m}{n}$</td>
<td id="S6.SS3.p2.2.2.4" class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom: 2.0pt;">product telescope</td></tr>
<tr id="S6.SS3.p2.2.3" class="ltx_tr">
<td id="S6.SS3.p2.2.3.1" class="ltx_td ltx_align_left" style="padding-bottom: 2.0pt;">$\operatorname{Var}(T)$</td>
<td id="S6.SS3.p2.2.3.2" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;">$+g^{\prime}(s)$</td>
<td id="S6.SS3.p2.2.3.3" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;">$+H=\sum 1/j$</td>
<td id="S6.SS3.p2.2.3.4" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;">1st log-derivative</td></tr>
<tr id="S6.SS3.p2.2.4" class="ltx_tr">
<td id="S6.SS3.p2.2.4.1" class="ltx_td ltx_align_left" style="padding-bottom: 2.0pt;">$\mu_{3}(T)$</td>
<td id="S6.SS3.p2.2.4.2" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;">$+g^{\prime\prime}(s)$</td>
<td id="S6.SS3.p2.2.4.3" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;">$+H^{(2)}=\sum 1/j^{2}$</td>
<td id="S6.SS3.p2.2.4.4" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;">2nd log-derivative</td></tr>
<tr id="S6.SS3.p2.2.5" class="ltx_tr">
<td id="S6.SS3.p2.2.5.1" class="ltx_td ltx_align_left ltx_border_bb">$\mu_{k}(T)$</td>
<td id="S6.SS3.p2.2.5.2" class="ltx_td ltx_align_center ltx_border_bb">$+g^{(k-1)}(s)$</td>
<td id="S6.SS3.p2.2.5.3" class="ltx_td ltx_align_center ltx_border_bb">$+H^{(k-1)}=\sum 1/j^{k-1}$</td>
<td id="S6.SS3.p2.2.5.4" class="ltx_td ltx_align_center ltx_border_bb">$(k{-}1)$-th log-deriv.</td></tr>
</tbody>
</table>
<p id="S6.SS3.p2.3" class="ltx_p">Each row adds exactly one new finite harmonic sum: $H^{(k-1)}=\sum_{j=m+1}^{n+m}j^{-(k-1)}\text{.}$ The CCP thus provides the sharpest illustration of the harmonic complexity staircase—a feature absent in base processes with rational PGF structure (§<a href="#S7" title="7 Application: Multi-Phase Task with Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a>).</p>
</div>
</section>
<section id="S6.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="phase-transition-and-sharp-kolmogorov-bound"><span class="ltx_tag ltx_tag_subsection">6.4 </span>Phase Transition and Sharp Kolmogorov Bound</h3>

<div id="S6.SS4.p1" class="ltx_para">
<p id="S6.SS4.p1.1" class="ltx_p">The CCP perturbation parameter, obtained by substituting $p=1/C$ and $qD_{1}=m(n+m)H/(nC)$ into Definition <a href="#S4.Thmtheorem1" title="Definition 4.1 (Perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.1</span></a>, is</p>
<table id="S6.E51" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha=\frac{s-mH}{C-1},\qquad|\alpha|\sim\frac{m!\,m\ln n}{n^{m}}\quad\text{as }n\to\infty.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(51)</span></td></tr></tbody>
</table>
<p id="S6.SS4.p1.2" class="ltx_p">Since $p=1/C\sim m!/n^{m}$ and $|\alpha|\sim m!\,m\ln n/n^{m}\text{,}$ the ratio $p/|\alpha|\sim 1/(m\ln n)\to 0\text{:}$ the perturbation term dominates.</p>
</div>
<div id="S6.SS4.p2" class="ltx_para ltx_noindent">
<p id="S6.SS4.p2.1" class="ltx_p"><span id="S6.SS4.p2.1.1" class="ltx_text ltx_font_bold">The Gumbel-to-Exponential phase transition.</span> 
For the classical CCP ($m=0$), the limit law is Gumbel: $(T_{0}-n\ln n)/n\xrightarrow{d}\text{Gumbel}$ (<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib13" title="" class="ltx_ref">13</a>, <a href="#bib.bib3" title="" class="ltx_ref">3</a>]</cite>). For $m\geq 1\text{,}$ the general theory (applied via the Bridge Theorem, Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a>) gives $T/E[T]\xrightarrow{d}\operatorname{Exp}(1)\text{.}$ The transition at $m=0\to m\geq 1$ is discontinuous:</p>
</div>
<div id="S6.SS4.p3" class="ltx_para">
<table id="S6.SS4.p3.1" class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr id="S6.SS4.p3.1.1" class="ltx_tr">
<th id="S6.SS4.p3.1.1.1" class="ltx_td ltx_th ltx_th_row ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"></th>
<td id="S6.SS4.p3.1.1.2" class="ltx_td ltx_align_left ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.1.2.1" class="ltx_text ltx_font_bold" style="font-size:90%;">Classical ($m=0$)</span></td>
<td id="S6.SS4.p3.1.1.3" class="ltx_td ltx_align_left ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.1.3.1" class="ltx_text ltx_font_bold" style="font-size:90%;">Reset ($m\geq 1$)</span></td></tr>
<tr id="S6.SS4.p3.1.2" class="ltx_tr">
<th id="S6.SS4.p3.1.2.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.2.1.1" class="ltx_text" style="font-size:90%;">Scale</span></th>
<td id="S6.SS4.p3.1.2.2" class="ltx_td ltx_align_left ltx_border_t" style="padding-top:0.9pt;padding-bottom:0.9pt;">$\Theta(n\log n)$</td>
<td id="S6.SS4.p3.1.2.3" class="ltx_td ltx_align_left ltx_border_t" style="padding-top:0.9pt;padding-bottom:0.9pt;">$\sim n^{m+1}/(m\cdot m!)$</td></tr>
<tr id="S6.SS4.p3.1.3" class="ltx_tr">
<th id="S6.SS4.p3.1.3.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.3.1.1" class="ltx_text" style="font-size:90%;">Fluctuations</span></th>
<td id="S6.SS4.p3.1.3.2" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;">$\Theta(n)\ll E[T]$</td>
<td id="S6.SS4.p3.1.3.3" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;">$\Theta(E[T])$</td></tr>
<tr id="S6.SS4.p3.1.4" class="ltx_tr">
<th id="S6.SS4.p3.1.4.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.4.1.1" class="ltx_text" style="font-size:90%;">Coefficient of variation</span></th>
<td id="S6.SS4.p3.1.4.2" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;">$\to 0$</td>
<td id="S6.SS4.p3.1.4.3" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;">$\to 1$</td></tr>
<tr id="S6.SS4.p3.1.5" class="ltx_tr">
<th id="S6.SS4.p3.1.5.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.5.1.1" class="ltx_text" style="font-size:90%;">Limit law</span></th>
<td id="S6.SS4.p3.1.5.2" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.5.2.1" class="ltx_text" style="font-size:90%;">Gumbel</span></td>
<td id="S6.SS4.p3.1.5.3" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.5.3.1" class="ltx_text" style="font-size:90%;">Exponential</span></td></tr>
<tr id="S6.SS4.p3.1.6" class="ltx_tr">
<th id="S6.SS4.p3.1.6.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.6.1.1" class="ltx_text" style="font-size:90%;">Mechanism</span></th>
<td id="S6.SS4.p3.1.6.2" class="ltx_td ltx_align_left ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.6.2.1" class="ltx_text" style="font-size:90%;">last coupon (extreme value)</span></td>
<td id="S6.SS4.p3.1.6.3" class="ltx_td ltx_align_left ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S6.SS4.p3.1.6.3.1" class="ltx_text" style="font-size:90%;">lucky streak (geometric)</span></td></tr>
</tbody>
</table>
</div>
<div id="S6.SS4.p4" class="ltx_para">
<p id="S6.SS4.p4.1" class="ltx_p">In the classical CCP, the bottleneck is the last missing coupon—an extreme value problem yielding the Gumbel law. A single reset coupon destroys this mechanism: completion now requires a lucky streak (an attempt succeeding without catastrophe), and the number of attempts is geometric. The geometric waiting time’s memorylessness propagates to $T/E[T]\to\operatorname{Exp}(1)\text{,}$ making the completion time fundamentally unpredictable.</p>
</div>
<div id="S6.Thmtheorem3" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmtheorem3.2" class="ltx_text ltx_font_italic">Remark 6.3</span></span><span id="S6.Thmtheorem3.3" class="ltx_text ltx_font_italic"> </span>(CCP convergence via the Bridge Theorem)<span id="S6.Thmtheorem3.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S6.Thmtheorem3.p1" class="ltx_para">
<p id="S6.Thmtheorem3.p1.1" class="ltx_p">The CCP has $q=m/(n+m)\to 0$ as $n\to\infty\text{,}$ so Corollary <a href="#S4.Thmtheorem6" title="Corollary 4.6 (Exponential limit). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.6</span></a> (which assumes fixed $q$) does not apply directly. Instead, CCP convergence follows from the Bridge Theorem (Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a>): the conditions $p\to 0$ and uniform boundedness of moment ratios of $A$ are verified below in the proof of Theorem <a href="#S6.Thmtheorem4" title="Theorem 6.4 (CCP sharp bound). ‣ 6.4 Phase Transition and Sharp Kolmogorov Bound ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.4</span></a>.</p>
</div>
</div>
<div id="S6.Thmtheorem4" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S6.Thmtheorem4.2" class="ltx_text ltx_font_bold">Theorem 6.4</span></span><span id="S6.Thmtheorem4.3" class="ltx_text ltx_font_bold"> </span>(CCP sharp bound)<span id="S6.Thmtheorem4.4" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S6.Thmtheorem4.p1" class="ltx_para">
<p id="S6.Thmtheorem4.p1.1" class="ltx_p"><span id="S6.Thmtheorem4.p1.1.1" class="ltx_text ltx_font_italic">For the coupon collector with $n$ standard and $m\geq 1$ reset coupons, $m$ fixed, $n\to\infty\text{:}$</span></p>
<table id="S6.E52" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{K}}\!\left(\frac{T}{E[T]},\,\operatorname{Exp}(1)\right)\in\bigl[1-o(1),\;2+o(1)\bigr]\cdot|\alpha|.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(52)</span></td></tr></tbody>
</table>
</div>
</div>
<div id="S6.SS4.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of the upper bound.</h6>
<div id="S6.SS4.p5" class="ltx_para">
<p id="S6.SS4.p5.1" class="ltx_p"><span id="S6.SS4.p5.1.1" class="ltx_text">To apply the Bridge Theorem (Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a>), it suffices to show
that the moment ratios
$\rho_{j}:=\frac{E[A^{j}]}{E[A]^{j}},j=2,3\text{,}$ are bounded uniformly in $n$ for each fixed $m\geq 1\text{.}$ We first bound the numerator. By Lemma <a href="#S4.Thmtheorem8" title="Lemma 4.8 (Failed-attempt tail bound). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.8</span></a>,
$P(A\geq t)\leq s^{t-1},t\geq 1\text{.}$
Hence, by the tail-sum formula,</span></p>
<table id="S6.Ex52" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[A^{k}]=\sum_{t\geq 1}\bigl(t^{k}-(t-1)^{k}\bigr)P(A\geq t)\leq k\sum_{t\geq 1}t^{k-1}s^{t-1}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS4.p5.2" class="ltx_p"><span id="S6.SS4.p5.2.1" class="ltx_text">Since $s=1-q\leq e^{-q}\text{,}$</span></p>
<table id="S6.Ex53" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{t\geq 1}t^{k-1}s^{t-1}\leq 2\sum_{t\geq 1}t^{k-1}e^{-qt}\leq C_{k}q^{-k},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS4.p5.3" class="ltx_p"><span id="S6.SS4.p5.3.1" class="ltx_text">for a constant $C_{k}$ depending only on $k\text{.}$ Therefore, $E[A^{k}]\leq C_{k}q^{-k}\text{.}$</span></p>
</div>
<div id="S6.SS4.p6" class="ltx_para">
<p id="S6.SS4.p6.1" class="ltx_p"><span id="S6.SS4.p6.1.1" class="ltx_text">For the lower bound on $E[A]\text{,}$ use the explicit failed-attempt law
$P(A=j)=\frac{q\,s^{j-1}P(T_{0}&gt;j)}{1-p},j\geq 1\text{.}$
In the CCP, $T_{0}\geq n$ almost surely, so $P(T_{0}&gt;j)=1$ for $1\leq j\leq n-1\text{.}$
Hence</span></p>
<table id="S6.Ex54" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E[A]=\frac{1}{1-p}\sum_{j\geq 1}jqs^{j-1}P(T_{0}&gt;j)\geq\sum_{j=1}^{n-1}jqs^{j-1}=\frac{1-ns^{\,n-1}+(n-1)s^{n}}{q}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS4.p6.2" class="ltx_p"><span id="S6.SS4.p6.2.1" class="ltx_text">Since $q=m/(n+m)$ and $s=n/(n+m)\text{,}$ for each fixed $m\geq 1\text{,}$
$1-ns^{\,n-1}+(n-1)s^{n}\to 1-(m+1)e^{-m}&gt;0\text{,}$
so there exists $c_{m}&gt;0$ such that
$E[A]\geq\frac{c_{m}}{q}$ for all sufficiently large $n\text{.}$</span></p>
</div>
<div id="S6.SS4.p7" class="ltx_para">
<p id="S6.SS4.p7.1" class="ltx_p"><span id="S6.SS4.p7.1.1" class="ltx_text">Combining the two estimates gives</span></p>
<table id="S6.Ex55" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{E[A^{k}]}{E[A]^{k}}\leq\frac{C_{k}q^{-k}}{(c_{m}q^{-1})^{k}}=\frac{C_{k}}{c_{m}^{k}}=O_{m}(1).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS4.p7.2" class="ltx_p"><span id="S6.SS4.p7.2.1" class="ltx_text">Hence $\rho_{2},\rho_{3}=O_{m}(1)\text{,}$ and Brown’s constant in
Theorem <a href="#S4.Thmtheorem13" title="Theorem 4.13 (Bridge Theorem). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.13</span></a> satisfies $C_{1}=O_{m}(1)\text{.}$ Thus, from (<a href="#S6.E51" title="In 6.4 Phase Transition and Sharp Kolmogorov Bound ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">51</span></a>) and Proposition <a href="#S4.Thmtheorem2" title="Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a> (<a href="#S4.I2.i2" title="item b ‣ Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">b</span></a>): $b/\mu=\frac{mH}{C-1}=|\alpha|+\frac{s}{C-1}\text{,}$ and $\frac{s}{C-1}=O(p)\text{.}$ Finally, $d_{\mathrm{K}}\leq O_{m}(p)+2|\alpha|+O(p)=(2+o(1))|\alpha|\text{.}$
∎</span></p>
</div>
</div>
<div id="S6.SS4.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of the lower bound.</h6>
<div id="S6.SS4.p8" class="ltx_para">
<p id="S6.SS4.p8.1" class="ltx_p"><span id="S6.SS4.p8.1.1" class="ltx_text">This is the one point where CCP-specific structure goes beyond substitution into general formulas. Choose $\theta=\theta_{n}=(\ln n)^{1/2}$ and set $w=e^{-\theta/\mu}\text{,}$ $u=ws\text{,}$ $\epsilon=\theta/\mu\text{.}$ By (<a href="#S4.E33" title="In Proof of the lower bound. ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">33</span></a>), $d_{\mathrm{K}}\geq|G_{T}(w)-1/(1+\theta)|\text{.}$</span></p>
</div>
<div id="S6.SS4.p9" class="ltx_para">
<p id="S6.SS4.p9.1" class="ltx_p"><em id="S6.SS4.p9.1.1" class="ltx_emph ltx_font_italic">Step 1: PGF reduction.</em><span id="S6.SS4.p9.1.2" class="ltx_text"> 
From (<a href="#S2.E9" title="In Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a>), setting $c=g(u)/p\text{:}$</span></p>
<table id="S6.Ex56" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{T}(w)=\frac{c+O_{m}(\theta p)}{c+\theta+O_{m}(\theta p)}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS4.p9.2" class="ltx_p"><span id="S6.SS4.p9.2.1" class="ltx_text">Hence $G_{T}(w)-1/(1+\theta)=(c-1)\theta/((c+\theta)(1+\theta))+O_{m}(\theta p)\text{.}$</span></p>
</div>
<div id="S6.SS4.p10" class="ltx_para">
<p id="S6.SS4.p10.1" class="ltx_p"><em id="S6.SS4.p10.1.1" class="ltx_emph ltx_font_italic">Step 2: Product-structure evaluation of $\log c\text{.}$</em><span id="S6.SS4.p10.1.2" class="ltx_text"> 
The product structure $g=\prod_{k=1}^{n}G_{X_{k}}$ gives</span></p>
<table id="S6.Ex57" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log c=\sum_{k=1}^{n}\log(G_{X_{k}}(u)/G_{X_{k}}(s)).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS4.p10.2" class="ltx_p"><span id="S6.SS4.p10.2.1" class="ltx_text">Each ratio $G_{X_{k}}(u)/G_{X_{k}}(s)$ expands as</span></p>
<table id="S6.Ex58" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\frac{G_{X_{k}}(u)}{G_{X_{k}}(s)}=\frac{w(1-a_{k})}{1-a_{k}w}=\frac{1-\delta}{1+x_{k}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS4.p10.3" class="ltx_p"><span id="S6.SS4.p10.3.1" class="ltx_text">where $x_{k}=a_{k}\delta/(1-a_{k})$ with $a_{k}=(k{-}1)/(n{+}m)$ and $\delta=1-w\text{.}$ Since $\sup_{k}x_{k}=O_{m}(\sqrt{\ln n}/n^{m})\to 0\text{,}$ the expansion $\log(1+x_{k})=x_{k}+O(x_{k}^{2})$ is uniformly valid. Summing and using the identity $\sum_{k=1}^{n}a_{k}/(1-a_{k})=(n+m)H-n\text{:}$</span></p>
<table id="S6.Ex59" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log c=-\delta(n+m)H+O(\delta^{2}S_{2}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS4.p10.4" class="ltx_p"><span id="S6.SS4.p10.4.1" class="ltx_text">where $S_{2}=\sum_{k=2}^{n}a_{k}^{2}/(1-a_{k})^{2}=O_{m}(n^{2})\text{.}$ Converting $\delta(n+m)H$ to $\theta|\alpha|(1+o(1))$ and verifying $\delta^{2}S_{2}=o(\theta|\alpha|)\text{:}$</span></p>
<table id="S6.Ex60" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log c=-\theta|\alpha|(1+o(1)).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S6.SS4.p10.5" class="ltx_p"><span id="S6.SS4.p10.5.1" class="ltx_text">Since $\theta|\alpha|\to 0\text{,}$ this gives $c=1-\theta|\alpha|(1+o(1))\text{.}$</span></p>
</div>
<div id="S6.SS4.p11" class="ltx_para">
<p id="S6.SS4.p11.1" class="ltx_p"><em id="S6.SS4.p11.1.1" class="ltx_emph ltx_font_italic">Step 3: Assembly.</em><span id="S6.SS4.p11.1.2" class="ltx_text"> 
$(c-1)\theta/((c+\theta)(1+\theta))=-(1+o(1))\theta^{2}|\alpha|/(1+\theta)^{2}\text{,}$ and the correction $O_{m}(\theta p)=o(|\alpha|)\text{.}$ Hence $d_{\mathrm{K}}\geq(1+o(1))\theta^{2}|\alpha|/(1+\theta)^{2}=(1-o(1))|\alpha|\text{,}$ using $\theta^{2}/(1+\theta)^{2}=1-O(1/\sqrt{\ln n})\text{.}$
∎</span></p>
</div>
</div>
</section>
</section>
<section id="S7" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="application-multi-phase-task-with-catastrophe"><span class="ltx_tag ltx_tag_section">7 </span>Application: Multi-Phase Task with Catastrophe</h2>

<div id="S7.p1" class="ltx_para">
<p id="S7.p1.1" class="ltx_p">The CCP of §<a href="#S6" title="6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a> features a base PGF that is a product of $n$ distinct Möbius factors, producing a <em id="S7.p1.1.1" class="ltx_emph ltx_font_italic">harmonic complexity staircase</em> whose successive levels introduce new finite harmonic sums $H^{(r)}\text{.}$ We now present a structurally contrasting application: a base process whose PGF is a <em id="S7.p1.1.2" class="ltx_emph ltx_font_italic">power</em> of a single Möbius factor, yielding a purely <em id="S7.p1.1.3" class="ltx_emph ltx_font_italic">algebraic</em> staircase. The DRP applies identically in both cases; the difference lies entirely in what it saves.</p>
</div>
<section id="S7.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="model-and-the-algebraic-staircase"><span class="ltx_tag ltx_tag_subsection">7.1 </span>Model and the Algebraic Staircase</h3>

<div id="S7.SS1.p1" class="ltx_para">
<p id="S7.SS1.p1.1" class="ltx_p">A task consists of $r\geq 2$ sequential phases, each requiring $\operatorname{Geom}_{1}(\pi)$ steps independently. The base completion time is $T_{0}=X_{1}+\cdots+X_{r}\text{,}$ $X_{i}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\operatorname{Geom}_{1}(\pi)\text{,}$ with PGF</p>
<table id="S7.E53" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$g(z)=\left[\frac{\pi z}{1-(1-\pi)z}\right]^{\!r}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(53)</span></td></tr></tbody>
</table>
<p id="S7.SS1.p1.2" class="ltx_p">Catastrophe at each step (probability $q\text{,}$ independent) destroys all accumulated progress, resetting the phase counter to zero. Define $\sigma=1-(1-\pi)s=\pi+q(1-\pi)$ and $\rho=\pi s/\sigma\text{.}$ Then</p>
<table id="S7.E54" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$p=g(s)=\rho^{r},\qquad E[T]=\frac{1-\rho^{r}}{q\rho^{r}},\qquad D_{1}=g^{\prime}(s)=\frac{r\rho^{r}}{s\sigma},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(54)</span></td></tr></tbody>
</table>
<p id="S7.SS1.p1.3" class="ltx_p">and the variance, obtained from (<a href="#S2.E17" title="In Example 2.9 (First two moments). ‣ 2.3 Moment Recursion and the Complexity Staircase ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">17</span></a>), depends on $p$ and $D_{1}$ but not on $D_{2}$—exactly as the DRP guarantees.</p>
</div>
<div id="S7.SS1.p2" class="ltx_para">
<p id="S7.SS1.p2.1" class="ltx_p">The key structural feature is that $\log g=r\log f$ with $f(z)=\pi z/(1-(1-\pi)z)\text{,}$ so every logarithmic derivative</p>
<table id="S7.E55" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(\log g)^{(k)}(s)=r(k-1)!\left[\frac{(-1)^{k-1}}{s^{k}}+\frac{(1-\pi)^{k}}{\sigma^{k}}\right]$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(55)</span></td></tr></tbody>
</table>
<p id="S7.SS1.p2.2" class="ltx_p">is a <em id="S7.SS1.p2.2.1" class="ltx_emph ltx_font_italic">rational function</em> of $(s,\pi,r)$—no new generalized harmonic statistic appears at any level. Displayed alongside the CCP realization:</p>
</div>
<div id="S7.SS1.p3" class="ltx_para">
<table id="S7.SS1.p3.1" class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr id="S7.SS1.p3.1.1" class="ltx_tr">
<th id="S7.SS1.p3.1.1.1" class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_th_row ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS1.p3.1.1.1.1" class="ltx_text ltx_font_bold" style="font-size:90%;">Moment of $T$</span></th>
<th id="S7.SS1.p3.1.1.2" class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS1.p3.1.1.2.1" class="ltx_text ltx_font_bold" style="font-size:90%;">New input (DRP)</span></th>
<th id="S7.SS1.p3.1.1.3" class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS1.p3.1.1.3.1" class="ltx_text ltx_font_bold" style="font-size:90%;">CCP realization</span></th>
<th id="S7.SS1.p3.1.1.4" class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS1.p3.1.1.4.1" class="ltx_text ltx_font_bold" style="font-size:90%;">Multi-phase realization</span></th></tr>
</thead>
<tbody class="ltx_tbody">
<tr id="S7.SS1.p3.1.2" class="ltx_tr">
<th id="S7.SS1.p3.1.2.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$E[T]$</th>
<td id="S7.SS1.p3.1.2.2" class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$g(s)$</td>
<td id="S7.SS1.p3.1.2.3" class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$C=\binom{n+m}{n}$</td>
<td id="S7.SS1.p3.1.2.4" class="ltx_td ltx_align_center ltx_border_t" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$\rho^{r}$</td></tr>
<tr id="S7.SS1.p3.1.3" class="ltx_tr">
<th id="S7.SS1.p3.1.3.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$\operatorname{Var}(T)$</th>
<td id="S7.SS1.p3.1.3.2" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$+g^{\prime}(s)$</td>
<td id="S7.SS1.p3.1.3.3" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$+H=\sum 1/j$</td>
<td id="S7.SS1.p3.1.3.4" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$+r/(s\sigma)$</td></tr>
<tr id="S7.SS1.p3.1.4" class="ltx_tr">
<th id="S7.SS1.p3.1.4.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$\mu_{3}(T)$</th>
<td id="S7.SS1.p3.1.4.2" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$+g^{\prime\prime}(s)$</td>
<td id="S7.SS1.p3.1.4.3" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$+H^{(2)}=\sum 1/j^{2}$</td>
<td id="S7.SS1.p3.1.4.4" class="ltx_td ltx_align_center" style="padding-bottom: 2.0pt;padding-top:0.9pt;padding-bottom:0.9pt;">$+\,r\cdot[\text{rational in }s,\sigma,\pi]$</td></tr>
<tr id="S7.SS1.p3.1.5" class="ltx_tr">
<th id="S7.SS1.p3.1.5.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;">$\mu_{k}(T)$</th>
<td id="S7.SS1.p3.1.5.2" class="ltx_td ltx_align_center ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;">$+g^{(k-1)}(s)$</td>
<td id="S7.SS1.p3.1.5.3" class="ltx_td ltx_align_center ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;">$+H^{(k-1)}$</td>
<td id="S7.SS1.p3.1.5.4" class="ltx_td ltx_align_center ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;">$+r\cdot[\text{rational}]$</td></tr>
</tbody>
</table>
</div>
<div id="S7.SS1.p4" class="ltx_para">
<p id="S7.SS1.p4.1" class="ltx_p">The contrast traces to the PGF’s analytic structure: the CCP’s $n$ distinct poles produce new power sums $\sum j^{-k}$ at each level, while the multi-phase model’s single pole with multiplicity $r$ cycles through powers of the same two quantities $1/s$ and $(1-\pi)/\sigma\text{.}$</p>
</div>
<div id="S7.Thmtheorem1" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S7.Thmtheorem1.2" class="ltx_text ltx_font_italic">Remark 7.1</span></span><span id="S7.Thmtheorem1.3" class="ltx_text ltx_font_italic"> </span>(What the DRP saves)<span id="S7.Thmtheorem1.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S7.Thmtheorem1.p1" class="ltx_para">
<p id="S7.Thmtheorem1.p1.1" class="ltx_p">In the CCP, the DRP eliminates one new harmonic statistic at each level; here, it eliminates a routine rational computation. The mechanism—$\alpha_{N}(1)=\alpha_{D}(1)$ forcing cancellation of $g^{(k)}$ in $\Delta_{k}$—is identical. The DRP is a property of the catastrophe mechanism, not of the base process.</p>
</div>
</div>
</section>
<section id="S7.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="phase-transition-and-convergence-rate"><span class="ltx_tag ltx_tag_subsection">7.2 </span>Phase Transition and Convergence Rate</h3>

<div id="S7.SS2.p1" class="ltx_para">
<p id="S7.SS2.p1.1" class="ltx_p">Specializing Definition <a href="#S4.Thmtheorem1" title="Definition 4.1 (Perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.1</span></a>:</p>
<table id="S7.E56" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\alpha=\frac{\rho^{r}(s\sigma-qr)}{\sigma(1-\rho^{r})},\qquad|\alpha|\sim\frac{qr}{\sigma}\,\rho^{r},\quad p=\rho^{r}\qquad(r\to\infty).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(56)</span></td></tr></tbody>
</table>
<p id="S7.SS2.p1.2" class="ltx_p">Since $q$ is fixed, Corollary <a href="#S4.Thmtheorem6" title="Corollary 4.6 (Exponential limit). ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.6</span></a> applies directly: $T/E[T]\xrightarrow{d}\operatorname{Exp}(1)$ as $r\to\infty\text{.}$ Without catastrophe, $T_{0}\sim\mathrm{NegBin}(r,\pi)$ satisfies a CLT: $(T_{0}-r/\pi)/\sqrt{r(1-\pi)/\pi^{2}}\xrightarrow{d}N(0,1)\text{.}$ A single catastrophe mechanism thus induces a <span id="S7.SS2.p1.2.1" class="ltx_text ltx_font_bold">Gaussian-to-exponential phase transition</span>—distinct from the CCP’s Gumbel-to-Exponential transition, but driven by the same algebraic cause: the coefficient equality $\alpha_{N}(1)=\alpha_{D}(1)$ forces the $\theta^{1}$-coefficient in the Laplace expansion to vanish exactly (Proposition <a href="#S4.Thmtheorem2" title="Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a> (<a href="#S4.I2.i1" title="item a ‣ Proposition 4.2 (Properties of the perturbation parameters). ‣ 4.1 The Perturbation Parameter ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">a</span></a>)).</p>
</div>
<div id="S7.SS2.p2" class="ltx_para">
<p id="S7.SS2.p2.1" class="ltx_p">The sharp two-sided bound (Theorem <a href="#S4.Thmtheorem15" title="Theorem 4.15 (Two-sided bound). ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.15</span></a>) gives $d_{\mathrm{K}}(T/E[T],\,\operatorname{Exp}(1))\asymp p+|\alpha|\asymp r\rho^{r}$ as $r\to\infty\text{:}$ convergence is <em id="S7.SS2.p2.1.1" class="ltx_emph ltx_font_italic">exponentially fast</em> in $r$ with a linear prefactor, contrasting with the CCP’s polynomial rate $\Theta(m!\,m\ln n/n^{m})\text{.}$</p>
</div>
<div id="S7.SS2.p3" class="ltx_para">
<table id="S7.SS2.p3.1" class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr id="S7.SS2.p3.1.1" class="ltx_tr">
<th id="S7.SS2.p3.1.1.1" class="ltx_td ltx_th ltx_th_row ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"></th>
<td id="S7.SS2.p3.1.1.2" class="ltx_td ltx_align_left ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.1.2.1" class="ltx_text ltx_font_bold" style="font-size:90%;">CCP ($n\to\infty\text{,}$ $m$ fixed)</span></td>
<td id="S7.SS2.p3.1.1.3" class="ltx_td ltx_align_left ltx_border_tt" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.1.3.1" class="ltx_text ltx_font_bold" style="font-size:90%;">Multi-phase ($r\to\infty\text{,}$ $\pi,q$ fixed)</span></td></tr>
<tr id="S7.SS2.p3.1.2" class="ltx_tr">
<th id="S7.SS2.p3.1.2.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.2.1.1" class="ltx_text" style="font-size:90%;">Without catastrophe</span></th>
<td id="S7.SS2.p3.1.2.2" class="ltx_td ltx_align_left ltx_border_t" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.2.2.1" class="ltx_text" style="font-size:90%;">Gumbel</span></td>
<td id="S7.SS2.p3.1.2.3" class="ltx_td ltx_align_left ltx_border_t" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.2.3.1" class="ltx_text" style="font-size:90%;">Gaussian</span></td></tr>
<tr id="S7.SS2.p3.1.3" class="ltx_tr">
<th id="S7.SS2.p3.1.3.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.3.1.1" class="ltx_text" style="font-size:90%;">With catastrophe</span></th>
<td id="S7.SS2.p3.1.3.2" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.3.2.1" class="ltx_text" style="font-size:90%;">Exponential</span></td>
<td id="S7.SS2.p3.1.3.3" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.3.3.1" class="ltx_text" style="font-size:90%;">Exponential</span></td></tr>
<tr id="S7.SS2.p3.1.4" class="ltx_tr">
<th id="S7.SS2.p3.1.4.1" class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.4.1.1" class="ltx_text" style="font-size:90%;">Rate template</span></th>
<td id="S7.SS2.p3.1.4.2" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;">$p+|\alpha|\asymp m!\,m\ln n/n^{m}$</td>
<td id="S7.SS2.p3.1.4.3" class="ltx_td ltx_align_left" style="padding-top:0.9pt;padding-bottom:0.9pt;">$p+|\alpha|\asymp r\rho^{r}$</td></tr>
<tr id="S7.SS2.p3.1.5" class="ltx_tr">
<th id="S7.SS2.p3.1.5.1" class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.5.1.1" class="ltx_text" style="font-size:90%;">Rate type</span></th>
<td id="S7.SS2.p3.1.5.2" class="ltx_td ltx_align_left ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.5.2.1" class="ltx_text" style="font-size:90%;">polynomial in $n$</span></td>
<td id="S7.SS2.p3.1.5.3" class="ltx_td ltx_align_left ltx_border_bb" style="padding-top:0.9pt;padding-bottom:0.9pt;"><span id="S7.SS2.p3.1.5.3.1" class="ltx_text" style="font-size:90%;">exponential in $r$</span></td></tr>
</tbody>
</table>
</div>
<div id="S7.Thmtheorem2" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S7.Thmtheorem2.2" class="ltx_text ltx_font_italic">Remark 7.2</span></span><span id="S7.Thmtheorem2.3" class="ltx_text ltx_font_italic"> </span>(CV criterion and forced catastrophe)<span id="S7.Thmtheorem2.4" class="ltx_text ltx_font_italic">.</span></h6>
<div id="S7.Thmtheorem2.p1" class="ltx_para">
<p id="S7.Thmtheorem2.p1.1" class="ltx_p">The coefficient of variation of $T_{0}\sim\mathrm{NegBin}(r,\pi)$ satisfies $\operatorname{CV}^{2}=(1-\pi)/r&lt;1$ for $r\geq 2\text{.}$ By the Pal–Reuveni criterion (<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib37" title="" class="ltx_ref">37</a>]</cite>), adding voluntary restart to this base process is always detrimental. The present application demonstrates that the DRP framework remains fully operative—and produces non-trivial distributional information—even when catastrophe is imposed against the process’s interest. The algebraic structure does not consult the CV criterion.</p>
</div>
</div>
</section>
</section>
<section id="S8" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="related-work"><span class="ltx_tag ltx_tag_section">8 </span>Related Work</h2>

<section id="S8.SS0.SSS0.Px1" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="stochastic-resetting-and-the-pgf-formula">Stochastic Resetting and the PGF Formula.</h4>

<div id="S8.SS0.SSS0.Px1.p1" class="ltx_para">
<p id="S8.SS0.SSS0.Px1.p1.1" class="ltx_p">The renewal framework for stochastic resetting—developed in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib15" title="" class="ltx_ref">16</a>, <a href="#bib.bib37" title="" class="ltx_ref">37</a>, <a href="#bib.bib33" title="" class="ltx_ref">33</a>, <a href="#bib.bib8" title="" class="ltx_ref">8</a>]</cite> and surveyed in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib16" title="" class="ltx_ref">15</a>]</cite>—provides the attempt decomposition underlying Theorem <a href="#S2.Thmtheorem2" title="Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a>. The PGF formula was derived independently by <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib19" title="" class="ltx_ref">19</a>]</cite> and <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib4" title="" class="ltx_ref">4</a>]</cite>. These works primarily use the resulting transform for computation or restart optimization, without identifying the affine structure or establishing convergence rates. Our framework places the CV-unity criterion of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib37" title="" class="ltx_ref">37</a>]</cite>
in a broader structural context: the dependence on first and second moments appears as the $k=2$ shadow of the derivative reduction principle. Non-memoryless protocols <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib14" title="" class="ltx_ref">14</a>, <a href="#bib.bib9" title="" class="ltx_ref">9</a>, <a href="#bib.bib26" title="" class="ltx_ref">26</a>]</cite> fall outside this affine transform class; our characterization theorems (Theorems <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Characterization). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a>, <a href="#S5.Thmtheorem7" title="Theorem 5.7 (Continuous-time characterization). ‣ 5.4 Characterization: Affine Laplace Structure Is Poisson ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.7</span></a>) identify the precise algebraic boundary.</p>
</div>
</section>
<section id="S8.SS0.SSS0.Px2" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="linear-fractional-structure-across-domains">Linear-Fractional Structure across Domains.</h4>

<div id="S8.SS0.SSS0.Px2.p1" class="ltx_para">
<p id="S8.SS0.SSS0.Px2.p1.1" class="ltx_p">Geometric compounding inherently produces linear-fractional PGFs, exploited in branching process theory by <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib1" title="" class="ltx_ref">1</a>, <a href="#bib.bib38" title="" class="ltx_ref">38</a>]</cite> (see also <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib23" title="" class="ltx_ref">23</a>, <a href="#bib.bib28" title="" class="ltx_ref">28</a>]</cite>), in catastrophe queueing by <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib5" title="" class="ltx_ref">5</a>, <a href="#bib.bib20" title="" class="ltx_ref">20</a>]</cite> (see <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib27" title="" class="ltx_ref">27</a>, <a href="#bib.bib12" title="" class="ltx_ref">12</a>, <a href="#bib.bib2" title="" class="ltx_ref">2</a>]</cite> for extensions), and observed empirically in algorithmic restart, where <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib22" title="" class="ltx_ref">22</a>]</cite> noted that restart converts heavy-tailed SAT runtimes into geometric-like distributions (see <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib29" title="" class="ltx_ref">29</a>, <a href="#bib.bib39" title="" class="ltx_ref">39</a>, <a href="#bib.bib40" title="" class="ltx_ref">40</a>]</cite>). All these works treat linear-fractional structure as a convenient tractable family or an empirical regularity. Our characterization theorem reveals the complementary perspective: this structure is <em id="S8.SS0.SSS0.Px2.p1.1.1" class="ltx_emph ltx_font_italic">diagnostic</em>—it identifies the geometric-tail class among all age-based catastrophe mechanisms—and the Möbius-rigidity argument applies it as a characterization tool rather than a model assumption.</p>
</div>
</section>
<section id="S8.SS0.SSS0.Px3" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="exponential-approximation-of-geometric-sums">Exponential Approximation of Geometric Sums.</h4>

<div id="S8.SS0.SSS0.Px3.p1" class="ltx_para">
<p id="S8.SS0.SSS0.Px3.p1.1" class="ltx_p"><cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib36" title="" class="ltx_ref">36</a>]</cite> proved that normalized geometric sums converge to $\operatorname{Exp}(1)\text{.}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib6" title="" class="ltx_ref">6</a>]</cite> obtained optimal-order Kolmogorov bounds $d_{K}\leq C_{1}p\text{;}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib34" title="" class="ltx_ref">35</a>]</cite> introduced Stein’s method for this setting, achieving $O(p)$ Wasserstein and $O(\sqrt{p})$ Kolmogorov bounds (see <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib7" title="" class="ltx_ref">7</a>, <a href="#bib.bib35" title="" class="ltx_ref">34</a>]</cite> for refinements, and <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib21" title="" class="ltx_ref">21</a>, <a href="#bib.bib25" title="" class="ltx_ref">25</a>]</cite> for comprehensive treatments). Our Bridge Theorem matches Brown’s $O(p)$ rate for the geometric-sum component; the sharp two-sided bound $d_{\mathrm{K}}\asymp p+|\alpha|$ (Theorem <a href="#S4.Thmtheorem15" title="Theorem 4.15 (Two-sided bound). ‣ 4.4 The Sharp Two-Sided Bound ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.15</span></a>) closes a logarithmic gap from the smoothing inequality by exploiting the specific two-parameter structure produced by the affine PGF analysis. Stein’s method does not directly yield this two-parameter template: existing Stein bounds apply to the pure geometric sum $U$ (achieving $O(\sqrt{p})$ in Kolmogorov distance <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib34" title="" class="ltx_ref">35</a>]</cite>, weaker than Brown’s $O(p)$), while the $|\alpha|$-term arises from the successful-attempt perturbation $B$—an additive component outside the geometric-sum framework that the Bridge Theorem handles via direct probabilistic arguments (Lemmas <a href="#S4.Thmtheorem10" title="Lemma 4.10 (Scaling perturbation). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.10</span></a>–<a href="#S4.Thmtheorem11" title="Lemma 4.11 (Additive perturbation). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.11</span></a>). The matching lower bound, obtained by evaluating the Laplace expansion at a fixed $\theta\text{,}$ is likewise orthogonal to the Stein approach.</p>
</div>
<div id="S8.SS0.SSS0.Px3.p2" class="ltx_para">
<p id="S8.SS0.SSS0.Px3.p2.1" class="ltx_p"><cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib10" title="" class="ltx_ref">10</a>]</cite> develop Stein’s method for the Gumbel approximation and obtain a $(\log n/n)$ rate for the classical coupon collector in a smooth Wasserstein-$1$ metric.</p>
</div>
</section>
<section id="S8.SS0.SSS0.Px4" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="coupon-collector-variants-and-phase-transitions">Coupon Collector Variants and Phase Transitions.</h4>

<div id="S8.SS0.SSS0.Px4.p1" class="ltx_para">
<p id="S8.SS0.SSS0.Px4.p1.1" class="ltx_p">The classical Gumbel limit was established by <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib13" title="" class="ltx_ref">13</a>]</cite> (see <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib3" title="" class="ltx_ref">3</a>, <a href="#bib.bib18" title="" class="ltx_ref">17</a>, <a href="#bib.bib17" title="" class="ltx_ref">18</a>, <a href="#bib.bib11" title="" class="ltx_ref">11</a>, <a href="#bib.bib31" title="" class="ltx_ref">31</a>]</cite> for refinements and extensions). The closest prior phase-transition result is <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib30" title="" class="ltx_ref">30</a>]</cite>, who identified a Gumbel-to-Gaussian transition in the CCP with bonuses. <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib24" title="" class="ltx_ref">24</a>]</cite> study a closely related reset-button CCP, deriving the waiting-time distribution in the unequal-probability setting and expected-value formulas with asymptotics in the equal-probability case. Our contribution is the structural theory (affine PGF framework, DRP, sharp exponential approximation), and the identification of the Gumbel-to-Exponential phase transition—which is qualitatively different from the Gumbel-to-Gaussian transition of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib30" title="" class="ltx_ref">30</a>]</cite> (it reflects memoryless catastrophe, not a CLT effect).</p>
</div>
<div id="S8.SS0.SSS0.Px4.p2" class="ltx_para">
<p id="S8.SS0.SSS0.Px4.p2.1" class="ltx_p">Our phase transitions differ from those of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib32" title="" class="ltx_ref">32</a>]</cite>, who study transitions in the <em id="S8.SS0.SSS0.Px4.p2.1.1" class="ltx_emph ltx_font_italic">optimal restart rate</em>. Ours are in the <em id="S8.SS0.SSS0.Px4.p2.1.2" class="ltx_emph ltx_font_italic">universality class</em> of the limit distribution—Gumbel $\to$ Exponential, Gaussian $\to$ Exponential—driven by the coefficient equality $\alpha_{N}(1)=\alpha_{D}(1)$ killing the first-order Laplace error.</p>
</div>
</section>
</section>
<section id="S9" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="further-directions"><span class="ltx_tag ltx_tag_section">9 </span>Further Directions</h2>

<section id="S9.SS0.SSS0.Px1" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="stability-and-refinement-of-affine-structure">Stability and Refinement of Affine Structure.</h4>

<div id="S9.SS0.SSS0.Px1.p1" class="ltx_para">
<p id="S9.SS0.SSS0.Px1.p1.1" class="ltx_p">Theorem <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Characterization). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a> characterizes affine PGF structure as equivalent to geometric-tail catastrophe, with full memorylessness singled out by $\lambda=1$ (Corollary <a href="#S3.Thmtheorem8" title="Corollary 3.8 (Full memorylessness). ‣ 3.4 From Geometric Tail to Full Memorylessness ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.8</span></a>). The gap—exactly one degree of freedom, the first-step hazard $h_{1}$—closes in continuous time (Theorem <a href="#S5.Thmtheorem7" title="Theorem 5.7 (Continuous-time characterization). ‣ 5.4 Characterization: Affine Laplace Structure Is Poisson ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5.7</span></a>). In the discrete setting, supplementary algebraic conditions (e.g., requiring the successful-attempt PGF $G_{B}$ to also depend on $g$ at a single shifted point) may close this gap; formalizing this would strengthen the characterization.</p>
</div>
<div id="S9.SS0.SSS0.Px1.p2" class="ltx_para">
<p id="S9.SS0.SSS0.Px1.p2.1" class="ltx_p">A related stability question: for near-memoryless mechanisms with $|h_{t}-q|\leq\varepsilon$ for $t\geq 2\text{,}$ does the DRP cancellation error $|\Delta_{k}-(-ks^{k-1}D_{k-1})|$ admit an $O(\varepsilon)$ bound? More broadly, quantifying DRP degradation under Gamma-distributed inter-reset times (shape parameter near $1$) would connect the algebraic theory to the restart optimization literature. At the application level, the CCP sharp bound (Theorem <a href="#S6.Thmtheorem4" title="Theorem 6.4 (CCP sharp bound). ‣ 6.4 Phase Transition and Sharp Kolmogorov Bound ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.4</span></a>) gives leading constants in $[1,2]\text{;}$ numerical evidence suggests the exact constant is closer to $1\text{,}$ likely requiring a finer analysis of the additive perturbation step.</p>
</div>
</section>
<section id="S9.SS0.SSS0.Px2" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="partial-reset">Partial Reset.</h4>

<div id="S9.SS0.SSS0.Px2.p1" class="ltx_para">
<p id="S9.SS0.SSS0.Px2.p1.1" class="ltx_p">When catastrophe clears each coupon independently with probability $r\in(0,1)\text{,}$ the i.i.d. attempt structure of (<a href="#S2.E6" title="In 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>) breaks down: partial reset creates state-dependent catastrophe that cannot be described by a hazard sequence $(h_{t})_{t\geq 1}\text{.}$ Theorem <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Characterization). ‣ 3.3 The Characterization Theorem ‣ 3 Characterization of Geometric-Tail Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a> predicts that affine PGF structure is lost, but a quantitative understanding—what replaces the DRP, what the correct rate template is—remains open. Partial reset interpolates between the memoryless regime ($r=1\text{,}$ exponential limit) and the classical CCP ($r=0\text{,}$ Gumbel limit); understanding this interpolation would reveal whether the Gumbel-to-Exponential phase transition is sharp or admits a crossover regime. A probabilistic proof of the DRP—perhaps via coupling—might extend to this setting where the PGF algebra breaks down.</p>
</div>
</section>
<section id="S9.SS0.SSS0.Px3" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="non-uniform-coupon-probabilities">Non-Uniform Coupon Probabilities.</h4>

<div id="S9.SS0.SSS0.Px3.p1" class="ltx_para">
<p id="S9.SS0.SSS0.Px3.p1.1" class="ltx_p">For non-uniform CCP with probabilities $p_{1},\ldots,p_{n}\text{,}$ the PGF no longer telescopes, but the general theory (Theorem <a href="#S2.Thmtheorem2" title="Theorem 2.2 (PGF formula). ‣ 2.1 Model and PGF Formula ‣ 2 Completion Time under Memoryless Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.2</span></a>, DRP, exponential approximation) applies unchanged to the non-uniform base process. The challenge is evaluating the CCP-specific quantities ($D_{1}\text{,}$ $\alpha$) in terms of the non-uniform parameters and understanding how the phase transition depends on the coupon probability vector.</p>
</div>
</section>
<section id="S9.SS0.SSS0.Px4" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="universality-classes-of-completion-time-limits">Universality Classes of Completion-Time Limits.</h4>

<div id="S9.SS0.SSS0.Px4.p1" class="ltx_para">
<p id="S9.SS0.SSS0.Px4.p1.1" class="ltx_p">The present paper establishes that memoryless catastrophe (i.i.d. attempts, affine PGF structure) produces exponential limits. A structurally contrasting regime may arise in non-renewal recycling mechanisms with weakly dependent increments, where CLT-type arguments yield log-normal completion-time limits instead. This contrast raises a natural question: <em id="S9.SS0.SSS0.Px4.p1.1.1" class="ltx_emph ltx_font_italic">what properties of the catastrophe or recycling mechanism determine the universality class of the completion-time limit law?</em></p>
</div>
<div class="ltx_pagination ltx_role_newpage"></div>
</section>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography" id="references">References</h2>

<ul id="bib.L1" class="ltx_biblist">
<li id="bib.bib1" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[1]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Agresti</span><span class="ltx_text ltx_bib_year"> (1974)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Bounds on the extinction time distribution of a branching process</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Adv. in Appl. Probab.</span> <span class="ltx_text ltx_bib_volume">6</span>, <span class="ltx_text ltx_bib_pages">pp. 322–335</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p4.1" title="1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib2" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[2]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">C. Banderier and M. Wallner</span><span class="ltx_text ltx_bib_year"> (2017)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Lattice paths with catastrophes</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Discrete Math. Theor. Comput. Sci.</span> <span class="ltx_text ltx_bib_volume">19</span> (<span class="ltx_text ltx_bib_number">1</span>).
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib3" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[3]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">L. E. Baum and P. Billingsley</span><span class="ltx_text ltx_bib_year"> (1965)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Asymptotic distributions for the coupon collector’s problem</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Math. Statist.</span> <span class="ltx_text ltx_bib_volume">36</span>, <span class="ltx_text ltx_bib_pages">pp. 1835–1839</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S6.SS4.p2.1" title="6.4 Phase Transition and Sharp Kolmogorov Bound ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§6.4</span></a>,
<a href="#S8.SS0.SSS0.Px4.p1.1" title="Coupon Collector Variants and Phase Transitions. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib4" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[4]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">O. L. Bonomo and A. Pal</span><span class="ltx_text ltx_bib_year"> (2021)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">First passage under restart for discrete space and time: Application to one-dimensional confined lattice random walks</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Phys. Rev. E</span> <span class="ltx_text ltx_bib_volume">103</span>, <span class="ltx_text ltx_bib_pages">pp. 052129</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p4.1" title="1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS2.p2.2" title="1.2 Setup and the PGF Formula ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.2</span></a>,
<a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib5" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[5]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. J. Brockwell, J. Gani, and S. I. Resnick</span><span class="ltx_text ltx_bib_year"> (1982)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Birth, immigration and catastrophe processes</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Adv. in Appl. Probab.</span> <span class="ltx_text ltx_bib_volume">14</span>, <span class="ltx_text ltx_bib_pages">pp. 709–731</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.I1.i2.p1.1" title="In 1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2nd item</span></a>,
<a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib6" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[6]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Brown</span><span class="ltx_text ltx_bib_year"> (1990)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Error bounds for exponential approximations of geometric convolutions</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Probab.</span> <span class="ltx_text ltx_bib_volume">18</span> (<span class="ltx_text ltx_bib_number">3</span>), <span class="ltx_text ltx_bib_pages">pp. 1388–1402</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p10.1" title="1.3 Main Results ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S4.SS3.p9.1" title="4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4.3</span></a>,
<a href="#S4.Thmtheorem12" title="Theorem 4.12 (Theorem 2.1 (ii), []). ‣ 4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem 4.12</span></a>,
<a href="#S8.SS0.SSS0.Px3.p1.1" title="Exponential Approximation of Geometric Sums. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib7" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[7]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Brown</span><span class="ltx_text ltx_bib_year"> (2015)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Sharp bounds for exponential approximations under a hazard rate upper bound</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">J. Appl. Probab.</span> <span class="ltx_text ltx_bib_volume">52</span>, <span class="ltx_text ltx_bib_pages">pp. 841–850</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px3.p1.1" title="Exponential Approximation of Geometric Sums. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib8" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[8]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Chechkin and I. M. Sokolov</span><span class="ltx_text ltx_bib_year"> (2018)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Random search with resetting: A unified renewal approach</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Phys. Rev. Lett.</span> <span class="ltx_text ltx_bib_volume">121</span>, <span class="ltx_text ltx_bib_pages">pp. 050601</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p2.1" title="1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S5.SS2.p1.1" title="5.2 The Laplace Transform Formula and Affine Structure ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§5.2</span></a>,
<a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib9" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[9]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">H. Chen and Y. Ye</span><span class="ltx_text ltx_bib_year"> (2022)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Random walks on complex networks under time-dependent stochastic resetting</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Phys. Rev. E</span> <span class="ltx_text ltx_bib_volume">106</span>, <span class="ltx_text ltx_bib_pages">pp. 044139</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib10" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[10]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">B. Costacèque and L. Decreusefond</span><span class="ltx_text ltx_bib_year"> (2026)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Convergence rate for the coupon collector’s problem with Stein’s method</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Stochastic Process. Appl.</span> <span class="ltx_text ltx_bib_volume">193</span>, <span class="ltx_text ltx_bib_pages">pp. 104835</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px3.p2.1" title="Exponential Approximation of Geometric Sums. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib11" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[11]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. V. Doumas and V. G. Papanicolaou</span><span class="ltx_text ltx_bib_year"> (2012)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The coupon collector’s problem revisited: Asymptotics of the variance</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Adv. in Appl. Probab.</span> <span class="ltx_text ltx_bib_volume">44</span>, <span class="ltx_text ltx_bib_pages">pp. 166–195</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px4.p1.1" title="Coupon Collector Variants and Phase Transitions. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib12" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[12]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Economou and D. Fakinos</span><span class="ltx_text ltx_bib_year"> (2003)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">A continuous-time Markov chain under the influence of a regulating point process and applications in stochastic models with catastrophes</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">European J. Oper. Res.</span> <span class="ltx_text ltx_bib_volume">149</span>, <span class="ltx_text ltx_bib_pages">pp. 625–640</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib13" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[13]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. Erdős and A. Rényi</span><span class="ltx_text ltx_bib_year"> (1961)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">On a classical problem of probability theory</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Magyar Tud. Akad. Mat. Kutató Int. Közl.</span> <span class="ltx_text ltx_bib_volume">6</span>, <span class="ltx_text ltx_bib_pages">pp. 215–220</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S6.SS4.p2.1" title="6.4 Phase Transition and Sharp Kolmogorov Bound ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§6.4</span></a>,
<a href="#S8.SS0.SSS0.Px4.p1.1" title="Coupon Collector Variants and Phase Transitions. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib14" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[14]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Eule and J. J. Metzger</span><span class="ltx_text ltx_bib_year"> (2016)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Non-equilibrium steady states of stochastic processes with intermittent resetting</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">New J. Phys.</span> <span class="ltx_text ltx_bib_volume">18</span>, <span class="ltx_text ltx_bib_pages">pp. 033006</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib16" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[15]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. R. Evans, S. N. Majumdar, and G. Schehr</span><span class="ltx_text ltx_bib_year"> (2020)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Stochastic resetting and applications</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">J. Phys. A</span> <span class="ltx_text ltx_bib_volume">53</span>, <span class="ltx_text ltx_bib_pages">pp. 193001</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.I1.i3.p1.1" title="In 1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3rd item</span></a>,
<a href="#S5.SS2.p1.1" title="5.2 The Laplace Transform Formula and Affine Structure ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§5.2</span></a>,
<a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib15" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[16]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. R. Evans and S. N. Majumdar</span><span class="ltx_text ltx_bib_year"> (2011)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Diffusion with stochastic resetting</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Phys. Rev. Lett.</span> <span class="ltx_text ltx_bib_volume">106</span>, <span class="ltx_text ltx_bib_pages">pp. 160601</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.I1.i3.p1.1" title="In 1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3rd item</span></a>,
<a href="#S1.SS3.p14.1" title="1.3 Main Results ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S5.SS6.p1.1" title="5.6 Worked Example: Brownian First Passage ‣ 5 Continuous-Time Theory ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§5.6</span></a>,
<a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib18" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[17]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. Flajolet, D. Gardy, and L. Thimonier</span><span class="ltx_text ltx_bib_year"> (1992)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Birthday paradox, coupon collectors, caching algorithms and self-organizing search</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Discrete Appl. Math.</span> <span class="ltx_text ltx_bib_volume">39</span>, <span class="ltx_text ltx_bib_pages">pp. 207–229</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px4.p1.1" title="Coupon Collector Variants and Phase Transitions. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib17" class="ltx_bibitem ltx_bib_book"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[18]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. Flajolet and R. Sedgewick</span><span class="ltx_text ltx_bib_year"> (2009)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Analytic combinatorics</span>.
</span>
<span class="ltx_bibblock"> <span class="ltx_text ltx_bib_publisher">Cambridge University Press</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px4.p1.1" title="Coupon Collector Variants and Phase Transitions. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib19" class="ltx_bibitem ltx_bib_misc"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[19]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">J. M. Flynn and S. S. Pilyugin</span><span class="ltx_text ltx_bib_year"> (2021)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">First passage with restart in discrete time: with applications to biased random walks on the half-line</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2108.11508</span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p4.1" title="1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S1.SS2.p2.2" title="1.2 Setup and the PGF Formula ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.2</span></a>,
<a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib20" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[20]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">E. Gelenbe</span><span class="ltx_text ltx_bib_year"> (1991)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Product-form queueing networks with negative and positive customers</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">J. Appl. Probab.</span> <span class="ltx_text ltx_bib_volume">28</span>, <span class="ltx_text ltx_bib_pages">pp. 656–663</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.I1.i2.p1.1" title="In 1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2nd item</span></a>,
<a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib21" class="ltx_bibitem ltx_bib_book"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[21]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">B. V. Gnedenko and V. Y. Korolev</span><span class="ltx_text ltx_bib_year"> (1996)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Random summation: limit theorems and applications</span>.
</span>
<span class="ltx_bibblock"> <span class="ltx_text ltx_bib_publisher">CRC Press</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S4.SS2.p8.1.1" title="Proof. ‣ 4.2 The Laplace Expansion ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4.2</span></a>,
<a href="#S4.p1.1" title="4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4</span></a>,
<a href="#S8.SS0.SSS0.Px3.p1.1" title="Exponential Approximation of Geometric Sums. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib22" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[22]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">C. P. Gomes, B. Selman, N. Crato, and H. Kautz</span><span class="ltx_text ltx_bib_year"> (2000)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Heavy-tailed phenomena in satisfiability and constraint satisfaction problems</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">J. Automat. Reason.</span> <span class="ltx_text ltx_bib_volume">24</span>, <span class="ltx_text ltx_bib_pages">pp. 67–100</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib23" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[23]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">N. Grosjean and T. Huillet</span><span class="ltx_text ltx_bib_year"> (2017)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Additional aspects of the generalized linear-fractional branching process</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Inst. Statist. Math.</span> <span class="ltx_text ltx_bib_volume">69</span>, <span class="ltx_text ltx_bib_pages">pp. 1075–1097</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib24" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[24]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">J. Jocković and B. Todić</span><span class="ltx_text ltx_bib_year"> (2024)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Coupon collector problem with reset button</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Mathematics</span> <span class="ltx_text ltx_bib_volume">12</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 239</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S6.SS1.p1.2" title="6.1 Model ‣ 6 Application: Coupon Collector with Reset ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§6.1</span></a>,
<a href="#S8.SS0.SSS0.Px4.p1.1" title="Coupon Collector Variants and Phase Transitions. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib25" class="ltx_bibitem ltx_bib_book"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[25]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">V. V. Kalashnikov</span><span class="ltx_text ltx_bib_year"> (1997)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Geometric sums: bounds for rare events with applications</span>.
</span>
<span class="ltx_bibblock"> <span class="ltx_text ltx_bib_publisher">Springer</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S4.SS3.p1.1" title="4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4.3</span></a>,
<a href="#S4.p1.1" title="4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4</span></a>,
<a href="#S8.SS0.SSS0.Px3.p1.1" title="Exponential Approximation of Geometric Sums. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib26" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[26]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">T. D. Keidar, O. Blumer, B. Hirshberg, and S. Reuveni</span><span class="ltx_text ltx_bib_year"> (2025)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Adaptive resetting for informed search strategies and the design of non-equilibrium steady-states</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Nature Commun.</span> <span class="ltx_text ltx_bib_volume">16</span>, <span class="ltx_text ltx_bib_pages">pp. 7259</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib27" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[27]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">B. Krishna Kumar and D. Arivudainambi</span><span class="ltx_text ltx_bib_year"> (2000)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Transient solution of an M/M/1 queue with catastrophes</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Comput. Math. Appl.</span> <span class="ltx_text ltx_bib_volume">40</span>, <span class="ltx_text ltx_bib_pages">pp. 1233–1240</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib28" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[28]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Lindo and S. Sagitov</span><span class="ltx_text ltx_bib_year"> (2018)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">General linear-fractional branching processes with discrete time</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Stochastics: International Journal of Probability and Stochastic Processes</span> <span class="ltx_text ltx_bib_volume">90</span>, <span class="ltx_text ltx_bib_pages">pp. 364–378</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib29" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[29]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Luby, A. Sinclair, and D. Zuckerman</span><span class="ltx_text ltx_bib_year"> (1993)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Optimal speedup of Las Vegas algorithms</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Inform. Process. Lett.</span> <span class="ltx_text ltx_bib_volume">47</span>, <span class="ltx_text ltx_bib_pages">pp. 173–180</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.I1.i1.p1.1" title="In 1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1st item</span></a>,
<a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib30" class="ltx_bibitem ltx_bib_inproceedings"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[30]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">T. Nakata and I. Kubo</span><span class="ltx_text ltx_bib_year"> (2006)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">A coupon collector’s problem with bonuses</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">DMTCS Proceedings</span>,
</span>
<span class="ltx_bibblock">Vol. <span class="ltx_text ltx_bib_volume">AG</span>, <span class="ltx_text ltx_bib_pages">pp. 215–224</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px4.p1.1" title="Coupon Collector Variants and Phase Transitions. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib31" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[31]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. Neal</span><span class="ltx_text ltx_bib_year"> (2008)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The generalised coupon collector problem</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">J. Appl. Probab.</span> <span class="ltx_text ltx_bib_volume">45</span>, <span class="ltx_text ltx_bib_pages">pp. 621–629</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px4.p1.1" title="Coupon Collector Variants and Phase Transitions. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib32" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[32]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Pal and V. V. Prasad</span><span class="ltx_text ltx_bib_year"> (2019)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Landau-like expansion for phase transitions in stochastic resetting</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Phys. Rev. Research</span> <span class="ltx_text ltx_bib_volume">1</span>, <span class="ltx_text ltx_bib_pages">pp. 032001</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px4.p2.1" title="Coupon Collector Variants and Phase Transitions. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib33" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[33]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Pal and S. Reuveni</span><span class="ltx_text ltx_bib_year"> (2017)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">First passage under restart</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Phys. Rev. Lett.</span> <span class="ltx_text ltx_bib_volume">118</span>, <span class="ltx_text ltx_bib_pages">pp. 030603</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p2.1" title="1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib35" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[34]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">E. A. Peköz, A. Röllin, and N. Ross</span><span class="ltx_text ltx_bib_year"> (2013)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Total variation error bounds for geometric approximation</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Bernoulli</span> <span class="ltx_text ltx_bib_volume">19</span>, <span class="ltx_text ltx_bib_pages">pp. 610–632</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px3.p1.1" title="Exponential Approximation of Geometric Sums. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib34" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[35]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">E. A. Peköz and A. Röllin</span><span class="ltx_text ltx_bib_year"> (2011)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">New rates for exponential approximation and the theorems of Rényi and Yaglom</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Ann. Probab.</span> <span class="ltx_text ltx_bib_volume">39</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages">pp. 587–608</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px3.p1.1" title="Exponential Approximation of Geometric Sums. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib36" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[36]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Rényi</span><span class="ltx_text ltx_bib_year"> (1956)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">A Poisson-folyamat egy jellemzése</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">MTA Mat. Kutató Int. Közl.</span> <span class="ltx_text ltx_bib_volume">1</span>, <span class="ltx_text ltx_bib_pages">pp. 519–527</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.p7.1" title="1.3 Main Results ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S4.SS3.p9.1" title="4.3 The Bridge Theorem ‣ 4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4.3</span></a>,
<a href="#S4.p1.1" title="4 Exponential Approximation ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4</span></a>,
<a href="#S8.SS0.SSS0.Px3.p1.1" title="Exponential Approximation of Geometric Sums. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib37" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[37]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Reuveni</span><span class="ltx_text ltx_bib_year"> (2016)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Optimal stochastic restart renders fluctuations in first passage times universal</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Phys. Rev. Lett.</span> <span class="ltx_text ltx_bib_volume">116</span>, <span class="ltx_text ltx_bib_pages">pp. 170601</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p2.1" title="1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S7.Thmtheorem2.p1.1" title="Remark 7.2 (CV criterion and forced catastrophe). ‣ 7.2 Phase Transition and Convergence Rate ‣ 7 Application: Multi-Phase Task with Catastrophe ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark 7.2</span></a>,
<a href="#S8.SS0.SSS0.Px1.p1.1" title="Stochastic Resetting and the PGF Formula. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib38" class="ltx_bibitem ltx_bib_article"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[38]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Sagitov</span><span class="ltx_text ltx_bib_year"> (2013)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Linear-fractional branching processes with countably many types</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Stochastic Process. Appl.</span> <span class="ltx_text ltx_bib_volume">123</span>, <span class="ltx_text ltx_bib_pages">pp. 2940–2956</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS1.p4.1" title="1.1 Motivation ‣ 1 Introduction ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.1</span></a>,
<a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib39" class="ltx_bibitem ltx_bib_inproceedings"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[39]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. P. A. van Moorsel and K. Wolter</span><span class="ltx_text ltx_bib_year"> (2004)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Analysis and algorithms for restart</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">QEST 2004</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages">pp. 195–204</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
<li id="bib.bib40" class="ltx_bibitem ltx_bib_book"><span class="ltx_tag ltx_bib_key ltx_role_refnum ltx_tag_bibitem">[40]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">K. Wolter</span><span class="ltx_text ltx_bib_year"> (2010)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Stochastic models for fault tolerance: restart, rejuvenation and checkpointing</span>.
</span>
<span class="ltx_bibblock"> <span class="ltx_text ltx_bib_publisher">Springer</span>.
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S8.SS0.SSS0.Px2.p1.1" title="Linear-Fractional Structure across Domains. ‣ 8 Related Work ‣ On Completion Times under Memoryless Catastrophe" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§8</span></a>.
</span></li>
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Sichen Wang, Zhipeng Lu"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="On Completion Times under Memoryless Catastrophe"></div>

</article>
