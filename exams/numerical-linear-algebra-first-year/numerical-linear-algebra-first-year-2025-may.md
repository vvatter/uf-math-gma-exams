# Numerical Linear Algebra, first year exam, May 2025

*Do 4 (four) problems.*

**1.** Assume \(A \in \mathbb{C}^{m\times m}\).
* (a) Show that \(A\) has a Schur decomposition.
* (b) If \(A\) is normal, show that \(A\) is diagonalizable.

**2.** Suppose \(A\) is Hermitian positive definite.
* (a) Prove that each principal submatrix of \(A\) is Hermitian positive definite.
* (b) Prove that an element of \(A\) with largest magnitude lies on the diagonal.
* (c) Prove that \(A\) has a Cholesky decomposition.

**3.** This problem has two parts.
* (a) Show that \(\lVert x\rVert_\infty\) is equivalent to \(\lVert x\rVert_2\) for all \(x\in\mathbb{R}^n\). That is to find \(C\) and \(c\) such that \(c\lVert x\rVert_\infty\leq \lVert x\rVert_2\leq C\lVert x\rVert_\infty\), for all \(x\in\mathbb{R}^n\). Note that the constants should be determined so that the equalities hold for some nonzero \(x\in\mathbb{R}^n\).
* (b) Show that \(\lVert QA\rVert_2=\lVert A\rVert_2\) if \(Q\) is a unitary matrix.

**4.** Assume that \(A\in\mathbb{C}^{n\times n}\) and there exists \(p\geq 1\) such that \(\lVert A\rVert_p<1\), where \(\lVert\cdot\rVert_p\) is a vector-induced matrix norm.
* (a) Prove that \(I-A\) is invertible.
* (b) Prove that
  \[
  (I-A)^{-1}=\sum_{k=0}^{\infty}A^k.
  \]
* (c) Prove that \(\lVert A\rVert_q\lVert A^{-1}\rVert_q\geq 1\), \(\forall\,1\leq q\leq\infty\).
* (d) Prove that
  \[
  \frac{1}{1+\lVert A\rVert_p}\leq \lVert(I-A)^{-1}\rVert_p\leq\frac{1}{1-\lVert A\rVert_p}.
  \]

**5.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\). Let \(u_j\) denote column \(j\) of \(U\).
* (a) Suppose \(\operatorname{rank}(A)=p<n<m\). Show \(\{u_1,u_2,\ldots,u_p\}\) is a basis for \(\operatorname{Col}(A)\) and \(\{u_{p+1},u_{p+2},\ldots,u_m\}\) is a basis for \(\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank and \(x\neq 0\). Let \(\sigma_i\), \(i=1,\ldots,n\), be the singular values of \(A\). Show
  \[
  \sigma_1\geq\frac{\lVert Ax\rVert_2}{\lVert x\rVert_2}\geq\sigma_n>0.
  \]
  If you want to use the property that \(\lVert A\rVert_2=\sigma_1\), then you must prove that it holds.
