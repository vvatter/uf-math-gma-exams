# Numerical Linear Algebra first year exam, August 2017

*Do 4 (four) problems.*

**1.** Assume that \(A\) is Hermitian and all its eigenvalues are distinct and nonzero.
* (a) Show that each pair of distinct eigenvectors of \(A\) are orthogonal.
* (b) If \(\lambda\) is an eigenvalue of \(A\) with eigenvector \(x\) with \(\lVert x\rVert_2=1\), then \(B=A-\lambda xx^*\) has the same eigenvectors as \(A\) while \(B\)'s eigenvalues are the same as those of \(A\) except \(\lambda\) is replaced with zero.

**2.** This problem has two parts.
* (a) If \(P\) is a projector, prove that \(\operatorname{null}(P)\cap\operatorname{range}(P)=\{0\}\) and \(\operatorname{null}(P)=\operatorname{range}(I-P)\).
* (b) Prove that \(P\) is an orthogonal projector if and only if it is Hermitian.

**3.** This problem has three parts.
* (a) If both \(A\) and \(U\) are in \(\mathbb{C}^{m,m}\) and \(U\) is unitary, prove that \(\lVert UA\rVert_F=\lVert AU\rVert_F=\lVert A\rVert_F\).
* (b) If both \(A\) and \(U\) are in \(\mathbb{C}^{m,m}\) and \(U\) is unitary, prove that \(\lVert UA\rVert_2=\lVert AU\rVert_2=\lVert A\rVert_2\).
* (c) Prove that \(\lVert A\rVert_2=(\rho(A^*A))^{1/2}=\sigma_1\), where \(\sigma_1\) is the largest singular value of \(A\).

**4.** This problem has two parts.
* (a) If \(A\in\mathbb{C}^{m,n}\) with \(m\geq n\), prove that \(A^*A\) is invertible if and only if \(\operatorname{rank}(A)=n\).
* (b) Give an explicit formula for \(\det(\lambda I-ww^*)\) when \(\lambda\in\mathbb{C}\), \(I\) is the \(m\times m\) identity matrix and \(w\in\mathbb{C}^m\).

**5.** Assume that \(T\) is tridiagonal and symmetric with the diagonal entries given by \(a_j\) for \(j=1,\ldots,m\) and the super- and sub-diagonal entries by \(b_j\) for \(j=1,\ldots,m-1\). Let \(p_k\) be the characteristic polynomial of the \(k\times k\) matrix in the upper left hand corner of \(T\). Prove that
\[
p_k(x)=(a_k-x)p_{k-1}(x)-b_{k-1}^2p_{k-2}(x).
\]
