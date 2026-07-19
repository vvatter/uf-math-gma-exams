# Numerical Analysis, PhD exam, August 2019, Part 1

*Do 4 (four) problems.*

**1.** Let \(A \in \mathbb{C}^{m\times n}\).
* (a) Prove or give a counterexample: \(\|A\|_2 \leq \sqrt{\|A\|_\infty\|A\|_1}\). If you prove this, make sure to justify each nontrivial step.
* (b) Prove or give a counterexample: \(\|A\|_2 \leq \|A\|_F\), where \(\|A\|_F\) is the Frobenius norm of \(A\). If you prove this, make sure to justify each nontrivial step.

**2.** This problem has two parts.
* (a) Prove that the inverse of an upper-triangular matrix is upper-triangular.
* (b) Let \(A \in \mathbb{C}^{m\times n}\) with \(m>n\). Consider the least-squares problem of finding \(x \in \mathbb{C}^n\) that minimizes \(\|Ax-b\|\) in the 2-norm. Describe a method for solving the problem efficiently, and explain (and justify) why the normal equations should not be solved.

**3.** Let \(A \in \mathbb{C}^{m\times n}\), with \(m\geq n\) and \(\operatorname{rank}(A)=p=n\geq 3\). Let \(a_1,a_2,\ldots\) denote the columns of \(A\).
* (a) Using the classical Gram–Schmidt process, write out expressions for \(q_1,q_2,q_3\), the first three columns of \(Q\) in the \(QR\) decomposition of \(A\).
* (b) Show the vector \(q_3\) found in part (a) is orthogonal to both \(q_1\) and \(q_2\).
* (c) Write an expression for the first Householder reflector \(H_1\), used to find the \(QR\) decomposition of \(A\). Show \(H_1\) is both unitary and Hermitian.

**4.** Let \(A \in \mathbb{C}^{m\times m}\) be Hermitian.
* (a) Show that all eigenvalues of \(A\) are real.
* (b) Define the stationary iterative method (a.k.a. fixed point method)
  \[
  x^{(k+1)}=Ax^{(k)}+b. \tag{1}
  \]
  Suppose (1) has fixed-point \(x\), namely \(x\) satisfies \(x=Ax+b\). Show the iteration (1) converges to \(x\) from any starting guess \(x^{(0)}\), that is \(x^{(k)}\to x\) as \(k\to\infty\), if and only if the eigenvalues \(\lambda_i\) of \(A\) satisfy \(|\lambda_i|<1\), \(i=1,\ldots,m\). You may use the fact that Hermitian matrix \(A\) is unitarily diagonalizable.

**5.** Consider the matrix \(A\) given by
\[
\begin{pmatrix}
1 & -1 & 2 & 0\\
-1 & 4 & -1 & 1\\
2 & -1 & 6 & -2\\
0 & 1 & -2 & 4
\end{pmatrix}.
\]
Suppose the eigenvalues of \(A\) are all distinct (they are) and satisfy \(\lambda_1>\lambda_2>\lambda_3>\lambda_4\).
* (a) Show that \(A\) is positive definite.
* (b) Describe an algorithm that could be used to approximate \(\lambda_4\).
* (c) Describe algorithms that could be used to approximate \(\lambda_2,\lambda_3\), and their eigenvectors.
