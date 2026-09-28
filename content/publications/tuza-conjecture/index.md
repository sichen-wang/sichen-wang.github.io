---
title: "A Bound Below 2.8 for Tuza's Conjecture"

authors:
  - me

# arXiv v1 submission date.
date: 2026-09-12

publication_types: ["manuscript"]
publication: "*Preprint*, arXiv:2609.13831"
publication_short: "Preprint"

abstract: |
  Let $\nu(G)$ be the maximum number of edge-disjoint triangles in a graph $G$ and
  $\tau(G)$ the minimum number of edges meeting every triangle. Tuza conjectured that
  $\tau(G)\le 2\nu(G)$. We prove that $\tau(G)\le (165/59)\nu(G)$. The constant
  $165/59\approx 2.797$ improves the bound $66/23\approx 2.870$ that Haxell proved in
  1999. The key observation is that, for a suitable red-blue coloring, the families
  left over in Haxell's construction contain every triangle with exactly one red edge.
  Such a family $\mathcal{F}$ admits an exchange that forces certain red edges to lie
  in a single triangle once the blue edges of a maximum packing are deleted, which
  gives $\tau(\mathcal{F})\le (8/3)\nu(\mathcal{F})$.

tags:
  - Graph Theory
  - Triangle Packing
  - Extremal Combinatorics

featured: false

links:
  - type: pdf
    url: paper.pdf
    label: Paper
  - type: code
    url: https://github.com/sichen-wang/tuza-lean
  - type: preprint
    provider: arxiv
    id: 2609.13831
    label: arXiv
---

<article class="ltx_document ltx_authors_1line">




<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="introduction"><span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p id="S1.p1.1" class="ltx_p">A triangle packing in a graph $G$ is a set of pairwise edge-disjoint triangles, and a triangle transversal is a set of edges meeting every triangle. Let $\nu(G)$ and $\tau(G)$ denote their maximum and minimum sizes. A transversal contains an edge of every packed triangle, and the edges of a maximum packing form a transversal, so $\nu(G)\leq\tau(G)\leq 3\nu(G)\text{.}$ Tuza <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx2" title="" class="ltx_ref">Tuz90</a>]</cite> conjectured that $\tau(G)\leq 2\nu(G)$ for every graph $G\text{.}$ The constant $2$ would be best possible, as $K_{4}$ and $K_{5}$ show.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p id="S1.p2.1" class="ltx_p">Haxell <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx1" title="" class="ltx_ref">Hax99</a>]</cite> proved $\tau(G)\leq(66/23)\,\nu(G)\text{,}$ where $66/23\approx 2.870\text{,}$ and noted without proof that the argument can be pushed to $(1+\sqrt{481})/8\approx 2.866\text{.}$ Very recently, Yi <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx3" title="" class="ltx_ref">Yi26</a>]</cite> lowered the constant to $(162+4\sqrt{3})/59\approx 2.863$ by proving $\tau\leq(1+\sqrt{3})\nu$ for every family of triangles that admits a red-blue edge coloring with one red edge per triangle, and observed that this route alone cannot bring the constant below $54/19\approx 2.842\text{.}$ Independently of Yi’s work, we prove the following bound, whose constant $165/59\approx 2.797$ crosses this barrier and lies below $2.8\text{.}$</p>
</div>
<div id="Thmtheorem1" class="ltx_theorem ltx_theorem_theorem">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmtheorem1.2" class="ltx_text ltx_font_bold">Theorem 1</span></span><span id="Thmtheorem1.3" class="ltx_text ltx_font_bold">.</span></h6>
<div id="Thmtheorem1.p1" class="ltx_para">
<p id="Thmtheorem1.p1.1" class="ltx_p"><span id="Thmtheorem1.p1.1.1" class="ltx_text ltx_font_italic">Every finite simple graph $G$ satisfies</span></p>
<table id="S1.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau(G)\leq\frac{165}{59}\nu(G).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="S1.p3" class="ltx_para">
<p id="S1.p3.1" class="ltx_p">Our starting point is the following exchange property. Let the edges of a graph be colored red and blue, and consider the family of all triangles with exactly one red edge. Fix a maximum packing in this family and delete the blue edges of its triangles. By maximality, every triangle of the family that survives meets the packing only in its red edge. Suppose now that a surviving triangle $uvy$ contains the red edge $uv$ of a packed triangle $uvx\text{,}$ and that $xy$ is a red edge not used by the packing. Then $uvy$ is the only surviving triangle containing $uv\text{.}$ Indeed, $uxy$ has exactly one red edge, and the family contains every such triangle. So if $uvz$ were a second surviving triangle containing $uv\text{,}$ then replacing $uvx$ by $uxy$ and $uvz$ would enlarge the packing (<a href="#S2.Thmlemma1" title="Lemma 2.1. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>). A red edge that lies in a single surviving triangle can be omitted from any transversal containing the other two edges of that triangle. Two transversals of the family, built in <a href="#S2" title="2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a>, allow this omission. Combining the two resulting bounds gives $\tau\leq(8/3)\nu$ for every family of this kind, and every packed triangle whose red edge lies in no other triangle of the family lowers the bound by a further $2/3$ (<a href="#S2.Thmlemma3" title="Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>).</p>
</div>
<div id="S1.p4" class="ltx_para">
<p id="S1.p4.1" class="ltx_p">Families of this kind arise in Haxell’s construction. The construction fixes a maximum packing $P\text{,}$ calls the edges of its triangles old, and packs the remaining triangles in two further rounds: a maximum packing $A$ of triangles with one old edge, and, after the edges of $A$ are deleted, a packing $P^{\prime}$ with as many triangles with two old edges as possible. Color new edges red and old edges blue. After the deletion of the edges of $A\text{,}$ the triangles with two old edges form a family of the above kind, and so do the triangles that survive the further deletion of the old edges of $P^{\prime}\text{.}$ We build four transversals of $G$ from these packings, using books of triangles with a common edge, the bounds of <a href="#S2.Thmlemma3" title="Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>, and a random bipartition of the vertex set. Each gives an inequality between $\tau(G)\text{,}$ $\nu(G)\text{,}$ and the sizes of the packings, and a linear combination of the four inequalities yields $165/59\text{.}$ <a href="#S2" title="2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a> proves the exchange property and <a href="#S2.Thmlemma3" title="Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>, and <a href="#S3" title="3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a> carries out the construction. The complete proof has been formalized in Lean 4 with Mathlib.<span id="footnote1" class="ltx_note ltx_role_footnote"><sup class="ltx_note_mark">1</sup><span class="ltx_note_outer"><span class="ltx_note_content"><sup class="ltx_note_mark">1</sup>
            <span class="ltx_tag ltx_tag_note">1</span>
            
            
            
            
            
            
            
          <a href="https://github.com/sichen-wang/tuza-lean" title="" class="ltx_ref ltx_url ltx_font_typewriter">https://github.com/sichen-wang/tuza-lean</a></span></span></span></p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="colored-triangle-families"><span class="ltx_tag ltx_tag_section">2 </span>Colored Triangle Families</h2>

<div id="S2.p1" class="ltx_para">
<p id="S2.p1.1" class="ltx_p">Throughout, graphs are finite and simple, a triangle is identified with its set of three edges, and two triangles meet if they share an edge. For a family of triangles, a packing is a set of pairwise edge-disjoint members, a transversal is a set of edges meeting every member, and a packing is maximal if no member of the family can be added to it. Maximum packings are maximal. For a set $P$ of triangles, $E(P)$ is the union of their edge sets, and $H-X$ is the graph $H$ with the edge set $X$ deleted.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p id="S2.p2.1" class="ltx_p">This section proves the three lemmas used in <a href="#S3" title="3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">3</span></a>: the exchange property (<a href="#S2.Thmlemma1" title="Lemma 2.1. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>), a covering lemma for books (<a href="#S2.Thmlemma2" title="Lemma 2.2. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>), and the two colored bounds (<a href="#S2.Thmlemma3" title="Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a>). Let $H$ be a graph whose edges are colored red and blue, and let $\mathcal{F}(H)$ be the family of all triangles of $H$ with exactly one red edge. We write $\mathcal{F}$ for $\mathcal{F}(H)$ when $H$ is clear. For a packing $P$ in $\mathcal{F}(H)\text{,}$ let $R(P)$ and $B(P)$ be the sets of red and blue edges of its members, and let</p>
<table id="S2.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{F}_{P}=\mathcal{F}(H-B(P))$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.p2.2" class="ltx_p">be the family of triangles with one red edge that survive the deletion of the blue edges of $P\text{.}$ If $P$ is maximum, every member of $\mathcal{F}_{P}$ has its red edge in $R(P)\text{,}$ since otherwise it could be added to $P\text{.}$ Hence it meets $E(P)$ exactly in its red edge, and it meets exactly one member of $P\text{.}$ We say that an edge is <em id="S2.p2.2.1" class="ltx_emph ltx_font_italic">private</em> in a family of triangles if exactly one member of the family contains it.</p>
</div>
<div id="S2.Thmlemma1" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma1.2" class="ltx_text ltx_font_bold">Lemma 2.1</span></span><span id="S2.Thmlemma1.3" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmlemma1.p1" class="ltx_para">
<p id="S2.Thmlemma1.p1.1" class="ltx_p"><span id="S2.Thmlemma1.p1.1.1" class="ltx_text ltx_font_italic">Let $P$ be a maximum packing in $\mathcal{F}(H)\text{,}$ let $uvx\in P$ have red edge $uv\text{,}$ and let $uvy\in\mathcal{F}_{P}\text{.}$ If $xy$ is a red edge outside $R(P)\text{,}$ then $uv$ is private in $\mathcal{F}_{P}\text{.}$</span></p>
</div>
</div>
<div id="S2.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.p3" class="ltx_para">
<p id="S2.p3.1" class="ltx_p"><span id="S2.p3.1.1" class="ltx_text">Suppose that $uvz\in\mathcal{F}_{P}$ for some $z\neq y\text{.}$ Since $uz\notin B(P)$ while $ux\in B(P)\text{,}$ also $z\neq x\text{.}$ The triangle $uxy$ has blue edges $ux,uy$ and red edge $xy\text{,}$ so it belongs to $\mathcal{F}(H)\text{,}$ and it meets $E(P)$ only in $ux\text{,}$ because $uy\notin B(P)$ and $xy\notin R(P)\text{.}$ The triangle $uvz$ meets $E(P)$ only in $uv\text{.}$ As $z\notin\{x,y\}\text{,}$ the triangles $uxy$ and $uvz$ are edge-disjoint, so replacing $uvx$ by both of them gives a packing in $\mathcal{F}(H)$ larger than $P\text{.}$
∎</span></p>
</div>
</div>
<div id="S2.p4" class="ltx_para">
<p id="S2.p4.1" class="ltx_p">The transversals below are built from books. A <em id="S2.p4.1.1" class="ltx_emph ltx_font_italic">book</em> with <em id="S2.p4.1.2" class="ltx_emph ltx_font_italic">spine</em> $uv$ is a set of triangles containing the edge $uv\text{.}$ Its members are its <em id="S2.p4.1.3" class="ltx_emph ltx_font_italic">pages</em>, and the union of their edge sets is its <em id="S2.p4.1.4" class="ltx_emph ltx_font_italic">support</em>. If a book has exactly two pages $uvx$ and $uvy$ and $xy$ is an edge, then $xy$ is the <em id="S2.p4.1.5" class="ltx_emph ltx_font_italic">opposite edge</em> of the book.</p>
</div>
<div id="S2.Thmlemma2" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma2.2" class="ltx_text ltx_font_bold">Lemma 2.2</span></span><span id="S2.Thmlemma2.3" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmlemma2.p1" class="ltx_para">
<p id="S2.Thmlemma2.p1.1" class="ltx_p"><span id="S2.Thmlemma2.p1.1.1" class="ltx_text ltx_font_italic">Let $\mathcal{B}$ be a set of books with at most three pages each and pairwise edge-disjoint supports, and let $\mathcal{T}$ be a family of triangles such that every selection of one page from each book is a maximal packing in $\mathcal{T}\text{.}$ Let $C$ consist of all edges of the one-page books and the spines of the other books. Then every member of $\mathcal{T}$ avoiding $C$ is $uxy$ or $vxy$ for some two-page book $\{uvx,uvy\}$ in $\mathcal{B}\text{.}$ Consequently, $C$ together with the opposite edges of the two-page books is a transversal of $\mathcal{T}$ of size at most $\sum_{B\in\mathcal{B}}(4-|B|)\text{.}$</span></p>
</div>
</div>
<div id="S2.3" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.p5" class="ltx_para">
<p id="S2.p5.1" class="ltx_p"><span id="S2.p5.1.1" class="ltx_text">Let $T\in\mathcal{T}$ avoid $C\text{.}$ If every book had a page edge-disjoint from $T\text{,}$ choosing such a page in each book would give a maximal packing in $\mathcal{T}$ to which $T$ could still be added, a contradiction. So $T$ meets every page of some book $B\text{.}$ Since all edges of a one-page book lie in $C\text{,}$ $B$ has two or three pages, and $T$ avoids its spine $uv\text{,}$ so $T$ contains $uz$ or $vz$ for every page $uvz$ of $B\text{.}$ If $B$ had three pages, these would be three edges of $T$ with distinct ends outside $\{u,v\}\text{,}$ but a triangle has only three vertices. So $B=\{uvx,uvy\}\text{,}$ and $T$ contains one of $ux,vx$ and one of $uy,vy\text{.}$ Two edges of a triangle share a vertex, so these are $ux,uy$ or $vx,vy\text{,}$ and $T$ is $uxy$ or $vxy\text{.}$ Finally, a book with $k$ pages contributes at most $4-k$ edges to the transversal.
∎</span></p>
</div>
</div>
<div id="S2.Thmlemma3" class="ltx_theorem ltx_theorem_lemma">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="S2.Thmlemma3.2" class="ltx_text ltx_font_bold">Lemma 2.3</span></span><span id="S2.Thmlemma3.3" class="ltx_text ltx_font_bold">.</span></h6>
<div id="S2.Thmlemma3.p1" class="ltx_para">
<p id="S2.Thmlemma3.p1.1" class="ltx_p"><span id="S2.Thmlemma3.p1.1.1" class="ltx_text ltx_font_italic">Let $P$ be a maximum packing in $\mathcal{F}(H)$ and $Q$ a maximum packing in $\mathcal{F}_{P}\text{,}$ with $p=|P|$ and $q=|Q|\text{,}$ and let $u$ be the number of members of $P$ whose red edge is private in $\mathcal{F}(H)\text{.}$ Then</span></p>

<div class="paper-eqgroup"><span class="paper-eq-anchor" id="S2.EGx1"></span><span class="paper-eq-anchor" id="S2.E1"></span><span class="paper-eq-anchor" id="S2.E2"></span><div class="paper-eqgroup-body">$$\begin{aligned}
\displaystyle\tau(\mathcal{F}(H)) &amp; \displaystyle\leq\tfrac{8}{3}p-\tfrac{2}{3}u, \\
\displaystyle\tau(\mathcal{F}(H)) &amp; \displaystyle\leq\tfrac{9}{4}p+\tfrac{3}{2}q-\tfrac{1}{4}u.
\end{aligned}$$</div><div class="paper-eqgroup-no paper-eqgroup-no-rows"><span class="paper-eqgroup-number">(1)</span><span class="paper-eqgroup-number">(2)</span></div></div>

</div>
</div>
<div id="S2.4" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof.</h6>
<div id="S2.p6" class="ltx_para">
<p id="S2.p6.1" class="ltx_p"><span id="S2.p6.1.1" class="ltx_text">Let $r$ be the number of members of $Q$ whose red edge is private in $\mathcal{F}_{P}\text{.}$ We build two transversals of $\mathcal{F}\text{,}$ which give</span></p>
<table id="S2.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau(\mathcal{F})\leq 3p-2q+r-u\qquad\text{and}\qquad\tau(\mathcal{F})\leq 2p+3q-r,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.p6.2" class="ltx_p"><span id="S2.p6.2.1" class="ltx_text">and then combine these bounds, once directly and once after applying <a href="#S2.E1" title="In Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1</span></a> to $\mathcal{F}_{P}\text{.}$</span></p>
</div>
<div id="S2.p7" class="ltx_para">
<p id="S2.p7.1" class="ltx_p"><span id="S2.p7.1.1" class="ltx_text">The first transversal comes from books. Each member of $Q$ shares its red edge with exactly one member of $P\text{,}$ and the two form a book with that red edge as spine. Each unpaired member of $P$ forms a one-page book. No member of $P$ is paired twice, as $Q$ is a packing, and the supports are edge-disjoint, as the blue edges of $Q$ avoid $B(P)\text{.}$ Every selection of one page per book is a packing in $\mathcal{F}$ of size $p=\nu(\mathcal{F})\text{,}$ hence maximal. A member of $P$ whose red edge is private in $\mathcal{F}$ is unpaired, since a page of $Q$ on the same spine would be a second member of $\mathcal{F}$ containing that edge.</span></p>
</div>
<div id="S2.p8" class="ltx_para">
<p id="S2.p8.1" class="ltx_p"><span id="S2.p8.1.1" class="ltx_text">Let $C$ consist of the $3(p-q)$ edges of the one-page books and the $q$ spines. By <a href="#S2.Thmlemma2" title="Lemma 2.2. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a>, a member of $\mathcal{F}$ avoiding $C$ is $uxy$ or $vxy$ for a two-page book $\{uvx,uvy\}$ with $uvx\in P$ and $uvy\in Q\text{.}$ The two edges it shares with the pages are blue, so $xy$ is red, and $xy\notin R(P)$ since $R(P)\subseteq C\text{.}$ By <a href="#S2.Thmlemma1" title="Lemma 2.1. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a>, $uv$ is private in $\mathcal{F}_{P}\text{,}$ so $uvy$ is one of the $r$ members of $Q$ with a private red edge. Adding the opposite edges of these at most $r$ books to $C$ therefore gives a transversal of $\mathcal{F}\text{.}$ Finally, delete the red edges of the $u$ unpaired members of $P$ whose red edge is private in $\mathcal{F}\text{:}$ the only member of $\mathcal{F}$ containing such an edge is that member of $P\text{,}$ which is met by its blue edges in $C\text{.}$ The transversal now has at most $3(p-q)+q+r-u$ edges, which is the first bound.</span></p>
</div>
<div id="S2.p9" class="ltx_para">
<p id="S2.p9.1" class="ltx_p"><span id="S2.p9.1.1" class="ltx_text">The second transversal starts from $B(P)\cup E(Q)\text{.}$ A member of $\mathcal{F}$ avoiding $B(P)$ lies in $\mathcal{F}_{P}$ and, as $Q$ is maximal there, meets $E(Q)\text{.}$ So $B(P)\cup E(Q)$ is a transversal of $\mathcal{F}\text{.}$ Delete the red edges of the $r$ members of $Q$ whose red edge is private in $\mathcal{F}_{P}\text{:}$ a member of $\mathcal{F}$ avoiding the remaining edges lies in $\mathcal{F}_{P}$ and contains a deleted edge, so it is the corresponding member of $Q\text{,}$ which is met by its blue edges. The remaining $2p+3q-r$ edges give the second bound.</span></p>
</div>
<div id="S2.p10" class="ltx_para">
<p id="S2.p10.1" class="ltx_p"><span id="S2.p10.1.1" class="ltx_text">Twice the first bound plus the second gives $3\tau(\mathcal{F})\leq 8p-q+r-2u\leq 8p-2u\text{,}$ as $r\leq q\text{,}$ which is <a href="#S2.E1" title="In Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1</span></a>. Next, $Q$ is a maximum packing in $\mathcal{F}(H-B(P))=\mathcal{F}_{P}\text{,}$ and $r$ of its members have a red edge that is private in $\mathcal{F}_{P}\text{,}$ so <a href="#S2.E1" title="In Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">1</span></a> for the graph $H-B(P)$ gives $\tau(\mathcal{F}_{P})\leq\tfrac{8}{3}q-\tfrac{2}{3}r\text{.}$ Since $B(P)$ meets every member of $\mathcal{F}\setminus\mathcal{F}_{P}\text{,}$</span></p>
<table id="S2.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau(\mathcal{F})\leq 2p+\tfrac{8}{3}q-\tfrac{2}{3}r.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S2.p10.2" class="ltx_p"><span id="S2.p10.2.1" class="ltx_text">Three times this bound plus the first bound gives $4\tau(\mathcal{F})\leq 9p+6q-u-r\leq 9p+6q-u\text{,}$ which is <a href="#S2.E2" title="In Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2</span></a>.
∎</span></p>
</div>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section" id="the-general-bound"><span class="ltx_tag ltx_tag_section">3 </span>The General Bound</h2>

<div id="S3.2" class="ltx_proof">
<h6 class="ltx_title ltx_runin ltx_font_italic ltx_title_proof">Proof of <a href="#Thmtheorem1" title="Theorem 1. ‣ 1 Introduction ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Theorem</span> <span class="ltx_text ltx_ref_tag">1</span></a>.</h6>
<div id="S3.p1" class="ltx_para">
<p id="S3.p1.1" class="ltx_p"><span id="S3.p1.1.1" class="ltx_text">We follow Haxell’s construction <cite class="ltx_cite ltx_citemacro_cite">[<a href="#bib.bibx1" title="" class="ltx_ref">Hax99</a>]</cite>: the packings below and the first transversal are taken from it, and the other three transversals rest on the lemmas of <a href="#S2" title="2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Section</span> <span class="ltx_text ltx_ref_tag">2</span></a>. Choose a maximum triangle packing $P$ in $G\text{,}$ and put $n=|P|=\nu(G)$ and $O=E(P)\text{.}$ Call edges in $O$ old and all other edges new. A triangle has type $j$ if it contains exactly $j$ old edges. By maximality of $P$ there are no type-0 triangles.</span></p>
</div>
<div id="S3.p2" class="ltx_para">
<p id="S3.p2.1" class="ltx_p"><span id="S3.p2.1.1" class="ltx_text">Choose a maximum packing $A$ of type-1 triangles and put $a=|A|\text{.}$ The first transversal comes from books formed by $P$ and $A\text{.}$ Pair each member of $A$ with the member of $P$ containing its old edge. If two members of $A$ met the same member of $P\text{,}$ replacing it by both would enlarge $P\text{,}$ since a type-1 triangle meets $E(P)$ only in its old edge. These pairs and the remaining members of $P$ form $n$ books with $n+a$ pages. Their supports are edge-disjoint, since the new edges of $A$ avoid $O\text{,}$ and every selection of one page per book is a packing of size $n=\nu(G)\text{,}$ hence maximal. <a href="#S2.Thmlemma2" title="Lemma 2.2. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> gives a transversal with at most $3(n-a)+2a$ edges, that is,</span></p>
<table id="S3.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau(G)\leq 3n-a.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3)</span></td></tr></tbody>
</table>
</div>
<div id="S3.p3" class="ltx_para">
<p id="S3.p3.1" class="ltx_p"><span id="S3.p3.1.1" class="ltx_text">Put $G^{\prime}=G-E(A)$ and $O^{\prime}=O\setminus E(A)\text{.}$ Every type-1 triangle meets $E(A)$ by maximality of $A\text{,}$ so every triangle of $G^{\prime}$ has type $2$ or $3\text{,}$ and $|O^{\prime}|=3n-a\text{.}$ Each remaining transversal of $G$ consists of $E(A)$ and a transversal of $G^{\prime}\text{.}$ Color the new edges of $G^{\prime}$ red and its old edges blue. Then $\mathcal{F}(G^{\prime})$ is the family $\mathcal{F}_{2}$ of type-2 triangles of $G^{\prime}\text{.}$</span></p>
</div>
<div id="S3.p4" class="ltx_para">
<p id="S3.p4.1" class="ltx_p"><span id="S3.p4.1.1" class="ltx_text">Choose a packing $P^{\prime}$ in $G^{\prime}$ that maximizes first its number of type-2 members and then its size $m\text{.}$ Let $B^{*}$ be the set of type-2 members of $P^{\prime}$ and put $b=|B^{*}|\text{.}$ Any packing in $\mathcal{F}_{2}$ is a packing in $G^{\prime}\text{,}$ so $B^{*}$ is a maximum packing in $\mathcal{F}_{2}\text{.}$ The new edges of $P^{\prime}$ are the new edges of the members of $B^{*}\text{,}$ one for each. Let $N$ be their set, so that $R(B^{*})=N$ and $|N|=b\text{.}$ Since $A\cup P^{\prime}$ is a packing in $G\text{,}$ we have $a+m\leq n\text{.}$ The choice of $P^{\prime}$ makes every packing in $G^{\prime}$ with $m$ members, $b$ of them of type $2\text{,}$ maximal in $G^{\prime}\text{:}$ adding a triangle would give a packing with at least $b$ type-2 members and $m+1$ members.</span></p>
</div>
<div id="S3.p5" class="ltx_para">
<p id="S3.p5.1" class="ltx_p"><span id="S3.p5.1.1" class="ltx_text">Let $B(P^{\prime})$ be the set of old edges of $P^{\prime}\text{,}$ and put</span></p>
<table id="S3.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\mathcal{S}=\mathcal{F}(G^{\prime}-B(P^{\prime})),$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.p5.2" class="ltx_p"><span id="S3.p5.2.1" class="ltx_text">the family of type-2 triangles of $G^{\prime}$ whose old edges avoid $E(P^{\prime})\text{.}$ Since $B(B^{*})\subseteq B(P^{\prime})\text{,}$ we have $\mathcal{S}\subseteq(\mathcal{F}_{2})_{B^{*}}=\mathcal{F}(G^{\prime}-B(B^{*}))\text{,}$ and since $B^{*}$ is a maximum packing in $\mathcal{F}_{2}\text{,}$ the red edge of every member of $\mathcal{S}$ lies in $R(B^{*})=N\text{.}$ Choose a maximum packing $Q$ in $\mathcal{S}\text{,}$ put $c=|Q|\text{,}$ and let $h$ be the number of members of $Q$ whose red edge is private in $\mathcal{S}\text{.}$</span></p>
</div>
<div id="S3.p6" class="ltx_para">
<p id="S3.p6.1" class="ltx_p"><span id="S3.p6.1.1" class="ltx_text">The second transversal combines books formed by $B^{*}$ and $Q$ with a random bipartition. Pair each member of $Q$ with the member of $B^{*}$ containing its red edge. No member of $B^{*}$ is paired twice, as $Q$ is a packing. These pairs and the unpaired members of $B^{*}$ form $b$ books, whose supports are edge-disjoint since the old edges of $Q$ avoid $E(P^{\prime})\text{.}$ Every selection of one page per book consists of $b$ type-2 triangles and is therefore a maximum packing in $\mathcal{F}_{2}\text{.}$ Let $W$ be the set of old edges of the one-page books, so $|W|=2(b-c)\text{.}$ The set $C$ of <a href="#S2.Thmlemma2" title="Lemma 2.2. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> for these books lies in $W\cup N\text{,}$ since spines are edges of $N$ and a one-page book has its old edges in $W$ and its new edge in $N\text{.}$</span></p>
</div>
<div id="S3.p7" class="ltx_para">
<p id="S3.p7.1" class="ltx_p"><span id="S3.p7.1.1" class="ltx_text">Assign each vertex of $G^{\prime}$ a bit, independently and uniformly at random, and call an edge crossing if its ends receive different bits. Select $W$ and every non-crossing edge of $O^{\prime}\text{,}$ then add the new edge of each triangle of $G^{\prime}$ not yet met. A type-3 triangle has two vertices with the same bit and hence a non-crossing old edge, so the selected edges meet every triangle of $G^{\prime}\text{.}$ Their expected number is $|W|+\frac{1}{2}(|O^{\prime}|-|W|)$ plus the expected number of added new edges, which we bound in two parts.</span></p>
</div>
<div id="S3.p8" class="ltx_para">
<p id="S3.p8.1" class="ltx_p"><span id="S3.p8.1.1" class="ltx_text">A new edge is added only if both old edges of its triangle are crossing, and then it is non-crossing. Each edge of $N$ is non-crossing with probability $\frac{1}{2}\text{,}$ so the expected number of added edges in $N$ is at most $\frac{b}{2}\text{.}$</span></p>
</div>
<div id="S3.p9" class="ltx_para">
<p id="S3.p9.1" class="ltx_p"><span id="S3.p9.1.1" class="ltx_text">Now let an edge $xy\notin N$ be added as the new edge of a type-2 triangle $T$ not yet met. Then $T$ contains no edge of $N$ and avoids $W\text{,}$ hence avoids $C\text{,}$ and <a href="#S2.Thmlemma2" title="Lemma 2.2. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> for these books and $\mathcal{F}_{2}$ shows that $T$ is $uxy$ or $vxy$ for a two-page book $\{uvx,uvy\}$ with $uvx\in B^{*}$ and $uvy\in Q\text{.}$ The two edges that $T$ shares with the pages are old, so its new edge $xy$ is the opposite edge of the book. Since $uvy\in\mathcal{S}\subseteq(\mathcal{F}_{2})_{B^{*}}$ and $xy$ is a red edge outside $R(B^{*})=N\text{,}$ <a href="#S2.Thmlemma1" title="Lemma 2.1. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.1</span></a> shows that $uv$ is private in $(\mathcal{F}_{2})_{B^{*}}\text{,}$ hence in $\mathcal{S}\text{,}$ so $uvy$ is one of the $h$ members of $Q$ with a private red edge. Such a book contributes an added edge only if $uxy$ or $vxy$ is not yet met, which requires $x$ and $y$ to receive the same bit and $u$ or $v$ a different one. As $u,v,x,y$ are distinct, this has probability $\frac{1}{2}-\frac{1}{8}=\frac{3}{8}\text{.}$ Distinct added edges come from distinct books, as each book has one opposite edge, so the expected number of added edges outside $N$ is at most $\frac{3}{8}h\text{.}$ The expected total is at most</span></p>
<table id="S3.Ex6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$|W|+\frac{|O^{\prime}|-|W|}{2}+\frac{b}{2}+\frac{3}{8}h=\frac{|O^{\prime}|}{2}+\frac{3}{2}b-c+\frac{3}{8}h,$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
<p id="S3.p9.2" class="ltx_p"><span id="S3.p9.2.1" class="ltx_text">so some assignment of bits gives a transversal of $G^{\prime}$ of at most this size. Adding $E(A)$ and using $|O^{\prime}|=3n-a$ gives</span></p>
<table id="S3.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau(G)\leq\tfrac{3}{2}n+\tfrac{5}{2}a+\tfrac{3}{2}b-c+\tfrac{3}{8}h.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4)</span></td></tr></tbody>
</table>
</div>
<div id="S3.p10" class="ltx_para">
<p id="S3.p10.1" class="ltx_p"><span id="S3.p10.1.1" class="ltx_text">For the third transversal, we add a third page to some of these books and include the remaining members of $P^{\prime}\text{.}$ Choose a maximum packing $Q_{1}$ in $\mathcal{S}_{Q}=\mathcal{F}(G^{\prime}-B(P^{\prime})-B(Q))$ and put $d=|Q_{1}|\text{.}$ The red edge of each member of $Q_{1}$ lies in $R(Q)\text{,}$ and distinct members of $Q_{1}$ have distinct red edges. Add each member of $Q_{1}$ as a third page to the book whose spine is its red edge, and add the members of $P^{\prime}\setminus B^{*}$ as one-page books. The old edges of $Q_{1}$ avoid $E(P^{\prime})\cup E(Q)\text{,}$ so the supports remain edge-disjoint. Every selection of one page per book is a packing in $G^{\prime}$ with $m$ members, $b$ of them of type $2\text{,}$ hence maximal in $G^{\prime}\text{.}$ These $m$ books have $m+c+d$ pages, so <a href="#S2.Thmlemma2" title="Lemma 2.2. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.2</span></a> gives a transversal of $G^{\prime}$ of size at most $3m-c-d\text{.}$ Adding $E(A)$ and using $a+m\leq n$ gives</span></p>
<table id="S3.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau(G)\leq 3n-c-d.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5)</span></td></tr></tbody>
</table>
</div>
<div id="S3.p11" class="ltx_para">
<p id="S3.p11.1" class="ltx_p"><span id="S3.p11.1.1" class="ltx_text">The fourth transversal consists of $E(A)\text{,}$ the old edges of $P^{\prime}\text{,}$ and a transversal of $\mathcal{S}\text{.}$ The first two sets have at most $3a+3m-b\leq 3n-b$ edges. A triangle avoiding them lies in $G^{\prime}-B(P^{\prime})$ and is not of type $3\text{,}$ since a type-3 triangle avoiding $B(P^{\prime})$ would avoid $E(P^{\prime})$ and could be added to $P^{\prime}\text{.}$ So it belongs to $\mathcal{S}\text{.}$ <a href="#S2.Thmlemma3" title="Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Lemma</span> <span class="ltx_text ltx_ref_tag">2.3</span></a> applied to $G^{\prime}-B(P^{\prime})\text{,}$ with $Q\text{,}$ $Q_{1}\text{,}$ $c\text{,}$ $d\text{,}$ $h$ in the roles of $P\text{,}$ $Q\text{,}$ $p\text{,}$ $q\text{,}$ $u\text{,}$ gives $\tau(\mathcal{S})\leq\frac{9}{4}c+\frac{3}{2}d-\frac{1}{4}h$ by <a href="#S2.E2" title="In Lemma 2.3. ‣ 2 Colored Triangle Families ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equation</span> <span class="ltx_text ltx_ref_tag">2</span></a>, so</span></p>
<table id="S3.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$\tau(G)\leq 3n-b+\tfrac{9}{4}c+\tfrac{3}{2}d-\tfrac{1}{4}h.$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(6)</span></td></tr></tbody>
</table>
</div>
<div id="S3.p12" class="ltx_para">
<p id="S3.p12.1" class="ltx_p"><span id="S3.p12.1.1" class="ltx_text">Multiply <a href="#S3.E3" title="In Proof of . ‣ 3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">3</span></a>, <a href="#S3.E4" title="Equation 4 ‣ Proof of . ‣ 3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>, <a href="#S3.E5" title="Equation 5 ‣ Proof of . ‣ 3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5</span></a> and <a href="#S3.E6" title="Equation 6 ‣ Proof of . ‣ 3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a> by $20,8,19,12\text{,}$ respectively, and add. The coefficients of $a,b,c,h$ cancel, giving</span></p>
<table id="S3.Ex7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center">$$59\tau(G)\leq 165n-d\leq 165\nu(G).$$</td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td></tr></tbody>
</table>
</div>
</div>
<div id="Thmremarkx1" class="ltx_theorem ltx_theorem_remark">
<h6 class="ltx_title ltx_runin ltx_title_theorem"><span class="ltx_tag ltx_tag_theorem"><span id="Thmremarkx1.2" class="ltx_text ltx_font_italic">Remark</span></span><span id="Thmremarkx1.3" class="ltx_text ltx_font_italic">.</span></h6>
<div id="Thmremarkx1.p1" class="ltx_para">
<p id="Thmremarkx1.p1.1" class="ltx_p">The weights are best possible for the system <a href="#S3.E3" title="In Proof of . ‣ 3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">Equations</span> <span class="ltx_text ltx_ref_tag">3</span></a>, <a href="#S3.E4" title="Equation 4 ‣ Proof of . ‣ 3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a>, <a href="#S3.E5" title="Equation 5 ‣ Proof of . ‣ 3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5</span></a> and <a href="#S3.E6" title="Equation 6 ‣ Proof of . ‣ 3 The General Bound ‣ A Bound Below 2.8 for Tuza’s Conjecture" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a>. For $a=c=12n/59\text{,}$ $b=m=39n/59\text{,}$ and $d=h=0\text{,}$ which satisfy the relations $a+m\leq n\text{,}$ $d\leq c\leq b\leq m\text{,}$ and $h\leq c$ that hold in the proof, all four right-hand sides equal $165n/59\text{.}$ So no nonnegative combination of the four inequalities gives a smaller constant.</p>
</div>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography" id="references">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bibx1" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Hax99]</span>
<span class="ltx_bibblock">
P. E. Haxell, <em id="bib.bibx1.2" class="ltx_emph ltx_font_italic">Packing and covering triangles in graphs</em>,
Discrete Mathematics <span id="bib.bibx1.3" class="ltx_text ltx_font_bold">195</span> (1999), 251–254.
<a href="https://doi.org/10.1016/S0012-365X(98)00183-6" title="" class="ltx_ref ltx_href">doi:10.1016/S0012-365X(98)00183-6</a>.

</span></li>
      
<li id="bib.bibx2" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Tuz90]</span>
<span class="ltx_bibblock">
Z. Tuza, <em id="bib.bibx2.2" class="ltx_emph ltx_font_italic">A conjecture on triangles of graphs</em>,
Graphs and Combinatorics <span id="bib.bibx2.3" class="ltx_text ltx_font_bold">6</span> (1990), 373–380.
<a href="https://doi.org/10.1007/BF01787705" title="" class="ltx_ref ltx_href">doi:10.1007/BF01787705</a>.

</span></li>
      
<li id="bib.bibx3" class="ltx_bibitem ltx_align_left"><span class="ltx_tag ltx_tag_bibitem">[Yi26]</span>
<span class="ltx_bibblock">
L. Yi, <em id="bib.bibx3.2" class="ltx_emph ltx_font_italic">An improved upper bound for Tuza’s conjecture via 2-colorable triangle families</em>,
<a href="https://arxiv.org/abs/2608.23010v1" title="" class="ltx_ref ltx_href">arXiv:2608.23010v1</a> (2026).

</span></li>
    
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Sichen Wang"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="A Bound Below 2.8 for Tuza's Conjecture"></div>

</article>
