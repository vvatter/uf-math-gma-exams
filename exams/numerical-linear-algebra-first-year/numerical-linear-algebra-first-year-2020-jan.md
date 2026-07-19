# Numerical Linear Algebra, first year exam, January 2020

*Do 4 (four) problems.*

**1.** Let \(A \in \mathbb{C}^{m \times n}\).
* (a) Determine constants \(\alpha\) and \(\beta\) such that the following inequality holds for the \(p\) and \(\infty\) norms of matrix \(A\), for integers \(p \ge 1\). Justify your answer.
  \[
  \alpha \lVert A \rVert_\infty \le \lVert A \rVert_p \le \beta \lVert A \rVert_\infty.
  \]
* (b) Prove or give a counterexample: \(\lVert A \rVert_2 \le \lVert A \rVert_F\), where \(\lVert A \rVert_F\) is the Frobenius norm of \(A\). If you prove this, make sure to justify each nontrivial step.

**2.** Suppose \(A\) is Hermitian positive definite.
* (a) Prove that each principal submatrix of \(A\) is Hermitian positive definite.
* (b) Prove that an element of \(A\) with largest magnitude lies on the diagonal.
* (c) Prove that \(A\) has a Cholesky decomposition.

**3.** Define the matrices \(A\) and \(B\) by
\[
A = \begin{pmatrix}
1 & 2 & 0 \\
1 & 2 & 0 \\
1 & 2 & 0 \\
1 & 2 & 0
\end{pmatrix},
\qquad
B = \begin{pmatrix}
1 & 0 & 1 \\
0 & 2 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{pmatrix}.
\]
* (a) Find both full and economy singular value decompositions of \(A\).
* (b) Find both full and economy QR decompositions of \(B\).

**4.** Let \(\lVert \cdot \rVert\) be a subordinate (induced) matrix norm.
* (a) If \(E\) is \(n \times n\) with \(\lVert E \rVert < 1\), then show \(I+E\) is nonsingular and
  \[
  \lVert (I+E)^{-1} \rVert \le \frac{1}{1-\lVert E \rVert}.
  \]
* (b) If \(A\) is \(n \times n\) invertible and \(E\) is \(n \times n\) with \(\lVert A^{-1} \rVert \lVert E \rVert < 1\), then show \(A+E\) is nonsingular and
  \[
  \lVert (A+E)^{-1} \rVert \le \frac{\lVert A^{-1} \rVert}{1-\lVert A^{-1} \rVert \lVert E \rVert}.
  \]

**5.** Suppose the linear equation \(Ax=b\), with
\[
A = \begin{pmatrix}
\delta & 1 \\
1 & 1
\end{pmatrix},
\qquad |\delta| < \epsilon_m/4,
\]
is solved on a floating-point system with machine-epsilon \(\epsilon_m\), using an LU factorization (no pivoting!) followed by forward and back substitution. (You may assume the operations \((+, -, \div, \times)\), do not incur any additional errors).
* (a) If \(b=(1,0)^T\), compute the backward error, \(\lVert \hat{b}-b \rVert_2/\lVert b \rVert_2\), where \(\hat{b}\) is the data that satisfies \(A\hat{x}=\hat{b}\), and \(\hat{x}\) is the computed solution.
* (b) Is the result of (a) sufficient to draw any conclusions about the backward-stability of the algorithm used to compute \(\hat{x}\)? Explain.
