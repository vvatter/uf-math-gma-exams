# Numerical Linear Algebra first year exam, January 2016

*Do 4 (four) problems.*

**1.** Prove that every square matrix \(A\) has a Schur factorization.

**2.** Given a matrix \(A \in \mathbb{C}^{m \times n}\), let
\[
B=\begin{pmatrix}0&A^*\\A&0\end{pmatrix}
\quad\text{and}\quad C=A^*A.
\]
* (a) Show that the singular values of \(A\) are the absolute values of eigenvalues of \(B\).
* (b) Show that the singular values of \(A\) are the square roots of eigenvalues of \(C\).
* (c) Assume now that \(A\) is square and invertible. Compute the two-norm condition numbers of \(B\) and \(C\) in terms of the two-norm condition number of \(A\).
* (d) If \(A\) has condition number bigger than one, which has the larger condition number, \(B\) or \(C\)?

**3.** This problem has two parts.
* (a) Compute \(\det(\lambda I+uv^*)\) when \(\lambda \in \mathbb{C}\), \(I\) is the \(m \times m\) identity matrix, and \(u,v \in \mathbb{C}^m\).
* (b) Prove necessary and sufficient conditions for \(I+uv^*\) to be nonsingular and when it is, give a formula for its inverse.

**4.** This problem has two parts.
* (a) Given Cholesky decomposition of the Hermitian positive definite matrix \(A=R^*R\), prove that \(\lVert R\rVert_2=\lVert R^*\rVert_2=\lVert A\rVert_2^{1/2}\).
* (b) Now assume that \(B\) is a matrix that can be expressed as \(B=T^*T\) for some upper triangular matrix \(T\). Show that \(B\) is Hermitian and positive semi-definite, i.e. \(x^*Bx \geq 0\) for all \(x\).

**5.** Let \(\{q_1,q_2,\ldots,q_n\}\) be an orthonormal subset of \(\mathbb{C}^m\). Show that
\[
P=\sum_{i=1}^n q_iq_i^*
\]
is an orthogonal projector with range equal to the span of \(\{q_1,q_2,\ldots,q_n\}\).
