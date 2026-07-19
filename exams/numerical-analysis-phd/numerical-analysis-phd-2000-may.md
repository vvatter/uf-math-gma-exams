# Numerical Analysis, PhD exam, May 2000

**1.** This problem has two parts.
* (a) State the conditions under which a square matrix \(A\) can be decomposed into a form \(A=SDS^{-1}\), where \(D\) is diagonal.
* (b) Can
  \[
  A=\begin{pmatrix}5&1\\0&3\end{pmatrix}
  \]
  be diagonalized in the sense of (a)? Why?

**2.** This problem has three parts.
* (a) State the procedure for factoring a matrix \(A\) into a form \(A=LU\), where \(L\) is lower triangular, and \(U\) is upper triangular.
* (b) When can this type of decomposition be accomplished?
* (c) What is the computational advantage of having lower and upper triangular matrices. An explanation without specific computation counts is sufficient.

**3.** Assume that a symmetric matrix can be factored into a Cholesky decomposition \(A=LL^t\), where \(L\) is lower triangular.
* (a) Give an exact numerical method for finding the specific entries \(l_{i,j}\) of \(L=\{l_{i,j}\}\), where \(i=1:n\), and \(j=1:n\)?
* (b) What numerical problems would you anticipate with this method?

**4.** This problem has three parts.
* (a) Describe the method for factoring a matrix \(A\) into a form \(A=QR\), where \(Q\) is orthogonal, and \(R\) is upper triangular.
* (b) When can such a decomposition be accomplished?
* (c) What numerical “tricks” can be used to make it more stable?

**5.** This problem has three parts.
* (a) State the Gershgorin Circle Theorem.
* (b) Prove the first assertion, i.e. that the eigenvalues must be within one of the circles.
* (c) Let
  \[
  A=\begin{pmatrix}
  5&.01&.03\\
  .02&4&.01\\
  .03&-.01&4
  \end{pmatrix}.
  \]
  What can you say, from the Gershgorin Circle Theorem, about the eigenvalues of \(A\).

**6.** Suppose that a sequence is defined by \(x_{n+1}=g(x_n)\), where \(g\) is continuous, and \(g([a,b])\subset[a,b]\).
* (a) Show that there is a fixed point \(\alpha\in[a,b]\) such that \(g(\alpha)=\alpha\).
* (b) If in addition, \(|g'(x)|\leq k<1\) prove that this fixed point must be unique.
* (c) Under the above assumptions show that the sequence must converge to the unique fixed point.

**7.** This problem has three parts.
* (a) Give an exact expression for a Lagrange polynomial of degree \(n\), which would interpolate \(n+1\) given data points, \(f(x_k)\).
* (b) Describe the differences between Hermite polynomials and Lagrange polynomials.
* (c) Describe a procedure for using a limiting set of Lagrange polynomials, which interpolates a function at the points \(x_0,x_0+h,x_1,x_1+h,x_2,x_2+h,\ldots\) to construct the Hermite polynomial at the points \(x_0,x_1,x_2,\ldots\).

**8.** Given the Lagrange interpolation formula for \(f(x)\),
\[
f(x)=f(-h)\frac{x-h}{-2h}+f(h)\frac{x+h}{2h}+f''(\zeta(x))\frac{(x-h)(x+h)}{2!};
\]
* (a) Derive the trapezoid rule for \(\int_{-h}^{h}f(x)\,dx\),
* (b) Derive the error formula for the trapezoid rule, and
* (c) Describe the idea behind Gaussian Quadrature, and explain why it is more accurate than “traditional methods” such as trapezoid, Simpson’s, etc.

**9.** This problem has two parts.
* (a) Triple Recursion Formula. Let \(\{\phi_n(x)\}\) be an orthogonal family of polynomials on \([a,b]\), with weight function \(w(x)>0\). Then for \(n\geq1\), show that
  \[
  \phi_{n+1}(x)=(a_nx+b_n)\phi_n(x)-c_n\phi_{n-1}(x),
  \]
  for some constants \(a_n,b_n\), and \(c_n\). Hint: Let \(g(x)=\phi_{n+1}(x)-A_nx\phi_n(x)\), where \(A_n\) is a constant chosen so that \(g(x)\) has degree \(n\).
* (b) What can you say about the location of the zeros of a family of orthogonal polynomials on \([a,b]\)?

**10.** This problem has two parts.
* (a) Describe Euler’s method for solving the initial value problem \(y'=f(t,y)\), \(y(a)=y_0\).
* (b) Suppose that \(|f(t,x)-f(t,y)|\leq L|x-y|\), for a fixed constant \(L\), and all \(t\), \(x\) and \(y\). Suppose further that all solutions \(y(t)\) to the initial value problem described in (a) satisfy \(|y''(t)|\leq M\), for some constant \(M\). Then if \(w_i\) is the Euler solution to the initial value problem, prove that
  \[
  |y_{i+1}-w_{i+1}|\leq(1+hL)|y_i-w_i|+\frac{h^2M}{2}.
  \]
