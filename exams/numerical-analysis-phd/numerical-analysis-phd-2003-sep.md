# Numerical Analysis PhD exam, September 2003

*Do any 8 of the following 10 problems:*

**1.** This problem has three parts.
* (a) Let \(V\) be the space of all complex \(m\times n\) matrices endowed with any norm. Prove that its subset of full rank matrices is dense in \(V\).
* (b) Suppose \(A\) and \(B\) are square matrices.
    * i. If \(A\) is invertible, show that \(AB\) and \(BA\) are similar matrices (so their spectra coincide).
    * ii. How will you use Problem (1a) to conclude that the spectra of \(AB\) and \(BA\) coincide when nothing is known about the invertibility of \(A\) or \(B\)?
* (c) For all rectangular matrices \(A\in\mathbb C^{m\times n}\), \(B\in\mathbb C^{n\times m}\) (\(m\ne n\)), does the spectrum of \(AB\) and \(BA\) coincide?

**2.** Let \(A\in\mathbb C^{m\times m}\), and let \(E\in\mathbb C^{m\times m}\) be of rank \(k<m\). Suppose the matrix \(M=A+E\) is invertible. Consider GMRES applied to the preconditioned system
\[
M^{-1}Ax=M^{-1}b.
\]
Give a tight bound, independent of the starting guess, on the number of GMRES iterations needed to compute the exact solution \(x\) (ignoring roundoff). Your answer should be less than \(m\). Give clear reasons.

**3.** Let \(U\) be the upper triangular matrix obtained by applying Gaussian elimination with partial pivoting (the “\(PA=LU\)” factorization) to a matrix \(A\in\mathbb C^{m\times m}\). Show that the growth factor
\[
\rho=\frac{\max_{i,j}|U_{ij}|}{\max_{i,j}|A_{ij}|}
\]
satisfies
\[
\rho\le 2^{m-1}.
\]
Exhibit a matrix \(A\) for which the growth factor is \(2^{m-1}\).

**4.** This problem has two parts.
* (a) Suppose \(A=QR\) is a QR factorization of a symmetric tridiagonal \(A\). Which entries of \(R\) and \(Q\) are zero, in general?
* (b) State the (unshifted) QR iteration for eigenvalues. Show that if one iterate of the QR iteration is symmetric and tridiagonal, then the next one is also symmetric and tridiagonal.

**5.** Given \(\mathbf v\) and \(\mathbf w\in\mathbb R^n\), show that
\[
\mathbf v\mathbf w^{\mathsf T}+\mathbf w\mathbf v^{\mathsf T}
=\frac{\lVert\mathbf v\rVert\lVert\mathbf w\rVert}{2}
\left(\mathbf a\mathbf a^{\mathsf T}-\mathbf b\mathbf b^{\mathsf T}\right)
\]
\[
=\begin{bmatrix}
\dfrac{\mathbf a}{\lVert\mathbf a\rVert} & \big| & \dfrac{\mathbf b}{\lVert\mathbf b\rVert}
\end{bmatrix}
\begin{bmatrix}
\mathbf v^{\mathsf T}\mathbf w+\lVert\mathbf v\rVert\lVert\mathbf w\rVert & 0\\
0 & \mathbf v^{\mathsf T}\mathbf w-\lVert\mathbf v\rVert\lVert\mathbf w\rVert
\end{bmatrix}
\begin{bmatrix}
\dfrac{\mathbf a}{\lVert\mathbf a\rVert} & \big| & \dfrac{\mathbf b}{\lVert\mathbf b\rVert}
\end{bmatrix}^{\mathsf T},
\]
where
\[
\mathbf a=\frac{\mathbf v}{\lVert\mathbf v\rVert}+\frac{\mathbf w}{\lVert\mathbf w\rVert}
\quad\text{and}\quad
\mathbf b=\frac{\mathbf v}{\lVert\mathbf v\rVert}-\frac{\mathbf w}{\lVert\mathbf w\rVert}.
\]
What is \(\mathbf a^{\mathsf T}\mathbf b\)? What are the eigenvalues of \(\mathbf v\mathbf w^{\mathsf T}+\mathbf w\mathbf v^{\mathsf T}\)?

**6.** Show that \(x=1+\tan^{-1}(x)\) has a solution \(\alpha\). Find an interval \([a,b]\) containing \(\alpha\) such that for every \(x_0\in[a,b]\) the iteration
\[
x_{n+1}=1+\tan^{-1}(x_n)
\]
will converge to \(\alpha\).

**7.** Let \(x_0,\ldots,x_n\) be distinct real points. Let
\[
\{l_j(x)\}_{j=0,\ldots,n}
\]
be the Lagrange basis functions for these points. Prove that
\[
\sum_{j=0}^n l_j(x)=1
\]
for all \(x\).

**8.** Suppose you want to solve numerically the ode
\[
y'=f(x,y),\qquad y(0)=y_0.
\]
* (a) By applying the midpoint rule to the integral in the equation
  \[
  y(x_{n+1})=y(x_{n-1})+\int_{x_{n-1}}^{x_{n+1}}f(s,y(s))\,ds,
  \]
  derive the midpoint method for odes.
* (b) Find the order of the local truncation error for this method.
* (c) Determine if this method is stable or not.
* (d) Would this method be a good choice for a stiff system such as \(y'=-100y\)? Why or why not?

**9.** This problem has two parts.
* (a) Find the linear least squares approximation to \(f(x)=x^2\) on the interval \([0,2]\) by optimizing the least squares error over \(a\) and \(b\) in \(r^*(x)=ax+b\).
* (b) Find the first two orthonormal polynomials \(\phi_0(x),\phi_1(x)\) on \([0,2]\) (weight function \(w(x)=1\)). Use these to find the linear least squares approx to \(f(x)=x^2\), and check this result agrees with the previous problem.

**10.** Derive the one point Gaussian quadrature formula for
\[
I=\int_0^1 xf(x)\,dx\approx\sum_{j=1}^n w_jf(x_j)
\]
with weight function \(w(x)=x\). Find the system to solve for the two point Gaussian quadrature formula. (You do not need to solve the system)
