# Numerical Analysis, PhD exam, May 2008

*Answer any 8 questions.*

**1.** Prove that any matrix has a singular value decomposition.

**2.** Suppose \(A\) and \(B\) are square matrices such that \(AB\) is normal. Prove that \(\lVert AB\rVert_2\leq \lVert BA\rVert\) for any matrix norm \(\lVert\cdot\rVert\) induced by a vector norm (where \(\lVert\cdot\rVert_2\) denotes the spectral norm).

**3.** Let the singular values of any matrix \(M\) in \(\mathbb{C}^{m\times n}\) be denoted by \(\sigma_1(M)\geq \sigma_2(M)\geq\cdots\geq\sigma_q(M)\) with \(q=\min(m,n)\). Prove that if \(A\) and \(B\) are two matrices in \(\mathbb{C}^{m\times n}\), then
\[
\sigma_{i+j-1}(A+B)\leq \sigma_i(A)+\sigma_j(B),
\]
for all \(i,j=1,2,\ldots,q\) and \(i+j\leq q\).

**4.** Let \(T\) be any square matrix and let \(\lVert\cdot\rVert\) denote any induced norm. Prove that
\[
\lim_{n\to\infty}\lVert T^n\rVert^{1/n}
\]
exists and equals
\[
\inf_{n=1,2,\ldots}\lVert T^n\rVert^{1/n}.
\]

**5.** Suppose \(\widetilde Q\) and \(\widetilde R\) are the Householder QR factors of a well conditioned square nonsingular matrix \(A=QR\), computed in a floating point number system of machine precision \(\varepsilon_{\mathrm{mac}}\).
* (a) State an algorithm in which you use \(\widetilde Q\) and \(\widetilde R\) to compute an approximation \(\widetilde x\) to the solution \(x\) of \(Ax=b\).
* (b) Let \(\lVert\cdot\rVert\) denote any vector norm as well as the matrix norm induced by it. Out of the following three statements A–C, pick one that is true, and prove it. (You may use the backward stability results that you know of without proof.)
    * A: \(\lVert\widetilde Q-Q\rVert=O(\varepsilon_{\mathrm{mac}})\).
    * B: \(\dfrac{\lVert\widetilde R-R\rVert}{\lVert R\rVert}=O(\varepsilon_{\mathrm{mac}})\).
    * C: \(\dfrac{\lVert\widetilde x-x\rVert}{\lVert x\rVert}=O(\varepsilon_{\mathrm{mac}})\).

**6.** Let \(L_nf\) denote the Lagrange interpolant of \(f\in C^{n+1}[a,b]\) based on an equispaced partition \(a=x_0<x_1<\cdots<x_{n-1}<x_n=b\).
* (a) State an error formula for \(f(x)-L_nf(x)\) in terms of Newton’s divided differences.
* (b) Use \(L_nf\) to determine an approximation of the integral
  \[
  \int_a^b f(x)\,dx
  \]
  by a sum
  \[
  \sum_{k=0}^n\omega_k f(x_k),
  \]
  and find a formula for \(\omega_k\) in its simplest form.
* (c) Show that \(\displaystyle\sum_{k=0}^n\omega_k=b-a\).

**7.** Consider the solution of the equation \(\tan x=4x/\pi\) in the interval \([0,\pi/2]\) (what is it?), and how it perturbs due to errors in evaluating the coefficient \(4/\pi\). Using Taylor expansion, give two expressions approximating the difference between the roots of \(\tan x-4x/\pi=0\) and \(\tan x-(\varepsilon+4/\pi)x=0\) in the interval \([0,\pi/2]\):
* (a) one in terms of a linear function of \(\varepsilon\), and
* (b) another in terms of a quadratic function of \(\varepsilon\).

**8.** Let \(a=x_0<x_1<\cdots<x_{n-1}<x_n=b\) be a partition \(P\) of the interval \([a,b]\) and \(f\in C^2[a,b]\). Define what is meant by saying that
* (a) \(S_c\) is the “natural” cubic spline on \(P\) interpolating \(f\), and
* (b) \(S_n\) is the “not-a-knot” cubic spline on \(P\) interpolating \(f\).
* (c) Show that \(S_n\) is a cubic polynomial on \([x_0,x_2]\).

**9.** Let \(x_0,x_1,\ldots,x_n\) be distinct points in a finite interval \([a,b]\) and \(f\in C^1[a,b]\). Show that for any given \(\varepsilon>0\) there exists a polynomial \(p\) such that \(\lVert f-p\rVert_\infty<\varepsilon\) and \(p(x_i)=f(x_i)\) for all \(i=0,1,\ldots,n\) (where \(\lVert\cdot\rVert_\infty\) denotes the \(L^\infty(a,b)\)-norm).

**10.** Let \(x_m\) and \(x_{m+1}\) be two successive (complex) iterates when Newton’s method is applied to a polynomial \(p(z)\) of degree \(n\). Prove that there is a zero of \(p(z)\) in the disk
\[
\{z\in\mathbb{C}:|z-x_m|\leq n|x_{m+1}-x_m|\}.
\]
