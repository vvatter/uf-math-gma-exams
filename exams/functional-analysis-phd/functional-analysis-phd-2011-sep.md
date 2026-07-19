# Functional Analysis PhD exam, September 2011

*Do any SIX problems. Write solutions in a neat and logical fashion, giving complete reasons for all steps.*

**1.** Let \(X\) be a vector space and \(\mathcal F\) a vector space of linear functionals on \(X\) that separates points.
* a) Write down a base for the weak topology on \(X\) induced by \(\mathcal F\).
* b) Prove that if a linear functional \(\varphi\) on \(X\) is continuous in this topology, then \(\varphi \in \mathcal F\).

**2.** Let \(X\) be a normed vector space. Suppose \((x_n)\) is a sequence in \(X\), converging weakly to \(x \in X\). (That is, \(\varphi(x_n) \to \varphi(x)\) for every norm-continuous linear functional \(\varphi\).) Prove that there is a sequence \(y_n\), where each \(y_n\) is a convex combination of finitely many of the \(x_n\), such that \(\lim \lVert y_n-x\rVert=0\).

**3.** Let \(T\) be a bounded linear operator on a Hilbert space \(H\). Prove that if both \(T\) and \(T^*\) are bounded below, then \(T\) is invertible. (Recall that \(T\) bounded below means that there is a constant \(c>0\) so that \(\lVert Tx\rVert \geq c\lVert x\rVert\) for all \(x\in H\).)

**4.** Let \(T\) be a bounded linear operator on Hilbert space. Prove that there is a positive operator \(P\) and a partial isometry \(U\) such that \(\ker U=\ker T\) and \(T=UP\) (that is, \(T\) has a polar decomposition).

**5.** Let \(T\) be a Hilbert space operator with \(\lVert T\rVert\leq 1\).
* a) Prove that \(I-T^*T\) and \(I-TT^*\) are positive operators.
* b) Prove that
  \[
  T(I-T^*T)^{1/2}=(I-TT^*)^{1/2}T.
  \]
  (Hint: approximate \(\sqrt{1-x}\) by polynomials \(p_n(x)\) and use the spectral theorem.)

**6.** Let \((\lambda_n)\) be a bounded sequence of complex numbers. Consider the weighted shift operator \(S\) defined on \(\ell^2(\mathbb N)\) by
\[
S(x_0,x_1,x_2,\ldots)=(0,\lambda_0x_0,\lambda_1x_1,\lambda_2x_2,\ldots).
\]
Characterize those sequences \((\lambda_n)\) for which \(S\) is compact.

**7.** Let \(A\) be a Banach algebra (over \(\mathbb C\)) and \(a\in A\).
* a) Define the spectrum of \(a\).
* b) Show that if \(\lambda\in\mathbb C\) and \(|\lambda|>\lVert a\rVert\), then \(\lambda\) does not lie in the spectrum of \(a\).
