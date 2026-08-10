---
title: "The Price of Order in the Logarithmic Method"

authors:
  - me
  - Zhipeng Lu
  - Jingbang Chen

# arXiv v1 提交日期
date: 2026-07-26

# 预印本用 manuscript：它是 Hugo Blox 里表示「未经同行评审的稿件」的类型，
# 与 ICML 那篇的 paper-conference 区分开。
#
# publication_short 是列表页徽章的取值。这里写 Preprint 而不是 arXiv 编号或
# 投稿目标会议：编号在一瞥之下不可读、也没人靠 ID 认论文；写目标会议会被读成
# 已录用。Preprint 直接回答读者唯一在意的问题——过没过同行评审。
# 论文录用后把这里改成会议名（如 SODA 2027），徽章自动跟着变。
publication_types: ["manuscript"]
publication: "*Preprint*, arXiv:2608.06388"
publication_short: "Preprint"

# 与 main.tex 的 \begin{abstract} 逐字一致：保留 itemize 的列表结构，数学用原始
# LaTeX（abstract 走 markdownify，KaTeX 扫 document.body，两者都渲染得出来）。
abstract: |
  The logarithmic method is a classical static-to-dynamic transformation: it stores
  one dynamic ordered set as several immutable static components and rebuilds them
  by merges. The same component-and-merge discipline underlies write-optimized
  ordered indexes, where cheap insertions must be reconciled with exact ordered
  queries. In this paper, we study the insertion-only version after $n$ insertions, over
  abstract keys, in a strongly materialized merge-stack model with sequential
  component merges and one forward scan of the live components per query. We bound
  the product between the total amount of data written during the $n$ insertions
  and the worst-case amount of data read by a single query, known as the
  *write-read product*. The optimal bounds are as follows:

  - Membership and local certificates: $\Theta(n\log^2 n)$.
  - Order and range queries with named keys or endpoints: $\Theta(n\log^3 n)$.
  - Select: $\Theta(n^2)$.

  Thus, the logarithmic method does not impose a universal dynamic overhead:
  under materialized one-way access, the optimum depends on what information the
  query reveals before the scan starts. This pinpoints the access-model
  obstruction behind the extra logarithm for exact order and range queries, and
  the quadratic barrier for select.

tags:
  - Data Structures
  - Lower Bounds
  - Write-Optimized Indexes

# featured 是「代表作」机制，目前站上没有任何地方在用它。等论文攒够再统一启用，
# 现在两篇都标或都不标都没有意义。
featured: false

links:
  - type: preprint
    provider: arxiv
    id: 2608.06388
    label: arXiv
---

<article class="ltx_document ltx_authors_1line">





<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="introduction">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">A classical theme in dynamic data structures is to obtain dynamism by
rebuilding static structures in batches. The logarithmic method of Bentley and
Saxe keeps several static structures of different ages and merges them as updates
arrive <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib1" title="Decomposable searching problems I: static-to-dynamic transformation" class="ltx_ref">BS80</a>]</cite>; lower-bound and structural versions go back to
Mehlhorn and Overmars <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib2" title="Lower bounds on the efficiency of transforming static data structures into dynamic structures" class="ltx_ref">MEH81</a>, <a href="#bib.bib30" title="The design of dynamic data structures" class="ltx_ref">OVE83</a>]</cite>. This is also a natural
abstraction of write-optimized ordered storage. The LSM-tree was introduced to
make high-rate updates sequential and cheap <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib22" title="The log-structured merge-tree (LSM-tree)" class="ltx_ref">OCG+96</a>]</cite>; sorted-run
architectures appear in large-scale storage systems and key-value stores such as
Bigtable, Cassandra, MyRocks/RocksDB, WiscKey, and
PebblesDB <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib23" title="Bigtable: a distributed storage system for structured data" class="ltx_ref">CDG+08</a>, <a href="#bib.bib24" title="Cassandra: a decentralized structured storage system" class="ltx_ref">LM10</a>, <a href="#bib.bib27" title="MyRocks: LSM-tree database storage engine serving facebook’s social graph" class="ltx_ref">MDL20</a>, <a href="#bib.bib25" title="WiscKey: separating keys from values in SSD-conscious storage" class="ltx_ref">LPG+17</a>, <a href="#bib.bib26" title="PebblesDB: building key-value stores using fragmented log-structured merge trees" class="ltx_ref">RKC+17</a>]</cite>,
and in cache-oblivious write-optimized search structures <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib35" title="Cache-oblivious streaming B-trees" class="ltx_ref">BFF+07</a>]</cite>.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">The broad area is active because write optimization creates a persistent tension
between update cost, point lookup cost, range-query cost, and space. The systems
literature formulates this tension explicitly through the RUM tradeoff, optimizes
merge policies and filter allocation for point lookups, and designs range filters
or range-query mechanisms for LSM-style stores <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib31" title="Designing access methods: the RUM conjecture" class="ltx_ref">AKM+16</a>, <a href="#bib.bib17" title="Monkey: optimal navigable key-value store" class="ltx_ref">DAI17</a>, <a href="#bib.bib18" title="Dostoevsky: better space-time trade-offs for LSM-tree based key-value stores via adaptive removal of superfluous merging" class="ltx_ref">DI18</a>, <a href="#bib.bib6" title="How to grow an LSM-tree? Towards bridging the gap between theory and practice" class="ltx_ref">MLI25</a>, <a href="#bib.bib33" title="SuRF: practical range query filtering with fast succinct tries" class="ltx_ref">ZLL+18</a>, <a href="#bib.bib34" title="Rosetta: a robust space-time optimized range filter for key-value stores" class="ltx_ref">LCK+20</a>, <a href="#bib.bib32" title="REMIX: efficient range query for LSM-trees" class="ltx_ref">ZCW+21</a>]</cite>.
From a theory point of view, however, these systems raise a more basic question:
what does the logarithmic method itself do to the complexity of ordered-search
queries?</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">At a fixed time, a logarithmic-method structure is not one search tree. It is a
set of independently built sorted components. A point lookup can often be
certified locally in each component, for instance by a hash table or filter. An
exact ordered query is different: predecessor, rank, and exact range queries must
know where the query key, or the interval endpoints, fall inside the relevant
components. Thus the issue is not only the number of components, but also what
kind of information the query must recover inside each component.</p>
</div>
<div id="S1.p4" class="ltx_para ltx_noindent">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Question.</span>
For each query family $Q$, what is the optimal product of amortized write cost
and worst-case read cost for a logarithmic-method ordered set?
Equivalently, if $E$ is the total amount of data written and $\widehat{R}_{Q}$ is the
worst read cost for $Q$, we study</p>
<table id="S1.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$P_{Q}(n)=\inf_{\mathcal{A}}\left(\frac{E_{\mathcal{A}}(n)}{n}\right)\widehat{R}_{\mathcal{A},Q}(n),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">and throughout the paper we report the unnormalized product $E\widehat{R}_{Q}$.</p>
</div>
<div id="S1.p5" class="ltx_para">
<p class="ltx_p">This question is not answered by the closest existing lines of work. Classical
static-to-dynamic transformations analyze the overhead of maintaining many static
structures, but do not separate query families that all have logarithmic static
search cost <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib1" title="Decomposable searching problems I: static-to-dynamic transformation" class="ltx_ref">BS80</a>, <a href="#bib.bib2" title="Lower bounds on the efficiency of transforming static data structures into dynamic structures" class="ltx_ref">MEH81</a>, <a href="#bib.bib30" title="The design of dynamic data structures" class="ltx_ref">OVE83</a>, <a href="#bib.bib5" title="Competitive data-structure dynamization" class="ltx_ref">MRY+21</a>]</cite>.
LSM and write-optimized-storage work optimizes concrete tradeoffs for point and
range queries, but does not give a matching query-by-query lower-bound
classification under a single merge history <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib31" title="Designing access methods: the RUM conjecture" class="ltx_ref">AKM+16</a>, <a href="#bib.bib17" title="Monkey: optimal navigable key-value store" class="ltx_ref">DAI17</a>, <a href="#bib.bib18" title="Dostoevsky: better space-time trade-offs for LSM-tree based key-value stores via adaptive removal of superfluous merging" class="ltx_ref">DI18</a>, <a href="#bib.bib33" title="SuRF: practical range query filtering with fast succinct tries" class="ltx_ref">ZLL+18</a>, <a href="#bib.bib34" title="Rosetta: a robust space-time optimized range filter for key-value stores" class="ltx_ref">LCK+20</a>, <a href="#bib.bib32" title="REMIX: efficient range query for LSM-trees" class="ltx_ref">ZCW+21</a>]</cite>.
Fractional cascading explains how repeated searches across related catalogs can
be shared <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib21" title="Fractional cascading: I. A data structuring technique" class="ltx_ref">CG86</a>, <a href="#bib.bib37" title="Dynamic fractional cascading" class="ltx_ref">MN90</a>, <a href="#bib.bib4" title="A lower bound for dynamic fractional cascading" class="ltx_ref">AFS21</a>]</cite>, but assumes
that the cross-catalog links needed by the search are actually available. Lower
bounds in cell-probe and external-memory models study different access regimes,
where memory cells or blocks can be probed by address <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib38" title="The cell probe complexity of dynamic data structures" class="ltx_ref">FS89</a>, <a href="#bib.bib20" title="Lower bounds for external memory dictionaries" class="ltx_ref">BF03</a>, <a href="#bib.bib39" title="The cell probe complexity of dynamic range counting" class="ltx_ref">LAR12</a>, <a href="#bib.bib40" title="Unifying the landscape of cell-probe lower bounds" class="ltx_ref">PĂT11</a>]</cite>.
Our focus is the restricted but natural merge-stack regime in which components
are written by sequential merges and later read once in chronological order.</p>
</div>
<div id="S1.p6" class="ltx_para">
<p class="ltx_p">The main obstruction is easy to see in a small example. Suppose the current set
is stored in three sorted components $C_{1},C_{2},C_{3}$, scanned in that order. For
membership of a key $x$, each component only has to certify whether $x$ occurs
there. For predecessor or rank of $x$, the query must learn the local gap of $x$
inside each $C_{i}$. A search in $C_{1}$ does not reveal the gap in $C_{2}$ or $C_{3}$
unless some cross-component search shortcut has already been materialized. The
natural algorithmic objection is fractional cascading: repeated searches in many
sorted catalogs are precisely what fractional cascading was designed to remove
<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib21" title="Fractional cascading: I. A data structuring technique" class="ltx_ref">CG86</a>]</cite>, and dynamic variants maintain such links under updates
<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib37" title="Dynamic fractional cascading" class="ltx_ref">MN90</a>, <a href="#bib.bib4" title="A lower bound for dynamic fractional cascading" class="ltx_ref">AFS21</a>]</cite>.</p>
</div>
<div id="S1.p7" class="ltx_para">
<p class="ltx_p">In a materialized one-way merge stack, however, the shortcut has the wrong time
direction. The query scans older components before younger ones. A bridge into a
younger component would have to be encountered in an older component, but the
younger component did not exist when the older one was written. Rewriting the
older component later changes its birth time and moves it behind the younger one
in the scan. Thus the components remain independent sorted catalogs for the
purpose of exact order localization.</p>
</div>
<div id="S1.p8" class="ltx_para">
<p class="ltx_p">We formalize this obstruction in a merge-stack model. An insertion-only ordered
set is stored as immutable sorted <em class="ltx_emph ltx_font_italic">components</em>. Updates append singleton
components and rebuild suffixes by sequential merges. Queries make one forward
pass over the live components, from old to young, and cannot return to a component
after passing it. Our main theorem is for <em class="ltx_emph ltx_font_italic">abstract keys</em>, which can be
compared and hashed but carry no word-RAM coordinate revealing their rank, and for
<em class="ltx_emph ltx_font_italic">strongly materialized</em> components, which are self-contained encodings of
their own keys rather than directories for other components. These assumptions
are the clean setting in which the missing fractional cascade is exposed. The
select query gives the forward scan even less information: it supplies only a
rank $K$, not a target key value, and the threshold key may be in a component that
has already passed under the head.</p>
</div>
<section id="S1.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="our-results">
<span class="ltx_tag ltx_tag_subsection">1.1 </span>Our Results</h3>

<div id="S1.SS1.p1" class="ltx_para">
<p class="ltx_p">The main result is a tight, query-sensitive classification of the logarithmic
method in this model.</p>
</div>
<div id="S1.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 1.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Main Classification)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S1.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">In the strongly materialized merge-stack model over abstract keys, with oblivious
merge schedules and bounded-error randomized query evaluation, the optimal
write-read product satisfies</span></p>
<table id="S1.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\min E\widehat{R}_{Q}=\begin{cases}\Theta(n\log^{2}n),&amp;Q\text{ is locally certifiable in each component},\\[2.84526pt] \Theta(n\log^{3}n),&amp;Q\text{ is a target-key order or exact range query},\\[2.84526pt] \Theta(n^{2}),&amp;Q\text{ is select}.\end{cases}$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Here the first line includes membership, point-emptiness, and global
minimum/maximum. The second line includes predecessor, successor, rank,
range-count, exact range-sum with unit weights, range-minimum, range-maximum, and
bounded-interval emptiness.</span></p>
</div>
</div>
<div id="S1.SS1.p2" class="ltx_para">
<p class="ltx_p">The minimum ranges over all algorithms in the model. The upper bounds are
explicit merge schedules with forward-readable static indexes. The lower bounds
are worst-case over insertion sequences and query instances.</p>
</div>
<div id="S1.SS1.p3" class="ltx_para">
<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_justify ltx_align_top ltx_th ltx_th_column ltx_border_tt" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:95.4pt;"><span class="ltx_text" style="font-size:90%;">family</span></span>
</span>
</th>
<th class="ltx_td ltx_align_justify ltx_align_top ltx_th ltx_th_column ltx_border_tt" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:130.1pt;"><span class="ltx_text" style="font-size:90%;">examples</span></span>
</span>
</th>
<th class="ltx_td ltx_align_justify ltx_align_top ltx_th ltx_th_column ltx_border_tt" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:112.7pt;"><span class="ltx_text" style="font-size:90%;">information available before the scan</span></span>
</span>
</th>
<th class="ltx_td ltx_nopad_r ltx_align_justify ltx_align_top ltx_th ltx_th_column ltx_border_tt" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:65.0pt;"><span class="ltx_text" style="font-size:90%;">product</span></span>
</span>
</th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_t" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:95.4pt;"><span class="ltx_text" style="font-size:90%;">local certificates</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_t" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:130.1pt;"><span class="ltx_text" style="font-size:90%;">membership, point-emptiness, global min/max</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_t" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:112.7pt;"><span class="ltx_text" style="font-size:90%;">a key or constant-size certificate checked component by component</span></span>
</span>
</td>
<td class="ltx_td ltx_nopad_r ltx_align_justify ltx_align_top ltx_border_t" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:65.0pt;">$\Theta(n\log^{2}n)$</span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:95.4pt;"><span class="ltx_text" style="font-size:90%;">target-key order/range</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:130.1pt;"><span class="ltx_text" style="font-size:90%;">predecessor, rank, range-count, exact range aggregates</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:112.7pt;"><span class="ltx_text" style="font-size:90%;">key values or interval endpoints whose local gaps must be found</span></span>
</span>
</td>
<td class="ltx_td ltx_nopad_r ltx_align_justify ltx_align_top" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:65.0pt;">$\Theta(n\log^{3}n)$</span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_bb" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:95.4pt;"><span class="ltx_text" style="font-size:90%;">selection</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_bb" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:130.1pt;"><span class="ltx_text" style="font-size:90%;">select</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_bb" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:112.7pt;"><span class="ltx_text" style="font-size:90%;">only a rank </span>$K$<span class="ltx_text" style="font-size:90%;">, with no target key value</span></span>
</span>
</td>
<td class="ltx_td ltx_nopad_r ltx_align_justify ltx_align_top ltx_border_bb" style="padding:0.8pt 4.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:65.0pt;">$\Theta(n^{2})$</span>
</span>
</td>
</tr>
</tbody>
</table>
</div>
<div id="S1.SS1.p4" class="ltx_para">
<p class="ltx_p"><a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main Classification). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> is not an answer-size separation. Membership, rank, and select
all have $\Theta(\log n)$-bit answers on the hard instances, and rank and select
are inverse operations. The difference is what the scan knows before it starts.
Membership names a key and equality can be checked locally. Predecessor, rank,
and range queries name key values, but exactness requires locating those values
inside each component. Select names no key at all; the answer value is unknown
while early components pass under the one-way scan.</p>
</div>
<div id="S1.SS1.p5" class="ltx_para">
<p class="ltx_p">The assumptions in <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main Classification). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> are also close to the boundary of the
phenomenon. Integer keys reduce the cost of searching within one component;
random access removes the no-backseek difficulty behind select; and
non-materialized cross-component directories can reintroduce fractional-cascading
information. We treat these variants after the main proof, in <a href="#S7" title="7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7</span></a>
and <a href="#A1" title="Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">A</span></a>. They are not part of the headline model, but they help
separate which restriction is responsible for which line of the classification.</p>
</div>
</section>
<section id="S1.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="overview">
<span class="ltx_tag ltx_tag_subsection">1.2 </span>Overview</h3>

<div id="S1.SS2.p1" class="ltx_para">
<p class="ltx_p">The proof has a simple architecture. For each query family we prove a read
barrier at a fixed state, and then combine it with an accounting lemma for all
suffix-merge histories.</p>
</div>
<div id="S1.SS2.p2" class="ltx_para">
<p class="ltx_p">For membership, the fixed-state barrier is the number of live components. Let
$\widehat{W}$ be the maximum number of live components, and let $\widetilde{D}$ be the average
number of times an item is written, including its initial write. The edit floor
and the merge-forest counting lemma give</p>
<table id="S1.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E=\Omega(n\widetilde{D}),\qquad\widetilde{D}\widehat{W}=\Omega(\log^{2}n).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Some membership query must inspect all live components, so $\widehat{R}=\Omega(\widehat{W})$.
This gives $E\widehat{R}=\Omega(n\log^{2}n)$, matched by the balanced Bentley–Saxe
schedule with local hashes.</p>
</div>
<div id="S1.SS2.p3" class="ltx_para">
<p class="ltx_p">For target-key order and range queries, the read barrier is the summed static
search cost in the live components. At a state with component sizes $m_{i}$, we
prove</p>
<table id="S1.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{R}_{\mathrm{ord}}=\Omega\!\left(\sum_{i}\log(m_{i}+1)\right).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The terms add because strong materialization forbids a read in one component from
revealing the private search position of the query key in another component. The
merge-history side then proves the size-diversity law</p>
<table id="S1.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E\cdot\max_{t}\sum_{C\text{ live at }t}\log(|C|+1)=\Omega(n\log^{3}n).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">This is the only extra logarithm in the middle line of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main Classification). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>. Once the
predecessor lower bound is established, direct-sum arguments transfer it to rank,
range-count, exact range-sum, range-minimum, range-maximum, and bounded-interval
emptiness.</p>
</div>
<div id="S1.SS2.p4" class="ltx_para">
<p class="ltx_p">For select, the query is target-free. Consider a boundary in the scan with $P$
stored keys before it and $U$ stored keys after it. We construct a rank query
whose answer is one of $\min\{P,U\}$ possible prefix keys, but the index of the
right key is determined only by suffix information. Since the scan cannot go
back, it must read</p>
<table id="S1.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\Omega(\min\{P,U\})$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">words before crossing the boundary. If the read budget is small, nearly all live
keys must repeatedly sit in one huge component; immutability then forces that
component to be rebuilt many times. This yields $E=\Omega(n^{2}/\widehat{R})$ and hence
$E\widehat{R}=\Omega(n^{2})$.</p>
</div>
<div id="S1.SS2.p5" class="ltx_para">
<p class="ltx_p"><a href="#S2" title="2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a> defines the model, costs, query families, and key assumptions.
<a href="#S3" title="3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a> proves the membership line. <a href="#S4" title="4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a> proves the
no-cascade read floor, the size-diversity law, and the order/range line.
<a href="#S5" title="5 Select ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5</span></a> proves the cut lower bound and the quadratic select line.
<a href="#S6" title="6 Static-to-Dynamic Lifting ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6</span></a> gives a general static-to-dynamic lifting principle for
additive queries. <a href="#S7" title="7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7</span></a> records access-model variants, and
<a href="#A1" title="Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">A</span></a> studies cascades beyond strong materialization.</p>
</div>
</section>
<section id="S1.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="related-works">
<span class="ltx_tag ltx_tag_subsection">1.3 </span>Related Works</h3>

<div id="S1.SS3.p1" class="ltx_para">
<p class="ltx_p">The closest prior work explains pieces of the landscape: dynamization by merging,
write-optimized storage, fractional cascading, and lower bounds in richer memory
models. The following table summarizes why none of these directions already
implies <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main Classification). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>.</p>
</div>
<div id="S1.SS3.p2" class="ltx_para">
<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_justify ltx_align_top ltx_th ltx_th_column ltx_border_tt" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:91.1pt;"><span class="ltx_text" style="font-size:90%;">line of work</span></span>
</span>
</th>
<th class="ltx_td ltx_align_justify ltx_align_top ltx_th ltx_th_column ltx_border_tt" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:130.1pt;"><span class="ltx_text" style="font-size:90%;">what it explains</span></span>
</span>
</th>
<th class="ltx_td ltx_nopad_r ltx_align_justify ltx_align_top ltx_th ltx_th_column ltx_border_tt" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:164.8pt;"><span class="ltx_text" style="font-size:90%;">difference from this paper</span></span>
</span>
</th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_t" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:91.1pt;"><span class="ltx_text" style="font-size:90%;">logarithmic method</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_t" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:130.1pt;"><span class="ltx_text" style="font-size:90%;">how to maintain many rebuilt static structures</span></span>
</span>
</td>
<td class="ltx_td ltx_nopad_r ltx_align_justify ltx_align_top ltx_border_t" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:164.8pt;"><span class="ltx_text" style="font-size:90%;">no classification separating query families with similar static costs</span></span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:91.1pt;"><span class="ltx_text" style="font-size:90%;">LSM and write-optimized storage</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:130.1pt;"><span class="ltx_text" style="font-size:90%;">practical read/write/space tradeoffs for sorted runs</span></span>
</span>
</td>
<td class="ltx_td ltx_nopad_r ltx_align_justify ltx_align_top" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:164.8pt;"><span class="ltx_text" style="font-size:90%;">not a matching lower-bound theorem for membership, order/range, and select under one merge history</span></span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:91.1pt;"><span class="ltx_text" style="font-size:90%;">fractional cascading</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:130.1pt;"><span class="ltx_text" style="font-size:90%;">how to share repeated searches across related catalogs</span></span>
</span>
</td>
<td class="ltx_td ltx_nopad_r ltx_align_justify ltx_align_top" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:164.8pt;"><span class="ltx_text" style="font-size:90%;">the useful bridge has the wrong chronological direction in a materialized one-way merge stack</span></span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_bb" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:91.1pt;"><span class="ltx_text" style="font-size:90%;">cell-probe and external-memory lower bounds</span></span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_bb" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:130.1pt;"><span class="ltx_text" style="font-size:90%;">tradeoffs under random access to cells or blocks</span></span>
</span>
</td>
<td class="ltx_td ltx_nopad_r ltx_align_justify ltx_align_top ltx_border_bb" style="padding:0.7pt 3.0pt;">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:164.8pt;"><span class="ltx_text" style="font-size:90%;">our restriction is not cell access but the order in which materialized information can be read and rewritten</span></span>
</span>
</td>
</tr>
</tbody>
</table>
</div>
<section id="S1.SS3.SSS0.Px1" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="static-to-dynamic-transformations">Static-to-Dynamic Transformations.</h4>

<div id="S1.SS3.SSS0.Px1.p1" class="ltx_para">
<p class="ltx_p">Bentley and Saxe introduced the logarithmic method for decomposable searching
problems <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib1" title="Decomposable searching problems I: static-to-dynamic transformation" class="ltx_ref">BS80</a>]</cite>. Mehlhorn proved lower bounds for such
transformations <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib2" title="Lower bounds on the efficiency of transforming static data structures into dynamic structures" class="ltx_ref">MEH81</a>]</cite>, and Overmars developed a systematic theory
of dynamic structures built from static ones <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib30" title="The design of dynamic data structures" class="ltx_ref">OVE83</a>]</cite>. Recent
competitive dynamization studies merge policies under nonuniform inputs and
read/write ratios <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib5" title="Competitive data-structure dynamization" class="ltx_ref">MRY+21</a>]</cite>. These works explain the overhead of
maintaining many static structures. They do not distinguish query types whose
static problems are all logarithmic; the extra logarithm in <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main Classification). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> is
caused by exact order localization across materialized components.</p>
</div>
</section>
<section id="S1.SS3.SSS0.Px2" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="write-optimized-storage">Write-Optimized Storage.</h4>

<div id="S1.SS3.SSS0.Px2.p1" class="ltx_para">
<p class="ltx_p">The LSM-tree was introduced to make high-rate updates sequential and cheap
<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib22" title="The log-structured merge-tree (LSM-tree)" class="ltx_ref">OCG+96</a>]</cite>. LSM-style sorted runs appear in large-scale storage systems and
key-value stores <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib23" title="Bigtable: a distributed storage system for structured data" class="ltx_ref">CDG+08</a>, <a href="#bib.bib24" title="Cassandra: a decentralized structured storage system" class="ltx_ref">LM10</a>, <a href="#bib.bib27" title="MyRocks: LSM-tree database storage engine serving facebook’s social graph" class="ltx_ref">MDL20</a>, <a href="#bib.bib25" title="WiscKey: separating keys from values in SSD-conscious storage" class="ltx_ref">LPG+17</a>, <a href="#bib.bib26" title="PebblesDB: building key-value stores using fragmented log-structured merge trees" class="ltx_ref">RKC+17</a>]</cite>.
The systems literature maps the read/update/storage tradeoff <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib31" title="Designing access methods: the RUM conjecture" class="ltx_ref">AKM+16</a>]</cite>,
optimizes merge policies and filter allocation for point lookups
<cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib17" title="Monkey: optimal navigable key-value store" class="ltx_ref">DAI17</a>, <a href="#bib.bib18" title="Dostoevsky: better space-time trade-offs for LSM-tree based key-value stores via adaptive removal of superfluous merging" class="ltx_ref">DI18</a>, <a href="#bib.bib6" title="How to grow an LSM-tree? Towards bridging the gap between theory and practice" class="ltx_ref">MLI25</a>]</cite>, and builds succinct or probabilistic
range filters and range-query mechanisms <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib33" title="SuRF: practical range query filtering with fast succinct tries" class="ltx_ref">ZLL+18</a>, <a href="#bib.bib34" title="Rosetta: a robust space-time optimized range filter for key-value stores" class="ltx_ref">LCK+20</a>, <a href="#bib.bib32" title="REMIX: efficient range query for LSM-trees" class="ltx_ref">ZCW+21</a>]</cite>.
This work motivates the access discipline, but it does not prove a tight
query-by-query product classification under the same merge histories.</p>
</div>
</section>
<section id="S1.SS3.SSS0.Px3" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="fractional-cascading">Fractional Cascading.</h4>

<div id="S1.SS3.SSS0.Px3.p1" class="ltx_para">
<p class="ltx_p">Fractional cascading removes repeated binary searches across related catalogs in
static structures <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib21" title="Fractional cascading: I. A data structuring technique" class="ltx_ref">CG86</a>]</cite>; dynamic fractional cascading studies
how to maintain such links under updates <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib37" title="Dynamic fractional cascading" class="ltx_ref">MN90</a>, <a href="#bib.bib4" title="A lower bound for dynamic fractional cascading" class="ltx_ref">AFS21</a>]</cite>.
Our obstruction is orthogonal. The issue is not only the cost of updating a
cascade, but whether the bridge can appear before the component it accelerates is
created. In the strongly materialized one-way model it cannot; <a href="#A1" title="Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">A</span></a>
examines what changes when such cross-component data are allowed.</p>
</div>
</section>
<section id="S1.SS3.SSS0.Px4" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph" id="lower-bounds-and-restricted-access">Lower Bounds and Restricted Access.</h4>

<div id="S1.SS3.SSS0.Px4.p1" class="ltx_para">
<p class="ltx_p">External-memory dictionary lower bounds study update/query tradeoffs under random
block access <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib20" title="Lower bounds for external memory dictionaries" class="ltx_ref">BF03</a>, <a href="#bib.bib7" title="External-memory dictionaries with worst-case update cost" class="ltx_ref">DIN22</a>]</cite>. Cell-probe lower bounds
for dynamic data structures, including dynamic range counting, use a more
powerful random-access memory model <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib38" title="The cell probe complexity of dynamic data structures" class="ltx_ref">FS89</a>, <a href="#bib.bib39" title="The cell probe complexity of dynamic range counting" class="ltx_ref">LAR12</a>, <a href="#bib.bib40" title="Unifying the landscape of cell-probe lower bounds" class="ltx_ref">PĂT11</a>, <a href="#bib.bib41" title="Unifying the landscape of super-logarithmic dynamic cell-probe lower bounds" class="ltx_ref">KO25</a>]</cite>.
Our bounds are orthogonal: component encodings are static and transparent, but the
read and rewrite order is restricted. The lifting theorem in <a href="#S6" title="6 Static-to-Dynamic Lifting ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6</span></a>
connects our merge-stack bounds to static predecessor and range-searching lower
bounds <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib8" title="Time-space trade-offs for predecessor search" class="ltx_ref">PT06</a>, <a href="#bib.bib9" title="Randomization does not help searching predecessors" class="ltx_ref">PT07</a>, <a href="#bib.bib13" title="Lower bounds for 2-dimensional range counting" class="ltx_ref">PĂT07</a>, <a href="#bib.bib14" title="Adaptive and approximate orthogonal range counting" class="ltx_ref">CW13</a>]</cite>.
The merge-history accounting is closest in spirit to list labeling and file
maintenance <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib28" title="A sparse table implementation of priority queues" class="ltx_ref">IKR81</a>, <a href="#bib.bib3" title="Tight lower bounds for the online labeling problem" class="ltx_ref">BKS12</a>, <a href="#bib.bib19" title="Online list labeling: breaking the log2n barrier" class="ltx_ref">BCF+22</a>, <a href="#bib.bib29" title="Nearly optimal list labeling" class="ltx_ref">BCF+24</a>]</cite>; the select lower
bound is related to selection under restricted access <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib36" title="Selection and sorting with limited storage" class="ltx_ref">MP80</a>, <a href="#bib.bib15" title="Generalized selection and ranking: sorted matrices" class="ltx_ref">FJ84</a>, <a href="#bib.bib16" title="Selection from heaps, row-sorted matrices, and +XY using soft heaps" class="ltx_ref">KKZ+19</a>, <a href="#bib.bib42" title="A nearly optimal randomized algorithm for explorable heap selection" class="ltx_ref">BDH+23</a>]</cite>.</p>
</div>
</section>
</section>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="preliminaries">
<span class="ltx_tag ltx_tag_section">2 </span>Preliminaries</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">This section fixes the model used in the main classification. The objects are
merge histories of immutable sorted components, the costs are total rewritten mass
and prefix-worst read cost, and the key assumptions isolate the absence of
cross-component order information.</p>
</div>
<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="merge-histories-and-components">
<span class="ltx_tag ltx_tag_subsection">2.1 </span>Merge Histories and Components</h3>

<div id="S2.SS1.p1" class="ltx_para">
<p class="ltx_p">A <em class="ltx_emph ltx_font_italic">merge stack</em> maintains a sequence of immutable sorted components
$C_{1},\dots,C_{W}$, oldest at the bottom. Each component stores a sorted block of
key-value samples together with any static index built from that block alone.
Three operations maintain it:</p>
<ul id="S2.I1" class="ltx_itemize">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">insert</em>$(x,y)$ pushes a new singleton component $\{(x,y)\}$ on top;</p>
</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">merge</em> pops a suffix $C_{i},\dots,C_{W}$ and pushes a single component
holding the union of their samples in sorted order;</p>
</div>
</li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">query</em> makes one forward pass over $C_{1},C_{2},\dots$ in stack order,
reading component data; after an $O(1)$ header it may skip a component’s body,
but it never returns to an earlier component.</p>
</div>
</li>
</ul>
<p class="ltx_p">Inserts and merges interleave according to a schedule of the algorithm’s choice.
The main lower bounds consider schedules that are oblivious to the key values;
this condition is part of strong materialization below.</p>
</div>
</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="cost-measures">
<span class="ltx_tag ltx_tag_subsection">2.2 </span>Cost Measures</h3>

<div id="S2.SS2.p1" class="ltx_para">
<p class="ltx_p">The <em class="ltx_emph ltx_font_italic">write cost</em> $E$ is the total component data created or rewritten over
the execution. The read cost of a query is the data it reads, and $\widehat{R}$ is its
prefix-worst value: the maximum, over every time $t$ and every query, of the cost
of answering that query against the state after step $t$. Making $\widehat{R}$
prefix-worst keeps the read cost from being amortized away by periodic global
rebuilds, since every intermediate state must remain queryable. For a randomized
evaluator the cost of a query is its expected number of charged reads, and
$\widehat{R}$ is again prefix-worst. The complexity measure throughout is the product
$E\widehat{R}$.</p>
</div>
<div id="S2.SS2.p2" class="ltx_para">
<p class="ltx_p">A token is a machine word of $w=\Theta(\log n)$ bits, and keys and values are drawn
from universes of size $\mathrm{poly}(n)$, so a sample occupies $O(1)$ tokens and a
component of $m$ samples occupies $\Theta(m)$. We use the following notation.</p>
</div>
<div id="S2.SS2.p3" class="ltx_para">
<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_th_row ltx_border_tt" style="padding:0.65pt 5.0pt;"><span class="ltx_text" style="font-size:90%;">symbol</span></th>
<th class="ltx_td ltx_nopad_r ltx_align_left ltx_th ltx_th_column ltx_border_tt" style="padding:0.65pt 5.0pt;"><span class="ltx_text" style="font-size:90%;">meaning</span></th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" style="padding:0.65pt 5.0pt;">$E$</th>
<td class="ltx_td ltx_nopad_r ltx_align_left ltx_border_t" style="padding:0.65pt 5.0pt;"><span class="ltx_text" style="font-size:90%;">total rewritten component data</span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding:0.65pt 5.0pt;">$\widehat{R}_{Q}$</th>
<td class="ltx_td ltx_nopad_r ltx_align_left" style="padding:0.65pt 5.0pt;">
<span class="ltx_text" style="font-size:90%;">prefix-worst read cost for query family </span>$Q$
</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding:0.65pt 5.0pt;">$\widehat{W}$</th>
<td class="ltx_td ltx_nopad_r ltx_align_left" style="padding:0.65pt 5.0pt;"><span class="ltx_text" style="font-size:90%;">maximum number of live components over the execution</span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding:0.65pt 5.0pt;">$\widetilde{D}$</th>
<td class="ltx_td ltx_nopad_r ltx_align_left" style="padding:0.65pt 5.0pt;"><span class="ltx_text" style="font-size:90%;">average item write depth, including the initial write</span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" style="padding:0.65pt 5.0pt;">$L$</th>
<td class="ltx_td ltx_nopad_r ltx_align_left" style="padding:0.65pt 5.0pt;">$\log_{2}n$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb" style="padding:0.65pt 5.0pt;">$\lambda$</th>
<td class="ltx_td ltx_nopad_r ltx_align_left ltx_border_bb" style="padding:0.65pt 5.0pt;">$\log_{2}\log_{2}n$</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="S2.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="query-families">
<span class="ltx_tag ltx_tag_subsection">2.3 </span>Query Families</h3>

<div id="S2.SS3.p1" class="ltx_para">
<p class="ltx_p">Three query types drive the paper. <em class="ltx_emph ltx_font_italic">Membership</em> is the exact-match point
query: given $x$, return its value if $x$ is live and a default otherwise. It is
locally certifiable because equality can be settled inside each component by a
hash or perfect dictionary. <em class="ltx_emph ltx_font_italic">Predecessor</em> is the basic target-key order
query: given $x$, return the value of the largest live key at most $x$. Successor,
rank, and exact range queries – count, sum, minimum, maximum, and emptiness over
an interval – are target-key order or range queries of the same kind, since each
must locate a key value or endpoint in the live order. Membership and these order
queries are <em class="ltx_emph ltx_font_italic">decomposable</em>: an answer combines fixed per-component
contributions. <em class="ltx_emph ltx_font_italic">Select</em> is different. It is given a rank $K$ and returns
the $K$-th smallest live key; no target key value is supplied to the scan. Inserted
keys are distinct, and the lower bounds use distinct-key instances.</p>
</div>
</section>
<section id="S2.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="key-models-and-materialization">
<span class="ltx_tag ltx_tag_subsection">2.4 </span>Key Models and Materialization</h3>

<div id="S2.SS4.p1" class="ltx_para">
<p class="ltx_p">Keys come in two models, and the order separation depends on which one is used.
An <em class="ltx_emph ltx_font_italic">abstract key</em> is the model for string, tuple, or opaque record keys: it is
hashable and comparable, but carries no integer structure. We read it through an
oracle. A key has an opaque equality label and an unknown position in the total
order, and neither the label nor its hash reveals that position. A single read
returns at most one stored key handle together with $O(1)$ control words, and the
handle’s rank among those already read is learned only by comparison. The encoder
cannot manufacture an order-bearing separator it has not read, and an answer must
be a key or value decoded from the words read, not a pointer into an unread cell.
The $O(1)$ control words therefore cannot stand in for the order of a whole block.
An <em class="ltx_emph ltx_font_italic">integer key</em> is an integer in a $\mathrm{poly}(n)$ universe, with the
word-RAM available: a van Emde Boas tree or y-fast trie locates the predecessor
inside a component in $O(\lambda)$ reads, independent of its size, and the order
gap narrows accordingly (<a href="#S7" title="7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7</span></a>).</p>
</div>
<div id="S2.SS4.p2" class="ltx_para">
<p class="ltx_p">The main theorems hold in executions realized by size-based log-structured
merging. Ordinary materialization, which constrains only a component’s contents,
is not enough: once the merge schedule may depend on the data, the partition into
components itself carries order information across them, and an unread block is no
longer free for an adversary to complete. We use the following stronger
condition.</p>
</div>
<div id="S2.Thmtheorem1" class="ltx_theorem ltx_theorem_definition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Strong Materialization)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p">An execution is <em class="ltx_emph ltx_font_italic">strongly materialized</em> if it satisfies the following.</p>
<ul id="S2.I2" class="ltx_itemize">
<li id="S2.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i1.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Canonical updates</em>: after each insertion the active components
partition the inserted samples into contiguous blocks of consecutive
insertion times, and each insertion performs at most one merge, replacing a
suffix of the active components and the new singleton by a single component.</p>
</div>
</li>
<li id="S2.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i2.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Oblivious schedule</em>: the merged suffix at each step depends only on
the step index and the current component sizes, not on the keys, values,
query answers, or any coins.</p>
</div>
</li>
<li id="S2.I2.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i3.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Exact layout</em>: a component of $m$ samples occupies a publicly fixed
length $\ell(m)\in[c_{0}m,c_{1}m]$, so component boundaries, addresses, and the
merge structure are functions of the size sequence alone.</p>
</div>
</li>
<li id="S2.I2.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i4.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">Local encoding</em>: a component’s tokens depend only on its own
samples, their insertion order and values, and comparisons among its own keys;
inputs that agree on every component’s internal order, labels, values, and
insertion history, and differ only in how keys of distinct components
interleave, induce identical component encodings.</p>
</div>
</li>
<li id="S2.I2.i5" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i5.p1" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">No external state</em>: no sample-dependent state persists outside the
components, the query evaluator starts from a data-independent configuration
with coins independent of the data, and every dependence on the data passes
through reads of component tokens.</p>
</div>
</li>
</ul>
</div>
</div>
<div id="S2.SS4.p3" class="ltx_para">
<p class="ltx_p">This is what an LSM run already is, a self-contained sorted file; <a href="#A1" title="Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">A</span></a>
removes the condition and lets a young component share or copy order information
from older ones.</p>
</div>
<div id="S2.SS4.p4" class="ltx_para">
<p class="ltx_p">The per-component arguments use one consequence. Call an execution
<em class="ltx_emph ltx_font_italic">no-cascade</em> if a read in one component cannot shrink another component’s set
of candidate answers. Strong materialization supplies it: changing one block
leaves the partition, every other component’s encoding, and the layout untouched,
so a read elsewhere says nothing about that block. A non-materialized global key
order, searchable by random access, would violate this, the components then
admitting a joint search in $O(\log n)$ reads; random access alone, with the
components still materialized, does not. This locality is what <a href="#A1" title="Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">A</span></a>
gives up.</p>
</div>
<div id="S2.SS4.p5" class="ltx_para">
<p class="ltx_p">The canonical-updates clause is without loss of generality: the merges performed
between two insertions act on nested suffixes of the stack and coalesce into their
final suffix merge, and collapsing them removes the intermediate writes and
queryable states, so neither $E$ nor $\widehat{R}$ grows. Under exact layout the write
cost is structural rather than informational: building a component of $m$ samples
costs $\Theta(m)$ tokens whatever it holds, a fact the edit floor of
<a href="#S3" title="3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a> reads off directly.</p>
</div>
</section>
<section id="S2.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="serialization-and-forward-reads">
<span class="ltx_tag ltx_tag_subsection">2.5 </span>Serialization and Forward Reads</h3>

<div id="S2.SS5.p1" class="ltx_para">
<p class="ltx_p">The lower bounds are cleaner in a low-level view of the same execution. Serialize
the components in stack order into a single token string, each component a
contiguous block preceded by a length-prefix header. Edits become tail operations:
an insert pushes one block at the tail, and a merge of a stack suffix pops the most
recently pushed blocks and pushes one new block. Writing $\mathrm{LCP}$ for the
longest common prefix, the edit $s_{t-1}\to s_{t}$ costs</p>
<table id="S2.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$d_{\mathrm{LIFO}}(s_{t-1},s_{t})=\bigl(|s_{t-1}|-|\mathrm{LCP}|\bigr)+\bigl(|s_{t}|-|\mathrm{LCP}|\bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">the number of tokens popped and pushed at the tail, so
$E=\sum_{t}d_{\mathrm{LIFO}}(s_{t-1},s_{t})$; we call such tail-only edits
<em class="ltx_emph ltx_font_italic">LIFO</em>. A query is run by a <em class="ltx_emph ltx_font_italic">forward, no-backseek</em> head: it starts at
position $0$ and at each step either reads the current token, at unit cost,
advancing one place, or skips forward at no cost by an amount it computes from its
finite control, the query, and the tokens read so far. It never moves backward,
working memory is free, and only reads are charged.</p>
</div>
<div id="S2.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 2.2</span></span><span class="ltx_text ltx_font_bold"> </span>(Serialization Equivalence)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For strongly materialized executions, the merge-stack model and the LIFO-token,
forward-no-backseek model agree up to constant factors in $(E,\widehat{R})$.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS5.p2" class="ltx_para">
<p class="ltx_p">Serialize as above. An insert pushes a block of $\Theta(1)$ tokens at the tail,
and a merge pops exactly the most recently pushed blocks and pushes one new block,
so every edit is tail-only; the pushed token mass equals the rewritten component
data up to the matching pops, a constant factor, so $E_{\mathrm{token}}=\Theta(E)$.
The components occupy the string in stack order, which is birth order and the order
a forward head reads them, and skipping a body after its header is a legal
no-backseek pass, so $\widehat{R}_{\mathrm{token}}=\Theta(\widehat{R})$. Conversely, a
tail-only token execution whose pushed blocks are local encodings of the unions of
the popped blocks splits into contiguous blocks in birth order, since the tokens
pushed at one step are consecutive and share a birth time, and is a merge-stack
execution with the same merge structure.
∎</p>
</div>
</div>
<div id="S2.SS5.p3" class="ltx_para">
<p class="ltx_p">One may therefore keep the merge-stack picture throughout and read the lower-bound
proofs as statements about the token string.</p>
</div>
</section>
<section id="S2.SS6" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="baseline-upper-bounds">
<span class="ltx_tag ltx_tag_subsection">2.6 </span>Baseline Upper Bounds</h3>

<div id="S2.SS6.p1" class="ltx_para">
<p class="ltx_p">The serial Bentley–Saxe transform <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib1" title="Decomposable searching problems I: static-to-dynamic transformation" class="ltx_ref">BS80</a>]</cite> supplies the upper
bounds the lower bounds will match.</p>
</div>
<div id="S2.Thmtheorem3" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Proposition 2.3</span></span><span class="ltx_text ltx_font_bold"> </span>(Bentley–Saxe Baseline)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S2.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">A single schedule has $E=O(n\log n)$ with at most $\lceil\log_{2}(n+1)\rceil$
active components at all times, and answers membership in $\widehat{R}=O(\log n)$,
abstract-key predecessor in $\widehat{R}=O(\log^{2}n)$, and integer predecessor in
$\widehat{R}=O(\lambda\log n)$. The corresponding products are</span></p>
<table id="S2.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E\widehat{R}=O(n\log^{2}n),\qquad O(n\log^{3}n),\qquad O(n\log^{2}n\,\lambda).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.SS6.p2" class="ltx_para">
<p class="ltx_p">Keep the components whose sizes are the set bits of the insert count, merging
equal-sized ones on each insert. A component of size $2^{k}$ is built at most
$n/2^{k}$ times, each at $\Theta(2^{k})$ tokens, so $E=O(n\log n)$, and at most
$\lceil\log_{2}(n+1)\rceil$ components are live at any time. Each component carries
a forward-readable static structure, length-prefixed so the head skips its body
after one header read. A static perfect hash answers membership in $O(1)$ reads
per component, even against an adversarial query, so $\widehat{R}=O(\log n)$. For
abstract-key predecessor, a balanced search tree laid out in search-round order,
all depth-one nodes, then all depth-two, and so on, is traversed root to leaf as a
forward scan of $O(\log m_{k})$ comparison reads in component $k$, summing to
$O(\log^{2}n)$ over the active components. For integer predecessor, a y-fast trie
answers in $O(\lambda)$ reads per component under the same round-by-round layout,
giving $\widehat{R}=O(\lambda\log n)$.
∎</p>
</div>
</div>
<div id="S2.SS6.p3" class="ltx_para">
<p class="ltx_p">The membership and predecessor products are the first the lower bounds match
(<a href="#S3" title="3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Sections</span> <span class="ltx_text ltx_ref_tag">3</span></a> and <a href="#S4" title="4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>); select needs a different schedule and is
polynomially larger (<a href="#S5" title="5 Select ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5</span></a>). How the predecessor bound responds when
these conditions are relaxed, and why the relaxations are not interchangeable, is
the subject of <a href="#S7" title="7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7</span></a>.</p>
</div>
</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="membership">
<span class="ltx_tag ltx_tag_section">3 </span>Membership</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The Bentley–Saxe schedule of <a href="#S2" title="2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a> answers membership with product
$n\log^{2}n$. We show this is best possible, and in doing so establish the three
structural facts the later lower bounds reuse: a level decomposition that the
tail-only discipline forces, an edit floor on the write cost, and a counting
bound that trades depth against frontier. Together they expose the mechanism the
paper turns on, that $E\widehat{R}$ factors into a write budget and a sum of per-level
read charges. Membership is the case where a hash holds every charge at $O(1)$;
order and rank raise it.</p>
</div>
<section id="S3.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="merge-forests">
<span class="ltx_tag ltx_tag_subsection">3.1 </span>Merge Forests</h3>

<div id="S3.SS1.p1" class="ltx_para">
<p class="ltx_p">Fix an execution. A live token in $s_{t}$ has a <em class="ltx_emph ltx_font_italic">birth step</em>, the step at
which it was last pushed, and tokens with a common birth step form a
<em class="ltx_emph ltx_font_italic">level</em>; by <a href="#S2.Thmtheorem2" title="Lemma 2.2 (Serialization Equivalence). ‣ 2.5 Serialization and Forward Reads ‣ 2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> a level is just a component of <a href="#S2" title="2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a>
in token-string form. Write $W(t)$ for the number of live levels at time $t$.</p>
</div>
<div id="S3.Thmtheorem1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Level Decomposition)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">At every time $t$ the live levels are contiguous and ordered by birth,
$s_{t}=L_{t_{1}}\cdots L_{t_{W}}$ with $t_{1}&lt;\cdots&lt;t_{W}$, and the edit $s_{t-1}\to s_{t}$
pops a suffix of them and pushes one new top level.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS1.p2" class="ltx_para">
<p class="ltx_p">A canonical update pops a suffix of the active components and pushes one merged
component (<a href="#S2" title="2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a>). The tokens pushed at one step are consecutive at
the tail and share a birth step, so each level is contiguous and older levels lie
earlier; an edit pops a suffix of whole levels and makes the pushed tokens the
new top level.
∎</p>
</div>
</div>
<div id="S3.SS1.p3" class="ltx_para">
<p class="ltx_p">The decomposition makes the execution a <em class="ltx_emph ltx_font_italic">merge forest</em>: an internal node for
each step that merges, its children the levels popped there and the singleton
inserted then, and a leaf for each insert. Leaf $j$ takes part in $d_{j}$ merges,
one for each of its internal ancestors. The rewritten sample mass is therefore</p>
<table id="S3.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$M:=\sum_{j}d_{j}=\sum_{P}|P|,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">$|P|$ being the number of leaves below the internal node $P$. The forest is fixed by the
schedule alone, whatever the tokens mean, and the lower bounds read off it.</p>
</div>
<div id="S3.SS1.p4" class="ltx_para">
<p class="ltx_p">The hard instances carry their entropy in the values: each inserted value is
independent and uniform over a $\mathrm{poly}(n)$ universe, so it is
$\Theta(\log n)$ bits, the content of one token.</p>
</div>
<div id="S3.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.2</span></span><span class="ltx_text ltx_font_bold"> </span>(Incompressibility)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">On the i.i.d.-value instance, a materialized level that is the sole source for $m$
of its samples occupies $\Omega(m)$ tokens.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS1.p5" class="ltx_para">
<p class="ltx_p">The state must determine those $m$ values, whose joint entropy is
$\Theta(m\log n)$ bits, or $\Theta(m)$ tokens. Materialization places them in this
level alone, so it occupies $\Omega(m)$ tokens.
∎</p>
</div>
</div>
<div id="S3.Thmtheorem3" class="ltx_theorem ltx_theorem_corollary">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Corollary 3.3</span></span><span class="ltx_text ltx_font_bold"> </span>(Edit Floor)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">With <em class="ltx_emph ltx_font_upright">augmented depth</em> $\widetilde{D}:=(M+n)/n$, the write cost is
$E=\Omega(n\widetilde{D})$.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS1.p6" class="ltx_para">
<p class="ltx_p">Under exact layout a level of $m$ samples costs $\Theta(m)$ tokens, so
$E=\Theta(n+M)=\Theta(n\widetilde{D})$. With no layout fixed, <a href="#S3.Thmtheorem2" title="Lemma 3.2 (Incompressibility). ‣ 3.1 Merge Forests ‣ 3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.2</span></a> applies to
each level when it is built, the sole source for its samples at that moment, and
summing over the levels built, of total size $n+M$, gives $E\geq c(n+M)=cn\widetilde{D}$
for a constant $c\in(0,1]$.
∎</p>
</div>
</div>
<div id="S3.SS1.p7" class="ltx_para">
<p class="ltx_p">The third fact ties depth to frontier. Its counting argument is the
online-labeling lemma of Bulánek, Koucký, and Saks <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib3" title="Tight lower bounds for the online labeling problem" class="ltx_ref">BKS12</a>]</cite>, recast in
merge-forest terms. Write $\widehat{W}:=\max_{t}W(t)$ for the <em class="ltx_emph ltx_font_italic">frontier width</em>.</p>
</div>
<div id="S3.Thmtheorem4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.4</span></span><span class="ltx_text ltx_font_bold"> </span>(Frontier Width)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Every merge forest on $n$ leaves with augmented depth $\widetilde{D}$ and frontier width
$\widehat{W}$ has $\widetilde{D}\widehat{W}=\Omega(\log^{2}n)$.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS1.p8" class="ltx_para">
<p class="ltx_p">With a dummy root above the final frontier, a leaf in $d_{j}$ merges has augmented
depth $d_{j}+1$, of mean $\widetilde{D}$. Let $N(h,W)$ be the most leaves an ordered suffix-merge
tree of height at most $h$ can have while its live frontier never exceeds $W$. Its
root pops a suffix of $r\leq W$ children, each a completed subtree that holds a
frontier slot until the merge, together with the singleton inserted then, a
height-$0$ child holding no slot. With $N(0,W)=1$,</p>
<table id="S3.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$N(h,W)\ \leq\ 1+\sum_{q=1}^{W}N(h-1,q)\ \leq\ \sum_{q=0}^{W}\binom{h-1+q}{q}\ =\ \binom{h+W}{W},$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">the singleton being the $q=0$ term and the last step the hockey-stick identity.
For $a\leq b$, $\log_{2}\binom{a+b}{a}\leq a\log_{2}\frac{e(a+b)}{a}=O(\sqrt{ab})$ using
$\log_{2}u\leq 2\sqrt{u}$. By Markov at least $n/2$ leaves have augmented depth at
most $2\widetilde{D}$; keeping them and suppressing empty internal nodes leaves an ordered
tree with at least $n/2$ leaves, height at most $\lceil 2\widetilde{D}\rceil$, and
frontier at most $\widehat{W}$, so</p>
<table id="S3.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\log_{2}\tfrac{n}{2}\ \leq\ \log_{2}\binom{\lceil 2\widetilde{D}\rceil+\widehat{W}}{\widehat{W}}\ =\ O\!\bigl(\sqrt{\widetilde{D}\widehat{W}}\bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">that is $\widetilde{D}\widehat{W}=\Omega(\log^{2}n)$.
∎</p>
</div>
</div>
</section>
<section id="S3.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-membership-bound">
<span class="ltx_tag ltx_tag_subsection">3.2 </span>The Membership Bound</h3>

<div id="S3.SS2.p1" class="ltx_para">
<p class="ltx_p">The read side needs one fact: a forward head must visit every live level.</p>
</div>
<div id="S3.Thmtheorem5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 3.5</span></span><span class="ltx_text ltx_font_bold"> </span>(Sequential Access)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For an oblivious schedule, some strongly materialized realization forces
$\widehat{R}\geq\widehat{W}$ on a fresh membership query against a deterministic evaluator, and
$\widehat{R}\geq\widehat{W}/3$ against a bounded-error one.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS2.p2" class="ltx_para">
<p class="ltx_p">At a time of maximum frontier, take the realization in which every live level
straddles a fresh key $x$ matching none of its samples. Each live level must
be decided on its own, that $x$ is absent there, and under strong materialization
no other level constrains it, so a level left unread can be filled with $x$ by the
adversary, flipping the answer. A deterministic evaluator therefore reads all
$\widehat{W}$ levels, so $\widehat{R}\geq\widehat{W}$. For a bounded-error one, couple this input
with the one in which only level $i$ gains $x$: the transcripts agree until level
$i$ is read, so skipping it makes the evaluator answer both alike and err on one,
and the two error probabilities sum to at least the probability of skipping level
$i$. Bounded error keeps that sum below $\tfrac{2}{3}$, so level $i$ is read with
probability at least $\tfrac{1}{3}$ and $\widehat{R}\geq\widehat{W}/3$. A length header does not
escape the charge, that read being the one counted.
∎</p>
</div>
</div>
<div id="S3.Thmtheorem6" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 3.6</span></span><span class="ltx_text ltx_font_bold"> </span>(Tight Membership Bound)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S3.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Strongly materialized membership has $E\widehat{R}=\Theta(n\log^{2}n)$, attained at
$(E,\widehat{R})=(\Theta(n\log n),\Theta(\log n))$ by hashing on the Bentley–Saxe
schedule.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S3.SS2.p3" class="ltx_para">
<p class="ltx_p">The upper bound is <a href="#S2.Thmtheorem3" title="Proposition 2.3 (Bentley–Saxe Baseline). ‣ 2.6 Baseline Upper Bounds ‣ 2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>. For the lower bound, <a href="#S3.Thmtheorem5" title="Lemma 3.5 (Sequential Access). ‣ 3.2 The Membership Bound ‣ 3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.5</span></a>
gives $\widehat{R}\geq\widehat{W}$, <a href="#S3.Thmtheorem3" title="Corollary 3.3 (Edit Floor). ‣ 3.1 Merge Forests ‣ 3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Corollary</span> <span class="ltx_text ltx_ref_tag">3.3</span></a> gives $E=\Omega(n\widetilde{D})$, and
<a href="#S3.Thmtheorem4" title="Lemma 3.4 (Frontier Width). ‣ 3.1 Merge Forests ‣ 3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.4</span></a> gives $\widetilde{D}\widehat{W}=\Omega(\log^{2}n)$, so
$E\widehat{R}=\Omega(n\widetilde{D}\widehat{W})=\Omega(n\log^{2}n)$.
∎</p>
</div>
</div>
<div id="S3.SS2.p4" class="ltx_para">
<p class="ltx_p">Nothing in the lower bound used what membership computes, only that every live
level must be decided, so $n\log^{2}n$ is a floor for the whole model, reached by
membership. It is robust to randomization through <a href="#S3.Thmtheorem5" title="Lemma 3.5 (Sequential Access). ‣ 3.2 The Membership Bound ‣ 3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.5</span></a>, and it
constrains the tradeoff and not just the product: $\widehat{R}=O(\log n)$ forces
$\widehat{W}=O(\log n)$, hence $\widetilde{D}=\Omega(\log n)$ and $E=\Omega(n\log n)$. Membership
is the hashable extreme, each level settled by one probe. The rest of the paper
keeps this write budget and asks whether the read side can stay at $O(1)$ per
level; once the query needs order, it cannot.</p>
</div>
</section>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="order-queries">
<span class="ltx_tag ltx_tag_section">4 </span>Order Queries</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">This section proves the middle line of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main Classification). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>. The proof has three
steps. First, strong materialization and one-way access rule out the
cross-component shortcut that fractional cascading would need. Second, once the
components cannot share searches, a fixed state with component sizes $m_{i}$ forces
$\Omega(\sum_{i}\log(m_{i}+1))$ reads for a hard predecessor query. Third, every
cheap suffix-merge history exposes some state where this summed log-size is
large, giving the product lower bound $\Omega(n\log^{3}n)$. The final subsection
transfers predecessor to rank and exact range queries.</p>
</div>
<section id="S4.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="no-cascading-across-components">
<span class="ltx_tag ltx_tag_subsection">4.1 </span>No Cascading Across Components</h3>

<div id="S4.SS1.p1" class="ltx_para">
<p class="ltx_p">Membership spends $O(1)$ per level because a hash names where the answer sits.
Order has no such shortcut and cannot build one by linking levels. Call a
<em class="ltx_emph ltx_font_italic">forward bridge</em> from a level $L_{i}$ to a younger level $L_{j}$ any data stored
in $L_{i}$ that lets the head, once it has read $L_{i}$, reach the query’s predecessor
in $L_{j}$ within $O(1)$ further reads.</p>
</div>
<div id="S4.Thmtheorem1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Causal-Bridge Obstruction)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Under forward, no-backseek access with LIFO edits, no forward bridge can be
consulted when it would help.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS1.p2" class="ltx_para">
<p class="ltx_p">Levels are read oldest first (<a href="#S3.Thmtheorem1" title="Lemma 3.1 (Level Decomposition). ‣ 3.1 Merge Forests ‣ 3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">3.1</span></a>). A bridge that speeds up a
younger level $L_{j}$ must be read before $L_{j}$, hence stored in an older level
$L_{i}$; but its content depends on $L_{j}$, fixed only when $L_{j}$ is built, so its
carrier must be younger than $L_{j}$. The two demands collide: when $L_{i}$ was built
$L_{j}$ did not yet exist, and on adversarial independent keys no guess survives.
Rebuilding $L_{i}$ after $L_{j}$ only pushes its birth past $L_{j}$, moving it behind in
read order, and a younger level pointing into an older one is reached only once
the older target has been passed.
∎</p>
</div>
</div>
<div id="S4.SS1.p3" class="ltx_para">
<p class="ltx_p">This is the obstruction behind Afshani’s dynamic fractional-cascading lower
bound <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib4" title="A lower bound for dynamic fractional cascading" class="ltx_ref">AFS21</a>]</cite>, sharpened from a tax to an impossibility: the bridge a
cascade needs would have to be written before its target exists. The other route,
a young level carrying a directory into the older ones, is closed not by access
but by strong materialization, each component encoding only its own samples
(<a href="#S2" title="2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a>); <a href="#A1" title="Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">A</span></a> drops that assumption. What remains is the
cost of searching one level alone.</p>
</div>
<div id="S4.SS1.p4" class="ltx_para">
<p class="ltx_p">Within a level a hash still names one specific key, while the predecessor is
another, fixed by the level’s order, that the hash of $x$ does not reach. Locating
it is a comparison search, and on a level of $m$ keys an adversarial query forces
$\Omega(\log m)$ reads, made precise against a hard gap distribution in
<a href="#S4.Thmtheorem2" title="Lemma 4.2 (Zero-Side Ordered Gap). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>.</p>
</div>
</section>
<section id="S4.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="per-state-search-lower-bound">
<span class="ltx_tag ltx_tag_subsection">4.2 </span>Per-State Search Lower Bound</h3>

<div id="S4.SS2.p1" class="ltx_para">
<p class="ltx_p">Fix a time and write $\Phi(t)=\sum_{\text{active }L}\log_{2}|L|$ for the summed
log-size of the live levels. Since the per-level searches do not combine
(<a href="#S4.Thmtheorem1" title="Lemma 4.1 (Causal-Bridge Obstruction). ‣ 4.1 No Cascading Across Components ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>), the read cost is their sum. This sum is not forced at
every state: with the live levels in disjoint key ranges a single header settles
all but one. What does hold is that each size skeleton, the live levels’ sizes alone, admits
an adversarial key assignment making the sum necessary, which under an oblivious
schedule is all the lower bound needs.</p>
</div>
<div id="S4.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.2</span></span><span class="ltx_text ltx_font_bold"> </span>(Zero-Side Ordered Gap)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix stored keys $k_{1}&lt;\cdots&lt;k_{m}$ and handles $b&lt;x$. For $0\leq j\leq m$ let $Z_{j}$
place $k_{1},\dots,k_{j}&lt;b&lt;x&lt;k_{j+1},\dots,k_{m}$, and for $0\leq j&lt;m$ let $H_{j}$ place
$k_{1},\dots,k_{j}&lt;b&lt;k_{j+1}&lt;x&lt;k_{j+2},\dots,k_{m}$, so the predecessor of $x$ is $b$ on
$Z_{j}$ and $k_{j+1}$ on $H_{j}$. Any randomized comparison tree reads $\Omega(\log(m+1))$ keys in
expectation on $Z_{J}$, $J$ uniform, if it uses the known internal order of the
$k_{r}$, learns the order of an unread key only by reading it, and errs with
probability at most $\tfrac{1}{3}$ over $\{Z_{j},H_{j}\}$.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS2.p2" class="ltx_para">
<p class="ltx_p">Take a deterministic tree first. A read key has three relevant outcomes,
$k_{r}&lt;b$, $b&lt;k_{r}&lt;x$, and $x&lt;k_{r}$. Let $E_{0}$ count the zero instances not answered
$b$, $E_{1}$ the hot instances answered $b$, and $\Lambda$ the distinct $b$-leaves
reached by correctly answered zero instances. The zero instances reaching one leaf
form an interval: if $Z_{a}$ and $Z_{c}$ ($a&lt;c$) share a $b$-leaf then no $k_{r}$ with
$a&lt;r\leq c$ was read, being above $x$ in $Z_{a}$ and below $b$ in $Z_{c}$, so every
$H_{h}$ with $a\leq h&lt;c$ follows the same transcript and is wrongly answered $b$. A
leaf covering $z$ zero instances thus forces $z-1$ hot errors, whence
$\Lambda\geq(m+1)-E_{0}-E_{1}$. Average error at most $\tfrac{5}{12}$ over the uniform
mixture of the $2m+1$ instances gives $E_{0}+E_{1}\leq\tfrac{5}{12}(2m+1)$ and
$\Lambda\geq(m+1)/6$. With one correct zero instance per leaf, at depths
$d_{1},\dots,d_{\Lambda}$, the ternary Kraft inequality $\sum_{\ell}3^{-d_{\ell}}\leq 1$
forces mean depth $\geq\log_{3}\Lambda$, so</p>
<table id="S4.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathbb{E}_{J}[\text{reads on }Z_{J}]\ \geq\ \tfrac{\Lambda}{m+1}\log_{3}\Lambda\ =\ \Omega(\log(m+1)).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">For a randomized tree the coin-fixed error averages at most $\tfrac{1}{3}$, so by
Markov a $\tfrac{1}{5}$ fraction of the fixings have error at most $\tfrac{5}{12}$, and
averaging over them keeps $\Omega(\log(m+1))$.
∎</p>
</div>
</div>
<div id="S4.Thmtheorem3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.3</span></span><span class="ltx_text ltx_font_bold"> </span>(Anchor-and-Zones Floor)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix a public size vector $(m_{1},\dots,m_{W})$ of an oblivious schedule and an
evaluator of error at most $\tfrac{1}{3}$. Some strongly materialized state with these
sizes admits a query $x$ on which the evaluator has
$\widehat{R}\geq c\sum_{i=1}^{W}\log_{2}(m_{i}+1)$, for an absolute $c&gt;0$.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS2.p3" class="ltx_para">
<p class="ltx_p">We average over a distribution of states, so some realization meets the
expectation, and obliviousness makes it carry the prescribed sizes. Take level $1$
as anchor: fix its internal order, draw the query gap uniformly among the $m_{1}$
gaps with a stored lower endpoint, and put $x$ there with $b$ that endpoint.
Locating $b$ is a randomized predecessor search among equally likely gaps, one
ternary split per read, so a bounded-error evaluator spends $\Omega(\log(m_{1}+1))$
reads, and an $O(1)$ header holds only constantly many handles and cannot help.
For $i\geq 2$ fix three private zones, a low slab below every anchor key, a high
slab above $x$, and a hot subzone inside $(b,x)$, all ordered publicly by level
index. Draw $J_{i}$ uniform in $\{0,\dots,m_{i}\}$; the zero placement puts
$k_{i,1},\dots,k_{i,J_{i}}$ in the low slab and the rest in the high slab, and the
hot alternative, when $J_{i}&lt;m_{i}$, moves $k_{i,J_{i}+1}$ into the hot subzone. Expose
all outside information for free, $b$ included. Reading $k_{i,r}$ then reveals only
its zone, comparisons within the level giving the known index order and
comparisons across levels only the public zone order, so nothing finer about
$J_{i}$ is learned without reading level $i$. The task is <a href="#S4.Thmtheorem2" title="Lemma 4.2 (Zero-Side Ordered Gap). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> with
$m=m_{i}$ and inherits its error guarantee, costing $\Omega(\log(m_{i}+1))$. Summing
over the anchor and the levels gives the bound.
∎</p>
</div>
</div>
<div id="S4.SS2.p4" class="ltx_para">
<p class="ltx_p">The floor is existential over the states realizing a skeleton, not a property of
every state; specialized to one read per level it is the randomized membership
floor $\widehat{R}\geq\widehat{W}/3$ of <a href="#S3.Thmtheorem6" title="Theorem 3.6 (Tight Membership Bound). ‣ 3.2 The Membership Bound ‣ 3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">3.6</span></a>. On the hard realization
$\widehat{R}\geq c\sum_{k}\log_{2}(m_{k}+1)\geq c\max\{\widehat{W},\Phi(t)\}$, and the separation turns
on whether a schedule can hold $\Phi$ down throughout while editing for only
$O(n\log n)$. It cannot.</p>
</div>
</section>
<section id="S4.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="merge-history-size-diversity">
<span class="ltx_tag ltx_tag_subsection">4.3 </span>Merge-History Size Diversity</h3>

<div id="S4.SS3.p1" class="ltx_para">
<p class="ltx_p">A logarithm above membership needs $\Phi(t)=\Omega(\log^{2}n)$ at some moment, and
no schedule holds $\Phi$ at the membership scale $O(\log n)$ throughout. The
size-diversity law prices the time-averaged potential from below by the edit
budget. It is an entropy-prefix argument on the merge forest, budget-free, the
budget entering only through the augmented depth $\widetilde{D}$.</p>
</div>
<div id="S4.SS3.p2" class="ltx_para">
<p class="ltx_p">Add a dummy root above the final frontier, with $S_{v_{0}}=n$. For an internal node
$v$ write $S_{v}$ for the leaves below it, $q_{v}=S_{v}/n$, and $z_{v}=\log_{2}S_{v}$; its
children in birth order have sizes $s_{1},\dots,s_{r}$, weights $p_{i}=s_{i}/S_{v}$, entropy
$h_{v}=\sum_{i}p_{i}\log_{2}(1/p_{i})$, and <em class="ltx_emph ltx_font_italic">ordered prefix load</em>
$a_{v}=\sum_{j}p_{j}\sum_{i&lt;j}\log_{2}s_{i}$. A merge coalesces an active suffix, so
$r\leq\widehat{W}+1$.</p>
</div>
<div id="S4.Thmtheorem4" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.4</span></span><span class="ltx_text ltx_font_bold"> </span>(Four Identities)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For every merge forest, exactly and with no budget hypothesis,</span></p>
<table id="S4.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathrm{(I)}\ \tfrac{1}{n}\!\int_{0}^{n}\!\Phi=\sum_{v}q_{v}a_{v},\quad\mathrm{(II)}\ \sum_{v}q_{v}h_{v}=L,\quad\mathrm{(III)}\ \sum_{v}q_{v}h_{v}z_{v}\geq\tfrac{1}{2}L^{2},\quad\mathrm{(IV)}\ \sum_{v}q_{v}=\widetilde{D}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p3" class="ltx_para">
<p class="ltx_p">For (I), read the integral as a sum over the intervals between insertions; it is
the lifetime identity $\int_{0}^{n}\Phi=\sum_{L}\tau_{L}\log_{2}|L|$, where $\tau_{L}$, the
inserts during $L$’s life, equals the mass of $L$’s younger siblings at its
parent, since a LIFO merge carries off exactly the levels younger than $L$. As
$S_{v}a_{v}=\sum_{i}(\sum_{j&gt;i}s_{j})\log_{2}s_{i}=\sum_{i}\tau_{v_{i}}\log_{2}s_{i}$, summing over
$v$ and dividing by $n$ gives (I). For (II) and (III), sample a leaf uniformly and
let $Z_{0}=L&gt;Z_{1}&gt;\cdots\geq 0$ be the log-sizes along its root-to-leaf path, with
$X_{k}=Z_{k}-Z_{k+1}$ and $\sum_{k}X_{k}=L$. At a node $v$ on the path
$\mathbb{E}[X_{k}\mid v]=h_{v}$ and $\Pr[v\text{ on path}]=q_{v}$, giving (II); and
$\sum_{k}Z_{k}X_{k}=\tfrac{1}{2}(\sum_{k}X_{k})^{2}+\tfrac{1}{2}\sum_{k}X_{k}^{2}\geq\tfrac{1}{2}L^{2}$ with
$\mathbb{E}[Z_{k}X_{k}\mid v]=z_{v}h_{v}$, giving (III). For (IV),
$\sum_{v}q_{v}=\tfrac{1}{n}\sum_{\text{leaves}}(d_{j}+1)=\widetilde{D}$, since each leaf has
$d_{j}+1$ internal ancestors.
∎</p>
</div>
</div>
<div id="S4.SS3.p4" class="ltx_para">
<p class="ltx_p">Identity (III) is the engine: entropy weighted by current log-size unavoidably
reaches $\Omega(L^{2})$, exactly. Turning it into a bound on (I) is a local
computation.</p>
</div>
<div id="S4.Thmtheorem5" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.5</span></span><span class="ltx_text ltx_font_bold"> </span>(Local Prefix Bound)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix $\varepsilon\in(0,\tfrac{1}{4})$, $\gamma=\varepsilon^{2}$, $c_{0}=L^{-7}$, and write
$\mu=G^{-1}$ for $G(m)=(m+1)\log_{2}(m+1)-m\log_{2}m$. Uniformly over internal nodes
with $z_{v}\geq\varepsilon L$, $h_{v}\geq c_{0}$, and $r\leq n^{\gamma}+1$,</span></p>
<table id="S4.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$a_{v}\ \geq\ (1-\kappa)\,z_{v}\,\mu(h_{v}),\qquad\kappa\leq\varepsilon+o(1).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p5" class="ltx_para">
<p class="ltx_p">Put $\theta=(\log_{2}r+9\log_{2}L)/(\varepsilon L)$, so $\theta=\varepsilon+o(1)$
under the hypotheses. Call a child <em class="ltx_emph ltx_font_italic">good</em> if $p_{i}\geq 2^{-\theta z_{v}}$, so
$\log_{2}s_{i}=z_{v}+\log_{2}p_{i}\geq(1-\theta)z_{v}$. A bad child has
$p_{i}&lt;2^{-\theta\varepsilon L}=(rL^{9})^{-1}$, so the bad mass is at most $L^{-9}$,
and renormalizing onto the good children shifts the entropy by $O(L^{-8})$ and
hence $\mu$ by a factor $1-o(1)$: since $(\ln\mu)^{\prime}=O(1+1/h)$ and $h_{v}\geq c_{0}$, the
shift in $\ln\mu$ is $O((1+L^{7})L^{-8})=O(L^{-1})$. The maximum-entropy bound, that
a law on $\{0,1,2,\dots\}$ of entropy $h$ has mean at least $\mu(h)$, applied to a
child drawn by $p_{j}$, gives at least $(1-o(1))\mu(h_{v})$ expected earlier good
children; each adds $\geq(1-\theta)z_{v}$ to $a_{v}$, so
$a_{v}\geq(1-\theta-o(1))z_{v}\mu(h_{v})$.
∎</p>
</div>
</div>
<div id="S4.Thmtheorem6" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 4.6</span></span><span class="ltx_text ltx_font_bold"> </span>(Size-Diversity Law)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem6.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Every LIFO merge forest with $\widehat{W}\leq n^{\gamma}$ and $\widetilde{D}\leq L^{6}$ satisfies</span></p>
<table id="S4.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tfrac{1}{n}\!\int_{0}^{n}\!\Phi(t)\,dt\ \geq\ (1-\varepsilon-o(1))\,\widetilde{D}\,L\,\mu\!\Bigl(\tfrac{\beta L}{\widetilde{D}}\Bigr),\qquad\beta=\tfrac{1}{2}-\varepsilon-o(1),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p"><span class="ltx_text ltx_font_italic">so $\max_{t}\Phi(t)$ is at least the same value.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p6" class="ltx_para">
<p class="ltx_p">Discard from (III) the nodes with $z_{v}&lt;\varepsilon L$, contributing at most
$\varepsilon L\sum_{v}q_{v}h_{v}=\varepsilon L^{2}$ by (II), and those with $h_{v}&lt;c_{0}$,
contributing at most $c_{0}L\widetilde{D}=o(L^{2})$ by (IV). The survivors have
$z_{v}\geq\varepsilon L$, $h_{v}\geq c_{0}$, $r\leq\widehat{W}+1\leq n^{\gamma}+1$, and carry
$\sum^{\mathrm{s}}q_{v}h_{v}z_{v}\geq\beta L^{2}$. Write $Y_{v}=q_{v}h_{v}z_{v}/L^{2}$, so
$m_{Y}:=\sum^{\mathrm{s}}Y_{v}\geq\beta$ and
$\sum^{\mathrm{s}}Y_{v}/h_{v}=L^{-2}\sum^{\mathrm{s}}q_{v}z_{v}\leq\widetilde{D}/L$ by (IV). Set
$\varphi(u)=u\,\mu(1/u)$, convex and decreasing, and note
$q_{v}z_{v}\mu(h_{v})=L^{2}Y_{v}\varphi(1/h_{v})$. Identity (I) and the local prefix bound
give</p>
<table id="S4.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tfrac{1}{nL^{2}}\!\int\!\Phi\ \geq\ (1-\kappa)\,m_{Y}\,\mathbb{E}[\varphi(1/h)],$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">the expectation under $Y/m_{Y}$. Jensen and then the monotonicity of $\varphi$ at
$\mathbb{E}[1/h]\leq\widetilde{D}/(Lm_{Y})$ give</p>
<table id="S4.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$m_{Y}\,\mathbb{E}[\varphi(1/h)]\ \geq\ m_{Y}\,\varphi\!\Bigl(\tfrac{\widetilde{D}}{Lm_{Y}}\Bigr)\ =\ \tfrac{\widetilde{D}}{L}\,\mu\!\Bigl(\tfrac{m_{Y}L}{\widetilde{D}}\Bigr)\ \geq\ \tfrac{\widetilde{D}}{L}\,\mu\!\Bigl(\tfrac{\beta L}{\widetilde{D}}\Bigr),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">using $m_{Y}\geq\beta$ and $\mu$ increasing. Multiply by $L^{2}$.
∎</p>
</div>
</div>
<div id="S4.SS3.p7" class="ltx_para">
<p class="ltx_p">The frontier cap is necessary for the law, since the never-merge schedule has
$\Phi\equiv 0$, but it does not constrain the predecessor bound: the assembly below
routes wide-frontier executions through the read floors instead. The cap aside,
the law is the right general form rather than a relaxation, asymptotically tight
along the lazy base-$q$ counter, so the uniform reading $\max_{t}\Phi\geq c\log^{2}n$
for all schedules is false, that family sending $\max_{t}\Phi/\log^{2}n\to 0$ as $q$
grows. Since $\Phi$ depends only on the forest, the bound holds for every
realization of a randomized algorithm.</p>
</div>
<div id="S4.Thmtheorem7" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.7</span></span><span class="ltx_text ltx_font_bold"> </span>(Calculus Floor)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem7.p1" class="ltx_para">
<p class="ltx_p">$\min_{h&gt;0}\mu(h)/h^{2}=\tfrac{1}{4}$<span class="ltx_text ltx_font_italic">, attained only at $h=2$; equivalently
$G(m)\leq 2\sqrt{m}$ with equality iff $m=1$. Hence
$\widetilde{D}^{2}\,\mu(\beta L/\widetilde{D})\geq(\beta^{2}/4)L^{2}$.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS3.p8" class="ltx_para">
<p class="ltx_p">Substituting $m=\mu(h)$, the claim $\mu(h)\geq h^{2}/4$ reads $G(m)\leq 2\sqrt{m}$. Let
$F(m)=2\sqrt{m}-G(m)$, so $F(0^{+})=F(1)=0$ and $F^{\prime}(m)=m^{-1/2}-\log_{2}(1+1/m)$, of the
sign of $1-u(m)$ for $u(m)=\sqrt{m}\,\log_{2}(1+1/m)$. Here $u$ is unimodal, with
$u^{\prime}(m)=0$ at a single point since $(1+1/m)^{m+1}$ decreases strictly to $e$, and
with $u\to 0$ at both ends and $u(1)=1$ it exceeds $1$ on exactly one interval
$(m_{1},1)$. So $F$ rises on $(0,m_{1})$, returns to $F(1)=0$, then rises, giving
$F\geq 0$ with equality only at $m\in\{0,1\}$. The lone interior contact $m=1$ gives
$h=G(1)=2$ and $\mu(2)=1$, so the minimum is $\tfrac{1}{4}$; substituting
$h=\beta L/\widetilde{D}$ gives the last inequality.
∎</p>
</div>
</div>
</section>
<section id="S4.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-predecessor-bound">
<span class="ltx_tag ltx_tag_subsection">4.4 </span>The Predecessor Bound</h3>

<div id="S4.Thmtheorem8" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 4.8</span></span><span class="ltx_text ltx_font_bold"> </span>(Tight Predecessor Bound)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem8.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Every strongly materialized algorithm with a bounded-error evaluator, under no
hypothesis on the frontier $\widehat{W}$ or the budget $M$, has predecessor
$E\widehat{R}=\Omega(n\log^{3}n)$, which binary Bentley–Saxe attains. Predecessor is
$\Theta(n\log^{3}n)$, one clean logarithm above membership.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS4.p1" class="ltx_para">
<p class="ltx_p">The upper bound is <a href="#S2.Thmtheorem3" title="Proposition 2.3 (Bentley–Saxe Baseline). ‣ 2.6 Baseline Upper Bounds ‣ 2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>. Fix the algorithm; its oblivious schedule
fixes the size trajectory and $E$ independently of the keys. Fix
$\varepsilon=10^{-2}$, $\gamma=\varepsilon^{2}$, $\widetilde{D}=(M+n)/n$, and split on the
schedule.</p>
</div>
<div id="S4.SS4.p2" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">(i) $\widehat{W}&gt;n^{\gamma}$.</em> <a href="#S4.Thmtheorem3" title="Lemma 4.3 (Anchor-and-Zones Floor). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> at a maximum-frontier skeleton
gives $\widehat{R}=\Omega(\widehat{W})&gt;\Omega(n^{\gamma})$, and $E\geq n$, so
$E\widehat{R}=\Omega(n^{1+\gamma})\gg n\log^{3}n$.</p>
</div>
<div id="S4.SS4.p3" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">(ii) $\widehat{W}\leq n^{\gamma}$, $\widetilde{D}&gt;L^{6}$.</em> The edit floor gives
$E=\Omega(n\widetilde{D})&gt;\Omega(nL^{6})$ and <a href="#S4.Thmtheorem3" title="Lemma 4.3 (Anchor-and-Zones Floor). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> at the final skeleton,
where $\sum_{k}\log_{2}(m_{k}+1)\geq\log_{2}(n+1)$, gives $\widehat{R}=\Omega(L)$, so
$E\widehat{R}=\Omega(nL^{7})\gg n\log^{3}n$.</p>
</div>
<div id="S4.SS4.p4" class="ltx_para">
<p class="ltx_p"><em class="ltx_emph ltx_font_italic">(iii) $\widehat{W}\leq n^{\gamma}$, $\widetilde{D}\leq L^{6}$.</em> The size-diversity law gives a
time $t^{\star}$ with $\Phi(t^{\star})\geq(1-\varepsilon-o(1))\widetilde{D}L\,\mu(\beta L/\widetilde{D})$;
<a href="#S4.Thmtheorem3" title="Lemma 4.3 (Anchor-and-Zones Floor). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> there gives $\widehat{R}=\Omega(\Phi(t^{\star}))$, the edit floor
gives $E=\Omega(n\widetilde{D})$, and the calculus floor closes it:</p>
<table id="S4.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$E\widehat{R}\ \geq\ \Omega\bigl(nL\cdot\widetilde{D}^{2}\mu(\beta L/\widetilde{D})\bigr)\ \geq\ \Omega\bigl(\tfrac{\beta^{2}}{4}\,nL^{3}\bigr)=\Omega(nL^{3}).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The cases are exhaustive. Obliviousness makes the size trajectory the same on
every input, so the skeleton each case invokes occurs along the execution, and
<a href="#S4.Thmtheorem3" title="Lemma 4.3 (Anchor-and-Zones Floor). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> exhibits a hard realization there; the product is the
algorithm’s worst case over inputs, in expectation over its coins.
∎</p>
</div>
</div>
<div id="S4.SS4.p5" class="ltx_para">
<p class="ltx_p">The bound $\widehat{R}\geq\widehat{W}$ alone yields only $n\log^{2}n$, one logarithm short;
the extra logarithm needs $\widehat{R}=\Omega(\Phi)$ at a high-$\Phi$ time, which the
size-diversity law supplies. Predecessor pays for size diversity, not merely
frontier width: membership is priced by $\widehat{W}$, order by $\Phi$.</p>
</div>
</section>
<section id="S4.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="extensions-to-rank-and-range-queries">
<span class="ltx_tag ltx_tag_subsection">4.5 </span>Extensions to Rank and Range Queries</h3>

<div id="S4.SS5.p1" class="ltx_para">
<p class="ltx_p">Predecessor is one order query among many. Whether a decomposable query pays the
extra logarithm is read off the combiner, from how much of a single block’s
contribution can reach the global answer, and for natural exact queries this takes
one of two sizes. It is $O(1)$ when an $O(1)$-read witness settles a block’s
contribution, as for membership, point-emptiness, and the global minimum or
maximum. It is $\Theta(\log m)$ when the contribution turns on $q$’s position
among a block’s $m$ sorted keys, as for predecessor, successor, rank, range-count,
range-sum, range-minimum, range-maximum, and bounded-interval emptiness. The bridge
to a read floor in the second case is a per-level direct sum, supplied for
predecessor and successor by <a href="#S4.Thmtheorem3" title="Lemma 4.3 (Anchor-and-Zones Floor). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> and for the rest by the two
lemmas below.</p>
</div>
<div id="S4.SS5.p2" class="ltx_para">
<p class="ltx_p">Call $Q$ <em class="ltx_emph ltx_font_italic">additive</em> if $Q(S,q)=\sum_{k}\varphi(L_{k},q)$ in an abelian group,
each contribution $\varphi(B,q)$ a function of $q$’s position in $B$; rank,
range-count, and unit-weight range-sum qualify. Let $g_{Q}(m)$ be the worst-case
reads to compute $\varphi(B,q)$ on one static block of $m$ samples under a hard
distribution $\mathcal{D}_{m}$, and call the family $\{\mathcal{D}_{m}\}$
<em class="ltx_emph ltx_font_italic">embeddable</em> when every active size vector is realized by independent private
blocks and one shared query whose marginal at level $i$ is $\mathcal{D}_{m_{i}}$.</p>
</div>
<div id="S4.Thmtheorem9" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.9</span></span><span class="ltx_text ltx_font_bold"> </span>(Additive Direct Sum)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem9.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">For an additive $Q$ with an embeddable hard family of per-level complexity $g_{Q}$
under an oblivious schedule, the hard realization at time $t$ forces
$\widehat{R}_{Q}\geq\Omega\bigl(\sum_{k}g_{Q}(m_{k})\bigr)$, deterministically and, with $g_{Q}$
the randomized static complexity, against bounded-error evaluators.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS5.p3" class="ltx_para">
<p class="ltx_p">Draw the embedded product instance and fix a level $i$. Run the evaluator from
$B_{i}$’s draw alone, charging its reads inside $L_{i}$ and answering each read outside
$L_{i}$ for free from a block drawn on independent coins from its law given $q$,
which strong materialization and no-cascade make independent of $B_{i}$. The
evaluator returns $Q(S,q)$, and subtracting the $\sum_{j\neq i}\varphi(L_{j},q)$ just
sampled leaves $\varphi(L_{i},q)$ by the group inverse. This is a single-block
evaluator for $\mathcal{D}_{m_{i}}$ whose outside answers are advice independent of
$B_{i}$, so it cannot read $L_{i}$ below the static floor $g_{Q}(m_{i})$. The blocks are
disjoint, so the reads sum.
∎</p>
</div>
</div>
<div id="S4.SS5.p4" class="ltx_para">
<p class="ltx_p">For abstract keys $g_{Q}(m)=\Theta(\log(m+1))$: computing $q$’s position in a block
is the comparison search of <a href="#S4.Thmtheorem2" title="Lemma 4.2 (Zero-Side Ordered Gap). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a>, and a balanced tree matches it.
The lemma then gives $\widehat{R}_{Q}\geq c\sum_{k}\log_{2}(m_{k}+1)$ for rank, range-count, and
unit-weight range-sum, the floor predecessor pays; <a href="#S6" title="6 Static-to-Dynamic Lifting ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">6</span></a> reuses it
with the integer and two-dimensional complexities.</p>
</div>
<div id="S4.Thmtheorem10" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 4.10</span></span><span class="ltx_text ltx_font_bold"> </span>(Idempotent Direct Sum)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem10.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix a public size vector of an oblivious schedule and a bounded-error evaluator.
For bounded-interval emptiness, range-minimum, and range-maximum, each with a
fixed empty-interval default, some strongly materialized state with these sizes admits an interval $I$, empty
in every level, on which the evaluator has $\widehat{R}_{Q}\geq c\sum_{i}\log_{2}(m_{i}+1)$, for
an absolute $c&gt;0$.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS5.p5" class="ltx_para">
<p class="ltx_p">Give each level $i$ a low slab below $I$, a high slab above $I$, and a hot
subinterval inside $I$, the zones disjoint and ordered publicly by level index.
Draw $J_{i}$ uniform in $\{0,\dots,m_{i}\}$, placing the first $J_{i}$ keys of level $i$
in its low slab and the rest in its high slab, so $I$ holds no key and $Q$ returns
its default; the hot alternative, when $J_{i}&lt;m_{i}$, moves $k_{i,J_{i}+1}$ into the hot
subinterval, making $I$ nonempty and changing the answer while every other
encoding stays fixed. Expose every level but $i$ in its empty state for free;
deciding the global answer is then deciding whether level $i$ leaves $I$ empty,
the task of <a href="#S4.Thmtheorem2" title="Lemma 4.2 (Zero-Side Ordered Gap). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.2</span></a> with $m=m_{i}$ and the endpoints of $I$ as the two
handles, at $\Omega(\log(m_{i}+1))$ reads. By no-cascade, reads elsewhere do not help,
the per-level costs sum, and some all-empty realization meets the bound.
∎</p>
</div>
</div>
<div id="S4.Thmtheorem11" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 4.11</span></span><span class="ltx_text ltx_font_bold"> </span>(Order/Range Dichotomy)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S4.Thmtheorem11.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">A decomposable query has $E\widehat{R}_{Q}=\Theta(n\log^{2}n)$ when an $O(1)$-read per-level
certificate settles it and some unread live level can change its answer, as with
membership, point-emptiness, and the global extrema. When instead a level’s
contribution turns on $q$’s position among its keys, as for predecessor and
successor, the additive rank, range-count, and range-sum, and the idempotent
range-minimum, range-maximum, and bounded-interval emptiness, the cost is
$E\widehat{R}_{Q}=\Theta(n\log^{3}n)$, with no hypothesis on frontier or budget.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S4.SS5.p6" class="ltx_para">
<p class="ltx_p">On the cheap side an $O(1)$-read witness per level answers $Q$ in
$\widehat{R}=O(W)=O(\log n)$, hence $E\widehat{R}=O(n\log^{2}n)$, matched below by the
membership floor of <a href="#S3" title="3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a>, whose argument needs only that an unread
live level can flip the answer. On the order-localizing side the direct sums give
$\widehat{R}_{Q}\geq c\sum_{k}\log_{2}(m_{k}+1)\geq c\max\{\widehat{W},\Phi(t)\}$ on the hard skeleton,
predecessor’s own floor: <a href="#S4.Thmtheorem3" title="Lemma 4.3 (Anchor-and-Zones Floor). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> for predecessor and, reversing the
order, successor; <a href="#S4.Thmtheorem9" title="Lemma 4.9 (Additive Direct Sum). ‣ 4.5 Extensions to Rank and Range Queries ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a> for rank, range-count, and unit-weight
range-sum; and <a href="#S4.Thmtheorem10" title="Lemma 4.10 (Idempotent Direct Sum). ‣ 4.5 Extensions to Rank and Range Queries ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.10</span></a> for the idempotent range queries, where an
empty query interval keeps every level pivotal. The three-case assembly of
<a href="#S4.Thmtheorem8" title="Theorem 4.8 (Tight Predecessor Bound). ‣ 4.4 The Predecessor Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.8</span></a> then gives $\Omega(n\log^{3}n)$, attained by binary
Bentley–Saxe carrying the matching static structure, a balanced tree with subtree
counts, prefix sums, or subtree extrema, at $O(\log m_{k})$ reads per level.
∎</p>
</div>
</div>
<div id="S4.SS5.p7" class="ltx_para">
<p class="ltx_p">The line is hashing against within-level order localization: membership and
point-emptiness fall to a hash and the global extrema to one stored value per
level, all staying at the membership scale, while predecessor, successor, rank,
and the range queries turn on $q$’s position in each block and pay the logarithm.
Total count is cheaper still, fixed by the public size sequence at $\Theta(n)$ and
lying outside the trichotomy. What the logarithm buys is exactness of the order. The idempotent range queries
carry no group inverse, yet an empty interval makes
every level pivotal, a single hidden key overturning the empty default
(<a href="#S4.Thmtheorem10" title="Lemma 4.10 (Idempotent Direct Sum). ‣ 4.5 Extensions to Rank and Range Queries ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.10</span></a>). The logarithm is specific to abstract keys, and integer
keys shrink it (<a href="#S7" title="7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7</span></a>).</p>
</div>
<div id="S4.Thmtheorem12" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 4.12</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S4.Thmtheorem12.p1" class="ltx_para">
<p class="ltx_p">Approximation refunds the logarithm. A constant additive error $\pm\varepsilon n$
in rank or range-count, or a constant-precision quantile, separates only $O(1)$
buckets and returns the query to $\Theta(n\log^{2}n)$; a multiplicative error keeps
the $\Theta(\log n)$ scales and does not.</p>
</div>
</div>
</section>
</section>
<section id="S5" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="select">
<span class="ltx_tag ltx_tag_section">5 </span>Select</h2>

<div id="S5.p1" class="ltx_para">
<p class="ltx_p">Select proves the third line of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main Classification). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a>. Rank is a key-to-count query: the
query names a key, and each component contributes a count. Select is the inverse,
count-to-key query: the query names only a rank $K$. In a one-way scan the key
that will become the answer is not known while the early components are being
read, and those components cannot be revisited once later components reveal the
threshold. The proof first turns this target-free difficulty into a cut lower
bound, and then shows that any structure with small read cost must repeatedly
rebuild a large component.</p>
</div>
<section id="S5.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-cut-lower-bound">
<span class="ltx_tag ltx_tag_subsection">5.1 </span>The Cut Lower Bound</h3>

<div id="S5.SS1.p1" class="ltx_para">
<p class="ltx_p">Comparisons among keys already read are free, so the lower bound is on token reads
and the adversary attacks the unread keys. Two lemmas carry it: a bound on what a
single read can learn, and a cut floor built from it.</p>
</div>
<div id="S5.Thmtheorem1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Layout Channel)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Fix the query $q$, its coins $\rho$, and the data-independent initial
configuration $\sigma_{0}$. Condition on the public layout $G$, the size sequence
together with the boundaries and addresses it determines. Let $X$ be the
stored keys and values. For one run of the forward head let $T$ be its number of
charged reads and $\Pi$ its transcript, the words it reads together with its
working memory. Then</span></p>
<table id="S5.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$I(X;\Pi\mid G,q,\rho,\sigma_{0})\ \leq\ b\,\mathbb{E}[T\mid G,q,\rho,\sigma_{0}]\ =\ O\bigl(\mathbb{E}[T]\log n\bigr),\qquad b=\Theta(\log n).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS1.p2" class="ltx_para">
<p class="ltx_p">Assume $\mathbb{E}[T]&lt;\infty$, the bound being vacuous otherwise, and condition
throughout on $G,q,\rho,\sigma_{0}$. Record the $k$-th read as $V_{k}=(A_{k},Y_{k})$ when
$T\geq k$ and $V_{k}=\bot$ otherwise, where $A_{k}$ is the address read and $Y_{k}$ the
returned word together with the rank of its handle among those already read. A
query reads at most the $O(n)$ live tokens, so that rank fits in $O(\log n)$ bits
and $Y_{k}$ carries $b=\Theta(\log n)$ bits. The head is deterministic given the
conditioning and the reads so far, so $\{T\geq k\}$ is a function of
$V_{1},\dots,V_{k-1}$, and on that event so is $A_{k}$, by <a href="#S2.Thmtheorem1" title="Definition 2.1 (Strong Materialization). ‣ 2.4 Key Models and Materialization ‣ 2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Definition</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>; hence
$I(X;A_{k}\mid V_{&lt;k})=0$ and</p>
<table id="S5.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$I(X;V_{k}\mid V_{&lt;k})\ \leq\ H(Y_{k}\mid V_{&lt;k},A_{k})\ \leq\ b.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">Since $V_{k}=\bot$ when $T&lt;k$, chain rule over $k\leq K$ gives
$I(X;V_{1},\dots,V_{K})\leq b\,\mathbb{E}[\min\{T,K\}]$, and $K\to\infty$ gives
$I(X;V^{\infty})\leq b\,\mathbb{E}[T]$. The transcript $\Pi$ is a function of the
conditioning and $V^{\infty}$ by the no-external-state clause, so data processing
closes it.
∎</p>
</div>
</div>
<div id="S5.SS1.p3" class="ltx_para">
<p class="ltx_p">For a randomized evaluator the coins $\rho$ are independent of the data, so the
bound holds with $\Pi$ replaced by $(\Pi,\rho)$ and averaged over $\rho$.</p>
</div>
<div id="S5.Thmtheorem2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Lemma 5.2</span></span><span class="ltx_text ltx_font_bold"> </span>(Cut Floor)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">At a boundary between two active levels holding $P$ samples before it and $U$
after, with $r=\min\{P,U\}$, some input family with the fixed rank $K=r$ forces
every bounded-error forward evaluator to read $\Omega(r)$ words before the head
crosses the boundary. Hence $\widehat{R}(t)\geq c\min\{P,U\}$ for an absolute $c&gt;0$.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS1.p4" class="ltx_para">
<p class="ltx_p">Place $r$ disjoint rank slabs $S_{1}&lt;\cdots&lt;S_{r}$ in the prefix, separated by fixed
guards, each slab a public range of $Q=\mathrm{poly}(n)$ candidate positions. Draw
$a_{i}$ uniformly and independently from $S_{i}$ and let $Z_{i}$ name which candidate it
is, so the $a_{i}$ carry $\Theta(\log n)$ independent bits while their order is fixed
by the slabs; put the remaining $P-r$ prefix keys in a guard above $S_{r}$. The
suffix encodes an index $j$: place $r-j$ of its keys in a guard below $S_{1}$ and the
rest in a guard above every slab. Then exactly $r-j$ suffix keys and the $j-1$
slab keys $a_{1},\dots,a_{j-1}$ lie below $a_{j}$, so $a_{j}$ is the $r$-th smallest of
the union, while the prefix and the rank $K=r$ are the same for every $j$.</p>
</div>
<div id="S5.SS1.p5" class="ltx_para">
<p class="ltx_p">Draw $J$ uniform on $\{1,\dots,r\}$, independent of $Z=(Z_{1},\dots,Z_{r})$, and let
$\Pi$ be the transcript and coins at the crossing. The prefix is read before the
crossing and does not depend on $J$, so $(Z,\Pi)$ is independent of $J$, while the
suffix determines $J$ and carries nothing about $Z$. A correct answer is $a_{J}$,
which the head must decode from $\Pi$ and $J$ since it cannot return to the prefix;
so by Fano $I(Z_{j};\Pi\mid J=j)=\Omega(\log Q)$, equal to $I(Z_{j};\Pi)$ by that
independence. As the $Z_{i}$ are independent,
$I(Z;\Pi)\geq\sum_{i}I(Z_{i};\Pi)=\Omega(r\log n)$. Since $Z$ is a function of $X$ and
$\Pi$ records the $T$ prefix reads, <a href="#S5.Thmtheorem1" title="Lemma 5.1 (Layout Channel). ‣ 5.1 The Cut Lower Bound ‣ 5 Select ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.1</span></a> gives
$\Omega(r\log n)\leq I(X;\Pi)\leq O(\mathbb{E}[T]\log n)$, whence $\mathbb{E}[T]=\Omega(r)$ and $\widehat{R}(t)\geq\mathbb{E}[T]=\Omega(r)$.
∎</p>
</div>
</div>
<div id="S5.SS1.p6" class="ltx_para">
<p class="ltx_p">The guards keep the suffix clear of $Z$: its keys sit in fixed slabs, never at a
data-dependent value such as $a_{1}-1$, so reading them reveals only $j$. The floor
rests on a single boundary rather than a sum over levels, but that is enough: a
low read cost forces almost all the live mass into one level, and building such a
level again and again is the write cost select cannot escape.</p>
</div>
</section>
<section id="S5.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="the-quadratic-product-bound">
<span class="ltx_tag ltx_tag_subsection">5.2 </span>The Quadratic Product Bound</h3>

<div id="S5.Thmtheorem3" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 5.3</span></span><span class="ltx_text ltx_font_bold"> </span>(Quadratic Select Bound)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S5.Thmtheorem3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Strongly materialized select has $\min E\widehat{R}=\Theta(n^{2})$, with no hypothesis on
the frontier or the budget, and the lower bound holds against bounded-error query
randomization.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S5.SS2.p1" class="ltx_para">
<p class="ltx_p">Write $R=\widehat{R}$ and $s=R/c$ with $c$ the constant of <a href="#S5.Thmtheorem2" title="Lemma 5.2 (Cut Floor). ‣ 5.1 The Cut Lower Bound ‣ 5 Select ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">5.2</span></a>. The live
mass at time $t$ is $t$, and at every boundary $\min\{P,U\}\leq R/c=s$, so each
boundary mass is $\leq s$ or $\geq t-s$ and the level spanning $(s,t-s)$ has size
$\geq t-2s$. Suppose $R&lt;cn/8$, so $s&lt;n/8$ and this level exceeds $n/4$ throughout
$t\in[n/2,n]$. Take times $t_{0}&lt;\cdots&lt;t_{K}$ spaced by $\Delta=\lceil 2s\rceil+1$
across $[n/2,n]$, so $K=\Omega(n/(R+1))$, and let $B_{i}$ be such a level at $t_{i}$.
Being materialized, $B_{i}$ is static after birth, so $|B_{i}|\leq t_{i}$, while
$|B_{i+1}|\geq t_{i+1}-2s&gt;t_{i}\geq|B_{i}|$; the $B_{i}$ are therefore distinct components,
each costing $\Omega(n)$ tokens. Hence $E=\Omega(n^{2}/(R+1))$, and as $R\geq 1$,
$E\widehat{R}=\Omega(n^{2})$. If instead $R\geq cn/8$, then $E\geq n$ gives
$E\widehat{R}\geq nR=\Omega(n^{2})$.</p>
</div>
<div id="S5.SS2.p2" class="ltx_para">
<p class="ltx_p">For the upper bound, keep one large level together with a suffix of at most $s$
singletons, merging the whole stack into a fresh large level every $s$ inserts.
Rebuilding the large level at sizes $s,2s,\dots,n$ costs $E=\Theta(n^{2}/s)$. The large
level is a sorted array at the bottom of the stack, so the head jumps by a computed
offset to its rank window $[K-s,K]$, reads those $O(s)$ keys and the $\leq s$
singletons above it, and selects the global $K$-th among these candidates; the
suffix shifts the answer’s rank in the large level by at most $s$, so the window
holds it, and $\widehat{R}=O(s)$. The product is $\Theta(n^{2})$ at every $s$.
∎</p>
</div>
</div>
<div id="S5.SS2.p3" class="ltx_para">
<p class="ltx_p">The three query classes now stand in a line, governed by what the query hands the
forward head:</p>
<table id="S5.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\underbrace{\Theta(n\log^{2}n)}_{\text{hashable witness}}\ &lt;\ \underbrace{\Theta(n\log^{3}n)}_{\text{known key value}}\ \ll\ \underbrace{\Theta(n^{2})}_{\text{rank, no value}}.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The first gap is one logarithm, order against hashing; the second is a polynomial. Rank and select are inverse operations, value to count and
count to value, and select’s answer is itself only $O(\log n)$ bits, yet the two
lie polynomially apart: the gap is made by the access discipline, not by the
information in the answer. Select gives the head no value to aim at, and that is
what carries it past predecessor. The cost is a property of the forward head, not of
the key model, since the lower bound forces its reads by completing cells the head
has not visited and never inspects a key’s representation; it therefore persists
for integer keys, where the word-RAM that narrows the order gap (<a href="#S7" title="7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7</span></a>)
still leaves select at $\Theta(n^{2})$.</p>
</div>
<div id="S5.Thmtheorem4" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 5.4</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S5.Thmtheorem4.p1" class="ltx_para">
<p class="ltx_p">Constant-precision approximate select returns to $\Theta(n\log^{2}n)$: $O(1)$
samples at evenly spaced ranks per level form a forward quantile sketch that needs
no refinement of the exact threshold. Exactness is again what the cost buys.</p>
</div>
</div>
<div id="S5.Thmtheorem5" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 5.5</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S5.Thmtheorem5.p1" class="ltx_para">
<p class="ltx_p">A cross-level rank catalog would answer select in $O(1)$ reads, but maintaining one
under LIFO appears to cost $\Omega(n^{2})$ edits, which would carry the $\Theta(n^{2})$
past strong materialization, as <a href="#A1" title="Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix</span> <span class="ltx_text ltx_ref_tag">A</span></a> carries the predecessor bound. We
do not pursue this here.</p>
</div>
</div>
</section>
</section>
<section id="S6" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="static-to-dynamic-lifting">
<span class="ltx_tag ltx_tag_section">6 </span>Static-to-Dynamic Lifting</h2>

<div id="S6.p1" class="ltx_para">
<p class="ltx_p">Every query that pays the order logarithm lands at the same $n\log^{3}n$, and a
single reduction explains why. Each pays, per level, the static cost of locating
the query there; the model forbids sharing those costs across levels, so the read
cost is their sum. For an additive query this turns the dynamization optimum into
the edit budget times a sum of static per-level complexities, a dynamic lower bound
read off a static one. The logarithm of order is then no artifact of maintenance
but the faithful lift of a static search cost.</p>
</div>
<div id="S6.p2" class="ltx_para">
<p class="ltx_p">Recall the additive queries of <a href="#S4" title="4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a>: $Q(S,q)=\sum_{k}\varphi(L_{k},q)$ in
an abelian group, with per-level static complexity $g_{Q}(m)$, the reads to compute
one block’s contribution $\varphi(B,q)$, and embeddable hard families that plant an
independent
instance in every level (<a href="#S4.Thmtheorem9" title="Lemma 4.9 (Additive Direct Sum). ‣ 4.5 Extensions to Rank and Range Queries ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a>).</p>
</div>
<div id="S6.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 6.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Static-to-Dynamic Lifting)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S6.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $Q$ be additive with an embeddable hard family and per-level static complexity
$g_{Q}$: a forward-readable static structure attains $O(g_{Q}(m))$ reads on a block of
$m$ samples, and the hard family forces $\Omega(g_{Q}(m))$. Suppose $g_{Q}$ is
nondecreasing with $g_{Q}(1)\geq 1$ and of linear rate $g_{Q}(2^{k})\geq\zeta_{Q}k$ for some
$\zeta_{Q}\in(0,1]$, and $\Sigma_{Q}:=\sum_{k=0}^{L}g_{Q}(2^{k})=\Theta(\zeta_{Q}L^{2})$. Then
every strongly materialized algorithm with a bounded-error evaluator has
$E\widehat{R}_{Q}=\Omega(nL\,\Sigma_{Q})$, which binary Bentley–Saxe attains, so
$\min E\widehat{R}_{Q}=\Theta(nL\,\Sigma_{Q})$.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S6.p3" class="ltx_para">
<p class="ltx_p">For the upper bound, the schedule of <a href="#S2.Thmtheorem3" title="Proposition 2.3 (Bentley–Saxe Baseline). ‣ 2.6 Baseline Upper Bounds ‣ 2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">2.3</span></a> carries that static
structure at each level, a balanced search tree with subtree aggregates for the
additive queries. Then $E=O(nL)$, and the active sizes being distinct powers of
two, $\widehat{R}=\sum_{\text{active}}g_{Q}(m_{k})\leq\Sigma_{Q}$.</p>
</div>
<div id="S6.p4" class="ltx_para">
<p class="ltx_p">For the lower bound, <a href="#S4.Thmtheorem9" title="Lemma 4.9 (Additive Direct Sum). ‣ 4.5 Extensions to Rank and Range Queries ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.9</span></a> gives
$\widehat{R}_{Q}(t)=\Omega(\sum_{k}g_{Q}(m_{k}))$; the linear rate and the floor $g_{Q}(1)\geq 1$
make $g_{Q}(m)=\Omega(\zeta_{Q}\log_{2}(m+1))$, so
$\widehat{R}_{Q}(t)=\Omega(\zeta_{Q}\sum_{k}\log_{2}(m_{k}+1))$. Since $\sum_{k}\log_{2}(m_{k}+1)$ is at
least $\max\{W(t),\Phi(t)\}$ at all times and at least $\log_{2}(n+1)$ at the final
skeleton, this is the read floor of <a href="#S4.Thmtheorem8" title="Theorem 4.8 (Tight Predecessor Bound). ‣ 4.4 The Predecessor Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.8</span></a> scaled by $\zeta_{Q}$. Its
three-case assembly then applies: the wide-frontier and deep cases exceed
$nL\,\Sigma_{Q}$, while the size-diversity case multiplies $E=\Omega(n\widetilde{D})$ by
$\widehat{R}_{Q}=\Omega(\zeta_{Q}\Phi(t^{\star}))$ and closes with the calculus floor, giving
$E\widehat{R}_{Q}=\Omega(\zeta_{Q}nL^{3})$. By $\Sigma_{Q}=\Theta(\zeta_{Q}L^{2})$ this is
$\Omega(nL\,\Sigma_{Q})$.
∎</p>
</div>
</div>
<div id="S6.p5" class="ltx_para">
<p class="ltx_p">The middle row of the dichotomy is now one line: abstract-key rank, range-count,
and range-sum have $g_{Q}(m)=\Theta(\log(m+1))$, hence $\zeta_{Q}=\Theta(1)$,
$\Sigma_{Q}=\Theta(L^{2})$, and $E\widehat{R}_{Q}=\Theta(nL^{3})$. Beyond recovering the additive
row of <a href="#S4.Thmtheorem11" title="Theorem 4.11 (Order/Range Dichotomy). ‣ 4.5 Extensions to Rank and Range Queries ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">4.11</span></a>, the lift names the structure of the cost. The read
bound is a sum of per-level static search complexities, one term per live level,
because maintenance does not inflate a single level and cascading cannot amortize
across them. That this sum cannot stay below $L^{2}$ is the size-diversity of
<a href="#S4" title="4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">4</span></a>: that section forces the sum up to $L^{2}$, and this one explains why
the cost is that sum to begin with. The two are the lower-bound face and the
structural face of the same $n\log^{3}n$.</p>
</div>
<div id="S6.Thmtheorem2" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_italic">Remark 6.2</span></span><span class="ltx_text ltx_font_italic">.</span>
</h6>
<div id="S6.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p">Because $g_{Q}$ is a static complexity, the lift inherits its robustness. Integer keys
shrink the per-level cost and carry rank, range-count, and range-sum to
$\Theta(n\log^{2}n\,\lambda)$, while in two dimensions the separation survives the
word-RAM, with range-counting lifting to $\Theta(n\log^{3}n/\lambda)$ and no van Emde
Boas collapse. Both are taken up in <a href="#S7" title="7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">7</span></a>; the integer bounds there are
deterministic and Las Vegas cell-probe bounds, and a bounded-error version would
need a randomized static one. Integer predecessor, not an additive
query, stays open between $1$ and $\lambda$.</p>
</div>
</div>
</section>
<section id="S7" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="access-model-variants">
<span class="ltx_tag ltx_tag_section">7 </span>Access-Model Variants</h2>

<div id="S7.p1" class="ltx_para">
<p class="ltx_p">The classification of <a href="#S1.Thmtheorem1" title="Theorem 1.1 (Main Classification). ‣ 1.1 Our Results ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1.1</span></a> is stated for abstract keys, strong
materialization, and one-way scans. This section records what happens when one
restriction at a time is relaxed. These variants are not needed for the main
lower bounds; their role is to identify which assumption supports which
separation. Integer keys reduce the cost of searching inside one component,
random access removes the no-backseek obstruction for select, and
non-materialized cascade data can remove the abstract-key predecessor gap only
when it can be placed in the right scan direction.</p>
</div>
<section id="S7.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="integer-keys">
<span class="ltx_tag ltx_tag_subsection">7.1 </span>Integer Keys</h3>

<div id="S7.SS1.p1" class="ltx_para">
<p class="ltx_p">The order logarithm is a property of abstract keys. An integer key in a
$\mathrm{poly}(n)$ universe is searchable by the word-RAM: a y-fast
trie <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib10" title="Log-logarithmic worst-case range queries are possible in space ⁢Θ(N)" class="ltx_ref">WIL83</a>]</cite> finds a run’s predecessor in $O(\lambda)$ reads and a
fusion tree <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib11" title="Surpassing the information theoretic bound with fusion trees" class="ltx_ref">FW93</a>]</cite> in $O(\log_{w}m)$, both forward-readable under
the round-by-round layout of <a href="#S2.Thmtheorem3" title="Proposition 2.3 (Bentley–Saxe Baseline). ‣ 2.6 Baseline Upper Bounds ‣ 2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>. Predecessor then costs
$O(n\log^{2}n\,\lambda)$, its gap over membership shrinking from $\log n$ to
$\lambda$, the way radix sort undercuts the comparison-sorting bound without
refuting it.</p>
</div>
<div id="S7.SS1.p2" class="ltx_para">
<p class="ltx_p">The collapse is not uniform, and the reason is what makes abstract keys hard. An
additive query reads a contribution from every run, so each must still be searched,
now at integer cost: a rank among $m$ integers is a predecessor search of static
complexity $g_{Q}(m)=\Theta(\max\{1,\min\{\log_{w}m,\lambda\}\})$, the y-fast or fusion layout
above, matched from below by Pătraşcu and
Thorup <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib8" title="Time-space trade-offs for predecessor search" class="ltx_ref">PT06</a>, <a href="#bib.bib9" title="Randomization does not help searching predecessors" class="ltx_ref">PT07</a>]</cite>, deterministic and Las Vegas
alike. Its binary sum is $\Sigma_{Q}=\Theta(L\lambda)$, so <a href="#S6.Thmtheorem1" title="Theorem 6.1 (Static-to-Dynamic Lifting). ‣ 6 Static-to-Dynamic Lifting ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">6.1</span></a> places
rank, range-count, and range-sum at $\Theta(n\log^{2}n\,\lambda)$, exactly
$\Theta(\lambda)$ above membership.</p>
</div>
<div id="S7.SS1.p3" class="ltx_para">
<p class="ltx_p">Predecessor behaves differently, because it is settled by one run and the rest need
only be ruled out. Ruling run $i$ out asks whether its keys meet the open interval
between the running best and the query, a range-emptiness test the word-RAM answers
in $O(1)$ <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib12" title="Optimal static range reporting in one dimension" class="ltx_ref">ABR01</a>]</cite> but abstract keys answer only by localizing the query
inside the run, the $\Omega(\log m)$ step behind the separation. The per-run floor
the additive queries enjoy has no integer counterpart here, so the exact integer
cost of predecessor stays open between $\Theta(n\log^{2}n)$ and
$\Theta(n\log^{2}n\,\lambda)$: a lower bound would need a per-run test that stays
$\Omega(\lambda)$-hard under a shared query, and the natural one, whether a run
holds the global predecessor, is the range-emptiness integers trivialize. The key
models part exactly here.</p>
</div>
<div id="S7.SS1.p4" class="ltx_para">
<p class="ltx_p">The collapse is one-dimensional. Two-dimensional range-counting has no van Emde
Boas speedup, its cell-probe complexity $\Omega(\log m/\lambda)$ at linear
space <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib13" title="Lower bounds for 2-dimensional range counting" class="ltx_ref">PĂT07</a>]</cite> matched by a range tree <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib14" title="Adaptive and approximate orthogonal range counting" class="ltx_ref">CW13</a>]</cite>, so
lifting $g_{Q}(m)=\Theta(\max\{1,\log m/\lambda\})$ gives $\Theta(n\log^{3}n/\lambda)$, above
membership by $\Theta(\log n/\log\log n)$. The separation is no artifact of
unstructured keys; it survives the word-RAM as soon as the queries are
two-dimensional, the regime of multi-attribute range search.</p>
</div>
</section>
<section id="S7.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="random-access">
<span class="ltx_tag ltx_tag_subsection">7.2 </span>Random Access</h3>

<div id="S7.SS2.p1" class="ltx_para">
<p class="ltx_p">Select’s polynomial cost is the signature of the no-backseek head, and it vanishes
the moment the head may return. The obstacle of <a href="#S5" title="5 Select ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5</span></a> was an answer
threshold fixed by all runs jointly, unknown while the early runs are read and out
of reach once they are passed. Random access dissolves it: selecting the $K$-th
smallest among $W$ sorted runs is classical, $O(W+\sum_{i}\log(k_{i}+1))$ comparisons
with $k_{i}$ run $i$’s share of the $K$ smallest <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib15" title="Generalized selection and ranking: sorted matrices" class="ltx_ref">FJ84</a>, <a href="#bib.bib16" title="Selection from heaps, row-sorted matrices, and +XY using soft heaps" class="ltx_ref">KKZ+19</a>]</cite>,
which is $O(\log^{2}n)$ at a diverse frontier. Random access brings select to
$O(n\log^{3}n)$, the value-query scale, with the exact optimum open.</p>
</div>
<div id="S7.SS2.p2" class="ltx_para">
<p class="ltx_p">It does no more. Predecessor stays at $n\log^{3}n$ under random access, since every
run must still be searched and no run bridges another; what random access removes
is not the per-run search but the forward head’s inability to revisit an internal
threshold. The polynomial gap was never in the answer, only $O(\log n)$ bits, but
in that head. Integer keys touch only the order gap and random access only select’s,
each isolating the restriction its cost depends on.</p>
</div>
</section>
<section id="S7.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="deque-edits">
<span class="ltx_tag ltx_tag_subsection">7.3 </span>Deque Edits</h3>

<div id="S7.SS3.p1" class="ltx_para">
<p class="ltx_p">Two restrictions guard the cascade together: a merge stack writes only at the tail,
behind the forward head, and its runs are strongly materialized, so no run holds
order information about another. Relax both, writing at the head’s entrance and
letting a young run carry a bridge into an older one, and the separation falls.
Model the relaxation by <em class="ltx_emph ltx_font_italic">deque</em> edits, popping and pushing at both ends of the
token string while keeping the same forward, no-backseek head, so a component may be
placed at position $0$, ahead of all the head will read; dropping materialization
lets a young component store forward handles into the older ones, charged to itself
and leaving them unedited.</p>
</div>
<div id="S7.Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Theorem 7.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Deque Collapse)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Under deque edits with non-materialized runs, abstract-key predecessor admits
$E=O(n\log n)$ and $\widehat{R}=O(\log n)$, so $E\widehat{R}=O(n\log^{2}n)$ and the order
separation does not survive.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S7.SS3.p2" class="ltx_para">
<p class="ltx_p">A useful bridge from $U$ to $V$ needs $U$ read before $V$ and $V$ born before $U$
(<a href="#S4.Thmtheorem1" title="Lemma 4.1 (Causal-Bridge Obstruction). ‣ 4.1 No Cascading Across Components ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.1</span></a>), and tail-only editing forces birth order to follow read
order and kills it. Deque editing breaks the coupling: lay the active components
youngest first, $C_{1},\dots,C_{W}$ read from the entrance with sizes increasing, so
$C_{i}$ is read before $C_{i+1}$ while $C_{i+1}$ is the older of the two, the very
order a cascade needs.</p>
</div>
<div id="S7.SS3.p3" class="ltx_para">
<p class="ltx_p">Run the Bentley–Saxe counter mirrored at the entrance: each insert pushes a
singleton at the front and, while the two front components share a size, pops both,
merges, and pushes one new front component. A component of $m_{i}$ keys stores its
block as a forward-readable balanced tree together with a sparse cascade into the
next-older $C_{i+1}$, cutting $C_{i+1}$’s order into $O(m_{i})$ intervals of span
$O(m_{i+1}/m_{i})$ and keeping, per gap, its own predecessor and a forward handle to
the precomputed subtree root for that interval, a node already inside $C_{i+1}$’s
own tree once $C_{i+1}$ is serialized. Each older component is serialized once with
its roots in place, so a younger one adds only its $O(m_{i})$ handles and never edits
it; hence $|C_{i}|=O(m_{i})$, and a size-$2^{k}$ component is built $O(n/2^{k})$ times at
$O(2^{k})$ tokens, giving $E=O(n\log n)$.</p>
</div>
<div id="S7.SS3.p4" class="ltx_para">
<p class="ltx_p">A query searches $C_{1}$ in $O(\log m_{1})$ reads, then at each step follows the stored
handle into a span-$O(1+m_{i+1}/m_{i})$ interval of $C_{i+1}$, searches its
precomputed subtree, updates the best candidate, and moves on without a backseek.
The reads telescope,</p>
<table id="S7.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\widehat{R}=O\Bigl(W+\log m_{1}+\sum_{i\geq 2}\log\tfrac{m_{i}}{m_{i-1}}\Bigr)=O(W+\log m_{W})=O(\log n).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
</div>
<div id="S7.SS3.p5" class="ltx_para">
<p class="ltx_p">The collapse is one of orientation, not of two-endedness. A queue, pushing at the
tail and popping at the head, still builds its components at the scan’s exit and
does not collapse; what predecessor pays for under tail-only editing is exactly
that new connectivity must be written behind the forward scan. The gap sits at the
missing cascade, and the cascade the deque builds is non-materialized, a young run
pointing into an older one, so the collapse leaves the materialized model and the
tail-only one together. This is why random access alone, the runs still
materialized, does not collapse predecessor. The matching $\Omega(n\log^{2}n)$ would
follow from a membership floor under deque edits, a minor open point since the
universal floor of <a href="#S3" title="3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a> uses the tail-only frontier-width bound; the
collapse out of the $n\log^{3}n$ class is unconditional. Afshani’s dynamic
fractional-cascading lower bound <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib4" title="A lower bound for dynamic fractional cascading" class="ltx_ref">AFS21</a>]</cite> forces either fully dynamic
updates or worst-case update time, while the construction here is insertion-only
with amortized rebuilding, and escapes both.</p>
</div>
</section>
<section id="S7.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="lsm-read-amplification">
<span class="ltx_tag ltx_tag_subsection">7.4 </span>LSM Read Amplification</h3>

<div id="S7.SS4.p1" class="ltx_para">
<p class="ltx_p">The read gap reaches past edit histories to the runs in place at query time, though
only under a hypothesis. A run can hold its median and successor in an $O(1)$ header
and certify a query’s predecessor between them in two reads, so overlap by itself
does not force $\Omega(\log m)$. What forces it is a query distribution that, after
all outside information is exposed, still leaves $\Omega(\log m_{i})$ of conditional
gap entropy in each overlapped run, exactly the hard family of <a href="#S4.Thmtheorem3" title="Lemma 4.3 (Anchor-and-Zones Floor). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a>.</p>
</div>
<div id="S7.Thmtheorem2" class="ltx_theorem ltx_theorem_proposition">
<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Proposition 7.2</span></span><span class="ltx_text ltx_font_bold"> </span>(Range Read Amplification)<span class="ltx_text ltx_font_bold">.</span>
</h6>
<div id="S7.Thmtheorem2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let $R_{1},\dots,R_{W}$ be active sorted runs, pairwise no-cascade and carrying no
cross-run order catalog. Under a query distribution leaving $\Omega(\log m_{i})$
conditional gap entropy in each run it crosses, an exact range or order query has
read cost $\Omega(\sum_{i\,\text{crossed}}\log m_{i})$, while a point query is settled
in $O(1)$ reads per run.</span></p>
</div>
</div>
<div class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S7.SS4.p2" class="ltx_para">
<p class="ltx_p">The runs being mutually no-cascade, a read in one cannot shrink another’s candidate
set, so the per-run argument of <a href="#S4.Thmtheorem3" title="Lemma 4.3 (Anchor-and-Zones Floor). ‣ 4.2 Per-State Search Lower Bound ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">4.3</span></a> applies to each crossed run
on its own: the hypothesis leaves $\Omega(\log m_{i})$ gap entropy there, and
localizing the endpoint costs $\Omega(\log m_{i})$ reads. Carrying no cross-run
catalog, the runs do not share the cost, so it sums. A point query is hashable,
settled per run by a filter in $O(1)$.
∎</p>
</div>
</div>
<div id="S7.SS4.p3" class="ltx_para">
<p class="ltx_p">The bound is on the runs in place, however built or read, so it holds
in any leveled sorted-run store. In a random-access store the per-run filters let a
point query skip the runs that miss it, leaving $O(1)$; a range or order query has
no such escape and localizes in every run it spans,
$\Theta(\log_{T}n)$ at size-ratio $T$, each localization irreducible by
<a href="#S7.Thmtheorem2" title="Proposition 7.2 (Range Read Amplification). ‣ 7.4 LSM Read Amplification ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Proposition</span> <span class="ltx_text ltx_ref_tag">7.2</span></a>. This
range-over-point read amplification closes only two ways: a word-RAM integer index,
which serves one dimension but not string keys or multi-attribute ranges, where the
two-dimensional separation persists; or a cross-run order catalog, which appears to
need $\Omega(n^{2})$ edits to maintain under append-only merging (<a href="#S5" title="5 Select ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">5</span></a>).
For write-optimized, string-keyed, multi-attribute engines in the insertion-only
regime the model captures, the range read amplification is intrinsic, not an
implementation artifact <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bib22" title="The log-structured merge-tree (LSM-tree)" class="ltx_ref">OCG+96</a>, <a href="#bib.bib17" title="Monkey: optimal navigable key-value store" class="ltx_ref">DAI17</a>, <a href="#bib.bib18" title="Dostoevsky: better space-time trade-offs for LSM-tree based key-value stores via adaptive removal of superfluous merging" class="ltx_ref">DI18</a>]</cite>.</p>
</div>
</section>
<section id="S7.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection" id="intermediate-queries">
<span class="ltx_tag ltx_tag_subsection">7.5 </span>Intermediate Queries</h3>

<div id="S7.SS5.p1" class="ltx_para">
<p class="ltx_p">Order at $n\log^{3}n$ and select at $n^{2}$ are the two ends of one scale, set by how
much the query reveals about its answer’s value. A $w$-windowed select, the $K$-th
smallest under the promise that the answer lies in a bracket of at most $w$ live
keys, interpolates between them: at $w=O(1)$ the bracket pins the value and the
query is an order query, at $w=N$ the promise is empty and it is select. The cut
floor restricted to the bracket gives $\widehat{R}\geq c\min\{w,P,U\}$, only the $\leq w$
keys inside it carrying the ambiguity. The matching write tradeoff across the
interior is open, and we leave it.</p>
</div>
</section>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography" id="references">References</h2>

<ul id="bib.L1" class="ltx_biblist">
<li id="bib.bib4" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[AFS21]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. Afshani</span><span class="ltx_text ltx_bib_year"> (2021)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">A lower bound for dynamic fractional cascading</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SODA</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 2229–2248</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2011.00503</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1137/1.9781611976465.133" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#A1.Thmtheorem5.p1" title="Remark A.5. ‣ Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark A.5</span></a>,
<a href="#S1.SS3.SSS0.Px3.p1" title="Fractional Cascading. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p6" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S4.SS1.p3" title="4.1 No Cascading Across Components ‣ 4 Order Queries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§4.1</span></a>,
<a href="#S7.SS3.p5" title="7.3 Deque Edits ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.3</span></a>.
</span>
</li>
<li id="bib.bib12" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[ABR01]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Alstrup, G. S. Brodal, and T. Rauhe</span><span class="ltx_text ltx_bib_year"> (2001)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Optimal static range reporting in one dimension</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">STOC</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 476–482</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/380752.380842" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S7.SS1.p3" title="7.1 Integer Keys ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.1</span></a>.
</span>
</li>
<li id="bib.bib31" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[AKM+16]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Athanassoulis, M. S. Kester, L. M. Maas, R. Stoica, S. Idreos, A. Ailamaki, and M. Callaghan</span><span class="ltx_text ltx_bib_year"> (2016)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Designing access methods: the RUM conjecture</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">EDBT</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 461–466</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.5441/002/edbt.2016.42" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p2" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib29" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[BCF+24]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. A. Bender, A. Conway, M. Farach-Colton, H. Komlós, M. Koucký, W. Kuszmaul, and M. Saks</span><span class="ltx_text ltx_bib_year"> (2024)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Nearly optimal list labeling</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">FOCS</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 2253–2274</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2405.00807</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1109/FOCS61266.2024.00132" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span>
</li>
<li id="bib.bib19" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[BCF+22]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. A. Bender, A. Conway, M. Farach-Colton, H. Komlós, W. Kuszmaul, and N. Wein</span><span class="ltx_text ltx_bib_year"> (2022)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Online list labeling: breaking the $\log^{2}n$ barrier</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">FOCS</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 980–990</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2203.02763</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1109/FOCS54457.2022.00096" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#A1.p12" title="Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix A</span></a>,
<a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span>
</li>
<li id="bib.bib35" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[BFF+07]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. A. Bender, M. Farach-Colton, J. T. Fineman, Y. R. Fogel, B. C. Kuszmaul, and J. Nelson</span><span class="ltx_text ltx_bib_year"> (2007)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Cache-oblivious streaming B-trees</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SPAA</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 81–92</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/1248377.1248393" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#A1.Thmtheorem5.p1" title="Remark A.5. ‣ Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Remark A.5</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib1" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[BS80]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">J. L. Bentley and J. B. Saxe</span><span class="ltx_text ltx_bib_year"> (1980)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Decomposable searching problems I: static-to-dynamic transformation</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Journal of Algorithms</span> <span class="ltx_text ltx_bib_volume">1</span> (<span class="ltx_text ltx_bib_number">4</span>), <span class="ltx_text ltx_bib_pages"> pp. 301–358</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1016/0196-6774%2880%2990015-2" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px1.p1" title="Static-to-Dynamic Transformations. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S2.SS6.p1" title="2.6 Baseline Upper Bounds ‣ 2 Preliminaries ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§2.6</span></a>.
</span>
</li>
<li id="bib.bib42" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[BDH+23]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Borst, D. Dadush, S. Huiberts, and D. Kashaev</span><span class="ltx_text ltx_bib_year"> (2023)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">A nearly optimal randomized algorithm for explorable heap selection</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">IPCO</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_series">Lecture Notes in Computer Science</span>, Vol. <span class="ltx_text ltx_bib_volume">13904</span>, <span class="ltx_text ltx_bib_pages"> pp. 29–43</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2210.05982</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1007/978-3-031-32726-1%5F3" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span>
</li>
<li id="bib.bib20" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[BF03]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">G. S. Brodal and R. Fagerberg</span><span class="ltx_text ltx_bib_year"> (2003)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Lower bounds for external memory dictionaries</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SODA</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 546–554</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.5555/644108.644201" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib3" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[BKS12]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">J. Bulánek, M. Koucký, and M. Saks</span><span class="ltx_text ltx_bib_year"> (2012)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Tight lower bounds for the online labeling problem</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">STOC</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 1185–1198</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:1112.5636</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/2213977.2214083" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#A1.p10" title="Appendix A Cascades Beyond Materialization ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Appendix A</span></a>,
<a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S3.SS1.p7" title="3.1 Merge Forests ‣ 3 Membership ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§3.1</span></a>.
</span>
</li>
<li id="bib.bib14" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[CW13]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">T. M. Chan and B. T. Wilkinson</span><span class="ltx_text ltx_bib_year"> (2013)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Adaptive and approximate orthogonal range counting</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SODA</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 241–251</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1137/1.9781611973105.18" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S7.SS1.p4" title="7.1 Integer Keys ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.1</span></a>.
</span>
</li>
<li id="bib.bib23" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[CDG+08]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">F. Chang, J. Dean, S. Ghemawat, W. C. Hsieh, D. A. Wallach, M. Burrows, T. Chandra, A. Fikes, and R. E. Gruber</span><span class="ltx_text ltx_bib_year"> (2008)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Bigtable: a distributed storage system for structured data</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">ACM Transactions on Computer Systems</span> <span class="ltx_text ltx_bib_volume">26</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages"> pp. 1–26</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/1365815.1365816" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib21" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[CG86]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">B. Chazelle and L. J. Guibas</span><span class="ltx_text ltx_bib_year"> (1986)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Fractional cascading: I. A data structuring technique</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Algorithmica</span> <span class="ltx_text ltx_bib_volume">1</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages"> pp. 133–162</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1007/BF01840440" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px3.p1" title="Fractional Cascading. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p6" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib7" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[DIN22]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">R. Das, J. Iacono, and Y. Nekrich</span><span class="ltx_text ltx_bib_year"> (2022)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">External-memory dictionaries with worst-case update cost</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">ISAAC</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_series">LIPIcs</span>, Vol. <span class="ltx_text ltx_bib_volume">248</span>, <span class="ltx_text ltx_bib_pages"> pp. 21:1–21:13</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2211.06044</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.4230/LIPIcs.ISAAC.2022.21" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span>
</li>
<li id="bib.bib17" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[DAI17]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">N. Dayan, M. Athanassoulis, and S. Idreos</span><span class="ltx_text ltx_bib_year"> (2017)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Monkey: optimal navigable key-value store</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SIGMOD</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 79–94</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/3035918.3064054" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p2" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S7.SS4.p3" title="7.4 LSM Read Amplification ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.4</span></a>.
</span>
</li>
<li id="bib.bib18" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[DI18]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">N. Dayan and S. Idreos</span><span class="ltx_text ltx_bib_year"> (2018)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Dostoevsky: better space-time trade-offs for LSM-tree based key-value stores via adaptive removal of superfluous merging</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SIGMOD</span>,
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/3183713.3196927" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p2" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S7.SS4.p3" title="7.4 LSM Read Amplification ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.4</span></a>.
</span>
</li>
<li id="bib.bib15" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[FJ84]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">G. N. Frederickson and D. B. Johnson</span><span class="ltx_text ltx_bib_year"> (1984)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Generalized selection and ranking: sorted matrices</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">SIAM Journal on Computing</span> <span class="ltx_text ltx_bib_volume">13</span> (<span class="ltx_text ltx_bib_number">1</span>), <span class="ltx_text ltx_bib_pages"> pp. 14–30</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1137/0213002" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S7.SS2.p1" title="7.2 Random Access ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.2</span></a>.
</span>
</li>
<li id="bib.bib38" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[FS89]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. L. Fredman and M. E. Saks</span><span class="ltx_text ltx_bib_year"> (1989)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The cell probe complexity of dynamic data structures</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">STOC</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 345–354</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/73007.73040" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib11" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[FW93]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. L. Fredman and D. E. Willard</span><span class="ltx_text ltx_bib_year"> (1993)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Surpassing the information theoretic bound with fusion trees</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Journal of Computer and System Sciences</span> <span class="ltx_text ltx_bib_volume">47</span> (<span class="ltx_text ltx_bib_number">3</span>), <span class="ltx_text ltx_bib_pages"> pp. 424–436</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1016/0022-0000%2893%2990040-4" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S7.SS1.p1" title="7.1 Integer Keys ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.1</span></a>.
</span>
</li>
<li id="bib.bib28" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[IKR81]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Itai, A. G. Konheim, and M. Rodeh</span><span class="ltx_text ltx_bib_year"> (1981)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">A sparse table implementation of priority queues</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">ICALP</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_series">Lecture Notes in Computer Science</span>, Vol. <span class="ltx_text ltx_bib_volume">115</span>, <span class="ltx_text ltx_bib_pages"> pp. 417–431</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1007/3-540-10843-2%5F34" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span>
</li>
<li id="bib.bib16" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[KKZ+19]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">H. Kaplan, L. Kozma, O. Zamir, and U. Zwick</span><span class="ltx_text ltx_bib_year"> (2019)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Selection from heaps, row-sorted matrices, and $X+Y$ using soft heaps</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SOSA</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_series">OASIcs</span>, Vol. <span class="ltx_text ltx_bib_volume">69</span>, <span class="ltx_text ltx_bib_pages"> pp. 5:1–5:21</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.4230/OASIcs.SOSA.2019.5" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S7.SS2.p1" title="7.2 Random Access ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.2</span></a>.
</span>
</li>
<li id="bib.bib41" class="ltx_bibitem ltx_bib_misc">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[KO25]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">Y. K. Ko</span><span class="ltx_text ltx_bib_year"> (2025)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Unifying the landscape of super-logarithmic dynamic cell-probe lower bounds</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2510.17717; ECCC TR25-156</span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span>
</li>
<li id="bib.bib24" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[LM10]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">A. Lakshman and P. Malik</span><span class="ltx_text ltx_bib_year"> (2010)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Cassandra: a decentralized structured storage system</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">ACM SIGOPS Operating Systems Review</span> <span class="ltx_text ltx_bib_volume">44</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages"> pp. 35–40</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/1773912.1773922" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib39" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[LAR12]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">K. G. Larsen</span><span class="ltx_text ltx_bib_year"> (2012)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The cell probe complexity of dynamic range counting</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">STOC</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 85–94</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:1105.5933</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/2213977.2213987" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib25" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[LPG+17]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">L. Lu, T. S. Pillai, H. Gopalakrishnan, A. C. Arpaci-Dusseau, and R. H. Arpaci-Dusseau</span><span class="ltx_text ltx_bib_year"> (2017)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">WiscKey: separating keys from values in SSD-conscious storage</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">ACM Transactions on Storage</span> <span class="ltx_text ltx_bib_volume">13</span> (<span class="ltx_text ltx_bib_number">1</span>), <span class="ltx_text ltx_bib_pages"> pp. 1–28</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/3033273" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib34" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[LCK+20]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">S. Luo, S. Chatterjee, R. Ketsetsidis, N. Dayan, W. Qin, and S. Idreos</span><span class="ltx_text ltx_bib_year"> (2020)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Rosetta: a robust space-time optimized range filter for key-value stores</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SIGMOD</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 2071–2086</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/3318464.3389731" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p2" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib5" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[MRY+21]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">C. Mathieu, R. Rajaraman, N. E. Young, and A. Yousefi</span><span class="ltx_text ltx_bib_year"> (2021)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Competitive data-structure dynamization</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SODA</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 2269–2287</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2011.02615</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1137/1.9781611976465.135" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px1.p1" title="Static-to-Dynamic Transformations. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib27" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[MDL20]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">Y. Matsunobu, S. Dong, and H. Lee</span><span class="ltx_text ltx_bib_year"> (2020)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">MyRocks: LSM-tree database storage engine serving facebook’s social graph</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Proceedings of the VLDB Endowment</span> <span class="ltx_text ltx_bib_volume">13</span> (<span class="ltx_text ltx_bib_number">12</span>), <span class="ltx_text ltx_bib_pages"> pp. 3217–3230</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.14778/3415478.3415546" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib37" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[MN90]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">K. Mehlhorn and S. Näher</span><span class="ltx_text ltx_bib_year"> (1990)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Dynamic fractional cascading</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Algorithmica</span> <span class="ltx_text ltx_bib_volume">5</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages"> pp. 215–241</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1007/BF01840386" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px3.p1" title="Fractional Cascading. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p6" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib2" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[MEH81]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">K. Mehlhorn</span><span class="ltx_text ltx_bib_year"> (1981)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Lower bounds on the efficiency of transforming static data structures into dynamic structures</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Mathematical Systems Theory</span> <span class="ltx_text ltx_bib_volume">15</span> (<span class="ltx_text ltx_bib_number">1</span>), <span class="ltx_text ltx_bib_pages"> pp. 1–16</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1007/BF01786969" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px1.p1" title="Static-to-Dynamic Transformations. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib6" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[MLI25]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">D. Mo, S. Luo, and S. Idreos</span><span class="ltx_text ltx_bib_year"> (2025)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">How to grow an LSM-tree? Towards bridging the gap between theory and practice</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Proceedings of the ACM on Management of Data</span> <span class="ltx_text ltx_bib_volume">3</span> (<span class="ltx_text ltx_bib_number">3</span>), <span class="ltx_text ltx_bib_pages"> pp. 173:1–173:25</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2504.17178</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/3725310" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p2" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib36" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[MP80]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">J. I. Munro and M. S. Paterson</span><span class="ltx_text ltx_bib_year"> (1980)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Selection and sorting with limited storage</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Theoretical Computer Science</span> <span class="ltx_text ltx_bib_volume">12</span> (<span class="ltx_text ltx_bib_number">3</span>), <span class="ltx_text ltx_bib_pages"> pp. 315–323</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1016/0304-3975%2880%2990061-4" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>.
</span>
</li>
<li id="bib.bib22" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[OCG+96]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. O’Neil, E. Cheng, D. Gawlick, and E. O’Neil</span><span class="ltx_text ltx_bib_year"> (1996)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The log-structured merge-tree (LSM-tree)</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Acta Informatica</span> <span class="ltx_text ltx_bib_volume">33</span> (<span class="ltx_text ltx_bib_number">4</span>), <span class="ltx_text ltx_bib_pages"> pp. 351–385</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1007/s002360050048" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S7.SS4.p3" title="7.4 LSM Read Amplification ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.4</span></a>.
</span>
</li>
<li id="bib.bib30" class="ltx_bibitem ltx_bib_book">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[OVE83]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. H. Overmars</span><span class="ltx_text ltx_bib_year"> (1983)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">The design of dynamic data structures</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_series">Lecture Notes in Computer Science</span>, Vol. <span class="ltx_text ltx_bib_volume">156</span>,  <span class="ltx_text ltx_bib_publisher">Springer</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1007/BFb0014927" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px1.p1" title="Static-to-Dynamic Transformations. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib8" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[PT06]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Pătraşcu and M. Thorup</span><span class="ltx_text ltx_bib_year"> (2006)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Time-space trade-offs for predecessor search</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">STOC</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 232–240</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:cs/0603043</span>
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/1132516.1132551" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S7.SS1.p2" title="7.1 Integer Keys ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.1</span></a>.
</span>
</li>
<li id="bib.bib9" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[PT07]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Pătraşcu and M. Thorup</span><span class="ltx_text ltx_bib_year"> (2007)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Randomization does not help searching predecessors</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SODA</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 555–564</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.5555/1283383.1283443" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S7.SS1.p2" title="7.1 Integer Keys ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.1</span></a>.
</span>
</li>
<li id="bib.bib13" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[PĂT07]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Pătraşcu</span><span class="ltx_text ltx_bib_year"> (2007)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Lower bounds for 2-dimensional range counting</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">STOC</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 40–46</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/1250790.1250797" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S7.SS1.p4" title="7.1 Integer Keys ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.1</span></a>.
</span>
</li>
<li id="bib.bib40" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[PĂT11]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">M. Pătraşcu</span><span class="ltx_text ltx_bib_year"> (2011)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Unifying the landscape of cell-probe lower bounds</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">SIAM Journal on Computing</span> <span class="ltx_text ltx_bib_volume">40</span> (<span class="ltx_text ltx_bib_number">3</span>), <span class="ltx_text ltx_bib_pages"> pp. 827–847</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1137/09075336X" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px4.p1" title="Lower Bounds and Restricted Access. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib26" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[RKC+17]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">P. Raju, R. Kadekodi, V. Chidambaram, and I. Abraham</span><span class="ltx_text ltx_bib_year"> (2017)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">PebblesDB: building key-value stores using fragmented log-structured merge trees</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SOSP</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 497–514</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/3132747.3132765" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p1" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib10" class="ltx_bibitem ltx_bib_article">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[WIL83]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">D. E. Willard</span><span class="ltx_text ltx_bib_year"> (1983)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">Log-logarithmic worst-case range queries are possible in space $\Theta(N)$</span>.
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_journal">Information Processing Letters</span> <span class="ltx_text ltx_bib_volume">17</span> (<span class="ltx_text ltx_bib_number">2</span>), <span class="ltx_text ltx_bib_pages"> pp. 81–84</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1016/0020-0190%2883%2990075-3" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S7.SS1.p1" title="7.1 Integer Keys ‣ 7 Access-Model Variants ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§7.1</span></a>.
</span>
</li>
<li id="bib.bib33" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[ZLL+18]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">H. Zhang, H. Lim, V. Leis, D. G. Andersen, M. Kaminsky, K. Keeton, and A. Pavlo</span><span class="ltx_text ltx_bib_year"> (2018)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">SuRF: practical range query filtering with fast succinct tries</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">SIGMOD</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 323–336</span>.
</span>
<span class="ltx_bibblock">External Links: <span class="ltx_text ltx_bib_links"><a href="https://dx.doi.org/10.1145/3183713.3196931" title="" class="ltx_ref doi ltx_bib_external">Document</a></span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p2" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
<li id="bib.bib32" class="ltx_bibitem ltx_bib_inproceedings">
<span class="ltx_tag ltx_bib_abbrv ltx_role_refnum ltx_tag_bibitem">[ZCW+21]</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_author">W. Zhong, C. Chen, X. Wu, and S. Jiang</span><span class="ltx_text ltx_bib_year"> (2021)</span>
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_title">REMIX: efficient range query for LSM-trees</span>.
</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_bib_inbook">USENIX FAST</span>,
</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_bib_pages"> pp. 51–64</span>.
</span>
<span class="ltx_bibblock">Note: <span class="ltx_text ltx_bib_note">arXiv:2010.12734</span>
</span>
<span class="ltx_bibblock ltx_bib_cited">Cited by: <a href="#S1.SS3.SSS0.Px2.p1" title="Write-Optimized Storage. ‣ 1.3 Related Works ‣ 1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1.3</span></a>,
<a href="#S1.p2" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>,
<a href="#S1.p5" title="1 Introduction ‣ The Price of Order in the Logarithmic Method" class="ltx_ref"><span class="ltx_text ltx_ref_tag">§1</span></a>.
</span>
</li>
</ul>
</section>
