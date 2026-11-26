---
title: "Unitary Synthesis with a PSPACE Oracle"

authors:
  - me

# 尚未上 arXiv：这里是投稿终稿的定稿日期（2026 年 11 月），按作者要求显示。
# 上 arXiv 后改成 v1 提交日期。
date: 2026-11-03

publication_types: ["manuscript"]
publication: "*Preprint*"
publication_short: "Preprint"

# Publications 列表与上一篇 / 下一篇导航的顺序（越小越靠前），按作者指定。
weight: 5

# 一句话摘要，显示在列表卡片上（不带 TL;DR 标签）。
tldr: 'Every unitary implementable in polynomial space can be implemented in quantum polynomial time with a PSPACE oracle.'

# 与投稿版 sections/abstract.tex 一致；\PSPACE、\BQP 宏展开为 \mathsf{...}。
abstract: |
  For decision problems, polynomial space is the same as polynomial time with a
  $\mathsf{PSPACE}$ oracle. The analogue for unitaries is not obvious, because a
  classical oracle answers questions about strings, while a unitary must be applied to a
  quantum state that cannot be read. We show that every unitary that can be implemented
  in polynomial space can also be implemented in quantum polynomial time with a
  $\mathsf{PSPACE}$ oracle, up to exponentially small error. A classical oracle helps
  because the unitary enters our circuits only through classical gate parameters, which
  can be computed from its matrix entries in polynomial space. More generally, an oracle
  $L$ suffices to implement all polynomial-space unitaries in quantum polynomial time if
  and only if $\mathsf{PSPACE}\subseteq\mathsf{BQP}^L$, so these unitaries are exactly
  as hard as $\mathsf{PSPACE}$ decision problems. In cryptography, this means that
  quantum commitments imply $\mathsf{BQP}\ne\mathsf{PSPACE}$, since a commitment yields
  an EFI pair, whose two states can be distinguished by a measurement implemented in
  polynomial space. For unitary synthesis problems whose input and output sizes can be
  computed in polynomial time, we also show that interaction with an untrusted prover
  gives a polynomial-time verifier exactly the power of polynomial space, even when the
  verifier must be correct on every input state, just as for decision problems.

tags:
  - Quantum Complexity
  - Unitary Synthesis
  - Quantum Cryptography

featured: false

links:
  - type: pdf
    url: paper.pdf
    label: Paper
  - type: code
    url: https://github.com/sichen-wang/unitary-synthesis-pspace-oracle-lean
    label: Lean
---

<article class="ltx_document ltx_authors_1line">




<div class="ltx_pagination ltx_role_newpage"></div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="introduction">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Unitary synthesis is the task of applying a prescribed unitary to an unknown quantum state. A computation can neither copy such a state nor measure it without disturbing it, and the state may be entangled with a system that the computation does not hold, so the unitary has to be applied coherently. This task arises in breaking quantum commitments, compressing quantum states and decoding noisy channels <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>]</cite>.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">Some unitaries are hard for a simple reason. Deciding a language $L$ amounts to implementing its oracle gate $O_{L}\lvert x,b\rangle=\lvert x,b\oplus L(x)\rangle\text{,}$ so a unitary can be as hard as any decision problem. Is this the only reason? If decision problems were easy, would unitaries be easy too? Aaronson and Kuperberg asked this question in 2007, in a form now called the Unitary Synthesis Problem: can every unitary, computable or not, be implemented in polynomial time with a suitable classical oracle <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx5" title="" class="ltx_ref">AK07</a>, Section 7, Problem (4)]</cite>?</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">They conjectured that the answer is no <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx1" title="" class="ltx_ref">Aar16</a>, Section 3.2]</cite>, and there was good reason. A classical oracle answers questions about strings. The state to be transformed is not a string, and the computation cannot read it, so it is not clear what the computation should ask. For preparing a state this problem does not arise, because there is no input: an oracle can supply the rotations that prepare the state qubit by qubit <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx24" title="" class="ltx_ref">GR02</a>]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx1" title="" class="ltx_ref">Aar16</a>, Proposition 3.3.5]</cite>, and one query suffices up to exponentially small error <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx45" title="" class="ltx_ref">Ros24</a>]</cite>. In the same way an oracle can map $\lvert v\rangle\lvert 0\rangle$ to $\lvert v\rangle U\lvert v\rangle$ for a unitary $U$ and each basis state $\lvert v\rangle\text{,}$ but this leaves $v$ in a register, and removing it coherently is the difficulty. Indeed, no circuit with one query of polynomial length implements every unitary, even when the oracle may depend on the unitary <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>]</cite>, and the best algorithm took time $2^{n/2}\operatorname{poly}(n)$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx46" title="" class="ltx_ref">Ros26</a>]</cite>.</p>
</div>
<div id="S1.p4" class="ltx_para">
<p class="ltx_p">A recursive construction then gave a positive answer at constant error <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx43" title="" class="ltx_ref">Ope26</a>]</cite>, with an oracle that is shown to exist but not shown to be computable. This left two questions: how powerful the oracle has to be and, since no generic error reduction is known <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Open Problem 1]</cite>, whether the error can be made exponentially small. For unitaries that can be implemented in polynomial space, the natural candidate is a $\mathsf{PSPACE}$ oracle, because for decision problems $\mathsf{PSPACE}=\mathsf{P}^{\mathsf{PSPACE}}$ is immediate. Bostanci, Efron, Metger, Poremba, Qian and Yuen <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Section 1.1, footnote 3]</cite> and Kretschmer and Tang <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Section 1.1]</cite> ask for the analogue: can every unitary that is implementable in polynomial space also be implemented in quantum polynomial time with a classical $\mathsf{PSPACE}$ oracle?</p>
</div>
<section id="S1.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="results">
<span class="ltx_tag ltx_tag_subsection">1.1 </span>Results</h3>

<div id="S1.SS1.p1" class="ltx_para">
<p class="ltx_p">The answer is yes: every polynomial-space unitary can be implemented in quantum polynomial time with an oracle for $\mathrm{TQBF}\text{,}$ up to exponentially small error. A language $L$ can replace $\mathrm{TQBF}$ if and only if $\mathsf{PSPACE}\subseteq\mathsf{BQP}^{L}\text{,}$ so polynomial-space unitaries are exactly as hard as $\mathsf{PSPACE}$ decision problems. Both statements hold relative to every classical oracle $A\text{,}$ with a $\mathsf{PSPACE}^{A}$-complete language in place of $\mathrm{TQBF}$ and $\mathsf{PSPACE}^{A}$ in place of $\mathsf{PSPACE}\text{.}$</p>
</div>
<div id="S1.SS1.p2" class="ltx_para">
<p class="ltx_p">To state this precisely, we use the classes of Kretschmer and Tang <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>]</cite>, defined formally in <a href="#S2.SS2" title="2.2 Unitary Languages and Their Complexity Classes ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>. A unitary language is a sequence $U=(U_{n})_{n\geq 1}$ in which $U_{n}$ is a unitary on $n$ qubits. It lies in $\mathsf{unitaryP}^{A}$ if a polynomial-time algorithm maps $(1^{n},1^{m})$ to a circuit with oracle gates $O_{A}\text{,}$ which query $A$ in superposition, and this circuit is within $2^{-m}$ in operator norm of a unitary that maps $\lvert\psi\rangle\lvert 0\rangle$ to $(U_{n}\lvert\psi\rangle)\lvert 0\rangle$ for every $\lvert\psi\rangle\text{,}$ where $\lvert 0\rangle$ is the state of the ancillas. The class $\mathsf{unitaryPSPACE}^{A}$ allows a polynomial-space algorithm instead, with circuits of polynomial width and possibly exponentially many gates. The projective classes $\mathsf{projUnitaryP}^{A}$ and $\mathsf{projUnitaryPSPACE}^{A}$ allow the ancillas to end in a fixed state that does not depend on $\lvert\psi\rangle\text{,}$ instead of returning to zero as in the clean classes $\mathsf{unitaryP}^{A}$ and $\mathsf{unitaryPSPACE}^{A}\text{.}$</p>
</div>
<div id="S1.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 1.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Main theorem)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S1.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every classical oracle $A\text{,}$</span></p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="Sx1.EGx1"></span><span class="paper-eq-anchor" id="S1.Ex1"></span><span class="paper-eq-anchor" id="S1.Ex2"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\mathsf{unitaryPSPACE}^{A} &amp; \displaystyle=\bigcup_{L\in\mathsf{PSPACE}^{A}}\mathsf{unitaryP}^{L}, \\
\displaystyle\mathsf{projUnitaryPSPACE}^{A} &amp; \displaystyle=\bigcup_{L\in\mathsf{PSPACE}^{A}}\mathsf{projUnitaryP}^{L}.
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p class="ltx_p"><span class="ltx_text ltx_font_italic">Moreover, if a language $K$ is $\mathsf{PSPACE}^{A}$-complete under polynomial-time many-one reductions computed without access to $A\text{,}$ then $\mathsf{unitaryPSPACE}^{A}=\mathsf{unitaryP}^{K}$ and $\mathsf{projUnitaryPSPACE}^{A}=\mathsf{projUnitaryP}^{K}\text{.}$</span></p>
</div>
</div>
<div id="S1.SS1.p3" class="ltx_para">
<p class="ltx_p">Thus one language, $\mathrm{TQBF}$ when $A=\emptyset\text{,}$ suffices for all sizes and all precisions, with resources polynomial in $n+m\text{.}$</p>
</div>
<div id="S1.SS1.p4" class="ltx_para">
<p class="ltx_p">It was known that the entries of a unitary in $\mathsf{unitaryPSPACE}^{A}$ can be computed in polynomial space relative to $A$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Theorem 6.17]</cite>. Our proof uses nothing else about the unitary. A classical oracle helps because a unitary can be implemented by a circuit that depends only on the sizes, with everything specific to the unitary in classical gate parameters. Our main technical result (<a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>) is a polynomial-time algorithm that writes such a circuit from $(1^{n},1^{m})$ alone. The circuit has polynomially many gates, and in those specific to the unitary a control string selects which one-qubit gate is applied, among possibly exponentially many. These one-qubit gates are computed from the entries of $U_{n}$ in polynomial space, so one language $B\in\mathsf{PSPACE}^{A}\text{,}$ which depends on $U\text{,}$ can encode short words over a fixed gate set that approximate them. The circuit reads the selected words by querying $B$ in superposition over the control strings, and it erases the answers after using them.</p>
</div>
<div id="S1.SS1.p5" class="ltx_para">
<p class="ltx_p">The construction works relative to every classical oracle, so it applies also to a unitary that cannot be computed at all. The language $A_{U}$ that encodes the bits of its entries is the entry oracle of $U$ (<a href="#S2.SS3" title="2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>). Let $\mathsf{unitaryALL}$ be the class of all unitary languages and let $\mathsf{unitaryP}^{\mathsf{ALL}}=\bigcup_{L}\mathsf{unitaryP}^{L}\text{.}$</p>
</div>
<div id="S1.Thmtheorem2" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Corollary 1.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S1.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every unitary language $U$ there is a language $B_{U}\in\mathsf{PSPACE}^{A_{U}}$ with $U\in\mathsf{unitaryP}^{B_{U}}\text{,}$ and one polynomial-time algorithm, which does not depend on $U\text{,}$ produces the circuits. In particular, $\mathsf{unitaryALL}=\mathsf{unitaryP}^{\mathsf{ALL}}\text{.}$</span></p>
</div>
</div>
<div id="S1.SS1.p6" class="ltx_para">
<p class="ltx_p">This answers the Unitary Synthesis Problem at exponential precision, with one algorithm for all unitaries and an oracle for each of them, as in the original question. Under the formalization of Lombardi, Ma and Wright <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>, Definition 3.16]</cite> it is a positive answer, so their Strong Non-Synthesis Conjecture <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>, Conjecture 1.5]</cite> is false (<a href="#S5.Thmtheorem4" title="Proposition 5.4. ‣ 5.3 A Polynomial-Query Adversary for the Oracle State Distinguishing Game ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">5.4</span></a>).</p>
</div>
<div id="S1.SS1.p7" class="ltx_para">
<p class="ltx_p">Is a $\mathsf{PSPACE}$ oracle necessary? The observation we started from says that it is: the oracle gate of a language in $\mathsf{PSPACE}^{A}$ is itself a polynomial-space unitary, and a circuit that implements it decides the language, so a language $L$ can suffice only if $\mathsf{PSPACE}^{A}\subseteq\mathsf{BQP}^{L}\text{.}$ Conversely, if $\mathsf{PSPACE}^{A}\subseteq\mathsf{BQP}^{L}\text{,}$ each oracle gate in the circuits of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> can be replaced by a coherent run of a decider in $\mathsf{BQP}^{L}$ (<a href="#S5.SS1" title="5.1 The Oracle Characterization ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>).</p>
</div>
<div id="S1.Thmtheorem3" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Corollary 1.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S1.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For all classical oracles $A$ and $L\text{,}$</span></p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="Sx1.EGx2"></span><span class="paper-eq-anchor" id="S1.Ex3"></span><span class="paper-eq-anchor" id="S1.Ex4"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\mathsf{unitaryPSPACE}^{A}\subseteq\mathsf{unitaryP}^{L} &amp; \displaystyle\iff\mathsf{PSPACE}^{A}\subseteq\mathsf{BQP}^{L} \\
 &amp; \displaystyle\iff\mathsf{projUnitaryPSPACE}^{A}\subseteq\mathsf{projUnitaryP}^{L}.
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p class="ltx_p"><span class="ltx_text ltx_font_italic">In particular, $\mathsf{unitaryP}^{A}=\mathsf{unitaryPSPACE}^{A}$ if and only if $\mathsf{BQP}^{A}=\mathsf{PSPACE}^{A}\text{,}$ and the same holds for the projective classes.</span></p>
</div>
</div>
<div id="S1.SS1.p8" class="ltx_para">
<p class="ltx_p">So, relative to classical oracles, the hardness of decision problems is the only reason why polynomial-space unitaries are hard. In particular, $\mathsf{P}=\mathsf{PSPACE}$ implies $\mathsf{unitaryP}=\mathsf{unitaryPSPACE}\text{,}$ and no classical oracle can make this implication fail, which answers a question of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Section 1.4]</cite> and <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Section 1.1]</cite>.</p>
</div>
<section id="S1.SS1.SSS0.Px1" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="quantum-cryptography">Quantum cryptography.</h4>

<div id="S1.SS1.SSS0.Px1.p1" class="ltx_para">
<p class="ltx_p">Classically, $\mathsf{P}=\mathsf{NP}$ rules out one-way functions, so cryptography requires hard decision problems. Quantum cryptography might require less: pseudorandom states, which are efficiently generated and cannot be distinguished efficiently from Haar-random states, exist relative to a classical oracle with $\mathsf{P}=\mathsf{NP}\text{,}$ against adversaries with one copy <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx34" title="" class="ltx_ref">KQST23</a>]</cite> and even with polynomially many <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx35" title="" class="ltx_ref">KQT25</a>]</cite>. A weaker assumption still is the existence of EFI pairs <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx9" title="" class="ltx_ref">BCQ23</a>]</cite>, pairs of efficiently generated mixed states that are statistically far apart but computationally indistinguishable, which is equivalent to the existence of quantum commitments <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx9" title="" class="ltx_ref">BCQ23</a>, Theorem 13]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx57" title="" class="ltx_ref">Yan22</a>]</cite>. Since the two states are far apart, some measurement distinguishes them, and the security of the pair says that this measurement is hard to implement. Brakerski, Canetti and Qian ask whether EFI pairs separate $\mathsf{BQP}$ from $\mathsf{PSPACE}\text{,}$ and they suggest synthesizing the measurement with a $\mathsf{PSPACE}$ oracle <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx9" title="" class="ltx_ref">BCQ23</a>, Section 1.2]</cite>. Our results carry this out.</p>
</div>
<div id="S1.Thmtheorem4" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Corollary 1.4</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S1.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">If EFI pairs exist relative to a classical oracle $A\text{,}$ then $\mathsf{BQP}^{A}\neq\mathsf{PSPACE}^{A}\text{.}$ In particular, EFI pairs imply $\mathsf{BQP}\neq\mathsf{PSPACE}\text{.}$</span></p>
</div>
</div>
<div id="S1.SS1.SSS0.Px1.p2" class="ltx_para">
<p class="ltx_p">A proof that quantum commitments exist would therefore separate $\mathsf{BQP}$ from $\mathsf{PSPACE}\text{.}$ A smooth version of the distinguishing measurement can be implemented by a uniform polynomial-time algorithm with a $\mathsf{PSPACE}^{A}$ oracle, and it distinguishes the two states from one copy with inverse-polynomial advantage (<a href="#S5.Thmtheorem3" title="Lemma 5.3. ‣ 5.2 Distinguishing States with a PSPACE Oracle ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.3</span></a>). <a href="#S1.Thmtheorem3" title="Corollary 1.3. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.3</span></a> removes this oracle if $\mathsf{BQP}^{A}=\mathsf{PSPACE}^{A}\text{.}$ The same algorithm breaks single-copy pseudorandom states that are longer than their key, which answers, for these states, the question of Lombardi, Ma and Wright whether a $\mathsf{PSPACE}$ oracle breaks every single-copy pseudorandom state <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>, Section 1.1]</cite>. So the existence of these states implies $\mathsf{BQP}\neq\mathsf{PSPACE}\text{,}$ and hence $\mathsf{P}\neq\mathsf{PSPACE}\text{,}$ as asked in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx34" title="" class="ltx_ref">KQST23</a>, Section 1.4]</cite>.</p>
</div>
</section>
<section id="S1.SS1.SSS0.Px2" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="interactive-synthesis">Interactive synthesis.</h4>

<div id="S1.SS1.SSS0.Px2.p1" class="ltx_para">
<p class="ltx_p">In an interactive implementation, a polynomial-time verifier holds the quantum input and interacts with an untrusted prover, and if it accepts, it should hold the transformed input. For decision problems interaction gives exactly polynomial space <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx30" title="" class="ltx_ref">JJUW11</a>]</cite>, as it does for preparing states <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx47" title="" class="ltx_ref">RY22</a>; <a href="#bib.bibx41" title="" class="ltx_ref">MY23</a>]</cite> and for unitaries in the average case <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Theorem 7.10]</cite>. The worst case is harder, because the verifier holds the only copy of its input, and a prover that receives this copy could alter it without being detected. It remained open <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Open Problem 10]</cite>, even given a $\mathsf{PSPACE}$ oracle for synthesis <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx44" title="" class="ltx_ref">Ros23</a>, Open Problem 29]</cite>. We settle it for size-computable problems, those whose register sizes can be computed in polynomial time. Our verifier never sends its input. It runs a polynomial-time oracle circuit for the problem on its own qubits, and it uses the prover only to obtain quantum states that do not depend on the input, with which it implements the oracle gates.</p>
</div>
<div id="S1.SS1.SSS0.Px2.p2" class="ltx_para">
<p class="ltx_p">We use the model of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>]</cite> (<a href="#S2.SS5" title="2.5 Unitary Synthesis Problems and the Channel-Model Classes ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Sections</span> <span class="ltx_text ltx_ref_tag">2.5</span></a> and <a href="#S2.SS6" title="2.6 The Interactive Class ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.6</span></a>). The target is a partial isometry $U_{x}$ named by an instance $x\text{,}$ from $n_{\mathrm{in}}(x)$ to $n_{\mathrm{out}}(x)\geq n_{\mathrm{in}}(x)$ qubits, that is, a map that acts as an isometry on a subspace, its support, and as zero on the orthogonal complement. The family $(U_{x})_{x}$ is called a unitary synthesis problem <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Definition 3.1]</cite>, not to be confused with the Unitary Synthesis Problem above. A circuit may measure and discard qubits, and at precision $r$ its channel must be within $1/r$ in diamond norm of a channel that agrees with $U_{x}$ on the support. The diamond norm measures the worst case over inputs, including inputs entangled with another register. Such circuits define $\mathsf{unitaryBQP}^{\diamond}$ when they are written in time polynomial in $\lvert x\rvert+r\text{,}$ and $\mathsf{unitaryPSPACE}^{\diamond}$ when they are written and run in space polynomial in $\lvert x\rvert+r\text{.}$ A problem lies in $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}$ if a polynomial-time algorithm writes from $(x,1^{r})$ a verifier with two properties. Some prover is accepted with probability one on every input in the support. For every input, possibly entangled with a register that neither party holds, and every prover accepted with probability at least $1/2\text{,}$ the output on acceptance, together with that register, is within trace distance $1/r$ of the output of some channel that agrees with $U_{x}$ on the support, applied to that input.</p>
</div>
<div id="S1.Thmtheorem5" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 1.5</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S1.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $U$ be a size-computable unitary synthesis problem. Then</span></p>
<table id="S1.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$U\in\mathsf{unitaryPSPACE}^{\diamond}\iff U\in\mathsf{unitaryQIP}^{\diamond}_{1,1/2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div id="S1.SS1.SSS0.Px2.p3" class="ltx_para">
<p class="ltx_p">This is the worst-case analogue of $\mathsf{QIP}=\mathsf{PSPACE}$ for size-computable problems. The condition on the register sizes cannot be dropped from the inclusion of $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}$ in $\mathsf{unitaryPSPACE}^{\diamond}\text{,}$ and it cannot be dropped from the other inclusion unless $\mathsf{P}=\mathsf{PSPACE}$ (<a href="#S7.Thmtheorem11" title="Remark 7.11. ‣ 7.4 The Converse ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark</span> <span class="ltx_text ltx_ref_tag">7.11</span></a>). In this model too, the collapse of the classes is determined by decision classes (<a href="#S6.Thmtheorem5" title="Theorem 6.5. ‣ 6.2 The Collapse Criterion ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.5</span></a>). The size-computable problems in $\mathsf{unitaryPSPACE}^{\diamond}$ all lie in $\mathsf{unitaryBQP}^{\diamond}$ exactly when $\mathsf{BQP}=\mathsf{PSPACE}\text{,}$ and the classes themselves coincide exactly when $\mathsf{P}=\mathsf{PSPACE}\text{,}$ because $\mathsf{unitaryBQP}^{\diamond}$ requires the register sizes to be computed in deterministic polynomial time.</p>
</div>
</section>
</section>
<section id="S1.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="overview">
<span class="ltx_tag ltx_tag_subsection">1.2 </span>Overview</h3>

<div id="S1.SS2.p1" class="ltx_para">
<p class="ltx_p">Every result above uses <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>, which implements a unitary from its entries. Preparing a column of $U_{n}$ leaves its index in a register, which is the difficulty described above. The index can be removed when the matrix has few nonzero entries per row, because a row then gives a short list of candidates for the index. A general $U_{n}$ has no such structure, so we reduce to matrices that do. We implement $U_{n}$ by applying a map, then one call to a family of unitaries of smaller dimension, selected in superposition by a control register, and then the adjoint of a second map. In a suitable basis these two maps have few nonzero entries per row, because the control register records which of the removed coordinates the computation passes through. This is one stage of a recursion. Each stage removes an inverse-polynomial fraction of the coordinates, so polynomially many stages reach dimension one. In the resulting circuit the registers and the order of the gates depend only on $n$ and $m\text{,}$ and the unitary enters only through the one-qubit gates applied for each value of the control registers, which we call the parameters of the circuit (<a href="#S3" title="3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a>). We then compute the parameters in polynomial space, where the required precision grows only additively over the stages, and collect them in one language (<a href="#S4" title="4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a>).</p>
</div>
<div id="S1.SS2.p2" class="ltx_para">
<p class="ltx_p">Consider a stage that implements a unitary $U^{(j)}$ on $d$ coordinates, with $U^{(0)}=U_{n}\text{.}$ We split the coordinates into $k$ leading and $s=d-k$ trailing ones, with $s\geq d/\operatorname{poly}(n)\text{.}$ To remove the trailing ones, we take a unitary $G$ obtained from $U^{(j)}$ in a way described below, with blocks $G_{11},G_{12},G_{21},G_{22}$ for this split, and we return the trailing part of its output to the trailing part of its input through a diagonal unitary $Z\text{,}$ forming a loop. On a leading input $u\text{,}$ the trailing output $x$ then satisfies $x=G_{21}u+G_{22}Zx\text{,}$ and the leading output is $G_{11}u+G_{12}Zx\text{.}$ If $\lVert G_{22}\rVert\leq 3/4\text{,}$ this gives $x=Xu$ and the leading output $U^{(j+1)}u\text{,}$ where</p>
<table id="S1.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$X=(I-G_{22}Z)^{-1}G_{21},\qquad U^{(j+1)}=G_{11}+G_{12}ZX.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $G$ and $Z$ preserve norms, $\lVert u\rVert^{2}+\lVert Xu\rVert^{2}=\lVert U^{(j+1)}u\rVert^{2}+\lVert Xu\rVert^{2}\text{,}$ so $U^{(j+1)}$ is a unitary on the leading coordinates. This is the unitary of the next stage. The inverse $(I-G_{22}Z)^{-1}$ is a geometric series in $G_{22}Z\text{,}$ whose terms are sums over paths, the sequences of trailing coordinates that the loop passes through.</p>
</div>
<div id="S1.SS2.p3" class="ltx_para">
<p class="ltx_p">The trailing block of $U^{(j)}$ itself can have norm one, so we take $G=P_{\mathrm{L}}U^{(j)}P_{\mathrm{R}}\text{,}$ where $P_{\mathrm{L}},P_{\mathrm{R}}$ are unitaries with short descriptions. Random sign diagonals and Hadamard transforms achieve $\lVert G_{22}\rVert\leq 3/4\text{.}$ The argument uses only moments of degree about $n\text{,}$ so signs from seeds of polynomial length suffice, and a search over the seeds in polynomial space replaces the random choice (<a href="#S3.SS2" title="3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>).</p>
</div>
<div id="S1.SS2.p4" class="ltx_para">
<p class="ltx_p">To implement $G$ we relate it to $U^{(j+1)}\text{.}$ In the loop, $G$ maps the input $(u,ZXu)$ to the output $(U^{(j+1)}u,Xu)\text{.}$ With $E=\binom{I}{ZX}$ and $E^{\prime}=\binom{I}{XU^{(j+1)\dagger}}$ this reads $GE=E^{\prime}U^{(j+1)}\text{,}$ and hence $U^{(j+1)}E^{\dagger}=E^{\prime\dagger}G\text{.}$ This would express $G$ through $U^{(j+1)}$ if $E^{\dagger}$ and $E^{\prime\dagger}$ were isometries, but they map $d$ coordinates to $k$ and so cannot be. To supply the missing dimensions, we let $Z=Z(z)$ depend on a control string $z$ and take a superposition over $z\text{.}$ Let $\mathcal{E}_{N}$ be the map $M^{-1/2}\sum_{z}\lvert z\rangle\otimes E(z)^{\dagger}$ over the $M$ control strings, with the geometric series truncated after $N$ terms, so that only paths of length at most $N$ occur, and let $\mathcal{E}^{\prime}_{N}$ be the same map for $G^{\dagger}\text{,}$ with $-z$ in place of $z\text{.}$</p>
</div>
<div id="S1.SS2.p5" class="ltx_para">
<p class="ltx_p">We take the entry of $Z(z)$ at a trailing coordinate $\lambda$ to be $\omega^{v_{\lambda}\cdot z}\text{,}$ where $v_{\lambda}=(1,\lambda,\dots,\lambda^{N})$ and $\omega$ is a root of unity whose order exceeds every coordinate of any sum of at most $N$ of the vectors $v_{\lambda}\text{.}$ A path then contributes to one Fourier frequency of the control register only, the sum of the vectors $v_{\lambda}$ along the path, up to a sign. Thus the frequency records the visited coordinates: the first coordinate of this sum is the length, and the others are power sums, which determine the multiset of visited coordinates by Newton’s identities.</p>
</div>
<div id="S1.SS2.p6" class="ltx_para">
<p class="ltx_p">This record gives the two properties we need. First, the contributions of different path lengths have different frequencies, so they are orthogonal, and the sum of their squared norms telescopes because $G$ is unitary. Therefore $\mathcal{E}_{N}$ and $\mathcal{E}^{\prime}_{N}$ are near-isometries, which preserve norms up to an error exponentially small in $N\text{,}$ and the identity above gives</p>
<table id="S1.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Bigl(\bigoplus_{z}U^{(j+1)}(z)\Bigr)\mathcal{E}_{N}\approx\mathcal{E}^{\prime}_{N}G.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Thus $G$ is implemented by applying $\mathcal{E}_{N}\text{,}$ then the family controlled by $z\text{,}$ then the adjoint of $\mathcal{E}^{\prime}_{N}$ (<a href="#S3.SS3" title="3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>). Second, a path that contributes to a trailing column passes through the coordinate of that column, so a nonzero frequency leaves at most $N$ candidates for the column index, and a row at frequency zero has its only entry in the column of its own leading coordinate. In the Fourier basis each row of these maps therefore has at most $N$ candidate columns, computable from the row index.</p>
</div>
<div id="S1.SS2.p7" class="ltx_para">
<p class="ltx_p">The index can now be removed. After we prepare a column, reversing the preparation of the uniform superposition over the candidates takes the index to zero with inverse-polynomial amplitude. A rotation of a flag qubit makes this amplitude the same for all rows, and amplitude amplification raises it to nearly one, because all singular values of the maps are close to one (<a href="#S3.SS4" title="3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.4</span></a>). With the circuits $C_{\mathcal{E},j},C_{\mathcal{E}^{\prime},j}$ obtained in this way, a stage is</p>
<table id="S1.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C_{j}=P_{\mathrm{L}}^{\dagger}C_{\mathcal{E}^{\prime},j}^{\dagger}C_{j+1}C_{\mathcal{E},j}P_{\mathrm{R}}^{\dagger},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where $C_{j+1}$ implements $\bigoplus_{z}U^{(j+1)}(z)\text{,}$ with the control registers of all earlier stages as further controls. Each stage contains one call to $C_{j+1}\text{,}$ so gate counts add over the stages, and the surrounding maps are contractions, so errors add as well. A truncation length $N$ linear in $m+\log n$ then gives total error below $2^{-m}$ over all stages (<a href="#S3.SS5" title="3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.5</span></a>).</p>
</div>
<div id="S1.SS2.p8" class="ltx_para">
<p class="ltx_p">The unitary enters only through the parameters, which are functions of the unitaries $U^{(j)}\text{,}$ so we must compute entries of these unitaries in polynomial space. An entry of $U^{(j+1)}$ is computed from entries of $U^{(j)}\text{,}$ and so on down to $U_{n}\text{.}$ A term-by-term bound on the series, which has exponentially many paths, multiplies the required precision by a factor greater than one at each stage, and over polynomially many stages this would demand exponentially many bits. Instead we first round the blocks of $G\operatorname{diag}(I,Z)$ to a grid, bound the effect on the inverse through $\lVert(I-G_{22}Z)^{-1}\rVert\leq 4\text{,}$ and then sum the truncated series exactly on the rounded numbers. An entry to $t$ bits of precision then needs entries of the previous stage only to $t+O(n)$ bits, so all precisions are polynomial and polynomial space suffices (<a href="#S4.SS1" title="4.1 The Parameters in Polynomial Space ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>). No error reduction is needed for exponential precision, since error $2^{-m}$ requires only a truncation length linear in $m$ and parameters computed to polynomially many bits.</p>
</div>
<div id="S1.SS2.p9" class="ltx_para">
<p class="ltx_p">Each parameter is a one-qubit gate, which we approximate by short words over $\{I,H,T,T^{\dagger}\}$ using the Solovay–Kitaev theorem, with one further qubit for its global phase. These words can be found in polynomial space, and the language $B$ contains their bits for all sizes, gates and control strings. The algorithm that writes the circuit needs only the format of the queries, so it never evaluates $B$ and is the same for all $A$ and $U$ (<a href="#S4.SS2" title="4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>). This gives <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>.</p>
</div>
<div id="S1.SS2.p10" class="ltx_para">
<p class="ltx_p"><a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> follows. The entries of a unitary in $\mathsf{unitaryPSPACE}^{A}$ can be computed in polynomial space relative to $A\text{,}$ which gives one inclusion, and so can the entries of a polynomial-time circuit with an oracle in $\mathsf{PSPACE}^{A}\text{,}$ which gives the other. A complete language replaces $B$ through the reduction from $B$ to it. The projective classes reduce to the clean ones through $U_{n}\otimes U_{n}^{\dagger}\text{.}$ A circuit for $U_{n}$ that leaves a fixed state on its ancillas, followed by its adjoint on a second data register with the same ancillas, implements this product and returns the ancillas to zero, and setting the second data register to zero turns a circuit for the product into a circuit for $U_{n}$ (<a href="#S4.SS3" title="4.3 The Main Theorem ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4.3</span></a>).</p>
</div>
<div id="S1.SS2.p11" class="ltx_para">
<p class="ltx_p">The other results use <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> as a tool: to implement something, we construct a unitary whose entries can be computed in polynomial space. For <a href="#S1.Thmtheorem4" title="Corollary 1.4. ‣ Quantum cryptography. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.4</span></a>, the optimal measurement between two states depends discontinuously on them, so we take a Hadamard test that implements a smooth version of it (<a href="#S5.SS2" title="5.2 Distinguishing States with a PSPACE Oracle ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>). For <a href="#S1.Thmtheorem5" title="Theorem 1.5. ‣ Interactive synthesis. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.5</span></a> we first need such circuits in the channel model, where a polynomial-space circuit may discard exponentially many qubits, so that keeping them does not give a unitary on polynomially many qubits. The channel itself acts on polynomially many qubits, and the square root of its Choi matrix gives a Stinespring isometry, which a reflection embeds in a unitary whose entries can be computed in polynomial space (<a href="#S6" title="6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6</span></a>).</p>
</div>
<div id="S1.SS2.p12" class="ltx_para">
<p class="ltx_p">This gives the oracle circuit that the verifier of <a href="#S1.Thmtheorem5" title="Theorem 1.5. ‣ Interactive synthesis. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.5</span></a> runs. Up to Hadamard gates, an oracle gate is a phase unitary, a diagonal unitary with entries $\pm 1$ given by a Boolean function $f\text{.}$ The uniform superposition with the same signs, its phase state, can be prepared in polynomial space, so interactive state synthesis lets the verifier obtain it from the prover <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx45" title="" class="ltx_ref">Ros24</a>; <a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>]</cite>. State injection consumes this state and applies the phase unitary, up to the phase unitary of the Boolean derivative $u\mapsto f(u)\oplus f(u\oplus v)\text{,}$ where $v$ is the measurement outcome. Injecting the state of each correction in turn takes further derivatives, and each derivative lowers the degree of the function as a polynomial over $\mathbb{F}_{2}\text{,}$ so after polynomially many injections the correction vanishes. One prover with a persistent memory supplies all these states, but because the target states are pure, the subnormalized state on acceptance is close to a product with the prover’s memory, so the errors add over the calls (<a href="#S7.SS1" title="7.1 State Injection ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Sections</span> <span class="ltx_text ltx_ref_tag">7.1</span></a>, <a href="#S7.SS2" title="7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7.2</span></a> and <a href="#S7.SS3" title="7.3 A Verifier for Oracle Circuits ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7.3</span></a>).</p>
</div>
<div id="S1.SS2.p13" class="ltx_para">
<p class="ltx_p">For the converse, a polynomial-space circuit runs the verifier against a prover that is near-optimal on the all-zero input and computable in polynomial space <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx41" title="" class="ltx_ref">MY23</a>]</cite>. If a prover were accepted with very different probabilities on two inputs, acceptance on a superposition of them, entangled with one further qubit, would change the distribution of this qubit, which no channel on the input can do. So soundness implies that high acceptance on one input gives high acceptance on all inputs. Applied to an honest prover, this gives high acceptance on the all-zero input, so the near-optimal prover is accepted with high probability there, and hence on all inputs. A minimax argument then gives one channel for all inputs (<a href="#S7.SS4" title="7.4 The Converse ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7.4</span></a>).</p>
</div>
<div id="S1.SS2.p14" class="ltx_para">
<p class="ltx_p">Every theorem, corollary and proposition of this paper has also been formalized in Lean 4, with the four facts quoted from the literature (<a href="#S2.Thmtheorem5" title="Fact 2.5 ([KT26, Theorem 6.17, items 1 and 6]). ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Facts</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>, <a href="#S2.Thmtheorem8" title="Fact 2.8 ([DN06, Theorem 1]). ‣ 2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.8</span></a>, <a href="#S7.Thmtheorem4" title="Fact 7.4 ([Ros24, Theorem 1.5 and Section 6], [BEM+26, Section 7.1]). ‣ 7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7.4</span></a> and <a href="#S7.Thmtheorem8" title="Fact 7.8 ([MY23, Theorem 7.1], [BEM+26, Theorem 7.9]). ‣ 7.4 The Converse ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7.8</span></a>) as axioms. The code, with a table matching each statement to its Lean counterpart, is available at <a href="https://github.com/sichen-wang/unitary-synthesis-pspace-oracle-lean" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://github.com/sichen-wang/unitary-synthesis-pspace-oracle-lean</a>.</p>
</div>
</section>
<section id="S1.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="related-work">
<span class="ltx_tag ltx_tag_subsection">1.3 </span>Related Work</h3>

<div id="S1.SS3.p1" class="ltx_para">
<p class="ltx_p">The Unitary Synthesis Problem <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx1" title="" class="ltx_ref">Aar16</a>, Question 3.2.6]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx2" title="" class="ltx_ref">Aar21</a>, Problem 6]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Problem 7.1]</cite> allows an oracle because, by counting, almost all unitaries need exponentially many gates <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx33" title="" class="ltx_ref">Kni95</a>]</cite>. It has been approached from two sides. Aaronson and Kuperberg gave a first lower bound: one query does not suffice for circuits that implement some unitary on their data qubits for every oracle <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx5" title="" class="ltx_ref">AK07</a>, Theorem 6.7]</cite>. Lombardi, Ma and Wright removed this restriction and ruled out one query and polynomially many parallel queries <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>]</cite>, and later work treats few queries <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx29" title="" class="ltx_ref">Hua25</a>; <a href="#bib.bibx20" title="" class="ltx_ref">DLM26</a>]</cite>, the input length of the oracle <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx14" title="" class="ltx_ref">BY26</a>]</cite> and random oracles <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx28" title="" class="ltx_ref">HRW26</a>]</cite>. On the side of algorithms, Rosenthal gave time $2^{n/2}\operatorname{poly}(n)$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx46" title="" class="ltx_ref">Ros26</a>]</cite>, and the manuscript <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx43" title="" class="ltx_ref">Ope26</a>]</cite> gives polynomial resources at constant diamond error. Our circuits make polynomially many sequential queries of polynomial length, at exponentially small error.</p>
</div>
<div id="S1.SS3.p2" class="ltx_para">
<p class="ltx_p">A second question is how powerful the oracle has to be. Aaronson asks whether $\mathsf{P}=\mathsf{PSPACE}$ would give small circuits for explicit unitaries <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx1" title="" class="ltx_ref">Aar16</a>, Section 3.3.1]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx2" title="" class="ltx_ref">Aar21</a>, Section 6]</cite>. Rosenthal observes that polynomial-time synthesis with an oracle in $\mathsf{PSPACE}$ would give such circuits if $\mathsf{BQP}=\mathsf{PSPACE}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx44" title="" class="ltx_ref">Ros23</a>, Section 1.2]</cite>, and Kretschmer and Tang show that efficient synthesis of a polynomial-space unitary with a classical oracle also works with an oracle for the bits of $\mathsf{NEXP}$ witnesses <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Lemma 7.4 and Corollary 7.5]</cite>. <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> and <a href="#S1.Thmtheorem3" title="Corollary 1.3. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.3</span></a> settle this question at exponential precision. Unitary oracles behave differently: an unknown unitary cannot be controlled <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx3" title="" class="ltx_ref">AFCB14</a>]</cite>, and garbage, the fixed state left on the ancillas in the projective classes, cannot always be erased, even in polynomial space <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Theorem 6.23]</cite>. Kretschmer and Tang ask whether polynomial-time implementations can always erase it, up to a global phase <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Question 3.9]</cite>, and relative to a classical oracle $A$ with $\mathsf{BQP}^{A}=\mathsf{PSPACE}^{A}$ they can (<a href="#S5.SS1" title="5.1 The Oracle Characterization ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.1</span></a>).</p>
</div>
<div id="S1.SS3.p3" class="ltx_para">
<p class="ltx_p">These questions belong to the study of complexity classes of states and unitaries, which Rosenthal and Yuen began by asking which tasks interaction can achieve <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx47" title="" class="ltx_ref">RY22</a>]</cite>. They showed that interaction can prepare every state that can be prepared in polynomial space, and that it can implement every polynomial-space unitary acting nontrivially on a polynomial-dimensional subspace <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx47" title="" class="ltx_ref">RY22</a>, Theorem 1.3]</cite>, by sample-based Hamiltonian simulation <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx38" title="" class="ltx_ref">LMR14</a>; <a href="#bib.bibx32" title="" class="ltx_ref">KLL<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>17</a>]</cite>. Metger and Yuen proved the converse for states, and they showed that near-optimal provers can be implemented in polynomial space <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx41" title="" class="ltx_ref">MY23</a>, Theorem 7.1]</cite>, which our converse uses. Bostanci, Efron, Metger, Poremba, Qian and Yuen introduced the channel model and proved the equality of the average-case classes <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Theorem 7.10]</cite>. <a href="#S1.Thmtheorem5" title="Theorem 1.5. ‣ Interactive synthesis. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.5</span></a> gives the worst case for size-computable problems, with completeness one and threshold $1/2\text{.}$</p>
</div>
<div id="S1.SS3.p4" class="ltx_para">
<p class="ltx_p">Part of the interest in these classes comes from cryptography. Multi-copy pseudorandom states <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx31" title="" class="ltx_ref">JLS18</a>]</cite> of superlogarithmic length are broken by one query to a $\mathsf{PSPACE}$ oracle <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx36" title="" class="ltx_ref">Kre21</a>, Theorem 27]</cite>. For EFI pairs, prior work derived separations of unitary classes <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Theorem 8.15]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Theorem 7.14]</cite> and of polynomial time from polynomial space for decision problems with quantum inputs <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx15" title="" class="ltx_ref">CCH<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Theorem 1.19]</cite>. <a href="#S1.Thmtheorem4" title="Corollary 1.4. ‣ Quantum cryptography. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.4</span></a> extends this to decision classes with classical inputs, relative to every classical oracle, and shows that a classical oracle breaks EFI pairs, which was not known <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx19" title="" class="ltx_ref">CMY26</a>, Section 1.3]</cite>. Relative to Haar-random state and unitary oracles, by contrast, commitments are secure against adversaries with unbounded computation and polynomially many copies or queries <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx16" title="" class="ltx_ref">CCS25</a>; <a href="#bib.bibx4" title="" class="ltx_ref">AGL25</a>; <a href="#bib.bibx8" title="" class="ltx_ref">BCN25</a>; <a href="#bib.bibx18" title="" class="ltx_ref">CM26</a>]</cite>.</p>
</div>
<div id="S1.SS3.p5" class="ltx_para">
<p class="ltx_p">On the technical side, our parameters are computed by the kind of recursion that underlies space-bounded quantum computation. It goes back to Savitch <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx48" title="" class="ltx_ref">Sav70</a>]</cite>, and through $\mathsf{BQPSPACE}=\mathsf{PSPACE}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx55" title="" class="ltx_ref">Wat99</a>; <a href="#bib.bibx56" title="" class="ltx_ref">Wat03</a>]</cite> and its relativized form <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Proposition 4.8]</cite> it determines acceptance probabilities and matrix entries. <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> turns such entries into an implementation. For channels we must also remove measurements. Intermediate measurements can be eliminated while preserving decision probabilities <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx22" title="" class="ltx_ref">FR21</a>]</cite>, measurements whose outcomes are discarded can be eliminated in circuits without resets <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx25" title="" class="ltx_ref">GR22</a>]</cite>, and black-box conversions must increase space or time significantly <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx58" title="" class="ltx_ref">Zha24</a>]</cite>. We need a unitary that reproduces a channel on every input, including entangled inputs, and <a href="#S6.Thmtheorem3" title="Lemma 6.3. ‣ 6.1 Implementing Channels with a PSPACE Oracle ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemmas</span> <span class="ltx_text ltx_ref_tag">6.3</span></a> and <a href="#S6.Thmtheorem4" title="Lemma 6.4. ‣ 6.1 Implementing Channels with a PSPACE Oracle ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.4</span></a> construct it from the Choi matrix.</p>
</div>
</section>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="preliminaries">
<span class="ltx_tag ltx_tag_section">2 </span>Preliminaries</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">To prove <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>, we construct polynomial-time circuits with oracle gates from polynomial-space algorithms for matrix entries.</p>
</div>
<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="circuits-and-oracles">
<span class="ltx_tag ltx_tag_subsection">2.1 </span>Circuits and Oracles</h3>

<div id="S2.SS1.p1" class="ltx_para">
<p class="ltx_p">Logarithms are base two, $1^{n}$ is $n$ in unary, basis indices start at $0\text{,}$ and $\mathrm{i}$ is the imaginary unit. We write $\lVert\cdot\rVert\text{,}$ $\lVert\cdot\rVert_{1}$ and $\lVert\cdot\rVert_{F}$ for the operator, trace and Frobenius norms, $D(\rho,\sigma)=\frac{1}{2}\lVert\rho-\sigma\rVert_{1}$ for the trace distance, and $\preceq$ for the Loewner order. A pure state $\lvert\psi\rangle$ is also written $\psi=\lvert\psi\rangle\langle\psi\rvert\text{.}$ The diamond norm of a difference $\Lambda$ of channels is $\lVert\Lambda\rVert_{\diamond}=\sup_{\psi}\lVert(\Lambda\otimes\mathrm{id})(\psi)\rVert_{1}\text{,}$ over pure states $\psi$ on the input and a further register, so diamond distance $\varepsilon$ means trace distance at most $\varepsilon/2$ on every such input.</p>
</div>
<div id="S2.SS1.p2" class="ltx_para">
<p class="ltx_p">We use the circuit model of Kretschmer and Tang <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>]</cite>. A unitary gate acts on named wires. It is given by these wires and by encodings of the real and imaginary parts of its matrix entries, from which a fixed polynomial-time algorithm computes each number to any precision <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definitions 4.1–4.3]</cite>. The matrix it describes is exact, including its global phase. A classical oracle is a language $A\subseteq\{0,1\}^{*}\text{,}$ and its oracle gate <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definition 4.4]</cite> on $\ell$ query qubits and one answer qubit is</p>
<table id="S2.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$O_{A}\lvert x,b\rangle=\lvert x,b\oplus A(x)\rangle\qquad(x\in\{0,1\}^{\ell},\ b\in\{0,1\}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">A unitary circuit is a list of unitary gates and oracle gates. Its width is its number of wires, and $C^{A}$ is the circuit $C$ with its oracle gates set to $O_{A}\text{.}$ The circuits we construct are over the gate set</p>
<table id="S2.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{G}=\{H,T,T^{\dagger},\mathrm{CNOT}\},\qquad H=\frac{1}{\sqrt{2}}\begin{pmatrix}1&amp;1\\ 1&amp;-1\end{pmatrix},\qquad T=\begin{pmatrix}1&amp;0\\ 0&amp;e^{\mathrm{i}\pi/4}\end{pmatrix},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">that is, they use only these gates and oracle gates. Toffoli and NOT gates are exact over $\mathcal{G}$ with ancillas (<a href="#S4.Thmtheorem3" title="Lemma 4.3. ‣ 4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a>), and we use them freely.</p>
</div>
<div id="S2.SS1.p3" class="ltx_para">
<p class="ltx_p">An ancilla is a qubit initialized to $\lvert 0\rangle\text{.}$ We write $\iota_{a}\lvert\psi\rangle=\lvert\psi\rangle\lvert 0^{a}\rangle$ and call the range of $\iota_{a}$ the zero-ancilla subspace. A unitary circuit $C$ on $n+a$ qubits implements a unitary $U$ on $n$ qubits on the zero-ancilla subspace with error $\varepsilon$ if $\lVert C\iota_{a}-\iota_{a}U\rVert\leq\varepsilon$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Section 5.1]</cite>.</p>
</div>
<div id="S2.SS1.p4" class="ltx_para">
<p class="ltx_p">Circuits that decide languages or implement channels may also measure and discard qubits.</p>
</div>
<div id="S2.Thmtheorem1" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">general quantum circuit</em> <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Section 2.3]</cite> consists of gates from $\mathcal{G}\text{,}$ oracle gates, initialization of new qubits to $\lvert 0\rangle\text{,}$ computational-basis measurement and discarding of qubits. A measurement is the dephasing map on its wire, and the outcome stays on that wire. The <em class="ltx_emph ltx_font_italic">space</em> of the circuit is the largest number of qubits present at any point, counting input qubits and initialized qubits that have not yet been discarded. Its description lists its input wires, its output wires and its gates in order, and its <em class="ltx_emph ltx_font_italic">size</em> is the length of the description. A general quantum circuit $\mathcal{C}$ implements a channel, which we denote by the same symbol. A general quantum circuit <em class="ltx_emph ltx_font_italic">with encoded gates</em> <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definitions 4.2 and 4.3]</cite> may in addition apply any channel to named wires, given by encodings of the entries of its matrix representation. This form is needed only for the EFI pairs of <a href="#S5.SS2" title="5.2 Distinguishing States with a PSPACE Oracle ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>. The <em class="ltx_emph ltx_font_italic">matrix representation</em> of an operation $\Lambda$ is the matrix with entries $\langle u\rvert\Lambda(\lvert u^{\prime}\rangle\langle v^{\prime}\rvert)\lvert v\rangle$ for basis indices $u,v$ of the output and $u^{\prime},v^{\prime}$ of the input.</p>
</div>
<div id="S2.Thmtheorem1.p2" class="ltx_para">
<p class="ltx_p">A family of circuits indexed by strings is <em class="ltx_emph ltx_font_italic">time-uniform</em> (<em class="ltx_emph ltx_font_italic">space-uniform</em>) if a deterministic polynomial-time (polynomial-space) machine with no oracle and a write-only output tape, its <em class="ltx_emph ltx_font_italic">generator</em>, writes the description of each member on input its index. In a space-uniform family the description of each gate has length polynomial in the length of the index <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Definition 2.7]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definition 4.5]</cite>.</p>
</div>
</div>
<div id="S2.SS1.p5" class="ltx_para">
<p class="ltx_p">Numbers in an index are written in unary: the index is $(1^{n},1^{m})$ for a circuit that implements a unitary on $n$ qubits at error $2^{-m}\text{,}$ and $(x,1^{r})$ in the channel model of <a href="#S2.SS5" title="2.5 Unitary Synthesis Problems and the Channel-Model Classes ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>. A time-uniform family has size polynomial in the length of the index, whereas a space-uniform family of polynomial width may have exponentially many gates, because the output tape does not count toward the space of its generator.</p>
</div>
</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="unitary-languages-and-their-complexity-classes">
<span class="ltx_tag ltx_tag_subsection">2.2 </span>Unitary Languages and Their Complexity Classes</h3>

<div id="S2.SS2.p1" class="ltx_para">
<p class="ltx_p">The objects we implement are sequences of unitaries, one for each number of qubits. A circuit with ancillas can implement a unitary in two ways: it returns the ancillas to zero, so that it can be used inside a larger coherent computation, or it leaves them in a fixed state.</p>
</div>
<div id="S2.Thmtheorem2" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">unitary language</em> is a sequence $U=(U_{n})_{n\geq 1}$ with $U_{n}\in\mathrm{U}(2^{n})$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definition 4.9]</cite>. A unitary $\widetilde{U}$ on $n+a$ qubits is an <em class="ltx_emph ltx_font_italic">$a$-qubit extension</em> of $U_{n}$ if $\widetilde{U}\iota_{a}=\iota_{a}U_{n}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx59" title="" class="ltx_ref">Zha25</a>]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definition 5.1]</cite>. It is an <em class="ltx_emph ltx_font_italic">$a$-qubit dilation</em> of $U_{n}$ with <em class="ltx_emph ltx_font_italic">garbage state</em> $\lvert g\rangle$ if $\widetilde{U}(\lvert\psi\rangle\lvert 0^{a}\rangle)=(U_{n}\lvert\psi\rangle)\lvert g\rangle$ for every $\lvert\psi\rangle$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definition 5.11]</cite>.</p>
</div>
</div>
<div id="S2.SS2.p2" class="ltx_para">
<p class="ltx_p">By linearity both identities also hold in the presence of further registers.</p>
</div>
<div id="S2.Thmtheorem3" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p">Let $A$ be a classical oracle. A unitary language $U$ belongs to $\mathsf{unitaryP}^{A}$ if there is a time-uniform family $(C_{n,m})_{n,m\geq 1}$ of unitary circuits of width polynomial in $n+m$ such that, for all $n,m\text{,}$ some extension $\widetilde{U}_{n,m}$ of $U_{n}$ satisfies</p>
<table id="S2.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert C^{A}_{n,m}-\widetilde{U}_{n,m}\rVert\leq 2^{-m}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The class $\mathsf{unitaryPSPACE}^{A}$ is defined in the same way with space-uniform families. The classes $\mathsf{projUnitaryP}^{A}$ and $\mathsf{projUnitaryPSPACE}^{A}$ are defined with dilations in place of extensions. As in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>]</cite>, we call the first two the <em class="ltx_emph ltx_font_italic">clean classes</em> and the last two the <em class="ltx_emph ltx_font_italic">projective classes</em>. The class of all unitary languages is $\mathsf{unitaryALL}\text{.}$ We write $\mathsf{unitaryP}^{\mathsf{PSPACE}^{A}}=\bigcup_{L\in\mathsf{PSPACE}^{A}}\mathsf{unitaryP}^{L}$ and $\mathsf{unitaryP}^{\mathsf{ALL}}=\bigcup_{L}\mathsf{unitaryP}^{L}\text{,}$ and likewise for the projective classes.</p>
</div>
</div>
<div id="S2.SS2.p3" class="ltx_para">
<p class="ltx_p">The norm compares matrices, so the global phase of $U_{n}$ counts in the clean classes. In the projective classes it does not, because a dilation of $U_{n}$ with garbage state $\lvert g\rangle$ is also a dilation of $\phi U_{n}$ with garbage state $\bar{\phi}\lvert g\rangle$ for $\lvert\phi\rvert=1\text{.}$ An extension is a dilation with $\lvert g\rangle=\lvert 0^{a}\rangle\text{,}$ so the clean classes lie in the projective ones.</p>
</div>
<div id="S2.SS2.p4" class="ltx_para">
<p class="ltx_p">These are the classes of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definitions 5.2, 5.6, 5.12 and 5.17]</cite> for a classical oracle. Kretschmer and Tang write the precision as a number $\varepsilon$ with $O(\log(1/\varepsilon))$ bits, which amounts to our unary $m\text{.}$ Their circuits may also use the adjoint, transpose and conjugate of $O_{A}\text{,}$ which are all $O_{A}$ itself, and in the clean classes they may use controlled queries. A controlled query with control $c$ and answer $b$ is obtained exactly by doing the following twice: query into a further qubit $b^{\prime}\text{,}$ then apply a Toffoli gate from $c$ and $b^{\prime}$ onto $b\text{.}$ For every value of $b^{\prime}$ this adds $c(b^{\prime}\oplus A(x))\oplus cb^{\prime}=c\,A(x)$ to $b$ and restores $b^{\prime}\text{,}$ so the replacement does not change the error.</p>
</div>
<div id="S2.SS2.p5" class="ltx_para">
<p class="ltx_p">For decision problems, $\mathsf{BQP}^{A}$ is the class of languages $L$ for which there is a time-uniform family $(\mathcal{C}_{n})_{n\geq 1}\text{,}$ indexed by $1^{n}\text{,}$ of general quantum circuits with oracle gates $O_{A}\text{,}$ each with $n$ input wires and one output wire, such that measuring the output of $\mathcal{C}_{n}$ on $\lvert x\rangle\text{,}$ for $x\in\{0,1\}^{n}\text{,}$ gives $L(x)$ with probability at least $2/3\text{.}$</p>
</div>
<div id="S2.SS2.p6" class="ltx_para">
<p class="ltx_p">The class $\mathsf{PSPACE}^{A}$ consists of the languages decided by deterministic polynomial-space machines with oracle $A$ whose query tape counts toward the space bound, so that queries have polynomial length. This is the convention of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definitions 4.4–4.6 and footnote 5]</cite>. A language $K$ is $\mathsf{PSPACE}^{A}$-complete if it lies in $\mathsf{PSPACE}^{A}$ and every language in $\mathsf{PSPACE}^{A}$ reduces to it by a polynomial-time many-one reduction computed without access to $A\text{.}$ One such language consists of the triples $(M,x,1^{s})$ such that the oracle machine $M$ with oracle $A$ accepts $x$ within space $s\text{,}$ and for $A=\emptyset$ another is $\mathrm{TQBF}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx52" title="" class="ltx_ref">SM73</a>]</cite>.</p>
</div>
</section>
<section id="S2.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="entries-computable-in-polynomial-space">
<span class="ltx_tag ltx_tag_subsection">2.3 </span>Entries Computable in Polynomial Space</h3>

<div id="S2.SS3.p1" class="ltx_para">
<p class="ltx_p">Our proofs access a unitary only through its matrix entries, and the entrywise characterization of Kretschmer and Tang (<a href="#S2.Thmtheorem5" title="Fact 2.5 ([KT26, Theorem 6.17, items 1 and 6]). ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>) shows that this is no restriction for polynomial-space unitaries.</p>
</div>
<div id="S2.SS3.p2" class="ltx_para">
<p class="ltx_p">A dyadic number is a rational with a power of two as denominator, written in binary, and a complex dyadic number has dyadic real and imaginary parts. An algorithm computes a complex number to precision $t$ if it outputs a complex dyadic number within $2^{-t}$ of it. The $2^{-t}$ grid consists of the complex numbers whose two components are multiples of $2^{-t}\text{.}$ To round a computable number to this grid, we compute it to precision $t+4$ and round each component of the result to the nearest multiple of $2^{-t}\text{,}$ with ties to the smaller rational. The result is within $2^{-t}$ of the number, and it is the same every time we compute it.</p>
</div>
<div id="S2.Thmtheorem4" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.4</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p">Let $A$ be a classical oracle. A unitary language $U$ has <em class="ltx_emph ltx_font_italic">entries computable in polynomial space relative to $A$</em> if a deterministic polynomial-space algorithm with oracle $A\text{,}$ its <em class="ltx_emph ltx_font_italic">entry algorithm</em>, computes $\langle u\rvert U_{n}\lvert v\rangle$ to precision $t$ on input $(1^{n},u,v,1^{t})\text{,}$ for $u,v\in\{0,1\}^{n}\text{,}$ with $O(t+1)$ bits per component.</p>
</div>
</div>
<div id="S2.Thmtheorem5" class="ltx_theorem ltx_theorem_fact">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Fact 2.5</span></span><span class="ltx_text ltx_font_bold"> </span>(<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Theorem 6.17, items 1 and 6]</cite>)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every classical oracle $A\text{,}$ a unitary language lies in $\mathsf{unitaryPSPACE}^{A}$ if and only if it has entries computable in polynomial space relative to $A\text{.}$</span></p>
</div>
</div>
<div id="S2.SS3.p3" class="ltx_para">
<p class="ltx_p">Kretschmer and Tang state this for the real and imaginary parts of $\langle v\rvert U_{n}\lvert u\rangle$ on input $(u,v)$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definition 6.10]</cite>. We obtain the form above by swapping the indices, computing each part to precision $t+3$ and rounding it to the $2^{-t-2}$ grid.</p>
</div>
<div id="S2.SS3.p4" class="ltx_para">
<p class="ltx_p">The entries of an arbitrary unitary language need not be computable, but an oracle can encode them. The entry oracle $A_{U}$ of a unitary language $U$ is the set of strings $\langle 1^{n},u,v,1^{t},\mathrm{part},j\rangle$ with $u,v\in\{0,1\}^{n}\text{,}$ $t\geq 0\text{,}$ $\mathrm{part}\in\{\mathrm{re},\mathrm{im}\}$ and $j\geq 0$ such that bit $j\text{,}$ least significant first, of the integer $\lfloor(\alpha+1)2^{t+2}\rfloor$ is one, where $\alpha$ is the part of $\langle u\rvert U_{n}\lvert v\rangle$ selected by $\mathrm{part}\text{.}$ Malformed strings are not in $A_{U}\text{.}$ Since $\lvert\alpha\rvert\leq 1\text{,}$ the integer lies in $[0,2^{t+3}]\text{,}$ so its bits with $j\leq t+3$ determine $\alpha$ within $2^{-t-2}\text{.}$ Hence one polynomial-time oracle machine $\mathrm{dec}\text{,}$ the same for all $U\text{,}$ queries these $2(t+4)$ bits and computes $\langle u\rvert U_{n}\lvert v\rangle$ to precision $t\text{,}$ and $\mathrm{dec}^{A_{U}}$ is an entry algorithm for every $U\text{.}$</p>
</div>
<div id="S2.SS3.p5" class="ltx_para">
<p class="ltx_p">In polynomial space one can sum exponentially many terms and multiply exponentially many matrices, and hence compute the matrix representation of a space-uniform circuit of polynomial space. Below, $\operatorname{poly}(\cdot)$ stands for a polynomial in the listed quantities that depends on nothing else.</p>
</div>
<div id="S2.Thmtheorem6" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 2.6</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The following hold relative to every classical oracle $A\text{.}$</span></p>
<ol id="S2.I1" class="ltx_enumerate">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(i)</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p class="ltx_p">$\mathsf{PSPACE}^{\mathsf{PSPACE}^{A}}=\mathsf{PSPACE}^{A}$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(ii)</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The number </span>$\pi$<span class="ltx_text ltx_font_italic">, square roots of nonnegative rationals, and sines and cosines of rational angles and of rational multiples of </span>$\pi$<span class="ltx_text ltx_font_italic"> can be computed to precision </span>$t$<span class="ltx_text ltx_font_italic"> in space polynomial in </span>$t$<span class="ltx_text ltx_font_italic"> and the bit length of the input </span><cite class="ltx_cite ltx_citemacro_cite"><span class="ltx_text ltx_font_italic">[</span><a href="#bib.bibx12" title="" class="ltx_ref">Bre76</a><span class="ltx_text ltx_font_italic">]</span></cite><span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(iii)</span> 
<div id="S2.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">A sum of exponentially many dyadic numbers of polynomial bit length, each computable in polynomial space from an index of polynomial length, can be computed exactly in polynomial space.</span></p>
</div>
</li>
<li id="S2.I1.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(iv)</span> 
<div id="S2.I1.i4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The lexicographically first string of polynomial length that passes a polynomial-space test can be found in polynomial space.</span></p>
</div>
</li>
<li id="S2.I1.i5" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(v)</span> 
<div id="S2.I1.i5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let </span>$S_{1},\dots,S_{\ell}$<span class="ltx_text ltx_font_italic"> be </span>$2^{w}\times 2^{w}$<span class="ltx_text ltx_font_italic"> matrices such that every product </span>$S_{k}\cdots S_{j}$<span class="ltx_text ltx_font_italic"> with </span>$1\leq j\leq k\leq\ell$<span class="ltx_text ltx_font_italic"> has entries of modulus at most one. Suppose that an algorithm computes the entries of each </span>$S_{i}$<span class="ltx_text ltx_font_italic"> to precision </span>$t$<span class="ltx_text ltx_font_italic">, with </span>$O(t+1)$<span class="ltx_text ltx_font_italic"> bits per component, in space </span>$\mathrm{sp}(w,t)$<span class="ltx_text ltx_font_italic"> on input the index </span>$i$<span class="ltx_text ltx_font_italic">, the two basis indices and </span>$1^{t}$<span class="ltx_text ltx_font_italic">, where </span>$\mathrm{sp}$<span class="ltx_text ltx_font_italic"> is nondecreasing in </span>$t$<span class="ltx_text ltx_font_italic">. Then an algorithm computes the entries of </span>$S_{\ell}\cdots S_{1}$<span class="ltx_text ltx_font_italic"> to precision </span>$t$<span class="ltx_text ltx_font_italic">, with </span>$O(t+1)$<span class="ltx_text ltx_font_italic"> bits per component, in space</span></p>
<table id="S2.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathrm{sp}\bigl(w,\,t+(w+2)\lceil\log\ell\rceil\bigr)+\operatorname{poly}(w,t,\log\ell).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</li>
<li id="S2.I1.i6" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(vi)</span> 
<div id="S2.I1.i6.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let </span>$d$<span class="ltx_text ltx_font_italic"> be a power of two. The quantum Fourier transform </span>$F_{d}\lvert u\rangle=d^{-1/2}\sum_{v&lt;d}e^{2\pi\mathrm{i}uv/d}\lvert v\rangle$<span class="ltx_text ltx_font_italic"> has entries that can be computed to precision </span>$t$<span class="ltx_text ltx_font_italic"> in space </span>$\operatorname{poly}(\log d,t)$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
<li id="S2.I1.i7" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(vii)</span> 
<div id="S2.I1.i7.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let </span>$(\mathcal{C}_{x})_{x}$<span class="ltx_text ltx_font_italic"> be a space-uniform family of general quantum circuits, possibly with encoded gates, with oracle gates </span>$O_{A}$<span class="ltx_text ltx_font_italic"> and with space polynomial in </span>$\lvert x\rvert$<span class="ltx_text ltx_font_italic">. Then the entries of the matrix representation of </span>$\mathcal{C}_{x}$<span class="ltx_text ltx_font_italic"> can be computed to precision </span>$t$<span class="ltx_text ltx_font_italic">, with </span>$O(t+1)$<span class="ltx_text ltx_font_italic"> bits per component, on input </span>$x$<span class="ltx_text ltx_font_italic">, the four basis indices and </span>$1^{t}$<span class="ltx_text ltx_font_italic">, in space polynomial in </span>$\lvert x\rvert+t$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
</ol>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS3.p6" class="ltx_para">
<p class="ltx_p">A polynomial-space machine can run a subroutine on an input of polynomial length, keep a counter over exponentially many indices, and keep a running sum or the current candidate. This proves (iii) and (iv), and it proves (i) because the queries of the outer machine have polynomial length. Item (ii) is standard multiple-precision arithmetic <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx12" title="" class="ltx_ref">Bre76</a>]</cite>, and (vi) follows from (ii).</p>
</div>
<div id="S2.SS3.p7" class="ltx_para">
<p class="ltx_p">Item (v) is the recursion of Savitch <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx48" title="" class="ltx_ref">Sav70</a>]</cite> applied to matrices. To compute an entry of $S_{k}\cdots S_{k^{\prime}}$ to precision $t^{\prime}\text{,}$ we split the product at its midpoint, compute the entries of the two halves to precision $t^{\prime}+w+2\text{,}$ sum the $2^{w}$ products of entries, and round each component of the sum to $t^{\prime}+2$ fractional bits. The true entries have modulus at most one, so each product has error at most $3\cdot 2^{-t^{\prime}-w-2}$ and the sum at most $\frac{3}{4}2^{-t^{\prime}}\text{,}$ and the rounding adds at most $\sqrt{2}\,2^{-t^{\prime}-3}&lt;\frac{1}{4}2^{-t^{\prime}}\text{.}$ The depth of the recursion is $\lceil\log\ell\rceil\text{,}$ so the factors are computed at precision at most $t+(w+2)\lceil\log\ell\rceil\text{.}$ Each level stores the ends of its interval, its basis indices, a counter over the $2^{w}$ intermediate indices, one computed entry and the partial sum, and only one entry of a factor is computed at a time, which gives the stated space.</p>
</div>
<div id="S2.SS3.p8" class="ltx_para">
<p class="ltx_p">For item (vii), let $p$ be a polynomial bound on the space of $\mathcal{C}_{x}\text{.}$ A table, updated with each operation of $\mathcal{C}_{x}\text{,}$ assigns the at most $p$ qubits present at each point to $p$ fixed wires, and the other wires are in state $\lvert 0\rangle\text{.}$ Each operation is then a channel on these wires: a unitary or oracle gate acts by conjugation, an encoded gate by its given matrix representation, a measurement of a wire has the two projectors of this wire as Kraus operators, and a new qubit and a discarded qubit both act as the reset of a wire, with Kraus operators $\lvert 0\rangle\langle 0\rvert$ and $\lvert 0\rangle\langle 1\rvert\text{.}$ The matrix representations of these channels are the factors for item (v), with $2p$-bit indices, and their entries can be computed in polynomial space, since the generator, run with a counter, gives any single operation. The hypothesis of item (v) holds because a product of these factors is the matrix representation of a channel, with Kraus operators $M_{i}$ say, and</p>
<table id="S2.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Bigl\lvert\sum_{i}\langle u\rvert M_{i}\lvert u^{\prime}\rangle\langle v^{\prime}\rvert M_{i}^{\dagger}\lvert v\rangle\Bigr\rvert\leq 1$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">by the Cauchy–Schwarz inequality and $\sum_{i}M_{i}^{\dagger}M_{i}=I\text{.}$ A bound on the operator norm would not suffice, since the matrix representation of a reset on $p$ wires has norm $2^{p/2}\text{.}$ An entry of the matrix representation of $\mathcal{C}_{x}$ is the sum, over the at most $2^{p}$ basis states of the wires outside the output, of entries of the product with the wires outside the input at $\lvert 0\rangle\text{.}$ We compute these to precision $t+p+1\text{,}$ with error at most $2^{-t-1}$ in the sum, and round to $t+2$ fractional bits.
∎</p>
</div>
</div>
</section>
<section id="S2.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="approximation-of-unitaries-and-channels">
<span class="ltx_tag ltx_tag_subsection">2.4 </span>Approximation of Unitaries and Channels</h3>

<div id="S2.SS4.p1" class="ltx_para">
<p class="ltx_p">The classes of <a href="#S2.Thmtheorem3" title="Definition 2.3. ‣ 2.2 Unitary Languages and Their Complexity Classes ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Definition</span> <span class="ltx_text ltx_ref_tag">2.3</span></a> require a bound on the whole space, while our constructions give a bound on the zero-ancilla subspace. The next lemma converts the second bound into the first.</p>
</div>
<div id="S2.Thmtheorem7" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 2.7</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem7.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $Y_{1},Y_{2}\colon\mathcal{K}\to\mathcal{H}$ be isometries with $\lVert Y_{1}-Y_{2}\rVert\leq\varepsilon&lt;1\text{.}$ There is a unitary $W$ on $\mathcal{H}$ with $WY_{1}=Y_{2}$ and $\lVert W-I\rVert\leq 2\varepsilon+\varepsilon^{2}\text{.}$ Consequently, if a unitary circuit $C$ implements a unitary $U$ on the zero-ancilla subspace with error $\varepsilon&lt;1\text{,}$ then $U$ has an extension $\widetilde{U}$ with $\lVert C-\widetilde{U}\rVert\leq 3\varepsilon\text{.}$ The same holds for a dilation with garbage state $\lvert g\rangle$ if $\lVert C\iota_{a}-U\otimes\lvert g\rangle\rVert\leq\varepsilon\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS4.p2" class="ltx_para">
<p class="ltx_p">We extend $Y_{2}Y_{1}^{\dagger}$ from the range of $Y_{1}$ to the whole space and take the unitary part of its polar decomposition. Let $\Pi_{i}=Y_{i}Y_{i}^{\dagger}$ and $X=Y_{2}Y_{1}^{\dagger}+(I-\Pi_{2})(I-\Pi_{1})\text{.}$ Since $(I-\Pi_{1})Y_{1}=0$ and $(I-\Pi_{2})Y_{2}=0\text{,}$ we have</p>
<table id="S2.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$XY_{1}=Y_{2},\qquad X-I=(Y_{2}-Y_{1})Y_{1}^{\dagger}-\Pi_{2}(I-\Pi_{1}),\qquad X^{\dagger}X=I-(I-\Pi_{1})\Pi_{2}(I-\Pi_{1}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Put $E=(I-\Pi_{1})Y_{2}=(I-\Pi_{1})(Y_{2}-Y_{1})\text{,}$ so that $\lVert E\rVert\leq\varepsilon\text{.}$ Then $\Pi_{2}(I-\Pi_{1})=Y_{2}E^{\dagger}$ and $(I-\Pi_{1})\Pi_{2}(I-\Pi_{1})=EE^{\dagger}\text{,}$ hence $\lVert X-I\rVert\leq 2\varepsilon$ and $(1-\varepsilon^{2})I\preceq X^{\dagger}X\preceq I\text{.}$ So $X$ is invertible and $W=X(X^{\dagger}X)^{-1/2}$ is unitary. The identity for $X^{\dagger}X$ gives $(X^{\dagger}X)Y_{1}=Y_{1}\text{,}$ so $(X^{\dagger}X)^{-1/2}Y_{1}=Y_{1}$ and $WY_{1}=XY_{1}=Y_{2}\text{.}$ Finally $X=W(X^{\dagger}X)^{1/2}$ gives $\lVert W-X\rVert=\lVert I-(X^{\dagger}X)^{1/2}\rVert\leq 1-\sqrt{1-\varepsilon^{2}}\leq\varepsilon^{2}\text{,}$ so $\lVert W-I\rVert\leq 2\varepsilon+\varepsilon^{2}\text{.}$</p>
</div>
<div id="S2.SS4.p3" class="ltx_para">
<p class="ltx_p">For the second statement, apply this to $Y_{1}=C\iota_{a}$ and $Y_{2}=\iota_{a}U$ and put $\widetilde{U}=WC\text{.}$ Then $\widetilde{U}\iota_{a}=\iota_{a}U$ and $\lVert C-\widetilde{U}\rVert=\lVert W-I\rVert\leq 3\varepsilon\text{.}$ For a dilation, take $Y_{2}=U\otimes\lvert g\rangle$ instead.
∎</p>
</div>
</div>
<div id="S2.SS4.p4" class="ltx_para">
<p class="ltx_p">Isometries that are close also give channels that are close. For unit vectors, $\lVert\psi-\psi^{\prime}\rVert_{1}\leq 2\lVert\lvert\psi\rangle-\lvert\psi^{\prime}\rangle\rVert\text{,}$ because $\psi-\psi^{\prime}=(\lvert\psi\rangle-\lvert\psi^{\prime}\rangle)\langle\psi\rvert+\lvert\psi^{\prime}\rangle(\langle\psi\rvert-\langle\psi^{\prime}\rvert)\text{.}$ So for isometries $Y,Y^{\prime}$ at distance $\varepsilon$ into an output register and a register $\mathsf{E}\text{,}$ the channels $\operatorname{Tr}_{\mathsf{E}}(Y\cdot Y^{\dagger})$ and $\operatorname{Tr}_{\mathsf{E}}(Y^{\prime}\cdot Y^{\prime\dagger})$ are at diamond distance at most $2\varepsilon\text{.}$ Likewise an acceptance probability changes by at most $2\varepsilon$ when the output vector moves by $\varepsilon\text{,}$ and composing with a channel does not increase the diamond distance.</p>
</div>
<div id="S2.SS4.p5" class="ltx_para">
<p class="ltx_p">The Solovay–Kitaev theorem says that short words over a suitable finite set approximate every one-qubit gate of determinant one. Here a word over a set $\mathcal{S}$ of matrices is a finite list of its elements, multiplied in application order, and its length is its number of letters.</p>
</div>
<div id="S2.Thmtheorem8" class="ltx_theorem ltx_theorem_fact">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Fact 2.8</span></span><span class="ltx_text ltx_font_bold"> </span>(<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx21" title="" class="ltx_ref">DN06</a>, Theorem 1]</cite>)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem8.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $\mathcal{S}\subset\mathrm{SU}(2)$ be a finite inverse-closed set that generates a dense subgroup of $\mathrm{SU}(2)\text{.}$ There is a polynomial $p_{\mathcal{S}}$ such that every $W\in\mathrm{SU}(2)$ is within $2^{-t}$ of a word over $\mathcal{S}$ of length at most $p_{\mathcal{S}}(t)\text{.}$</span></p>
</div>
</div>
</section>
<section id="S2.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="unitary-synthesis-problems-and-the-channel-model-classes">
<span class="ltx_tag ltx_tag_subsection">2.5 </span>Unitary Synthesis Problems and the Channel-Model Classes</h3>

<div id="S2.SS5.p1" class="ltx_para">
<p class="ltx_p">In <a href="#S6" title="6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Sections</span> <span class="ltx_text ltx_ref_tag">6</span></a> and <a href="#S7" title="7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a> we use the model of Bostanci, Efron, Metger, Poremba, Qian and Yuen <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>]</cite>, in which their questions about collapse and interaction are posed. The map to be implemented is indexed by a string and may be defined only on a subspace, circuits may measure and discard, and the error is $1/r$ in diamond norm. In this model circuits have no oracle gates unless stated otherwise.</p>
</div>
<div id="S2.SS5.p2" class="ltx_para">
<p class="ltx_p">A partial isometry from a register $\mathsf{A}$ to a register $\mathsf{B}$ is a map $U=Y\Pi$ with $\Pi$ a projector on $\mathsf{A}$ and $Y\colon\mathsf{A}\to\mathsf{B}$ an isometry <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Definition 2.3]</cite>. Its support $\operatorname{supp}U$ is the range of $\Pi\text{.}$ A channel completion of $U$ is a channel $\Phi$ with $\Phi(\Pi\rho\Pi)=U\rho U^{\dagger}$ for every state $\rho$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Definition 2.4]</cite>, so it is prescribed on the support and arbitrary off it.</p>
</div>
<div id="S2.Thmtheorem9" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.9</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem9.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">unitary synthesis problem</em> <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Definition 3.1]</cite> is a family $U=(U_{x})_{x\in\{0,1\}^{*}}$ of partial isometries from a register $\mathsf{A}_{x}$ of $n_{\mathrm{in}}(x)$ qubits to a register $\mathsf{B}_{x}$ of $n_{\mathrm{out}}(x)$ qubits, both polynomial in $\lvert x\rvert\text{.}$ The string $x$ is the <em class="ltx_emph ltx_font_italic">instance</em>, and $\Pi_{x}$ is the projector onto $\operatorname{supp}U_{x}\text{.}$ The problem is <em class="ltx_emph ltx_font_italic">size-computable</em> if $x\mapsto(n_{\mathrm{in}}(x),n_{\mathrm{out}}(x))$ is computable in polynomial time.</p>
</div>
<div id="S2.Thmtheorem9.p2" class="ltx_para">
<p class="ltx_p">A problem $U$ belongs to $\mathsf{unitaryPSPACE}^{\diamond}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Definitions 3.2 and 3.8]</cite> if there is a space-uniform family $(\mathcal{C}_{x,r})_{x,r}$ of general quantum circuits of space polynomial in $\lvert x\rvert+r\text{,}$ with input register $\mathsf{A}_{x}$ and output register $\mathsf{B}_{x}\text{,}$ such that, for all $x$ and $r\geq 1\text{,}$ some channel completion $\Phi_{x,r}$ of $U_{x}$ satisfies</p>
<table id="S2.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert\mathcal{C}_{x,r}-\Phi_{x,r}\rVert_{\diamond}\leq 1/r.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The class $\mathsf{unitaryBQP}^{\diamond}$ is defined in the same way with time-uniform families, and $\mathsf{unitaryBQP}^{\diamond,L}$ allows oracle gates $O_{L}$ as well. We call this setting the <em class="ltx_emph ltx_font_italic">channel model</em>.</p>
</div>
</div>
<div id="S2.SS5.p3" class="ltx_para">
<p class="ltx_p">Since $T^{\dagger}=T^{7}\text{,}$ these are the classes of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>]</cite>, whose gate set is $\{H,T,\mathrm{CNOT}\}\text{.}$ The marker $\diamond$ distinguishes them from the classes of <a href="#S2.Thmtheorem3" title="Definition 2.3. ‣ 2.2 Unitary Languages and Their Complexity Classes ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Definition</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>, since the name $\mathsf{unitaryPSPACE}$ denotes both in the literature.</p>
</div>
</section>
<section id="S2.SS6" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-interactive-class">
<span class="ltx_tag ltx_tag_subsection">2.6 </span>The Interactive Class</h3>

<div id="S2.SS6.p1" class="ltx_para">
<p class="ltx_p">In an interactive implementation a polynomial-time verifier keeps the quantum input and interacts with an untrusted prover. The input may be entangled with a register that neither party holds, called the purifying register $\mathsf{R}\text{,}$ and the output of an accepted run, together with $\mathsf{R}\text{,}$ must be correct.</p>
</div>
<div id="S2.Thmtheorem10" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.10</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem10.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">verifier</em> is a sequence of general quantum circuits, one for each round, on an ancilla register, a message register, an acceptance qubit and the output register $\mathsf{B}_{x}\text{.}$ It starts with all its registers at zero except the input, which occupies the first $n_{\mathrm{in}}(x)$ qubits of its ancilla register <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Section 2.4]</cite>. A <em class="ltx_emph ltx_font_italic">prover</em> $\mathcal{P}$ consists of an initial state of a private memory $\mathsf{M}\text{,}$ independent of $\mathsf{A}_{x}\mathsf{R}\text{,}$ and a sequence of channels on the message register and $\mathsf{M}\text{,}$ so the memory persists through the interaction. A unitary synthesis problem $U$ belongs to $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Definition 4.1]</cite> if a deterministic polynomial-time machine maps $(x,1^{r})$ to a verifier $V_{x,r}$ such that the following hold for all $x$ and $r\geq 1\text{.}$</p>
<dl id="S2.I2" class="ltx_description">
<dt id="S2.I2.ix1" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_italic">Completeness.</span></span></dt>
<dd class="ltx_item">
<div id="S2.I2.ix1.p1" class="ltx_para">
<p class="ltx_p">Some prover, the <em class="ltx_emph ltx_font_italic">honest prover</em>, is accepted with probability one on every input supported in $\operatorname{supp}U_{x}\text{.}$</p>
</div>
</dd>
<dt id="S2.I2.ix2" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_italic">Soundness.</span></span></dt>
<dd class="ltx_item">
<div id="S2.I2.ix2.p1" class="ltx_para">
<p class="ltx_p">For every pure state $\psi$ on $\mathsf{A}_{x}\mathsf{R}$ and every prover $\mathcal{P}$ that is accepted on $\psi$ with probability at least $1/2\text{,}$ there is a channel completion $\Phi$ of $U_{x}$ with</p>
<table id="S2.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D\bigl(\sigma,(\Phi\otimes\mathrm{id})(\psi)\bigr)\leq 1/r,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where $\sigma$ is the state of $\mathsf{B}_{x}\mathsf{R}$ conditioned on acceptance.</p>
</div>
</dd>
</dl>
</div>
</div>
<div id="S2.SS6.p2" class="ltx_para">
<p class="ltx_p">Completeness asks only for acceptance, because soundness then bounds the error of the honest output.</p>
</div>
</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="implementing-unitaries-from-their-entries">
<span class="ltx_tag ltx_tag_section">3 </span>Implementing Unitaries from Their Entries</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">By <a href="#S2.Thmtheorem5" title="Fact 2.5 ([KT26, Theorem 6.17, items 1 and 6]). ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>, every language in $\mathsf{unitaryPSPACE}^{A}$ has entries computable in polynomial space relative to $A\text{.}$ To place it in $\mathsf{unitaryP}^{\mathsf{PSPACE}^{A}}\text{,}$ which is the main inclusion of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>, it therefore suffices to implement a unitary language from its entries.</p>
</div>
<div id="S3.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 3.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $A$ be a classical oracle and let $U$ be a unitary language with entries computable in polynomial space relative to $A\text{.}$ There are a language $B\in\mathsf{PSPACE}^{A}$ and a polynomial-time algorithm that maps $(1^{n},1^{m})$ to a unitary circuit $C_{n,m}$ over $\mathcal{G}$ such that, for all $n,m\geq 1\text{,}$ some extension $\widetilde{U}$ of $U_{n}$ satisfies</span></p>
<table id="S3.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert C^{B}_{n,m}-\widetilde{U}\rVert\leq 2^{-m}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The algorithm that produces $C_{n,m}$ is the same for every $A$ and every $U\text{,}$ and only $B$ depends on them.</span></p>
</div>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">The circuits come from a recursion on the dimension. One stage implements a unitary on $d$ coordinates by one call to a family of unitaries on $d-s$ coordinates, with $s\geq d/\operatorname{poly}(n)\text{,}$ and a control register selects the member of this family in superposition. Polynomially many stages therefore reach dimension one, and since the error of the call enters with coefficient one, the errors of the stages only add. The call is preceded by one map and followed by the adjoint of another. In a Fourier basis these two maps have few nonzero entries per row, so the index of a prepared column can be removed coherently. This recursive scheme comes from <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx43" title="" class="ltx_ref">Ope26</a>]</cite>, and we prove here every fact we use about it.</p>
</div>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">The gate list of the resulting circuit depends only on the sizes, and the unitary enters only through the one-qubit gates that the circuit applies for each value of its control registers. We therefore construct the circuit here with these gates left as parameters, and prove it correct for their exact values. In <a href="#S4" title="4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a> we compute the parameters in polynomial space and compile them into the language $B\text{.}$</p>
</div>
<section id="S3.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="parameterized-circuits-and-the-recursion">
<span class="ltx_tag ltx_tag_subsection">3.1 </span>Parameterized Circuits and the Recursion</h3>

<div id="S3.SS1.p1" class="ltx_para">
<p class="ltx_p">The one-qubit gates selected by control strings are uniformly controlled gates <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx13" title="" class="ltx_ref">BVMS05</a>]</cite>, also called multiplexors <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx49" title="" class="ltx_ref">SBM06</a>]</cite>. Such a gate has a control register, a target register and a unitary $W_{y}$ on the target register for each control string $y\text{,}$ and it acts as</p>
<table id="S3.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\bigoplus_{y}W_{y}:=\sum_{y}\lvert y\rangle\langle y\rvert\otimes W_{y}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">For example, a diagonal unitary on a register is one such gate, with one qubit as the target and the others as controls. Since the norm of a direct sum of matrices is the largest norm of its summands, a bound that holds for every control string holds for the whole gate.</p>
</div>
<div id="S3.SS1.p2" class="ltx_para">
<p class="ltx_p">A parameterized circuit is a unitary circuit over $\mathcal{G}$ and uniformly controlled gates with one-qubit targets in which the unitaries $W_{y}$ are left unspecified. These unitaries are its parameters. There can be exponentially many of them, but the registers, the gate order and the control lists form a short description. In our circuits this description depends only on the sizes, and a polynomial-time algorithm writes it (<a href="#S3.Thmtheorem8" title="Lemma 3.8. ‣ 3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.8</span></a>).</p>
</div>
<div id="S3.SS1.p3" class="ltx_para">
<p class="ltx_p">The recursion works in an $n$-qubit register, the data register, on the subspace $\mathcal{H}_{d}$ spanned by $\lvert 0\rangle,\dots,\lvert d-1\rangle$ for some $d\leq 2^{n}\text{.}$ For a unitary $T$ on a subspace of the state space of the non-ancilla qubits, such as $\mathcal{H}_{d}\text{,}$ a circuit $C$ implements $T$ on the zero-ancilla subspace with error $\varepsilon$ if $\lVert C\iota_{a}-\iota_{a}T\rVert\leq\varepsilon$ on the subspace of $T\text{.}$ A parameterized circuit can implement a whole family of unitaries with the same description: if, with parameters that depend on a string $y\text{,}$ it implements $T_{y}$ with error $\varepsilon_{y}\text{,}$ then adding a control register that holds $y$ to each uniformly controlled gate gives a parameterized circuit that implements $\bigoplus_{y}T_{y}$ with error $\max_{y}\varepsilon_{y}\text{.}$</p>
</div>
<div id="S3.SS1.p4" class="ltx_para">
<p class="ltx_p">For a split $d=k+s\text{,}$ the leading coordinates $c=1,\dots,k$ are the basis states $\lvert c-1\rangle$ and the trailing coordinates $\lambda=1,\dots,s$ are the basis states $\lvert k+\lambda-1\rangle\text{.}$ A matrix on $\mathcal{H}_{d}$ then has four blocks, and its lower right $s\times s$ block is its trailing block.</p>
</div>
<div id="S3.Thmtheorem2" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 3.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p">Fix $n\text{,}$ an integer $N\geq 1$ and $\beta=nN+\lceil\log(N+1)\rceil\text{,}$ so that $2^{\beta}&gt;N2^{nN}\text{.}$ The recursion runs in <em class="ltx_emph ltx_font_italic">stages</em> $j=0,1,\dots\text{.}$ Stage $j$ implements a unitary $U^{(j)}$ on $\mathcal{H}_{d_{j}}\text{,}$ with $d_{0}=2^{n}$ and $U^{(0)}=U_{n}\text{,}$ and $d_{j}=k_{j}+s_{j}$ is split into leading and trailing coordinates. It has a <em class="ltx_emph ltx_font_italic">control register</em> that holds a <em class="ltx_emph ltx_font_italic">control string</em> $z\in\mathbb{Z}_{2^{\beta}}^{N+1}\text{,}$ and $z$ selects the unitary $U^{(j+1)}(z)$ on $\mathcal{H}_{k_{j}}$ that stage $j+1$ implements. Thus $U^{(j)}$ depends on the control strings $z_{&lt;j}$ of all earlier stages, and we write $U^{(j)}$ for $U^{(j)}(z_{&lt;j})$ when these are fixed.</p>
</div>
</div>
<div id="S3.SS1.p5" class="ltx_para">
<p class="ltx_p">Given $U^{(j)}$ on $\mathcal{H}_{d}$ with $d\geq 2\text{,}$ we find unitaries $P_{\mathrm{L}},P_{\mathrm{R}}$ with short descriptions such that the trailing block of $G=P_{\mathrm{L}}U^{(j)}P_{\mathrm{R}}$ has norm at most $3/4$ (<a href="#S3.SS2" title="3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>). From the blocks of $G$ we define, by a geometric series in the trailing block, the unitaries $U^{(j+1)}(z)$ and two maps $\mathcal{E}_{N},\mathcal{E}^{\prime}_{N}$ from $\mathcal{H}_{d}$ to the control register and the leading coordinates. These maps are close to isometries, and $(\bigoplus_{z}U^{(j+1)}(z))\mathcal{E}_{N}$ is close to $\mathcal{E}^{\prime}_{N}G$ (<a href="#S3.SS3" title="3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>). Hence $G$ is close to $\mathcal{E}_{N}^{\prime\dagger}(\bigoplus_{z}U^{(j+1)}(z))\mathcal{E}_{N}\text{.}$ In the Fourier basis of the control register the two maps have few nonzero entries per row, so they can be implemented by circuits $C_{\mathcal{E},j},C_{\mathcal{E}^{\prime},j}$ (<a href="#S3.SS4" title="3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.4</span></a>), and</p>
<table id="S3.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C_{j}=P_{\mathrm{L}}^{\dagger}C_{\mathcal{E}^{\prime},j}^{\dagger}C_{j+1}C_{\mathcal{E},j}P_{\mathrm{R}}^{\dagger}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.1)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">implements $U^{(j)}$ if $C_{j+1}$ implements $\bigoplus_{z}U^{(j+1)}(z)$ (<a href="#S3.SS5" title="3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.5</span></a>). At dimension one $U^{(j)}$ is a phase, and $C_{j}$ is one diagonal gate that applies it.</p>
</div>
</section>
<section id="S3.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="a-contractive-trailing-block">
<span class="ltx_tag ltx_tag_subsection">3.2 </span>A Contractive Trailing Block</h3>

<div id="S3.SS2.p1" class="ltx_para">
<p class="ltx_p">The unitaries of the next stage are defined by a series in the trailing block of the current unitary, and this series converges geometrically when the block has norm bounded away from one. The trailing block can have norm one, as the identity shows. We therefore multiply the unitary on both sides by unitaries with short descriptions that reduce this norm to at most $3/4\text{.}$ We also want the block to be large, because its coordinates are the ones that a stage removes: with $s\geq d/\operatorname{poly}(n)\text{,}$ polynomially many stages reach dimension one. For $2\leq d\leq 2^{n}\text{,}$ we take</p>
<table id="S3.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d^{\prime}=2^{\lfloor\log d\rfloor},\qquad s=\max\bigl\{1,\lfloor d^{\prime}/(2^{20}(n+1)^{2})\rfloor\bigr\},\qquad k=d-s,\qquad\kappa=\frac{3}{4}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.2)</span></td>
</tr></tbody>
</table>
</div>
<div id="S3.Thmtheorem3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $2\leq d\leq 2^{n}\text{,}$ and let $U$ be a unitary on $\mathcal{H}_{d}$ whose entries a deterministic algorithm computes to any requested precision. There are unitaries $P_{\mathrm{L}},P_{\mathrm{R}}$ on $\mathcal{H}_{d}$ such that the trailing block of $G=P_{\mathrm{L}}UP_{\mathrm{R}}$ has norm at most $\kappa\text{.}$ Extended by the identity outside $\mathcal{H}_{d}\text{,}$ these unitaries and their adjoints are implemented exactly, with ancillas returned to zero, by parameterized circuits of $O(n)$ uniformly controlled gates on $O(n)$ ancillas whose gate lists depend only on $n$ and $d\text{.}$ The parameters can be computed with polynomial additional space, calling the algorithm for the entries of $U$ only at the precision $t_{0}=16(n+1)\text{.}$</span></p>
</div>
</div>
<div id="S3.SS2.p2" class="ltx_para">
<p class="ltx_p">For $s=1\text{,}$ swapping two rows is enough. For $s&gt;1$ we take each of $P_{\mathrm{L}},P_{\mathrm{R}}$ to be a sign diagonal and a Hadamard transform, and random signs suffice. The signs of $P_{\mathrm{R}}$ make all rows of the trailing $d^{\prime}\times s$ submatrix $\Gamma$ of $UP_{\mathrm{R}}$ small. The trailing block of $G$ is then a sum of matrices built from these rows, with independent signs from $P_{\mathrm{L}}\text{,}$ and small rows make the variance of this sum small. The second moment alone is not enough, because it controls only the Frobenius norm, whose square has expectation as large as $s^{2}/d^{\prime}\text{.}$ That would limit $s$ to about $\sqrt{d^{\prime}}$ and require about $2^{n/2}$ stages, whereas moments of degree about $n$ allow $s=d^{\prime}/\operatorname{poly}(n)\text{.}$ A moment of degree $2\nu$ is a polynomial of degree $2\nu$ in the signs, so $2\nu$-wise independent signs have the same moments. Signs from seeds of polynomial length therefore suffice, and a search over seeds replaces the random choice.</p>
</div>
<div id="S3.Thmtheorem4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.4</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $\nu$ be a positive integer and let $(\xi_{i})_{i}$ be finitely many $2\nu$-wise independent unbiased signs.</span></p>
<ol id="S3.I1" class="ltx_enumerate">
<li id="S3.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(i)</span> 
<div id="S3.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">If </span>$\alpha_{i}\in\mathbb{C}$<span class="ltx_text ltx_font_italic"> and </span>$\sum_{i}\lvert\alpha_{i}\rvert^{2}\leq\tau$<span class="ltx_text ltx_font_italic">, then </span>$\mathbb{E}\lvert\sum_{i}\xi_{i}\alpha_{i}\rvert^{2\nu}\leq(4\nu\tau)^{\nu}$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
<li id="S3.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(ii)</span> 
<div id="S3.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">If </span>$\Theta_{i}$<span class="ltx_text ltx_font_italic"> are Hermitian </span>$d\times d$<span class="ltx_text ltx_font_italic"> matrices and </span>$\sum_{i}\Theta_{i}^{2}\preceq\tau I$<span class="ltx_text ltx_font_italic">, then </span>$\mathbb{E}\operatorname{Tr}(\sum_{i}\xi_{i}\Theta_{i})^{2\nu}\leq d(4\nu\tau)^{\nu}$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
</ol>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS2.p3" class="ltx_para">
<p class="ltx_p">The quantities in both bounds are polynomials of degree $2\nu$ in the signs, so their expectations are the same as for independent signs, and we assume independence. Part (i) is the case $d=2$ of part (ii): for $\Theta_{i}=\bigl(\begin{smallmatrix}0&amp;\alpha_{i}\\ \bar{\alpha}_{i}&amp;0\end{smallmatrix}\bigr)$ we have $\Theta_{i}^{2}=\lvert\alpha_{i}\rvert^{2}I$ and $(\sum_{i}\xi_{i}\Theta_{i})^{2}=\lvert\sum_{i}\xi_{i}\alpha_{i}\rvert^{2}I\text{.}$</p>
</div>
<div id="S3.SS2.p4" class="ltx_para">
<p class="ltx_p">For part (ii), let $X=\sum_{i}\xi_{i}\Theta_{i}\text{.}$ We show that $\mathbb{E}\operatorname{Tr}X^{2k}\leq(2k-1)\tau\,\mathbb{E}\operatorname{Tr}X^{2k-2}$ for $k\geq 1\text{.}$ Starting from $\operatorname{Tr}X^{0}=d\text{,}$ this gives $\mathbb{E}\operatorname{Tr}X^{2\nu}\leq d(2\nu-1)!!\,\tau^{\nu}\leq d(4\nu\tau)^{\nu}\text{.}$ For $k=1\text{,}$ independence gives $\mathbb{E}\operatorname{Tr}X^{2}=\sum_{i}\operatorname{Tr}\Theta_{i}^{2}\leq d\tau\text{.}$ For $k\geq 2\text{,}$ let $h=2k-2\text{.}$ Fix $i$ and let $X_{+},X_{-}$ be $X$ with $\xi_{i}=1,-1\text{,}$ so that $X_{+}-X_{-}=2\Theta_{i}\text{.}$ Averaging over $\xi_{i}$ and writing $X_{+}^{h+1}-X_{-}^{h+1}=\sum_{l=0}^{h}X_{+}^{l}(X_{+}-X_{-})X_{-}^{h-l}$ gives</p>
<table id="S3.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}\operatorname{Tr}X^{2k}=\sum_{i}\mathbb{E}\,\xi_{i}\operatorname{Tr}(\Theta_{i}X^{h+1})=\sum_{i}\mathbb{E}\sum_{l=0}^{h}\operatorname{Tr}\bigl(\Theta_{i}X_{+}^{l}\Theta_{i}X_{-}^{h-l}\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">In eigenbases $X_{+}\lvert e_{u}\rangle=\lambda_{u}\lvert e_{u}\rangle$ and $X_{-}\lvert f_{v}\rangle=\lambda^{\prime}_{v}\lvert f_{v}\rangle\text{,}$ the weighted inequality of arithmetic and geometric means, for even $h\text{,}$ gives</p>
<table id="S3.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{Tr}\bigl(\Theta_{i}X_{+}^{l}\Theta_{i}X_{-}^{h-l}\bigr)=\sum_{u,v}\lvert\langle f_{v}\rvert\Theta_{i}\lvert e_{u}\rangle\rvert^{2}\lambda_{u}^{l}\lambda_{v}^{\prime\,h-l}\leq\frac{l}{h}\operatorname{Tr}(\Theta_{i}^{2}X_{+}^{h})+\frac{h-l}{h}\operatorname{Tr}(\Theta_{i}^{2}X_{-}^{h}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Summing over $l$ gives $h+1$ times the average over $\xi_{i}$ of $\operatorname{Tr}(\Theta_{i}^{2}X^{h})\text{.}$ Summing over $i$ and using $\sum_{i}\Theta_{i}^{2}\preceq\tau I$ and $X^{h}\succeq 0$ proves the claim.
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>.</h6>
<div id="S3.SS2.p5" class="ltx_para">
<p class="ltx_p">Suppose first that $s&gt;1\text{,}$ and let $\nu=4(n+1)\text{.}$ Let $U^{\prime}$ be the trailing $d^{\prime}\times d^{\prime}$ submatrix of $U$ and let $H_{s}$ consist of the last $s$ columns of the Hadamard transform $H^{\otimes\log d^{\prime}}\text{,}$ whose entries are $\pm 1/\sqrt{d^{\prime}}\text{.}$ For sign diagonals $\Xi_{1},\Xi_{2}$ of size $d^{\prime}\text{,}$ let $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ act on the last $d^{\prime}$ coordinates of $\mathcal{H}_{d}$ as $H^{\otimes\log d^{\prime}}\Xi_{1}$ and $\Xi_{2}H^{\otimes\log d^{\prime}}\text{,}$ and as the identity on the other coordinates. The Hadamard transform is real and symmetric, so its last $s$ rows form $H_{s}^{\dagger}\text{,}$ and the trailing block of $G$ is</p>
<table id="S3.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$G_{22}=H_{s}^{\dagger}\Xi_{1}\Gamma,\qquad\Gamma=U^{\prime}\Xi_{2}H_{s}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.3)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">To bound its norm, let $\Theta=\bigl(\begin{smallmatrix}0&amp;G_{22}\\ G_{22}^{\dagger}&amp;0\end{smallmatrix}\bigr)\text{.}$ The eigenvalues of $\Theta$ are $\pm$ the singular values of $G_{22}\text{,}$ so $\lVert G_{22}\rVert^{2\nu}\leq\operatorname{Tr}\Theta^{2\nu}\text{,}$ and it suffices to make $\operatorname{Tr}\Theta^{2\nu}$ smaller than $2^{-2\nu}\text{.}$</p>
</div>
<div id="S3.SS2.p6" class="ltx_para">
<p class="ltx_p">To search for the signs in polynomial space, we take them from seeds of polynomial length. A seed is a polynomial $f$ of degree below $2\nu$ over the field with $d^{\prime}$ elements, and we represent this field by the first monic irreducible binary polynomial of degree $\log d^{\prime}\text{.}$ Its signs are $\xi_{i}=(-1)^{\phi(f(i))}\text{,}$ where $i$ runs over the field, identified with the last $d^{\prime}$ coordinates, and $\phi$ is a fixed nonzero $\mathbb{F}_{2}$-linear functional. For a uniformly random seed these signs are $2\nu$-wise independent and unbiased <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx54" title="" class="ltx_ref">Vad12</a>, Remark 3.25, Construction 3.32 and Proposition 3.33]</cite>. To test a pair of seeds, we use the entries of $U$ at precision $t_{0}\text{.}$ Let $\widehat{U}^{\prime}$ be the matrix of these computed entries, let $\widehat{G}_{22}=H_{s}^{\dagger}\Xi_{1}\widehat{U}^{\prime}\Xi_{2}H_{s}\text{,}$ and let $\widehat{\Theta}=\bigl(\begin{smallmatrix}0&amp;\widehat{G}_{22}\\ \widehat{G}_{22}^{\dagger}&amp;0\end{smallmatrix}\bigr)\text{.}$ Two entries of $H_{s}$ multiply to $\pm 1/d^{\prime}\text{,}$ so the entries of $\widehat{G}_{22}$ are dyadic numbers within $d^{\prime}2^{-t_{0}}$ of those of $G_{22}\text{,}$ and $\lVert\widehat{G}_{22}-G_{22}\rVert\leq\varepsilon$ with $\varepsilon=sd^{\prime}2^{-t_{0}}\leq 2^{2n-t_{0}}\text{.}$ Since $\lVert\widehat{\Theta}-\Theta\rVert\leq\varepsilon\text{,}$ $\lVert\Theta\rVert\leq 1$ and $(1+\varepsilon)^{2\nu}\leq 2\text{,}$ writing $\widehat{\Theta}^{2\nu}-\Theta^{2\nu}$ as a sum of $2\nu$ terms with one factor $\widehat{\Theta}-\Theta$ each gives</p>
<table id="S3.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\bigl\lvert\operatorname{Tr}\widehat{\Theta}^{2\nu}-\operatorname{Tr}\Theta^{2\nu}\bigr\rvert\leq 2s\cdot 2\nu\,\varepsilon(1+\varepsilon)^{2\nu}\leq 2^{n+1}\cdot 4\nu\cdot 2^{2n-t_{0}}&lt;2^{-2\nu}/4.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The number $\operatorname{Tr}\widehat{\Theta}^{2\nu}$ is a sum of products of entries of $\widehat{\Theta}$ and can be computed exactly. The algorithm takes the lexicographically first pair of seeds with $\operatorname{Tr}\widehat{\Theta}^{2\nu}\leq 2^{-2\nu}/2\text{.}$ For this pair $\operatorname{Tr}\Theta^{2\nu}\leq\frac{3}{4}2^{-2\nu}\text{,}$ and hence $\lVert G_{22}\rVert&lt;1/2\text{.}$</p>
</div>
<div id="S3.SS2.p7" class="ltx_para">
<p class="ltx_p">It remains to show that some pair of seeds satisfies this inequality. We choose the seed of $\Xi_{2}$ first. An entry of $\Gamma$ is a sum over the signs of $\Xi_{2}$ whose squared coefficients sum to at most $1/d^{\prime}\text{,}$ because the rows of $U^{\prime}$ have norm at most one. By Markov’s inequality for the moment of degree $2\nu$ and <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a>(i) with $\tau=1/d^{\prime}\text{,}$ the event $\lvert\Gamma_{il}\rvert^{2}&gt;32(n+1)/d^{\prime}$ has probability at most $(4\nu/(32(n+1)))^{\nu}=2^{-\nu}\text{.}$ There are at most $2^{2n}$ entries and $2^{2n-\nu}&lt;1\text{,}$ so some seed gives $\lvert\Gamma_{il}\rvert^{2}\leq 32(n+1)/d^{\prime}$ for all entries. For this seed, every row $\Gamma_{i}$ of $\Gamma$ satisfies $\lVert\Gamma_{i}\rVert^{2}\leq\tau\text{,}$ now with $\tau=32s(n+1)/d^{\prime}\text{.}$</p>
</div>
<div id="S3.SS2.p8" class="ltx_para">
<p class="ltx_p">Now fix this $\Xi_{2}$ and choose the seed of $\Xi_{1}\text{.}$ With $(H_{s})_{i}$ the rows of $H_{s}$ and $\xi_{i}$ the signs of $\Xi_{1}\text{,}$ <a href="#S3.E3" title="In 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.3)</span></a> reads $G_{22}=\sum_{i}\xi_{i}(H_{s})_{i}^{\dagger}\Gamma_{i}\text{,}$ so $\Theta=\sum_{i}\xi_{i}\Theta_{i}$ with $\Theta_{i}=\bigl(\begin{smallmatrix}0&amp;(H_{s})_{i}^{\dagger}\Gamma_{i}\\ \Gamma_{i}^{\dagger}(H_{s})_{i}&amp;0\end{smallmatrix}\bigr)\text{.}$ Since $\lVert\Gamma_{i}\rVert^{2}\leq\tau\text{,}$ $\lVert(H_{s})_{i}\rVert^{2}=s/d^{\prime}\leq\tau\text{,}$ $H_{s}^{\dagger}H_{s}=I$ and $\Gamma^{\dagger}\Gamma\preceq I\text{,}$</p>
<table id="S3.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{i}\Theta_{i}^{2}=\begin{pmatrix}\sum_{i}\lVert\Gamma_{i}\rVert^{2}(H_{s})_{i}^{\dagger}(H_{s})_{i}&amp;0\\ 0&amp;(s/d^{\prime})\,\Gamma^{\dagger}\Gamma\end{pmatrix}\preceq\tau I.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $s\leq d^{\prime}/(2^{20}(n+1)^{2})\text{,}$ we have $4\nu\tau\leq 2^{-11}\text{,}$ and <a href="#S3.Thmtheorem4" title="Lemma 3.4. ‣ 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a>(ii) in dimension $2s\leq 2^{n+1}$ gives $\mathbb{E}\operatorname{Tr}\Theta^{2\nu}\leq 2s\,2^{-11\nu}&lt;2^{-2\nu}/4\text{.}$ Some seed of $\Xi_{1}$ therefore has $\operatorname{Tr}\Theta^{2\nu}&lt;2^{-2\nu}/4\text{.}$ Then $\operatorname{Tr}\widehat{\Theta}^{2\nu}&lt;2^{-2\nu}/2\text{,}$ as required.</p>
</div>
<div id="S3.SS2.p9" class="ltx_para">
<p class="ltx_p">Suppose now that $s=1\text{.}$ Some entry of the last column of $U$ has squared modulus at most $1/d\leq 1/2\text{.}$ The squared moduli of the entries of this column at precision $t_{0}$ are within $3\cdot 2^{-t_{0}}\leq 1/64$ of the true ones, and the algorithm selects the first row whose computed value is at most $1/2+1/64\text{.}$ Its entry has squared modulus at most $1/2+1/32&lt;\kappa^{2}\text{.}$ Let $P_{\mathrm{L}}$ be the transposition of this row and the last row, and let $P_{\mathrm{R}}=I\text{.}$ The trailing block of $G$ is then this entry, of modulus below $\kappa\text{.}$</p>
</div>
<div id="S3.SS2.p10" class="ltx_para">
<p class="ltx_p">It remains to implement $P_{\mathrm{L}},P_{\mathrm{R}}\text{.}$ A permutation $\pi$ of $n$-bit strings uses $O(n)$ uniformly controlled gates and $n$ ancillas returned to zero: gates controlled on $u$ write $\pi(u)$ on the ancillas, gates controlled on $v=\pi(u)$ add $\pi^{-1}(v)$ to the data register, which clears it, and CNOT gates swap the two registers. For $s=1$ this gives the transposition. For $s&gt;1\text{,}$ the permutation $u\mapsto u-(d-d^{\prime})\bmod 2^{n}$ moves the last $d^{\prime}$ coordinates of $\mathcal{H}_{d}$ to the first $d^{\prime}$ basis states. Then, controlled on the high $n-\log d^{\prime}$ bits being zero, one diagonal gate applies the signs and $\log d^{\prime}$ gates apply the Hadamard transform on the low bits, the signs first for $P_{\mathrm{L}}$ and the Hadamard transform first for $P_{\mathrm{R}}\text{.}$ The inverse permutation follows, and the result acts as the identity outside $\mathcal{H}_{d}\text{.}$ An adjoint reverses the gates and takes the adjoints of the parameters.</p>
</div>
<div id="S3.SS2.p11" class="ltx_para">
<p class="ltx_p">The gate lists depend only on $n$ and $d\text{,}$ and the parameters are determined by the selected pair of seeds or the selected row. This selection is a function of the outputs at precision $t_{0}$ alone. The seeds, their signs, the terms of $\widehat{G}_{22}$ and the products in $\operatorname{Tr}\widehat{\Theta}^{2\nu}$ are enumerated with polynomially many bits, so by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(iii) and (iv) the selection takes polynomial additional space.
∎</p>
</div>
</div>
<div id="S3.SS2.p12" class="ltx_para">
<p class="ltx_p">Because rounding down a number that is at least one loses at most a factor of two, and because $d^{\prime}&gt;d/2\text{,}$ <a href="#S3.E2" title="In 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.2)</span></a> gives $s\geq d/(2^{22}(n+1)^{2})$ in all cases. Each stage therefore multiplies the dimension by at most $1-1/(2^{22}(n+1)^{2})\text{,}$ and dimension one is reached in fewer than $J=2^{23}(n+1)^{3}$ stages, because $J$ such factors would reduce $2^{n}$ to at most $2^{n}e^{-2(n+1)}&lt;1\text{.}$</p>
</div>
</section>
<section id="S3.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="smaller-unitaries-and-two-near-isometries">
<span class="ltx_tag ltx_tag_subsection">3.3 </span>Smaller Unitaries and Two Near-Isometries</h3>

<div id="S3.SS3.p1" class="ltx_para">
<p class="ltx_p">Let $G$ be a unitary on $\mathcal{H}_{d}$ with blocks $G_{11},G_{12},G_{21},G_{22}$ for the split $d=k+s$ and with $\lVert G_{22}\rVert\leq\kappa\text{.}$ This bound lets us eliminate the trailing coordinates and still obtain a unitary. For a diagonal unitary $Z$ on the trailing coordinates, $I-G_{22}Z$ is invertible, and we put</p>
<table id="S3.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$X=(I-G_{22}Z)^{-1}G_{21},\qquad U^{(j+1)}=G_{11}+G_{12}ZX.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.4)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">To see that $U^{(j+1)}$ is a unitary on the leading coordinates, let $E_{\infty}=\binom{I}{ZX}\text{.}$ Since $(I-G_{22}Z)X=G_{21}\text{,}$ the lower block of $GE_{\infty}$ is $G_{21}+G_{22}ZX=X\text{,}$ so</p>
<table id="S3.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$GE_{\infty}=\binom{U^{(j+1)}}{X}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.5)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">As $G$ is unitary, $I+X^{\dagger}X=E_{\infty}^{\dagger}E_{\infty}=U^{(j+1)\dagger}U^{(j+1)}+X^{\dagger}X\text{,}$ and hence $U^{(j+1)\dagger}U^{(j+1)}=I\text{.}$</p>
</div>
<div id="S3.SS3.p2" class="ltx_para">
<p class="ltx_p">To relate $G$ to $U^{(j+1)}\text{,}$ let $X^{\prime}=XU^{(j+1)\dagger}$ and $E^{\prime}_{\infty}=\binom{I}{X^{\prime}}\text{,}$ so that $GE_{\infty}=E^{\prime}_{\infty}U^{(j+1)}\text{.}$ Taking adjoints and multiplying by $U^{(j+1)}$ on the left and by $G$ on the right gives</p>
<table id="S3.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$U^{(j+1)}E_{\infty}^{\dagger}=E_{\infty}^{\prime\dagger}G.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.6)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">This would express $G$ through $U^{(j+1)}$ if $E_{\infty}^{\dagger}$ and $E_{\infty}^{\prime\dagger}$ were isometries, but they map $d$ coordinates to $k&lt;d$ and so cannot be. To supply the missing dimensions, we let $Z$ depend on a control string $z$ and take a superposition over all control strings. For a suitable family of diagonal unitaries, averaging over the control strings cancels the cross terms between different degrees of the series, and the resulting maps are close to isometries.</p>
</div>
<div id="S3.SS3.p3" class="ltx_para">
<p class="ltx_p">Let $\omega=e^{2\pi\mathrm{i}/2^{\beta}}$ with $\beta$ as in <a href="#S3.Thmtheorem2" title="Definition 3.2. ‣ 3.1 Parameterized Circuits and the Recursion ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Definition</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>. Each trailing coordinate $\lambda$ has the frequency vector $v_{\lambda}=(1,\lambda,\dots,\lambda^{N})\text{,}$ and a control string $z\in\mathbb{Z}_{2^{\beta}}^{N+1}$ gives</p>
<table id="S3.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Z(z)=\operatorname{diag}\bigl(\omega^{v_{\lambda}\cdot z}\bigr)_{\lambda=1,\dots,s}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">We write $X(z)\text{,}$ $U^{(j+1)}(z)\text{,}$ $E_{\infty}(z)\text{,}$ $E^{\prime}_{\infty}(z)$ for the objects above at $Z=Z(z)\text{.}$ We truncate the Neumann series of $X(z)$ after $N$ terms, so that only paths of at most $N$ trailing coordinates occur in it:</p>
<table id="S3.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E_{N}(z)=\binom{I}{\sum_{h&lt;N}Z(z)(G_{22}Z(z))^{h}G_{21}},\qquad\lVert E_{\infty}(z)-E_{N}(z)\rVert\leq\frac{\kappa^{N}}{1-\kappa}=4\kappa^{N}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The truncation of $E^{\prime}_{\infty}(z)$ comes from the same formula applied to $G^{\dagger}\text{.}$ Indeed, the lower block of the identity $G^{\dagger}E^{\prime}_{\infty}=E_{\infty}U^{(j+1)\dagger}$ reads $G_{12}^{\dagger}+G_{22}^{\dagger}X^{\prime}=ZX^{\prime}\text{,}$ so $X^{\prime}=(I-Z^{\dagger}G_{22}^{\dagger})^{-1}Z^{\dagger}G_{12}^{\dagger}=Z^{\dagger}(I-G_{22}^{\dagger}Z^{\dagger})^{-1}G_{12}^{\dagger}\text{.}$ Since $Z(z)^{\dagger}=Z(-z)\text{,}$ this says that $E^{\prime}_{\infty}(z)$ is $E_{\infty}(-z)$ for the unitary $G^{\dagger}\text{,}$ whose trailing block also has norm at most $\kappa\text{.}$ We therefore let $E^{\prime}_{N}(z)$ be $E_{N}(-z)$ for $G^{\dagger}\text{,}$ and again $\lVert E^{\prime}_{\infty}(z)-E^{\prime}_{N}(z)\rVert\leq 4\kappa^{N}\text{.}$</p>
</div>
<div id="S3.SS3.p4" class="ltx_para">
<p class="ltx_p">The superpositions over control strings are the two maps of the recursion, from $\mathcal{H}_{d}$ to the control register and the leading coordinates:</p>
<table id="S3.E7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{E}_{N}=2^{-\beta(N+1)/2}\sum_{z}\lvert z\rangle\otimes E_{N}(z)^{\dagger},\qquad\mathcal{E}^{\prime}_{N}=2^{-\beta(N+1)/2}\sum_{z}\lvert z\rangle\otimes E^{\prime}_{N}(z)^{\dagger}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.7)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">By the definition of $E^{\prime}_{N}\text{,}$ the map $\mathcal{E}^{\prime}_{N}$ is $\mathcal{E}_{N}$ for $G^{\dagger}$ followed by the permutation $z\mapsto-z$ of the control register.</p>
</div>
<div id="S3.SS3.p5" class="ltx_para">
<p class="ltx_p">To implement these maps we need rows with few nonzero entries, and these appear in the Fourier basis $F_{2^{\beta}}^{\otimes(N+1)}\lvert\zeta\rangle=2^{-\beta(N+1)/2}\sum_{z}\omega^{\zeta\cdot z}\lvert z\rangle$ of the control register. There the maps have coefficient matrices $\Lambda_{\mathcal{E}},\Lambda_{\mathcal{E}^{\prime}}\text{,}$ defined by</p>
<table id="S3.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{E}_{N}=(F_{2^{\beta}}^{\otimes(N+1)}\otimes I)\Lambda_{\mathcal{E}},\qquad\mathcal{E}^{\prime}_{N}=(F_{2^{\beta}}^{\otimes(N+1)}\otimes I)\Lambda_{\mathcal{E}^{\prime}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">with rows indexed by a frequency $\zeta\in\mathbb{Z}_{2^{\beta}}^{N+1}$ and a leading coordinate $c\text{.}$ When the series is expanded, a path through the trailing coordinates contributes to one frequency only, plus or minus the sum of the frequency vectors along the path. The powers in $v_{\lambda}$ are chosen so that this sum determines the coordinates that the path visits. Thus the control register, introduced to supply the missing dimensions, also records the visited coordinates, and each row has few candidate columns. We call a matrix $\Lambda$ an $\varepsilon$-near-isometry if $(1-\varepsilon)I\preceq\Lambda^{\dagger}\Lambda\preceq I\text{.}$ A sparsity pattern of a matrix is a set of positions that contains all its nonzero entries and may contain others.</p>
</div>
<div id="S3.Thmtheorem5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.5</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $G$ be a unitary on $\mathcal{H}_{d}\text{,}$ $d\leq 2^{n}\text{,}$ with $\lVert G_{22}\rVert\leq\kappa\text{,}$ and let $N\geq 1\text{.}$ Then $\mathcal{E}_{N}$ and $\mathcal{E}^{\prime}_{N}$ are $\kappa^{2N}$-near-isometries, and</span></p>
<table id="S3.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Bigl\lVert\Bigl(\bigoplus_{z}U^{(j+1)}(z)\Bigr)\mathcal{E}_{N}-\mathcal{E}^{\prime}_{N}G\Bigr\rVert\leq 8\kappa^{N}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Each of $\Lambda_{\mathcal{E}},\Lambda_{\mathcal{E}^{\prime}}$ has a sparsity pattern of at most $N$ positions per row, which does not depend on $G$ and is computable from the row index in space polynomial in $n+N\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS3.p6" class="ltx_para">
<p class="ltx_p">For matrices $M(z)\text{,}$ the map $2^{-\beta(N+1)/2}\sum_{z}\lvert z\rangle\otimes M(z)$ has as its Gram matrix the average of $M(z)^{\dagger}M(z)\text{,}$ and therefore has norm at most $\max_{z}\lVert M(z)\rVert\text{.}$</p>
</div>
<div id="S3.SS3.p7" class="ltx_para">
<p class="ltx_p">Thus $\mathcal{E}_{N}^{\dagger}\mathcal{E}_{N}$ is the average over $z$ of $E_{N}(z)E_{N}(z)^{\dagger}\text{,}$ and averaging over a common phase cancels its cross terms. Every frequency vector has first coordinate one, so $Z(z)=\omega^{z_{0}}Z^{\prime}\text{,}$ where $Z^{\prime}$ depends only on $z_{1},\dots,z_{N}\text{.}$ With $R=Z^{\prime}G_{22}$ we have $Z^{\prime}(G_{22}Z^{\prime})^{h}=R^{h}Z^{\prime}\text{,}$ so the lower block of $E_{N}(z)$ is $\sum_{h&lt;N}\omega^{(h+1)z_{0}}R^{h}Z^{\prime}G_{21}\text{.}$ Fix $z_{1},\dots,z_{N}$ and average over $z_{0}\text{.}$ The average of $\omega^{hz_{0}}$ vanishes for $0&lt;\lvert h\rvert\leq N$ because $N&lt;2^{\beta}\text{,}$ so the off-diagonal blocks and all cross terms vanish, and the upper left block is $I\text{.}$ The identity $GG^{\dagger}=I$ gives $G_{21}G_{21}^{\dagger}=I-G_{22}G_{22}^{\dagger}\text{,}$ hence $(Z^{\prime}G_{21})(Z^{\prime}G_{21})^{\dagger}=I-RR^{\dagger}\text{,}$ and the lower right block telescopes:</p>
<table id="S3.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{h&lt;N}R^{h}(I-RR^{\dagger})R^{\dagger h}=I-R^{N}R^{\dagger N}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">As $\lVert R\rVert\leq\kappa\text{,}$ this lies between $(1-\kappa^{2N})I$ and $I\text{,}$ and averaging over $z_{1},\dots,z_{N}$ keeps these bounds. Thus $\mathcal{E}_{N}$ is a $\kappa^{2N}$-near-isometry, and so is $\mathcal{E}^{\prime}_{N}\text{,}$ which is $\mathcal{E}_{N}$ for $G^{\dagger}$ followed by a permutation.</p>
</div>
<div id="S3.SS3.p8" class="ltx_para">
<p class="ltx_p">The matrix in the second bound has the same form, and <a href="#S3.E6" title="In 3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.6)</span></a> turns its summands into tails:</p>
<table id="S3.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$M(z)=U^{(j+1)}(z)E_{N}(z)^{\dagger}-E^{\prime}_{N}(z)^{\dagger}G=U^{(j+1)}(z)(E_{N}(z)-E_{\infty}(z))^{\dagger}-(E^{\prime}_{N}(z)-E^{\prime}_{\infty}(z))^{\dagger}G.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Each tail has norm at most $4\kappa^{N}\text{,}$ so $\lVert M(z)\rVert\leq 8\kappa^{N}\text{.}$</p>
</div>
<div id="S3.SS3.p9" class="ltx_para">
<p class="ltx_p">For the sparsity, consider the columns of $E_{N}(z)^{\dagger}\text{.}$ The column of a leading coordinate is the corresponding basis vector and does not depend on $z\text{,}$ so in $\Lambda_{\mathcal{E}}$ it has its only nonzero entry, equal to one, at frequency $\zeta=0$ and the same leading coordinate. The column of a trailing coordinate $\lambda$ is column $\lambda$ of $\sum_{h&lt;N}G_{21}^{\dagger}(Z(z)^{\dagger}G_{22}^{\dagger})^{h}Z(z)^{\dagger}\text{.}$ Expanding over paths $\lambda_{1},\dots,\lambda_{\ell}$ with $\lambda_{\ell}=\lambda\text{,}$ the diagonal phases multiply to $\omega^{-(v_{\lambda_{1}}+\dots+v_{\lambda_{\ell}})\cdot z}\text{,}$ so the entry of $\Lambda_{\mathcal{E}}$ in row $(\zeta,c)$ and the column of $\lambda$ is</p>
<table id="S3.E8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sum_{\ell=1}^{N}\ \sum_{\lambda_{1},\dots,\lambda_{\ell-1}}\mathbf{1}\Bigl[\zeta=-\sum_{i\leq\ell}v_{\lambda_{i}}\Bigr]\ \overline{(G_{21})_{\lambda_{1},c}}\prod_{i&lt;\ell}\overline{(G_{22})_{\lambda_{i+1},\lambda_{i}}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.8)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">where the equality of frequencies is in $\mathbb{Z}_{2^{\beta}}^{N+1}\text{.}$</p>
</div>
<div id="S3.SS3.p10" class="ltx_para">
<p class="ltx_p">Suppose that this entry is nonzero. Then $-\zeta$ is a sum of $\ell\leq N$ vectors $v_{\lambda_{i}}\text{,}$ one of them $v_{\lambda}\text{.}$ Each coordinate of the sum is an integer at most $N2^{nN}&lt;2^{\beta}\text{,}$ so the sum is the representative of $-\zeta$ in $\{0,\dots,2^{\beta}-1\}^{N+1}\text{.}$ Its first coordinate is $\ell\text{,}$ and its next $\ell$ coordinates are the power sums of $\lambda_{1},\dots,\lambda_{\ell}\text{,}$ which determine the multiset $\{\lambda_{1},\dots,\lambda_{\ell}\}$ by Newton’s identities <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx40" title="" class="ltx_ref">Mac95</a>, Chapter I, Section 2]</cite>. Hence $\zeta$ determines a set of at most $\ell\leq N$ candidates for $\lambda\text{,}$ which are found by enumerating nondecreasing tuples and comparing power sums, in space polynomial in $n+N\text{.}$ Moreover $1\leq\ell\leq N&lt;2^{\beta}\text{,}$ so $\zeta\neq 0$ for every nonzero entry in a trailing column. Hence a row $(0,c)$ has only the entry in the column of $c\text{,}$ and a row with $\zeta\neq 0$ has no nonzero entry in a leading column, which gives the pattern of $\Lambda_{\mathcal{E}}\text{.}$</p>
</div>
<div id="S3.SS3.p11" class="ltx_para">
<p class="ltx_p">The permutation $z\mapsto-z$ sends $F_{2^{\beta}}^{\otimes(N+1)}\lvert\zeta\rangle$ to $F_{2^{\beta}}^{\otimes(N+1)}\lvert-\zeta\rangle\text{.}$ Therefore the row $(\zeta,c)$ of $\Lambda_{\mathcal{E}^{\prime}}$ is the row $(-\zeta,c)$ of $\Lambda_{\mathcal{E}}$ for $G^{\dagger}\text{,}$ and the pattern of $\Lambda_{\mathcal{E}^{\prime}}$ follows.
∎</p>
</div>
</div>
</section>
<section id="S3.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="implementing-a-row-sparse-near-isometry">
<span class="ltx_tag ltx_tag_subsection">3.4 </span>Implementing a Row-Sparse Near-Isometry</h3>

<div id="S3.SS4.p1" class="ltx_para">
<p class="ltx_p">To apply a matrix $\Lambda$ to $\lvert v\rangle\text{,}$ we can prepare its column, but $v$ then remains in a register. To remove it, we apply, controlled on the row $u\text{,}$ the inverse preparation of the uniform superposition over the set $I_{u}$ of positions of that row. This gives each $v\in I_{u}$ amplitude $\lvert I_{u}\rvert^{-1/2}$ at zero, and a flag rotation, also controlled on the row, compensates for this factor, so that every entry of $\Lambda$ appears with the same factor. Thus $\Lambda$ is a block of a circuit, up to an inverse-polynomial factor. We choose this factor so that $N$ iterations of amplitude amplification raise it to one on a singular vector with singular value one, and since all singular values of $\Lambda$ are close to one, the iterations give $\Lambda$ up to a small error. These two steps adapt the sparse-access block encoding <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx26" title="" class="ltx_ref">GSLW19</a>, Lemma 48]</cite>, which assumes row and column access, and oblivious amplitude amplification <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx7" title="" class="ltx_ref">BCC<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>14</a>, Lemma 3.6]</cite>, which is stated for a unitary.</p>
</div>
<div id="S3.SS4.p2" class="ltx_para">
<p class="ltx_p">The columns and the superpositions are prepared with uniformly controlled gates, as in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx24" title="" class="ltx_ref">GR02</a>]</cite>. For a unit vector $\sum_{u}a_{u}\lvert u\rangle$ on $\ell$ qubits, the prefix probability of a bit string $y$ is $\mu(y)=\sum_{u}\lvert a_{u}\rvert^{2}$ over the strings $u$ that extend $y\text{.}$ Processing the qubits in order, at prefix $y$ we apply to the next qubit the rotation</p>
<table id="S3.E9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\begin{pmatrix}\sqrt{\mu(y0)/\mu(y)}&amp;-\sqrt{\mu(y1)/\mu(y)}\\ \sqrt{\mu(y1)/\mu(y)}&amp;\sqrt{\mu(y0)/\mu(y)}\end{pmatrix}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.9)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">if $\mu(y)&gt;0$ and the identity otherwise, so that by induction the amplitude at each prefix $y$ is $\sqrt{\mu(y)}\text{.}$ A final diagonal gate applies the phases $a_{u}/\lvert a_{u}\rvert\text{,}$ taken to be one when $a_{u}=0\text{.}$ This prepares the vector exactly from $\lvert 0^{\ell}\rangle$ with $\ell+1$ uniformly controlled gates.</p>
</div>
<div id="S3.Thmtheorem6" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.6</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $\Lambda$ be a matrix with columns indexed by $v&lt;d\text{,}$ where $d\leq 2^{n}\text{,}$ and rows indexed by $u&lt;2^{w}\text{.}$ Suppose that $\Lambda$ is an $\varepsilon$-near-isometry with $0\leq\varepsilon&lt;1$ and has a sparsity pattern of at most $N$ positions per row. Consider an index register of $n$ qubits, a row register of $w$ qubits and two flag qubits, with the embeddings</span></p>
<table id="S3.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\iota_{\mathrm{in}}\lvert v\rangle=\lvert v\rangle\lvert 0^{w}\rangle\lvert 0\rangle\lvert 0\rangle,\qquad\iota_{\mathrm{out}}\lvert u\rangle=\lvert 0^{n}\rangle\lvert u\rangle\lvert 1\rangle\lvert 1\rangle.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p"><span class="ltx_text ltx_font_italic">There is a parameterized circuit $C_{\Lambda}$ on these registers such that</span></p>
<table id="S3.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert C_{\Lambda}\iota_{\mathrm{in}}-\iota_{\mathrm{out}}\Lambda\rVert\leq 5\varepsilon.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p"><span class="ltx_text ltx_font_italic">It has $O(N(n+w))$ uniformly controlled gates, its gate list depends only on $n,w,N\text{,}$ and its parameters are determined by $\Lambda$ and the pattern, as given in <a href="#S3.E10" title="In 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">(3.10)</span></a> and <a href="#S3.E11" title="Equation 3.11 ‣ 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">(3.11)</span></a>.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS4.p3" class="ltx_para">
<p class="ltx_p">Let $\theta=\pi/(4N+2)\text{,}$ so that $(2N+1)\theta=\pi/2\text{.}$ We first build a unitary $C^{(0)}_{\Lambda}$ whose block between the two embeddings is $\sin\theta\cdot\Lambda\text{.}$ For $v&lt;d\text{,}$ let $C_{v}$ be the preparation on the row register and the first flag with</p>
<table id="S3.E10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C_{v}\lvert 0^{w}\rangle\lvert 0\rangle=\sum_{u}\Lambda_{uv}\lvert u\rangle\lvert 1\rangle+\sqrt{1-\lVert\Lambda\lvert v\rangle\rVert^{2}}\,\lvert 0^{w}\rangle\lvert 0\rangle,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.10)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">and let $C_{v}=I$ for $v\geq d\text{.}$ For a row $u\text{,}$ let $I_{u}$ be its set of positions in the pattern, let $C^{\prime}_{u}$ be the preparation on the index register with</p>
<table id="S3.E11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C^{\prime}_{u}\lvert 0^{n}\rangle=\lvert I_{u}\rvert^{-1/2}\sum_{i\in I_{u}}\lvert i\rangle,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.11)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">and let $C^{\prime}_{u}=I$ if $I_{u}$ is empty. Let $W_{\theta}=\bigoplus_{u}W_{\theta,u}$ be the uniformly controlled gate with the row register as its control and the second flag as its target, where $W_{\theta,u}\lvert 0\rangle=\sqrt{1-\lvert I_{u}\rvert\sin^{2}\theta}\,\lvert 0\rangle+\sqrt{\lvert I_{u}\rvert}\sin\theta\,\lvert 1\rangle\text{.}$ This rotation exists because $\lvert I_{u}\rvert\leq N$ and $\sqrt{N}\sin\theta\leq\sqrt{N}\theta\leq 1\text{.}$ Put</p>
<table id="S3.Ex15" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C^{(0)}_{\Lambda}=W_{\theta}\Bigl(\sum_{u}\lvert u\rangle\langle u\rvert\otimes C_{u}^{\prime\dagger}\Bigr)\Bigl(\sum_{v}\lvert v\rangle\langle v\rvert\otimes C_{v}\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where the preparations $C_{v}$ are controlled on the index register and the preparations $C_{u}^{\prime\dagger}$ on the row register. Apply this to $\iota_{\mathrm{in}}\lvert v\rangle\text{.}$ The term of <a href="#S3.E10" title="In 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.10)</span></a> with first flag zero stays orthogonal to the range of $\iota_{\mathrm{out}}\text{.}$ On a term $\Lambda_{uv}\lvert u\rangle\lvert 1\rangle$ with $\Lambda_{uv}\neq 0$ we have $v\in I_{u}\text{,}$ so the amplitude of zero on the index register is $\overline{\langle v\rvert C^{\prime}_{u}\lvert 0^{n}\rangle}=\lvert I_{u}\rvert^{-1/2}\text{,}$ and the second flag contributes $\sqrt{\lvert I_{u}\rvert}\sin\theta\text{.}$ Hence</p>
<table id="S3.E12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\iota_{\mathrm{out}}^{\dagger}C^{(0)}_{\Lambda}\iota_{\mathrm{in}}=\sin\theta\cdot\Lambda.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.12)</span></td>
</tr></tbody>
</table>
</div>
<div id="S3.SS4.p4" class="ltx_para">
<p class="ltx_p">To raise the factor $\sin\theta$ to nearly one, let $\Pi_{\mathrm{in}}=\iota_{\mathrm{in}}\iota_{\mathrm{in}}^{\dagger}$ and $\Pi_{\mathrm{out}}=\iota_{\mathrm{out}}\iota_{\mathrm{out}}^{\dagger}\text{,}$ and let</p>
<table id="S3.Ex16" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C_{\Lambda}=\Bigl(\bigl(2C^{(0)}_{\Lambda}\Pi_{\mathrm{in}}C_{\Lambda}^{(0)\dagger}-I\bigr)\bigl(I-2\Pi_{\mathrm{out}}\bigr)\Bigr)^{N}C^{(0)}_{\Lambda}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">This circuit acts separately on each singular vector of $\Lambda\text{.}$ Take a singular value decomposition $\Lambda\lvert v_{i}\rangle=\sigma_{i}\lvert e_{i}\rangle\text{,}$ with $\{\lvert v_{i}\rangle\}$ an orthonormal basis of $\mathbb{C}^{d}\text{,}$ $\{\lvert e_{i}\rangle\}$ orthonormal and $\sqrt{1-\varepsilon}\leq\sigma_{i}\leq 1\text{,}$ and identify vectors with their embeddings. By <a href="#S3.E12" title="In 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.12)</span></a>,</p>
<table id="S3.Ex17" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C^{(0)}_{\Lambda}\lvert v_{i}\rangle=\sin\alpha_{i}\lvert e_{i}\rangle+\cos\alpha_{i}\lvert e^{\prime}_{i}\rangle,\qquad\alpha_{i}=\arcsin(\sin\theta\cdot\sigma_{i}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">with $\lvert e^{\prime}_{i}\rangle$ a unit vector orthogonal to the range of $\iota_{\mathrm{out}}\text{.}$ Since $C^{(0)}_{\Lambda}$ is unitary and $\cos\alpha_{i}&gt;0\text{,}$ the $\lvert e^{\prime}_{i}\rangle$ are orthonormal, so the planes spanned by $\lvert e_{i}\rangle,\lvert e^{\prime}_{i}\rangle$ are mutually orthogonal, and the range of $C^{(0)}_{\Lambda}\Pi_{\mathrm{in}}$ is spanned by one vector in each plane. Both reflections therefore preserve each plane. On the plane of $i\text{,}$ write a unit vector as $\sin\gamma\lvert e_{i}\rangle+\cos\gamma\lvert e^{\prime}_{i}\rangle\text{.}$ Then $I-2\Pi_{\mathrm{out}}$ maps $\gamma$ to $-\gamma\text{,}$ and the other reflection, which fixes $C^{(0)}_{\Lambda}\lvert v_{i}\rangle$ and negates the vector of the plane orthogonal to it, maps $\gamma$ to $2\alpha_{i}-\gamma\text{,}$ so one iteration maps $\gamma$ to $\gamma+2\alpha_{i}\text{.}$ After $N$ iterations, $C_{\Lambda}\lvert v_{i}\rangle$ has angle $(2N+1)\alpha_{i}\text{.}$</p>
</div>
<div id="S3.SS4.p5" class="ltx_para">
<p class="ltx_p">Since $\sigma_{i}\leq 1\text{,}$ we have $\alpha_{i}\leq\theta$ and $(2N+1)\alpha_{i}\leq(2N+1)\theta=\pi/2\text{.}$ Thus $C_{\Lambda}\lvert v_{i}\rangle$ is within arc length $(2N+1)(\theta-\alpha_{i})$ of $\lvert e_{i}\rangle\text{,}$ hence within $(2N+1)(\theta-\alpha_{i})+1-\sigma_{i}$ of $\sigma_{i}\lvert e_{i}\rangle\text{.}$ On $[0,\sin\theta]\text{,}$ a subset of $[0,1/2]\text{,}$ the derivative of $\arcsin$ is at most $2\text{,}$ so $\theta-\alpha_{i}\leq 2\sin\theta(1-\sigma_{i})\leq 2\theta(1-\sigma_{i})\text{,}$ and therefore</p>
<table id="S3.Ex18" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert C_{\Lambda}\lvert v_{i}\rangle-\sigma_{i}\lvert e_{i}\rangle\rVert\leq(\pi+1)(1-\sigma_{i})\leq 5\varepsilon,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">using $1-\sigma_{i}\leq 1-\sqrt{1-\varepsilon}\leq\varepsilon\text{.}$ These error vectors lie in mutually orthogonal planes, so the bound holds for every superposition of the $\lvert v_{i}\rangle\text{.}$</p>
</div>
<div id="S3.SS4.p6" class="ltx_para">
<p class="ltx_p">Each preparation uses one gate per qubit and one diagonal gate, so $C^{(0)}_{\Lambda}$ uses $O(n+w)$ gates. Since $2C^{(0)}_{\Lambda}\Pi_{\mathrm{in}}C_{\Lambda}^{(0)\dagger}-I=C^{(0)}_{\Lambda}(2\Pi_{\mathrm{in}}-I)C_{\Lambda}^{(0)\dagger}\text{,}$ the circuit $C_{\Lambda}$ has $2N+1$ occurrences of $C^{(0)}_{\Lambda}$ or its adjoint and $2N$ diagonal reflections.
∎</p>
</div>
</div>
</section>
<section id="S3.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-recursive-circuit">
<span class="ltx_tag ltx_tag_subsection">3.5 </span>The Recursive Circuit</h3>

<div id="S3.SS5.p1" class="ltx_para">
<p class="ltx_p">The parameters of <a href="#S3.Thmtheorem6" title="Lemma 3.6. ‣ 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.6</span></a> are discontinuous functions of $\Lambda\text{,}$ since the rotation of <a href="#S3.E9" title="In 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.9)</span></a> changes form when a prefix probability vanishes. To compute them in <a href="#S4" title="4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a> we need exact zero tests, so we apply the lemma to rounded coefficient matrices, whose prefix probabilities are exact rational numbers.</p>
</div>
<div id="S3.SS5.p2" class="ltx_para">
<p class="ltx_p">Let $\delta$ be the largest power of two with $\delta\leq 2^{-m}/(4096J)\text{,}$ let $N=4\log(1/\delta)\text{,}$ and let $\beta$ be as in <a href="#S3.Thmtheorem2" title="Definition 3.2. ‣ 3.1 Parameterized Circuits and the Recursion ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Definition</span> <span class="ltx_text ltx_ref_tag">3.2</span></a>, the same at every stage. Then $\kappa^{N}&lt;\delta\text{,}$ because $\kappa^{4}&lt;1/2\text{.}$ The row register of <a href="#S3.Thmtheorem6" title="Lemma 3.6. ‣ 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.6</span></a> has $w=\beta(N+1)+n$ qubits and holds a frequency and an $n$-qubit basis state, and rows whose basis state is not a leading coordinate are zero. Let $\Lambda$ be $\Lambda_{\mathcal{E}}$ or $\Lambda_{\mathcal{E}^{\prime}}$ and let $t_{\Lambda}=\log(1/\delta)+n+w+4\text{.}$ Round each entry in the sparsity pattern to the $2^{-t_{\Lambda}}$ grid, set the other entries to zero, and let $\widehat{\Lambda}$ be the result divided by $1+\delta\text{.}$ There are at most $2^{n+w}$ entries, so the rounded matrix differs from $\Lambda$ by at most $2^{(n+w)/2-t_{\Lambda}}\leq\delta$ in Frobenius norm. Dividing by $1+\delta$ makes it a contraction, $\lVert\widehat{\Lambda}\rVert\leq 1\text{,}$ at the cost of $\lVert\widehat{\Lambda}-\Lambda\rVert\leq 2\delta\text{.}$ For a unit vector $\lvert\psi\rangle\text{,}$</p>
<table id="S3.Ex19" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\bigl\lvert\lVert\widehat{\Lambda}\lvert\psi\rangle\rVert^{2}-\lVert\Lambda\lvert\psi\rangle\rVert^{2}\bigr\rvert\leq\lVert(\widehat{\Lambda}-\Lambda)\lvert\psi\rangle\rVert\bigl(\lVert\widehat{\Lambda}\lvert\psi\rangle\rVert+\lVert\Lambda\lvert\psi\rangle\rVert\bigr)\leq 4\delta,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">so by <a href="#S3.Thmtheorem5" title="Lemma 3.5. ‣ 3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.5</span></a> the matrix $\widehat{\Lambda}$ is a $(\kappa^{2N}+4\delta)$-near-isometry with the same pattern.</p>
</div>
<div id="S3.SS5.p3" class="ltx_para">
<p class="ltx_p">The two circuits of a stage are $C_{\mathcal{E},j}=(F_{2^{\beta}}^{\otimes(N+1)}\otimes I)C_{\widehat{\Lambda}_{\mathcal{E}}}$ and $C_{\mathcal{E}^{\prime},j}=(F_{2^{\beta}}^{\otimes(N+1)}\otimes I)C_{\widehat{\Lambda}_{\mathcal{E}^{\prime}}}\text{,}$ where the Fourier transforms act on the frequency part of the row register, which is then the control register. Since these transforms commute with $\iota_{\mathrm{out}}\text{,}$ <a href="#S3.Thmtheorem6" title="Lemma 3.6. ‣ 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.6</span></a> with $\varepsilon=\kappa^{2N}+4\delta&lt;1$ gives $\lVert C_{\mathcal{E},j}\iota_{\mathrm{in}}-\iota_{\mathrm{out}}\mathcal{E}_{N}\rVert\leq 5\varepsilon+2\delta=5\kappa^{2N}+22\delta\text{,}$ and the same for $C_{\mathcal{E}^{\prime},j}$ and $\mathcal{E}^{\prime}_{N}\text{.}$ After $C_{\mathcal{E},j}\text{,}$ the last $n$ qubits of the row register are the data register of the next stage.</p>
</div>
<div id="S3.Thmtheorem7" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.7</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem7.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $U^{(j)}$ be a unitary of stage $j\text{,}$ on $\mathcal{H}_{d}$ with $d\geq 2\text{,}$ let $P_{\mathrm{L}},P_{\mathrm{R}}$ be as in <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>, and let $G=P_{\mathrm{L}}U^{(j)}P_{\mathrm{R}}\text{.}$ Let $C_{j+1}$ be a unitary circuit that acts only on the control register, the data register of the next stage and its own ancillas, and that implements $\bigoplus_{z}U^{(j+1)}(z)$ on the zero-ancilla subspace with error $\varepsilon_{j+1}\text{.}$ Then the circuit $C_{j}$ of <a href="#S3.E1" title="In 3.1 Parameterized Circuits and the Recursion ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.1)</span></a> implements $U^{(j)}$ on the zero-ancilla subspace with error at most $\varepsilon_{j+1}+18\kappa^{N}+44\delta\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS5.p4" class="ltx_para">
<p class="ltx_p">Let $W=\bigoplus_{z}U^{(j+1)}(z)\text{,}$ and let $\iota_{\mathrm{in}},\iota_{\mathrm{out}}$ also set the ancillas of $C_{j+1}$ to zero. Since $C_{j+1}$ acts as the identity on the index register and the flags, the bound $\lVert C_{j+1}\iota_{\mathrm{out}}-\iota_{\mathrm{out}}W\rVert\leq\varepsilon_{j+1}$ holds on the control register and the leading coordinates, which contain the range of $\mathcal{E}_{N}\text{.}$ Inserting $\iota_{\mathrm{out}}\mathcal{E}_{N}$ and $\iota_{\mathrm{out}}\mathcal{E}^{\prime}_{N}\text{,}$</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="Sx1.EGx3"></span><span class="paper-eq-anchor" id="S3.Ex20"></span><span class="paper-eq-anchor" id="S3.Ex21"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\lVert C_{j+1}C_{\mathcal{E},j}\iota_{\mathrm{in}}-C_{\mathcal{E}^{\prime},j}\iota_{\mathrm{in}}G\rVert &amp; \displaystyle\leq\lVert C_{j+1}(C_{\mathcal{E},j}\iota_{\mathrm{in}}-\iota_{\mathrm{out}}\mathcal{E}_{N})\rVert+\lVert(C_{j+1}\iota_{\mathrm{out}}-\iota_{\mathrm{out}}W)\mathcal{E}_{N}\rVert \\
 &amp; \displaystyle\quad+\lVert\iota_{\mathrm{out}}(W\mathcal{E}_{N}-\mathcal{E}^{\prime}_{N}G)\rVert+\lVert(\iota_{\mathrm{out}}\mathcal{E}^{\prime}_{N}-C_{\mathcal{E}^{\prime},j}\iota_{\mathrm{in}})G\rVert.
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p class="ltx_p">The first and last terms are bounded by the estimate before the lemma, the second by $\varepsilon_{j+1}$ since $\lVert\mathcal{E}_{N}\rVert\leq 1\text{,}$ and the third by $8\kappa^{N}$ by <a href="#S3.Thmtheorem5" title="Lemma 3.5. ‣ 3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.5</span></a>. Their sum is at most $\varepsilon_{j+1}+8\kappa^{N}+10\kappa^{2N}+44\delta\leq\varepsilon_{j+1}+18\kappa^{N}+44\delta\text{.}$ The circuits of $P_{\mathrm{L}}^{\dagger},P_{\mathrm{R}}^{\dagger}$ are exact on zero ancillas and preserve $\mathcal{H}_{d}\text{,}$ and $U^{(j)}=P_{\mathrm{L}}^{\dagger}GP_{\mathrm{R}}^{\dagger}\text{,}$ so</p>
<table id="S3.Ex22" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C_{j}\iota-\iota U^{(j)}=P_{\mathrm{L}}^{\dagger}\bigl(C_{\mathcal{E}^{\prime},j}^{\dagger}C_{j+1}C_{\mathcal{E},j}\iota_{\mathrm{in}}-\iota_{\mathrm{in}}G\bigr)P_{\mathrm{R}}^{\dagger},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where $\iota$ sets all ancillas of $C_{j}$ to zero. The norm of this difference is the norm just bounded.
∎</p>
</div>
</div>
<div id="S3.SS5.p5" class="ltx_para">
<p class="ltx_p">The recursion ends at dimension one, where one diagonal gate on the data register, controlled on all control registers, applies the phase exactly. <a href="#S3.Thmtheorem7" title="Lemma 3.7. ‣ 3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.7</span></a> holds for each fixed $z_{&lt;j}\text{,}$ so it holds for the direct sum over $z_{&lt;j}$ with the same error, by adding $z_{&lt;j}$ to the controls as in <a href="#S3.SS1" title="3.1 Parameterized Circuits and the Recursion ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>. Induction from the last stage gives, with fewer than $J$ stages and $\kappa^{N}&lt;\delta\leq 2^{-m}/(4096J)\text{,}$</p>
<table id="S3.E13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\varepsilon_{0}\leq J(18\kappa^{N}+44\delta)&lt;2^{-m}/64.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3.13)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">The precision $m$ enters only through $\log(1/\delta)\text{,}$ which is linear in $m+\log n\text{,}$ so exponential precision needs no error reduction. Nothing in the gate list of $C_{0}$ depends on $U_{n}\text{,}$ so it can be written from the sizes alone.</p>
</div>
<div id="S3.Thmtheorem8" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.8</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem8.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">There is a polynomial-time algorithm, which does not depend on $A$ or $U\text{,}$ that on input $(1^{n},1^{m})$ outputs the registers, gate order and control lists of the parameterized circuit $C_{0}\text{.}$ The circuit has $S=\operatorname{poly}(n+m)$ uniformly controlled gates and width $w^{\prime}=\operatorname{poly}(n+m)\text{.}$ For each gate, the algorithm also records its stage, the component it belongs to ($P_{\mathrm{L}}\text{,}$ $P_{\mathrm{R}}\text{,}$ the circuit for $\widehat{\Lambda}_{\mathcal{E}}$ or $\widehat{\Lambda}_{\mathcal{E}^{\prime}}\text{,}$ a Fourier transform, or the gate at dimension one), its position in that component, and whether the component occurs as an adjoint.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS5.p6" class="ltx_para">
<p class="ltx_p">The sizes $d_{j},s_{j},k_{j}$ are computed from $n$ by <a href="#S3.E2" title="In 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.2)</span></a>, and $\delta,N,\beta,w$ from $(n,m)\text{.}$ The gate lists of <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemmas</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> and <a href="#S3.Thmtheorem6" title="Lemma 3.6. ‣ 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3.6</span></a> depend only on these sizes, and the sparsity patterns enter only through the parameters. The transform $F_{2^{\beta}}$ uses $O(\beta)$ gates, because in the textbook circuit <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx42" title="" class="ltx_ref">NC10</a>, Section 5.1]</cite> the controlled rotations on one target commute and merge into one diagonal uniformly controlled gate. Each stage contains exactly one recursive call, so gate counts and widths add over fewer than $J$ stages, and the gates of stage $j$ have $j\beta(N+1)$ further control qubits. All these numbers are polynomial in $n+m\text{.}$
∎</p>
</div>
</div>
</section>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="computing-the-parameters">
<span class="ltx_tag ltx_tag_section">4 </span>Computing the Parameters</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">Let $A$ and $U$ be as in <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>. With its exact parameters, the circuit $C_{0}$ of <a href="#S3.Thmtheorem8" title="Lemma 3.8. ‣ 3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.8</span></a> implements $U_{n}$ with error below $2^{-m}/64\text{.}$ To prove the theorem, it therefore remains to compute these parameters in polynomial space and to encode them in one language. The parameters are functions of the unitaries $U^{(j)}\text{,}$ and $U^{(j+1)}$ is defined from $U^{(j)}\text{,}$ so computing an entry of $U^{(j+1)}$ requires entries of $U^{(j)}\text{,}$ and so on down to stage zero. If an entry of $U^{(j+1)}$ at precision $t$ needed entries of $U^{(j)}$ at precision $ct$ for a constant $c&gt;1\text{,}$ the precision at stage zero would be exponential in $J\text{.}$ We show that precision $t+O(n)$ suffices. The truncated series for the inverse in <a href="#S3.E4" title="In 3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.4)</span></a> has exponentially many paths, and bounding the error of each path separately would need entries of $U^{(j)}$ at a precision of order $nt\text{.}$ We instead round the matrices before expanding the series and multiply the rounded numbers exactly, so the length of the series does not enter the precision.</p>
</div>
<section id="S4.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-parameters-in-polynomial-space">
<span class="ltx_tag ltx_tag_subsection">4.1 </span>The Parameters in Polynomial Space</h3>

<div id="S4.SS1.p1" class="ltx_para">
<p class="ltx_p">Fix $n$ and $m\text{.}$ In <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>, $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ are selected from the entries of $U^{(j)}$ computed to precision $t_{0}\text{,}$ so the unitaries $U^{(j+1)}(z)$ depend on the algorithm that computes these entries and not only on $U^{(j)}\text{.}$ We therefore define the unitaries and the algorithms together, by induction on $j\text{.}$ For $j=0$ they are $U_{n}$ and the given entry algorithm. Given a deterministic algorithm for the entries of $U^{(j)}$ and fixed earlier control strings $z_{&lt;j}\text{,}$ the outputs of this algorithm at precision $t_{0}$ determine $P_{\mathrm{L}}\text{,}$ $P_{\mathrm{R}}$ and $G\text{,}$ and <a href="#S3.E4" title="In 3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.4)</span></a> defines $U^{(j+1)}(z)\text{.}$ The algorithm for the entries of $U^{(j+1)}(z)$ is the one in the proof below. It uses entries of $U^{(j)}$ at other precisions, but $U^{(j+1)}(z)$ does not depend on them.</p>
</div>
<div id="S4.SS1.p2" class="ltx_para">
<p class="ltx_p">The unitaries $U^{(j)}$ determine the parameters of $C_{0}\text{.}$ We number the uniformly controlled gates of $C_{0}$ by $i\in[S]$ and write the $i$-th gate as $W_{i}=\bigoplus_{y}W_{i,y}\text{.}$</p>
</div>
<div id="S4.Thmtheorem1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">There are deterministic algorithms with oracle $A$ that use space polynomial in $n+m+t$ and, on input $1^{n},1^{m},1^{t}$ and the following data, compute to precision $t\text{:}$</span></p>
<ol id="S4.I1" class="ltx_enumerate">
<li id="S4.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(i)</span> 
<div id="S4.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">the entry </span>$\langle u\rvert U^{(j)}(z_{&lt;j})\lvert v\rangle$<span class="ltx_text ltx_font_italic">, given </span>$j,z_{&lt;j},u,v$<span class="ltx_text ltx_font_italic">;</span></p>
</div>
</li>
<li id="S4.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(ii)</span> 
<div id="S4.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">each entry of the parameter </span>$W_{i,y}$<span class="ltx_text ltx_font_italic">, given </span>$i,y$<span class="ltx_text ltx_font_italic"> and the two basis indices.</span></p>
</div>
</li>
</ol>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS1.p3" class="ltx_para">
<p class="ltx_p">For item (i), we compute an entry of $U^{(j+1)}(z)$ to precision $t$ from entries of $U^{(j)}\text{,}$ with $z_{&lt;j}$ fixed, and write $U^{(j)}$ for $U^{(j)}(z_{&lt;j})\text{.}$ Let $Z=Z(z)$ and $G^{\prime}=G\operatorname{diag}(I,Z)\text{.}$ In the blocks of $G^{\prime}\text{,}$ <a href="#S3.E4" title="In 3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.4)</span></a> reads</p>
<table id="S4.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$X=(I-G^{\prime}_{22})^{-1}G^{\prime}_{21},\qquad U^{(j+1)}(z)=G^{\prime}_{11}+G^{\prime}_{12}X.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">An entry of $G=P_{\mathrm{L}}U^{(j)}P_{\mathrm{R}}$ or of $G^{\prime}$ is a sum of at most $2^{2n}$ products of an entry of $U^{(j)}$ with at most two entries of $P_{\mathrm{L}},P_{\mathrm{R}}$ and at most one entry of $Z\text{.}$ All these factors have modulus at most one, and those of $P_{\mathrm{L}},P_{\mathrm{R}},Z$ are computed by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(ii). Hence, if all factors are computed to precision $t^{\prime}+2n+3\text{,}$ then the exact sum of the products is within $2^{-t^{\prime}}$ of the entry.</p>
</div>
<div id="S4.SS1.p4" class="ltx_para">
<p class="ltx_p">Let $t_{1}=t+n+10\text{,}$ and let $\widehat{G}^{\prime}$ be $G^{\prime}$ with its entries rounded to the $2^{-t_{1}}$ grid. The blocks have dimensions at most $2^{n}\text{,}$ so each block of $\widehat{G}^{\prime}$ is within $\varepsilon=2^{-t-10}$ of the exact block in operator norm, and $\lVert\widehat{G}^{\prime}_{22}\rVert&lt;4/5$ because $\lVert G^{\prime}_{22}\rVert\leq\kappa\text{.}$ Let $N^{\prime}=4(t+10)$ and $\widehat{X}=\sum_{h&lt;N^{\prime}}(\widehat{G}^{\prime}_{22})^{h}\widehat{G}^{\prime}_{21}\text{,}$ so that $\lVert\widehat{X}\rVert\leq 6\text{.}$ Since $(I-\widehat{G}^{\prime}_{22})\widehat{X}=\widehat{G}^{\prime}_{21}-(\widehat{G}^{\prime}_{22})^{N^{\prime}}\widehat{G}^{\prime}_{21}$ and $(4/5)^{N^{\prime}}&lt;\varepsilon\text{,}$</p>
<table id="S4.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert(I-G^{\prime}_{22})\widehat{X}-G^{\prime}_{21}\rVert\leq\varepsilon\lVert\widehat{X}\rVert+\varepsilon+(4/5)^{N^{\prime}}(1+\varepsilon)\leq 9\varepsilon.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">As $\lVert(I-G^{\prime}_{22})^{-1}\rVert\leq 4\text{,}$ this gives $\lVert\widehat{X}-X\rVert\leq 36\varepsilon\text{,}$ and therefore</p>
<table id="S4.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert\widehat{G}^{\prime}_{11}+\widehat{G}^{\prime}_{12}\widehat{X}-U^{(j+1)}(z)\rVert\leq\varepsilon+6\varepsilon+36\varepsilon=43\varepsilon.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The output of the algorithm is the required entry of $\widehat{G}^{\prime}_{11}+\widehat{G}^{\prime}_{12}\widehat{X}\text{,}$ rounded to the $2^{-t-4}$ grid. Its error is at most $43\varepsilon+\sqrt{2}\,2^{-t-5}&lt;2^{-t}\text{,}$ and it has $O(t+1)$ bits per component.</p>
</div>
<div id="S4.SS1.p5" class="ltx_para">
<p class="ltx_p">The entry of $\widehat{G}^{\prime}_{11}+\widehat{G}^{\prime}_{12}\widehat{X}$ is a sum, over paths through at most $N^{\prime}$ trailing coordinates, of products of at most $N^{\prime}+1$ rounded numbers. These products are exact, so $N^{\prime}$ does not enter the precision at which entries of $U^{(j)}$ are needed. Rounding to the $2^{-t_{1}}$ grid needs entries of $G^{\prime}$ at precision $t_{1}+4\text{,}$ hence entries of $U^{(j)}$ at precision $t+3n+17\text{.}$ By <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>, $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ need entries of $U^{(j)}$ at precision $t_{0}$ only. So computing an entry of $U^{(j+1)}(z)$ to precision $t$ requires entries of $U^{(j)}$ at precision at most $\max\{t+3n+17,t_{0}\}\text{.}$</p>
</div>
<div id="S4.SS1.p6" class="ltx_para">
<p class="ltx_p">Let $\mathrm{sp}_{j}(t)$ be the space of the algorithm for stage $j$ at precisions at most $t\text{.}$ The input, the seeds or the row selected in <a href="#S3.Thmtheorem3" title="Lemma 3.3. ‣ 3.2 A Contractive Trailing Block ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.3</span></a>, and the counters, partial products and partial sums of the nested sums take at most $q(n+m+t)$ bits, by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(iii), for a polynomial $q$ that does not depend on $j\text{.}$ Since the entries of $U^{(j)}$ are computed one at a time,</p>
<table id="S4.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathrm{sp}_{j+1}(t)\leq\mathrm{sp}_{j}(\max\{t+3n+17,t_{0}\})+q(n+m+t).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $j&lt;J\text{,}$ every precision that occurs is at most $t_{\max}=\max\{t,t_{0}\}+J(3n+17)\text{,}$ and $\mathrm{sp}_{j}(t)\leq\mathrm{sp}_{0}(t_{\max})+J\,q(n+m+t_{\max})\text{.}$ This is polynomial in $n+m+t\text{,}$ because $J$ and $t_{0}$ are polynomial in $n$ and $\mathrm{sp}_{0}$ is the space of the given entry algorithm.</p>
</div>
<div id="S4.SS1.p7" class="ltx_para">
<p class="ltx_p">For item (ii), <a href="#S3.Thmtheorem8" title="Lemma 3.8. ‣ 3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.8</span></a> gives the stage $j$ and the component of gate $i\text{,}$ and the control string $y$ contains $z_{&lt;j}\text{,}$ which determines $U^{(j)}\text{,}$ $P_{\mathrm{L}}\text{,}$ $P_{\mathrm{R}}$ and $G\text{.}$ A component that occurs as an adjoint has the conjugate transposes of the parameters given below. In $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ the parameters are NOT or the identity in the permutation, signs in the diagonal gate, and $H$ or the identity in the Hadamard transform, all fixed by the selected seeds or row. In the Fourier transforms and in the reflections of <a href="#S3.Thmtheorem6" title="Lemma 3.6. ‣ 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.6</span></a> they are fixed by the sizes, with phases at rational multiples of $\pi\text{,}$ and at dimension one the gate applies a phase, the entry of $U^{(j)}$ given by item (i). This leaves the circuits for $\widehat{\Lambda}_{\mathcal{E}}$ and $\widehat{\Lambda}_{\mathcal{E}^{\prime}}\text{,}$ whose parameters come from these matrices and their patterns, and the patterns are computable from the row index by <a href="#S3.Thmtheorem5" title="Lemma 3.5. ‣ 3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.5</span></a>.</p>
</div>
<div id="S4.SS1.p8" class="ltx_para">
<p class="ltx_p">In the column of a leading coordinate, the entries of $\Lambda_{\mathcal{E}}$ are $0$ or $1\text{.}$ By <a href="#S3.E8" title="In 3.3 Smaller Unitaries and Two Near-Isometries ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.8)</span></a>, an entry in the column of a trailing coordinate is a sum over at most $N2^{nN}$ paths of products of at most $N$ conjugated entries of $G_{21},G_{22}\text{,}$ which have modulus at most one. Let $t_{2}$ be the least integer with $2N^{2}2^{nN-t_{2}}\leq 2^{-t_{\Lambda}-4}\text{.}$ Rounding the entries of $G_{21},G_{22}$ to the $2^{-t_{2}}$ grid changes each path product by at most $N2^{-t_{2}}(1+2^{-t_{2}})^{N}\leq 2N2^{-t_{2}}\text{,}$ so the exact sum of the rounded products is within $2^{-t_{\Lambda}-4}$ of the entry, which is the precision that the rounding in <a href="#S3.SS5" title="3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3.5</span></a> requires. The same bound holds for $\Lambda_{\mathcal{E}^{\prime}}\text{,}$ because its row $(\zeta,c)$ is the row $(-\zeta,c)$ of $\Lambda_{\mathcal{E}}$ for $G^{\dagger}\text{.}$ These computations use item (i) at one precision, polynomial in $n+m$ and independent of $t\text{,}$ so $\widehat{\Lambda}$ does not depend on $t\text{.}$ Each of its entries is a Gaussian integer divided by $D_{\Lambda}=2^{t_{\Lambda}}(1+\delta)=2^{t_{\Lambda}}+2^{n+w+4}\text{.}$</p>
</div>
<div id="S4.SS1.p9" class="ltx_para">
<p class="ltx_p">The rounding makes the prefix probabilities exact rational numbers. In <a href="#S3.E10" title="In 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.10)</span></a> every squared amplitude, including $1-\lVert\widehat{\Lambda}\lvert v\rangle\rVert^{2}\text{,}$ is an integer divided by $D_{\Lambda}^{2}\text{.}$ The prefix probability $\mu(y)$ is the sum of the squared amplitudes of the basis states that extend $y\text{,}$ so $D_{\Lambda}^{2}\mu(y)$ is an integer: the sum of $\lvert D_{\Lambda}\widehat{\Lambda}_{uv}\rvert^{2}$ over the rows $u$ whose pattern contains $v$ and for which $u1$ extends $y\text{,}$ plus $D_{\Lambda}^{2}(1-\lVert\widehat{\Lambda}\lvert v\rangle\rVert^{2})$ if $0^{w+1}$ extends $y\text{.}$ By <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(iii) it can be computed exactly. Therefore the condition $\mu(y)&gt;0$ in <a href="#S3.E9" title="In 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.9)</span></a> is decided exactly, and each ratio there is a rational of polynomial bit length, whose square root can be computed to precision $t$ by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(ii). A nonzero amplitude $a/D_{\Lambda}\text{,}$ with $a$ a Gaussian integer, has the phase $a/\lvert a\rvert\text{,}$ whose real and imaginary parts are $\pm\sqrt{(\operatorname{Re}a)^{2}/\lvert a\rvert^{2}}$ and $\pm\sqrt{(\operatorname{Im}a)^{2}/\lvert a\rvert^{2}}\text{,}$ with the signs of $\operatorname{Re}a$ and $\operatorname{Im}a\text{.}$ The amplitude at $\lvert 0^{w}\rangle\lvert 0\rangle$ is nonnegative and has phase one.</p>
</div>
<div id="S4.SS1.p10" class="ltx_para">
<p class="ltx_p">In <a href="#S3.E11" title="In 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.11)</span></a>, for nonempty $I_{u}\text{,}$ the prefix probability of $y$ is the number of positions in $I_{u}$ that extend $y\text{,}$ divided by $\lvert I_{u}\rvert\text{,}$ and the phases are one. We take $W_{\theta,u}$ to be the rotation of the form <a href="#S3.E9" title="In 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.9)</span></a> with the first column given in <a href="#S3.Thmtheorem6" title="Lemma 3.6. ‣ 3.4 Implementing a Row-Sparse Near-Isometry ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.6</span></a>, and its entries are computed from $\sin\theta$ by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(ii).
∎</p>
</div>
</div>
</section>
<section id="S4.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-language-b">
<span class="ltx_tag ltx_tag_subsection">4.2 </span>The Language $B$
</h3>

<div id="S4.SS2.p1" class="ltx_para">
<p class="ltx_p">The circuit $C_{0}$ has polynomially many gates and exponentially many parameters, each a matrix in $\mathrm{U}(2)\text{.}$ We approximate each parameter by short words over $\mathcal{G}\text{,}$ and the language $B$ contains the bits of these words. The determinant of a word over $\{H,T,T^{\dagger}\}$ is an eighth root of unity, so such a word approximates a parameter only up to a phase, and the phases of the parameters $W_{i,y}$ for different $y$ are relative phases of the gate $W_{i}\text{.}$ We therefore use two words, one on the target of the gate and one on an ancilla, the phase qubit. If $W=e^{\mathrm{i}\gamma}W_{1}$ with $W_{1}\in\mathrm{SU}(2)\text{,}$ then</p>
<table id="S4.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\bigl(W_{1}\otimes\operatorname{diag}(e^{\mathrm{i}\gamma},e^{-\mathrm{i}\gamma})\bigr)(\lvert\psi\rangle\lvert 0\rangle)=(W\lvert\psi\rangle)\lvert 0\rangle,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4.1)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">and both factors on the left have determinant one. By <a href="#S2.Thmtheorem8" title="Fact 2.8 ([DN06, Theorem 1]). ‣ 2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.8</span></a>, words over the set of the next lemma approximate them.</p>
</div>
<div id="S4.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">There is a finite inverse-closed set $\mathcal{S}$ of words over $\{H,T,T^{\dagger}\}\text{,}$ each of determinant one, that generates a dense subgroup of $\mathrm{SU}(2)\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS2.p2" class="ltx_para">
<p class="ltx_p">Let $\Gamma_{0}$ be the group generated by $H$ and $T\text{,}$ which is dense in $\mathrm{U}(2)$ modulo global phases <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx42" title="" class="ltx_ref">NC10</a>, Section 4.5.3]</cite>. The determinant maps $\Gamma_{0}$ to the eighth roots of unity, so its kernel $\Gamma$ has finite index in $\Gamma_{0}\text{,}$ and $\Gamma$ is finitely generated by Schreier’s lemma <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx50" title="" class="ltx_ref">Sch27</a>]</cite>. Let $\mathcal{S}$ consist of generators of $\Gamma\text{,}$ written as words over $\{H,T,T^{\dagger}\}\text{,}$ and their inverses. To show that $\Gamma$ is dense in $\mathrm{SU}(2)\text{,}$ let $W\in\mathrm{SU}(2)\text{,}$ and let $W_{k}\in\Gamma_{0}$ and phases $\phi_{k}$ satisfy $\phi_{k}W_{k}\to W\text{.}$ Taking determinants gives $\phi_{k}^{16}=\det(\phi_{k}W_{k})^{8}\to 1\text{,}$ so $W_{k}^{16}\to W^{16}\text{,}$ and $W_{k}^{16}\in\Gamma\text{.}$ Thus the closure of $\Gamma$ contains the sixteenth power of every element of $\mathrm{SU}(2)\text{,}$ and every element of $\mathrm{SU}(2)$ is such a power.
∎</p>
</div>
</div>
<div id="S4.Thmtheorem3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The NOT gate, the Toffoli gate and the uniformly controlled gate with a two-bit control that applies $I,H,T,T^{\dagger}$ for the strings $00,01,10,11$ are implemented exactly over $\mathcal{G}$ with ancillas returned to zero.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS2.p3" class="ltx_para">
<p class="ltx_p">The matrix $T^{4}$ is $\operatorname{diag}(1,-1)\text{,}$ and NOT is $HT^{4}H\text{.}$ For bits $u_{1},u_{2},u_{3}\text{,}$</p>
<table id="S4.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$4u_{1}u_{2}u_{3}=u_{1}+u_{2}+u_{3}-(u_{1}\oplus u_{2})-(u_{1}\oplus u_{3})-(u_{2}\oplus u_{3})+(u_{1}\oplus u_{2}\oplus u_{3}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Hence the gate with phase $e^{\mathrm{i}\pi u_{1}u_{2}u_{3}}\text{,}$ which is $T^{4}$ with two controls, is obtained by computing each parity on an ancilla with CNOT gates, applying $T$ or $T^{\dagger}$ according to the sign, and uncomputing the parity. Conjugating its target by $H$ gives the Toffoli gate. A controlled $T$ or $T^{\dagger}$ is $T$ or $T^{\dagger}$ applied to an ancilla that holds the conjunction of control and target, computed and uncomputed by a Toffoli gate. Let $W=T^{2}HT\text{,}$ which satisfies $W\,\mathrm{NOT}\,W^{\dagger}=H\text{.}$ Then $W^{\dagger}$ on the target, followed by a CNOT and by $W$ on the target, is the controlled $H\text{.}$ Finally, for each control string, NOT and Toffoli gates compute on an ancilla whether the control has this value, the corresponding unitary is applied with this ancilla as control, and the ancilla is uncomputed.
∎</p>
</div>
</div>
<div id="S4.Thmtheorem4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.4</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $\eta=2^{-m}/(64(S+1))\text{.}$ There are a language $B\in\mathsf{PSPACE}^{A}$ and a polynomial-time algorithm, which does not depend on $A$ or $U\text{,}$ that on input $(1^{n},1^{m},i)$ outputs a unitary circuit $\widehat{W}_{i}$ over $\mathcal{G}$ such that $\widehat{W}^{B}_{i}$ implements $W_{i}$ on the zero-ancilla subspace with error $\eta\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS2.p4" class="ltx_para">
<p class="ltx_p">Fix the set $\mathcal{S}$ of <a href="#S4.Thmtheorem2" title="Lemma 4.2. ‣ 4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>, the polynomial $p_{\mathcal{S}}$ of <a href="#S2.Thmtheorem8" title="Fact 2.8 ([DN06, Theorem 1]). ‣ 2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.8</span></a> and the largest number $\ell_{\mathcal{S}}$ of letters of an element of $\mathcal{S}\text{,}$ and let $\ell=\ell_{\mathcal{S}}\,p_{\mathcal{S}}(\lceil\log(16/\eta)\rceil)\text{.}$ Fix $i,y$ and let $W=W_{i,y}\text{.}$ For a pair $(W^{\prime},W^{\prime\prime})$ of words of length $\ell$ over $\{I,H,T,T^{\dagger}\}\text{,}$ let $\operatorname{dist}(W^{\prime},W^{\prime\prime})=\lVert(W^{\prime}\otimes W^{\prime\prime})\iota_{1}-W\otimes\lvert 0\rangle\rVert_{F}^{2}\text{.}$ From the entries of $W$ and of the two words at a precision $t^{\prime}$ with $2^{8-t^{\prime}}\leq\eta^{2}/64\text{,}$ we compute a number $\widehat{\operatorname{dist}}(W^{\prime},W^{\prime\prime})$ within $\eta^{2}/64$ of $\operatorname{dist}(W^{\prime},W^{\prime\prime})\text{.}$ The entries of $W$ are given by <a href="#S4.Thmtheorem1" title="Lemma 4.1. ‣ 4.1 The Parameters in Polynomial Space ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>(ii), and those of the words by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(v), whose hypothesis holds because the letters are unitary.</p>
</div>
<div id="S4.SS2.p5" class="ltx_para">
<p class="ltx_p">By <a href="#S2.Thmtheorem8" title="Fact 2.8 ([DN06, Theorem 1]). ‣ 2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.8</span></a>, the factors in <a href="#S4.E1" title="In 4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(4.1)</span></a> are within $\eta/16$ of words $W^{\prime}_{0},W^{\prime\prime}_{0}$ over $\mathcal{S}$ with at most $p_{\mathcal{S}}(\lceil\log(16/\eta)\rceil)$ elements, which become words of length $\ell$ after padding with $I\text{.}$ Then $\lVert(W^{\prime}_{0}\otimes W^{\prime\prime}_{0})\iota_{1}-W\otimes\lvert 0\rangle\rVert\leq\eta/8\text{,}$ so $\operatorname{dist}(W^{\prime}_{0},W^{\prime\prime}_{0})\leq 2(\eta/8)^{2}$ and $\widehat{\operatorname{dist}}(W^{\prime}_{0},W^{\prime\prime}_{0})\leq\eta^{2}/32+\eta^{2}/64&lt;\eta^{2}/4\text{.}$ Let $(W^{\prime},W^{\prime\prime})$ be the lexicographically first pair with $\widehat{\operatorname{dist}}(W^{\prime},W^{\prime\prime})\leq\eta^{2}/4\text{,}$ the selected pair for $(i,y)\text{.}$ Then $\operatorname{dist}(W^{\prime},W^{\prime\prime})\leq\eta^{2}/4+\eta^{2}/64&lt;\eta^{2}\text{,}$ and hence $\lVert(W^{\prime}\otimes W^{\prime\prime})\iota_{1}-W\otimes\lvert 0\rangle\rVert&lt;\eta\text{.}$</p>
</div>
<div id="S4.SS2.p6" class="ltx_para">
<p class="ltx_p">A query string of $B$ consists of $1^{n}0\text{,}$ $1^{m}0\text{,}$ the index $i\text{,}$ the control string $y$ padded with zeros to the width $w^{\prime}\text{,}$ a bit that selects one of the two words, the position of a letter, and a bit that selects one of the two bits of the index of this letter, where $00,01,10,11$ index $I,H,T,T^{\dagger}\text{.}$ The fields have fixed lengths for given $(n,m)\text{.}$ The string is in $B$ if the bit that these fields specify in the selected pair for $(i,y)$ is one, and malformed strings are not in $B\text{.}$ The gate list of <a href="#S3.Thmtheorem8" title="Lemma 3.8. ‣ 3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.8</span></a> is computable from $(n,m)\text{,}$ and by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(iv) the selected pair can be computed in space polynomial in $n+m\text{.}$ The string contains $1^{n}$ and $1^{m}\text{,}$ so this space is polynomial in the length of the string. Thus $B\in\mathsf{PSPACE}^{A}\text{.}$</p>
</div>
<div id="S4.SS2.p7" class="ltx_para">
<p class="ltx_p">For a position and a word, let $Q$ be the circuit that, for each of the two values of the last bit of the query string, writes this string on a register of ancillas, by NOT gates and by CNOT gates from the controls of gate $i\text{,}$ applies a gate $O_{B}$ with its answer on one of two further ancillas, and repeats the NOT and CNOT gates, which clears the register. Thus $Q$ writes the index of the letter on the two further ancillas. The circuit for this position and word is $Q\text{,}$ followed by the gate of <a href="#S4.Thmtheorem3" title="Lemma 4.3. ‣ 4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> controlled on these ancillas and acting on the target of gate $i$ or on the phase qubit, followed by $Q^{-1}\text{.}$ Let $\widehat{W}_{i}$ be the product of these circuits over all positions and both words. On a control string $y$ with the ancillas at zero, $\widehat{W}^{B}_{i}$ applies the selected pair to the target and the phase qubit and returns the other ancillas to zero. Hence $\widehat{W}^{B}_{i}\iota-\iota W_{i}$ is a direct sum over $y$ of matrices of norm below $\eta\text{.}$ The circuit is computed from $(n,m,i)$ through $S\text{,}$ $w^{\prime}\text{,}$ $\eta$ and $\ell\text{,}$ without evaluating $B\text{.}$
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>.</h6>
<div id="S4.SS2.p8" class="ltx_para">
<p class="ltx_p">Let $B$ be the language of <a href="#S4.Thmtheorem4" title="Lemma 4.4. ‣ 4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.4</span></a>. Write $C_{0}$ with its exact parameters as a product $\Gamma_{h}\cdots\Gamma_{1}$ of gates, and let $C_{n,m}$ be the product $\widehat{\Gamma}_{h}\cdots\widehat{\Gamma}_{1}\text{,}$ with $\widehat{\Gamma}_{k}=\widehat{W}_{i}$ if $\Gamma_{k}=W_{i}$ and $\widehat{\Gamma}_{k}=\Gamma_{k}$ otherwise. If $\iota$ sets the ancillas of <a href="#S4.Thmtheorem4" title="Lemma 4.4. ‣ 4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.4</span></a> to zero, then</p>
<table id="S4.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$C^{B}_{n,m}\iota-\iota C_{0}=\sum_{k=1}^{h}\widehat{\Gamma}^{B}_{h}\cdots\widehat{\Gamma}^{B}_{k+1}(\widehat{\Gamma}^{B}_{k}\iota-\iota\Gamma_{k})\Gamma_{k-1}\cdots\Gamma_{1},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">which has norm at most $S\eta$ by <a href="#S4.Thmtheorem4" title="Lemma 4.4. ‣ 4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.4</span></a>. With <a href="#S3.E13" title="In 3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(3.13)</span></a>, $C^{B}_{n,m}$ implements $U_{n}$ on the zero-ancilla subspace with error less than $S\eta+2^{-m}/64&lt;2^{-m}/32\text{,}$ and <a href="#S2.Thmtheorem7" title="Lemma 2.7. ‣ 2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.7</span></a> gives an extension $\widetilde{U}$ of $U_{n}$ with $\lVert C^{B}_{n,m}-\widetilde{U}\rVert&lt;3\cdot 2^{-m}/32&lt;2^{-m}\text{.}$ The set $\mathcal{S}$ and the polynomial $p_{\mathcal{S}}$ do not depend on $A$ or $U\text{,}$ and neither do the algorithms of <a href="#S3.Thmtheorem8" title="Lemma 3.8. ‣ 3.5 The Recursive Circuit ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemmas</span> <span class="ltx_text ltx_ref_tag">3.8</span></a> and <a href="#S4.Thmtheorem4" title="Lemma 4.4. ‣ 4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.4</span></a>, so the algorithm that produces $C_{n,m}$ is the same for every $A$ and $U\text{.}$
∎</p>
</div>
</div>
</section>
<section id="S4.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-main-theorem">
<span class="ltx_tag ltx_tag_subsection">4.3 </span>The Main Theorem</h3>

<div id="S4.SS3.p1" class="ltx_para">
<p class="ltx_p"><a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> and <a href="#S2.Thmtheorem5" title="Fact 2.5 ([KT26, Theorem 6.17, items 1 and 6]). ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.5</span></a> give the clean case of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> directly. For the projective classes we reduce to the clean ones through $U_{n}\otimes U_{n}^{\dagger}\text{,}$ a construction of Kretschmer and Tang <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Theorems 5.20 and 5.23]</cite>. The garbage state of a dilation does not depend on the input, so a circuit for a dilation of $U_{n}$ on one data register, followed by its adjoint on a second data register with the same ancillas, implements $U_{n}\otimes U_{n}^{\dagger}$ with the ancillas returned to zero. Let $U\otimes U^{\dagger}$ be the unitary language whose member of length $2n$ is $U_{n}\otimes U_{n}^{\dagger}$ and whose members of odd length are identities.</p>
</div>
<div id="S4.Thmtheorem5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.5</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $L$ be a classical oracle. If $U\in\mathsf{projUnitaryP}^{L}\text{,}$ then $U\otimes U^{\dagger}\in\mathsf{unitaryP}^{L}\text{,}$ and if $U\in\mathsf{projUnitaryPSPACE}^{L}\text{,}$ then $U\otimes U^{\dagger}\in\mathsf{unitaryPSPACE}^{L}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p2" class="ltx_para">
<p class="ltx_p">Let $C=C_{n,m+1}$ be a circuit of the given family on $n+a$ qubits, and let $\widetilde{U}$ be a dilation of $U_{n}$ with garbage state $\lvert g\rangle$ and $\lVert C^{L}-\widetilde{U}\rVert\leq 2^{-m-1}\text{.}$ Let $C^{\prime}$ act on $n$-qubit registers $\mathsf{X},\mathsf{Y}$ and the ancilla register $\mathsf{W}$ as $C$ on $\mathsf{X}\mathsf{W}$ followed by $C^{\dagger}$ on $\mathsf{Y}\mathsf{W}\text{,}$ and let $\widetilde{W}=\widetilde{U}^{\dagger}_{\mathsf{Y}\mathsf{W}}\widetilde{U}_{\mathsf{X}\mathsf{W}}\text{.}$ Then $\lVert C^{\prime L}-\widetilde{W}\rVert\leq 2\lVert C^{L}-\widetilde{U}\rVert\leq 2^{-m}\text{.}$ Since $\widetilde{U}(\lvert\chi\rangle\lvert 0^{a}\rangle)=(U_{n}\lvert\chi\rangle)\lvert g\rangle$ for every $\lvert\chi\rangle\text{,}$ also $\widetilde{U}^{\dagger}(\lvert\chi\rangle\lvert g\rangle)=(U_{n}^{\dagger}\lvert\chi\rangle)\lvert 0^{a}\rangle\text{.}$ Both identities hold in the presence of further registers, so for $\lvert\Psi\rangle$ on $\mathsf{X}\mathsf{Y}\text{,}$</p>
<table id="S4.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widetilde{W}(\lvert\Psi\rangle\lvert 0^{a}\rangle)=\widetilde{U}^{\dagger}_{\mathsf{Y}\mathsf{W}}\bigl(((U_{n}\otimes I)\lvert\Psi\rangle)\lvert g\rangle\bigr)=((U_{n}\otimes U_{n}^{\dagger})\lvert\Psi\rangle)\lvert 0^{a}\rangle.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Thus $\widetilde{W}$ is an extension of $U_{n}\otimes U_{n}^{\dagger}\text{.}$ The circuits $C^{\prime}\text{,}$ with empty circuits at odd lengths, form a uniform family: the adjoint of a gate list is the reversed list of adjoint gates, with $O_{L}^{\dagger}=O_{L}\text{,}$ and in polynomial space the $h$-th gate from the end can be found by running the generator with a counter.
∎</p>
</div>
</div>
<div id="S4.Thmtheorem6" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.6</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $L$ be a classical oracle. If $U\otimes U^{\dagger}\in\mathsf{unitaryP}^{L}\text{,}$ then $U\in\mathsf{projUnitaryP}^{L}\text{,}$ and if $U\otimes U^{\dagger}\in\mathsf{unitaryPSPACE}^{L}\text{,}$ then $U\in\mathsf{projUnitaryPSPACE}^{L}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p3" class="ltx_para">
<p class="ltx_p">Let $\widetilde{W}$ be an extension of $U_{n}\otimes U_{n}^{\dagger}$ on $2n+a$ qubits. For every $\lvert\psi\rangle$ on the first $n$ qubits,</p>
<table id="S4.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widetilde{W}(\lvert\psi\rangle\lvert 0^{n}\rangle\lvert 0^{a}\rangle)=(U_{n}\lvert\psi\rangle)(U_{n}^{\dagger}\lvert 0^{n}\rangle)\lvert 0^{a}\rangle,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">so $\widetilde{W}$ is a dilation of $U_{n}$ on $n+a$ ancillas, with garbage state $(U_{n}^{\dagger}\lvert 0^{n}\rangle)\lvert 0^{a}\rangle\text{.}$ Hence the circuits of the given family at length $2n\text{,}$ with the last $n+a$ qubits as ancillas, form a family for $U\text{.}$
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>.</h6>
<div id="S4.SS3.p4" class="ltx_para">
<p class="ltx_p">For the clean classes, if $U\in\mathsf{unitaryPSPACE}^{A}\text{,}$ then <a href="#S2.Thmtheorem5" title="Fact 2.5 ([KT26, Theorem 6.17, items 1 and 6]). ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.5</span></a> and <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> give $B\in\mathsf{PSPACE}^{A}$ with $U\in\mathsf{unitaryP}^{B}\text{.}$ Conversely, let $L\in\mathsf{PSPACE}^{A}$ and $U\in\mathsf{unitaryP}^{L}\text{.}$ A time-uniform family is space-uniform, so $U\in\mathsf{unitaryPSPACE}^{L}\text{,}$ and by <a href="#S2.Thmtheorem5" title="Fact 2.5 ([KT26, Theorem 6.17, items 1 and 6]). ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.5</span></a> it has entries computable in polynomial space relative to $L\text{.}$ By <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(i) these entries are computable in polynomial space relative to $A\text{,}$ so $U\in\mathsf{unitaryPSPACE}^{A}$ by <a href="#S2.Thmtheorem5" title="Fact 2.5 ([KT26, Theorem 6.17, items 1 and 6]). ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>.</p>
</div>
<div id="S4.SS3.p5" class="ltx_para">
<p class="ltx_p">For the projective classes, the first and last equivalences of</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="Sx1.EGx4"></span><span class="paper-eq-anchor" id="S4.Ex9"></span><span class="paper-eq-anchor" id="S4.Ex10"></span><span class="paper-eq-anchor" id="S4.Ex11"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle U\in\mathsf{projUnitaryPSPACE}^{A} &amp; \displaystyle\iff U\otimes U^{\dagger}\in\mathsf{unitaryPSPACE}^{A} \\
 &amp; \displaystyle\iff U\otimes U^{\dagger}\in\mathsf{unitaryP}^{L}\text{ for some }L\in\mathsf{PSPACE}^{A} \\
 &amp; \displaystyle\iff U\in\mathsf{projUnitaryP}^{L}\text{ for some }L\in\mathsf{PSPACE}^{A}
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p class="ltx_p">are <a href="#S4.Thmtheorem5" title="Lemma 4.5. ‣ 4.3 The Main Theorem ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemmas</span> <span class="ltx_text ltx_ref_tag">4.5</span></a> and <a href="#S4.Thmtheorem6" title="Lemma 4.6. ‣ 4.3 The Main Theorem ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.6</span></a>, and the middle one is the clean case.</p>
</div>
<div id="S4.SS3.p6" class="ltx_para">
<p class="ltx_p">Now let $K$ be $\mathsf{PSPACE}^{A}$-complete, let $L\in\mathsf{PSPACE}^{A}\text{,}$ and let $f$ be a reduction from $L$ to $K\text{,}$ computed without access to $A\text{,}$ with $\lvert f(x)\rvert\leq p(\lvert x\rvert)\text{.}$ Let $O_{L}$ be a gate on $\ell$ query qubits and an answer qubit. There is a circuit $R$ of Toffoli, CNOT and NOT gates <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx11" title="" class="ltx_ref">Ben73</a>; <a href="#bib.bibx53" title="" class="ltx_ref">Tof80</a>]</cite>, computable in polynomial time without an oracle, that computes on ancillas the string $f(x)\text{,}$ padded to $p(\ell)$ wires, and the bits $\mathbf{1}[\lvert f(x)\rvert=\ell^{\prime}]$ for $\ell^{\prime}\leq p(\ell)\text{.}$ For each $\ell^{\prime}\text{,}$ let $Q_{\ell^{\prime}}$ be the query to $O_{K}$ on the first $\ell^{\prime}$ wires of $f(x)\text{,}$ with the answer qubit of $O_{L}$ as its answer, controlled on the bit $\mathbf{1}[\lvert f(x)\rvert=\ell^{\prime}]$ as in <a href="#S2.SS2" title="2.2 Unitary Languages and Their Complexity Classes ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>. On a basis state $\lvert x,b\rangle$ with the ancillas at zero, only $Q_{\lvert f(x)\rvert}$ acts, and it adds $K(f(x))=L(x)$ to $b\text{.}$ Hence $R^{-1}(\prod_{\ell^{\prime}}Q_{\ell^{\prime}})R$ acts as $O_{L}$ on the zero-ancilla subspace.</p>
</div>
<div id="S4.SS3.p7" class="ltx_para">
<p class="ltx_p">Let $C$ be a circuit of a $\mathsf{unitaryP}^{L}$ family at precision $m+2\text{,}$ and let $C^{\prime}$ be $C$ with each $O_{L}$ replaced by $R^{-1}(\prod_{\ell^{\prime}}Q_{\ell^{\prime}})R\text{.}$ Then $C^{\prime K}$ implements $U_{n}$ on the zero-ancilla subspace with error $2^{-m-2}\text{,}$ so <a href="#S2.Thmtheorem7" title="Lemma 2.7. ‣ 2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.7</span></a> gives an extension at distance $3\cdot 2^{-m-2}&lt;2^{-m}\text{.}$ For a family of a projective class, the last statement of <a href="#S2.Thmtheorem7" title="Lemma 2.7. ‣ 2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.7</span></a> gives a dilation at distance $3\cdot 2^{-m-2}\text{.}$ Hence $\mathsf{unitaryP}^{L}\subseteq\mathsf{unitaryP}^{K}$ and $\mathsf{projUnitaryP}^{L}\subseteq\mathsf{projUnitaryP}^{K}\text{.}$ Since $K\in\mathsf{PSPACE}^{A}\text{,}$ both unions are attained at $K\text{.}$
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S1.Thmtheorem2" title="Corollary 1.2. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.2</span></a>.</h6>
<div id="S4.SS3.p8" class="ltx_para">
<p class="ltx_p"><a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> with $A=A_{U}$ and the entry algorithm $\mathrm{dec}^{A_{U}}$ of <a href="#S2.SS3" title="2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.3</span></a> gives $B_{U}\in\mathsf{PSPACE}^{A_{U}}$ with $U\in\mathsf{unitaryP}^{B_{U}}\text{,}$ and the algorithm that produces the circuits does not depend on $U\text{.}$ In particular every unitary language lies in $\mathsf{unitaryP}^{\mathsf{ALL}}\text{,}$ and the reverse inclusion holds by definition.
∎</p>
</div>
</div>
</section>
</section>
<section id="S5" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="oracle-characterization-and-cryptography">
<span class="ltx_tag ltx_tag_section">5 </span>Oracle Characterization and Cryptography</h2>

<div id="S5.p1" class="ltx_para">
<p class="ltx_p">By <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>, any $\mathsf{PSPACE}^{A}$-complete language suffices as an oracle for all of $\mathsf{unitaryPSPACE}^{A}\text{.}$ In fact a language $L$ suffices exactly when $\mathsf{PSPACE}^{A}\subseteq\mathsf{BQP}^{L}\text{.}$ The oracle gate of a language in $\mathsf{PSPACE}^{A}$ is itself a polynomial-space unitary, so a circuit that implements it decides the language. Conversely, an oracle gate for a language in $\mathsf{BQP}^{L}$ can be replaced inside a unitary circuit by a coherent run of its decider.</p>
</div>
<div id="S5.p2" class="ltx_para">
<p class="ltx_p">By synthesizing a measurement, we also show that a polynomial-time algorithm with a $\mathsf{PSPACE}$ oracle distinguishes any two efficiently generated states at inverse-polynomial trace distance, from one copy and with inverse-polynomial advantage. If $\mathsf{BQP}=\mathsf{PSPACE}$ this oracle can be removed, so EFI pairs imply $\mathsf{BQP}\neq\mathsf{PSPACE}$ (<a href="#S5.SS2" title="5.2 Distinguishing States with a PSPACE Oracle ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>). In the Oracle State Distinguishing Game of Lombardi, Ma and Wright <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>]</cite> the oracle may depend on the states, and a synthesized unitary wins the game (<a href="#S5.SS3" title="5.3 A Polynomial-Query Adversary for the Oracle State Distinguishing Game ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.3</span></a>).</p>
</div>
<section id="S5.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-oracle-characterization">
<span class="ltx_tag ltx_tag_subsection">5.1 </span>The Oracle Characterization</h3>

<div id="S5.SS1.p1" class="ltx_para">
<p class="ltx_p">To replace an oracle gate $O_{B}$ for a language $B\in\mathsf{BQP}^{L}\text{,}$ we need a unitary circuit that acts correctly on superpositions of queries and returns its ancillas to zero. The compute-copy-uncompute construction <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx6" title="" class="ltx_ref">BBBV97</a>, Theorem 4.14 and Corollary 4.15]</cite> does this, and its error in operator norm is exponentially small, because the majority of many runs of the decider is wrong with exponentially small probability.</p>
</div>
<div id="S5.Thmtheorem1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $L$ be a classical oracle and $B\in\mathsf{BQP}^{L}\text{.}$ A polynomial-time algorithm with no oracle maps $(1^{\ell},1^{m})\text{,}$ for $\ell,m\geq 1\text{,}$ to a unitary circuit $C^{\mathrm{sim}}_{\ell,m}$ over $\mathcal{G}$ with oracle gates $O_{L}\text{,}$ on $\ell$ query qubits, one answer qubit and ancillas, that implements the oracle gate $O_{B}$ on the zero-ancilla subspace with error $2^{-m}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS1.p2" class="ltx_para">
<p class="ltx_p">Let $(\mathcal{C}_{\ell})_{\ell}$ be a family for $B$ as in the definition of $\mathsf{BQP}^{L}\text{.}$ A measurement is a CNOT onto a new ancilla that is never used again, followed by discarding this ancilla. Hence, using ancillas for new qubits and keeping all discarded qubits, we get a unitary circuit $C_{\ell}$ over $\mathcal{G}$ with oracle gates $O_{L}$ such that measuring its output wire on $\lvert x\rangle$ and zero ancillas gives $B(x)$ with probability at least $2/3\text{,}$ for $x\in\{0,1\}^{\ell}\text{.}$</p>
</div>
<div id="S5.SS1.p3" class="ltx_para">
<p class="ltx_p">Let $C$ be the circuit that copies the query register to $k=36(m+1)$ further registers by CNOT gates, runs $C_{\ell}$ on each of them with its own ancillas, and computes the majority of the $k$ output wires on a further ancilla by Toffoli, CNOT and NOT gates <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx11" title="" class="ltx_ref">Ben73</a>; <a href="#bib.bibx53" title="" class="ltx_ref">Tof80</a>]</cite>. Let $C^{\mathrm{sim}}_{\ell,m}=C^{-1}\,\mathrm{CNOT}\,C\text{,}$ where the CNOT goes from this ancilla to the answer qubit.</p>
</div>
<div id="S5.SS1.p4" class="ltx_para">
<p class="ltx_p">The circuit $C$ uses the query register only as a control, so $C$ maps $\lvert x\rangle$ and zero ancillas to $\lvert x\rangle\lvert\varphi_{x}\rangle\text{.}$ Write $\lvert\varphi_{x}\rangle=\lvert\varphi_{x}^{+}\rangle+\lvert\varphi_{x}^{-}\rangle\text{,}$ where the majority ancilla equals $B(x)$ in the first term and $1-B(x)$ in the second. The $k$ runs are independent and each is wrong with probability at most $1/3\text{.}$ A wrong majority requires at least $k/2$ wrong runs, so by Hoeffding’s inequality</p>
<table id="S5.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert\lvert\varphi_{x}^{-}\rangle\rVert^{2}\leq e^{-2(k/6)^{2}/k}=e^{-2(m+1)}&lt;2^{-2m-2}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">For a unit vector $\lvert\beta\rangle$ on the answer qubit, the two terms give</p>
<table id="S5.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathrm{CNOT}(\lvert\beta\rangle\lvert\varphi_{x}\rangle)-(\mathrm{NOT}^{B(x)}\lvert\beta\rangle)\lvert\varphi_{x}\rangle=\bigl((\mathrm{NOT}^{1-B(x)}-\mathrm{NOT}^{B(x)})\lvert\beta\rangle\bigr)\lvert\varphi_{x}^{-}\rangle,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">which has norm at most $2\lVert\lvert\varphi_{x}^{-}\rangle\rVert&lt;2^{-m}\text{.}$ Applying $C^{-1}$ to both vectors on the left shows that $C^{\mathrm{sim}}_{\ell,m}$ on $\lvert x\rangle\lvert\beta\rangle$ and zero ancillas is within $2^{-m}$ of $O_{B}\lvert x\rangle\lvert\beta\rangle$ with zero ancillas. The circuit $C^{\mathrm{sim}}_{\ell,m}$ also uses the query register only as a control, so the difference between $C^{\mathrm{sim}}_{\ell,m}\iota_{a}$ and $\iota_{a}O_{B}$ is a direct sum over $x$ of matrices of norm below $2^{-m}\text{.}$
∎</p>
</div>
</div>
<div id="S5.Thmtheorem2" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Corollary 5.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $L$ be a classical oracle and $B\in\mathsf{BQP}^{L}\text{.}$ Then $\mathsf{unitaryP}^{B}\subseteq\mathsf{unitaryP}^{L}$ and $\mathsf{projUnitaryP}^{B}\subseteq\mathsf{projUnitaryP}^{L}\text{.}$ If the circuits of the given family are over $\mathcal{G}\text{,}$ then so are those of the new family.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS1.p5" class="ltx_para">
<p class="ltx_p">Let $C$ be a circuit of the given family at precision $m+3\text{,}$ with $Q$ oracle gates, let $\widetilde{U}$ be an extension or a dilation of $U_{n}$ with $\lVert C^{B}-\widetilde{U}\rVert\leq 2^{-m-3}\text{,}$ and let $m^{\prime}=m+3+\lceil\log(Q+1)\rceil\text{.}$ Let $C^{\prime}$ be $C$ with each oracle gate on $\ell\geq 1$ query qubits replaced by $C^{\mathrm{sim}}_{\ell,m^{\prime}}$ with its own ancillas, and each gate with no query qubits replaced by NOT or the identity, and let $\iota$ set the new ancillas to zero. The telescoping sum in the proof of <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> gives $\lVert C^{\prime}\iota-\iota C^{B}\rVert\leq Q2^{-m^{\prime}}\leq 2^{-m-3}\text{,}$ so $\lVert C^{\prime}\iota-\iota\widetilde{U}\rVert\leq 2^{-m-2}\text{.}$ On the old ancillas at zero, $\widetilde{U}$ acts as $U_{n}$ and leaves them at zero, or at $\lvert g\rangle$ for a dilation. So <a href="#S2.Thmtheorem7" title="Lemma 2.7. ‣ 2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.7</span></a> gives an extension or a dilation of $U_{n}$ at distance $3\cdot 2^{-m-2}&lt;2^{-m}$ from $C^{\prime}\text{.}$ The circuit $C^{\prime}$ is computed in polynomial time with no oracle.
∎</p>
</div>
</div>
<div id="S5.SS1.p6" class="ltx_para">
<p class="ltx_p">For all classical oracles $A$ and $L\text{,}$ <a href="#S1.Thmtheorem3" title="Corollary 1.3. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.3</span></a> states that</p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="Sx1.EGx5"></span><span class="paper-eq-anchor" id="S5.Ex3"></span><span class="paper-eq-anchor" id="S5.Ex4"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\mathsf{unitaryPSPACE}^{A}\subseteq\mathsf{unitaryP}^{L} &amp; \displaystyle\iff\mathsf{PSPACE}^{A}\subseteq\mathsf{BQP}^{L} \\
 &amp; \displaystyle\iff\mathsf{projUnitaryPSPACE}^{A}\subseteq\mathsf{projUnitaryP}^{L},
\end{aligned}$$</div><div class="paper-eqgroup-no"></div></div>

<p class="ltx_p">and that $\mathsf{unitaryP}^{A}=\mathsf{unitaryPSPACE}^{A}$ if and only if $\mathsf{BQP}^{A}=\mathsf{PSPACE}^{A}\text{,}$ and the same for the projective classes.</p>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S1.Thmtheorem3" title="Corollary 1.3. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.3</span></a>.</h6>
<div id="S5.SS1.p7" class="ltx_para">
<p class="ltx_p">Suppose that $\mathsf{PSPACE}^{A}\subseteq\mathsf{BQP}^{L}\text{.}$ A language in $\mathsf{unitaryPSPACE}^{A}$ lies, by <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>, in $\mathsf{unitaryP}^{B}$ for some $B\in\mathsf{PSPACE}^{A}\subseteq\mathsf{BQP}^{L}\text{,}$ and hence in $\mathsf{unitaryP}^{L}$ by <a href="#S5.Thmtheorem2" title="Corollary 5.2. ‣ 5.1 The Oracle Characterization ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>. The same argument applies to the projective classes.</p>
</div>
<div id="S5.SS1.p8" class="ltx_para">
<p class="ltx_p">Conversely, suppose that one of the two inclusions of unitary classes holds, and let $L^{\prime}\in\mathsf{PSPACE}^{A}\text{.}$ The oracle gates $O_{L^{\prime}}$ form a unitary language, whose member of length $n$ is the gate on $n-1$ query qubits and one answer qubit. Its entries are $0$ or $1$ and are computable in polynomial space relative to $A\text{,}$ so it lies in $\mathsf{unitaryPSPACE}^{A}$ by <a href="#S2.Thmtheorem5" title="Fact 2.5 ([KT26, Theorem 6.17, items 1 and 6]). ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">2.5</span></a>. Since the clean classes lie in the projective ones, either inclusion puts it in $\mathsf{projUnitaryP}^{L}\text{.}$ For $x\in\{0,1\}^{\ell}\text{,}$ let $C$ be the circuit of the family at $(1^{\ell+1},1^{3})\text{.}$ Then $C^{L}$ is within $1/8$ of a dilation of $O_{L^{\prime}}$ with garbage state $\lvert g\rangle\text{,}$ so $C^{L}\lvert x,0\rangle\lvert 0^{a}\rangle$ is within $1/8$ of $\lvert x,L^{\prime}(x)\rangle\lvert g\rangle\text{.}$</p>
</div>
<div id="S5.SS1.p9" class="ltx_para">
<p class="ltx_p">The circuit $C$ may contain encoded gates, while a decider for $\mathsf{BQP}^{L}$ is over $\mathcal{G}\text{.}$ An encoded gate on $k$ wires has a description of length at least $4^{k}\text{,}$ so its decomposition into one-qubit gates and CNOT gates <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx42" title="" class="ltx_ref">NC10</a>, Section 4.5]</cite> has polynomial size, and the effective Solovay–Kitaev theorem <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Section 2.2]</cite> compiles these gates in polynomial time. This gives a circuit over $\mathcal{G}$ with oracle gates $O_{L}$ that is within $1/8$ of $C^{L}$ up to a global phase. Its output vector on $\lvert x,0\rangle\lvert 0^{a}\rangle$ is therefore within $1/4$ of $\lvert x,L^{\prime}(x)\rangle\lvert g\rangle$ up to a phase, so measuring the answer qubit gives $L^{\prime}(x)$ except with probability at most $1/16\text{.}$ Hence $L^{\prime}\in\mathsf{BQP}^{L}\text{.}$</p>
</div>
<div id="S5.SS1.p10" class="ltx_para">
<p class="ltx_p">For the last statement, take $L=A\text{.}$ A time-uniform family is space-uniform, so $\mathsf{unitaryP}^{A}\subseteq\mathsf{unitaryPSPACE}^{A}$ and $\mathsf{projUnitaryP}^{A}\subseteq\mathsf{projUnitaryPSPACE}^{A}\text{.}$ Moreover $\mathsf{BQP}^{A}\subseteq\mathsf{PSPACE}^{A}\text{,}$ because by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(vii) the probability that a decider outputs one can be computed to precision $3\text{.}$
∎</p>
</div>
</div>
<div id="S5.SS1.p11" class="ltx_para">
<p class="ltx_p">Kretschmer and Tang ask whether polynomial-time implementations can always erase garbage, that is, whether every $U\in\mathsf{projUnitaryP}$ equals some $U^{\prime}\in\mathsf{unitaryP}$ up to global phases <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Question 3.9]</cite>, and they show that the answer is negative relative to a unitary oracle <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Theorem 6.23]</cite>. Relative to a classical oracle $A$ with $\mathsf{BQP}^{A}=\mathsf{PSPACE}^{A}$ the answer is positive: if $U\in\mathsf{projUnitaryP}^{A}\subseteq\mathsf{projUnitaryPSPACE}^{A}\text{,}$ then $U_{n}=e^{\mathrm{i}\gamma_{n}}U^{\prime}_{n}$ for some phases $e^{\mathrm{i}\gamma_{n}}$ and some $U^{\prime}\in\mathsf{unitaryPSPACE}^{A}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Theorem 6.19]</cite>, and $U^{\prime}\in\mathsf{unitaryP}^{A}$ by <a href="#S1.Thmtheorem3" title="Corollary 1.3. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.3</span></a>.</p>
</div>
</section>
<section id="S5.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="distinguishing-states-with-a-pspace-oracle">
<span class="ltx_tag ltx_tag_subsection">5.2 </span>Distinguishing States with a PSPACE Oracle</h3>

<div id="S5.SS2.p1" class="ltx_para">
<p class="ltx_p">An EFI pair <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx9" title="" class="ltx_ref">BCQ23</a>]</cite> is a pair of mixed states that can be generated efficiently and are statistically far apart, yet computationally indistinguishable. Following Kretschmer and Tang <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Definition 7.13]</cite>, an EFI pair relative to a classical oracle $A$ consists of two time-uniform families of general quantum circuits with encoded gates and oracle gates $O_{A}\text{.}$ Their output states $\rho_{0,n},\rho_{1,n}$ on $w(n)$ qubits satisfy $D(\rho_{0,n},\rho_{1,n})\geq 1/p(n)$ for a positive polynomial $p$ and all large $n\text{.}$ For every nonuniform polynomial-size family $(\mathcal{D}_{n})_{n}$ of such circuits with one output qubit, however, the advantage $\lvert\Pr[\mathcal{D}_{n}(\rho_{0,n})=1]-\Pr[\mathcal{D}_{n}(\rho_{1,n})=1]\rvert$ is negligible, that is, eventually smaller than $n^{-c}$ for every constant $c\text{.}$</p>
</div>
<div id="S5.SS2.p2" class="ltx_para">
<p class="ltx_p">Brakerski, Canetti and Qian ask whether EFI pairs separate $\mathsf{BQP}$ from $\mathsf{PSPACE}\text{,}$ and they suggest synthesizing the Helstrom measurement with a $\mathsf{PSPACE}$ oracle <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx9" title="" class="ltx_ref">BCQ23</a>, Section 1.2]</cite>. For two states with difference $\Delta\text{,}$ the Helstrom measurement <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx27" title="" class="ltx_ref">Hel76</a>]</cite> accepts on the positive eigenspace of $\Delta$ and has advantage equal to the trace distance. The projector onto this eigenspace depends discontinuously on $\Delta\text{,}$ and we can compute $\Delta$ only approximately. Kretschmer and Tang avoid this with phase estimation of $e^{\mathrm{i}\Delta}\text{,}$ which shows that EFI pairs relative to $A$ separate $\mathsf{unitaryP}^{A}$ from $\mathsf{unitaryPSPACE}^{A}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx37" title="" class="ltx_ref">KT26</a>, Theorem 7.14]</cite>. We instead replace this projector by a smooth function of $\Delta\text{,}$ the POVM element for outcome zero of one Hadamard test.</p>
</div>
<div id="S5.SS2.p3" class="ltx_para">
<p class="ltx_p">Fix a classical oracle $A$ and an integer-valued polynomial $p\geq 1\text{,}$ and let $\rho_{0,n},\rho_{1,n}$ be states on $w=w(n)$ qubits generated by two families of circuits as above. Let $\alpha=1/p(n)$ and $\Delta=\rho_{0,n}-\rho_{1,n}\text{,}$ and let $\tau$ be the largest power of two with $2^{w-1}\tau\leq\alpha/4\text{.}$ Since $\Delta$ is Hermitian, the matrix</p>
<table id="S5.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$W_{n}=(\Delta+\mathrm{i}\tau I)(\Delta^{2}+\tau^{2}I)^{-1/2}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">is unitary. Its Hermitian part $\Delta(\Delta^{2}+\tau^{2}I)^{-1/2}$ is close to the sign of $\Delta$ on eigenvalues of modulus much larger than $\tau\text{.}$ The Hadamard test of $W_{n}$ is the unitary</p>
<table id="S5.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$(H\otimes I)\bigl(\lvert 0\rangle\langle 0\rvert\otimes I+\lvert 1\rangle\langle 1\rvert\otimes W_{n}\bigr)(H\otimes I)$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">on a test qubit and a data register of $w$ qubits. A unitary language has one member of each length, so we fix an integer $c$ with $(n+1)^{c}\geq w+1$ for all $n\geq 1\text{,}$ and let $U_{\Delta}$ be the unitary language whose member of length $(n+1)^{c}$ is this unitary tensored with the identity on the remaining qubits, and whose other members are identities.</p>
</div>
<div id="S5.Thmtheorem3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">With the notation above, the following hold.</span></p>
<ol id="S5.I1" class="ltx_enumerate">
<li id="S5.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(i)</span> 
<div id="S5.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Suppose that </span>$D(\rho_{0,n},\rho_{1,n})\geq\alpha$<span class="ltx_text ltx_font_italic">, and let </span>$C$<span class="ltx_text ltx_font_italic"> be a unitary circuit that implements the member of </span>$U_{\Delta}$<span class="ltx_text ltx_font_italic"> of length </span>$(n+1)^{c}$<span class="ltx_text ltx_font_italic"> on the zero-ancilla subspace with error at most </span>$\alpha/8$<span class="ltx_text ltx_font_italic">. The circuit that applies </span>$C$<span class="ltx_text ltx_font_italic"> to its input on the data register with all other wires at zero, and outputs the test qubit, has advantage at least </span>$\alpha/4$<span class="ltx_text ltx_font_italic"> between </span>$\rho_{0,n}$<span class="ltx_text ltx_font_italic"> and </span>$\rho_{1,n}$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
<li id="S5.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(ii)</span> 
<div id="S5.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The language </span>$U_{\Delta}$<span class="ltx_text ltx_font_italic"> has entries computable in polynomial space relative to </span>$A$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
<li id="S5.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(iii)</span> 
<div id="S5.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">There are a language </span>$B\in\mathsf{PSPACE}^{A}$<span class="ltx_text ltx_font_italic"> and a time-uniform family </span>$(\mathcal{D}_{n})_{n}$<span class="ltx_text ltx_font_italic"> of general quantum circuits over </span>$\mathcal{G}$<span class="ltx_text ltx_font_italic"> with oracle gates </span>$O_{B}$<span class="ltx_text ltx_font_italic"> such that </span>$\mathcal{D}_{n}$<span class="ltx_text ltx_font_italic"> has advantage at least </span>$\alpha/4$<span class="ltx_text ltx_font_italic"> between </span>$\rho_{0,n}$<span class="ltx_text ltx_font_italic"> and </span>$\rho_{1,n}$<span class="ltx_text ltx_font_italic"> whenever </span>$D(\rho_{0,n},\rho_{1,n})\geq\alpha$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
</ol>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS2.p4" class="ltx_para">
<p class="ltx_p">For item (i), the $(0,0)$ block of the Hadamard test on the test qubit is $(I+W_{n})/2\text{,}$ so the test qubit is zero with probability $\operatorname{Tr}(E\rho)$ on an input state $\rho\text{,}$ where</p>
<table id="S5.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E=\Bigl(\frac{I+W_{n}}{2}\Bigr)^{\dagger}\frac{I+W_{n}}{2}=\frac{1}{2}\Bigl(I+\Delta(\Delta^{2}+\tau^{2}I)^{-1/2}\Bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $\operatorname{Tr}\Delta=0\text{,}$ summing over the eigenvalues $\lambda$ of $\Delta$ with multiplicity gives</p>
<table id="S5.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\operatorname{Tr}(E\Delta)=\frac{1}{2}\sum_{\lambda}\frac{\lambda^{2}}{\sqrt{\lambda^{2}+\tau^{2}}}\geq\frac{1}{2}\sum_{\lambda}\bigl(\lvert\lambda\rvert-\tau\bigr)=\frac{1}{2}\lVert\Delta\rVert_{1}-2^{w-1}\tau\geq\frac{3}{4}\alpha,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where the first inequality uses $\sqrt{\lambda^{2}+\tau^{2}}\leq\lvert\lambda\rvert+\tau$ and $\lambda^{2}\geq(\lvert\lambda\rvert-\tau)(\lvert\lambda\rvert+\tau)\text{.}$ Replacing the Hadamard test by $C$ moves the output vector on a pure input by at most $\alpha/8\text{,}$ so it changes each probability by at most $\alpha/4$ on pure inputs (<a href="#S2.SS4" title="2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.4</span></a>) and, by convexity, on mixed inputs. This leaves an advantage of at least $\alpha/4\text{.}$</p>
</div>
<div id="S5.SS2.p5" class="ltx_para">
<p class="ltx_p">For item (ii), all computations below use space polynomial in $n+t$ with oracle $A\text{.}$ A time-uniform family is space-uniform, so by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(vii), for circuits with no input, we can compute the entries of $\rho_{0,n}$ and $\rho_{1,n}\text{,}$ and hence those of $\Delta\text{.}$ Let $X=(1-\tau^{2})I-\Delta^{2}\text{,}$ so that $I-X=\Delta^{2}+\tau^{2}I\text{.}$ Since $0\preceq\Delta^{2}\preceq I$ and $\tau^{2}\leq 1/4\text{,}$ we have $\lVert X\rVert\leq 1-\tau^{2}\text{,}$ and the binomial series of $(1-z)^{-1/2}$ gives</p>
<table id="S5.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$W_{n}=\sum_{j\geq 0}c_{j}(\Delta+\mathrm{i}\tau I)X^{j},\qquad c_{j}=\prod_{r=1}^{j}\frac{2r-1}{2r}\leq 1.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">To compute an entry to precision $t\text{,}$ let $M=\tau^{-2}(t+3+2\log(1/\tau))\text{.}$ Since $\lVert\Delta+\mathrm{i}\tau I\rVert\leq 2\text{,}$ the terms with $j&gt;M$ have total norm at most $2(1-\tau^{2})^{M+1}/\tau^{2}\leq 2\tau^{-2}e^{-M\tau^{2}}\leq 2^{-t-2}\text{.}$ Term $j$ is twice the product of the contractions $(\Delta+\mathrm{i}\tau I)/2$ and $\frac{2r-1}{2r}X$ for $r\leq j\text{,}$ so its entries can be computed by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(v). The space used depends on $j$ only through $\log(j+1)\text{,}$ which is polynomial in $n+t$ for $j\leq M\text{.}$ We compute the entries of the terms with $j\leq M$ to precision $t+\lceil\log(M+1)\rceil+3\text{,}$ so that their errors add up to at most $2^{-t-3}\text{,}$ sum them exactly by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(iii), and round to $t+3$ fractional bits, which adds less than $2^{-t-3}\text{.}$ The total error is below $2^{-t}\text{.}$</p>
</div>
<div id="S5.SS2.p6" class="ltx_para">
<p class="ltx_p">The blocks of the Hadamard test are $(I\pm W_{n})/2\text{,}$ so its entries follow, and at lengths not of the form $(n+1)^{c}$ the entries are those of the identity.</p>
</div>
<div id="S5.SS2.p7" class="ltx_para">
<p class="ltx_p">For item (iii), <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> applied to $U_{\Delta}$ gives $B\in\mathsf{PSPACE}^{A}$ and circuits over $\mathcal{G}\text{.}$ The circuit at length $(n+1)^{c}$ and precision $\lceil\log(8p(n))\rceil$ implements the member on the zero-ancilla subspace with error at most $\alpha/8\text{,}$ so item (i) gives the family $(\mathcal{D}_{n})_{n}\text{.}$
∎</p>
</div>
</div>
<div id="S5.SS2.p8" class="ltx_para">
<p class="ltx_p"><a href="#S1.Thmtheorem4" title="Corollary 1.4. ‣ Quantum cryptography. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.4</span></a> states that if EFI pairs exist relative to a classical oracle $A\text{,}$ then $\mathsf{BQP}^{A}\neq\mathsf{PSPACE}^{A}\text{,}$ and in particular that EFI pairs imply $\mathsf{BQP}\neq\mathsf{PSPACE}\text{.}$</p>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S1.Thmtheorem4" title="Corollary 1.4. ‣ Quantum cryptography. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.4</span></a>.</h6>
<div id="S5.SS2.p9" class="ltx_para">
<p class="ltx_p">Suppose that $\mathsf{BQP}^{A}=\mathsf{PSPACE}^{A}$ and that an EFI pair relative to $A$ exists. Enlarging $p\text{,}$ we may assume that it is integer-valued with $p\geq 1\text{.}$ By <a href="#S5.Thmtheorem3" title="Lemma 5.3. ‣ 5.2 Distinguishing States with a PSPACE Oracle ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.3</span></a>(ii) and <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>, $U_{\Delta}\in\mathsf{unitaryP}^{B}$ for some $B\in\mathsf{PSPACE}^{A}=\mathsf{BQP}^{A}\text{,}$ and then $U_{\Delta}\in\mathsf{unitaryP}^{A}$ by <a href="#S5.Thmtheorem2" title="Corollary 5.2. ‣ 5.1 The Oracle Characterization ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>, in both cases with circuits over $\mathcal{G}\text{.}$ These circuits at length $(n+1)^{c}$ and precision $\lceil\log(8p(n))\rceil$ give, by <a href="#S5.Thmtheorem3" title="Lemma 5.3. ‣ 5.2 Distinguishing States with a PSPACE Oracle ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.3</span></a>(i), a time-uniform family of polynomial size with advantage at least $1/(4p(n))$ for all large $n\text{.}$ This contradicts the definition of an EFI pair. The second statement is the case $A=\emptyset\text{.}$
∎</p>
</div>
</div>
<div id="S5.SS2.p10" class="ltx_para">
<p class="ltx_p">For $A=\emptyset$ this distinguisher is a polynomial-time quantum algorithm over $\mathcal{G}$ with no advice. The corollary therefore also holds for the EFI pairs of Brakerski, Canetti and Qian, whose generators are polynomial-time quantum algorithms and whose distinguishers may have quantum advice <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx9" title="" class="ltx_ref">BCQ23</a>]</cite>. They show that EFI pairs exist if and only if commitment schemes do <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx9" title="" class="ltx_ref">BCQ23</a>, Theorem 13]</cite>, building on <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx57" title="" class="ltx_ref">Yan22</a>]</cite>, so computationally hiding and binding quantum commitments also imply $\mathsf{BQP}\neq\mathsf{PSPACE}\text{.}$</p>
</div>
<div id="S5.SS2.p11" class="ltx_para">
<p class="ltx_p">The same argument breaks single-copy pseudorandom states that are longer than their key <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx34" title="" class="ltx_ref">KQST23</a>, Definition 7]</cite>. These are pure states $\lvert\psi_{k}\rangle$ on $q(n)&gt;n$ qubits, for keys $k\in\{0,1\}^{n}\text{,}$ generated in polynomial time, such that polynomial-time quantum adversaries cannot distinguish one copy of $\lvert\psi_{k}\rangle$ for a random key from one copy of a Haar-random state. The average $\rho_{n}$ of $\lvert\psi_{k}\rangle\langle\psi_{k}\rvert$ over the keys has rank at most $2^{n}\text{,}$ and the average of a Haar-random state is $I/2^{q(n)}\text{.}$ With $\Pi_{\rho_{n}}$ the projector onto the support of $\rho_{n}\text{,}$ their trace distance is at least $\operatorname{Tr}(\Pi_{\rho_{n}}(\rho_{n}-I/2^{q(n)}))\geq 1-2^{n-q(n)}\geq 1/2\text{.}$ Both are generated by time-uniform families, so <a href="#S5.Thmtheorem3" title="Lemma 5.3. ‣ 5.2 Distinguishing States with a PSPACE Oracle ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.3</span></a>(iii) with $p=2$ gives a uniform distinguisher with a $\mathsf{PSPACE}$ oracle and advantage at least $1/8\text{.}$ Lombardi, Ma and Wright ask whether a $\mathsf{PSPACE}$ oracle breaks every single-copy pseudorandom state <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>, Section 1.1]</cite>, and for states longer than their key it does. Under $\mathsf{BQP}=\mathsf{PSPACE}\text{,}$ <a href="#S5.Thmtheorem2" title="Corollary 5.2. ‣ 5.1 The Oracle Characterization ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">5.2</span></a> removes the oracle from this distinguisher, so the existence of these states implies $\mathsf{BQP}\neq\mathsf{PSPACE}\text{,}$ and hence $\mathsf{P}\neq\mathsf{PSPACE}\text{,}$ as asked in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx34" title="" class="ltx_ref">KQST23</a>, Section 1.4]</cite>.</p>
</div>
</section>
<section id="S5.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="a-polynomial-query-adversary-for-the-oracle-state-distinguishing-game">
<span class="ltx_tag ltx_tag_subsection">5.3 </span>A Polynomial-Query Adversary for the Oracle State Distinguishing Game</h3>

<div id="S5.SS3.p1" class="ltx_para">
<p class="ltx_p">Lombardi, Ma and Wright study the Unitary Synthesis Problem through the following game <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>, Definition 1.3]</cite>. For $f\colon\{0,1\}^{\ell}\to\{0,1\}\text{,}$ write $Z_{f}\lvert u\rangle=(-1)^{f(u)}\lvert u\rangle$ for its phase unitary and $\lvert\varphi_{f}\rangle=2^{-\ell/2}\sum_{u}(-1)^{f(u)}\lvert u\rangle$ for its binary phase state. A uniformly random family $R=(R_{k})_{k}$ of Boolean functions on $\{0,1\}^{n}\text{,}$ indexed by keys, is drawn. A challenger sends the adversary $\lvert\varphi_{R_{k}}\rangle$ for a uniformly random key $k\text{,}$ or $\lvert\varphi_{f}\rangle$ for a uniformly random function $f\text{,}$ each with probability $1/2\text{,}$ and the adversary must output which of the two it received. The adversary is an oracle circuit, fixed before $R\text{,}$ whose queries apply the phase unitary of a Boolean function that may depend on $R$ arbitrarily.</p>
</div>
<div id="S5.SS3.p2" class="ltx_para">
<p class="ltx_p">The Strong Non-Synthesis Conjecture <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>, Conjecture 1.5]</cite> states that whenever the number of keys is superpolynomial in $n\text{,}$ every polynomial-query adversary wins with probability at most $1/2+\mathrm{negl}(n)\text{,}$ and its authors note that it would imply a negative answer to the Unitary Synthesis Problem. Because the queried Boolean function may depend on $R\text{,}$ it may encode a unitary built from $R\text{,}$ so <a href="#S1.Thmtheorem2" title="Corollary 1.2. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.2</span></a> supplies the implementation that the reduction of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>, Section 3.3]</cite> needs.</p>
</div>
<div id="S5.Thmtheorem4" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Proposition 5.4</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For the key set $\{0,1\}^{n-1}\text{,}$ there is a polynomial-query oracle circuit such that, for every $R\text{,}$ there is a Boolean function $f_{R}$ for which the circuit with queries to $f_{R}$ wins the game with probability at least $11/16\text{.}$ Hence the Strong Non-Synthesis Conjecture is false.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS3.p3" class="ltx_para">
<p class="ltx_p">Fix $n$ and $R\text{.}$ The states $\lvert\varphi_{R_{k}}\rangle$ span a subspace $\mathcal{H}_{R}$ of dimension at most $2^{n-1}\text{,}$ so there is a unitary $T_{R}$ on $n$ qubits that maps $\mathcal{H}_{R}$ into the span of the basis states with first qubit zero. Applying $T_{R}$ and outputting the first qubit gives zero with certainty on $\lvert\varphi_{R_{k}}\rangle\text{.}$ A uniformly random function gives the average state $I/2^{n}\text{,}$ since $(-1)^{f(u)+f(u^{\prime})}$ has expectation zero for $u\neq u^{\prime}\text{,}$ and $T_{R}$ preserves this state, so the output is then zero with probability $1/2\text{.}$ Applying $T_{R}$ would therefore win the game with probability $3/4\text{.}$</p>
</div>
<div id="S5.SS3.p4" class="ltx_para">
<p class="ltx_p">To approximate $T_{R}$ with queries, let $B_{R}$ be the language of <a href="#S1.Thmtheorem2" title="Corollary 1.2. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.2</span></a> for the unitary language with member $T_{R}$ at length $n$ and identities at other lengths, and let $C$ be its circuit at $(1^{n},1^{5})\text{.}$ The algorithm that produces $C$ does not depend on the unitary language, so $C$ does not depend on $R\text{.}$ The queries of an oracle circuit in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>, Definition 3.4]</cite> have one length, so let $\ell$ exceed the query lengths of all oracle gates of $C\text{,}$ and pad a query string $x$ to $x^{\prime}=x10^{\ell-\lvert x\rvert-1}\text{.}$ Let $f_{R}(x^{\prime},b)=b\cdot B_{R}(x)$ for a bit $b\text{,}$ and let $f_{R}$ be zero on all other strings of length $\ell+1\text{.}$ Then $Z_{f_{R}}\lvert x^{\prime},b\rangle=(-1)^{b\,B_{R}(x)}\lvert x^{\prime},b\rangle\text{,}$ so with the padding on ancillas, $Z_{f_{R}}$ conjugated by $H$ on the qubit of $b$ acts as the gate $O_{B_{R}}\text{,}$ as in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>, Remark 3.6]</cite>.</p>
</div>
<div id="S5.SS3.p5" class="ltx_para">
<p class="ltx_p">The adversary runs $C$ on the challenge and zero ancillas with each oracle gate replaced in this way, and outputs the first qubit. The circuit $C^{B_{R}}$ is within $2^{-5}$ of an extension of $T_{R}\text{,}$ which changes each probability by at most $1/16\text{,}$ so the adversary wins with probability at least $3/4-1/16=11/16\text{.}$ The number $2^{n-1}$ of keys is superpolynomial in $n\text{,}$ so this contradicts the conjecture.
∎</p>
</div>
</div>
<div id="S5.SS3.p6" class="ltx_para">
<p class="ltx_p">This adversary makes polynomially many sequential queries, whereas the lower bounds of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx39" title="" class="ltx_ref">LMW24</a>]</cite> concern one query and, through their Remark 3.6, polynomially many parallel queries.</p>
</div>
</section>
</section>
<section id="S6" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-channel-model">
<span class="ltx_tag ltx_tag_section">6 </span>The Channel Model</h2>

<div id="S6.p1" class="ltx_para">
<p class="ltx_p">Bostanci, Efron, Metger, Poremba, Qian and Yuen pose their questions about the collapse of unitary classes and about interactive proofs for unitaries in the channel model of <a href="#S2.SS5" title="2.5 Unitary Synthesis Problems and the Channel-Model Classes ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.5</span></a> <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>]</cite>. To answer them we need the counterpart of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main theorem). ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> in this model, namely polynomial-time circuits with a $\mathsf{PSPACE}$ oracle for the problems in $\mathsf{unitaryPSPACE}^{\diamond}\text{.}$</p>
</div>
<div id="S6.p2" class="ltx_para">
<p class="ltx_p">Such circuits exist only for size-computable problems, because every problem in $\mathsf{unitaryBQP}^{\diamond,L}\text{,}$ for any language $L\text{,}$ is size-computable: its generator runs in polynomial time with no oracle and writes the input and output wires of its circuit at $(x,1^{1})\text{.}$ The register sizes of a problem in $\mathsf{unitaryPSPACE}^{\diamond}\text{,}$ however, can encode a language in $\mathsf{PSPACE}\text{.}$</p>
</div>
<div id="S6.Thmtheorem1" class="ltx_theorem ltx_theorem_example">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Example 6.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p">Let $L^{\prime}\in\mathsf{PSPACE}\text{,}$ and let $U_{x}\lvert\psi\rangle=\lvert\psi\rangle\lvert 0^{L^{\prime}(x)}\rangle$ from one qubit to $1+L^{\prime}(x)$ qubits. This problem lies in $\mathsf{unitaryPSPACE}^{\diamond}$ with error zero: a generator decides $L^{\prime}(x)$ in polynomial space and writes the circuit that adds $L^{\prime}(x)$ new qubits. It is size-computable only if $L^{\prime}\in\mathsf{P}\text{.}$</p>
</div>
</div>
<section id="S6.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="implementing-channels-with-a-pspace-oracle">
<span class="ltx_tag ltx_tag_subsection">6.1 </span>Implementing Channels with a PSPACE Oracle</h3>

<div id="S6.Thmtheorem2" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 6.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $U\in\mathsf{unitaryPSPACE}^{\diamond}$ be size-computable. There is a language $B\in\mathsf{PSPACE}$ with $U\in\mathsf{unitaryBQP}^{\diamond,B}\text{.}$</span></p>
</div>
</div>
<div id="S6.SS1.p1" class="ltx_para">
<p class="ltx_p">A circuit of this model implements a channel, while <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> concerns unitaries. A space-uniform circuit may discard exponentially many qubits, so keeping them does not give a unitary on polynomially many qubits. The channel, however, acts on polynomially many qubits, and by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(vii) its matrix representation can be computed in polynomial space. So we write down a Stinespring isometry of the channel in terms of this matrix, with an environment of polynomially many qubits, and embed it in a unitary whose entries are computable in polynomial space. <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> then applies to this unitary.</p>
</div>
<div id="S6.SS1.p2" class="ltx_para">
<p class="ltx_p">Let $(\mathcal{C}_{x,r})_{x,r}$ be a space-uniform family of general quantum circuits of space polynomial in $\lvert x\rvert+r\text{,}$ with input register $\mathsf{A}_{x}$ of $n_{\mathrm{in}}=n_{\mathrm{in}}(x)$ qubits and output register $\mathsf{B}_{x}$ of $n_{\mathrm{out}}=n_{\mathrm{out}}(x)$ qubits. Fix $x$ and $r\text{,}$ and write $\mathcal{C}=\mathcal{C}_{x,r}$ and $d_{\mathrm{in}}=2^{n_{\mathrm{in}}}\text{.}$ A Stinespring isometry of a channel $\mathcal{N}$ is an isometry $Y$ into its output register and an environment $\mathsf{E}$ with $\mathcal{N}(\rho)=\operatorname{Tr}_{\mathsf{E}}(Y\rho Y^{\dagger})\text{.}$ To obtain one for $\mathcal{C}$ we use its Choi matrix <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx17" title="" class="ltx_ref">Cho75</a>]</cite></p>
<table id="S6.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$J_{\mathcal{C}}=\sum_{u,u^{\prime}}\lvert u\rangle\langle u^{\prime}\rvert\otimes\mathcal{C}(\lvert u\rangle\langle u^{\prime}\rvert).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Its entries are $\langle u,v\rvert J_{\mathcal{C}}\lvert u^{\prime},v^{\prime}\rangle=\langle v\rvert\mathcal{C}(\lvert u\rangle\langle u^{\prime}\rvert)\lvert v^{\prime}\rangle\text{,}$ and it is positive semidefinite, because it is $\mathrm{id}\otimes\mathcal{C}$ applied to the positive semidefinite matrix $\sum_{u,u^{\prime}}\lvert u,u\rangle\langle u^{\prime},u^{\prime}\rvert\text{.}$</p>
</div>
<div id="S6.Thmtheorem3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 6.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $\mathsf{E}$ be a register of $n_{\mathrm{in}}+n_{\mathrm{out}}$ qubits, with basis indices $i$ as for $\mathsf{A}_{x}\mathsf{B}_{x}\text{.}$ The map $Y\colon\mathsf{A}_{x}\to\mathsf{B}_{x}\mathsf{E}$ with $\langle v,i\rvert Y\lvert u\rangle=\langle u,v\rvert\sqrt{J_{\mathcal{C}}}\lvert i\rangle$ is a Stinespring isometry of $\mathcal{C}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS1.p3" class="ltx_para">
<p class="ltx_p">Since $\sqrt{J_{\mathcal{C}}}$ is Hermitian,</p>
<table id="S6.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\langle v\rvert\operatorname{Tr}_{\mathsf{E}}(Y\lvert u\rangle\langle u^{\prime}\rvert Y^{\dagger})\lvert v^{\prime}\rangle=\sum_{i}\langle u,v\rvert\sqrt{J_{\mathcal{C}}}\lvert i\rangle\langle i\rvert\sqrt{J_{\mathcal{C}}}\lvert u^{\prime},v^{\prime}\rangle=\langle u,v\rvert J_{\mathcal{C}}\lvert u^{\prime},v^{\prime}\rangle=\langle v\rvert\mathcal{C}(\lvert u\rangle\langle u^{\prime}\rvert)\lvert v^{\prime}\rangle.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Thus $\operatorname{Tr}_{\mathsf{E}}(Y\rho Y^{\dagger})=\mathcal{C}(\rho)$ for every matrix $\rho\text{.}$ Since $\mathcal{C}$ preserves the trace, this gives $\operatorname{Tr}(Y^{\dagger}Y\rho)=\operatorname{Tr}\rho$ for every $\rho\text{,}$ that is, $Y^{\dagger}Y=I\text{.}$
∎</p>
</div>
</div>
<div id="S6.SS1.p4" class="ltx_para">
<p class="ltx_p">To embed $Y$ in a unitary, let the first $n_{\mathrm{out}}$ wires of $\mathsf{B}_{x}\mathsf{E}$ be those of $\mathsf{B}_{x}\text{,}$ and let $\iota\colon\mathsf{A}_{x}\to\mathsf{B}_{x}\mathsf{E}$ place the input on the first $n_{\mathrm{in}}$ wires, $\iota\lvert\psi\rangle=\lvert\psi\rangle\lvert 0^{2n_{\mathrm{out}}}\rangle\text{.}$ With one further qubit $\mathsf{F}\text{,}$ the isometries $\lvert 0\rangle\otimes\iota$ and $\lvert 1\rangle\otimes Y$ have orthogonal ranges, and a reflection exchanges them. Indeed, let</p>
<table id="S6.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Z=\lvert 0\rangle\otimes\iota-\lvert 1\rangle\otimes Y,\qquad W=I-ZZ^{\dagger}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Then $Z^{\dagger}Z=2I\text{,}$ so $W$ is a reflection, and $Z^{\dagger}(\lvert 0\rangle\otimes\iota\lvert\psi\rangle)=\lvert\psi\rangle$ gives</p>
<table id="S6.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$W(\lvert 0\rangle\otimes\iota\lvert\psi\rangle)=\lvert 0\rangle\otimes\iota\lvert\psi\rangle-Z\lvert\psi\rangle=\lvert 1\rangle\otimes Y\lvert\psi\rangle.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Hence applying $W$ to an input placed by $\iota$ and keeping only the wires of $\mathsf{B}_{x}$ implements $\mathcal{C}$ exactly. It remains to compute the entries of $W\text{.}$ We say that a quantity is computable in polynomial space if it can be computed to precision $t\text{,}$ with $O(t+1)$ bits per component, in space polynomial in $\lvert x\rvert+r+t\text{.}$</p>
</div>
<div id="S6.Thmtheorem4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 6.4</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The entries of $W$ are computable in polynomial space.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS1.p5" class="ltx_para">
<p class="ltx_p">The main step is the square root of $J_{\mathcal{C}}\text{,}$ which we obtain from the binomial series of $\sqrt{1-z}$ applied to a matrix between $0$ and $I\text{.}$ By <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(vii) the entries of $J_{\mathcal{C}}$ are computable in polynomial space, and $\operatorname{Tr}J_{\mathcal{C}}=\sum_{u}\operatorname{Tr}\mathcal{C}(\lvert u\rangle\langle u\rvert)=d_{\mathrm{in}}\text{,}$ so $X=I-d_{\mathrm{in}}^{-1}J_{\mathcal{C}}$ satisfies $0\preceq X\preceq I$ and $\sqrt{J_{\mathcal{C}}}=2^{n_{\mathrm{in}}/2}\sqrt{I-X}\text{.}$</p>
</div>
<div id="S6.SS1.p6" class="ltx_para">
<p class="ltx_p">Let $c_{k}=\prod_{j=1}^{k}\frac{2j-1}{2j}\text{.}$ For $0\leq z&lt;1\text{,}$ Newton’s binomial series gives</p>
<table id="S6.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\sqrt{1-z}=1-\sum_{k\geq 1}\frac{c_{k-1}}{2k}z^{k}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $\frac{c_{k-1}}{2k}=c_{k-1}-c_{k}\text{,}$ the coefficients are positive and those with $k\leq M$ sum to $1-c_{M}\text{.}$ From $(2j-1)(2j+1)\leq(2j)^{2}$ we get $c_{M}^{2}\leq\prod_{j\leq M}\frac{2j-1}{2j+1}=\frac{1}{2M+1}\text{.}$ So the coefficients sum to one, the identity holds also at $z=1\text{,}$ and the terms with $k&gt;M$ sum to at most $c_{M}$ for all $0\leq z\leq 1\text{.}$ Applying this to the eigenvalues of $X$ with $M=4^{t+3}$ gives</p>
<table id="S6.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Bigl\lVert\sqrt{I-X}-I+\sum_{k=1}^{M}\frac{c_{k-1}}{2k}X^{k}\Bigr\rVert\leq c_{M}&lt;2^{-t-3}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The number of terms is exponential in $t\text{,}$ but the space used by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(v) and (iii) depends on it only through its logarithm. Term $k$ is the product of $X/(2k)$ and the matrices $\frac{2j-1}{2j}X$ for $j&lt;k\text{.}$ Every product of consecutive factors is a number in $[0,1]$ times a power of $X\text{,}$ so its entries have modulus at most one, and by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(v) the entries of term $k$ can be computed in polynomial space. Computing each term to precision $t+\log M+3\text{,}$ summing exactly by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(iii) and rounding to $t+3$ fractional bits gives the entries of $\sqrt{I-X}$ with error below $2^{-t}\text{,}$ since the truncation, the combined error of the $M$ computed terms and the rounding each contribute at most $2^{-t-3}\text{.}$</p>
</div>
<div id="S6.SS1.p7" class="ltx_para">
<p class="ltx_p">The entries of $Y$ are entries of $\sqrt{J_{\mathcal{C}}}=2^{n_{\mathrm{in}}/2}\sqrt{I-X}\text{,}$ so they are computable in polynomial space by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(ii). The entries of $Z$ are entries of $\iota$ or of $-Y\text{,}$ and an entry of $ZZ^{\dagger}$ is a sum of $d_{\mathrm{in}}$ products of entries of $Z$ and their conjugates, so it can be computed by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(iii).
∎</p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S6.Thmtheorem2" title="Theorem 6.2. ‣ 6.1 Implementing Channels with a PSPACE Oracle ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.2</span></a>.</h6>
<div id="S6.SS1.p8" class="ltx_para">
<p class="ltx_p"><a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> concerns one unitary for each length, while we have one unitary $W$ for each instance and precision, so we collect them with a control register. Let $(\mathcal{C}_{x,r})_{x,r}$ be a family for $U\text{.}$ For $r\geq 1\text{,}$ let $y=1^{r}0x$ encode $(x,1^{r})\text{,}$ and let $W_{y}$ be the unitary $W$ for $\mathcal{C}_{x,r}\text{.}$ For all other strings $y\text{,}$ let $W_{y}$ be the identity. Since $n_{\mathrm{in}}$ and $n_{\mathrm{out}}$ are polynomially bounded, we can fix an integer $c$ such that $(\lvert y\rvert+1)^{c}$ wires hold $\lvert y\rvert$ control wires and the wires of $W_{y}\text{,}$ for all $y\text{.}$ Let $U_{\mathcal{C}}$ be the unitary language whose member of length $(\ell+1)^{c}\text{,}$ for $\ell\geq 1\text{,}$ is</p>
<table id="S6.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\bigoplus_{y\in\{0,1\}^{\ell}}W_{y}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">on $\ell$ control wires and the remaining data wires, where $W_{y}$ acts on the first data wires, which are $\mathsf{F}$ followed by $\mathsf{B}_{x}\mathsf{E}\text{.}$ Its members of all other lengths are identities. An entry of a member is zero if its two control strings differ, and otherwise it is an entry of $W_{y}\otimes I\text{,}$ given by <a href="#S6.Thmtheorem4" title="Lemma 6.4. ‣ 6.1 Implementing Channels with a PSPACE Oracle ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">6.4</span></a>. Thus $U_{\mathcal{C}}$ has entries computable in polynomial space in the sense of <a href="#S2.Thmtheorem4" title="Definition 2.4. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Definition</span> <span class="ltx_text ltx_ref_tag">2.4</span></a>, and <a href="#S3.Thmtheorem1" title="Theorem 3.1. ‣ 3 Implementing Unitaries from Their Entries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.1</span></a> with $A=\emptyset$ gives $B\in\mathsf{PSPACE}$ and time-uniform circuits $C_{n,m}$ over $\mathcal{G}$ such that $\lVert C^{B}_{n,m}-\widetilde{U}\rVert\leq 2^{-m}$ for some extension $\widetilde{U}$ of the member of length $n\text{.}$</p>
</div>
<div id="S6.SS1.p9" class="ltx_para">
<p class="ltx_p">Given $(x,1^{r})\text{,}$ let $y=1^{2r}0x\text{,}$ $n=(\lvert y\rvert+1)^{c}$ and $m=\lceil\log r\rceil+2\text{.}$ The general quantum circuit $\mathcal{C}^{\prime}_{x,r}$ has as input wires the first $n_{\mathrm{in}}$ wires of $\mathsf{B}_{x}\mathsf{E}\text{,}$ and all other wires of $C_{n,m}$ are new qubits. It sets the control register to $\lvert y\rangle$ by NOT gates, runs $C_{n,m}\text{,}$ and discards all wires except the first $n_{\mathrm{out}}$ wires of $\mathsf{B}_{x}\mathsf{E}\text{,}$ which are its output wires. Since the problem is size-computable and $(C_{n,m})_{n,m}$ is time-uniform, the family $(\mathcal{C}^{\prime}_{x,r})_{x,r}$ is time-uniform.</p>
</div>
<div id="S6.SS1.p10" class="ltx_para">
<p class="ltx_p">With the extension $\widetilde{U}$ in place of $C^{B}_{n,m}\text{,}$ this circuit applies $W_{y}$ with all ancillas at zero, so it implements $\mathcal{C}_{x,2r}$ exactly. Since $\lVert C^{B}_{n,m}-\widetilde{U}\rVert\leq 2^{-m}\text{,}$ we get $\lVert\mathcal{C}^{\prime}_{x,r}-\mathcal{C}_{x,2r}\rVert_{\diamond}\leq 2^{1-m}\leq 1/(2r)$ (<a href="#S2.SS4" title="2.4 Approximation of Unitaries and Channels ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2.4</span></a>). Some channel completion $\Phi$ of $U_{x}$ satisfies $\lVert\mathcal{C}_{x,2r}-\Phi\rVert_{\diamond}\leq 1/(2r)\text{,}$ so $\lVert\mathcal{C}^{\prime}_{x,r}-\Phi\rVert_{\diamond}\leq 1/r\text{.}$
∎</p>
</div>
</div>
</section>
<section id="S6.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-collapse-criterion">
<span class="ltx_tag ltx_tag_subsection">6.2 </span>The Collapse Criterion</h3>

<div id="S6.SS2.p1" class="ltx_para">
<p class="ltx_p">The collapse question of <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Section 1.4]</cite> is whether $\mathsf{P}=\mathsf{PSPACE}$ can fail to imply $\mathsf{unitaryBQP}^{\diamond}=\mathsf{unitaryPSPACE}^{\diamond}\text{,}$ and <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Open Problem 4]</cite> asks whether these classes can be separated unconditionally. On size-computable problems the criterion is that of <a href="#S1.Thmtheorem3" title="Corollary 1.3. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">1.3</span></a>. On all problems the register sizes add one requirement, since they must be computable in polynomial time in $\mathsf{unitaryBQP}^{\diamond}\text{,}$ but only in polynomial space in $\mathsf{unitaryPSPACE}^{\diamond}\text{.}$</p>
</div>
<div id="S6.Thmtheorem5" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 6.5</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The following hold in the channel model.</span></p>
<ol id="S6.I1" class="ltx_enumerate">
<li id="S6.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(i)</span> 
<div id="S6.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every language </span>$L$<span class="ltx_text ltx_font_italic">, every size-computable problem in </span>$\mathsf{unitaryPSPACE}^{\diamond}$<span class="ltx_text ltx_font_italic"> lies in </span>$\mathsf{unitaryBQP}^{\diamond,L}$<span class="ltx_text ltx_font_italic"> if and only if </span>$\mathsf{PSPACE}\subseteq\mathsf{BQP}^{L}$<span class="ltx_text ltx_font_italic">. In particular, the size-computable problems in </span>$\mathsf{unitaryPSPACE}^{\diamond}$<span class="ltx_text ltx_font_italic"> all lie in </span>$\mathsf{unitaryBQP}^{\diamond}$<span class="ltx_text ltx_font_italic"> if and only if </span>$\mathsf{BQP}=\mathsf{PSPACE}$<span class="ltx_text ltx_font_italic">, and they all lie in </span>$\mathsf{unitaryBQP}^{\diamond,K}$<span class="ltx_text ltx_font_italic"> for every </span>$\mathsf{PSPACE}$<span class="ltx_text ltx_font_italic">-complete language </span>$K$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
<li id="S6.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(ii)</span> 
<div id="S6.I1.i2.p1" class="ltx_para">
<p class="ltx_p">$\mathsf{unitaryBQP}^{\diamond}=\mathsf{unitaryPSPACE}^{\diamond}$<span class="ltx_text ltx_font_italic"> if and only if </span>$\mathsf{P}=\mathsf{PSPACE}$<span class="ltx_text ltx_font_italic">.</span></p>
</div>
</li>
</ol>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.SS2.p2" class="ltx_para">
<p class="ltx_p">For (i), suppose that $\mathsf{PSPACE}\subseteq\mathsf{BQP}^{L}\text{,}$ and let $U\in\mathsf{unitaryPSPACE}^{\diamond}$ be size-computable. The proof of <a href="#S6.Thmtheorem2" title="Theorem 6.2. ‣ 6.1 Implementing Channels with a PSPACE Oracle ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.2</span></a> gives a unitary language $U_{\mathcal{C}}\in\mathsf{unitaryP}^{B}$ with circuits over $\mathcal{G}\text{,}$ for some $B\in\mathsf{PSPACE}\subseteq\mathsf{BQP}^{L}\text{.}$ By <a href="#S5.Thmtheorem2" title="Corollary 5.2. ‣ 5.1 The Oracle Characterization ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>, $U_{\mathcal{C}}\in\mathsf{unitaryP}^{L}$ with circuits over $\mathcal{G}\text{.}$ The rest of that proof applies to these circuits and gives a time-uniform family for $U$ with oracle gates $O_{L}\text{.}$</p>
</div>
<div id="S6.SS2.p3" class="ltx_para">
<p class="ltx_p">Conversely, suppose that every size-computable problem in $\mathsf{unitaryPSPACE}^{\diamond}$ lies in $\mathsf{unitaryBQP}^{\diamond,L}\text{,}$ and let $L^{\prime}\in\mathsf{PSPACE}\text{.}$ Let $U_{x}$ be the oracle gate $O_{L^{\prime}}$ on $\lvert x\rvert$ query qubits and one answer qubit, so that the circuits for $U_{1^{n}}$ decide $L^{\prime}$ on strings of length $n\text{.}$ A generator can enumerate the strings $z$ of length $\lvert x\rvert$ and, for each $z\in L^{\prime}\text{,}$ write a NOT on the answer qubit controlled on the query register being $z\text{,}$ by Toffoli and NOT gates with ancillas that return to zero. Thus $U$ is size-computable and lies in $\mathsf{unitaryPSPACE}^{\diamond}$ with error zero, so it has a time-uniform family with oracle gates $O_{L}\text{.}$ The only channel completion of the unitary $U_{x}$ is its unitary channel. Hence, for $z\in\{0,1\}^{n}\text{,}$ the output state $\rho$ of the circuit at $(1^{n},1^{8})$ on input $\lvert z,0\rangle$ satisfies $D(\rho,\lvert z,L^{\prime}(z)\rangle\langle z,L^{\prime}(z)\rvert)\leq 1/16\text{,}$ and measuring the answer qubit gives $L^{\prime}(z)$ except with probability at most $1/16\text{.}$ These circuits form a time-uniform family indexed by $1^{n}\text{,}$ so $L^{\prime}\in\mathsf{BQP}^{L}\text{.}$</p>
</div>
<div id="S6.SS2.p4" class="ltx_para">
<p class="ltx_p">The statement about $\mathsf{BQP}=\mathsf{PSPACE}$ is the case $L=\emptyset\text{,}$ since $\mathsf{BQP}\subseteq\mathsf{PSPACE}$ by <a href="#S2.Thmtheorem6" title="Lemma 2.6. ‣ 2.3 Entries Computable in Polynomial Space ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.6</span></a>(vii). For a $\mathsf{PSPACE}$-complete language $K$ we have $\mathsf{PSPACE}\subseteq\mathsf{P}^{K}\subseteq\mathsf{BQP}^{K}\text{.}$</p>
</div>
<div id="S6.SS2.p5" class="ltx_para">
<p class="ltx_p">For (ii), a time-uniform family is space-uniform, so $\mathsf{unitaryBQP}^{\diamond}\subseteq\mathsf{unitaryPSPACE}^{\diamond}\text{.}$ Suppose that $\mathsf{P}=\mathsf{PSPACE}\text{,}$ and let $U\in\mathsf{unitaryPSPACE}^{\diamond}\text{.}$ Counting the wires in the input and output lists that the generator writes on $(x,1^{1})$ computes $n_{\mathrm{in}}(x)$ and $n_{\mathrm{out}}(x)$ in polynomial space. So each bit of these numbers is decided by a language in $\mathsf{PSPACE}=\mathsf{P}\text{,}$ and $U$ is size-computable. Since $\mathsf{PSPACE}=\mathsf{P}\subseteq\mathsf{BQP}\text{,}$ part (i) gives $U\in\mathsf{unitaryBQP}^{\diamond}\text{.}$ Conversely, if the two classes are equal and $L^{\prime}\in\mathsf{PSPACE}\text{,}$ then the problem of <a href="#S6.Thmtheorem1" title="Example 6.1. ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Example</span> <span class="ltx_text ltx_ref_tag">6.1</span></a> lies in $\mathsf{unitaryBQP}^{\diamond}\text{,}$ so it is size-computable and $L^{\prime}\in\mathsf{P}\text{.}$
∎</p>
</div>
</div>
<div id="S6.Thmtheorem6" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 6.6</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S6.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p">By <a href="#S6.Thmtheorem5" title="Theorem 6.5. ‣ 6.2 The Collapse Criterion ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.5</span></a>(ii), $\mathsf{P}=\mathsf{PSPACE}$ does imply $\mathsf{unitaryBQP}^{\diamond}=\mathsf{unitaryPSPACE}^{\diamond}\text{,}$ and separating these classes is the same as proving $\mathsf{P}\neq\mathsf{PSPACE}\text{.}$ The possibility raised in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Section 3.7]</cite> that the classes differ while $\mathsf{BQP}=\mathsf{PSPACE}$ occurs exactly when $\mathsf{BQP}=\mathsf{PSPACE}\neq\mathsf{P}\text{,}$ and then only problems that are not size-computable separate them.</p>
</div>
</div>
</section>
</section>
<section id="S7" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="interactive-synthesis-1">
<span class="ltx_tag ltx_tag_section">7 </span>Interactive Synthesis</h2>

<div id="S7.p1" class="ltx_para">
<p class="ltx_p">By <a href="#S6.Thmtheorem2" title="Theorem 6.2. ‣ 6.1 Implementing Channels with a PSPACE Oracle ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.2</span></a>, a size-computable problem in $\mathsf{unitaryPSPACE}^{\diamond}$ can be implemented in polynomial time with a language in $\mathsf{PSPACE}$ as an oracle. A polynomial-time verifier can also obtain the results of polynomial-space computations by interacting with an untrusted prover. For decision problems this gives exactly polynomial space <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx30" title="" class="ltx_ref">JJUW11</a>]</cite>, and the same holds for preparing states <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx47" title="" class="ltx_ref">RY22</a>; <a href="#bib.bibx41" title="" class="ltx_ref">MY23</a>]</cite> and for unitaries in the average case, where the input is one register of a given state that can be prepared in polynomial space <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Theorem 7.10]</cite>. For size-computable problems, <a href="#S1.Thmtheorem5" title="Theorem 1.5. ‣ Interactive synthesis. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.5</span></a> answers the worst-case question posed in <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Open Problem 10]</cite>: such a problem lies in $\mathsf{unitaryPSPACE}^{\diamond}$ if and only if it lies in $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}\text{.}$</p>
</div>
<div id="S7.p2" class="ltx_para">
<p class="ltx_p">The difficulty in the worst case is that the verifier holds the only copy of its input, and a prover that receives this copy could alter it without being detected <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Remark 4.2]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx44" title="" class="ltx_ref">Ros23</a>, Section 1.4.2]</cite>. Our verifier never sends its input. It runs a circuit of <a href="#S6.Thmtheorem2" title="Theorem 6.2. ‣ 6.1 Implementing Channels with a PSPACE Oracle ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.2</span></a> on its own qubits and uses the prover only for the oracle gates, so the inclusion in $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}$ follows from the next theorem, which answers <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx44" title="" class="ltx_ref">Ros23</a>, Open Problem 29]</cite>.</p>
</div>
<div id="S7.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 7.1</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $L^{\prime}\in\mathsf{PSPACE}\text{.}$ Every problem in $\mathsf{unitaryBQP}^{\diamond,L^{\prime}}$ lies in $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}\text{.}$</span></p>
</div>
</div>
<div id="S7.p3" class="ltx_para">
<p class="ltx_p">The oracle gate $O_{L^{\prime}}$ is a phase unitary up to Hadamard gates, and the phase state of its function can be prepared in polynomial space, so interactive state synthesis lets the verifier obtain this state from the prover. The verifier consumes the state by state injection, which applies the phase unitary to the verifier’s own qubits up to a correction (<a href="#S7.SS1" title="7.1 State Injection ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7.1</span></a>). The remaining problem is that the verifier obtains many such states from one prover, which keeps its memory between the calls, and that acceptance in a single call can have small probability. Because the target states are pure, the subnormalized state on acceptance is close to a product with the prover’s memory, however small the acceptance probability, and this lets us compare a whole run with a run in which all phase states are exact (<a href="#S7.SS2" title="7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7.2</span></a>).</p>
</div>
<section id="S7.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="state-injection">
<span class="ltx_tag ltx_tag_subsection">7.1 </span>State Injection</h3>

<div id="S7.SS1.p1" class="ltx_para">
<p class="ltx_p">For $f\colon\{0,1\}^{\ell}\to\{0,1\}\text{,}$ recall from <a href="#S5.SS3" title="5.3 A Polynomial-Query Adversary for the Oracle State Distinguishing Game ‣ 5 Oracle Characterization and Cryptography ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5.3</span></a> the phase unitary $Z_{f}\lvert u\rangle=(-1)^{f(u)}\lvert u\rangle$ and the binary phase state $\lvert\varphi_{f}\rangle=2^{-\ell/2}\sum_{u}(-1)^{f(u)}\lvert u\rangle\text{.}$ To inject $\lvert\varphi_{f}\rangle$ into an $\ell$-qubit register $\mathsf{X}\text{,}$ we apply a CNOT from each qubit of $\mathsf{X}$ onto the corresponding qubit of a register $\mathsf{C}$ holding the resource state $\lvert\varphi_{f}\rangle\text{,}$ and we measure $\mathsf{C}$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx60" title="" class="ltx_ref">ZLC00</a>; <a href="#bib.bibx23" title="" class="ltx_ref">GC99</a>]</cite>. The CNOT gates map $\lvert u\rangle\lvert\varphi_{f}\rangle$ to $2^{-\ell/2}\lvert u\rangle\sum_{u^{\prime}}(-1)^{f(u^{\prime})}\lvert u^{\prime}\oplus u\rangle\text{,}$ and outcome $v$ selects the term $u^{\prime}=u\oplus v\text{.}$ So on every input, and with any further registers, each outcome has probability $2^{-\ell}\text{,}$ and outcome $v$ applies to $\mathsf{X}$ the diagonal unitary with entries $(-1)^{f(u\oplus v)}\text{,}$ which is</p>
<table id="S7.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$Z_{f}Z_{\partial_{v}f},\qquad\text{where}\quad\partial_{v}f(u)=f(u)\oplus f(u\oplus v).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">This is $Z_{f}$ up to a correction that is again a phase unitary. A further injection removes the correction and leaves a new one, and these corrections vanish after $\ell+1$ injections.</p>
</div>
<div id="S7.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 7.2</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $f_{0}\colon\{0,1\}^{\ell}\to\{0,1\}\text{.}$ Inject $\lvert\varphi_{f_{0}}\rangle,\dots,\lvert\varphi_{f_{\ell}}\rangle$ into $\mathsf{X}$ in this order, where $f_{j+1}=\partial_{v_{j}}f_{j}$ and $v_{j}$ is the outcome of the injection of $\lvert\varphi_{f_{j}}\rangle\text{.}$ For all outcomes, these injections apply $Z_{f_{0}}$ to $\mathsf{X}\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S7.SS1.p2" class="ltx_para">
<p class="ltx_p">Phase unitaries commute and square to the identity, so the injections apply $\prod_{j=0}^{\ell}Z_{f_{j}}Z_{f_{j+1}}=Z_{f_{0}}Z_{f_{\ell+1}}\text{.}$ By induction on $j\text{,}$</p>
<table id="S7.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$f_{j}(u)=\bigoplus_{J\subseteq\{0,\dots,j-1\}}f_{0}\Bigl(u\oplus\bigoplus_{i\in J}v_{i}\Bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(7.1)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">For $j=\ell+1\text{,}$ the map $J\mapsto\bigoplus_{i\in J}v_{i}$ is linear from $\mathbb{F}_{2}^{\ell+1}$ to $\mathbb{F}_{2}^{\ell}\text{,}$ so it has a nontrivial kernel and takes each value an even number of times. Hence $f_{\ell+1}=0\text{.}$ Alternatively, each derivative lowers the degree of the function as a polynomial over $\mathbb{F}_{2}\text{,}$ and $f_{0}$ has degree at most $\ell\text{.}$
∎</p>
</div>
</div>
<div id="S7.SS1.p3" class="ltx_para">
<p class="ltx_p">For $L^{\prime}\in\mathsf{PSPACE}\text{,}$ let $f_{0}(u,b)=b\cdot L^{\prime}(u)$ on $\ell+1$ bits. Then $O_{L^{\prime}}$ on $\ell$ query qubits is $Z_{f_{0}}$ conjugated by $H$ on the answer qubit. The verifier obtains the states $\lvert\varphi_{f_{j}}\rangle$ of <a href="#S7.Thmtheorem2" title="Lemma 7.2. ‣ 7.1 State Injection ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">7.2</span></a> for this function from the prover by interactive state synthesis, which applies to states that can be prepared in polynomial space.</p>
</div>
<div id="S7.SS1.p4" class="ltx_para">
<p class="ltx_p">A family $(\lvert\chi_{x}\rangle)_{x}$ of pure states indexed by strings lies in $\mathsf{statePSPACE}$ if a space-uniform family of general quantum circuits of space polynomial in $\lvert x\rvert+r$ prepares, on $(x,1^{r})\text{,}$ a state within trace distance $1/r$ of $\lvert\chi_{x}\rangle$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Definition 2.11 and Remark 2.14]</cite>. The states $\lvert\varphi_{f_{j}}\rangle\text{,}$ indexed by a string that encodes $1^{\ell}$ and $v_{0},\dots,v_{j-1}$ for $j\leq\ell+1\text{,}$ together with the state $\lvert 0\rangle$ at all other strings, form such a family. Indeed, by <a href="#S7.E1" title="In 7.1 State Injection ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">(7.1)</span></a> the value $f_{j}(u,b)$ can be computed from this string and $(u,b)$ in polynomial space, so a generator can write Hadamard gates on all qubits and then, for each string on which $f_{j}$ is one, a phase flip on that basis state, built from NOT, Toffoli and $T^{4}$ gates with ancillas returned to zero. These circuits prepare the states exactly.</p>
</div>
</section>
<section id="S7.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="resource-states-from-the-prover">
<span class="ltx_tag ltx_tag_subsection">7.2 </span>Resource States from the Prover</h3>

<div id="S7.SS2.p1" class="ltx_para">
<p class="ltx_p">Interactive state synthesis provides verifiers of the following kind.</p>
</div>
<div id="S7.Thmtheorem3" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 7.3</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">verifier for a pure state</em> $\lvert\chi\rangle$ with error $\varepsilon$ is a verifier with no input and an output register $\mathsf{C}$ such that some prover is accepted with probability one and every prover accepted with probability at least $1/2$ leaves $\mathsf{C}$ within trace distance $\varepsilon$ of $\chi\text{,}$ conditioned on acceptance.</p>
</div>
</div>
<div id="S7.Thmtheorem4" class="ltx_theorem ltx_theorem_fact">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Fact 7.4</span></span><span class="ltx_text ltx_font_bold"> </span>(<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx45" title="" class="ltx_ref">Ros24</a>, Theorem 1.5 and Section 6]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Section 7.1]</cite>)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $(\lvert\chi_{x}\rangle)_{x}\in\mathsf{statePSPACE}\text{,}$ where the number of qubits of $\lvert\chi_{x}\rangle$ is computable in polynomial time from $x\text{.}$ A deterministic polynomial-time machine maps $(x,1^{r^{\prime}})$ to a verifier for $\lvert\chi_{x}\rangle$ with error $1/r^{\prime}\text{.}$</span></p>
</div>
</div>
<div id="S7.SS2.p2" class="ltx_para">
<p class="ltx_p">This guarantee is conditioned on a large acceptance probability and says nothing about the prover’s memory. When many such verifiers run as subroutines against the same prover, one of them may accept with small probability on some measurement outcomes. The next lemma bounds the subnormalized state on acceptance, for every acceptance probability and together with the memory.</p>
</div>
<div id="S7.Thmtheorem5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 7.5</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Consider a verifier for $\lvert\chi\rangle$ with error $\varepsilon$ and any prover with memory $\mathsf{M}\text{,}$ which we take to include the message register. Let $\Omega$ be the subnormalized state of $\mathsf{C}\mathsf{M}$ on acceptance, that is, the final state projected onto acceptance and reduced to $\mathsf{C}\mathsf{M}\text{,}$ so that $\operatorname{Tr}\Omega$ is the acceptance probability. Then $\rho_{\mathsf{M}}=\langle\chi\rvert\Omega\lvert\chi\rangle$ satisfies</span></p>
<table id="S7.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert\Omega-\chi\otimes\rho_{\mathsf{M}}\rVert_{1}\leq 3\sqrt{\varepsilon}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S7.SS2.p3" class="ltx_para">
<p class="ltx_p">Let $\Pi_{\chi}=\chi\otimes I\text{,}$ $p_{\mathrm{acc}}=\operatorname{Tr}\Omega$ and $\varepsilon^{\prime}=\operatorname{Tr}((I-\Pi_{\chi})\Omega)\text{.}$ To bound $\varepsilon^{\prime}\text{,}$ consider the prover that uses a private coin to follow the given prover or an honest prover, each with probability $1/2\text{.}$ It is accepted with probability $(1+p_{\mathrm{acc}})/2\geq 1/2\text{,}$ so, conditioned on acceptance, the measurement $\{\chi,I-\chi\}$ on $\mathsf{C}$ gives $I-\chi$ with probability at most $\varepsilon\text{,}$ since $\chi$ itself gives this outcome with probability zero. Acceptance with outcome $I-\chi$ has probability at least $\varepsilon^{\prime}/2\text{,}$ so $\varepsilon^{\prime}/2\leq\varepsilon(1+p_{\mathrm{acc}})/2$ and $\varepsilon^{\prime}\leq 2\varepsilon\text{.}$</p>
</div>
<div id="S7.SS2.p4" class="ltx_para">
<p class="ltx_p">Since $\lvert\chi\rangle$ is pure, $\Pi_{\chi}\Omega\Pi_{\chi}=\chi\otimes\rho_{\mathsf{M}}\text{,}$ and $\Omega-\Pi_{\chi}\Omega\Pi_{\chi}=(I-\Pi_{\chi})\Omega+\Pi_{\chi}\Omega(I-\Pi_{\chi})\text{.}$ Writing $\Omega=\sqrt{\Omega}\sqrt{\Omega}$ and using $\lVert XX^{\prime}\rVert_{1}\leq\lVert X\rVert_{F}\lVert X^{\prime}\rVert_{F}\text{,}$ we get</p>
<table id="S7.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert\Omega-\Pi_{\chi}\Omega\Pi_{\chi}\rVert_{1}\leq\sqrt{\varepsilon^{\prime}p_{\mathrm{acc}}}+\sqrt{(p_{\mathrm{acc}}-\varepsilon^{\prime})\varepsilon^{\prime}}\leq 2\sqrt{\varepsilon^{\prime}}\leq 2\sqrt{2\varepsilon}\leq 3\sqrt{\varepsilon}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right" style="opacity:1">∎</td>
</tr></tbody>
</table>
</div>
</div>
<div id="S7.SS2.p5" class="ltx_para">
<p class="ltx_p">With this lemma, a verifier can use states obtained from the prover as if they were exact, with an error that adds over the calls.</p>
</div>
<div id="S7.Thmtheorem6" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 7.6</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $\psi_{0}$ be the initial state of a private register $\mathsf{X}$ of a verifier together with a further register $\mathsf{R}$ on which neither party acts. In each of $n_{\mathrm{inj}}$ steps, the verifier sends the outcomes $v$ of the earlier steps to the prover and runs, on new qubits and the message register set to zero, a verifier for a pure state $\lvert\chi_{v}\rangle$ with error $\varepsilon\text{.}$ It keeps the acceptance qubit of this call, applies to $\mathsf{X}$ and the output register $\mathsf{C}$ of the call an instrument that depends on $v\text{,}$ and appends the outcome to $v\text{.}$ It accepts at the end if all acceptance qubits are one.</span></p>
</div>
<div id="S7.Thmtheorem6.p2" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Suppose that if each call produced exactly $\lvert\chi_{v}\rangle\text{,}$ every complete sequence of outcomes would leave the same state $\psi^{\prime}$ on $\mathsf{X}\mathsf{R}\text{.}$ Then for every prover whose memory is initially independent of $\mathsf{X}\mathsf{R}$ and whose acceptance probability $p_{\mathrm{acc}}$ is positive, the state $\sigma$ of $\mathsf{X}\mathsf{R}$ conditioned on acceptance satisfies</span></p>
<table id="S7.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D(\sigma,\psi^{\prime})\leq 3n_{\mathrm{inj}}\sqrt{\varepsilon}/p_{\mathrm{acc}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S7.SS2.p6" class="ltx_para">
<p class="ltx_p">We keep the prover fixed and compare a run with its ideal execution, in which each accepted resource state is replaced by its target. By <a href="#S7.Thmtheorem5" title="Lemma 7.5. ‣ 7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">7.5</span></a>, this replacement in one step changes the subnormalized state by at most $3\sqrt{\varepsilon}$ in trace norm, however small the acceptance probability of an individual call is. In the ideal execution, $\mathsf{X}\mathsf{R}$ is in product with the prover’s memory on each sequence of outcomes.</p>
</div>
<div id="S7.SS2.p7" class="ltx_para">
<p class="ltx_p">Write $\mathsf{M}$ for the memory of the prover, including the message register. After a sequence $v$ of outcomes of the earlier steps, step $j$ acts on $\mathsf{M}$ by a map $\mathcal{A}_{j,v}$ to $\mathsf{C}\mathsf{M}\text{,}$ which sends $v$ to the prover, runs the call of this step, projects its acceptance qubit onto one and discards this qubit and the other new qubits of the call except $\mathsf{C}\text{.}$ Its ideal version is $\chi_{v}\otimes\mathcal{T}_{j,v}\text{,}$ where $\chi_{v}$ is the target of the call and $\mathcal{T}_{j,v}(\tau)=\langle\chi_{v}\rvert\mathcal{A}_{j,v}(\tau)\lvert\chi_{v}\rangle\text{.}$ For a state $\omega$ on $\mathsf{M}$ and a further register, which we may include in the memory of the prover of the call, <a href="#S7.Thmtheorem5" title="Lemma 7.5. ‣ 7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">7.5</span></a> gives</p>
<table id="S7.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert(\mathcal{A}_{j,v}\otimes\mathrm{id})(\omega)-\chi_{v}\otimes(\mathcal{T}_{j,v}\otimes\mathrm{id})(\omega)\rVert_{1}\leq 3\sqrt{\varepsilon}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The instrument $\mathcal{B}_{j}$ of step $j$ appends its outcome to the sequence and removes $\mathsf{C}\text{.}$ The whole step is $\mathcal{F}_{j}\text{,}$ which applies $\mathcal{A}_{j,v}$ on the block of each $v$ and then $\mathcal{B}_{j}\text{,}$ and its ideal version $\widetilde{\mathcal{F}}_{j}$ has $\chi_{v}\otimes\mathcal{T}_{j,v}$ in place of $\mathcal{A}_{j,v}\text{.}$ These maps are completely positive and trace nonincreasing, so they do not increase the trace norm of Hermitian matrices. The blocks of different $v$ are orthogonal, so scaling the bound above gives $\lVert(\mathcal{F}_{j}-\widetilde{\mathcal{F}}_{j})(\omega)\rVert_{1}\leq 3\sqrt{\varepsilon}\operatorname{Tr}\omega$ for every positive $\omega\text{.}$</p>
</div>
<div id="S7.SS2.p8" class="ltx_para">
<p class="ltx_p">Starting from $\rho_{0}=\psi_{0}\otimes\tau_{0}\text{,}$ with $\tau_{0}$ the initial state of $\mathsf{M}\text{,}$ a run and its ideal execution produce $\rho=\mathcal{F}_{n_{\mathrm{inj}}}\cdots\mathcal{F}_{1}(\rho_{0})$ and $\widetilde{\rho}=\widetilde{\mathcal{F}}_{n_{\mathrm{inj}}}\cdots\widetilde{\mathcal{F}}_{1}(\rho_{0})\text{.}$ Acceptance qubits are not changed after their call, so $\rho$ is the subnormalized final state on acceptance. By the telescoping identity</p>
<table id="S7.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\rho-\widetilde{\rho}=\sum_{j=1}^{n_{\mathrm{inj}}}\mathcal{F}_{n_{\mathrm{inj}}}\cdots\mathcal{F}_{j+1}(\mathcal{F}_{j}-\widetilde{\mathcal{F}}_{j})\widetilde{\mathcal{F}}_{j-1}\cdots\widetilde{\mathcal{F}}_{1}(\rho_{0}),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">we get $\lVert\rho-\widetilde{\rho}\rVert_{1}\leq\eta$ for $\eta=3n_{\mathrm{inj}}\sqrt{\varepsilon}\text{.}$</p>
</div>
<div id="S7.SS2.p9" class="ltx_para">
<p class="ltx_p">It remains to describe $\widetilde{\rho}\text{.}$ If $v$ has positive probability when each call produces exactly $\lvert\chi_{v}\rangle\text{,}$ let $\psi_{v}$ be the state of $\mathsf{X}\mathsf{R}$ on these outcomes in that case. By induction on $j\text{,}$</p>
<table id="S7.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widetilde{\mathcal{F}}_{j}\cdots\widetilde{\mathcal{F}}_{1}(\rho_{0})=\sum_{v}\lvert v\rangle\langle v\rvert\otimes\psi_{v}\otimes\tau_{v},\qquad\tau_{v}\succeq 0,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where $v$ ranges over the sequences of outcomes of the first $j$ steps that have positive probability. Indeed, the maps $\chi_{v}\otimes\mathcal{T}_{j,v}$ act on $\mathsf{M}$ alone and produce $\chi_{v}\text{,}$ and on $\psi_{v}\otimes\chi_{v}$ the instrument gives each outcome $v^{\prime}$ with some probability $c_{v^{\prime}}$ and, if $c_{v^{\prime}}&gt;0\text{,}$ leaves $\psi_{vv^{\prime}}$ on $\mathsf{X}\mathsf{R}\text{,}$ so $\tau_{vv^{\prime}}=c_{v^{\prime}}\mathcal{T}_{j,v}(\tau_{v})\text{.}$ By hypothesis $\psi_{v}=\psi^{\prime}$ for every complete sequence $v\text{,}$ so the reduced state of $\widetilde{\rho}$ on $\mathsf{X}\mathsf{R}$ is $(\operatorname{Tr}\widetilde{\rho})\psi^{\prime}\text{.}$ Hence $\lVert\rho_{\mathsf{X}\mathsf{R}}-(\operatorname{Tr}\widetilde{\rho})\psi^{\prime}\rVert_{1}\leq\eta\text{,}$ and taking the trace gives $\lvert p_{\mathrm{acc}}-\operatorname{Tr}\widetilde{\rho}\rvert\leq\eta\text{.}$ Since $\sigma=\rho_{\mathsf{X}\mathsf{R}}/p_{\mathrm{acc}}\text{,}$</p>
<table id="S7.Ex8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D(\sigma,\psi^{\prime})=\frac{\lVert\rho_{\mathsf{X}\mathsf{R}}-p_{\mathrm{acc}}\psi^{\prime}\rVert_{1}}{2p_{\mathrm{acc}}}\leq\frac{\eta}{p_{\mathrm{acc}}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right" style="opacity:1">∎</td>
</tr></tbody>
</table>
</div>
</div>
</section>
<section id="S7.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="a-verifier-for-oracle-circuits">
<span class="ltx_tag ltx_tag_subsection">7.3 </span>A Verifier for Oracle Circuits</h3>

<div id="S7.SS3.p1" class="ltx_para">
<p class="ltx_p">To prove <a href="#S7.Thmtheorem1" title="Theorem 7.1. ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">7.1</span></a>, let $L^{\prime}\in\mathsf{PSPACE}$ and let $U\in\mathsf{unitaryBQP}^{\diamond,L^{\prime}}\text{,}$ with a time-uniform family $(\mathcal{C}_{x,r})_{x,r}$ and channel completions $\Phi_{x,r}$ of $U_{x}$ such that $\lVert\mathcal{C}_{x,r}-\Phi_{x,r}\rVert_{\diamond}\leq 1/r\text{.}$ Fix $x$ and $r\text{,}$ and write $\mathcal{C}=\mathcal{C}_{x,r}\text{.}$ Let $\ell_{1},\dots,\ell_{Q}$ be the numbers of query qubits of the oracle gates of $\mathcal{C}\text{,}$ and let $n_{\mathrm{inj}}=\sum_{i}(\ell_{i}+2)$ and $r^{\prime}=(12(n_{\mathrm{inj}}+1)r)^{2}\text{.}$</p>
</div>
<div id="S7.SS3.p2" class="ltx_para">
<p class="ltx_p">The verifier $V_{x,r}$ runs $\mathcal{C}$ on its ancilla register, with the input of $\mathcal{C}$ on the qubits that hold the verifier’s input, and it performs the non-oracle operations of $\mathcal{C}$ itself. It replaces an oracle gate on $\ell$ query qubits by $\ell+2$ steps between two Hadamard gates on the answer qubit. In step $j\text{,}$ for $j=0,\dots,\ell+1\text{,}$ let $v_{0},\dots,v_{j-1}$ be the outcomes of the earlier steps for this gate. The verifier sends all injection outcomes so far to the prover, sets the message register to zero, and runs the verifier of <a href="#S7.Thmtheorem4" title="Fact 7.4 ([Ros24, Theorem 1.5 and Section 6], [BEM+26, Section 7.1]). ‣ 7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">7.4</span></a> for the family of <a href="#S7.SS1" title="7.1 State Injection ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7.1</span></a>, with target $\lvert\varphi_{f_{j}}\rangle$ and precision $r^{\prime}\text{,}$ keeping the acceptance qubit of this call. Then it injects the output register $\mathsf{C}$ of the call into the query and answer qubits, which gives the outcome $v_{j}\text{.}$ At the end, $V_{x,r}$ moves the output wires of $\mathcal{C}$ to $\mathsf{B}_{x}$ and accepts if the acceptance qubits of all calls are one.</p>
</div>
<div id="S7.SS3.p3" class="ltx_para">
<p class="ltx_p">The call in a step depends on the outcomes, while the circuits of $V_{x,r}$ are fixed before the interaction. So $V_{x,r}$ simulates the machine of <a href="#S7.Thmtheorem4" title="Fact 7.4 ([Ros24, Theorem 1.5 and Section 6], [BEM+26, Section 7.1]). ‣ 7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">7.4</span></a> reversibly with NOT and Toffoli gates <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx11" title="" class="ltx_ref">Ben73</a>; <a href="#bib.bibx53" title="" class="ltx_ref">Tof80</a>]</cite>, computing the description of the required verifier on ancillas from the outcome wires, and it pads this description so that the numbers of wires, message qubits and rounds do not depend on the outcomes. For each position in this description and each possible operation, $V_{x,r}$ applies the operation controlled on the description naming it at this position, using the exact controlled gates of <a href="#S4.Thmtheorem3" title="Lemma 4.3. ‣ 4.2 The Language 𝐵 ‣ 4 Computing the Parameters ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a>. A measurement becomes a CNOT onto a new qubit, an initialization takes a new qubit at zero, and a discarded qubit is left untouched. The new qubits of measurements and the untouched discarded qubits stay private until the call ends and are then discarded, so on each sequence of outcomes the accepted state of $\mathsf{C}$ and the prover’s memory is that of the verifier of <a href="#S7.Thmtheorem4" title="Fact 7.4 ([Ros24, Theorem 1.5 and Section 6], [BEM+26, Section 7.1]). ‣ 7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">7.4</span></a>. The extra message qubits and rounds are idle, so a prover for the padded verifier is a prover for this verifier, with these qubits in its memory. The generator of $\mathcal{C}$ and the machine of <a href="#S7.Thmtheorem4" title="Fact 7.4 ([Ros24, Theorem 1.5 and Section 6], [BEM+26, Section 7.1]). ‣ 7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">7.4</span></a> run in polynomial time, so $V_{x,r}$ can be written in time polynomial in $\lvert x\rvert+r\text{.}$</p>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S7.Thmtheorem1" title="Theorem 7.1. ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">7.1</span></a>.</h6>
<div id="S7.SS3.p4" class="ltx_para">
<p class="ltx_p">An honest prover reads the outcomes and acts as the honest prover of each call, so it is accepted with probability one on every input. For soundness, let $\psi$ be a pure state on $\mathsf{A}_{x}\mathsf{R}\text{,}$ and consider a prover with acceptance probability $p_{\mathrm{acc}}\geq 1/2\text{.}$ The verifier $V_{x,r}$ has the form of <a href="#S7.Thmtheorem6" title="Lemma 7.6. ‣ 7.2 Resource States from the Prover ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">7.6</span></a> with $\varepsilon=1/r^{\prime}\text{,}$ where $\mathsf{X}$ consists of the qubits of $\mathcal{C}$ present at each point, $\psi_{0}$ is the state of $\mathsf{X}\mathsf{R}$ after the operations on $\mathsf{X}$ that precede the first call, and the instrument of a step is its injection followed by the operations on $\mathsf{X}$ that precede the next call, so that finally $\mathsf{X}$ is $\mathsf{B}_{x}\text{.}$ If each call produced its target exactly, <a href="#S7.Thmtheorem2" title="Lemma 7.2. ‣ 7.1 State Injection ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">7.2</span></a> would give every oracle gate exactly on all outcomes, so every complete sequence of outcomes would leave $\psi^{\prime}=(\mathcal{C}\otimes\mathrm{id})(\psi)$ on $\mathsf{B}_{x}\mathsf{R}\text{.}$ Thus the accepted output $\sigma$ satisfies</p>
<table id="S7.Ex9" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D(\sigma,\psi^{\prime})\leq\frac{3n_{\mathrm{inj}}}{\sqrt{r^{\prime}}\,p_{\mathrm{acc}}}\leq\frac{6n_{\mathrm{inj}}}{\sqrt{r^{\prime}}}\leq\frac{1}{2r}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $\lVert\mathcal{C}-\Phi_{x,r}\rVert_{\diamond}\leq 1/r\text{,}$ also $D(\psi^{\prime},(\Phi_{x,r}\otimes\mathrm{id})(\psi))\leq 1/(2r)\text{,}$ and hence $D(\sigma,(\Phi_{x,r}\otimes\mathrm{id})(\psi))\leq 1/r\text{,}$ with the same channel completion for all $\psi$ and all provers.
∎</p>
</div>
</div>
</section>
<section id="S7.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-converse">
<span class="ltx_tag ltx_tag_subsection">7.4 </span>The Converse</h3>

<div id="S7.Thmtheorem7" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 7.7</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem7.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">A size-computable problem in $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}$ lies in $\mathsf{unitaryPSPACE}^{\diamond}\text{.}$</span></p>
</div>
</div>
<div id="S7.SS4.p1" class="ltx_para">
<p class="ltx_p">A polynomial-space circuit can run a verifier against a prover if the prover’s actions are computable in polynomial space. For a verifier that starts from zero, a near-optimal prover has this property.</p>
</div>
<div id="S7.Thmtheorem8" class="ltx_theorem ltx_theorem_fact">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Fact 7.8</span></span><span class="ltx_text ltx_font_bold"> </span>(<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx41" title="" class="ltx_ref">MY23</a>, Theorem 7.1]</cite>, <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Theorem 7.9]</cite>)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem8.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $(V_{x})_{x}$ be a time-uniform family of polynomial-time verifiers with polynomially many rounds that start with all registers at zero, let $p_{\mathrm{opt}}(V_{x})$ be the supremum of the acceptance probabilities of $V_{x}$ over all provers, and let $q$ be a positive polynomial. There is a space-uniform family of general quantum circuits of polynomial space that implement provers $\mathcal{P}_{x}$ such that $\mathcal{P}_{x}$ is accepted by $V_{x}$ with probability at least $p_{\mathrm{opt}}(V_{x})-1/q(\lvert x\rvert)\text{.}$</span></p>
</div>
</div>
<div id="S7.SS4.p2" class="ltx_para">
<p class="ltx_p">The verifier of a synthesis problem has a quantum input, and the circuit must use one prover for all inputs. We optimize the prover on the all-zero input, and soundness forces the acceptance probability to be nearly the same on all inputs. Indeed, if a prover were accepted with very different probabilities on two inputs, then acceptance on a superposition of them, entangled with a purifying qubit, would change the distribution of this qubit, which no channel on the input can do.</p>
</div>
<div id="S7.Thmtheorem9" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 7.9</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem9.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix a verifier that satisfies the soundness condition of <a href="#S2.Thmtheorem10" title="Definition 2.10. ‣ 2.6 The Interactive Class ‣ 2 Preliminaries ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Definition</span> <span class="ltx_text ltx_ref_tag">2.10</span></a> with error $\varepsilon$ in place of $1/r\text{,}$ and fix a prover. Let $p(\psi)$ be the acceptance probability on a pure input $\lvert\psi\rangle$ on $\mathsf{A}_{x}\text{.}$ If $p(\psi)\geq 3/4\text{,}$ then $p(\psi^{\prime})\geq p(\psi)-\frac{9}{2}\varepsilon$ for every pure input $\lvert\psi^{\prime}\rangle\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S7.SS4.p3" class="ltx_para">
<p class="ltx_p">Apply soundness to the input $\sqrt{2/3}\lvert\psi\rangle\lvert 0\rangle+\sqrt{1/3}\lvert\psi^{\prime}\rangle\lvert 1\rangle\text{,}$ where the second factor is one purifying qubit. Neither the verifier nor the prover acts on this qubit, so measuring it first does not change its joint distribution with acceptance. Thus the acceptance probability is $p_{\mathrm{acc}}=(2p(\psi)+p(\psi^{\prime}))/3\geq 1/2\text{,}$ and acceptance with outcome $0$ has probability $\frac{2}{3}p(\psi)\text{.}$ A channel completion preserves the trace and does not act on this qubit, so its output has outcome $0$ with probability $2/3\text{.}$ Soundness therefore gives</p>
<table id="S7.Ex10" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\varepsilon\geq\frac{2p(\psi)}{3p_{\mathrm{acc}}}-\frac{2}{3}=\frac{2(p(\psi)-p(\psi^{\prime}))}{9p_{\mathrm{acc}}},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">and $p_{\mathrm{acc}}\leq 1$ gives the claim.
∎</p>
</div>
</div>
<div id="S7.SS4.p4" class="ltx_para">
<p class="ltx_p">High acceptance and soundness will show that on each input the circuit is close to some channel completion of $U_{x}\text{,}$ which may depend on the input. The class $\mathsf{unitaryPSPACE}^{\diamond}$ requires one channel completion for all inputs, and a minimax argument provides it.</p>
</div>
<div id="S7.Thmtheorem10" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 7.10</span></span><span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem10.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $U$ be a partial isometry from a register $\mathsf{A}$ to a register $\mathsf{B}\text{,}$ and let $\mathcal{C}$ be a channel from $\mathsf{A}$ to $\mathsf{B}\text{.}$ Suppose that for every pure state $\psi$ on $\mathsf{A}\mathsf{R}$ there is a channel completion $\Phi$ of $U$ with $D((\mathcal{C}\otimes\mathrm{id})(\psi),(\Phi\otimes\mathrm{id})(\psi))\leq\varepsilon\text{.}$ Then some channel completion $\Phi$ of $U$ satisfies $\lVert\mathcal{C}-\Phi\rVert_{\diamond}\leq 2\varepsilon\text{.}$</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S7.SS4.p5" class="ltx_para">
<p class="ltx_p">For a state $\rho$ on $\mathsf{A}$ with a purification $\psi_{\rho}\text{,}$ let</p>
<table id="S7.Ex11" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$F(\rho,\Phi)=D\bigl((\mathcal{C}\otimes\mathrm{id})(\psi_{\rho}),(\Phi\otimes\mathrm{id})(\psi_{\rho})\bigr).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Purifications of $\rho$ differ by an isometry on the purifying register, so $F$ does not depend on the purification, and the purification $(\sqrt{\rho}\otimes I)\sum_{u}\lvert u,u\rangle$ shows that $F$ is continuous. It is convex in $\Phi\text{.}$ It is concave in $\rho\text{:}$ if $\rho=\lambda\rho_{1}+(1-\lambda)\rho_{2}\text{,}$ then $\sqrt{\lambda}\lvert\psi_{\rho_{1}}\rangle\lvert 0\rangle+\sqrt{1-\lambda}\lvert\psi_{\rho_{2}}\rangle\lvert 1\rangle$ purifies $\rho\text{,}$ and measuring the last qubit does not increase the trace distance, which gives $F(\rho,\Phi)\geq\lambda F(\rho_{1},\Phi)+(1-\lambda)F(\rho_{2},\Phi)\text{.}$ The states on $\mathsf{A}$ and the channel completions of $U$ form compact convex sets, so the minimax theorem <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx51" title="" class="ltx_ref">Sio58</a>]</cite> gives</p>
<table id="S7.Ex12" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tfrac{1}{2}\min_{\Phi}\lVert\mathcal{C}-\Phi\rVert_{\diamond}=\min_{\Phi}\max_{\rho}F(\rho,\Phi)=\max_{\rho}\min_{\Phi}F(\rho,\Phi)\leq\varepsilon.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right" style="opacity:1">∎</td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#S7.Thmtheorem7" title="Theorem 7.7. ‣ 7.4 The Converse ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">7.7</span></a>.</h6>
<div id="S7.SS4.p6" class="ltx_para">
<p class="ltx_p">Let $U$ be size-computable with verifiers $V_{x,r}\text{.}$ For $y=1^{r^{\prime}}0x$ with $r^{\prime}\geq 1\text{,}$ let $V_{y}$ be $V_{x,r^{\prime}}$ on the all-zero input, so that all its registers start at zero, and at other strings $y$ let $V_{y}$ be a fixed verifier. This family is time-uniform, so <a href="#S7.Thmtheorem8" title="Fact 7.8 ([MY23, Theorem 7.1], [BEM+26, Theorem 7.9]). ‣ 7.4 The Converse ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Fact</span> <span class="ltx_text ltx_ref_tag">7.8</span></a> with $q(s)=s+1$ gives provers $\mathcal{P}_{y}\text{.}$ Now fix $x$ and $r\text{,}$ let $r^{\prime}=32r\text{,}$ $\varepsilon=1/r^{\prime}$ and $y=1^{r^{\prime}}0x\text{,}$ so that $\mathcal{P}_{y}$ has acceptance probability at least $p_{\mathrm{opt}}(V_{y})-\varepsilon$ on the all-zero input. Let $\mathcal{C}_{x,r}$ be the general quantum circuit that runs $V_{x,r^{\prime}}$ against $\mathcal{P}_{y}$ and discards everything except $\mathsf{B}_{x}\text{.}$ Its input wires are the first $n_{\mathrm{in}}(x)$ qubits of the ancilla register of $V_{x,r^{\prime}}\text{,}$ which the generator can list because $U$ is size-computable. The family $(\mathcal{C}_{x,r})_{x,r}$ is space-uniform, of space polynomial in $\lvert x\rvert+r\text{.}$</p>
</div>
<div id="S7.SS4.p7" class="ltx_para">
<p class="ltx_p">If $\operatorname{supp}U_{x}=\{0\}\text{,}$ every channel is a channel completion of $U_{x}\text{.}$ Otherwise, an honest prover is accepted with probability one on a unit vector in $\operatorname{supp}U_{x}\text{,}$ so by <a href="#S7.Thmtheorem9" title="Lemma 7.9. ‣ 7.4 The Converse ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">7.9</span></a> it is accepted with probability at least $1-\frac{9}{2}\varepsilon$ on the all-zero input. Hence $p_{\mathrm{opt}}(V_{y})\geq 1-\frac{9}{2}\varepsilon\text{,}$ and $\mathcal{P}_{y}$ is accepted on the all-zero input with probability at least $1-\frac{11}{2}\varepsilon&gt;3/4\text{.}$ Applying <a href="#S7.Thmtheorem9" title="Lemma 7.9. ‣ 7.4 The Converse ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">7.9</span></a> to $\mathcal{P}_{y}$ shows that it is accepted with probability at least $1-10\varepsilon$ on every pure input. The same holds on every input with a purifying register, since the reduced state of the input is a mixture of pure states.</p>
</div>
<div id="S7.SS4.p8" class="ltx_para">
<p class="ltx_p">Let $\psi$ be a pure state on $\mathsf{A}_{x}\mathsf{R}\text{.}$ Its acceptance probability $p_{\mathrm{acc}}$ against $\mathcal{P}_{y}$ is at least $1-10\varepsilon&gt;1/2\text{,}$ so soundness gives a channel completion $\Phi$ of $U_{x}$ with $D(\sigma,(\Phi\otimes\mathrm{id})(\psi))\leq\varepsilon$ for the accepted output $\sigma\text{.}$ The output of $\mathcal{C}_{x,r}$ is $\sigma$ with probability $p_{\mathrm{acc}}$ and some other state otherwise, so</p>
<table id="S7.Ex13" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$D\bigl((\mathcal{C}_{x,r}\otimes\mathrm{id})(\psi),(\Phi\otimes\mathrm{id})(\psi)\bigr)\leq p_{\mathrm{acc}}\varepsilon+1-p_{\mathrm{acc}}\leq 11\varepsilon.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">By <a href="#S7.Thmtheorem10" title="Lemma 7.10. ‣ 7.4 The Converse ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">7.10</span></a>, one channel completion $\Phi_{x,r}$ of $U_{x}$ satisfies</p>
<table id="S7.Ex14" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\lVert\mathcal{C}_{x,r}-\Phi_{x,r}\rVert_{\diamond}\leq 22\varepsilon&lt;\frac{1}{r}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right" style="opacity:1">∎</td>
</tr></tbody>
</table>
</div>
</div>
<div id="S7.Thmtheorem11" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 7.11</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S7.Thmtheorem11.p1" class="ltx_para">
<p class="ltx_p">The condition on the register sizes in <a href="#S1.Thmtheorem5" title="Theorem 1.5. ‣ Interactive synthesis. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.5</span></a> cannot be removed from the converse, and it cannot be removed from the inclusion in $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}$ unless $\mathsf{P}=\mathsf{PSPACE}\text{.}$ The description of a verifier does not fix its input size, because the input is placed on the first qubits of an ancilla register that otherwise starts at zero <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx10" title="" class="ltx_ref">BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26</a>, Section 2.4]</cite>. Let $L$ be a language outside $\mathsf{PSPACE}\text{,}$ and let $U_{x}$ be the identity on two qubits if $x\in L$ and $\lvert\psi\rangle\mapsto\lvert\psi\rangle\lvert 0\rangle$ from one qubit to two qubits otherwise. One verifier for all $x\text{,}$ which moves the first two qubits of its ancilla register to $\mathsf{B}_{x}$ and accepts, implements $U_{x}$ with error zero. If $U$ were in $\mathsf{unitaryPSPACE}^{\diamond}\text{,}$ counting the input wires written by the generator would decide $L$ in polynomial space.</p>
</div>
<div id="S7.Thmtheorem11.p2" class="ltx_para">
<p class="ltx_p">The description of a verifier does fix its output register, so every problem in $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}$ has $n_{\mathrm{out}}$ computable in polynomial time. Thus the problem of <a href="#S6.Thmtheorem1" title="Example 6.1. ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Example</span> <span class="ltx_text ltx_ref_tag">6.1</span></a> lies in $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}$ only if $L^{\prime}\in\mathsf{P}\text{,}$ so if every problem in $\mathsf{unitaryPSPACE}^{\diamond}$ lies in $\mathsf{unitaryQIP}^{\diamond}_{1,1/2}$ then $\mathsf{P}=\mathsf{PSPACE}\text{.}$ Conversely, if $\mathsf{P}=\mathsf{PSPACE}\text{,}$ every problem in $\mathsf{unitaryPSPACE}^{\diamond}$ is size-computable, as in the proof of <a href="#S6.Thmtheorem5" title="Theorem 6.5. ‣ 6.2 The Collapse Criterion ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.5</span></a>(ii).</p>
</div>
</div>
<div id="S7.SS4.p9" class="ltx_para">
<p class="ltx_p">Together, <a href="#S6.Thmtheorem2" title="Theorem 6.2. ‣ 6.1 Implementing Channels with a PSPACE Oracle ‣ 6 The Channel Model ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorems</span> <span class="ltx_text ltx_ref_tag">6.2</span></a>, <a href="#S7.Thmtheorem1" title="Theorem 7.1. ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7.1</span></a> and <a href="#S7.Thmtheorem7" title="Theorem 7.7. ‣ 7.4 The Converse ‣ 7 Interactive Synthesis ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7.7</span></a> prove <a href="#S1.Thmtheorem5" title="Theorem 1.5. ‣ Interactive synthesis. ‣ 1.1 Results ‣ 1 Introduction ‣ Unitary Synthesis with a PSPACE Oracle" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.5</span></a>.


</p>
</div>
</section>
</section>
<section id="Sx1" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="ai-methodology-statement">AI Methodology Statement</h2>

<div id="Sx1.p1" class="ltx_para">
<p class="ltx_p">The author used ChatGPT and Codex from OpenAI and Claude Code from Anthropic to help organize and polish the exposition of this paper, based on the author’s own drafts. The same tools assisted in surveying the related literature, in understanding the current state of research in this area, in flagging possible errors in draft proofs, and in suggesting simpler proofs of some statements. The author checked, revised, and finalized every statement, proof, and reference in the paper. The Lean formalization was written almost entirely by these tools. Lean checks its proofs, and the author checked that its definitions and theorem statements match those in the paper. The author takes full responsibility for the content of the submission.</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography" id="references">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bibx1" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Aar16]</span>
<span class="ltx_bibblock">
Scott Aaronson.

</span>
<span class="ltx_bibblock">The complexity of quantum states and transformations: From quantum
money to black holes.

</span>
<span class="ltx_bibblock">Lecture notes, 28th McGill Invitational Workshop on Computational
Complexity, 2016.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/1607.05256" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:1607.05256</span></a>.

</span>
</li>
      
<li id="bib.bibx2" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Aar21]</span>
<span class="ltx_bibblock">
Scott Aaronson.

</span>
<span class="ltx_bibblock">Open problems related to quantum query complexity.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">ACM Transactions on Quantum Computing</span>, 2(4):14:1–14:9, 2021.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2109.06917" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2109.06917</span></a>,
<a href="https://doi.org/10.1145/3488559" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/3488559</span></a>.

</span>
</li>
      
<li id="bib.bibx3" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[AFCB14]</span>
<span class="ltx_bibblock">
Mateus Araújo, Adrien Feix, Fabio Costa, and Časlav Brukner.

</span>
<span class="ltx_bibblock">Quantum circuits cannot control unknown operations.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">New Journal of Physics</span>, 16(9):093026, 2014.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/1309.7976" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:1309.7976</span></a>,
<a href="https://doi.org/10.1088/1367-2630/16/9/093026" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1088/1367-2630/16/9/093026</span></a>.

</span>
</li>
      
<li id="bib.bibx4" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[AGL25]</span>
<span class="ltx_bibblock">
Prabhanjan Ananth, Aditya Gulati, and Yao-Ting Lin.

</span>
<span class="ltx_bibblock">Cryptography in the common Haar state model: Feasibility results
and separations.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Theory of Cryptography (TCC 2024)</span>, volume 15365 of <span class="ltx_text ltx_font_italic">Lecture Notes in Computer Science</span>, pages 94–125. Springer, 2025.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2407.07908" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2407.07908</span></a>,
<a href="https://doi.org/10.1007/978-3-031-78017-2_4" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/978-3-031-78017-2_4</span></a>.

</span>
</li>
      
<li id="bib.bibx5" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[AK07]</span>
<span class="ltx_bibblock">
Scott Aaronson and Greg Kuperberg.

</span>
<span class="ltx_bibblock">Quantum versus classical proofs and advice.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Theory of Computing</span>, 3(7):129–157, 2007.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/quant-ph/0604056" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:quant-ph/0604056</span></a>, <a href="https://doi.org/10.4086/toc.2007.v003a007" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.4086/toc.2007.v003a007</span></a>.

</span>
</li>
      
<li id="bib.bibx6" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[BBBV97]</span>
<span class="ltx_bibblock">
Charles H. Bennett, Ethan Bernstein, Gilles Brassard, and Umesh Vazirani.

</span>
<span class="ltx_bibblock">Strengths and weaknesses of quantum computing.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">SIAM Journal on Computing</span>, 26(5):1510–1523, 1997.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/quant-ph/9701001" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:quant-ph/9701001</span></a>, <a href="https://doi.org/10.1137/S0097539796300933" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1137/S0097539796300933</span></a>.

</span>
</li>
      
<li id="bib.bibx7" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[BCC<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>14]</span>
<span class="ltx_bibblock">
Dominic W. Berry, Andrew M. Childs, Richard Cleve, Robin Kothari, and
Rolando D. Somma.

</span>
<span class="ltx_bibblock">Exponential improvement in precision for simulating sparse
Hamiltonians.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Proceedings of the 46th Annual ACM Symposium on Theory of
Computing (STOC)</span>, pages 283–292. ACM, 2014.

</span>
<span class="ltx_bibblock">Numbered references are to arXiv version 2.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/1312.1414v2" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:1312.1414v2</span></a>,
<a href="https://doi.org/10.1145/2591796.2591854" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/2591796.2591854</span></a>.

</span>
</li>
      
<li id="bib.bibx8" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[BCN25]</span>
<span class="ltx_bibblock">
John Bostanci, Boyang Chen, and Barak Nehoran.

</span>
<span class="ltx_bibblock">Oracle separation between quantum commitments and quantum
one-wayness.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Advances in Cryptology – EUROCRYPT 2025</span>, volume 15607 of
<span class="ltx_text ltx_font_italic">Lecture Notes in Computer Science</span>, pages 3–22. Springer, 2025.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2410.03358" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2410.03358</span></a>,
<a href="https://doi.org/10.1007/978-3-031-91098-2_1" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/978-3-031-91098-2_1</span></a>.

</span>
</li>
      
<li id="bib.bibx9" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[BCQ23]</span>
<span class="ltx_bibblock">
Zvika Brakerski, Ran Canetti, and Luowen Qian.

</span>
<span class="ltx_bibblock">On the computational hardness needed for quantum cryptography.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">14th Innovations in Theoretical Computer Science Conference
(ITCS 2023)</span>, volume 251 of <span class="ltx_text ltx_font_italic">Leibniz International Proceedings in
Informatics (LIPIcs)</span>, pages 24:1–24:21. Schloss Dagstuhl – Leibniz-Zentrum
für Informatik, 2023.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2209.04101" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2209.04101</span></a>,
<a href="https://doi.org/10.4230/LIPIcs.ITCS.2023.24" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.4230/LIPIcs.ITCS.2023.24</span></a>.

</span>
</li>
      
<li id="bib.bibx10" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[BEM<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26]</span>
<span class="ltx_bibblock">
John Bostanci, Yuval Efron, Tony Metger, Alexander Poremba, Luowen Qian, and
Henry Yuen.

</span>
<span class="ltx_bibblock">Unitary complexity and the Uhlmann transformation problem.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">17th Innovations in Theoretical Computer Science Conference
(ITCS 2026)</span>, volume 362 of <span class="ltx_text ltx_font_italic">Leibniz International Proceedings in
Informatics (LIPIcs)</span>, pages 24:1–24:17. Schloss Dagstuhl – Leibniz-Zentrum
für Informatik, 2026.

</span>
<span class="ltx_bibblock">Numbered references are to arXiv version 3.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2306.13073v3" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2306.13073v3</span></a>, <a href="https://doi.org/10.4230/LIPIcs.ITCS.2026.24" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.4230/LIPIcs.ITCS.2026.24</span></a>.

</span>
</li>
      
<li id="bib.bibx11" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Ben73]</span>
<span class="ltx_bibblock">
Charles H. Bennett.

</span>
<span class="ltx_bibblock">Logical reversibility of computation.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">IBM Journal of Research and Development</span>, 17(6):525–532, 1973.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1147/rd.176.0525" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1147/rd.176.0525</span></a>.

</span>
</li>
      
<li id="bib.bibx12" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Bre76]</span>
<span class="ltx_bibblock">
Richard P. Brent.

</span>
<span class="ltx_bibblock">Fast multiple-precision evaluation of elementary functions.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Journal of the ACM</span>, 23(2):242–251, 1976.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1145/321941.321944" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/321941.321944</span></a>.

</span>
</li>
      
<li id="bib.bibx13" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[BVMS05]</span>
<span class="ltx_bibblock">
Ville Bergholm, Juha J. Vartiainen, Mikko Möttönen, and Martti M.
Salomaa.

</span>
<span class="ltx_bibblock">Quantum circuits with uniformly controlled one-qubit gates.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Physical Review A</span>, 71(5):052330, 2005.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/quant-ph/0410066" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:quant-ph/0410066</span></a>, <a href="https://doi.org/10.1103/PhysRevA.71.052330" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1103/PhysRevA.71.052330</span></a>.

</span>
</li>
      
<li id="bib.bibx14" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[BY26]</span>
<span class="ltx_bibblock">
Zvika Brakerski and Henry Yuen.

</span>
<span class="ltx_bibblock">On scalable pseudorandom unitaries and the unitary synthesis problem.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Advances in Cryptology – CRYPTO 2026</span>, volume 16804 of
<span class="ltx_text ltx_font_italic">Lecture Notes in Computer Science</span>, pages 372–401. Springer, 2026.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2605.09957" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2605.09957</span></a>,
<a href="https://doi.org/10.1007/978-3-032-35409-9_13" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/978-3-032-35409-9_13</span></a>.

</span>
</li>
      
<li id="bib.bibx15" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[CCH<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>26]</span>
<span class="ltx_bibblock">
Nai-Hui Chia, Kai-Min Chung, Tzu-Hsiang Huang, Chuhan Lu, and Jhih-Wei Shih.

</span>
<span class="ltx_bibblock">Complexity theory for quantum promise problems, 2026.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2411.03716v3" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2411.03716v3</span></a>.

</span>
</li>
      
<li id="bib.bibx16" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[CCS25]</span>
<span class="ltx_bibblock">
Boyang Chen, Andrea Coladangelo, and Or Sattath.

</span>
<span class="ltx_bibblock">The power of a single Haar random state: Constructing and
separating quantum pseudorandomness.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Advances in Cryptology – EUROCRYPT 2025</span>, volume 15607 of
<span class="ltx_text ltx_font_italic">Lecture Notes in Computer Science</span>, pages 108–137. Springer, 2025.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2404.03295" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2404.03295</span></a>,
<a href="https://doi.org/10.1007/978-3-031-91098-2_5" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/978-3-031-91098-2_5</span></a>.

</span>
</li>
      
<li id="bib.bibx17" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Cho75]</span>
<span class="ltx_bibblock">
Man-Duen Choi.

</span>
<span class="ltx_bibblock">Completely positive linear maps on complex matrices.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Linear Algebra and its Applications</span>, 10(3):285–290, 1975.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1016/0024-3795(75)90075-0" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1016/0024-3795(75)90075-0</span></a>.

</span>
</li>
      
<li id="bib.bibx18" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[CM26]</span>
<span class="ltx_bibblock">
Ezekiel Cochran and Atul Mantri.

</span>
<span class="ltx_bibblock">Black hole radiation decoding in the Haar random oracle model,
2026.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2610.07124" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2610.07124</span></a>.

</span>
</li>
      
<li id="bib.bibx19" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[CMY26]</span>
<span class="ltx_bibblock">
Boyang Chen, Tomoyuki Morimae, and Takashi Yamakawa.

</span>
<span class="ltx_bibblock">Quantum Pessiland, 2026.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2608.29493" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2608.29493</span></a>.

</span>
</li>
      
<li id="bib.bibx20" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[DLM26]</span>
<span class="ltx_bibblock">
Fangqi Dong, Alex Lombardi, and Fermi Ma.

</span>
<span class="ltx_bibblock">Explicit separations for one-query unitary synthesis, 2026.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2607.26478" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2607.26478</span></a>.

</span>
</li>
      
<li id="bib.bibx21" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[DN06]</span>
<span class="ltx_bibblock">
Christopher M. Dawson and Michael A. Nielsen.

</span>
<span class="ltx_bibblock">The Solovay–Kitaev algorithm.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Quantum Information and Computation</span>, 6(1):81–95, 2006.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/quant-ph/0505030" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:quant-ph/0505030</span></a>, <a href="https://doi.org/10.26421/QIC6.1-6" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.26421/QIC6.1-6</span></a>.

</span>
</li>
      
<li id="bib.bibx22" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[FR21]</span>
<span class="ltx_bibblock">
Bill Fefferman and Zachary Remscrim.

</span>
<span class="ltx_bibblock">Eliminating intermediate measurements in space-bounded quantum
computation.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory
of Computing (STOC)</span>, pages 1343–1356. ACM, 2021.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2006.03530" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2006.03530</span></a>,
<a href="https://doi.org/10.1145/3406325.3451051" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/3406325.3451051</span></a>.

</span>
</li>
      
<li id="bib.bibx23" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[GC99]</span>
<span class="ltx_bibblock">
Daniel Gottesman and Isaac L. Chuang.

</span>
<span class="ltx_bibblock">Demonstrating the viability of universal quantum computation using
teleportation and single-qubit operations.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Nature</span>, 402:390–393, 1999.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/quant-ph/9908010" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:quant-ph/9908010</span></a>, <a href="https://doi.org/10.1038/46503" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1038/46503</span></a>.

</span>
</li>
      
<li id="bib.bibx24" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[GR02]</span>
<span class="ltx_bibblock">
Lov Grover and Terry Rudolph.

</span>
<span class="ltx_bibblock">Creating superpositions that correspond to efficiently integrable
probability distributions, 2002.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/quant-ph/0208112" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:quant-ph/0208112</span></a>.

</span>
</li>
      
<li id="bib.bibx25" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[GR22]</span>
<span class="ltx_bibblock">
Uma Girish and Ran Raz.

</span>
<span class="ltx_bibblock">Eliminating intermediate measurements using pseudorandom generators.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">13th Innovations in Theoretical Computer Science Conference
(ITCS 2022)</span>, volume 215 of <span class="ltx_text ltx_font_italic">Leibniz International Proceedings in
Informatics (LIPIcs)</span>, pages 76:1–76:18. Schloss Dagstuhl – Leibniz-Zentrum
für Informatik, 2022.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2106.11877" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2106.11877</span></a>,
<a href="https://doi.org/10.4230/LIPIcs.ITCS.2022.76" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.4230/LIPIcs.ITCS.2022.76</span></a>.

</span>
</li>
      
<li id="bib.bibx26" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[GSLW19]</span>
<span class="ltx_bibblock">
András Gilyén, Yuan Su, Guang Hao Low, and Nathan Wiebe.

</span>
<span class="ltx_bibblock">Quantum singular value transformation and beyond: Exponential
improvements for quantum matrix arithmetics.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Proceedings of the 51st Annual ACM SIGACT Symposium on Theory
of Computing (STOC)</span>, pages 193–204. ACM, 2019.

</span>
<span class="ltx_bibblock">Numbered references are to the arXiv version.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/1806.01838" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:1806.01838</span></a>,
<a href="https://doi.org/10.1145/3313276.3316366" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/3313276.3316366</span></a>.

</span>
</li>
      
<li id="bib.bibx27" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Hel76]</span>
<span class="ltx_bibblock">
Carl W. Helstrom.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Quantum Detection and Estimation Theory</span>, volume 123 of <span class="ltx_text ltx_font_italic">Mathematics in Science and Engineering</span>.

</span>
<span class="ltx_bibblock">Academic Press, 1976.

</span>
</li>
      
<li id="bib.bibx28" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[HRW26]</span>
<span class="ltx_bibblock">
Andrew Huang, Akshar Ramkumar, and John Wright.

</span>
<span class="ltx_bibblock">Random-oracle unitary synthesis is impossible, 2026.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2610.06700" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2610.06700</span></a>.

</span>
</li>
      
<li id="bib.bibx29" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Hua25]</span>
<span class="ltx_bibblock">
Ting Jia Huang.

</span>
<span class="ltx_bibblock">A 1.5-query lower bound for the unitary synthesis problem, 2025.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2508.13215" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2508.13215</span></a>.

</span>
</li>
      
<li id="bib.bibx30" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[JJUW11]</span>
<span class="ltx_bibblock">
Rahul Jain, Zhengfeng Ji, Sarvagya Upadhyay, and John Watrous.

</span>
<span class="ltx_bibblock">QIP = PSPACE.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Journal of the ACM</span>, 58(6):30:1–30:27, 2011.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/0907.4737" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:0907.4737</span></a>,
<a href="https://doi.org/10.1145/2049697.2049704" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/2049697.2049704</span></a>.

</span>
</li>
      
<li id="bib.bibx31" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[JLS18]</span>
<span class="ltx_bibblock">
Zhengfeng Ji, Yi-Kai Liu, and Fang Song.

</span>
<span class="ltx_bibblock">Pseudorandom quantum states.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Advances in Cryptology – CRYPTO 2018</span>, volume 10993 of
<span class="ltx_text ltx_font_italic">Lecture Notes in Computer Science</span>, pages 126–152. Springer, 2018.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/1711.00385" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:1711.00385</span></a>,
<a href="https://doi.org/10.1007/978-3-319-96878-0_5" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/978-3-319-96878-0_5</span></a>.

</span>
</li>
      
<li id="bib.bibx32" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[KLL<sup class="ltx_sup"><span class="ltx_text ltx_font_italic">+</span></sup>17]</span>
<span class="ltx_bibblock">
Shelby Kimmel, Cedric Yen-Yu Lin, Guang Hao Low, Maris Ozols, and Theodore J.
Yoder.

</span>
<span class="ltx_bibblock">Hamiltonian simulation with optimal sample complexity.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">npj Quantum Information</span>, 3(1):13, 2017.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/1608.00281" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:1608.00281</span></a>,
<a href="https://doi.org/10.1038/s41534-017-0013-7" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1038/s41534-017-0013-7</span></a>.

</span>
</li>
      
<li id="bib.bibx33" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Kni95]</span>
<span class="ltx_bibblock">
Emanuel Knill.

</span>
<span class="ltx_bibblock">Approximation by quantum circuits.

</span>
<span class="ltx_bibblock">Technical Report LAUR-95-2225, Los Alamos National Laboratory, 1995.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/quant-ph/9508006" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:quant-ph/9508006</span></a>.

</span>
</li>
      
<li id="bib.bibx34" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[KQST23]</span>
<span class="ltx_bibblock">
William Kretschmer, Luowen Qian, Makrand Sinha, and Avishay Tal.

</span>
<span class="ltx_bibblock">Quantum cryptography in Algorithmica.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Proceedings of the 55th Annual ACM Symposium on Theory of
Computing (STOC)</span>, pages 1589–1602. ACM, 2023.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2212.00879" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2212.00879</span></a>,
<a href="https://doi.org/10.1145/3564246.3585225" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/3564246.3585225</span></a>.

</span>
</li>
      
<li id="bib.bibx35" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[KQT25]</span>
<span class="ltx_bibblock">
William Kretschmer, Luowen Qian, and Avishay Tal.

</span>
<span class="ltx_bibblock">Quantum-computable one-way functions without one-way functions.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Proceedings of the 57th Annual ACM Symposium on Theory of
Computing (STOC)</span>, pages 189–200. ACM, 2025.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2411.02554" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2411.02554</span></a>,
<a href="https://doi.org/10.1145/3717823.3718144" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/3717823.3718144</span></a>.

</span>
</li>
      
<li id="bib.bibx36" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Kre21]</span>
<span class="ltx_bibblock">
William Kretschmer.

</span>
<span class="ltx_bibblock">Quantum pseudorandomness and classical complexity.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">16th Conference on the Theory of Quantum Computation,
Communication and Cryptography (TQC 2021)</span>, volume 197 of <span class="ltx_text ltx_font_italic">Leibniz
International Proceedings in Informatics (LIPIcs)</span>, pages 2:1–2:20. Schloss
Dagstuhl – Leibniz-Zentrum für Informatik, 2021.

</span>
<span class="ltx_bibblock">Numbered references are to arXiv version 5, which corrects the
conference version.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2103.09320v5" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2103.09320v5</span></a>, <a href="https://doi.org/10.4230/LIPIcs.TQC.2021.2" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.4230/LIPIcs.TQC.2021.2</span></a>.

</span>
</li>
      
<li id="bib.bibx37" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[KT26]</span>
<span class="ltx_bibblock">
William Kretschmer and Ewin Tang.

</span>
<span class="ltx_bibblock">Unitary complexity in polynomial space, 2026.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2610.03705v2" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2610.03705v2</span></a>.

</span>
</li>
      
<li id="bib.bibx38" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[LMR14]</span>
<span class="ltx_bibblock">
Seth Lloyd, Masoud Mohseni, and Patrick Rebentrost.

</span>
<span class="ltx_bibblock">Quantum principal component analysis.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Nature Physics</span>, 10(9):631–633, 2014.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/1307.0401" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:1307.0401</span></a>,
<a href="https://doi.org/10.1038/nphys3029" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1038/nphys3029</span></a>.

</span>
</li>
      
<li id="bib.bibx39" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[LMW24]</span>
<span class="ltx_bibblock">
Alex Lombardi, Fermi Ma, and John Wright.

</span>
<span class="ltx_bibblock">A one-query lower bound for unitary synthesis and breaking quantum
cryptography.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Proceedings of the 56th Annual ACM Symposium on Theory of
Computing (STOC)</span>, pages 979–990. ACM, 2024.

</span>
<span class="ltx_bibblock">Numbered references are to the arXiv version.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2310.08870" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2310.08870</span></a>,
<a href="https://doi.org/10.1145/3618260.3649650" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/3618260.3649650</span></a>.

</span>
</li>
      
<li id="bib.bibx40" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Mac95]</span>
<span class="ltx_bibblock">
Ian G. Macdonald.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Symmetric Functions and Hall Polynomials</span>.

</span>
<span class="ltx_bibblock">Oxford Mathematical Monographs. Oxford University Press, second
edition, 1995.

</span>
</li>
      
<li id="bib.bibx41" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[MY23]</span>
<span class="ltx_bibblock">
Tony Metger and Henry Yuen.

</span>
<span class="ltx_bibblock">stateQIP = statePSPACE.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">2023 IEEE 64th Annual Symposium on Foundations of Computer
Science (FOCS)</span>, pages 1349–1356. IEEE, 2023.

</span>
<span class="ltx_bibblock">Numbered references are to arXiv version 2.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2301.07730v2" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2301.07730v2</span></a>, <a href="https://doi.org/10.1109/FOCS57990.2023.00082" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1109/FOCS57990.2023.00082</span></a>.

</span>
</li>
      
<li id="bib.bibx42" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[NC10]</span>
<span class="ltx_bibblock">
Michael A. Nielsen and Isaac L. Chuang.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Quantum Computation and Quantum Information</span>.

</span>
<span class="ltx_bibblock">Cambridge University Press, 10th anniversary edition, 2010.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1017/CBO9780511976667" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1017/CBO9780511976667</span></a>.

</span>
</li>
      
<li id="bib.bibx43" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Ope26]</span>
<span class="ltx_bibblock">
OpenAI.

</span>
<span class="ltx_bibblock">Polynomial-time unitary synthesis from a Boolean oracle.

</span>
<span class="ltx_bibblock">OpenAI Math Release preprint, October 5, 2026.

</span>
<span class="ltx_bibblock">URL:
<a href="https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026</a>.

</span>
</li>
      
<li id="bib.bibx44" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Ros23]</span>
<span class="ltx_bibblock">
Gregory Rosenthal.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Quantum State and Unitary Complexity</span>.

</span>
<span class="ltx_bibblock">PhD thesis, University of Toronto, 2023.

</span>
<span class="ltx_bibblock">URL: <a href="https://hdl.handle.net/1807/130326" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://hdl.handle.net/1807/130326</a>.

</span>
</li>
      
<li id="bib.bibx45" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Ros24]</span>
<span class="ltx_bibblock">
Gregory Rosenthal.

</span>
<span class="ltx_bibblock">Efficient quantum state synthesis with one query.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Proceedings of the 2024 Annual ACM-SIAM Symposium on Discrete
Algorithms (SODA)</span>, pages 2508–2534. SIAM, 2024.

</span>
<span class="ltx_bibblock">Numbered references are to arXiv version 4.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2306.01723v4" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2306.01723v4</span></a>, <a href="https://doi.org/10.1137/1.9781611977912.89" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1137/1.9781611977912.89</span></a>.

</span>
</li>
      
<li id="bib.bibx46" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Ros26]</span>
<span class="ltx_bibblock">
Gregory Rosenthal.

</span>
<span class="ltx_bibblock">Query and depth upper bounds for quantum unitaries via Grover
search.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Quantum</span>, 10:2144, 2026.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2111.07992" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2111.07992</span></a>,
<a href="https://doi.org/10.22331/q-2026-06-30-2144" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.22331/q-2026-06-30-2144</span></a>.

</span>
</li>
      
<li id="bib.bibx47" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[RY22]</span>
<span class="ltx_bibblock">
Gregory Rosenthal and Henry Yuen.

</span>
<span class="ltx_bibblock">Interactive proofs for synthesizing quantum states and unitaries.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">13th Innovations in Theoretical Computer Science Conference
(ITCS 2022)</span>, volume 215 of <span class="ltx_text ltx_font_italic">Leibniz International Proceedings in
Informatics (LIPIcs)</span>, pages 112:1–112:4. Schloss Dagstuhl –
Leibniz-Zentrum für Informatik, 2022.

</span>
<span class="ltx_bibblock">Numbered references are to arXiv version 2.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2108.07192v2" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2108.07192v2</span></a>, <a href="https://doi.org/10.4230/LIPIcs.ITCS.2022.112" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.4230/LIPIcs.ITCS.2022.112</span></a>.

</span>
</li>
      
<li id="bib.bibx48" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Sav70]</span>
<span class="ltx_bibblock">
Walter J. Savitch.

</span>
<span class="ltx_bibblock">Relationships between nondeterministic and deterministic tape
complexities.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Journal of Computer and System Sciences</span>, 4(2):177–192, 1970.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1016/S0022-0000(70)80006-X" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1016/S0022-0000(70)80006-X</span></a>.

</span>
</li>
      
<li id="bib.bibx49" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[SBM06]</span>
<span class="ltx_bibblock">
Vivek V. Shende, Stephen S. Bullock, and Igor L. Markov.

</span>
<span class="ltx_bibblock">Synthesis of quantum-logic circuits.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">IEEE Transactions on Computer-Aided Design of Integrated
Circuits and Systems</span>, 25(6):1000–1010, 2006.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/quant-ph/0406176" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:quant-ph/0406176</span></a>, <a href="https://doi.org/10.1109/TCAD.2005.855930" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1109/TCAD.2005.855930</span></a>.

</span>
</li>
      
<li id="bib.bibx50" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Sch27]</span>
<span class="ltx_bibblock">
Otto Schreier.

</span>
<span class="ltx_bibblock">Die Untergruppen der freien Gruppen.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Abhandlungen aus dem Mathematischen Seminar der Universität
Hamburg</span>, 5(1):161–183, 1927.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1007/BF02952517" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/BF02952517</span></a>.

</span>
</li>
      
<li id="bib.bibx51" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Sio58]</span>
<span class="ltx_bibblock">
Maurice Sion.

</span>
<span class="ltx_bibblock">On general minimax theorems.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Pacific Journal of Mathematics</span>, 8(1):171–176, 1958.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.2140/pjm.1958.8.171" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.2140/pjm.1958.8.171</span></a>.

</span>
</li>
      
<li id="bib.bibx52" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[SM73]</span>
<span class="ltx_bibblock">
Larry J. Stockmeyer and Albert R. Meyer.

</span>
<span class="ltx_bibblock">Word problems requiring exponential time (preliminary report).

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Proceedings of the 5th Annual ACM Symposium on Theory of
Computing (STOC)</span>, pages 1–9. ACM, 1973.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1145/800125.804029" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1145/800125.804029</span></a>.

</span>
</li>
      
<li id="bib.bibx53" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Tof80]</span>
<span class="ltx_bibblock">
Tommaso Toffoli.

</span>
<span class="ltx_bibblock">Reversible computing.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Automata, Languages and Programming (ICALP 1980)</span>, volume 85
of <span class="ltx_text ltx_font_italic">Lecture Notes in Computer Science</span>, pages 632–644. Springer, 1980.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1007/3-540-10003-2_104" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/3-540-10003-2_104</span></a>.

</span>
</li>
      
<li id="bib.bibx54" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Vad12]</span>
<span class="ltx_bibblock">
Salil P. Vadhan.

</span>
<span class="ltx_bibblock">Pseudorandomness.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Foundations and Trends in Theoretical Computer Science</span>,
7(1–3):1–336, 2012.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1561/0400000010" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1561/0400000010</span></a>.

</span>
</li>
      
<li id="bib.bibx55" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Wat99]</span>
<span class="ltx_bibblock">
John Watrous.

</span>
<span class="ltx_bibblock">Space-bounded quantum complexity.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Journal of Computer and System Sciences</span>, 59(2):281–326, 1999.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1006/jcss.1999.1655" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1006/jcss.1999.1655</span></a>.

</span>
</li>
      
<li id="bib.bibx56" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Wat03]</span>
<span class="ltx_bibblock">
John Watrous.

</span>
<span class="ltx_bibblock">On the complexity of simulating space-bounded quantum computations.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Computational Complexity</span>, 12(1–2):48–84, 2003.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1007/s00037-003-0177-8" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/s00037-003-0177-8</span></a>.

</span>
</li>
      
<li id="bib.bibx57" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Yan22]</span>
<span class="ltx_bibblock">
Jun Yan.

</span>
<span class="ltx_bibblock">General properties of quantum bit commitments (extended abstract).

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Advances in Cryptology – ASIACRYPT 2022</span>, volume 13794 of
<span class="ltx_text ltx_font_italic">Lecture Notes in Computer Science</span>, pages 628–657. Springer, 2022.

</span>
<span class="ltx_bibblock">Cryptology ePrint Archive, Paper 2020/1488.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1007/978-3-031-22972-5_22" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/978-3-031-22972-5_22</span></a>.

</span>
</li>
      
<li id="bib.bibx58" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Zha24]</span>
<span class="ltx_bibblock">
Mark Zhandry.

</span>
<span class="ltx_bibblock">The space-time cost of purifying quantum computations.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">15th Innovations in Theoretical Computer Science Conference
(ITCS 2024)</span>, volume 287 of <span class="ltx_text ltx_font_italic">Leibniz International Proceedings in
Informatics (LIPIcs)</span>, pages 102:1–102:22. Schloss Dagstuhl –
Leibniz-Zentrum für Informatik, 2024.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/2401.07974" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:2401.07974</span></a>,
<a href="https://doi.org/10.4230/LIPIcs.ITCS.2024.102" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.4230/LIPIcs.ITCS.2024.102</span></a>.

</span>
</li>
      
<li id="bib.bibx59" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Zha25]</span>
<span class="ltx_bibblock">
Mark Zhandry.

</span>
<span class="ltx_bibblock">How to model unitary oracles.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Advances in Cryptology – CRYPTO 2025</span>, volume 16001 of
<span class="ltx_text ltx_font_italic">Lecture Notes in Computer Science</span>, pages 237–268. Springer, 2025.

</span>
<span class="ltx_bibblock">Cryptology ePrint Archive, Paper 2025/1072.

</span>
<span class="ltx_bibblock"><a href="https://doi.org/10.1007/978-3-032-01878-6_8" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1007/978-3-032-01878-6_8</span></a>.

</span>
</li>
      
<li id="bib.bibx60" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[ZLC00]</span>
<span class="ltx_bibblock">
Xinlan Zhou, Debbie W. Leung, and Isaac L. Chuang.

</span>
<span class="ltx_bibblock">Methodology for quantum logic gate construction.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Physical Review A</span>, 62(5):052316, 2000.

</span>
<span class="ltx_bibblock"><a href="https://arxiv.org/abs/quant-ph/0002039" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">arXiv:quant-ph/0002039</span></a>, <a href="https://doi.org/10.1103/PhysRevA.62.052316" title="" class="ltx_ref ltx_href"><span class="ltx_ref ltx_nolink ltx_path ltx_font_typewriter">doi:10.1103/PhysRevA.62.052316</span></a>.

</span>
</li>
    
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Sichen Wang"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="Unitary Synthesis with a PSPACE Oracle"></div>

</article>
