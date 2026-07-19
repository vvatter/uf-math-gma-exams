# Numerical Analysis PhD exam, May 2011

*Answer any 8 questions.*

**1.** Suppose \(A\) and \(B\) are square matrices such that \(AB\) is normal. Prove that \(\|AB\|_2 \leq \|BA\|\). (We use \(\|\cdot\|_2\) to denote the spectral norm and \(\|\cdot\|\) to denote any induced matrix norm.)

**2.** Let \(P\) and \(Q\) be Hermitian positive definite matrices. Prove that
\[
x^*Px \leq x^*Qx \quad \text{for all } x \in \mathbb{C}^n
\]
if and only if
\[
x^*Q^{-1}x \leq x^*P^{-1}x \quad \text{for all } x \in \mathbb{C}^n.
\]

**3.** Suppose \(A\) is a Hermitian positive definite matrix split into \(A=C+C^*+D\) where \(D\) is also Hermitian positive definite. Prove that \(B=C+\omega^{-1}D\) is invertible whenever \(0<\omega<2\). Consider the iteration \(x_{n+1}=x_n+B^{-1}(b-Ax_n)\), with any initial iterate \(x_0\). Prove that \(x_n\) converges to \(x=A^{-1}b\) whenever \(0<\omega<2\).

**4.** Let the singular values of any matrix \(M\in\mathbb{C}^{m\times n}\) be denoted by \(\sigma_1(M)\geq\sigma_2(M)\geq\cdots\geq\sigma_q(M)\) with \(q=\min(m,n)\). Prove that if \(A\) and \(B\) are two matrices in \(\mathbb{C}^{m\times n}\), then
\[
\sigma_{i+j-1}(A+B)\leq\sigma_i(A)+\sigma_j(B)
\]
for all \(i,j=1,2,\ldots,q\) and \(i+j\leq q\).

**5.** Let \(A\in\mathbb{R}^{N\times N}\) and \(b\in\mathbb{R}^N\). Consider the following iteration for solving \(Ax=b\), that computes \(x_{n+1}\), given \(x_n\in\mathbb{R}^N\), as follows (in \(m\) intermediate steps): Setting \(x_{n+1}^{(0)}=x_n\), for \(\ell=1,2,\ldots,m\), compute \(x_{n+1}^{(\ell)}=x_{n+1}^{(\ell-1)}+\tau_\ell(b-Ax_{n+1}^{(\ell-1)})\). Then, define \(x_{n+1}=x_{n+1}^{(m)}\). There is a linear operator \(E\) such that \(x_{n+1}-x=E(x_n-x)\). Give a formula for \(E\). Suppose \(A\) is Hermitian and positive definite with spectral condition number \(\kappa\). Prove that there are real values of the \(m\) parameters \(\tau_\ell\) such that
\[
\rho(E)\leq 2\left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^m.
\]

**6.** Let \(I_n(f)=\sum_{j=0}^n w_{j,n}f(x_{j,n})\) be a sequence of quadratures on \([a,b]\) such that (i) \(I_n(p)\to I(p)\) as \(n\to+\infty\) for any polynomial \(p(x)\), and (ii) \(B=\sup_n\sum_{j=0}^n|w_{j,n}|<+\infty\). Prove that \(I_n(f)\to I(f)\) for all \(f\in C[a,b]\). Here, the notation \(I(f)=\int_a^b f(x)\,dx\) is used.

**7.** Design a stable quadratic algorithm for computing the positive root \(\alpha\) of the equation \(x^2+2px-q=0\) where \(p\) and \(q\) are arbitrary positive numbers. Prove that your algorithm is indeed stable and quadratic. Find an interval \([a,b]\) such that any iterative sequence starting in \([a,b]\) will converge to \(\alpha\).

**8.** State the Lagrange interpolation problem. Prove that the problem is well-posed, i.e. prove the existence and uniqueness of solutions. Derive the error formula for the interpolating polynomial.

**9.** Describe the Trapezoidal Rule for numerical integration. State and prove the error formula of the Trapezoidal Rule. Show that the error bound cannot be improved.

**10.** Let \(w(x)>0\) be integrable on \([a,b]\). Define an orthogonal polynomial family \(\{\phi_n\}\) on \([a,b]\) with weight \(w(x)\). Explain how \(\{\phi_n\}\) can be constructed from \(\{x^n\}\). Prove that \(\phi_n(x)\) has \(n\) distinct roots in the interval \((a,b)\).
