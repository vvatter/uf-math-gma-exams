# Numerical Analysis, PhD exam, May 1998

*Do any 8 of the following 10 problems.*

**1.** This problem has four parts.
* (1) Give a careful description of a Householder transformation.
* (2) Describe how Householder transformations can be used to bidiagonalize a \(5\times 5\) matrix.
* (3) Describe the \(QR\) Iteration Algorithm with shift \(\mu\).
* (4) Describe how the \(QR\) Iteration is used to compute the \(SVD\).

**2.** This problem has two parts.
* (1) Give a careful statement and proof of Gershgorin’s Circle Theorem.
* (2) Determine whether or not the matrix
  \[
  A=\begin{pmatrix}
  -3&1&1\\
  -1&-4&2\\
  -1&0&-2
  \end{pmatrix}
  \]
  has the property that each eigenvalue has negative real part.

**3.** Suppose it is known that every eigenvalue of a matrix \(A\) is real. Suppose the power method with shifts is to be used to approximate the largest eigenvalue of \(A\). Explain how Gershgorin’s method can be used to aid in the choice of reasonable shifts.

**4.** This problem has three parts.
* (1) Give a careful statement of the \(LU\) factorization theorem.
* (2) Give a careful statement and proof of the Cholesky Factorization Theorem.
* (3) Find (if possible) a Cholesky factorization of the matrix
  \[
  A=\begin{pmatrix}
  2&4&6\\
  4&7&8\\
  6&8&5
  \end{pmatrix}.
  \]

**5.** This problem has two parts.
* (1) Give a careful statement of the Sturm interlacing property for symmetric matrices.
* (2) Determine whether or not the matrix
  \[
  A=\begin{pmatrix}
  1&1&0\\
  1&1&1\\
  0&1&2
  \end{pmatrix}
  \]
  has any negative eigenvalues.

**6.** This problem has four parts.
* (1) Give a careful statement of the Pythagorean Theorem property for clamped cubic splines.
* (2) Give a careful statement of the integral minimization property for clamped cubic splines.
* (3) If \(s_n(x)\) denotes the clamped cubic spline interpolant for a function \(f(x)\) at the knots \((x_0,y_0),(x_1,y_1),\ldots,(x_n,y_n)\), then give a precise statement for the error between \(s_n(x)\) and \(f(x)\).
* (4) If \(s_n(x)\) denotes the clamped cubic spline interpolant for a function \(f(x)\) at the knots \((x_0,y_0),(x_1,y_1),\ldots,(x_n,y_n)\), then give a precise statement for the error between \(s_n''(x)\) and \(f''(x)\).

**7.** Let \(f(x)\) be a real valued function on \(\mathbb{R}\) with a continuous 3rd derivative at each point. Assume also that \(f(x)\) has a simple root at \(x=p\).
* (1) Show: If Newton’s method is used to approximate \(p\), then there is a \(\delta>0\) with the property that the convergence rate to \(p\) is 2nd order on the interval \([p-\delta,p+\delta]\).
* (2) Approximate a solution to the following nonlinear system using Newton’s method. (Please don’t iterate—just set up the procedure for the initial guess \(x_0=(1,1,1)^t\).)
  \[
  \begin{aligned}
  3x_1-\cos(x_2x_3)-0.5&=0,\\
  x_1^2-625x_2^2&=0,\\
  e^{-x_1x_2}+20x_3+9&=0.
  \end{aligned}
  \]
* (3) What happens to the iteration process if the initial guess is changed to \(x_0=(1,0,1)^t\)?

**8.** Consider the method \(y_{k+1}=y_{k-1}+\frac{h}{2}(3f_k+f_{k-1})\) for solving the initial value equation \(y'=f(x,y)\), \(y(0)=\alpha\).
* (1) If the method is applied to the equation \(y'=-10y\), \(y(0)=4\), then is there a step size \(h\) such that the global discretization error converges to zero as \(k\to\infty\)? Explain your answer.
* (2) Consider the equation \(y'=xy(y-2)\) where \(y(0)=2\). Is this an ill-posed or a well-posed problem? Explain your answer. (Note that the general solution is \(y(x)=\frac{2y_0}{y_0+(2-y_0)e^{x^2}}\), when \(y(0)=y_0\).)

**9.** This problem has three parts.
* (1) Give a careful statement of the Contraction Mapping Theorem.
* (2) Outline a proof of the Contraction Mapping Theorem.
* (3) Indicate how Aitken’s method can be used to accelerate convergence.

**10.** This problem has two parts.
* (1) Explain Romberg’s technique for numerical approximation of an integral.
* (2) Give a brief justification for the method.
