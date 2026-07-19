# Numerical Analysis first year exam, May 2022

*Do 4 (four) problems.*

**1.** This problem has two parts.
* (a) Let \(G=[0,2]\) and
  \[
  g(x)=\frac{1}{3}\left(\frac{x^3}{3}-x^2-\frac{5}{4}x+4\right).
  \]
  Use the contraction mapping theorem to prove that if \(x_0\in G\), then the sequence defined by \(x_{k+1}=g(x_k)\), \((k=0,1,\ldots)\) converges to a unique fixed point \(z\in G\).
* (b) Consider the fixed point iteration method \(x_{k+1}=g(x_k)\), \(k=0,1,\ldots\) for solving the nonlinear equation \(f(x)=0\). Consider choosing an iteration function of the form
  \[
  g(x)=x-af(x)-b(f(x))^2-c(f(x))^3,
  \]
  where \(a\), \(b\), and \(c\) are parameters to be determined. Assume \(f\) is sufficiently differentiable and the corresponding iterations \(x_{k+1}=g(x_k)\) converge to a unique fixed point \(z\). Find expressions for the parameters \(a\), \(b\), and \(c\) in terms of functions of \(z\) such that the iteration method is of fourth order.

**2.** Consider \(f(t)=\sin(t)\).
* (a) Without using orthogonal polynomials, find the best approximation \(p_1(t)\in \mathbb{P}^2[-1,1]\) to \(f(t)\in C[-1,1]\) with respect to the \(L^2\) norm.
* (b) Find the Taylor polynomial approximation \(p_2(t)\) of degree 3 at \(t=0\).
* (c) Find the Lagrange polynomial approximation \(p_3(t)\) of degree 3 that interpolates \(f(t)\) at \(t=-1,-\frac{1}{3},\frac{1}{3},1\).

**3.** Given a differentiable function \(f(x)\), consider the problem of finding a polynomial \(p(x)\in\mathbb{P}^n\) such that
\[
p(x_0)=f(x_0),\qquad p'(x_i)=f'(x_i),\qquad i=1,2,\ldots,n,
\]
where \(x_i\), \(i=1,2,\ldots,n\), are distinct nodes. (It is not excluded that \(x_1=x_0\).) Show that the problem has a unique solution and describe how it can be obtained.

**4.** Let \(Q_m(f)\) denote the \(m\)-point Gaussian quadrature rule over the interval \([a,b]\) and with continuous weight function \(\rho(x)\geq 0\), that is,
\[
Q_m(f)=\sum_{i=1}^m\alpha_i f(x_i)\approx J(f)=\int_a^b\rho(x)f(x)\,dx.
\]
Show that, if \(a\) and \(b\) are finite and \(f\) is continuous, then \(Q_m(f)\to J(f)\) as \(m\to\infty\).

**5.** Consider numerically solving the initial value problem
\[
y'(t)=f(t,y),\quad 0<t\leq t_f,\qquad \text{with }y(0)=\eta.
\]
Assume \(f\) is sufficiently differentiable and let \(h\) denote the step size. Show that all convergent members of the family of methods
\[
y_{n+2}+(\theta-2)y_{n+1}+(1-\theta)y_n=\frac{1}{4}h\big[(6+\theta)f_{n+2}+3(\theta-2)f_n\big],
\]
parameterized by \(\theta\), are also \(A_0\)-stable.
