# Numerical Analysis, PhD exam, September 2008

*Answer any 8 questions.*

**1.** Let \(M=\begin{bmatrix}A&B^t\\B&C\end{bmatrix}\) be real symmetric and positive definite matrix. Let \(S=C-BA^{-1}B^t\) be the Schur complement. Prove that \(S\) is symmetric and positive definite.

**2.** Suppose \(\widetilde Q\) and \(\widetilde R\) are the Householder QR factors of a well conditioned square nonsingular matrix \(A=QR\), computed in a floating point number system of machine precision \(\varepsilon_{\mathrm{mac}}\).
* (a) State an algorithm in which you use \(\widetilde Q\) and \(\widetilde R\) to compute an approximation \(\widetilde x\) to the solution \(x\) of \(Ax=b\).
* (b) Let \(\|\cdot\|\) denote any vector norm as well the matrix norm induced by it. Out of the following three statements A–C, pick one that is true, and prove it. (You may use the backward stability results that you know of without proof.)
    * A: \(\|\widetilde Q-Q\|=O(\varepsilon_{\mathrm{mac}})\).
    * B: \(\dfrac{\|\widetilde R-R\|}{\|R\|}=O(\varepsilon_{\mathrm{mac}})\).
    * C: \(\dfrac{\|\widetilde x-x\|}{\|x\|}=O(\varepsilon_{\mathrm{mac}})\).

**3.** Show that if \(P\) and \(Q\) be Hermitian positive definite matrices satisfying \(x^*Px\leq x^*Qx\), for all \(x\in\mathbb C^n\), then \(\|P\|_F\leq\|Q\|_F\).

**4.** Describe the finite element method for solving \(-\Delta u=f\) on \(\Omega=(0,1)\times(0,1)\) with zero Dirichlet boundary conditions on the boundary \(\partial\Omega\). Consider a subdivision of \(\Omega\) by right triangles whose orthogonal edges are of length \(h\). Prove that there is a \(C>0\) independent of \(h\) such that the spectral condition number of the stiffness matrix \(A\) satisfies \(\kappa(A)\leq Ch^{-2}\). (If you cannot prove this with the stated assumptions, you may try after placing further assumptions on the mesh.)

**5.** State the (unshifted) QR iteration for eigenvalues. Show that if one iterate of the QR iteration is symmetric and tridiagonal, then the next one is also symmetric and tridiagonal.

**6.** Let \(x_0,x_1,\ldots,x_n\) be distinct points in a finite interval \([a,b]\) and \(f\in C^1[a,b]\). Show that for any given \(\varepsilon>0\) there exists a polynomial \(p\) such that \(\|f-p\|_\infty<\varepsilon\) and \(p(x_i)=f(x_i)\) for all \(i=0,1,\ldots,n\) (where \(\|\cdot\|_\infty\) denotes the \(L^\infty(a,b)\)-norm).

**7.** Let \(\widehat f(s)\) be the continuous Fourier transform of \(f(t)\in L^2[-\infty,\infty]\). Suppose further that \(\widehat f(s)=0\) for \(|s|>\pi\). Derive the interpolation formula
\[
f(t)=\sum_{k=-\infty}^{\infty}f(k)\frac{\sin(\pi(t-k))}{\pi(t-k)}.
\]

**8.** Let \(L_n(f)\) be the Lagrange polynomial interpolating a function \(f\) at nodes \(a=x_0<x_1<\cdots<x_n=b\).
* (a) Give the formula for \(L_n(f)\).
* (b) Prove that there is a unique polynomial interpolating \(f\) at the nodes.
* (c) State and prove the formula for the error \(f(x)-L_n(f)(x)\) when \(f\in C^{n+1}[a,b]\),

**9.** Let \(S_n(f)\) be the Simpson’s rule approximation to \(\int_{x_0}^{x_2}f(x)\,dx\), with three nodes \(x_0<x_2\) and \(x_1=.5(x_0+x_2)\).
* (a) State Simpson’s rule and prove that it is exact for cubic polynomials.
* (b) Derive a formula for the error in Simpson’s rule by exploiting the formula for the error in Lagrange interpolation.

**10.** Let \(p>0\) and \(x=\sqrt{p+\sqrt{p+\sqrt{p+\cdots}}}\), where all the square roots are positive. Design a fixed point iteration \(x_{n+1}=F(x_n)\) with some \(F\) which has \(x\) as a fixed point. Prove that the fixed point iteration converges for all choices of initial guesses greater than \(-p+1/4\).
