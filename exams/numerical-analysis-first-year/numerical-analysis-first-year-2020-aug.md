# Numerical Analysis first year exam, August 2020

*Do 4 (four) problems.*

**1.** Let \(\{\phi_k\}_{k=0}^{n+1}\) be a set of orthogonal polynomials on \([a,b]\), with respect to the inner product \((f,g)=\int_a^b f(x)g(x)w(x)\,dx\), indexed so that \(\phi_k\) is of degree \(k\). Prove that \(\phi_k\) has \(k\) distinct roots \(\{x_j^{(k)}\}_{j=1}^k\), with \(x_j^{(k)}\in[a,b]\), \(j=1,\ldots,k\).

**2.** Consider the interval \([a,b]\) with the partition \(a=x_1<x_2<\cdots<x_n<x_{n+1}=b\). Suppose \(s(x)\) is the natural cubic spline that interpolates the data \(\{(x_i,y_i)\}_{i=1}^{n+1}\), and that \(g\in C^2[a,b]\) interpolates the same data. Show that
\[
\int_a^b (s''(x))^2\,dx\leq\int_a^b (g''(x))^2\,dx.
\]

**3.** This problem has two parts.
* (a) Consider the inner product on \(C(0,2)\) given by \((f,g)=\int_0^2 f(t)g(t)\,dt\). Find three orthonormal polynomials \(\phi_0,\phi_1,\phi_2\) on \((0,2)\) with respect to the given inner product such that the degree of \(\phi_n\) is equal to \(n\), \(n=0,1,2\).
* (b) Find the nodes \(t_1\) and \(t_2\) and weights \(w_1\) and \(w_2\) which yield the weighted Gaussian Quadrature formula
  \[
  \int_0^2 f(t)\,dt\approx w_1f(t_1)+w_2f(t_2)
  \]
  with degree of exactness \(m=3\). You should find the nodes exactly, and may leave the weights \(w_1,w_2\) in integral form.

**4.** Prove for any \(f\in C[a,b]\) and integer \(n\geq 0\), that the best uniform approximation of \(f\) in \(P_n\) is unique. You may assume the existence of at least one best uniform approximation of \(f\).

**5.** Suppose \(f\in C^{n+1}[a,b]\), and let \(p\in P_n\) be a polynomial that interpolates the data \(\{(x_i,f(x_i))\}_{i=0}^n\), where \(x_0,\ldots,x_n\) are distinct points in \([a,b]\). Consider an arbitrary fixed \(x\in[a,b]\), and derive an exact expression for the error \(f(x)-p(x)\).
