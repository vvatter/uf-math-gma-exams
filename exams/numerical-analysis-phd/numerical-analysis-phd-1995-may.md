# Numerical Analysis PhD exam, May 1995

**1.** Consider the linear system \(Ax=b\).
* (a) Suppose the columns of \(A\) are linearly independent. Derive the normal equation for the \(x\) that minimizes the 2-norm of the residual \(r=b-Ax\).
* (b) Suppose that the rows of \(A\) are linearly independent. Derive the normal equation for the solution to \(Ax=b\) that has the smallest 2-norm.
* (c) Using the singular value decomposition, obtain a formula for the least squares solution to \(Ax=b\). That is, if \(M\) denotes the set of all \(x\) for which the 2-norm of the residual is minimal, your formula should give the point in \(M\) with smallest 2-norm.

**2.** Suppose the columns of \(A\) are independent. Given the QR factorization of \(A\), give a formula for the distance from some given vector \(b\) to the space spanned by the columns of \(A\).

**3.** Verify the Woodbury formula
\[
(B-UV^T)^{-1}=B^{-1}+B^{-1}U(I-V^TB^{-1}U)^{-1}V^TB^{-1}.
\]

**4.** Explain how the singular value decomposition can be used to determine the rank of a matrix in the presence of rounding errors.

**5.** Derive a formula for the 2-norm of a matrix in terms of its singular values.

**6.** Let \(f\) be an \((n+1)\)-times continuously differentiable function on the interval \([a,b]\), and let \(a\leq x_0<x_1<\cdots<x_n\leq b\). Let \(P_n\) be the unique polynomial interpolant of degree at most \(n\), interpolating the data \((x_k,f(x_k))\), \(k=0,1,\ldots,n\). Prove that there exists a point \(\xi\in[a,b]\) such that
\[
f(x)-P_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{k=0}^n(x-x_k)
\]
for all \(x\in[a,b]\).

**7.** Let \(f\) be a twice continuously differentiable function on the interval \([a,b]\), and \(x_0,x_1,\ldots,x_N\) be an equi-spaced partition of \([a,b]\), with step size \(h\) and \(x_0=a\). Assume that only the values \(f(x_k)\), \(k=0,1,\ldots,N\), are known.
* (a) State the trapezoidal rule \(T(f,N)\) to approximate \(\int_a^b f(x)\,dx\).
* (b) Prove that
  \[
  \int_a^b f(x)\,dx-T(f,N)=-\frac{(b-a)^3}{12N^2}f''(\xi)
  \]
  for some point \(\xi\in(a,b)\).

**8.** Let \(f\) be a twice continuously differentiable, \(2\pi\)-periodic, function on \(\mathbb{R}\) and consider the problem of computing the Fourier coefficients
\[
\tag{8.1} c_n=\frac{1}{2\pi}\int_0^{2\pi}e^{-inx}f(x)\,dx
\]
by using the values \(f_k=f(2k\pi/N)\) for \(k=0,1,\ldots,N-1\).
* (a) Define the discrete Fourier transform \(\{\hat f_n\}\) of the sequence \(\{f_k\}\).
* (b) By applying the trapezoidal rule to the integral in (8.1), show that \(c_n\) can be approximated by \(\hat f_n\).
* (c) By performing an analysis of the error in the approximation in (b), show that \(\hat f_n\) is a poor approximation of \(c_n\). Hint: Investigate behavior of error as \(N\to\infty\).
* (d) Outline a method of obtaining a better approximation \(\tilde c_n\) of \(c_n\). (You do not need to actually find a formula for this \(\tilde c_n\).) For the \(\tilde c_n\) obtained by your method, define
  \[
  \lVert\tilde c-c\rVert_\infty=\max\{|\tilde c_n-c_n|,\ n=1,2,\ldots\}.
  \]
  Find the order of convergence of \(\lVert\tilde c-c\rVert_\infty\) as \(N\to\infty\).

**9.** Give a careful statement of the contraction mapping theorem for functions defined on subsets of \(\mathbb{R}^n\) into \(\mathbb{R}^n\).
* (a) Since it is usually not easy to demonstrate the contraction property in particular examples, state a stronger condition which implies the contraction property.
* (b) Discuss the relative merits of determining the fixed points of a function \(\varphi:\mathbb{R}\to\mathbb{R}\) by the iterations:
  \[
  \text{(FP)}\qquad x_{k+1}=\varphi(x_k)
  \]
  \[
  \text{(DFP)}\qquad x_{k+1}=\varphi(\varphi(x_k))
  \]
  \[
  \text{(STEF)}\qquad x_{k+1}=x_k-\frac{(\varphi(x_k)-x_k)^2}{\varphi(\varphi(x_k))-2\varphi(x_k)+x_k}.
  \]

**10.** Let \(A\) be a real, positive definite \(n\times n\) matrix and \(b\) be an \(n\times1\) vector.
* (a) Derive the steepest descent algorithm for approximating the true solution \(x\) of \(Ax=b\), by a sequence of iterates \(\{x_k\}\).
* (b) Define the real-valued function \(h\) on \(\mathbb{R}^n\) by
  \[
  h(x)=(Ax-b)^TA^{-1}(Ax-b)
  \]
  and show that
  \[
  h(x_{k+1})\leq(1-c(A)^{-1})^2h(x_k)
  \]
  where \(c(A)\) is the condition number of the matrix \(A\).
