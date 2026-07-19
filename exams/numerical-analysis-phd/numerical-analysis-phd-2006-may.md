# Numerical Analysis, PhD exam, May 2006

*Do any eight of the ten problems below.*

**1.** Let \(x_0,\ldots,x_n\) be distinct real points. Let \(\{l_j(x)\}_{j=0,\ldots,n}\) be the Lagrange basis functions for these points. Prove that
\[
\sum_{j=0}^n l_j(x)=1
\]
for all \(x\).

**2.** Suppose you want to solve numerically the ode
\[
y'=f(x,y),\qquad y(0)=y_0.
\]
* (a) By applying the midpoint rule to the integral in the equation
  \[
  y(x_{n+1})=y(x_{n-1})+\int_{x_{n-1}}^{x_{n+1}}f(s,y(s))\,ds,
  \]
  derive the midpoint method for odes.
* (b) Find the order of the local truncation error for this method.
* (c) Determine if this method is strongly stable, weakly stable or unstable.

**3.** Given \(x_0,x_1\) and smooth \(f(x)\), give a divided difference type formula for the cubic polynomial which satisfies:
\[
\begin{aligned}
p(x_0)&=f(x_0),\\
p'(x_0)&=f'(x_0),\\
p''(x_0)&=f''(x_0),\\
p(x_1)&=f(x_1).
\end{aligned}
\]
Also give a divided difference type error formula for \(f(x)-p(x)\).

**4.** This problem has two parts.
* (a) Find the linear least squares approximation to \(f(x)=x^2\) on the interval \([0,2]\) by optimizing the least squares error over \(a\) and \(b\) in \(r^*(x)=ax+b\).
* (b) Find the first two orthonormal polynomials \(\phi_0(x),\phi_1(x)\) on \([0,2]\) (weight function \(w(x)=1\)). Use these to find the linear least squares approx to \(f(x)=x^2\), and check this result agrees with the previous problem.

**5.** Consider the root-finding iteration defined by
\[
x_{n+1}=x_n-f(x_n)\left[\frac{f(x_n)}{f(x_n+f(x_n))-f(x_n)}\right].
\]
This is called Steffensen’s method. Show that the method converges quadratically when applied to \(f(x)=x^2-a\). (You may assume \(x_0\) is close enough to the root.)

**6.** This problem has three parts.
* (a) Evaluate the \(p\)-norm of a diagonal matrix, \(1\leq p\leq\infty\).
* (b) Evaluate the \(p\)-norm of a rank one matrix \(\mathbf u\mathbf v^*\), \(1\leq p\leq\infty\), \(\mathbf u\in\mathbb C^m\) and \(\mathbf v\in\mathbb C^n\).
* (c) Suppose \(\mathbf A\in\mathbb C^{m\times n}\) can be expressed
  \[
  \mathbf A=\sum_{k=1}^r\sigma_k\mathbf u_k\mathbf v_k^*,
  \]
  where the vectors \(\{\mathbf u_k:1\leq k\leq r\}\) and \(\{\mathbf v_k:1\leq k\leq r\}\) are orthonormal. What is \(\|\mathbf A\|_2\)?

**7.** This problem has two parts.
* (a) Given \(\mathbf A\in\mathbb C^{m\times n}\), show that \(\mathbf A^*\mathbf A\) is positive semidefinite and \(\mathbf A^*\mathbf A\) is positive definite if and only if the columns of \(\mathbf A\) are linearly independent.
* (b) If \(\mathbf A\) is a Hermitian, positive semidefinite matrix, show that the diagonal contains the largest in magnitude element of \(\mathbf A\). Hint: show that \(\lvert a_{ij}\rvert\leq\max\{\lvert a_{ii}\rvert,\lvert a_{jj}\rvert\}\).

**8.** Let \(\mathbf A\in\mathbb C^{n\times n}\) be nonsingular. Show that \(\mathbf A\) has an LU factorization if and only if for each \(k\) with \(1\leq k\leq n\), the upper-left \(k\times k\) block \(\mathbf A_{1:k,1:k}\) is nonsingular. Prove that this LU factorization is unique.

**9.** Consider the Arnoldi iteration on the Krylov spaces \(\mathcal K_k=\operatorname{span}\{\mathbf b,\mathbf A\mathbf b,\mathbf A^2\mathbf b,\ldots,\mathbf A^{k-1}\mathbf b\}\) for some \(\mathbf b\in\mathbb C^m\) and \(\mathbf A\in\mathbb C^{m\times m}\) (given at side). Suppose the algorithm proceeds without breakdown until for some \(n<m\), it encounters \(h_{n+1,n}=0\).

Algorithm 1 (Arnoldi iteration)

(a) Set \(\mathbf q_1=\mathbf b/\|\mathbf b\|_2\).

(b) For \(n=1,2,3,\ldots\) do:

i. Set \(\mathbf v=\mathbf A\mathbf q_n\).

ii. For \(j=1,2,\ldots,n\) do:

A. Set \(h_{jn}=\mathbf q_j^*\mathbf v\).

B. Replace \(\mathbf v\) by \(\mathbf v-h_{jn}\mathbf q_j\).

iii. Set \(h_{n+1,n}=\|\mathbf v\|_2\).

iv. Set \(\mathbf q_{n+1}=\mathbf v/h_{n+1,n}\).
* (a) Show that \(\mathcal K_n\) is an invariant subspace of \(\mathbf A\), i.e., \(\mathbf A\mathcal K_n\subseteq\mathcal K_n\).
* (b) Show that \(\mathcal K_n=\mathcal K_{n+1}=\mathcal K_{n+2}=\cdots\).
* (c) Let \(\mathbf H_n\) be the \(n\times n\) Hessenberg matrix whose \(ij\)-th entry (\(i\leq j+1\)) is the number \(h_{ij}\) computed in the algorithm. Show that each eigenvalue of \(\mathbf H_n\) is an eigenvalue of \(\mathbf A\).

**10.** Consider an invertible linear system \(\mathbf A\mathbf x=\mathbf b\) and a perturbation \((\mathbf A+\delta\mathbf A)(\mathbf x+\delta\mathbf x)=\mathbf b\). Assuming \(\|\mathbf A^{-1}\|\|\delta\mathbf A\|<1\), derive the condition estimate
\[
\frac{\|\delta\mathbf x\|}{\|\mathbf x\|}\leq\left(\frac{\|\mathbf A\|\|\mathbf A^{-1}\|}{1-\|\mathbf A^{-1}\|\|\delta\mathbf A\|}\right)\frac{\|\delta\mathbf A\|}{\|\mathbf A\|}.
\]
For given \(\mathbf A\) and \(\mathbf x\) and for the 2-norm, what choice of \(\delta\mathbf A\) yields the following equality:
\[
\|\mathbf A^{-1}\delta\mathbf A\mathbf x\|=\|\mathbf A^{-1}\|\|\delta\mathbf A\|\|\mathbf x\|?
\]
