# Numerical Analysis PhD exam, May 2014

*You have 2 hours to answer the following questions. You must show all your work as neatly and clearly as possible and indicate the final answer clearly. You may not use a calculator.*

**1.** Show that the fixed point equation \(x=f(x)\) with a fixed point \(\alpha\) can be solved iteratively, if \(f'(\alpha)\ne 1\), by one of the following fixed point iteration formulas:
* (a) \(x_{n+1}=f(x_n)\)
* (b) \(x_{n+1}=f^{-1}(x_n)\). Hint: The following formula for the derivative of an inverse is valid
  \[
  [f^{-1}]'(x)=\frac{1}{f'(f^{-1}(x))}.
  \]
* (c) \(x_{n+1}=(x_n+f(x_n))/2\)

**2.** Let \(f(x)\in C^1[a,b]\). Let \(p(x)\) be a polynomial for which
\[
\lVert f'-p\rVert_\infty\le \epsilon
\]
and define
\[
q(x)=f(a)+\int_a^x p(t)\,dt,\qquad a\le x\le b.
\]
Show that \(q(x)\) is a polynomial that satisfies
\[
\lVert f-q\rVert_\infty\le \epsilon(b-a).
\]

**3.** Consider the integral
\[
\int_0^\pi x^2\cos x\,dx. \tag{1}
\]
* (a) Consider a quadrature rule of the form
  \[
  \int_0^\pi x^\alpha f(x)\,dx\approx Af(0)+B\int_0^\pi f(x)\,dx
  \]
  where \(\alpha>-1\), \(\alpha\ne 0\) is a parameter. Determine the constants \(A,B\) so that the quadrature formula has degree of exactness one.
* (b) Use the formula in part (a) to approximate the integral (1).

**4.** For the function \(f(x)=\ln(1+x)\) for \(x\in[0,1]\), find the minimax approximation polynomial of degree one. Give the exact value of the minimax error.

**5.** Assume that you are solving the initial value problem
\[
\begin{aligned}
y'&=f(t,y), && a\le t\le b,\\
y(a)&=\alpha.
\end{aligned}
\]
* (a) Derive the formula for the global error of the numerical solutions for the ODE problem above obtained via Euler’s method. Hint: The formula is \(M=\lVert Y''\rVert_\infty\):
  \[
  \lvert Y(t_i)-w_i\rvert<\frac{hM}{2L}\left[e^{L(b-a)}-1\right].
  \]
* (b) Compute the value of \(M=\lVert Y''\rVert_\infty\) necessary to apply the global error formula above to the specific ODE problem
  \[
  \begin{aligned}
  y'&=\sin(t+2y)+e^t, && 0\le t\le 1,\\
  y(0)&=0.
  \end{aligned}
  \]
