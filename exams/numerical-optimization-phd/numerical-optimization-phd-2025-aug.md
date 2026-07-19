# Variational Analysis/Numerical Optimization PhD exam, August 2025

*Do 8 problems, 4 from problems 1–5 and 4 from problems 6–10.*

**1.** Recall that \(f:\mathbb R^n\to\mathbb R\) is convex with modulus \(\theta\geq 0\) if and only if
\[
f[(1-\alpha)\mathbf x+\alpha\mathbf y]\leq (1-\alpha)f(\mathbf x)+\alpha f(\mathbf y)+\frac{\theta\alpha(\alpha-1)}{2}\|\mathbf y-\mathbf x\|^2
\]
for all \(\mathbf x,\mathbf y\in\mathbb R^n\) and \(\alpha\in[0,1]\).
* (a) If \(f\) is continuously differentiable, then show that \(f\) is convex with modulus \(\theta\geq 0\) if and only if
  \[
  f(\mathbf y)\geq f(\mathbf x)+\nabla f(\mathbf x)(\mathbf y-\mathbf x)+\frac{\theta}{2}\|\mathbf y-\mathbf x\|^2
  \]
  for all \(\mathbf x,\mathbf y\in\mathbb R^n\).
* (b) If \(f\) is twice continuously differentiable, then show that \(f\) is convex with modulus \(\theta\geq 0\) if and only if the smallest eigenvalue of \(\nabla^2f\) is \(\geq\theta\).

**2.** Suppose \(f:\mathcal K\to\mathbb R\) where \(\mathcal K\subset\mathbb R^n\) is a convex set.
* (a) If \(\mathbf x^*\) is a local minimizer of \(f\), then show that
  \[
  \nabla f(\mathbf x^*)(\mathbf x-\mathbf x^*)\geq 0\qquad\text{for all }\mathbf x\in\mathcal K. \tag{1}
  \]
* (b) If \(f\) is convex and differentiable at some point \(\mathbf x^*\in\mathcal K\) where (1) holds, then show that \(\mathbf x^*\) is a global minimizer for \(f\) over \(\mathcal K\). Moreover, if the modulus of convexity of \(f\) is strictly greater than 0, then \(\mathbf x^*\) is the unique global minimizer of \(f\) over \(\mathcal K\).
* (c) Consider the quadratic programming problem
  \[
  \min \frac12\mathbf x^{\mathsf T}\mathbf A\mathbf x-\mathbf b^{\mathsf T}\mathbf x\qquad\text{subject to }\mathbf x\in\mathcal K,
  \]
  where \(\mathcal K\subset\mathbb R^n\) is a closed convex set and \(\mathbf A\in\mathbb R^{n\times n}\) is positive definite with smallest eigenvalue \(\alpha>0\). Show that the solutions \(\mathbf u_i\), \(i=1,2\), associated with \(\mathbf b=\mathbf b_i\), \(i=1,2\), respectively, satisfy
  \[
  \|\mathbf u_1-\mathbf u_2\|\leq \|\mathbf b_1-\mathbf b_2\|/\alpha.
  \]

**3.** Let \(\mathbf U\) and \(\mathbf V\in\mathbb R^{n\times m}\) and \(\mathbf M\in\mathbb R^{n\times n}\) with \(\mathbf M\) invertible.
* (a) If \(\mathbf I+\mathbf V^{\mathsf T}\mathbf M^{-1}\mathbf U\) is invertible, then show that \(\mathbf M+\mathbf U\mathbf V^{\mathsf T}\) is invertible with
  \[
  (\mathbf M+\mathbf U\mathbf V^{\mathsf T})^{-1}=\mathbf M^{-1}-\mathbf M^{-1}\mathbf U(\mathbf I+\mathbf V^{\mathsf T}\mathbf M^{-1}\mathbf U)^{-1}\mathbf V^{\mathsf T}\mathbf M^{-1}.
  \]
* (b) Consider the quadratic program
  \[
  \min \frac12\mathbf x^{\mathsf T}\mathbf A\mathbf x-\mathbf b^{\mathsf T}\mathbf x\qquad\text{subject to }\mathbf a^{\mathsf T}\mathbf x=c, \tag{2}
  \]
  where \(\mathbf A\) is a symmetric, positive definite matrix. The penalty approximation to (2) is
  \[
  \min \frac12\mathbf x^{\mathsf T}\mathbf A\mathbf x-\mathbf b^{\mathsf T}\mathbf x+\frac p2(\mathbf a^{\mathsf T}\mathbf x-c)^2,
  \]
  where \(p>0\) is the penalty parameter. Use the formula from (a) to obtain an explicit solution to the penalized problem in terms of \(\mathbf A^{-1}\), and the parameters of the quadratic program.

**4.** Consider the primal optimization problem
\[
\inf_{\mathbf x\in\mathcal K}\{f(\mathbf x):\mathbf h(\mathbf x)=0,\quad \mathbf g(\mathbf x)\leq 0\}, \tag{P}
\]
where \(\mathcal K\subset\mathbb R^n\), \(\mathbf h:\mathbb R^n\to\mathbb R^m\), and \(\mathbf g:\mathbb R^n\to\mathbb R^l\). The dual of (P) is
\[
\sup_{\substack{\boldsymbol\mu\geq 0\\\boldsymbol\lambda\in\mathbb R^m}}L(\boldsymbol\lambda,\boldsymbol\mu),
\qquad\text{where}\qquad
L(\boldsymbol\lambda,\boldsymbol\mu):=\inf_{\mathbf x\in\mathcal K}f(\mathbf x)+\boldsymbol\lambda^{\mathsf T}\mathbf h(\mathbf x)+\boldsymbol\mu^{\mathsf T}\mathbf g(\mathbf x). \tag{D}
\]
* (a) Show that the dual objective \(L\) is a concave function.
* (b) Suppose that \(\mathcal K=\mathbb R^n\), \(\mathbf h(\mathbf x)=\mathbf A\mathbf x-\mathbf b\) where \(\mathbf A\in\mathbb R^{m\times n}\), each component of \(\mathbf g\) is convex, and there exists a solution \(\mathbf x^*\) to (P) where the first-order optimality conditions are satisfied. Show that there is no duality gap. That is, show that the infimum in (P) is equal to the supremum in (D).

**5.** Consider the following primal quadratic program:
\[
\min q(\mathbf x):=\frac12\mathbf x^{\mathsf T}\mathbf x-\mathbf b^{\mathsf T}\mathbf x
\qquad\text{subject to }\mathbf a^{\mathsf T}\mathbf x=c,\ \mathbf x\geq 0, \tag{QP}
\]
where \(\mathbf b\) and \(\mathbf a\in\mathbb R^n\), \(\mathbf a>0\), and \(c>0\) is a scalar. An associated dual program is
\[
\max_{\lambda}L(\lambda):=\min_{\mathbf x\geq 0}q(\mathbf x)+\lambda(\mathbf a^{\mathsf T}\mathbf x-c). \tag{QD}
\]
Since \(\lambda\) is a scalar, the dual problem (QD) is much easier to solve than the primal problem (QP).
* (a) The minimization over \(\mathbf x\geq 0\) in the dual function \(L\) uncouples into \(n\) independent minimizations over each component \(x_i\). Give a formula for \(x_i(\lambda)\), the minimizer over \(x_i\geq 0\) of the dual function at \(\lambda\).
* (b) The points where \(\lambda=b_i/a_i\), \(1\leq i\leq n\), are known as the break points of the dual function. Give a formula for the value of the dual function and its derivative at any point \(\lambda\) which is not a break point. Show that \(L'(\lambda)=\mathbf a^{\mathsf T}\mathbf x(\lambda)-c\).
* (c) Show that \(L'\) is a decreasing function of \(\lambda\) (recall that \(L\) is concave), and \(L'(\lambda)\) is linear in \(\lambda\) between the break points. Based on these observations, give an algorithm for maximizing \(L\).
* (d) Given a solution \(\lambda^*\) of the dual problem, show that \(\mathbf x(\lambda^*)\) is the solution of the primal problem.

**6.** Let us consider the minimization problem
\[
\min I(y):=\int_0^1 f(y'(x),y(x),x)\,dx\qquad\text{subject to }y\in C_0^1, \tag{3}
\]
where \(f\) is a given continuously differentiable function. If \(y^*\) is a local minimizer of this problem, \(s\) is a scalar, \(h\in C_0^1\), then setting to zero the derivative of \(I(y^*+sh)\) evaluated at \(s=0\) yields the following first-order optimality condition:
\[
\int_0^1\left[\left(\frac{\partial f}{\partial y'}\right)^*(x)h'(x)+\left(\frac{\partial f}{\partial y}\right)^*(x)h(x)\right]dx=0 \tag{4}
\]
for all \(h\in C_0^1\), where
\[
\left(\frac{\partial f}{\partial y'}\right)^*(x):=\left(\frac{\partial f}{\partial y'}\right)^*(y^{*'}(x),y^*(x),x)
\quad\text{and}\quad
\left(\frac{\partial f}{\partial y}\right)^*(x):=\left(\frac{\partial f}{\partial y}\right)^*(y^{*'}(x),y^*(x),x).
\]
* (a) As a consequence of (4), show that
  \[
  \left(\frac{\partial f}{\partial y'}\right)^*\in C^1 \tag{5}
  \]
  and the Euler equation is satisfied. Note that it is only assumed that \(f\) is continuously differentiable; you should show that at a local minimizer of (3), the partial derivative in (5) is continuously differentiable.
* (b) For the special case
  \[
  f(y'(x),y(x),x)=\frac12y'(x)^2-\phi(x)y(x)^2,
  \]
  where \(\phi\in C^k\) for some integer \(k\geq 0\), what does the observation in (a) imply concerning the smoothness of a minimizer \(y^*\) for (3).

**7.** Consider the equation
\[
(P(x)u'(x))'=Q(x)u(x),\qquad x\in[0,1], \tag{E}
\]
where \(Q\) is continuous and \(P\) is continuously differentiable and strictly positive on \([0,1]\). Suppose (E) has the property that whenever \(u\) is a solution of (E) with \(u(0)=u(a)=0\) for some \(0<a\leq 1\), \(u\) is identically zero on \([0,a]\). Show that the solution of the initial-value problem for (E), with the initial conditions \(u(0)=0\) and \(u'(0)=1\), is strictly positive on \((0,1]\).

**8.** Consider the variational problem
\[
\min \int_0^1\left[\frac12u'(x)^2+e^{u(x)}\right]dx\qquad\text{subject to }u\in\mathcal H_0^1.
\]
* (a) What is the first-order necessary optimality condition (Euler equation) for this variational problem?
* (b) Consider a uniform mesh \(x_k=kh\) where \(h=1/N\); let \(u_k\) denote the approximation to \(u(x_k)\). Of course, \(u_0=u_N=0\). Give a finite difference approximation in terms of \(u_1,\ldots,u_{N-1}\) to the solution of the Euler equation.
* (c) Let \(\mathbf F(\mathbf u)=0\) denote the finite difference system where \(\mathbf u=(u_1,u_2,\ldots,u_{N-1})^{\mathsf T}\in\mathbb R^{N-1}\), and let \(\mathbf u^*\) denote the vector formed by evaluating the solution of the Euler equation at the mesh points \(x_1,x_2,\ldots,x_{N-1}\). Obtain a bound for the components of \(\mathbf F(\mathbf u^*)\) in terms of the mesh spacing \(h\).

**9.** Consider the initial-value problem
\[
\dot{\mathbf x}(t)=\mathbf A(t)\mathbf x(t)+\mathbf u(t),\qquad \mathbf x(0)=0,
\]
where \(\mathbf x:[0,1]\to\mathbb R^n\) and \(\mathbf A\in L^\infty([0,1];\mathbb R^{n\times n})\).
* (a) Assuming \(\mathbf u\in L^2\), obtain a bound for the sup-norm of \(\mathbf x\) in terms of the \(L^2\) norm of \(\mathbf u\).
* (b) Let \(\Omega:\mathcal H_0^1\to\mathbb R\) be defined by
  \[
  \Omega(h)=\frac12\int_0^1r^2(x)\,dx\qquad\text{where }r(x)=h'(x)+w(x)h(x),
  \]
  where \(w\) is uniformly bounded on \([0,1]\). Show that there exists \(\beta>0\) such that
  \[
  \Omega(h)\geq\beta(\|h\|^2+\|h'\|^2)\qquad\text{for all }h\in\mathcal H_0^1,
  \]
  where \(\|\cdot\|\) is the \(L^2\) norm.

**10.** Consider the following control problem:
\[
\min \int_0^1\left[\frac12u^2(x)+y(x)\right]dx
\qquad\text{subject to }y'(x)=u(x),\ y(0)=0,\ u(x)\geq\ell(x),
\]
where \(\ell(x)\) is a given lower bound for the control \(u(x)\) at each \(x\in[0,1]\).
* (a) What is the first-order optimality condition (Pontryagin minimum principle) for this problem?
* (b) What is the solution of the control problem?
