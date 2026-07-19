# Numerical Analysis, PhD exam, May 2017, Part 2

*Do all five (5) problems.*

**1.** With
\[
\phi(w,t)=a f(w+ch,t+bh),
\]
find the values of the parameters \(a,b,c\) so that the resulting one-step method
\[
w_0=\alpha
\]
\[
w_{i+1}=w_i+h\phi(w_i,t_i)
\]
has local truncation error \(O(h^2)\).

**2.** Hint: the error term in the one unit Trapezoid rule is \(-\frac{h^3}{12}f''(\eta)\) and in the one unit Simpson’s rule is \(-\frac{h^5}{90}f^{(4)}(\eta)\).

Let \(S\) be the cubic spline given by
\[
S(x)=(x+1)^3 \text{ for } x\in[-1,0]
\]
\[
S(x)=(1-x)^3 \text{ for } x\in[0,1].
\]
* (a) Estimate the error of the composite trapezoidal rule applied to \(\int_{-1}^1 S(x)\,dx\), when \([-1,1]\) is divided into \(n\) subintervals of equal length \(h=2/n\) and \(n\) is even (and so 0 is a node).
* (b) Estimate the error of the composite Simpson’s rule applied to \(\int_{-1}^1 S(x)\,dx\), when \([-1,1]\) is divided into \(n\) subintervals of equal length \(h=2/n\) and \(n\) is divisible by 4 (and so 0 is a node).

**3.** This problem has two parts.
* (a) If \(f\in C^1[a,b]\) and \(a\leq x_0<\cdots<x_n\leq b\) and \(H,G\) are degree at most \(2n+1\) polynomials with \(G(x_i)=H(x_i)=f(x_i)\) and \(G'(x_i)=H'(x_i)=f'(x_i)\) for all \(i\), then \(G=H\).
* (b) If \(\varphi_0,\varphi_1,\ldots,\varphi_n\) are polynomials with \(\varphi_i\) of degree \(i\), then the set of \(\varphi_i\) is linearly independent.

**4.** Consider the inner product on \(C[0,\infty)\) given by
\[
\langle f,g\rangle=\int_0^\infty f(x)g(x)e^{-x}\,dx.
\]
* (a) Starting with the basis \(\{1,t,t^2\}\) for \(\mathcal P_2[0,\infty)\), find three orthonormal polynomials \(\phi_0,\phi_1,\phi_2\) on \([0,\infty)\) with respect to the inner product and the degree of \(\phi_n\) is equal to \(n\). Hint: \(\int_0^\infty t^m e^{-t}\,dt=m!\).
* (b) Find the equations satisfied by the values of \(w_1,w_2,t_1\) and \(t_2\) which yield the weighted Gaussian Quadrature formula
  \[
  \int_0^\infty f(t)e^{-t}\,dt=w_1f(t_1)+w_2f(t_2)
  \]
  with degree of precision 3.

**5.** This problem has two parts.
* (a) Assume \(g\in C^2[a,b]\) with \(g([a,b])\subset[a,b]\) and fixed point \(p\in(a,b)\). Assume that \(g'(p)=0\). Show that for any \(x\in[a,b]\) with \(x\ne p\),
  \[
  \frac{|g(x)-p|}{|x-p|^2}\leq M,
  \]
  where \(M=\max\{|g''(z)|:z\in[a,b]\}/2\).
* (b) Let \(g(x)=x-\tan(x)\). Find a fixed point \(p\) of \(g\) with \(g'(p)=0\) and give an explicit \([a,b]\) where you prove that for all \(x\in[a,b]\), \(g^n(x)\to p\).
