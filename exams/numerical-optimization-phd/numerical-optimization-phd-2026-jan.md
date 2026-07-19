# Variational Analysis/Numerical Optimization PhD exam, January 2026

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

**2.** Given \(\mathbf{x}_0\in\mathbb{R}^n\), let \(0<\sigma<\mu<1\) be Wolfe line search parameters. In a Wolfe line search for minimizing \(f:\mathbb{R}^n\to\mathbb{R}\), \(\mathbf{x}_{k+1}=\mathbf{x}_k-s_k\mathbf{g}_k\), where \(\mathbf{g}_k=\nabla f(\mathbf{x}_k)^T\), and the stepsize \(s_k\) at step \(k\) is chosen so that the following two conditions hold:

W1. \(F(s_k)\leq F_L(s_k)\), where \(F(s)=f(\mathbf{x}_k-s\mathbf{g}_k)\) and \(F_L(s)=f(\mathbf{x}_k)-\sigma s\lVert\mathbf{g}_k\rVert^2\).

W2. \(F'(s_k)\geq\mu F'(0)=-\mu\lVert\mathbf{g}_k\rVert^2\).

If \(f\) is bounded from below, prove that there exists a stepsize \(s_k>0\) satisfying the Wolfe conditions. If \(f\) is twice continuously differentiable over the convex hull of the level set
\[
L=\{\mathbf{x}\in\mathbb{R}^n:f(\mathbf{x})\leq f(\mathbf{x}_0)\},
\]
and the largest eigenvalue of \(\nabla^2f\) is bounded by \(M<\infty\) over \(L\), then prove that the gradient \(\mathbf{g}_k\) converges to zero.

**3.** Suppose \(f:\mathcal{K}\to\mathbb{R}\), where \(\mathcal{K}\subset\mathbb{R}^n\) is a convex set.
* (a) If \(\mathbf{x}^*\) is a local minimizer of \(f\), then show that
  \[
  \nabla f(\mathbf{x}^*)(\mathbf{x}-\mathbf{x}^*)\geq 0\qquad\text{for all }\mathbf{x}\in\mathcal{K}. \tag{1}
  \]
* (b) If \(f\) is convex over \(\mathcal{K}\) and differentiable at some point \(\mathbf{x}^*\in\mathcal{K}\) where (1) holds, then show that \(\mathbf{x}^*\) is a global minimizer for \(f\) over \(\mathcal{K}\).
* (c) Consider the quadratic programming problem
  \[
  \min \frac{1}{2}\mathbf{x}^T\mathbf{A}\mathbf{x}-\mathbf{b}^T\mathbf{x}\qquad\text{subject to }\mathbf{x}\in\mathcal{K},
  \]
  where \(\mathcal{K}\subset\mathbb{R}^n\) is a closed convex set and \(\mathbf{A}\in\mathbb{R}^{n\times n}\) is positive definite with smallest eigenvalue \(\alpha>0\). Show that the solutions \(\mathbf{u}_i\), \(i=1,2\), associated with \(\mathbf{b}=\mathbf{b}_i\), \(i=1,2\), respectively, satisfy
  \[
  \lVert\mathbf{u}_1-\mathbf{u}_2\rVert\leq \lVert\mathbf{b}_1-\mathbf{b}_2\rVert/\alpha.
  \]

**4.** Prove the arithmetic-geometric mean inequality:
\[
\left(\prod_{i=1}^n x_i\right)^{1/n}\leq \frac{1}{n}\sum_{i=1}^n x_i
\]
where \(\mathbf{x}\geq 0\). Hint: change variables to \(\mathbf{y}=c\mathbf{x}\), where \(c\) is a scalar chosen so that the components of \(\mathbf{y}\) sum to 1. Note that maximizing the product of the \(y_i\) is equivalent to maximizing the log of the product since \(\log(t)\) is a monotone increasing function of \(t\) on \((0,\infty)\). Using duality, the max of the log of the product can be determined explicitly.

**5.** Consider the quadratic program
\[
\min \frac{1}{2}\mathbf{x}^T\mathbf{A}\mathbf{x}-\mathbf{b}^T\mathbf{x}\qquad\text{subject to }\mathbf{a}^T\mathbf{x}=c, \tag{2}
\]
where \(\mathbf{A}\) is a symmetric, positive definite matrix. The penalty approximation to (2) is
\[
\min \frac{1}{2}\mathbf{x}^T\mathbf{A}\mathbf{x}-\mathbf{b}^T\mathbf{x}+\frac{p}{2}(\mathbf{a}^T\mathbf{x}-c)^2, \tag{3}
\]
where \(p>0\) is the penalty parameter. Use the first-order optimality conditions for both (2) and (3) to obtain a bound for the distance between the solution of (2) and the solution of (3).

**6.** Let us consider the minimization problem
\[
\min I(y):=\int_0^1 f(y'(x),y(x),x)\,dx\qquad\text{subject to }y\in C_0^1, \tag{4}
\]
where \(f\) is a given continuously differentiable function. If \(y^*\) is a local minimizer of this problem, \(s\) is a scalar, \(h\in C_0^1\), then setting to zero the derivative of \(I(y^*+sh)\) evaluated at \(s=0\) yields the following first-order optimality condition:
\[
\int_0^1\left[\left(\frac{\partial f}{\partial y'}\right)^*(x)h'(x)+\left(\frac{\partial f}{\partial y}\right)^*(x)h(x)\right]dx=0 \tag{5}
\]
for all \(h\in C_0^1\), where
\[
\left(\frac{\partial f}{\partial y'}\right)^*(x):=\frac{\partial f}{\partial y'}(y^{*'}(x),y^*(x),x)
\quad\text{and}\quad
\left(\frac{\partial f}{\partial y}\right)^*(x):=\frac{\partial f}{\partial y}(y^{*'}(x),y^*(x),x).
\]
* (a) As a consequence of (5), show that
  \[
  \left(\frac{\partial f}{\partial y'}\right)^*\in C^1 \tag{6}
  \]
  and the Euler equation is satisfied. Note that it is only assumed that \(f\) is continuously differentiable; you should show that at a local minimizer of (4), the partial derivative in (6) is continuously differentiable.
* (b) For the special case
  \[
  f(y'(x),y(x),x)=\frac{1}{2}y'(x)^2-\varphi(x)y(x)^2,
  \]
  where \(\varphi\in C^k\) for some integer \(k\geq 0\), what does the observation in (a) imply concerning the smoothness of a minimizer \(y^*\) for (4)?

**7.** Suppose that \(P\) and \(Q\) are real-valued functions defined on the interval \([0,1]\), with \(P\) continuously differentiable and \(Q\) continuous. It is assumed that there exists \(\alpha>0\) such that \(P(x)\geq\alpha\) for all \(x\in[0,1]\). Define
\[
\text{[missing functional symbol]}(h):=\int_0^1 P(x)h'(x)^2+Q(x)h(x)^2\,dx.
\]
Suppose that \(\text{[missing functional symbol]}\) has the following property: There exists \(\text{[missing positive constant]}>0\) such that
\[
\text{[missing functional symbol]}(h)\geq \text{[missing positive constant]}\int_0^1 h'(x)^2+h(x)^2\,dx\qquad\text{for all }h\in H_0^1,
\]
where \(H_0^1\) is the space of functions with \(h'\) square integrable over \([0,1]\) and \(h(0)=h(1)=0\).

Prove the following: If \(u\) is a solution of the boundary-value problem
\[
\frac{d}{dx}(P(x)u'(x))=Q(x)u(x)\qquad\text{for all }x\in[0,a],\qquad u(0)=0=u(a),
\]
where \(a\in(0,1)\) is given, then \(u\) vanishes on the entire interval \([0,a]\). Hint: extend \(u\) from \([0,a]\) to \([0,1]\) by setting \(u(x)=0\) for \(x\in[a,1]\). Then integrate by parts to show that \(\text{[missing functional symbol]}(u)=0\).

**8.** Consider the variational problem
\[
\min \int_0^1\left(\frac{1}{2}u'(x)^2+e^{u(x)}\right)dx\qquad\text{subject to }u\in H_0^1. \tag{7}
\]
* (a) What is the first-order necessary optimality condition (Euler equation) for a local minimizer of this variational problem?
* (b) Show that if a minimizer of (7) exists, then it is unique.

**9.** Consider the initial-value problem
\[
\dot{\mathbf{x}}(t)=\mathbf{A}(t)\mathbf{x}(t)+\mathbf{u}(t),\qquad \mathbf{x}(0)=0,
\]
where \(\mathbf{x}:[0,1]\to\mathbb{R}^n\) and \(\mathbf{A}\in L^\infty([0,1];\mathbb{R}^{n\times n})\). Obtain a bound for the sup-norm of \(\mathbf{x}\) in terms of the \(L^2\) norm of \(\mathbf{u}\). Hint: Recall Grönwall’s inequality
\[
x(t)\leq\alpha(t)+L\int_0^t x(s)\,ds\text{ on }[0,a]\quad\Rightarrow\quad x(t)\leq\alpha(t)e^{Lt}\text{ on }[0,a],
\]
where \(\alpha\) is monotone nondecreasing.

**10.** Consider the following control problem:
\[
\min \int_0^1\left(\frac{1}{2}u^2(x)+y(x)\right)dx\qquad\text{subject to }y'(x)=u(x),\quad y(0)=0,\quad u(x)\geq\ell(x),
\]
where \(\ell(x)\) is a given lower bound for the control \(u(x)\) at each \(x\in[0,1]\).
* (a) What is the first-order optimality condition (Pontryagin minimum principle) for this problem?
* (b) What is the solution of the control problem?
