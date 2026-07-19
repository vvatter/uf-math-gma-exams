# Algebra, PhD exam, September 1992

*Please read through all the questions carefully before you begin. Your five best solutions will count. You may quote theorems from the course (within reason) as long as you make it clear that you are doing so and state them clearly. All rings have 1 and all modules are unital. Different parts of the same question may or may not be related, and do not usually carry equal credit.*

**1.** Let \(G\) be a finite group and \(p\) a prime. The normalizer of a subgroup \(K\leq G\) is defined to be the set of all elements \(x\in G\) such that \(x^{-1}Kx=K\).
* (a) If \(H\) is a normal subgroup of \(G\) and \(P\) is a Sylow \(p\)-subgroup of \(H\), show that every element of \(G\) can be written in the form
  \[
  g=hn,
  \]
  where \(h\in H\) and \(n\) belongs to the normalizer in \(G\) of \(P\).
* (b) Hence or otherwise show that the normalizer of a Sylow \(p\)-subgroup of a finite group is its own normalizer.

**2.** This problem has two parts.
* (a) Let \(R\) be a commutative ring, and \(M\) an \(R\)-module such that all of the localizations \(M_{\mathfrak m}\) at maximal ideals \(\mathfrak m\) of \(R\) are zero. Prove that \(M=0\). (Hint: Consider the annihilator in \(R\) of a nonzero element of \(M\).)
* (b) Suppose \(R\) is a subring of a field \(K\) and \(S\) is a multiplicative subset of \(R\) not containing \(0\). Show that if \(x\in K\) is integral over \(S^{-1}R\), then it may be written as \(x=b/s\), where \(s\in S\) and \(b\) is integral over \(R\).

**3.** Let \(k\) be an algebraically closed field and \(I\) a radical ideal of \(k[X_1,\ldots,X_n]\). Show that the set \(V(I)\) of simultaneous zeroes of \(I\) in \(k^n\) is irreducible in the Zariski topology (i.e., is not the union of two proper subsets which are algebraic sets) if and only if \(k[X_1,\ldots,X_n]/I\) is an integral domain. Give an example to show that if \(I\) is not radical, then \(V(I)\) may be irreducible without \(k[X_1,\ldots,X_n]/I\) being an integral domain.

**4.** Prove that all simple groups of order \(60\) are isomorphic to the alternating group on five letters.

**5.** In this question \(R\) is a ring with left modules \(A,B\) and \(C\) and a right module \(M\). For each of the following statements give a proof or furnish a counterexample.
* a) Given a surjective homomorphism \(f:B\to C\) of left \(R\)-modules, the induced homomorphism
  \[
  1\otimes f:M\otimes_R B\longrightarrow M\otimes_R C
  \]
  of abelian groups is also surjective.
* b) Given an injective homomorphism \(g:A\to B\) of left \(R\)-modules, the induced homomorphism
  \[
  1\otimes g:M\otimes_R A\longrightarrow M\otimes_R B
  \]
  of abelian groups is also injective.
* c) If \(R=\mathbb Z\) and \(M=\mathbb Q\), then every exact sequence
  \[
  0\longrightarrow A\xrightarrow{g}B\xrightarrow{f}C\longrightarrow 0
  \]
  of \(R\)-modules induces an exact sequence
  \[
  0\longrightarrow M\otimes_R A\xrightarrow{1\otimes g}M\otimes_R B\xrightarrow{1\otimes f}M\otimes_R C\longrightarrow 0
  \]
  of abelian groups.

**6.** Let \(G\) be a finite group and \(\mathbb CG\) the complex group algebra. Let \(M\) be a finite dimensional (left) \(\mathbb CG\)-module. An Hermitian form \((\ ,\ )\) on \(M\) is said to be \(G\)-invariant if
\[
(gm,gn)=(m,n),\qquad \text{for all }g\in G,\ m,n\in M.
\]
* a) Use the trick of averaging over the group to show that \(M\) has a \(G\)-invariant, positive definite hermitian form.
* b) Using (a) or by another method, prove: If \(N\) is a \(\mathbb CG\)-submodule of \(M\), then there is a \(\mathbb CG\)-submodule \(N'\) with \(M=N\oplus N'\).

**7.** Let \(R\) be the ring of lower triangular \(n\times n\) complex matrices.
* a) Determine the Jacobson radical of \(R\) (You may use any properties of the radical as long as you state them correctly.).
* b) Give an example to show that the converse of Schur’s Lemma is false, namely, that there exist modules which are not simple (irreducible) but whose endomorphisms form a division ring. (Hint: Use \(R\) with \(n=2\) and the obvious module for this ring.)

**8.** Prove or give a counterexample in each case.
* (a) If we have Galois extensions of fields \(K\subset L\) and \(L\subset M\), then the extension \(K\subset M\) is Galois.
* (b) If we have algebraic extensions of fields \(K\subset L\) and \(L\subset M\), then the extension \(K\subset M\) is algebraic.
* (c) Every finite extension of an infinite field is separable.

**9.** This problem has four parts.
* a) Let \(F\) be any field and \(p\) a prime. Show that the polynomial \(X^p-a\in F[X]\) either has a root in \(F\) or is irreducible.
* b) Let \(K\) be a subfield of the real numbers and \(f\in K[X]\) an irreducible cubic with three real roots. Show that if \(L\) is obtained from \(K\) by adjoining a real number \(\alpha\) with \(\alpha^p\in K\) for some prime \(p\neq 3\), then \(f\) remains irreducible over \(L\).
* c) Let \(E\) be a splitting field of \(f\) over \(K\). Show that there is an intermediate field \(K_1\) with \([E:K_1]=3\) which is a subfield of the real numbers and a radical extension of \(K\).
* (d) Prove that \(f\) remains irreducible over any subfield of the real numbers which is a radical extension of \(K\). (Hints: First, show that we may reduce to the case where \(K=K_1\) and the radical extension is given by an irreducible polynomial as in (a). Then use (b) for the case \(p\neq 3\). If \(p=3\), use the normality of \(E\) over \(K\) and the facts that \([L:K]=3=[E:K]\) to show that \(f\) cannot have a root in \(L\).)

**10.** Let \(R\) be a semisimple artinian ring.
* a) Use the structure theorem to show that as a left \(R\)-module,
  \[
  R=\bigoplus_i Re_i,
  \]
  where the elements \(e_i\) are idempotents such that \(\sum_i e_i=1_R\) and \(Re_i\) are minimal left ideals.
* b) Deduce that any left \(R\)-module \(M\) is the sum of submodules each isomorphic to some \(Re_i\). (Hint: For \(m\in M\) we have \(Rm=\bigoplus_i Re_i m\), the modules \(Re_i\) are simple and the map \(re_i\mapsto re_i m\) defines an \(R\)-module epimorphism \(Re_i\to Re_i m\). Now use Schur’s Lemma.)
* c) Show that \(M\) is in fact the direct sum of such submodules.
* d) Deduce that every left \(R\)-module is projective.
