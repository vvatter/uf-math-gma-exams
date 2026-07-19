# Numerical Linear Algebra first year exam, January 2019

*Do 4 (four) problems.*

**1.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\) with \(\operatorname{rank}(A)=p\) and \(p\leq n\leq m\).
* (a) Show \(\operatorname{Col}(A)=\operatorname{Span}\{u_1,u_2,\ldots,u_p\}\), where \(u_1,\ldots,u_p\) are the first \(p\) columns of \(U\).
* (b) Show \(\operatorname{Null}(A^*)=\operatorname{Span}\{u_{p+1},u_{p+2},\ldots,u_m\}\).
* (c) Show that \(A^*A\) is invertible if and only if \(A\) is full rank.

**2.** Let matrix \(A\in\mathbb{C}^{m\times n}\), with \(n<m\). Let vector \(b\in\mathbb{C}^m\), and let \(r\) denote the residual vector \(r=b-Ax\).
* (a) Show that \(x\) solves the least-squares problem \(\min \lVert b-Ax\rVert_2\) if and only if \(r\in\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank, and describe how to find the least-squares solution using the QR decomposition of \(A\).

**3.** This problem has three parts.
* (a) Show that if \(A\in\mathbb{C}^{m\times m}\), \(A\) has a Schur decomposition.
* (b) Show that if \(T\in\mathbb{C}^{m\times m}\) is normal and triangular, then \(T\) is diagonal.
* (c) Show that if \(A\in\mathbb{C}^{m\times m}\) is normal and \(\lambda\) is an eigenvalue of \(A\), then the geometric multiplicity of \(\lambda\) is equal to the algebraic multiplicity of \(\lambda\).

**4.** Let \(\lVert\cdot\rVert\) be a subordinate (induced) matrix norm. If \(A\) is \(n\times n\) invertible and \(E\) is \(n\times n\) with \(\lVert A^{-1}\rVert\lVert E\rVert<1\), then show
* (a) \(A+E\) is nonsingular.
* (b) \[\lVert(A+E)^{-1}\rVert\leq \frac{\lVert A^{-1}\rVert}{1-\lVert A^{-1}\rVert\lVert E\rVert}.\]

**5.** Consider the matrix \(A\) given by
\[A=\begin{pmatrix}1&1&2&-3\\1&10&-1&1\\2&-1&13&-2\\-3&1&-2&25\end{pmatrix}.\]
* (a) Show that \(A\) is positive definite.
* (b) What can you say about the location of each of the eigenvalues of \(A\)? Your answer should be in the form of an interval or a union of intervals.
* (c) Suppose the eigenvalues of \(A\) are all distinct (they are) and satisfy \(\lambda_1>\lambda_2>\lambda_3>\lambda_4\). Describe an algorithm that could be assured to converge to \(\lambda_4\).
