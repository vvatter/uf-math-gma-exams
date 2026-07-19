# Numerical Linear Algebra, first year exam, January 2018

*Do 4 (four) problems.*

**1.** Assume \(A \in \mathbb{R}^{m,n}\) with \(m \geq n\), \(\operatorname{rank}(A)=n\), and \(b \in \mathbb{R}^m\).
* (a) Define the least squares solution to \(Ax=b\).
* (b) Derive the normal equations for the least squares problem.
* (c) Prove that \(A^T A\) is invertible.
* (d) Prove that the unique solution to the least squares problem is \((A^T A)^{-1}A^T b\).
* (e) Describe how to solve the least squares problem using the QR decomposition of \(A\).

**2.** Define a normal matrix and prove that the following are equivalent.
* (a) \(A\) is normal.
* (b) \(\lVert Ax\rVert_2=\lVert A^*x\rVert_2\) for every \(x\).
* (c) \(A\) is unitarily diagonalizable.

**3.** Assume \(A \in \mathbb{R}^{m,m}\).
* (a) Prove that \(\langle x,y\rangle_A=x^*Ay\) is an inner product on \(\mathbb{R}^m\) if and only if \(A\) is symmetric and positive definite.
* (b) Assume now that \(A\) is symmetric and positive definite. If \(x_*\) is the solution to \(Ax=b\) and \(\{p_1,\ldots,p_m\}\) is an orthonormal basis for \(\mathbb{R}^m\) with respect to \(\langle\ ,\ \rangle_A\) and \(x_*=\sum c_i p_i\), give a formula for the \(c_i\).

**4.** If \(q_1,\ldots,q_n\) is an orthonormal basis for the subspace \(V \subset \mathbb{C}^m\) with \(m>n\), prove that the orthogonal projector onto \(V\) is \(QQ^*\), where \(Q\) is the matrix whose columns are the \(q_j\).

**5.** Assume \(A \in \mathbb{C}^{m,m}\).
* (a) Show that \(A\) has a Schur decomposition.
* (b) If \(A\) has a collection of \(m\) linearly independent eigenvectors, show that \(A\) is diagonalizable.
