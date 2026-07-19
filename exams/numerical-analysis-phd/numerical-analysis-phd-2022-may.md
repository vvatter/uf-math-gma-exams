# Numerical Analysis PhD exam, May 2022

*Do 4 (four) of the first 5 (1-5) and 4 (four) of the last 5 problems (6-10).*

**1.** Prove or provide a counterexample to each of the following.
* (a) If matrix \(A\) is normal and triangular, then it is diagonal.
* (b) Every matrix has a Schur factorization.

**2.** This problem has two parts.
* (a) For \(v\in\mathbb{C}^n\), define \(f_A(v):=(v^*Av)^{1/2}\). Under what condition(s) on \(A\in\mathbb{C}^{n\times n}\) is \(f_A(\mathord{\cdot})\) a norm on \(\mathbb{C}^n\)? (Full credit will only be given for a general condition or conditions. An example is not sufficient.) Prove that \(f_A(\mathord{\cdot})\) is a norm on \(\mathbb{C}^n\) under the condition(s) you require.
* (b) Assuming the condition(s) you require in (a), given a matrix \(A\), determine the best constants \(\alpha\) and \(\beta\) to satisfy the inequality
  \[
  \alpha\lVert v\rVert_2\leq f_A(v)\leq\beta\lVert v\rVert_2.
  \]

**3.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\). Let \(u_j\) denote column \(j\) of \(U\).
* (a) Suppose \(\operatorname{rank}(A)=p<n<m\). Show \(\{u_1,u_2,\ldots,u_p\}\) is a basis for \(\operatorname{Col}(A)\), and \(\{u_{p+1},u_{p+2},\ldots,u_m\}\) is a basis for \(\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank and \(x\neq0\). Let \(\sigma_i\), \(i=1,\ldots,n\), be the singular values of \(A\). Show
  \[
  \sigma_1\geq\frac{\lVert Ax\rVert_2}{\lVert x\rVert_2}\geq\sigma_n>0.
  \]
  If you want to use the property that \(\lVert A\rVert_2=\sigma_1\), then you must prove that also.

**4.** Let \(\{a_1,\ldots,a_n\}\) be a linearly independent set of vectors. Consider the Gram–Schmidt and modified Gram–Schmidt algorithms for computing an orthonormal basis \(\{q_1,\ldots,q_n\}\) so that \(\operatorname{span}\{q_1,\ldots q_k\}=\operatorname{span}\{a_1,\ldots a_k\}\), for each \(k=1,\ldots,n\).

Suppose in computing \(q_2\), an orthogonalization error is committed so that \(q_2^*q_1=\epsilon\).
* (a) Use the Gram–Schmidt algorithm to compute \(v_3\) so that \(q_3=v_3/\lVert v_3\rVert\). What is \(v_3^*q_2\)?
* (b) Use the modified Gram–Schmidt algorithm to compute \(v_3\) so that \(q_3=v_3/\lVert v_3\rVert\). What is \(v_3^*q_2\)?

**5.** Compute the Cholesky decomposition of the following matrix, or explain why it does not exist.
\[
A=\begin{pmatrix}
1 & 1/2 & 2 & 3\\
1/2 & 5/16 & 3/2 & 5/2\\
2 & 3/2 & 17 & 17\\
3 & 5/2 & 17 & 31
\end{pmatrix}.
\]

**6.** This problem has two parts.
* (a) Let \(G=[0,2]\) and
  \[
  g(x)=\frac{1}{3}\left(\frac{x^3}{3}-x^2-\frac{5}{4}x+4\right).
  \]
  Use the contraction mapping theorem to prove that if \(x_0\in G\), then the sequence defined by \(x_{k+1}=g(x_k)\), \((k=0,1,\ldots)\) converges to a unique fixed point \(z\in G\).
* (b) Consider the fixed point iteration method \(x_{k+1}=g(x_k)\), \(k=0,1,\ldots\) for solving the nonlinear equation \(f(x)=0\). Consider choosing an iteration function of the form
  \[
  g(x)=x-af(x)-b(f(x))^2-c(f(x))^3,
  \]
  where \(a\), \(b\), and \(c\) are parameters to be determined. Assume \(f\) is sufficiently differentiable and the corresponding iterations \(x_{k+1}=g(x_k)\) converge to a unique fixed point \(z\). Find expressions for the parameters \(a\), \(b\), and \(c\) in terms of functions of \(z\) such that the iteration method is of fourth order.

**7.** Consider \(f(t)=\sin(t)\).
* (a) Without using orthogonal polynomials, find the best approximation \(p_1(t)\in\mathbb{P}^2[-1,1]\) to \(f(t)\in C[-1,1]\) with respect to the \(L^2\) norm.
* (b) Find the Taylor polynomial approximation \(p_2(t)\) of degree 3 at \(t=0\).
* (c) Find the Lagrange polynomial approximation \(p_3(t)\) of degree 3 that interpolates \(f(t)\) at \(t=-1,-\frac{1}{3},\frac{1}{3},1\).

**8.** Given a differentiable function \(f(x)\), consider the problem of finding a polynomial \(p(x)\in\mathbb{P}^n\) such that
\[
p(x_0)=f(x_0),\qquad p'(x_i)=f'(x_i),\qquad i=1,2,\ldots,n,
\]
where \(x_i\), \(i=1,2,\ldots,n\), are distinct nodes. (It is not excluded that \(x_1=x_0\).) Show that the problem has a unique solution and describe how it can be obtained.

**9.** Let \(Q_m(f)\) denote the \(m\)-point Gaussian quadrature rule over the interval \([a,b]\) and with continuous weight function \(\rho(x)\geq0\), that is,
\[
Q_m(f)=\sum_{i=1}^m\alpha_i f(x_i)\approx J(f)=\int_a^b\rho(x)f(x)\,dx.
\]
Show that, if \(a\) and \(b\) are finite and \(f\) is continuous, then \(Q_m(f)\to J(f)\) as \(m\to\infty\).

**10.** Consider numerically solving the initial value problem
\[
y'(t)=f(t,y),\quad 0<t\leq t_f,\qquad\text{with }y(0)=\eta.
\]
Assume \(f\) is sufficiently differentiable and let \(h\) denote the step size. Show that all convergent members of the family of methods
\[
y_{n+2}+(\theta-2)y_{n+1}+(1-\theta)y_n=\frac{1}{4}h\big[(6+\theta)f_{n+2}+3(\theta-2)f_n\big],
\]
parameterized by \(\theta\), are also \(A_0\)-stable.
