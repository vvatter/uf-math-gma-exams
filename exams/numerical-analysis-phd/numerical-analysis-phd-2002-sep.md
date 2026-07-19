# Numerical Analysis, PhD exam, September 2002

*Do any 8 of the following 10 problems.*

**1.** Consider a function \(f(x)\in C^2(\mathbb R)\) that satisfies the following properties:

Using \(x_0=5/2\), do we know that Newton’s method will converge? If so, how many iterations are required to ensure \(10^{-4}\) accuracy?
* (a) There exists a unique root \(\alpha\in[2,3]\).
* (b) For any real \(x\), \(f'(x)\geq 3\) and \(0\leq f''(x)\leq 5\).

**2.** Let \(x_0,\ldots,x_n\) be distinct real points. Let
\[
P_n(x)=\sum_{j=0}^n c_j e^{jx}.
\]
For given data \(y_0,\ldots,y_n\), show that there exists a unique choice of \(c_0,\ldots,c_n\) such that
\[
P_n(x_i)=y_i.
\]
(Hint: Reduce to an ordinary interpolation problem)

**3.** Suppose you want to solve numerically the ode
\[
y'=f(x,y),\qquad y(0)=y_0.
\]
* (a) By applying Simpson’s rule to the integral in the equation
  \[
  y(x_{n+1})=y(x_{n-1})+\int_{x_{n-1}}^{x_{n+1}}f(s,y(s))\,ds,\qquad x_n=nh,\quad n=1,2,\ldots,
  \]
  derive the multistep Simpson’s method for odes.
* (b) Find the order of the local truncation error for this method.
* (c) Determine if this method is stable or not.

**4.** This problem has two parts.
* (a) Find the linear least squares approximation to \(f(x)=x^3\) on the interval \([0,2]\) by optimizing the least squares error over \(a\) and \(b\) in \(r^*(x)=ax+b\).
* (b) Find the first two orthonormal polynomials \(\phi_0(x),\phi_1(x)\) on \([0,2]\) (weight function \(w(x)=1\)). Use these to find the linear least squares approx to \(f(x)=x^3\), and check this result agrees with the previous problem.

**5.** This problem has two parts.
* (a) Let \(\mathbf A\in\mathbb C^{m\times n}\) with \(m\geq n\). Prove that \(\mathbf A^*\mathbf A\) is nonsingular if and only if \(\mathbf A\) has full rank.
* (b) Let the \(\mathbf a_1,\mathbf a_2,\ldots,\mathbf a_\ell\in\mathbb C^m\) be linearly independent vectors. Form an \(m\times\ell\) matrix \(\mathbf A\) whose \(i\)-th column is \(\mathbf a_i\). Prove that the matrix of the orthogonal projection onto span of \(\mathbf a_1,\mathbf a_2,\ldots,\mathbf a_\ell\) is
  \[
  \mathbf A(\mathbf A^*\mathbf A)^{-1}\mathbf A^*.
  \]

**6.** Let \(p\) and \(q\) be positive real numbers such that \(1/p+1/q=1\), and let \(\|\cdot\|_p\) for \(1\leq p\leq\infty\) denote the norm on \(m\times n\) matrices induced by the \(\ell^p\)-norm on vectors in \(\mathbb C^m\) and \(\mathbb C^n\).
* (a) For any matrix, show that \(\|\mathbf A\|_p=\|\mathbf A^{\mathsf T}\|_q\). (Hint: use the Hölder inequality for vectors).
* (b) Let \(\rho(\mathbf M)\) denote the spectral radius of any square matrix \(\mathbf M\). Prove that \(\rho(\mathbf M)\leq\|\mathbf M\|\) for any norm \(\|\cdot\|\) induced by a vector norm.
* (c) Show that
  \[
  \|\mathbf A\|_2\leq\sqrt{\|\mathbf A\|_p\|\mathbf A^{\mathsf T}\|_q}.
  \]

**7.** This problem has two parts.
* (a) Show that Jacobi’s iteration applied to \(\mathbf A\mathbf x=\mathbf b\) always converges when the matrix is row diagonally dominant.
* (b) Show that the Gauss–Seidel iteration applied to \(\mathbf A\mathbf x=\mathbf b\) always converges when the matrix is row diagonally dominant.

**8.** If \(\mathbf A\) is a square matrix, then \(e^{\mathbf A}\) is the matrix obtained by forming the Taylor expansion of \(e^x\) and replacing \(x\) by \(\mathbf A\). For any square matrix, show that \(\det e^{\mathbf A}\) is the product of the exponential of each eigenvalue of \(\mathbf A\).

**9.** If \(\mathbf A\) and \(\mathbf B\) are square invertible matrices and \(\mathbf u\) and \(\mathbf v\) are vectors with \(\mathbf A=\mathbf B-\mathbf u\mathbf v^{\mathsf T}\), obtain a formula for the scalar \(\alpha\) in the following identity relating the inverses of \(\mathbf A\) and \(\mathbf B\):
\[
\mathbf A^{-1}=\mathbf B^{-1}+\alpha\mathbf B^{-1}\mathbf u\mathbf v^{\mathsf T}\mathbf B^{-1}.
\]

**10.** Let \(\mathbf A\) be an \(n\times n\) Hermitian positive definite matrix. Define
\[
\|\mathbf y\|_{\mathbf A}=(\mathbf y^*\mathbf A\mathbf y)^{1/2},\qquad \text{for all }\mathbf y\in\mathbb C^n.
\]
Consider the following iterative method for solving \(\mathbf A\mathbf x=\mathbf b\):
\[
\mathbf x_{i+1}=\mathbf x_i+\alpha_i\mathbf r_i,\qquad \text{where }\mathbf r_i=\mathbf b-\mathbf A\mathbf x_i,\quad \text{and}\quad \alpha_i=\frac{\mathbf r_i^*\mathbf r_i}{\mathbf r_i^*\mathbf A\mathbf r_i}. \tag{1}
\]
Let error at the \(i\)-th step be \(\mathbf e_i=\mathbf x-\mathbf x_i\).
* (a) Prove that
  \[
  \|\mathbf e_{i+1}\|_{\mathbf A}=\inf_{\alpha\in\mathbb R}\|\mathbf e_i-\alpha\mathbf r_i\|_{\mathbf A}.
  \]
* (b) Use Problem (10a) to prove the following convergence rate estimate:
  \[
  \|\mathbf e_{i+1}\|_{\mathbf A}\leq\left(\frac{\kappa(\mathbf A)-1}{\kappa(\mathbf A)+1}\right)\|\mathbf e_i\|_{\mathbf A},
  \]
  where \(\kappa(\mathbf A)\) denotes the spectral condition number of \(\mathbf A\).
