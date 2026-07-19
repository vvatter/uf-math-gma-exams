# Numerical Analysis, PhD exam, May 2004

*Do any eight of the following ten problems.*

**1.** Let \(w(x)\) be a positive integrable function on \([a,b]\). Let \(p(x)\) denote the Hermite interpolant of \(f(x)\) such that \(d^\ell f/dx^\ell\) and \(d^\ell p/dx^\ell\) coincide at distinct nodes \(x_0,x_1,\ldots,x_n\) in \([a,b]\) for \(\ell=0,1\) and \(2\). Consider the quadrature that approximates \(\int_a^b f(x)w(x)\,dx\) by
\[
\int_a^b p(x)w(x)\,dx:=\sum_{k=0}^n\left(A_kf(x_k)+A'_kf'(x_k)+A''_kf''(x_k)\right). \tag{1}
\]
* (a) Prove that the precision of the quadrature is at least \(4n+3\) if and only if the nodes are chosen such that \(\pi_{n+1}(x)=(x-x_0)(x-x_1)\cdots(x-x_n)\) satisfies
  \[
  \int_a^b \pi_{n+1}(x)^3q(x)w(x)\,dx=0
  \]
  for all polynomials \(q\) of degree at most \(n\).
* (b) Prove that there cannot exist numbers \(\{A_j\},\{A'_j\},\{A''_j\},\{x_j\}\) such that a quadrature formula of the type (1) has precision greater than \(4n+3\).

**2.** To find a root of \(f(x)=0\), let \(g(x)=x+cf(x)\) for some constant \(c\ne0\). If \(\alpha\) is a root of \(f(x)\) and \(f'(\alpha)=2\), for what values of \(c\) will the sequence
\[
x_{n+1}=g(x_n)
\]
be guaranteed to converge to \(\alpha\) (assuming \(x_0\) is close enough to \(\alpha\) and \(f\) is smooth)? For what value of \(c\) will the convergence be quadratic?

**3.** Denote the complete and natural cubic splines interpolating \(f\in C^2[a,b]\) at knots \(t_0<t_1<\cdots<t_n\) by \(s_c(t)\) and \(s_n(t)\), respectively.
* (a) Prove that
  \[
  \int_a^b|s_c''(x)|^2\,dx\leq\int_a^b|f''(x)|^2\,dx.
  \]
  State an analogous inequality for \(s_n\).
* (b) Which of the two interpolating splines has smaller “energy”, i.e., which of \(\int_a^b|s_c''(x)|^2\,dx\) and \(\int_a^b|s_n''(x)|^2\,dx\) is smaller?

**4.** To numerically solve the initial value problem
\[
Y'(t)=f(t,Y),\qquad \text{for all }t\in(0,1), \tag{2}
\]
\[
Y(0)=Y_0, \tag{3}
\]
consider using the Runge–Kutta type iteration
\[
y_{n+1}=y_n+h(\alpha_1k_1+\alpha_2k_2),
\]
where \(k_1=f(t_n,y_n)\), \(k_2=f(t_n+\mu h,y_n+\mu hk_1)\), \(t_n=nh\), and \(\alpha_1,\alpha_2\), and \(\mu\) are three real parameters. Suppose \(f(t,Y)=Y^\lambda\) for some \(\lambda>0\). Find an interval \(I\) such that for \(\lambda\in I\) there are choices of the parameters \(\alpha_1,\alpha_2,\mu\in(0,1)\) for which the method is of third order. For these choices of parameters, what is the order of convergence one can expect in general when the method is applied to (2)–(3) with any \(f(t,Y)\)?

**5.** Let \(x_m\) and \(x_{m+1}\) be two successive iterates when Newton’s method is applied to a polynomial \(p(z)\) of degree \(n\). Prove that there is a zero of \(p(z)\) in the disk
\[
\{z\in\mathbb C:|z-x_m|\leq n|x_{m+1}-x_m|\}.
\]
(Suggestion: Use \(p'(z)/p(z)=\sum_{j=1}^n1/(z-r_j)\), where \(r_1,r_2,\ldots,r_n\) are the roots of \(p\).)

**6.** Consider the Arnoldi iteration on the Krylov spaces \(\mathcal K_k=\operatorname{span}\{b,Ab,A^2b,\ldots,A^{k-1}b\}\) for some \(b\in\mathbb C^m\) and \(A\in\mathbb C^{m\times m}\), using the following algorithm:

Algorithm 1 (Arnoldi iteration)

(a) Set \(q_1=b/\|b\|_2\).

(b) For \(n=1,2,3,\ldots\) do:

i. Set \(v=Aq_n\).

ii. For \(j=1,2,\ldots,n\) do:

A. Set \(h_{jn}=q_j^*v\).

B. Replace \(v\) by \(v-h_{jn}q_j\).

iii. Set \(h_{n+1,n}=\|v\|_2\).

iv. Set \(q_{n+1}=v/h_{n+1,n}\).

Suppose the algorithm proceeds without breakdown until, for some \(n<m\), it encounters \(h_{n+1,n}=0\).
* (a) Show that \(\mathcal K_n\) is an invariant subspace of \(A\), i.e., \(A\mathcal K_n\subseteq\mathcal K_n\).
* (b) Show that \(\mathcal K_n=\mathcal K_{n+1}=\mathcal K_{n+2}=\cdots\).
* (c) Let \(H_n\) be the \(n\times n\) Hessenberg matrix whose \(ij\)-th entry (\(i\leq j+1\)) is the number \(h_{ij}\) computed in the algorithm. Show that each eigenvalue of \(H_n\) is an eigenvalue of \(A\).
* (d) Show that if \(A\) is nonsingular, then the solution \(x\) of \(Ax=b\) lies in \(\mathcal K_n\).

**7.** Let \(A\in\mathbb C^{m\times m}\). Diagonalize the \(2m\times2m\) matrix
\[
\begin{pmatrix}0&A^*\\A&0\end{pmatrix}
\]
using an SVD of \(A\).

**8.** Consider \(\mathbb C^{m\times n}\) with any norm topology.
* (a) Let \(m=n\). The map \(f(A)=A^{-1}\) is defined on the (open) subset \(V\subseteq\mathbb C^{n\times n}\) of all invertible matrices. Is \(f\) continuous on \(V\)?
* (b) Let \(m\ne n\). The map \(g(A)=A^+\) (where \(A^+\) is the Moore–Penrose pseudoinverse) is defined on all \(\mathbb C^{m\times n}\). Is \(g\) continuous on \(\mathbb C^{m\times n}\)?

**9.** Given \(A\in\mathbb C^{m\times n}\) of full rank and \(b\in\mathbb C^m\), consider the block \(2\times2\) system
\[
\begin{pmatrix}I&A\\A^*&0\end{pmatrix}
\begin{pmatrix}r\\x\end{pmatrix}
=
\begin{pmatrix}b\\0\end{pmatrix},
\]
where \(I\) is the \(m\times m\) identity matrix. Show that this system has a unique solution \(\begin{pmatrix}r\\x\end{pmatrix}\), and that the vectors \(r\) and \(x\) are the residual and the solution respectively of the least squares problem: \(\min_x\|b-Ax\|_2\).

**10.** Consider the Rayleigh quotient iteration applied to the \(2\times2\) real matrix
\[
A=\begin{bmatrix}\lambda_1&0\\0&\lambda_2\end{bmatrix},
\]
where \(\lambda_1\ne\lambda_2\). Find the subset \(S\subset\mathbb R^2\) having the property that the Rayleigh quotient iteration with initial guesses in \(S\) do not converge. Is \(S\) a set of measure zero?
