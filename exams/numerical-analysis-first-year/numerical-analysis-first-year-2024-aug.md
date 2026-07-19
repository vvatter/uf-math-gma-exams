# Numerical Analysis, first year exam, August 2024

*Do 4 (four) problems.*

**1.** Consider an approximate integration scheme of the following form, for \(0<\alpha<1\),
\[
\int_0^1 x^\alpha f(x)\,dx \approx A\int_0^1 f(x)\,dx+B\int_0^1 xf(x)\,dx.
\]
* (a) Determine the constants \(A,B\) so that the formula has the maximum degree of exactness.
* (b) What is the degree of exactness of the formula in (a)?

**2.** Let \(f\) be an arbitrary (continuous) function on \([0,1]\) satisfying \(f(x)+f(1-x)\equiv 1\) for \(0\leq x\leq 1\).
* (a) Show that \(\int_0^1 f(x)\,dx=\frac12\).
* (b) Show that the composite trapezoidal rule for computing \(\int_0^1 f(x)\,dx\) is exact.

**3.** Discuss uniqueness and non-uniqueness of the least squares approximation to a function \(f\) in the case of a discrete set \(T=\{t_1,t_2\}\) (i.e., \(N=2\)) where \(t_1\neq t_2\) and \(\Phi_n=P_{n-1}\) (polynomial of degree \(\leq n-1\)). In case of non-uniqueness, determine all solutions.

**4.** Derive the three-point formula for the second derivative
\[
f''(x_0)=\frac{1}{h^2}\bigl(f(x_0-h)-2f(x_0)+f(x_0+h)\bigr)-\frac{h^2}{12}f^{(4)}(\eta),
\]
where \(\eta\) is between \(x_0-h\) and \(x_0+h\).

**5.** Let \(x_0,x_1,\ldots,x_n\) be pairwise distinct points in \([a,b]\), \(-\infty<a<b<\infty\), and \(f\in C^1[a,b]\). Show that given any \(\epsilon>0\), there exists a polynomial \(p\) such that \(\lVert f-p\rVert_\infty<\epsilon\) and at the same time \(p(x_i)=f(x_i)\), \(i=0,1,\ldots,n\). Here \(\lVert u\rVert_\infty=\max_{a\leq x\leq b}|u(x)|\).
