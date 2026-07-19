# Numerical Analysis PhD exam, May 2020

*Do 4 (four) of the first 5 (1-5) and 4 (four) of the last 5 problems (6-10).*

**1.** This problem has two parts.
* (a) Let \(A \in \mathbb{C}^{m \times n}\). Prove or give a counterexample: Every matrix norm that is induced by a vector norm satisfies the submultiplicative property \(\|AB\| \leq \|A\|\|B\|\). If you prove this, make sure to justify each nontrivial step.
* (b) Let \(A \in \mathbb{C}^{m \times m}\). Prove that \(\|A\|_2 = (\rho(A^*A))^{1/2}\), where \(\rho(A)\) is the spectral radius of \(A\).

**2.** Suppose \(A\) is Hermitian positive definite.
* (a) Prove that each principal submatrix of \(A\) is Hermitian positive definite.
* (b) Prove that an element of \(A\) with largest magnitude lies on the diagonal.
* (c) Prove that \(A\) has a Cholesky decomposition.

**3.** Let \(A \in \mathbb{C}^{m \times m}\) be Hermitian.
* (a) Show that all eigenvalues of \(A\) are real.
* (b) Define the stationary iterative method (a.k.a. fixed point method)
  \[
  x^{(k+1)}=Ax^{(k)}+b. \tag{1}
  \]
  Suppose (1) has fixed-point \(x\), namely \(x\) satisfies \(x=Ax+b\). Show the iteration (1) converges to \(x\) from any starting guess \(x^{(0)}\), that is \(x^{(k)} \to x\) as \(k \to \infty\), if and only if the eigenvalues \(\lambda_i\) of \(A\) satisfy \(|\lambda_i|<1\), \(i=1,\ldots,m\). You may use the fact that Hermitian matrix \(A\) is unitarily diagonalizable.

**4.** Suppose the \(5 \times 5\) symmetric matrix \(A\) has eigenvalues known to within the given tolerances.
\[
\begin{aligned}
3.5 &> \lambda_1 > 2.5\\
2.0 &> \lambda_2 > 1.0\\
1.0 &> \lambda_3 > -1.0\\
-1.0 &> \lambda_4 > -2.0\\
-2.5 &> \lambda_5 > -3.5.
\end{aligned}
\]
* (a) Describe how shifting can be used so that the power method can be used to compute \(\lambda_1\) with guaranteed convergence. Clearly explain your choice of shift.
* (b) Provide an upper bound for the convergence rate using the shift you chose in (a) for \(\lambda_1\). Is there another shift that would decrease this worst-case convergence rate?

**5.** For \(x,y>0\), consider computing \(f(x,y)=\sqrt{y+x^2}-\sqrt{y}\) in floating-point arithmetic with machine precision \(\epsilon_m\).
* (a) Explain the difficulties in computing \(f(x,y)\), if \(x \ll y\). What are the absolute and relative errors if \(x^2/y<\epsilon_m\), if \(f(x,y)\) is computed directly from the form given above?
* (b) Suppose \(x^2/y<\epsilon_m\). Describe a way to compute \(f(x,y)\) with more accuracy in this situation.

**6.** Let \(\alpha>0\). For (i) \(p=2\); (ii) \(p=\infty\), find the constant \(c_p\) that minimizes
\[
E_p(c)=\|t^\alpha-c\|_p=\left(\int_0^1 |t^\alpha-c|^p\,dt\right)^{1/p},
\]
and find \(E_p(c_p)\), for each of those values of \(p\).

**7.** Let \(\{\phi_k\}_{k=0}^{m+1}\) be the set of monic orthogonal polynomials with respect to inner product \((u,v)=\int_a^b u(x)v(x)w(x)\,dx\). Let \(\phi_{-1}=0\) and \(\phi_0=1\).
* (a) Find expressions for constants \(\alpha_k\) and \(\beta_k\) to determine a 3-term recurrence relation of the form
  \[
  \phi_{k+1}(x)=(x-\alpha_k)\phi_k-\beta_k\phi_{k-1}(x),\quad k=0,\ldots,m.
  \]
* (b) Use the above relation to determine \(\phi_1,\phi_2\) and \(\phi_3\), using the inner-product \((u,v)=\int_0^1 u(x)v(x)\,dx\).

**8.** Consider finding a zero of function \(f:D\subseteq\mathbb{R}^n\to\mathbb{R}^n\) that can be written as the sum of a linear and nonlinear part
\[
f(x)=Bx+G(x),
\]
where \(B\) is a nonsingular matrix and \(G:D\subseteq\mathbb{R}^n\to\mathbb{R}^n\) is some nonlinear function. At a point \(x_k\) consider an affine model \(M_k(x)=a_k+A_k(x-x_k)\), where the quantities \(a_k\in\mathbb{R}^n\) and \(A_k\in\mathbb{R}^{n\times n}\) are to be determined.
* (a) Determine \(a_k\) and \(A_k\) so that the following conditions hold:
  \[
  M_k(x_k)=f(x_k)\quad\text{and}\quad M_k'(x_k)=B.
  \]
* (b) Derive the iteration obtained by defining \(x_{k+1}\) as the zero of \(M_k(x)\).

**9.** Let \(f\in C^\infty(a,b)\). Let \(x_0<x_1<x_2\) be three points in \([a,b]\) that are not necessarily equally spaced.
* (a) Based on the quadratic interpolant \(p_2\) which satisfies \(p_2(x_0)=f(x_0)\), \(p_2(x_1)=f(x_1)\) and \(p_2(x_2)=f(x_2)\), find the centered finite difference approximations to \(f'(x_1)\) and \(f''(x_1)\) (you should explicitly show how the difference approximations are derived from the interpolant).
* (b) Derive an expression for the error, \(f'(x_1)-p_2'(x_1)\).

**10.** This problem has two parts.
* (a) For \(f\in C^\infty(a,b)\), the composite trapezoidal quadrature rule with \(n\) subintervals with length \(h=(b-a)/n\) satisfies
  \[
  \left|\int_a^b f(x)\,dx-I_{T,n}\right|=a_2h^2+a_4h^4+a_6h^6+\cdots,
  \]
  where the coefficients \(a_2,a_4,\ldots\), do not depend on \(n\). Find and inductively prove an expression for the \(k\)th Richardson extrapolant \(I_k\) of \(I_0:=I_{T,n}\).
* (b) Consider a quadrature formula of the type
  \[
  \int_0^1 f(x)\,dx\approx \alpha f(x_1)+\beta[f(1)-f(0)].
  \]
  Determine \(\alpha,\beta\) and \(x_1\) such that the degree of exactness is as large as possible. What is the maximum degree of exactness?
