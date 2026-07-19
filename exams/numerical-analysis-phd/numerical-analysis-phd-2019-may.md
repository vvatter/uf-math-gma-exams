# Numerical Analysis, PhD exam, May 2019

## Numerical Linear Algebra

*Do 4 (four) problems.*

**1.** This problem has three parts.
* (a) Show the matrix norm equality for \(A\in\mathbb{C}^{m\times n}\)
  \[
  \lVert A\rVert_\infty=\max_{1\le i\le m}\sum_{j=1}^n |a_{ij}|.
  \]
* (b) Explain why the matrix 1-norm, 2-norm and \(\infty\)-norm are the most commonly used of the matrix \(p\)-norms in scientific computing.
* (c) Show \(\rho(A)\le \lVert A\rVert\), where \(\lVert A\rVert\) is any subordinate (induced) matrix norm and \(\rho(A)\) is the spectral radius of \(A\).

**2.** Let \(A\in\mathbb{C}^{m\times n}\) with \(\operatorname{rank}(A)=n<m\). Let \(A=QR\) be the \(QR\) decomposition of \(A\), and \(A=Q_1R_1\) be the economy \(QR\) decomposition.
* (a) Show \(Q_1Q_1^*\) is an orthogonal projector onto \(\operatorname{Col}(A)\).
* (b) Let \(b\in\mathbb{C}^m\). Write down an expression for the least-squares solution to \(Ax=b\) as the solution to an \(n\times n\) system in terms of \(Q_1\), (and/or \(Q_1^*\)), \(R_1\), \(x\) and \(b\).

**3.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\) with \(\operatorname{rank}(A)=p\) and \(p\le n\le m\).
* (a) Show \(\operatorname{Col}(A^*)=\operatorname{Span}\{v_1,v_2,\ldots,v_p\}\), where \(v_1,\ldots,v_p\) are the first \(p\) columns of \(V\).
* (b) Show \(\operatorname{Null}(A)=\operatorname{Span}\{v_{p+1},v_{p+2},\ldots,v_n\}\).
* (c) Suppose the right singular vectors \(v_1,\ldots,v_p\) have been computed. Describe how to compute the left singular vectors \(u_1,\ldots,u_p\) (without solving a spectral problem).

**4.** Let \(\lVert\cdot\rVert\) be a subordinate (induced) matrix norm. If \(A\) is \(n\times n\) invertible and \(E\) is \(n\times n\) with \(\lVert A^{-1}\rVert\lVert E\rVert<1\), then show
* (a) \(A+E\) is nonsingular.
* (b)
  \[
  \lVert(A+E)^{-1}\rVert\le \frac{\lVert A^{-1}\rVert}{1-\lVert A^{-1}\rVert\lVert E\rVert}.
  \]

**5.** Consider the matrix \(A\) given by
\[
A=\begin{pmatrix}
1&-1&2&0\\
-1&4&-1&1\\
2&-1&6&-2\\
0&1&-2&4
\end{pmatrix}.
\]
Suppose the eigenvalues of \(A\) are all distinct (they are) and satisfy \(\lambda_1>\lambda_2>\lambda_3>\lambda_4\).
* (a) Show that \(A\) is positive definite.
* (b) Describe an algorithm that could be used to converge to \(\lambda_4\).
* (c) Describe an algorithm that could be used to converge to \(\lambda_2\).

## Numerical Analysis

*Do 4 (four) problems.*

**1.** Consider the fixed point problem \(x=f(x)\), where \(f(x)=e^{-(2+x)}\).
* (a) Find the largest open interval in \(\mathbb{R}\) where \(f(x)\) is a contraction.
* (b) Assuming all computations are done in exact arithmetic, find the largest open interval in \(\mathbb{R}\) where the fixed-point iteration \(x_{k+1}=f(x_k)\) is assured to converge.
* (c) Write a Newton iteration for finding the fixed-point.

**2.** Let \(x_1,x_2,\ldots,x_{n+1}\) be \(n+1\) distinct numbers. Let \(l_j(x)\) be the associated Lagrange basis polynomials, \(j=1,\ldots,n+1\).
* (a) State the definition of \(l_j(x)\) and show that \(\{l_j(x)\}_{j=1}^{n+1}\) form a basis for \(P_n\), the space of polynomials of degree at most \(n\).
* (b) Show that
  \[
  \sum_{j=1}^{n+1}(x-x_j)^k l_j(x)=0,\qquad \text{for all }k=1,\ldots,n.
  \]

**3.** Consider the interval \([a,b]\) with the partition \(a=x_1<x_2<\cdots<x_n<x_{n+1}=b\). Suppose \(s(x)\) is the natural cubic spline that interpolates the data \(\{(x_i,y_i)\}_{i=1}^{n+1}\), and that \(g\in C^2[a,b]\) interpolates the same data. Show that
\[
\int_a^b \bigl(s''(x)\bigr)^2\,dx\le \int_a^b \bigl(g''(x)\bigr)^2\,dx.
\]

**4.** This problem has two parts.
* (a) Consider the inner product on \(C(0,2)\) given by \((f,g)=\int_0^2 f(t)g(t)\,dt\). Find three orthonormal polynomials \(\phi_0,\phi_1,\phi_2\) on \((0,2)\) with respect to the given inner product such that the degree of \(\phi_n\) is equal to \(n\), \(n=0,1,2\).
* (b) Find the nodes \(t_1\) and \(t_2\) and weights \(w_1\) and \(w_2\) which yield the weighted Gaussian Quadrature formula
  \[
  \int_0^2 f(t)\,dt\approx w_1f(t_1)+w_2f(t_2)
  \]
  with degree of exactness \(m=3\). You should find the nodes exactly, and may leave the weights \(w_1,w_2\) in integral form.

**5.** Let \(f\in C^\infty(a-H,a+H)\), and let \(h<H\). Let \(x_0=a-h\), \(x_1=a\) and \(x_2=a+h\).
* (a) Find the finite difference approximation to \(f'(a)\) based on the interpolant \(p_2\) which satisfies \(p_2(x_0)=f(x_0)\), \(p_2(x_1)=f(x_1)\) and \(p_2(x_2)=f(x_2)\).
* (b) Let \(\psi_0(h)=\psi(h)\) be the difference approximation to \(f'(a)\) found in part (a). Assume (in exact arithmetic) \(\psi(h)\to\psi(0)=f'(a)\) as \(h\to0\), and that \(\psi(h)\) has the asymptotic expansion
  \[
  \psi(h)=\psi(0)+a_2h^2+a_4h^4+a_6h^6+\cdots.
  \]
  Find the general Richardson extrapolation formula for \(\psi_k(h)\) based on \(\psi_{k-1}(h)\) and \(\psi_{k-1}(h/2)\).
