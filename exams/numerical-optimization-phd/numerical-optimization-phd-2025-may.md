# Variational Analysis/Numerical Optimization PhD exam, May 2025

*Do 8 problems, 4 from problems 1–5 and 4 from problems 6–10.*

**1.** Recall that \(f:\mathbb{R}^n\to\mathbb{R}\) is convex if and only if
\[
f[(1-\alpha)\mathbf{x}+\alpha\mathbf{y}]\leq (1-\alpha)f(\mathbf{x})+\alpha f(\mathbf{y})
\]
for all \(\mathbf{x},\mathbf{y}\in\mathbb{R}^n\) and \(\alpha\in[0,1]\).
* (a) If \(f\) is continuously differentiable, then show that \(f\) is convex if and only if
  \[
  f(\mathbf{y})\geq f(\mathbf{x})+\nabla f(\mathbf{x})(\mathbf{y}-\mathbf{x})
  \]
  for all \(\mathbf{x},\mathbf{y}\in\mathbb{R}^n\).
* (b) If \(f\) is twice continuously differentiable, then show that \(f\) is convex if and only if \(\nabla^2f\) is positive semidefinite on \(\mathbb{R}^n\).

**2.** Suppose that \(\boldsymbol{\Phi}:\mathcal{K}\to\mathbb{R}^n\) is continuously differentiable on \(\mathcal{K}\subset\mathbb{R}^n\).
* (a) If \(\mathcal{K}\) is a convex set, then show that
  \[
  \|\boldsymbol{\Phi}(\mathbf{x})-\boldsymbol{\Phi}(\mathbf{y})\|\leq \mu\|\mathbf{x}-\mathbf{y}\|
  \]
  for all \(\mathbf{x}\) and \(\mathbf{y}\in\mathcal{K}\), where \(\mu\) is the supremum of the singular values of \(\nabla\boldsymbol{\Phi}\) over \(\mathcal{K}\).
* (b) If \(\boldsymbol{\Phi}\) is a contraction on \(\mathcal{K}\), where \(\mathcal{K}\) is a closed set, and \(\boldsymbol{\Phi}(\mathbf{x})\in\mathcal{K}\) for each \(\mathbf{x}\in\mathcal{K}\), then show that \(\boldsymbol{\Phi}\) has a unique fixed point in \(\mathcal{K}\).

**3.** Let \(\mathbf{U}\) and \(\mathbf{V}\in\mathbb{R}^{n\times m}\) and \(\mathbf{M}\in\mathbb{R}^{n\times n}\) with \(\mathbf{M}\) invertible.
* (a) If \(\mathbf{I}+\mathbf{V}^{\mathsf T}\mathbf{M}^{-1}\mathbf{U}\) is invertible, then show that \(\mathbf{M}+\mathbf{U}\mathbf{V}^{\mathsf T}\) is invertible with
  \[
  (\mathbf{M}+\mathbf{U}\mathbf{V}^{\mathsf T})^{-1}=\mathbf{M}^{-1}-\mathbf{M}^{-1}\mathbf{U}(\mathbf{I}+\mathbf{V}^{\mathsf T}\mathbf{M}^{-1}\mathbf{U})^{-1}\mathbf{V}^{\mathsf T}\mathbf{M}^{-1}.
  \]
* (b) If \(\mathbf{U}=\mathbf{V}=\mathbf{A}\in\mathbb{R}^{n\times m}\), where the columns of \(\mathbf{A}\) are linearly independent, and \(\mathbf{M}=\mathbf{Q}\), a symmetric matrix, then show that
  \[
  (\mathbf{Q}+p\mathbf{A}\mathbf{A}^{\mathsf T})(\mathbf{I}+p\mathbf{A}\mathbf{A}^{\mathsf T})^{-1}=\mathbf{Q}_0+\mathcal{O}(1/p),
  \]
  where
  \[
  \mathbf{Q}_0=\mathbf{Q}+(\mathbf{I}-\mathbf{Q})[\mathbf{A}(\mathbf{A}^{\mathsf T}\mathbf{A})^{-1}\mathbf{A}^{\mathsf T}].
  \]

**4.** Consider the following quadratic program:
\[
\min\ q(\mathbf{x}):=\sum_{i=1}^n 0.5x_i^2+c_i x_i
\quad\text{subject to}\quad \mathbf{a}^{\mathsf T}\mathbf{x}=b,\quad \mathbf{x}\geq 0. \tag{QP}
\]
where \(\mathbf{c}\) and \(\mathbf{a}\in\mathbb{R}^n\), \(\mathbf{a}\geq 0\), and \(b>0\) is a scalar.
* (a) Develop an algorithm for solving (QP) by maximizing the dual function
  \[
  L(\lambda)=\inf\{q(\mathbf{x})+\lambda(\mathbf{a}^{\mathsf T}\mathbf{x}-b):\mathbf{x}\geq 0\}
  \]
  over the dual multiplier \(\lambda\). Here, the constraint \(\mathcal{K}\) in the dual function is taken as \(\mathcal{K}=\{\mathbf{x}\in\mathbb{R}^n:\mathbf{x}\geq 0\}\).
* (b) Given the optimal \(\lambda\) for the dual problem, what is the solution of the primal problem?

**5.** Consider the primal problem
\[
\min\ f(\mathbf{x})\quad\text{subject to}\quad \mathbf{A}\mathbf{x}-\mathbf{b}=0,\quad \mathbf{g}(\mathbf{x})\leq 0, \tag{P}
\]
where \(f:\mathbb{R}^n\to\mathbb{R}\) and the components of \(\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^l\) are convex and continuously differentiable, \(\mathbf{A}\in\mathbb{R}^{m\times n}\), and \(\mathbf{b}\in\mathbb{R}^m\). The dual problem is
\[
\max\ L(\boldsymbol{\lambda},\boldsymbol{\mu})\quad\text{subject to}\quad \boldsymbol{\lambda}\in\mathbb{R}^m,\quad \boldsymbol{\mu}\in\mathbb{R}^l,\quad \boldsymbol{\mu}\geq 0, \tag{D}
\]
where
\[
\begin{aligned}
L(\boldsymbol{\lambda},\boldsymbol{\mu})&=\inf\{\mathcal{L}(\mathbf{x},\boldsymbol{\lambda},\boldsymbol{\mu}):\mathbf{x}\in\mathbb{R}^n\},\\
\mathcal{L}(\mathbf{x},\boldsymbol{\lambda},\boldsymbol{\mu})&=f(\mathbf{x})+\boldsymbol{\lambda}^{\mathsf T}(\mathbf{A}\mathbf{x}-\mathbf{b})+\boldsymbol{\mu}^{\mathsf T}\mathbf{g}(\mathbf{x}).
\end{aligned}
\]
* (a) Show that if (P) has a local minimizer \(\mathbf{x}^*\), then \(\mathbf{x}^*\) is a global minimizer for (P). Moreover, if the first-order optimality conditions hold at \(\mathbf{x}^*\), then there is a solution to (D) with no duality gap.
* (b) Returning to (QP) of problem 4, show that there is no duality gap. You may wish to consider both the set
  \[
  S=\{(r,s)\in\mathbb{R}^2:r\geq q(\mathbf{x})\text{ and }s=\mathbf{a}^{\mathsf T}\mathbf{x}-b\text{ for some }\mathbf{x}\geq 0\},
  \]
  and the point \((q^*,0)\), where \(q^*\) is the optimal cost for (QP). Explain why this point does not lie in the interior of \(S\). Use the separating hyperplane theorem to separate \(S\) and the point, and then analyze the resulting inequality.

**6.** Consider the initial-value problem
\[
\dot{\mathbf{x}}(t)=\mathbf{f}(\mathbf{x}(t),\mathbf{u}(t)),\qquad \mathbf{x}(0)=\mathbf{a},
\]
where \(\mathbf{a}\in\mathbb{R}^n\), \(\mathbf{f}:\mathcal{B}_\delta(\mathbf{a})\times\mathcal{U}\to\mathbb{R}^n\), with \(\mathcal{U}\subset\mathbb{R}^m\) a compact set and \(\delta>0\). It is assumed that \(\mathbf{f}\) is continuous on \(\mathcal{B}_\delta(\mathbf{a})\times\mathcal{U}\) and uniformly Lipschitz continuous in its first argument with Lipschitz constant \(L\) satisfying
\[
|\mathbf{f}(\mathbf{x}_1,\mathbf{u})-\mathbf{f}(\mathbf{x}_2,\mathbf{u})|\leq L|\mathbf{x}_1-\mathbf{x}_2|
\]
for all \(\mathbf{x}_1,\mathbf{x}_2\in\mathcal{B}_\delta(\mathbf{a})\) and \(\mathbf{u}\in\mathcal{U}\). If \(\epsilon=\delta/M\), where
\[
M=\max\{|\mathbf{f}(\mathbf{x},\mathbf{u})|:\mathbf{x}\in\mathcal{B}_\delta(\mathbf{a}),\ \mathbf{u}\in\mathcal{U}\},
\]
then show that the initial-value problem has a unique, absolutely continuous solution on the interval \([0,\epsilon]\) with \(\mathbf{x}(t)\in\mathcal{B}_\delta(\mathbf{a})\) for all \(t\in[0,\epsilon]\).

**7.** Consider the equation
\[
(P(x)u'(x))'=Q(x)u(x),\qquad x\in[0,1]. \tag{E}
\]
where \(Q\) is continuous and \(P\) is continuously differentiable and strictly positive on \([0,1]\). Show that if the solution to the initial-value problem for (E) with \(u(0)=0\) and \(u'(0)=1\) is strictly positive on the half-open interval \((0,1]\), then there exists a strictly positive solution to the second-order differential equation (E) (without boundary conditions at \(x=0\) or \(x=1\)).

**8.** Consider the variational problem
\[
\min\ \int_0^1\left(\frac{1}{2}u'(x)^2+e^{u(x)}\right)\,dx
\quad\text{subject to}\quad u\in\mathcal{H}_0^1.
\]
* (a) What is the first-order necessary optimality condition (Euler equation) for this variational problem?
* (b) Consider a uniform mesh \(x_k=kh\), where \(h=1/N\); let \(u_k\) denote an approximation to \(u(x_k)\). Of course, \(u_0=u_N=0\). Give a finite difference approximation in terms \(u_1,\ldots,u_{N-1}\) to the solution of the Euler equation.
* (c) Let \(\mathbf{F}(\mathbf{u})\) denote the finite difference system where \(\mathbf{u}=(u_1,u_2,\ldots,u_{N-1})^{\mathsf T}\in\mathbb{R}^{N-1}\), and let \(\mathbf{u}^*\) denote the vector formed by evaluating the solution of the Euler equation at the mesh points \(x_1,x_2,\ldots,x_{N-1}\). Obtain a bound for the components of \(\mathbf{F}(\mathbf{u}^*)\) in terms of the mesh spacing \(h\).

**9.** Consider the initial-value problem
\[
\dot{\mathbf{x}}(t)=\mathbf{A}(t)\mathbf{x}(t)+\mathbf{u}(t),\qquad \mathbf{x}(0)=0,
\]
where \(\mathbf{x}:[0,1]\to\mathbb{R}^n\) and \(\mathbf{A}\in\mathcal{L}^{\infty}([0,1];\mathbb{R}^{n\times n})\).
* (a) Assuming \(\mathbf{u}\in\mathcal{L}^2\), obtain a bound for the sup-norm of \(\mathbf{x}\) in terms of the \(\mathcal{L}^2\) norm of \(\mathbf{u}\).
* (b) Let \(\Omega:\mathcal{H}_0^1\to\mathbb{R}\) be defined by
  \[
  \Omega(h)=\frac{1}{2}\int_0^1 r^2(x)\,dx\qquad\text{where }r(x)=h'(x)+w(x)h(x).
  \]
  Show that there exists \(\beta>0\) such that
  \[
  \Omega(h)\geq\beta(\|h\|^2+\|h'\|^2)\qquad\text{for all }h\in\mathcal{H}_0^1,
  \]
  where \(\|\cdot\|\) is the \(\mathcal{L}^2\) norm.
* (c) Consider the quadratic programming problem
  \[
  \min\ \frac{1}{2}\mathbf{x}^{\mathsf T}\mathbf{R}\mathbf{x}+\mathbf{b}^{\mathsf T}\mathbf{x}
  \quad\text{subject to}\quad \mathbf{x}\in\mathcal{K},
  \]
  where \(\mathcal{K}\subset\mathbb{R}^n\) is a closed convex set and \(\mathbf{R}\in\mathbb{R}^{n\times n}\) is positive definite with smallest eigenvalue \(\alpha>0\). Show that the solutions \(\mathbf{u}_i\), \(i=1,2\), associated with \(\mathbf{b}=\mathbf{b}_i\), \(i=1,2\) respectively, satisfy
  \[
  \|\mathbf{u}_1-\mathbf{u}_2\|\leq \|\mathbf{b}_1-\mathbf{b}_2\|/\alpha.
  \]

**10.** Consider the following control problem:
\[
\min\ \int_0^1\left(\frac{1}{2}u^2(x)+y(x)\right)\,dx
\quad\text{subject to}\quad y'(x)=u(x),\quad y(0)=0,\quad u(x)\geq\ell(x),
\]
where \(\ell(x)\) is a given lower bound for the control \(u(x)\) at each \(x\in[0,1]\).
* (a) What is the first-order optimality condition (Pontryagin minimum principle) for this problem?
* (b) What is the solution of the control problem?
