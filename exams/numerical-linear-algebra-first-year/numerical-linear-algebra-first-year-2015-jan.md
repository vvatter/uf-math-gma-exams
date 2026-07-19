# Numerical Linear Algebra first year exam, January 2015

*Do 4 (four) problems.*

**1.** Assume \(A \in \mathbb{R}^{m,n}\) with \(m \geq n\), \(\operatorname{rank}(A)=n\) and \(b \in \mathbb{R}^m\).
* (a) Define the least squares solution to \(Ax=b\).
* (b) Derive the normal equations for the least squares problem.
* (c) Prove that \(A^T A\) is invertible.
* (d) Prove that the unique solution to the least squares problem is \((A^T A)^{-1}A^T b\).
* (e) Describe how to solve the least squares problem using the QR decomposition of \(A\).

**2.** This problem has two parts.
* (a) Compute \(\det(\lambda I+uv^*)\) when \(\lambda \in \mathbb{C}\), \(I\) is the \(m \times m\) identity matrix, and \(u,v \in \mathbb{C}^m\).
* (b) Prove necessary and sufficient conditions for \(I+uv^*\) to be nonsingular and when it is, give a formula for its inverse.

**3.** This problem has three parts.
* (a) If \(P\) is a projector, prove that \(\operatorname{null}(P) \cap \operatorname{range}(P)=\{0\}\) and \(\operatorname{null}(P)=\operatorname{range}(I-P)\).
* (b) Prove that \(P\) is an orthogonal projector if and only if it is Hermitian.
* (c) If \(q_1,\ldots,q_n\) is an orthonormal basis for the subspace \(V \subset \mathbb{C}^m\) with \(m>n\), prove that the orthogonal projector onto \(V\) is \(QQ^*\), where \(Q\) is the matrix whose columns are the \(q_j\).

**4.** This problem has three parts.
* (a) Prove that \(\lVert A\rVert_F=\operatorname{trace}(A^*A)^{1/2}\).
* (b) Prove that \(\lVert A\rVert_F=(\sum \sigma_i^2)^{1/2}\), where \(\{\sigma_i\}\) are the singular values of \(A\) counted with multiplicity.
* (c) If both \(A\) and \(U\) are in \(\mathbb{C}^{m,m}\) and \(U\) is unitary, prove that \(\lVert UA\rVert_F=\lVert AU\rVert_F=\lVert A\rVert_F\).

**5.** Define a normal matrix and prove that the following are equivalent.
* (a) \(A\) is normal.
* (b) \(A\) is unitarily diagonalizable.
* (c) \(\lVert A\rVert_F=(\sum |\lambda_i|^2)^{1/2}\), where \(\{\lambda_i\}\) are the eigenvalues of \(A\) counted with multiplicity.
