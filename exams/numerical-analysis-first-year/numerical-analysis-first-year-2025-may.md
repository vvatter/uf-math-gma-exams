# Numerical Analysis, first year exam, May 2025

*Do 4 (four) problems.*

**1.** Consider the function \(g(x)=e^{-x}\).
* (a) Prove that \(g\) is a contraction on \(G=[\ln 1.1,\ln 3]\).
* (b) Prove that \(g\) maps \(G=[\ln 1.1,\ln 3]\) into \(G=[\ln 1.1,\ln 3]\).
* (c) Prove that \(x_{k+1}=g(x_k)\) converges to an unique fixed point \(z\in G=[\ln 1.1,\ln 3]\) for any initial value \(x_0\in G=[\ln 1.1,\ln 3]\).

**2.** Based on \(u_1(x)=1,u_2(x)=x,u_3(x)=x^2\), use Gram–Schmidt orthogonalization process to compute the three polynomials \(w_1(x),w_2(x),w_3(x)\) which are orthonormal on the interval \([0,1]\) with respect to the inner product \((f,g)=\int_0^1 f(x)g(x)\,dx\). Using these polynomials, find the best approximation in \(P^2[0,1]\) for \(f(x)=x^{\frac12}\).

**3.** Consider the finite difference formula
\[
f'(t_j)=\frac{1}{12h}\left[f(t_j-2h)-8f(t_j-h)+8f(t_j+h)-f(t_j+2h)\right]+O(h^4).
\]
* (a) Derive this formula by using Taylor’s theorem.
* (b) Derive this formula by using Lagrange polynomial representation.

**4.** Assume the numerical quadrature for \(\hat f(\hat x)\) on \([0,1]\) is
\[
\hat J(\hat f)=\int_0^1 \hat f(\hat x)\,d\hat x\approx \hat Q(\hat f)=\sum_{j=0}^m \hat\alpha_j\hat f(\hat x_j).
\]
Derive the numerical quadrature of \(J(f)=\int_a^b f(x)\,dx\).

**5.** Consider numerically solving the initial value problem
\[
y'(t)=f(t,y),\quad 0<t\leq t_f,\qquad \text{with }y(0)=\eta.
\]
Assume \(f\) is sufficiently differentiable and let \(h\) denote the step size. Show that all convergent members of the family of methods
\[
y_{n+2}+(\theta-2)y_{n+1}+(1-\theta)y_n=\frac14h\left[(6+\theta)f_{n+2}+3(\theta-2)f_n\right],
\]
parameterized by \(\theta\), are also \(A_0\)-stable.
