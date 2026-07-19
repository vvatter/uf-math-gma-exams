# Numerical Analysis PhD exam, January 2017

*You must show all your work as neatly and clearly as possible and indicate the final answer clearly. You may not use a calculator.*

**1.** This problem has two parts.
* (a) Show that the equation \(x=\frac{1}{2}\cos(x)\) has a solution \(\alpha\).
* (b) Find an interval \([a,b]\) containing \(\alpha\) and such that for every \(x_0\in[a,b]\), the iterative sequence
  \[
  x_{n+1}=\frac{1}{2}\cos x_n
  \]
  will converge to \(\alpha\). Justify your answer.

**2.** For the basic Lagrange polynomials
\[
L_i(x)=\prod_{j\ne i}\frac{x-x_j}{x_i-x_j}\qquad\text{for}\qquad i=0,\ldots,n,
\]
show that
\[
\sum_i L_i(x)=1\qquad\text{for all }x.
\]

**3.** Consider a quadrature rule of the form for \(0<\alpha<1\):
\[
\int_0^1 x^\alpha f(x)\,dx\approx A\int_0^1 f(x)\,dx+B\int_0^1 xf(x)\,dx.
\]
* (a) Determine the constants \(A,B\) so that the quadrature formula has maximum degree of exactness.
* (b) What is the degree of exactness of the formula in part (a)?

**4.** Let \(f\) be an arbitrary (continuous) function on \([0,1]\) satisfying
\[
f(x)+f(1-x)\equiv 1\qquad\text{for}\qquad 0\le x\le 1.
\]
* (a) Show that \(\int_0^1 f(x)\,dx=\frac{1}{2}\).
* (b) Show that the composite trapezoidal rule for computing \(\int_0^1 f(x)\,dx\) is exact.

**5.** Assume that you are solving the initial value problem
\[
\begin{aligned}
y'&=f(t,y), && a\le t\le b,\\
y(a)&=\alpha.
\end{aligned}
\]
The formula for the global error of the numerical solutions for the ODE problem above obtained via Euler’s method is (\(M=\lVert Y''\rVert_\infty\)):
\[
\lvert Y(t_i)-w_i\rvert<\frac{hM}{2L}\left[e^{L(b-a)}-1\right].
\]
Compute the values of \(L\) and \(M=\lVert Y''\rVert_\infty\) necessary to apply the global error formula above to the specific ODE problem
\[
\begin{aligned}
y'&=\sin(t+2y)+e^t, && 0\le t\le 1,\\
y(0)&=0.
\end{aligned}
\]
