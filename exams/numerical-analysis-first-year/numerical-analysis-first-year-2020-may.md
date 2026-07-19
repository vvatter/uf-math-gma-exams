# Numerical Analysis first year exam, May 2020

*Do 4 (four) problems.*

**1.** Let \(\alpha>0\). For (i) \(p=2\); (ii) \(p=\infty\), find the constant \(c_p\) that minimizes
\[
E_p(c)=\lVert t^\alpha-c\rVert_p=\left(\int_0^1 |t^\alpha-c|^p\,dt\right)^{1/p},
\]
and find \(E_p(c_p)\), for each of those values of \(p\).

**2.** Let \(\{\phi_k\}_{k=0}^{m+1}\) be the set of monic orthogonal polynomials with respect to inner product \((u,v)=\int_a^b u(x)v(x)w(x)\,dx\). Let \(\phi_{-1}=0\) and \(\phi_0=1\).
* (a) Find expressions for constants \(\alpha_k\) and \(\beta_k\) to determine a 3-term recurrence relation of the form
  \[
  \phi_{k+1}(x)=(x-\alpha_k)\phi_k-\beta_k\phi_{k-1}(x),\quad k=0,\ldots,m.
  \]
* (b) Use the above relation to determine \(\phi_1,\phi_2\) and \(\phi_3\), using the inner-product \((u,v)=\int_0^1 u(x)v(x)\,dx\).

**3.** Consider finding a zero of function \(f:D\subseteq\mathbb{R}^n\to\mathbb{R}^n\) that can be written as the sum of a linear and nonlinear part
\[
f(x)=Bx+G(x),
\]
where \(B\) is a nonsingular matrix and \(G:D\subseteq\mathbb{R}^n\to\mathbb{R}^n\) is some nonlinear function. At a point \(x_k\) consider an affine model \(M_k(x)=a_k+A_k(x-x_k)\), where the quantities \(a_k\in\mathbb{R}^n\) and \(A_k\in\mathbb{R}^{n\times n}\) are to be determined.
* (a) Determine \(a_k\) and \(A_k\) so that the following conditions hold:
  \[
  M_k(x_k)=f(x_k)\quad\text{and}\quad M_k'(x_k)=B.
  \]
* (b) Derive the iteration obtained by defining \(x_{k+1}\) as the zero of \(M_k(x)\).

**4.** Let \(f\in C^\infty(a,b)\). Let \(x_0<x_1<x_2\) be three points in \([a,b]\) that are not necessarily equally spaced.
* (a) Based on the quadratic interpolant \(p_2\) which satisfies \(p_2(x_0)=f(x_0)\), \(p_2(x_1)=f(x_1)\) and \(p_2(x_2)=f(x_2)\), find the centered finite difference approximations to \(f'(x_1)\) and \(f''(x_1)\) (you should explicitly show how the difference approximations are derived from the interpolant).
* (b) Derive an expression for the error, \(f'(x_1)-p_2'(x_1)\).

**5.** This problem has two parts.
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
