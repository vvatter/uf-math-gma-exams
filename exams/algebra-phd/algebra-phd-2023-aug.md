# Algebra, PhD exam, August 2023

*Answer seven problems. Write your answers clearly in complete English sentences. You may quote results (within reason) as long as you state them clearly.*

**1.** Briefly explain your answers to the following, freely using standard results.
* (a) Find a polynomial \(f(x)\in\mathbb{F}_3[x]\) such that \(K=\mathbb{F}_3[x]/(f(x))\) is a field with 27 elements.
* (b) Show that \(K\) is Galois over \(\mathbb{F}_3\), and write down the automorphisms of \(K\) fixing \(\mathbb{F}_3\).
* (c) For which \(n\) is there an extension \(L/K\) of fields such that \(L\) has \(3^n\) elements?

**2.** Let \(f(x)\in\mathbb{Q}[x]\) be an irreducible polynomial of degree 5 with exactly three real roots. State and prove a result about the Galois group of the splitting field of \(f(x)\) over \(\mathbb{Q}\).

**3.** Let \(K=\mathbb{Q}(\zeta_{101})\), where \(\zeta_{101}\) is a primitive 101th root of unity.
* (a) Show that there is a unique subfield \(F\) of \(K\) such that \([F:\mathbb{Q}]=2\).
* (b) How many subfields of \(K\) contain \(F\)? Of these, which are Galois extensions of \(\mathbb{Q}\)?

**4.** Recall that the Abelianization of a group \(G\) is \(G^{\mathrm{ab}}:=G/[G,G]\).
* (a) Formulate and prove a universal property for abelianization.
* (b) Show that abelianization is left adjoint to the forgetful functor from the category of abelian groups to the category of groups.

**5.** Let \(K\) be a field and \(V\) a \(K\)-vector space. Recall that an alternating bilinear map \(f:V\times V\to W\) is a function which is \(K\)-linear in each coordinate (i.e. \(K\)-multilinear) and such that \(f(v,v)=0\) for all \(v\in V\). Show that the functor \(\operatorname{Alt}_V^2:\operatorname{Vec}_K\to\operatorname{Sets}\) defined by
\[
\operatorname{Alt}_V^2(W)=\{f:V\times V\to W:f\text{ is alternating bilinear}\}
\]
is a representable functor. (The representing object, usually denoted \(\Lambda^2(V)\), is an exterior power of \(V\).) Suggestion: A quotient of \(V\otimes_K V\).

**6.** Give examples of the following, and briefly explain your answers.
* (a) a ring \(R\) and a short exact sequence of \(R\)-modules
  \[
  0\to A\to B\to C\to 0
  \]
  that is not split.
* (b) a flat \(\mathbb{Z}\)-module which is not free.
* (c) a non-zero injective \(\mathbb{Z}\)-module.

**7.** Let \(R\) be a ring and \(M\) and \(N\) be \(R\)-modules. Let \(P_\bullet\) and \(P'_\bullet\) be projective resolutions of \(M\) and \(N\). Given a morphism of \(R\)-modules \(f:M\to N\), show that there exists a morphism of resolutions \(f:P_\bullet\to P'_\bullet\) extending \(f\). In other words, show there exists \(f_0,f_1,f_2,\ldots\) making the following diagram commute:

**8.** What are the dimensions of \(\mathbb{Q}[x]/(x^5)\otimes_{\mathbb{Q}}\mathbb{Q}[x]/(x^6)\) and of \(\mathbb{Q}[x]/(x^5)\otimes_{\mathbb{Q}[x]}\mathbb{Q}[x]/(x^6)\) as \(\mathbb{Q}\)-vector spaces?

**9.** Let \(F\) be a field. Prove that the power series ring
\[
F\llbracket x\rrbracket=\left\{\sum_{n=0}^{\infty}a_nx^n:a_n\in F\right\}
\]
is a Noetherian ring.

**10.** Let \(B=\mathbb{Q}[x,y]/(xy)\) and \(A=\mathbb{Q}[t]\). Note that both have Krull dimension 1. A homomorphism \(f:A\to B\) of rings turns \(B\) into an \(A\)-module: for \(a\in A\) and \(b\in B\), \(a.b=f(a)b\).
* (a) Explain why the Noether normalization lemma implies that there is a map \(A\to B\) making \(B\) into a finitely generated \(A\)-module.
* (b) Show that the map \(A\to B\) sending \(t\) to \(x\) does not make \(B\) into a finitely generated \(A\)-module.
* (c) Find an explicit map \(A\to B\) that makes \(B\) into a finitely generated \(A\)-module and explain your answer.

**11.** Let \(K\) be a field and consider the function \(v:K(x)\to\mathbb{Z}\cup\{\infty\}\) given by
\[
v(f/g)=\deg(g)-\deg(f),\qquad v(0)=\infty.
\]
* (a) Show that \(v\) is a discrete valuation on \(K(x)\).
* (b) Show that the valuation ring \(\mathcal{O}_v=\{R\in K(x):v(R)\geq 0\}\) is a local ring. (Do not appeal to general facts about DVR’s.)
