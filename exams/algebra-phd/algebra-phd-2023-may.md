# Algebra PhD exam, May 2023

*Answer seven problems. Write your answers clearly in complete English sentences. You may quote results (within reason) as long as you state them clearly.*

**1.** Let \(K\) be the splitting field of \(x^7-2\) over \(\mathbb{Q}\). What is \([K:\mathbb{Q}]\)? Justify your answer.

**2.** Give an example of a Galois extension of \(\mathbb{Q}(\zeta_5)\) with degree \(5\) (where \(\zeta_5\) is a primitive 5th root of unity). Give an example of a Galois extension of \(\mathbb{Q}\) with degree \(5\). Justify your answers.

**3.** Let \(K\) be a field and \(G\) a finite subgroup of \(\operatorname{Aut}(K)\).
* (i) What does the “theorem of the fixed field” say about \([K:K^G]\)?
* (ii) Use the theorem of the fixed field to show that if \(K/F\) is a finite extension of fields then \(\#\operatorname{Aut}(K/F)\leq [K:F]\) with equality if and only if \(F\) is the fixed field of \(\operatorname{Aut}(K/F)\).
* (iii) Use the theorem of the fixed field to show that if \(F=K^G\) then \(K/F\) is a Galois extension with Galois group \(G\).

**4.** Let \(\mathrm{Groups}\) denote the category of groups and \(\mathrm{Sets}\) denote the category of sets.
* (i) Use free groups to construct a left adjoint to the forgetful functor \(U:\mathrm{Groups}\to\mathrm{Sets}\). (You can skip checking “naturality” i.e. compatibility with morphisms.)
* (ii) Show that the functor \(F:\mathrm{Groups}\to\mathrm{Sets}\) defined by
  \[
  F(G)=\{(x,y)\in G\times G:xyx^{-1}y^{-1}=1\}
  \]
  is a representable functor. (Again, you can skip checking “naturality”.)

**5.** Let \(k\) be a field. For a \(k\)-vector space \(V\), recall that the dual vector space \(V^*\) is defined to be the \(k\)-vector space of linear functionals on \(V\), i.e. linear transformations from \(V\) to \(k\).
* (i) Construct a natural linear transformation \(\psi:V^*\otimes_k W^*\to(V\otimes_k W)^*\).
* (ii) Show that \(\psi\) is an isomorphism if \(V\) and \(W\) are finite dimensional.

**6.** Let \(R\) be a unital ring.
* (i) State at least two equivalent definitions of a projective \(R\)-module. (You don’t need to show they are equivalent, but you should include any definition you want to use in the next part.)
* (ii) Let \(M\) and \(N\) be \(R\)-modules with \(M\subset N\). If \(M\) is projective and \(N/M\) is projective, prove that \(N\) is projective.

**7.** Are the functors \(F(A)=\operatorname{Hom}_{\mathbb{Z}}(A,\mathbb{Q}/\mathbb{Z})\) and \(G(A)=\operatorname{Hom}_{\mathbb{Z}}(A,\mathbb{Z})\) from the category of \(\mathbb{Z}\)-modules to the category of \(\mathbb{Z}\)-modules exact? Justify your answer.

**8.** Prove that the intersection of all prime ideals in a commutative ring is the nilradical. (Suggestion: for one direction, given a non-nilpotent element \(a\) consider the set of all ideals not containing any power of \(a\).)

**9.** Let \(\mathbb{R}\) and \(\mathbb{C}\) denote the real and complex numbers as usual.
* (i) Give an example of two different maximal ideals of \(\mathbb{R}[x]\) which have the same zero set in the affine line \(\mathbb{A}^1_{\mathbb{R}}\).
* (ii) Give an example of two ideals of \(\mathbb{C}[x]\) which have the same zero set in \(\mathbb{A}^1_{\mathbb{C}}\).
* (iii) State Hilbert’s Nullstellensatz.

**10.** Let \(R\) be a commutative ring and \(D\) a multiplicatively closed subset of \(R\) containing \(1\). State the universal property for the localization \(D^{-1}R\), show that any two rings satisfying the universal property are isomorphic, and construct a ring satisfying the universal property. (Checking the construction is well-defined will involve a variety of verifications which you can skip. But do check it satisfies the universal property.)

**11.** Give an example of the following, and briefly justify your answers:
* (i) A discrete valuation ring whose field of fractions is not of characteristic zero.
* (ii) A Dedekind domain that is not a unique factorization domain.
