# Numerical Analysis, PhD exam, January 2016, Part 2

*You must show all your work as neatly and clearly as possible and indicate the final answer clearly.*

**1.** A fourth degree polynomial \(P(x)\) satisfies \(\Delta^4P(0)=24\), \(\Delta^3P(0)=6\), and \(\Delta^2P(0)=0\), where \(\Delta P(x)=P(x+1)-P(x)\). Compute \(\Delta^2P(10)\).

**2.** Consider the fixed point iteration
\[
x_{n+1}=\phi(x_n),\qquad n=0,1,2,\ldots
\]
where
\[
\phi(x)=Ax+Bx^2+Cx^3.
\]
Given a positive number \(\alpha\), determine the constants \(A,B,C\) such that the iteration converges locally to \(1/\alpha\) with order \(p=3\).

**3.** This problem has the following parts:
* (a) Find \(\alpha\), \(\beta\) and \(\gamma\) so that the quadrature formula has a maximum degree of precision. What is the exact degree of precision of this quadrature formula?
  \[
  \int_0^2 f(x)\,dx\approx \alpha(f(0)+f(2))+\beta(f'(0)-f'(2))+\gamma(f''(0)-f''(2)).
  \]
* (b) Suggest your own quadrature formula for the integral
  \[
  \int_0^2 f(x)\,dx.
  \]
  Your formula should have expected degree of precision at least four (you don’t have to compute to demonstrate that).

**4.** For the function
\[
f(x)=\sqrt[m]{|x|},\qquad m\ne\frac12,
\]
in the interval \([-1,1]\), find the polynomial of minimax approximation of degree 2. What is the minimax error? What happens if \(m=\frac12\)?

**5.** Prove that Gaussian quadrature formula (for any \(n\)) in the interval \([-1,1]\) and with weight \(w(x)=1\) is exact for all odd functions.
