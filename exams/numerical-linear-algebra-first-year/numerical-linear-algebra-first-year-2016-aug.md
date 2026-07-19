# Numerical Linear Algebra first year exam, August 2016

*Do 4 (four) problems*

**1.** Define a normal matrix and prove that the following are equivalent.
* (a) \(A\) is normal.
* (b) \(A\) is unitarily diagonalizable.
* (c) \(\|A\|_F = \left(\sum |\lambda_i|^2\right)^{1/2}\), where \(\{\lambda_i\}\) are the eigenvalues of \(A\) counted with multiplicity.

**2.** Let \(\kappa_2(A)\) be the two-norm condition number of the square, non-singular \(A\).
* (a) Prove that
  \[
  \kappa_2(A)=\frac{\sigma_1}{\sigma_m},
  \]
  where \(\sigma_1\) and \(\sigma_m\) are the largest and smallest singular values of \(A\), respectively.
* (b) Prove or disprove: If \(A=QBQ^*\) with \(Q\) unitary, then \(\kappa_2(A)=\kappa_2(B)\).
* (c) Prove or disprove: If \(A=CBC^{-1}\), then \(\kappa_2(A)=\kappa_2(B)\).

**3.** Assume \(A\in\mathbb{R}^{m,n}\) with \(m\geq n\), \(\operatorname{rank}(A)=n\) and \(b\in\mathbb{R}^m\).
* (a) Define the least squares solution to \(Ax=b\).
* (b) Derive the normal equations for the least squares problem.
* (c) Prove that \(A^T A\) is invertible.
* (d) Prove that the unique solution to the least squares problem is \((A^T A)^{-1}A^T b\).
* (e) Describe how to solve the least squares problem using the QR decomposition of \(A\).

**4.** This problem has two parts.
* (a) Prove that \(P\) is an orthogonal projector if and only if it is Hermitian.
* (b) Let \(\{q_1,q_2,\ldots,q_n\}\) be an orthonormal subset of \(\mathbb{C}^m\). Show that
  \[
  P=\sum_{i=1}^n q_iq_i^*
  \]
  is an orthogonal projector with range equal to the span of \(\{q_1,q_2,\ldots,q_n\}\).

**5.** Assume \(A\in\mathbb{R}^{m,m}\).
* (a) Prove that \(\langle x,y\rangle_A=x^T Ay\) is an inner product on \(\mathbb{R}^m\) if and only if \(A\) is symmetric and positive definite.
* (b) Assume now that \(A\) is symmetric and positive definite. If \(x_*\) is the solution to \(Ax=b\) and \(\{p_1,\ldots,p_m\}\) is an orthonormal basis for \(\mathbb{R}^m\) with respect to \(\langle\, , \,\rangle_A\) and \(x_*=\sum c_i p_i\), give a formula for the \(c_i\).
