# Numerical Analysis, PhD exam, January 2010

*Answer any 8 questions.*

**1.** Prove that a projector is normal if and only if it is self-adjoint.

**2.** Let \(A \in \mathbb{R}^{N\times N}\) and \(b \in \mathbb{R}^N\). Consider the following iteration for solving \(Ax=b\), that computes \(x_{n+1}\), given \(x_n \in \mathbb{R}^N\), as follows (in \(m\) intermediate steps): Setting \(x_{n+1}^{(0)}=x_n\), for \(\ell=1,2,\ldots,m\), compute \(x_{n+1}^{(\ell)}=x_{n+1}^{(\ell-1)}+\tau_\ell(b-Ax_{n+1}^{(\ell-1)})\). Then, define \(x_{n+1}=x_{n+1}^{(m)}\). There is a linear operator \(E\) such that \(x_{n+1}-x=E(x_n-x)\). Give a formula for \(E\). Suppose \(A\) is Hermitian and positive definite with spectral condition number \(\kappa\). Prove that there are real values of the \(m\) parameters \(\tau_\ell\) such that
\[
\rho(E)\leq 2\left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^m.
\]

**3.** Suppose \(A\) and \(B\) are square matrices such that \(AB\) is normal. Prove that \(\lVert AB\rVert_2\leq \lVert BA\rVert\). (We use \(\lVert\cdot\rVert_2\) to denote the spectral norm and \(\lVert\cdot\rVert\) to denote any induced matrix norm.)

**4.** Let \(A\in\mathbb{C}^{m\times m}\), and \(a_j\) be its \(j\)-th column. Prove that
\[
|\det A|\leq \prod_{j=1}^m\lVert a_j\rVert_2.
\]

**5.** Suppose \(A\) is a Hermitian positive definite matrix split into \(A=C+C^*+D\) where \(D\) is also Hermitian positive definite. Show that \(B=C+\omega^{-1}D\) is invertible. Consider the iteration \(x_{n+1}=x_n+B^{-1}(b-Ax_n)\), with any initial iterate \(x_0\). Prove that \(x_n\) converges to \(x=A^{-1}b\) whenever \(0<\omega<2\).

**6.** Let \(x_0,x_1,\ldots,x_n\) be distinct points in a finite interval \([a,b]\) and \(f\in C^1[a,b]\). Show that for any given \(\varepsilon>0\) there exists a polynomial \(p\) such that \(\lVert f-p\rVert_\infty<\varepsilon\) and \(p(x_i)=f(x_i)\) for all \(i=0,1,\ldots,n\) (where \(\lVert\cdot\rVert_\infty\) denotes the \(L^\infty(a,b)\)-norm).

**7.** Let \(p>0\) and \(x=\sqrt{p+\sqrt{p+\sqrt{p+\cdots}}}\), where all the square roots are positive. Design a fixed point iteration \(x_{n+1}=F(x_n)\) that converges to \(x\). You should write down a specific \(F\). Obtain a sufficient condition on the initial iterates for (global) convergence of the iteration.

**8.** Let \(n\) be a positive integer, \(h=1/n\), and consider the grid of points \((ih,jh)\) for \(i,j=0,1,\ldots,n\). Let \(A\) be the finite difference operator with the “5-point stencil” discretizing the Laplace operator \(-\Delta\), with zero Dirichlet boundary conditions on this grid. Describe it. Prove that the spectrum of \(A\) consists of the numbers
\[
\lambda_{lm}=4h^{-2}\bigl(\sin^2(l\pi h/2)+\sin^2(m\pi h/2)\bigr),
\]
for all \(l,m=1,\ldots,n-1\).

**9.** Let \(x_m\) and \(x_{m+1}\) be two successive (complex) iterates when Newton’s method is applied to a polynomial \(p(z)\) of degree \(n\). Prove that there is a zero of \(p(z)\) in the disk \(\{z\in\mathbb{C}:|z-x_m|\leq n|x_{m+1}-x_m|\}\).

**10.** Let \(w(x)\) be a positive integrable function on \([a,b]\). Consider the quadrature
\[
\int_a^b f(x)w(x)\,dx\approx\sum_{k=0}^n\bigl(A_kf(x_k)+B_kf'(x_k)+C_kf''(x_k)\bigr)
\]
for any \(f\) with continuous first and second derivatives (\(f'\) and \(f''\), respectively). Give conditions on \(A_k,B_k,C_k\) and \(x_k\) so that the quadrature has precision \(4n+3\).
