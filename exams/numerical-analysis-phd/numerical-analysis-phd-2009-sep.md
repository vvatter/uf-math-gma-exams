# Numerical Analysis, PhD exam, September 2009

*Answer any 8 questions.*

**1.** This problem has two parts.
* a. Suppose \(u\) and \(v\in\mathbb C^n\). Derive a formula for the \(p\)-norm of \(uv^*\), \(p\ge 1\).
* b. Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\), where the diagonal elements of \(\Sigma\) are in decreasing order:
  \[
  \sigma_1\geq\sigma_2\geq\sigma_3\geq\cdots.
  \]
  Show that \(\|A\|_2=\sigma_1\) and
  \[
  \|A\|_F=\sqrt{\sigma_1^2+\sigma_2^2+\sigma_3^2+\cdots}.
  \]

**2.** If \(A=QR\) is the \(QR\) factorization of \(A\), show that \(r_{ii}\) is the distance from the \(i\)-th column of \(A\) to the space spanned by the first \(i-1\) columns of \(A\).

**3.** Let \(\|\cdot\|_p\) for \(1\leq p\leq\infty\) denote the norm on \(m\times n\) matrices induced by the \(\ell^p\)-norm. For any positive \(p\) and \(q\) with \(p^{-1}+q^{-1}=1\), show that
\[
\|A\|_2^2\leq \|A\|_p\,\|A\|_q,\qquad\text{for all }A\in\mathbb C^{m\times n}.
\]
Hint: Recall that for a Hermitian matrix \(H\), \(\|H\|_2\) is the absolute largest eigenvalue. As a result, \(\|H\|_2\leq\|H\|\) for any matrix norm induced by a vector norm.

**4.** Prove Gershgorin’s theorem: If \(A\in\mathbb C^{n\times n}\), then each eigenvalue of \(A\) lies in the union of the disks
\[
D_i=\left\{\lambda\in\mathbb C:|\lambda-a_{ii}|\leq\sum_{j\ne i}|a_{ij}|\right\}.
\]
Moreover, if \(m\) disks form a connected domain that is disjoint from the other \(n-m\) disks, then there are precisely \(m\) eigenvalues of \(A\) within this domain.

**5.** Let \(P\) and \(Q\) be two \(m\times m\) orthogonal projectors. Prove that \(\|P-Q\|_2\leq 1\).

**6.** Assume that \(g(x)\) is continuously differentiable on \([a,b]\), that \(g([a,b])\subseteq[a,b]\), and that
\[
\lambda=\operatorname{Max}_{a\leq x\leq b}|g'(x)|<1.
\]
Prove that the following are true:
* (i) \(x=g(x)\) has a unique solution \(\alpha\) in \([a,b]\).
* (ii) For any initial choice \(x_0\) in \([a,b]\), the iteration \(x_{n+1}=g(x_n)\) has the property that \(\lim_{n\to\infty}x_n=\alpha\).
* (iii)
  \[
  \lim_{n\to\infty}\frac{\alpha-x_{n+1}}{\alpha-x_n}=g'(\alpha).
  \]

**7.** Assume that \(f(x)\), \(f'(x)\), and \(f''(x)\) are continuous in \([a,b]\), and that for some \(\alpha\in(a,b)\), we have \(f(\alpha)=0\) and \(f'(\alpha)\ne 0\). Show that if \(x_0\) is chosen close enough to \(\alpha\), the iterates
\[
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
\]
converge to \(\alpha\). Moreover,
\[
\lim_{n\to\infty}\frac{\alpha-x_{n+1}}{(\alpha-x_n)^2}=-\frac{f''(\alpha)}{2f'(\alpha)}.
\]

**8.** Let \(x_0,x_1,x_2,\ldots,x_n\) be distinct real numbers and let \(f\) be a given real-valued function with \(n+1\) continuous derivatives. Let \(I\) be an interval containing all of the \(x_k\), and \(t\). Show that there is a \(\xi\in I\) such that
\[
f(t)-\sum_{k=0}^n f(x_k)l_k(t)=\frac{(t-x_0)(t-x_1)\cdots(t-x_n)}{(n+1)!}f^{(n+1)}(\xi),
\]
where \(l_k\) is the Lagrange interpolating polynomial which is 1 at \(x_k\) and 0 at the other \(x_j\), \(j\ne k\).

**9.** Let \(I_n(f)=\sum_{j=0}^n w_{j,n}f(x_{j,n})\) be a sequence of approximations to \(I(f)=\int_a^b f(x)\,dx\). Let \(F\) be a family of functions which is dense in \(C[a,b]\), and suppose that (a) \(I_n(f)\to I(f)\) for all \(f\in F\), and (b) \(B=\sup_n\sum_{j=0}^n|w_{j,n}|<\infty\). Show that \(I_n(f)\to I(f)\) for all \(f\in C[a,b]\).

**10.** Consider the differential equation \(y'=f(t,y)\), \(y(0)=y_0\), where \(|f(t,y_1)-f(t,y_2)|\leq K|y_1-y_2|\) for all \(y_1\) and \(y_2\in\mathbb R\). Show that a multistep method
\[
y_{n+1}=\sum_{j=0}^p a_jy_{n-j}+h\sum_{j=-1}^p b_jf(x_{n-j},y_{n-j})
\]
has local truncation error \(\tau(h)=O(h^m)\) for all \(y(x)\) which are \((m+1)\) times continuously differentiable if and only if
\[
\sum_{j=0}^p a_j=1,
\]
and
\[
\sum_{j=0}^p(-j)^i a_j+i\sum_{j=-1}^p(-j)^{i-1}b_j=1
\]
for \(i=1,2,3,\ldots,m\).
