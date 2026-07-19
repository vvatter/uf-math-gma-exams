# Numerical Linear Algebra first year exam, January 2014

*Answer any 4 questions.*

**1.** Suppose that \(A \in \mathbb{C}^{n \times n}\) is a normal matrix; that is, \(AA^* = A^*A\) where \(A^*\) is the conjugate transpose of \(A\). Show that \(A = X\Lambda X^*\) where \(\Lambda\) is diagonal and \(X\) is unitary; that is, show that \(A\) can be diagonalized and its eigenvector matrix is unitary.

**2.** This problem has four parts.
* (a) Suppose \(p\) and \(q \in \mathbb{R}\) with \(p\) and \(q\) positive and \(p^{-1}+q^{-1}=1\). Show that for any matrix \(A \in \mathbb{C}^{m \times n}\), we have \(\lVert A\rVert_p=\lVert A^*\rVert_q\). Here \(\lVert A\rVert_p\) denotes the matrix \(p\)-norm induced by the vector \(p\)-norm.
* (b) Prove that
  \[
  \lVert A\rVert_2^2 \leq \lVert A\rVert_p\lVert A\rVert_q
  \]
  for any \(A \in \mathbb{C}^{m \times n}\) and any positive \(p\) and \(q \in \mathbb{R}\) with \(p^{-1}+q^{-1}=1\).
* (c) Prove that for any \(p \geq 1\) and any diagonal matrix \(D \in \mathbb{C}^{n \times n}\), we have
  \[
  \lVert D\rVert_p=\max\{\lvert d_{ii}\rvert:1\leq i\leq n\}.
  \]
* (d) Show that \(\lVert A\rVert_2\) is the largest singular value of \(A\).

**3.** This problem has two parts.
* (a) For any matrices \(A \in \mathbb{C}^{n \times m}\) and \(B \in \mathbb{C}^{m \times n}\), show that the nonzero eigenvalues of \(AB\) and \(BA\) are the same.
* (b) If \(AB\) is normal, \(\lVert\,\cdot\,\rVert_2\) is the 2-norm of a matrix, and \(\lVert\,\cdot\,\rVert\) is an induced matrix norm, then show that \(\lVert AB\rVert_2 \leq \lVert BA\rVert\).

**4.** This problem has two parts.
* (a) Show that the eigenvalues of a projector are either 0 or 1.
* (b) Show that a projector \(P\) is orthogonal if and only if \(P=P^*\).

**5.** Suppose that \(A \in \mathbb{C}^{n \times n}\) and consider the series
\[
S=\sum_{i=0}^{\infty}A^i.
\]
Show that the series is convergent if and only if the spectral radius of \(A\) is strictly smaller than 1. If the series is convergent, then show that \(S\) is invertible and \(S=(I-A)^{-1}\).
