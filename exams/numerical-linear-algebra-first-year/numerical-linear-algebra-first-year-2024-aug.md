# Numerical Linear Algebra, first year exam, August 2024

*Do 4 (four) problems.*

**1.** Let \(A\) be an \(m\times n\) matrix (\(m\ge n\)) and let \(A=\widehat Q\widehat R\) be a reduced \(QR\) factorization of \(A\). Prove that \(A\) has full rank if and only if the diagonal entries of \(\widehat R\) are nonzero.

**2.** Assume that \(A\in\mathbb C^{n\times n}\) and there exists \(p\ge 1\) such that \(\|A\|_p<1\), where \(\|\cdot\|_p\) is a vector-induced matrix norm.
* (a) Prove that \(I-A\) is invertible.
* (b) Prove that
  \[
  (I-A)^{-1}=\sum_{k=0}^{\infty}A^k.
  \]
* (c) Prove that \(\|A\|_q\|A^{-1}\|_q\ge 1\), \(\forall\,1\le q\le\infty\).
* (d) Prove that
  \[
  \frac{1}{1+\|A\|_p}\le \|(I-A)^{-1}\|_p\le\frac{1}{1-\|A\|_p}.
  \]

**3.** Suppose \(A\) is Hermitian positive definite.
* (a) Prove that each principal submatrix of \(A\) is Hermitian positive definite.
* (b) Prove that an element of \(A\) with largest magnitude lies on the diagonal.
* (c) Prove that \(A\) has a Cholesky decomposition.

**4.** Let \(\mathbf v=[2,-1,1]^T\) and \(H=(\operatorname{span}\{\mathbf v\})^\perp\).
* (a) Find the matrix \(P_{\mathbf v}\), the orthogonal projection onto \(\operatorname{span}\{\mathbf v\}\).
* (b) Find the matrix \(P_H\), the orthogonal projection onto \(H\).
* (c) Find \(Q_H\), the unitary matrix that reflects across \(H\).

**5.** Let \(A,\delta A\in\mathbb R^{n\times n}\) be full rank and \(b,x\) and \(\delta x\in\mathbb R^n\). Prove that if
\[
Ax=b,\quad\text{and}\quad(A+\delta A)(x+\delta x)=b,
\]
then
\[
\frac{\|\delta x\|}{\|x+\delta x\|}\le\kappa(A)\frac{\|\delta A\|}{\|A\|},
\]
where \(\kappa(A)\) is the condition number of \(A\).
