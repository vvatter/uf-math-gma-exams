# Numerical Analysis PhD exam, August 2025

*Do 4 (four) of the first 5 problems (1–5) and 4 (four) of the last 5 problems (6–10).*

**1.** Suppose \(A\) is Hermitian positive definite.
* (a) Prove that each principal submatrix of \(A\) is Hermitian positive definite.
* (b) Prove that an element of \(A\) with largest magnitude lies on the diagonal.
* (c) Prove that \(A\) has a Cholesky decomposition.

**2.** Assume \(A\in\mathbb{C}^{m\times m}\).
* (a) Show that \(A\) has a Schur decomposition.
* (b) If \(A\) has a collection of \(m\) linearly independent eigenvectors, show that \(A\) is diagonalizable.

**3.** Let \(A\in\mathbb{C}^{m\times n}\), with \(m\ge n\) and \(\operatorname{rank}(A)=p=n\ge3\). Let \(a_1,a_2,\ldots\) denote the columns of \(A\).
* (a) Using the modified Gram–Schmidt process, write out expressions for \(q_1,q_2,q_3\), the first three columns of \(Q\) in the QR decomposition of \(A\).
* (b) Show the vector \(q_3\) found in part (a) is orthogonal to both \(q_1\) and \(q_2\).

**4.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\). Let \(u_j\) denote column \(j\) of \(U\).
* (a) Suppose \(\operatorname{rank}(A)=p<n<m\). Show \(\{u_1,u_2,\ldots,u_p\}\) is a basis for \(\operatorname{Col}(A)\) and \(\{u_{p+1},u_{p+2},\ldots,u_m\}\) is a basis for \(\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank and \(x\ne0\). Let \(\sigma_i\), \(i=1,\ldots,n\), be the singular values of \(A\). Show
  \[
  \sigma_1\ge \frac{\lVert Ax\rVert_2}{\lVert x\rVert_2}\ge\sigma_n>0.
  \]
  If you want to use the property that \(\lVert A\rVert_2=\sigma_1\), then you must prove that.

**5.** If \(q_1,\ldots,q_n\in\mathbb{C}^m\) is an orthonormal basis for the subspace \(V\subset\mathbb{C}^m\), prove that the orthogonal projector onto \(V\) is \(QQ^*\), where \(Q\) is the matrix whose columns are the \(q_j\).

**6.** Consider the fixed point iteration method \(x_{k+1}=g(x_k)\), \(k=0,1,\ldots\), for solving the nonlinear equation \(f(x)=0\). Consider choosing an iteration function of the form
\[
g(x)=x-af(x)-b(f(x))^2-c(f(x))^3,
\]
where \(a,b,\) and \(c\) are parameters to be determined. Assume \(f\) is sufficiently differentiable and the corresponding iterations \(x_{k+1}=g(x_k)\) converge to a unique fixed point \(z\). Find expressions for the parameters \(a,b,\) and \(c\) in terms of functions of \(z\) such that the iteration method is of fourth order.

**7.** Consider the Lagrange polynomial approximation \(p(x)\) of a function \(f(x)\in C^2[a,b]\) at two points \(x_0,x_1\in[a,b]\). Determine \(\alpha(x)\) explicitly in the following formula
\[
f(x)-p(x)=\frac{f^{(n+1)}(\alpha(x))\prod_{i=0}^{n}(x-x_i)}{(n+1)!}
\]
for the case
\[
f(x)=\frac1x,\qquad x_0=1,\qquad x_1=2.
\]

**8.** Assume that \(f\in C^3[a,b]\) and \(x,x+h,x+2h\in[a,b]\). Determine constants \(c_1\) and \(c_2\) such that
\[
\left|f'(x)-\frac1h\left[-\frac32f(x)+c_1f(x+h)+c_2f(x+2h)\right]\right|\le ch^2\max_{a\le x\le b}|f'''(x)|,
\]
where \(c>0\) is a constant independent of \(h\).

**9.** Let \(Q_m(f)\) denote the \(m\)-point Gaussian quadrature rule over the interval \([a,b]\) and with continuous weight function \(\rho(x)\ge0\), that is,
\[
Q_m(f)=\sum_{i=1}^{m}\alpha_i f(x_i)\approx J(f)=\int_a^b\rho(x)f(x)\,dx.
\]
Show that, if \(a\) and \(b\) are finite and \(f\) is continuous, then \(Q_m(f)\to J(f)\) as \(m\to\infty\).

**10.** Consider numerically solving the initial value problem
\[
y'(t)=f(t,y),\quad 0<t\le t_f,\qquad \text{with }y(0)=\eta.
\]
Assume \(f\) is sufficiently differentiable and let \(h\) denote the step size. Prove that the method
\[
y_{n+3}+y_{n+2}-y_{n+1}-y_n=h(f_{n+3}+f_{n+2}+f_{n+1}+f_n)
\]
is consistent but not convergent.
