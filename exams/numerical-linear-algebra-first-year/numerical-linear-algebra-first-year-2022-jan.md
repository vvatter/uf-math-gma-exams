# Numerical Linear Algebra first year exam, January 2022

*Do 4 (four) problems.*

**1.** Let \(A \in \mathbb{C}^{m\times n}\) and \(B \in \mathbb{C}^{n\times p}\). Prove or provide a counterexample to the following statements. Justify each nontrivial step.
* (a) The Frobenius norm satisfies \(\lVert AB\rVert_F \leq \lVert A\rVert_F\lVert B\rVert_F\).
* (b) \(\lVert A\rVert_2 \leq \lVert A\rVert_F\), where \(\lVert A\rVert_F\) is the Frobenius norm of \(A\).

**2.** Define the matrices \(A\) and \(B\) by
\[
A=\begin{pmatrix}1&2&3\\2&4&6\\1&2&3\\2&4&6\end{pmatrix},\qquad B=\begin{pmatrix}1&1&0\\0&1&3\\0&1&3\\2&0&0\end{pmatrix}.
\]
* (a) Find an economy singular value decomposition of \(A\).
* (b) Find an economy QR decomposition of \(B\).

**3.** Let \(\lVert\cdot\rVert\) be a subordinate (induced) matrix norm.
* (a) If \(E\) is \(n\times n\) with \(\lVert E\rVert<1\), then show \(I+E\) is nonsingular and
  \[
  \lVert(I+E)^{-1}\rVert\leq \frac{1}{1-\lVert E\rVert}.
  \]
* (b) If \(A\) is \(n\times n\) invertible and \(E\) is \(n\times n\) with \(\lVert A^{-1}\rVert\lVert E\rVert<1\), then show \(A+E\) is nonsingular and
  \[
  \lVert(A+E)^{-1}\rVert\leq \frac{\lVert A^{-1}\rVert}{1-\lVert A^{-1}\rVert\lVert E\rVert}.
  \]

**4.** Let \(P\in\mathbb{C}^{m\times m}\) be a projector. Show that \(\lVert P\rVert_2=1\) if and only if \(P\) is an orthogonal projector.

**5.** Suppose \(A\) is Hermitian positive definite.
* (a) Prove that each principal submatrix of \(A\) is Hermitian positive definite.
* (b) Prove that an element of \(A\) with largest magnitude lies on the diagonal.
* (c) Prove that \(A\) has a Cholesky decomposition.
