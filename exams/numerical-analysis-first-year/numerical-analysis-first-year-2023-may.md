# Numerical Analysis, first year exam, May 2023

*Do 4 (four) problems.*

**1.** Consider
\[
y'=4ty,\qquad t\in[0,1],\qquad y(0)=2, \tag{1}
\]
which has solution \(Y(t)=2e^{2t^2}\).
* (a) Derive an error bound for the Euler scheme.
* (b) Derive the Taylor method of order 2 for (1).

**2.** Find \(a,b,c\) so that the quadrature formula
\[
\int_0^2 f(x)\,dx=af(0)+bf(1)+cf(2)
\]
has the largest degree of precision.

**3.** Suppose \(f\in C^{n+1}[a,b]\), and let \(p\in\mathcal{P}_n\) be a polynomial that interpolates the data \(\{(x_i,f(x_i))\}_{i=0}^n\), where \(x_0,\ldots,x_n\) are distinct points in \([a,b]\). Consider an arbitrary fixed \(x\in[a,b]\), and derive an exact expression for the error \(f(x)-p(x)\).

**4.** Let \(\mathcal{P}_1\) be the space of polynomials of degree at most one. Using the norm
\[
\lVert u\rVert_2=\left(\int_a^b u^2\,dx\right)^{1/2}.
\]
* (a) Find the least-squares approximation to \(f(x)=x^3\) in \(\mathcal{P}_1\) over \([a,b]=[-1,1]\).
* (b) Find the least-squares approximation to \(f(x)=x^3\) in \(\mathcal{P}_1\) over \([a,b]=[0,1]\).

**5.** Let \(G=[0,2]\) and
\[
g(x)=\frac{1}{3}\left(\frac{x^3}{3}-x^2-\frac{5x}{4}+4\right).
\]
Use the contraction mapping theorem to prove that if \(x_0\in G\), then the sequence defined by \(x_{k+1}=g(x_k)\) \((k=0,1,\ldots)\) converges to a unique fixed point \(z\in G\).
* (b) Consider the fixed point iteration method \(x_{k+1}=g(x_k)\) \((k=0,1,\ldots)\) for solving the nonlinear equation \(f(x)=0\). Consider choosing an iteration function of the form
  \[
  g(x)=x-af(x)-b(f(x))^2-c(f(x))^3,
  \]
  where \(a,b,c\) are parameters to be determined. Assume \(f\) is sufficiently differentiable and the corresponding iterations \(x_{k+1}=g(x_k)\) converge to a unique fixed point \(z\). Find expressions for the parameters \(a,b,c\) in terms of functions of \(z\) such that the iteration method is of fourth order.
