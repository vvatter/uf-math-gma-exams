# Numerical Analysis PhD exam, January 2002

*Do any 8 of the following 10 problems. Problems 1–5 are Part 1: Numerical Linear Algebra. Problems 6–10 are Part II: Numerical Analysis.*

**1.** This problem has three parts.
* (a) Prove: If \(A\in\mathbb R^{n\times n}\) has a set of \(n\) linearly independent eigenvectors, then \(A\) can be diagonalized.
* (b) Prove: If \(A\in\mathbb R^{n\times n}\) is symmetric, then \(A\) has an orthogonal set of eigenvectors.
* (c) Diagonalize the matrix
  \[
  A=\begin{pmatrix}66&12\\12&59\end{pmatrix}.
  \]

**2.** This problem has three parts.
* (a) Is the matrix
  \[
  A=\begin{pmatrix}5&1\\0&3\end{pmatrix}
  \]
  diagonalizable? Why?
* (b) Can the above matrix \(A\) be diagonalized by an orthogonal matrix \(S\)?
* (c) State a theorem or condition that ensures a matrix can be diagonalized by an orthogonal matrix.

**3.** This problem has three parts.
* (a) Give a careful statement of the singular value decomposition.
* (b) Give a careful proof of the singular value decomposition.
* (c) Compute the SVD for the matrix
  \[
  A=\begin{pmatrix}-6&17\\18&-1\end{pmatrix}.
  \]

**4.** Let
\[
A=\begin{pmatrix}1&2\\0&1\\1&0\end{pmatrix}.
\]
* (a) Determine the orthogonal projection of \(A\) onto the column space of \(A\).
* (b) Compute the \(QR\) factorization of \(A\).

**5.** This problem has five parts.
* (a) Define the operator 2-norm for any matrix \(A\) in \(\mathbb R^{m\times n}\).
* (b) Prove: If \(A\in\mathbb R^{m\times n}\) and \(B\in\mathbb R^{n\times q}\), then \(\lVert BA\rVert_2\leq\lVert B\rVert_2\cdot\lVert A\rVert_2\).
* (c) Prove: If \(A\) is any matrix in \(\mathbb R^{n\times n}\) and \(\lVert A\rVert_2<1\), then \(\lim_{n\to\infty}A^n=0\).
* (d) Prove: If \(A\) is a matrix in \(\mathbb R^{n\times n}\), then define \(e^A\) as a power series expansion. Show this series converges.
* (e) Prove: If \(A\in\mathbb R^{n\times n}\) is invertible, \(b\) and \(\Delta b\) are vectors in \(\mathbb R^n\), \(x\) and \(\Delta x\) are vectors in \(\mathbb R^n\) and are solutions to \(Ax=b\) and \(A\Delta x=\Delta b\), respectively, then
  \[
  \frac{\lVert\Delta x\rVert_2}{\lVert x\rVert_2}\leq\kappa_2(A)\frac{\lVert\Delta b\rVert_2}{\lVert b\rVert_2}.
  \]

**6.** This problem has three parts.
* (a) State Newton’s method (the algorithm) for solving \(f(x)=0\) where \(f:\mathbb R\to\mathbb R\).
* (b) Assuming \(f\) is smooth and we have an initial guess sufficiently close to the root, state sufficient condition(s) for the method to converge quadratically.
* (c) Prove: Let \(T(x):[a,b]\to[a,b]\) be a function such that \(T'''(x)\) is continuous for all \(x\in[a,b]\), \(T(p)=p\), \(T'(p)=T''(p)=0\). If \(x_0\in[a,b]\) is a point with the property that the sequence defined recursively by \(x_{k+1}=T(x_k)\) converges to \(p\), then the sequence \(\{x_k\}_{k=1}^{\infty}\) converges cubically to \(p\).

**7.** This problem has four parts.
* (a) Give a careful statement of the minimization property for clamped cubic splines.
* (b) Give a careful statement of the convergence theorem for clamped cubic splines.
* (c) Give a careful statement of the convergence theorem for the second derivatives for clamped cubic splines.
* (d) Outline a proof of the convergence theorem for clamped cubic splines.

**8.** This problem has two parts.
* (a) Given a set of data points \((x_0,y_0),(x_1,y_1),\ldots,(x_n,y_n)\) in the plane, describe how to find the conic section of the form \(Ax^2+Bxy+Cy^2+Dx+Ey+1=0\) which best fits the data in the sense of least squares.
* (b) How do you determine whether or not the conic section is an ellipse, a hyperbola, or a parabola?

**9.** Triple Recursion Formula. If \(\{\phi_n(x)\}\) is an orthogonal family of polynomials on \([a,b]\), with respect to the weight function \(w(x)\geq0\), and \(n\geq1\), then show that \(\phi_{n+1}(x)=(a_nx+b_n)\phi_n(x)-c_n\phi_{n-1}(x)\), for some constants \(a_n,b_n,\) and \(c_n\). (Hint: Let \(g(x)=\phi_{n+1}(x)-a_nx\phi_n(x)\), where \(a_n\) is a constant chosen so that \(g(x)\) has degree \(n\).)

**10.** This problem has four parts.
* (a) Give a careful statement of the contraction mapping theorem.
* (b) Prove the contraction mapping theorem.
* (c) Determine whether or not the function \(T(x)=\frac14\sin(3x+2)+12\) is a contraction.
* (d) Discuss the convergence rate ensured by the contraction mapping theorem. (ie Is it linear, quadratic, or cubic?)
