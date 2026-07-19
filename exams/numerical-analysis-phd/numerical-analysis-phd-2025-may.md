# Numerical Analysis, PhD exam, May 2025

*Do 4 (four) of the first 5 (1-5) and 4 (four) of the last 5 problems (6-10).*

**1.** Assume \(A \in \mathbb{C}^{m\times m}\).
* (a) Show that \(A\) has a Schur decomposition.
* (b) If \(A\) is normal, show that \(A\) is diagonalizable.

**2.** Suppose \(A\) is Hermitian positive definite.
* (a) Prove that each principal submatrix of \(A\) is Hermitian positive definite.
* (b) Prove that an element of \(A\) with largest magnitude lies on the diagonal.
* (c) Prove that \(A\) has a Cholesky decomposition.

**3.** This problem has two parts.
* (a) Show that \(\lVert x\rVert_\infty\) is equivalent to \(\lVert x\rVert_2\) for all \(x\in\mathbb{R}^n\). That is to find \(C\) and \(c\) such that \(c\lVert x\rVert_\infty\leq \lVert x\rVert_2\leq C\lVert x\rVert_\infty\), for all \(x\in\mathbb{R}^n\). Note that the constants should be determined so that the equalities hold for some nonzero \(x\in\mathbb{R}^n\).
* (b) Show that \(\lVert QA\rVert_2=\lVert A\rVert_2\) if \(Q\) is a unitary matrix.

**4.** Assume that \(A\in\mathbb{C}^{n\times n}\) and there exists \(p\geq 1\) such that \(\lVert A\rVert_p<1\), where \(\lVert\cdot\rVert_p\) is a vector-induced matrix norm.
* (a) Prove that \(I-A\) is invertible.
* (b) Prove that
  \[
  (I-A)^{-1}=\sum_{k=0}^{\infty}A^k.
  \]
* (c) Prove that \(\lVert A\rVert_q\lVert A^{-1}\rVert_q\geq 1\), \(\forall 1\leq q\leq\infty\).
* (d) Prove that
  \[
  \frac{1}{1+\lVert A\rVert_p}\leq \lVert(I-A)^{-1}\rVert_p\leq \frac{1}{1-\lVert A\rVert_p}.
  \]

**5.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\). Let \(u_j\) denote column \(j\) of \(U\).
* (a) Suppose \(\operatorname{rank}(A)=p<n<m\). Show \(\{u_1,u_2,\ldots,u_p\}\) is a basis for \(\operatorname{Col}(A)\) and \(\{u_{p+1},u_{p+2},\ldots,u_m\}\) is a basis for \(\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank and \(x\neq 0\). Let \(\sigma_i\), \(i=1,\ldots,n\), be the singular values of \(A\). Show
  \[
  \sigma_1\geq \frac{\lVert Ax\rVert_2}{\lVert x\rVert_2}\geq \sigma_n>0.
  \]
  If you want to use the property that \(\lVert A\rVert_2=\sigma_1\), then you must prove that it holds.

**6.** Consider the function \(g(x)=e^{-x}\).
* (a) Prove that \(g\) is a contraction on \(G=[\ln 1.1,\ln 3]\).
* (b) Prove that \(g\) maps \(G=[\ln 1.1,\ln 3]\) into \(G=[\ln 1.1,\ln 3]\).
* (c) Prove that \(x_{k+1}=g(x_k)\) converges to an unique fixed point \(z\in G=[\ln 1.1,\ln 3]\) for any initial value \(x_0\in G=[\ln 1.1,\ln 3]\).

**7.** Based on \(u_1(x)=1\), \(u_2(x)=x\), \(u_3(x)=x^2\), use Gram–Schmidt orthogonalization process to compute the three polynomials \(w_1(x)\), \(w_2(x)\), \(w_3(x)\) which are orthonormal on the interval \([0,1]\) with respect to the inner product \((f,g)=\int_0^1 f(x)g(x)\,dx\). Using these polynomials, find the best approximation in \(P^2[0,1]\) for \(f(x)=x^{1/2}\).

**8.** Consider the finite difference formula
\[
f'(t_j)=\frac{1}{12h}\bigl[f(t_j-2h)-8f(t_j-h)+8f(t_j+h)-f(t_j+2h)\bigr]+O(h^4).
\]
* (a) Derive this formula by using Taylor’s theorem.
* (b) Derive this formula by using Lagrange polynomial representation.

**9.** Assume the numerical quadrature for \(\hat f(\hat x)\) on \([0,1]\) is
\[
\hat J(\hat f)=\int_0^1\hat f(\hat x)\,d\hat x\approx \hat Q(\hat f)=\sum_{j=0}^m\hat\alpha_j\hat f(\hat x_j).
\]
Derive the numerical quadrature of \(J(f)=\int_a^b f(x)\,dx\).

**10.** Consider numerically solving the initial value problem
\[
y'(t)=f(t,y),\qquad 0<t\leq t_f,\qquad \text{with }y(0)=\eta.
\]
Assume \(f\) is sufficiently differentiable and let \(h\) denote the step size. Show that all convergent members of the family of methods
\[
y_{n+2}+(\theta-2)y_{n+1}+(1-\theta)y_n=\frac14h\bigl[(6+\theta)f_{n+2}+3(\theta-2)f_n\bigr],
\]
parameterized by \(\theta\), are also \(A_0\)-stable.
