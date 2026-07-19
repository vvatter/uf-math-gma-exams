# Numerical Linear Algebra, first year exam, April 2017

*Do 4 (four) problems.*

**1.** This problem has two parts.
* (a) Given \(A \in \mathbb{C}^{m \times n}\) with \(m \geq n\), show that \(A^*A\) is nonsingular if and only if \(A\) has full rank.
* (b) If \(u,v \in \mathbb{C}^m\) and \(A=uv^*\), show that \(\lVert A\rVert_2=\lVert u\rVert_2\lVert v\rVert_2\).

**2.** Assume \(S \in \mathbb{C}^{m \times m}\) is skew-Hermitian, so \(S^*=-S\).
* (a) Show that the eigenvalues of \(S\) are pure imaginary.
* (b) Show that \(I-S\) is nonsingular.
* (c) Show that the matrix \(Q=(I-S)^{-1}(I+S)\) is unitary.

**3.** If \(A \in \mathbb{R}^{m,n}\) with \(m \geq n\), \(\operatorname{rank}(A)=n\) and \(b \in \mathbb{R}^m\).
* (a) Define the least squares solution to \(Ax=b\).
* (b) Derive the normal equations for the least squares problem.
* (c) Prove that the unique solution to the least squares problem is \((A^T A)^{-1}A^T b\).
* (d) Describe how to solve the least squares problem using the SVD decomposition of \(A\).

**4.** This problem has two parts.
* (a) Prove that every square matrix \(A\) has a Schur factorization.
* (b) If \(A\) is normal (so \(A^*A=AA^*\)) show that the triangular matrix in its Schur factorization is diagonal.

**5.** Assume \(A \in \mathbb{C}^{m \times m}\).
* (a) If \(A\) has a collection of \(m\) linearly independent eigenvectors, show that \(A\) is diagonalizable.
* (b) When \(A\) is diagonalizable, prove the Cayley–Hamilton theorem for \(A\), i.e. \(A\) satisfies its own characteristic polynomial.
