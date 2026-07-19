# Numerical Analysis first year exam, January 2024

*Do 4 (four) problems.*

**1.** Derive the three-point formula for the second derivative
\[
f''(x_0)=\frac{1}{h^2}\bigl(f(x_0-h)-2f(x_0)+f(x_0+h)\bigr)-\frac{h^2}{12}f^{(4)}(\eta),
\]
for some \(\eta\in[x_0-h,x_0+h]\).

**2.** Consider
\[
y'=4ty;\qquad t\in[0,1];\qquad y(0)=2, \tag{1}
\]
which has solution \(Y(t)=2e^{2t^2}\).
* (a) Derive an error bound for the forward Euler scheme.
* (b) Derive the Taylor method of order 2 for (1).

**3.** Let \(\mathcal P_1\) be the space of polynomials of degree at most one. Using the norm
\[
\lVert u\rVert_2=\left(\int_a^b u^2\,dx\right)^{1/2}.
\]
* (a) Find the least-squares approximation to \(f(x)=x^3\) in \(\mathcal P_1\) over \([a,b]=[-1,1]\).
* (b) Find the least-squares approximation to \(f(x)=x^4\) in \(\mathcal P_1\) over \([a,b]=[0,1]\).

**4.** Consider the fixed point problem \(x=f(x)\) where \(f(x)=e^{-(3+x)}\).
* (a) Assuming all computations are done in exact arithmetic, find the largest open interval in \(\mathbb R\) where the fixed point iteration \(x_{k+1}=f(x_k)\) is ensured to converge.
* (b) Write a Newton iteration for finding the fixed point.

**5.** Suppose \(f\in C^{n+1}[a,b]\), and let \(p\in\mathcal P_n\) be a polynomial that interpolates the data \(\{(x_i,f(x_i))\}_{i=0}^n\), where \(x_0,\ldots,x_n\) are distinct points in \([a,b]\). Consider an arbitrary fixed \(x\in[a,b]\), and derive an exact expression for the error \(f(x)-p(x)\).
