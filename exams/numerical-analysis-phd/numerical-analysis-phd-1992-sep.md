# Numerical Analysis PhD exam, September 1992

**1.** Show that if \(A\in\mathbb{R}^{n\times n}\), then \(\lVert A\rVert_2=\sigma_1\), the largest singular value of \(A\).

**2.** Show that if \(A\in\mathbb{R}^{n\times n}\), then \(\lVert A\rVert_F=\lVert QA\rVert_F=\lVert AQ\rVert_F\), where \(Q\) is any orthogonal matrix. Show that \(\lVert A\rVert_F\) is the square root of the sum of the squares of the singular values of \(A\).

**3.** Carefully state the relation between the SVD of a matrix and its \(2\)-norm distance from matrices of lower rank.

**4.** Briefly discuss the distinction between the condition of a problem and the numerical stability of an algorithm for solving it.

**5.** This problem has two parts.
* a) Show that for invertible \(A\) and a suitably small perturbation \(E\), the exact solutions \(x\) and \(y\) of \(Ax=b\) and \((A+E)y=b\) satisfy
  \[
  \frac{\lVert y-x\rVert}{\lVert y\rVert}\leq \kappa(A)\frac{\lVert E\rVert}{\lVert A\rVert}.
  \]
* b) Recall that backward error analysis of Gaussian elimination with partial pivoting show that the computed solution \(\hat{x}\) of \(Ax=b\) is the exact solution of a nearby system \((A+E)\hat{x}=b\), where
  \[
  \lVert E\rVert_\infty\approx 8n^3\rho\lVert A\rVert_\infty\mu,
  \]
  where \(\mu\) is the unit roundoff and \(\rho\) is the growth factor. Show how to combine the perturbation theory results from part a) with these roundoff error results to obtain results on the accuracy of the computed solution of a linear system via Gaussian elimination with partial pivoting.

**6.** Create a Matlab function chol.m which will overwrite the upper triangle of an invertible upper triangular matrix with its inverse using no scratch arrays. Derive an analytic estimate of the number of flops required.

**7.** Give a careful statement and proof of Gershgorin’s Theorem. Find upper and lower bounds for the set of eigenvalues for the \(4\times 4\) Hilbert matrix \(a_{ij}=1/(i+j-1)\).

**8.** Discuss the relative merits of using a Newton–Cotes method and Gaussian quadrature for numerical integration.

**9.** Give a careful statement of the Contraction Mapping Theorem. If a matrix \(A\) is diagonally dominant, show how the Contraction Mapping Theorem can be used to justify the convergence of Jacobi’s method for solving \(Ax=b\).

**10.** For a given partition \(\{x_0,x_1,\ldots,x_n\}\) of an interval \([a,b]\),
* a) Define the Lagrange basis functions \(l_i(x)\).
* b) Derive Lagrange’s formula for the interpolating polynomial of the data \(\{y_0,y_1,\ldots,y_n\}\).
* c) Show that if \(\Psi(x):=(x-x_0)(x-x_1)\cdots(x-x_n)\), then
  \[
  l_i(x)=\frac{\Psi(x)}{(x-x_i)\Psi'(x_i)}.
  \]

**11.** Determine the cubic spline \(s(x)\) on the grid \(\{-1,0,1\}\) with \(s(-1)=s(0)=0\), \(s(1)=4\), and \(s''(-1)=s''(1)=0\).

**12.** Suppose that \(f:\mathbb{R}\longrightarrow\mathbb{R}\) is of class \(C^2\) with \(f(\alpha)=0\) and \(f'(\alpha)\neq 0\). Set \(g(x):=x-\frac{f(x)}{f'(x)}\) so that \(g(\alpha)=\alpha\).
* a) Show that on some neighborhood \([\alpha-\delta,\alpha+\delta]\) of \(\alpha\), \(g\) is a contraction.
* b) Show that for any \(x_0\in[\alpha-\delta,\alpha+\delta]\), \(\lim_{n\to\infty}x_n=\alpha\), where \(x_{n+1}:=g(x_n)\).
* c) Conclude that for any \(x_0\in[\alpha-\delta,\alpha+\delta]\), Newton’s method converges to \(\alpha\).
* d) Show that the convergence in b)—and hence in c)—is quadratic.

**13.** For a given partition \(\{x_0,x_1,\ldots,x_n\}\) of an interval \([a,b]\) and function \(f\) defined on \([a,b]\),
* a) State the divided difference formula for the polynomial \(p_n(x)\) interpolating \(f\).
* b) Show that the error in the approximation in part a) is given by
  \[
  f(x)-p_n(x)=(x-x_0)(x-x_1)\cdots(x-x_n)f[x_0,x_1,\ldots,x_n,x].
  \]
* c) For \(\{x_0,x_1,x_2\}=\{0,1,2\}\) and \(f(x)=\frac{1}{1+x^2}\), compute the divided difference formula for \(p_2(x)\).
