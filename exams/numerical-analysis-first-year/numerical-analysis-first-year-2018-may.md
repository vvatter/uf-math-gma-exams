# Numerical Analysis, first year exam, May 2018

*Do all five (5) problems.*

**1.** Consider
\[
y' = 4ty;\quad t \in [0,1];\quad y(0)=2, \tag{1}
\]
which has solution \(Y(t)=2e^{2t^2}\).
* (a) Using the Euler method error estimate find the value of \(h\) required to ensure that the Euler method solution \(w_i\) of (1) satisfies \(|Y(t_i)-w_i|\leq 0.1\) for all \(i\).
* (b) Derive the Taylor method of order 2 for (1).

**2.** Let \(g\in C^2([a,b])\) and \(p\in(a,b)\) with \(g(p)=p\), \(g'(p)=0\), \(g''(p)\neq 0\).
* (a) Show there is an \(\epsilon>0\) so that for all \(x\in[p-\epsilon,p+\epsilon]\), we have \(g^n(x)\to p\) as \(n\to\infty\).
* (b) With \(\epsilon\) as in part (a), show that for all \(x\in[p-\epsilon,p+\epsilon]\), we have \(|g(x)-p|\leq M|x-p|^2\), where \(M=\max\{|g''(x)|:|x-p|\leq\epsilon\}/2\).

**3.** Find the second order (i.e. quadratic) least squares approximation to the function \(f(x)=x^4\) on the interval \([-1,1]\) with respect to the weight \(w(x)\equiv 1\) using the fact that the first three orthonormal polynomials on \([-1,1]\) with respect to this weight are
\[
\varphi_0(x)=\sqrt{1/2},\quad \varphi_1(x)=\sqrt{3/2}\,x,\quad\text{and}\quad \varphi_2(x)=\sqrt{5/8}(3x^2-1).
\]

**4.** This problem has two parts.
* (a) Assume \(N(h)\) is the computed approximation for \(M\) for each \(h>0\) and
  \[
  M=N(h)+C_1h+C_2h^2+C_3h^3+\cdots.
  \]
  Use the values \(N(h)\), \(N(h/3)\), and \(N(h/9)\) to produce a \(O(h^3)\) approximation to \(M\).
* (b) Taylor’s formula yields the following.
  \[
  f'(x_0)=\frac{1}{h}\bigl(f(x_0+h)-f(x_0)\bigr)-\frac{h}{2}f''(x_0)-\frac{h^2}{6}f'''(x_0)+O(h^3).
  \]
  Use this with the extrapolation of part (a) to derive an \(O(h^3)\) formula for \(f'(x_0)\).

**5.** Find \(a,b,c\) so that the quadrature formula
\[
\int_0^2 f(x)\,dx=af(0)+bf(1)+cf(2)
\]
has degree of precision as large as possible, and show it is no larger than your answer.
