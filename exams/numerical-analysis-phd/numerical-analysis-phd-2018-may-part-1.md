# Numerical Analysis PhD exam, May 2018, Part 1

*Do 4 (four) problems.*

**1.** This problem has three parts.
* (a) If \(P\) is a projector, prove that \(\operatorname{null}(P)\cap\operatorname{range}(P)=\{0\}\) and \(\operatorname{null}(P)=\operatorname{range}(I-P)\).
* (b) Prove that \(P\) is an orthogonal projector if and only if it is Hermitian.
* (c) If \(q_1,\ldots,q_n\) is an orthonormal basis for the subspace \(V\subset\mathbb{C}^m\) with \(m>n\), prove that the orthogonal projector onto \(V\) is \(QQ^*\), where \(Q\) is the matrix whose columns are the \(q_j\).

**2.** Assume \(A\in\mathbb{C}^{m\times m}\).
* (a) Prove that \(\lVert A\rVert_2=(\rho(A^*A))^{1/2}=\sigma_1\), where \(\sigma_1\) is the largest singular value of \(A\) and \(\rho\) is the spectral radius.
* (b) Let \(\kappa_2(A)\) be the two-norm condition number of the square, non-singular \(A\). Prove that
  \[
  \kappa_2(A)=\frac{\sigma_1}{\sigma_m}.
  \]
  where \(\sigma_1\) and \(\sigma_m\) are the largest and smallest singular values of \(A\), respectively.
* (c) Show that \(\kappa_2(A)=1\) if and only if \(A=rQ\) with \(r\in\mathbb{R}\setminus\{0\}\) and \(Q\) unitary.

**3.** This problem has two parts.
* (a) Given \(A\in\mathbb{C}^{m\times n}\) with \(m\geq n\), show that \(A^*A\) is nonsingular if and only if \(A\) has full rank.
* (b) If \(u,v\in\mathbb{C}^m\) and \(A=uv^*\), show that \(\lVert A\rVert_2=\lVert u\rVert_2\lVert v\rVert_2\).

**4.** This problem has two parts.
* (a) Prove that every square matrix \(A\) has a Schur factorization.
* (b) If \(A\) is normal (so \(A^*A=AA^*\)) show that the triangular matrix in its Schur factorization is diagonal.

**5.** Assume \(A\in\mathbb{R}^{m,m}\).
* (a) Prove that \(\langle x,y\rangle_A=x^*Ay\) is an inner product on \(\mathbb{R}^m\) if and only if \(A\) is symmetric and positive definite.
* (b) Assume now that \(A\) is symmetric and positive definite. If \(x_*\) is the solution to \(Ax=b\) and \(\{p_1,\ldots,p_m\}\) is an orthonormal basis for \(\mathbb{R}^m\) with respect to \(\langle\, ,\,\rangle_A\) and \(x_*=\sum c_i p_i\), give a formula for the \(c_i\).
