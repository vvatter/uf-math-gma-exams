# Numerical Analysis PhD exam, September 2005

*Do any eight of the ten problems below.*

**1.** For solving \(dy/dt=f(t,y)\), consider a one-step method of the form
\[
y_1=y_0+h\Phi(t_0,y_0,h).
\]
For any \(t_0\), it computes an approximation \(y_1\) to \(y(t_0+h)\), given \(y(t_0)=y_0\). Assuming enough smoothness on \(f\), study the local truncation error of Runge–Kutta methods for which
\[
\Phi(t_0,y_0,h)=\alpha_1k_1+\alpha_2k_2,
\]
where
\[
k_1=f(t_0,y_0),
\]
and
\[
k_2=f(t_0+\mu h,y_0+\mu hk_1).
\]
Under what conditions on the constants \(\alpha_1,\alpha_2\), and \(\mu\) do we get second order methods?

**2.** Prove that any polynomial \(q\) of degree at most \(n-1\) satisfies
\[
\sum_{i=0}^n q(x_i)\prod_{\substack{j=0\\j\ne i}}^n\frac{1}{x_i-x_j}=0,
\]
for any distinct \(n+1\) numbers \(x_i\), \(i=0,1,\ldots,n\). (Suggestion: Identify the left hand side as a divided difference.)

**3.** Let \(p_2(x)\) be the quadratic polynomial that interpolates \(f(x)\) at nodes \(x=0,h\), and \(2h\).
* (a) Approximating
  \[
  Q=\int_0^{3h}f(x)\,dx
  \]
  by
  \[
  Q_h=\int_0^{3h}p_2(x)\,dx,
  \]
  derive a quadrature rule: Explicitly calculate \(w_1,w_2,w_3\) so that
  \[
  Q_h=w_1f(0)+w_2f(h)+w_3f(2h).
  \]
* (b) Assuming that \(f(x)\) is four times continuously differentiable, show that
  \[
  Q-Q_h=\frac{3}{8}h^4f'''(0)+O(h^5).
  \]

**4.** Denote the complete (or clamped) and natural cubic splines interpolating \(f\in C^2[a,b]\) at knots \(t_0<t_1<\cdots<t_n\) by \(s_c(t)\) and \(s_n(t)\), respectively.
* (a) Prove that
  \[
  \int_a^b|s_c''(x)|^2\,dx\leq\int_a^b|f''(x)|^2\,dx.
  \]
  State an analogous inequality for \(s_n\).
* (b) Which of the two interpolating splines has smaller “energy”, i.e., which of \(\int_a^b|s_c''(x)|^2\,dx\) and \(\int_a^b|s_n''(x)|^2\,dx\) is smaller?

**5.** Let \(p>0\) and
\[
x=\sqrt{p+\sqrt{p+\sqrt{p+\cdots}}},
\]
where all the square roots are positive. Let \(F(y)=\sqrt{p+y}\). (How is the fixed point of \(F\) related to \(x\)?)
* (a) Consider the fixed point iteration \(x_{n+1}=F(x_n)\). Prove that if the initial iterate \(x_0\) satisfies \(x_0+p>0\) then all iterates remain on the same side of \(x\) as \(x_0\).
* (b) Prove that the fixed point iteration converges for all choices of initial guesses greater than \(-p+1/4\).
* (c) Whenever the fixed point iteration converges, what is its order of convergence?

**6.** This problem has three parts.
* (a) Consider the matrix \(A=uv^*\) where \(u\) and \(v\in\mathbb{C}^n\). Under what condition on \(u\) and \(v\) is \(A\) a projector?
* (b) Show that the Householder matrix \(H=I-2ww^*\) where \(\lVert w\rVert=1\) is unitary.
* (c) Given a vector \(x\in\mathbb{C}^n\) and an integer \(k\) with \(1<k<n\), derive a formula for a Householder matrix with the property that \((Hx)_i=0\) for \(i>k\) and \((Hx)_i=x_i\) for \(i<k\). Be sure to choose the signs so that the formula is numerically stable.

**7.** Consider the conjugate gradient algorithm for solving \(Ax=b\) for a symmetric positive definite \(A\in\mathbb{R}^{m\times m}\).
* (a) State a relationship between the \(n\)-th iterate of the algorithm and the best approximation to \(x\) from a Krylov space (be sure to specify the norm).
* (b) Prove that if \(A\) has only \(n\leq m\) distinct eigenvalues then the iteration (in the absence of round off errors) converges to the exact solution \(x\) in at most \(n\) steps no matter what the initial iterate is. (You may use 7a.)

**8.** Let \(P\) and \(Q\) be two \(m\times m\) orthogonal projectors.
* (a) Prove that \(\lVert P-Q\rVert_2\leq 1\).
* (b) Prove that if \(\lVert P-Q\rVert_2<1\) then the ranges of \(P\) and \(Q\) have equal dimensions.

**9.** Let \(P\) and \(Q\) be Hermitian positive definite matrices. Prove that
\[
x^*Px\leq x^*Qx,\qquad\text{for all }x\in\mathbb{C}^n,
\]
if and only if
\[
x^*Q^{-1}x\leq x^*P^{-1}x,\qquad\text{for all }x\in\mathbb{C}^n.
\]

**10.** State the Rayleigh quotient iteration. Apply it to the \(2\times2\) real matrix
\[
A=\begin{bmatrix}\lambda_1&0\\0&\lambda_2\end{bmatrix},
\]
where \(\lambda_1\ne\lambda_2\). Find the subset \(S\subseteq\mathbb{R}^2\) having the property that the iteration applied to this matrix with initial guesses in \(S\) do not converge. Is \(S\) a set of measure zero?
