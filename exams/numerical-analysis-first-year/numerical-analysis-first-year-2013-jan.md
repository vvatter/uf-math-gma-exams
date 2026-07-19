# Numerical Analysis first year exam, January 2013

*Answer any 4 questions.*

**1.** Suppose that \(A \in \mathbb{C}^{n\times n}\) is Hermitian with \(\lambda_1\) and \(\lambda_n\) the smallest and largest eigenvalues of \(A\) respectively. Show that
\[
\lambda_1\lVert x\rVert^2 \leq x^*Ax \leq \lambda_n\lVert x\rVert^2
\]
for all \(x \in \mathbb{C}^n\).

**2.** This problem has three parts.
* (a) Suppose \(p\) and \(q \in \mathbb{R}\) with \(p\) and \(q\) positive and \(p^{-1}+q^{-1}=1\). Show that for any matrix \(A \in \mathbb{C}^{m\times n}\), we have \(\lVert A\rVert_p=\lVert A^*\rVert_q\), where \(A^*\) is the conjugate transpose of \(A\).
* (b) Prove that
  \[
  \lVert A\rVert_2^2 \leq \lVert A\rVert_p\lVert A\rVert_q
  \]
  for any \(A \in \mathbb{C}^{m\times n}\) and any positive \(p\) and \(q \in \mathbb{R}\) with \(p^{-1}+q^{-1}=1\).
* (c) Prove that for any \(p\geq 1\) and any diagonal matrix \(D \in \mathbb{C}^{n\times n}\), we have
  \[
  \lVert D\rVert_p=\max\{\lvert d_{ii}\rvert:1\leq i\leq n\}.
  \]

**3.** This problem has two parts.
* (a) Show that the eigenvalues of a projector are either \(0\) or \(1\).
* (b) Show that a projector \(P\) is orthogonal if and only if \(P=P^*\).

**4.** Show that the element of largest magnitude in a Hermitian, positive definite matrix lies on the diagonal.

**5.** Suppose that \(A \in \mathbb{C}^{n\times n}\) is an invertible matrix, \(u \in \mathbb{C}^n\), and \(v \in \mathbb{C}^n\).
* (a) Show that
  \[
  \det(A-uv^*)=(1-v^*A^{-1}u)\det A.
  \]
* (b) Suppose that \(A\) is a real diagonal matrix and \(u=v\) with \(u_i\neq 0\) for each \(i\). Show that the eigenvalues of \(A-uu^*\) are the roots of
  \[
  \sum_{i=1}^n \frac{\lvert u_i\rvert^2}{a_{ii}-\lambda}=1.
  \]
