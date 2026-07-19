# Numerical Analysis PhD exam, September 2004

*Do any eight of the ten problems below. Notations used are standard: \(\mathbb{C}\) and \(\mathbb{R}\) denote the fields of complex and real numbers, respectively. The space of all real valued continuous functions on \([a,b]\) whose derivatives up to order \(k\) are also continuous on \([a,b]\) is denoted by \(C^k[a,b]\). For all \(u\in C^0[a,b]\), let \(\lVert u\rVert_\infty=\max_{x\in[a,b]}|u(x)|\). While for vectors \(x\in\mathbb{C}^m\), the vector norm \(\lVert x\rVert_2\) denotes the Euclidean distance of \(x\) to the origin, for matrices \(A\in\mathbb{C}^{n\times n}\), \(\lVert A\rVert_2\) denotes the matrix norm induced by the vector norm \(\lVert\cdot\rVert_2\).*

**1.** Let \(S_n^1\) denote the space of linear splines based on knots \(a=t_0<t_1<\cdots<t_n=b\), i.e.,
\[
S_n^1=\{v:v|_{[t_j,t_{j+1}]}\text{ is linear for all }j=0,1,\ldots,n-1\text{ and }v\text{ is continuous on }[a,b]\}.
\]
Let \(s_f\in S_n^1\) interpolate \(f\in C^0[a,b]\) at the knots.
* (a) Prove that \(\lVert s_f\rVert_\infty\leq\lVert f\rVert_\infty\).
* (b) Prove that \(\lVert f-s_f\rVert_\infty\leq 2\lVert f-s\rVert_\infty\) for any \(s\in S_n^1\).
* (c) Consider the error in best approximation to \(f\) from \(S_n^1\) and the error in approximating \(f\) by its linear interpolant \(s_f\). If one goes to zero, does the other go to zero?

**2.** Let \(p>0\) and
\[
x=\sqrt{p+\sqrt{p+\sqrt{p+\cdots}}},
\]
where all the square roots are positive. Let \(F(y)=\sqrt{p+y}\). (How is the fixed point of \(F\) related to \(x\)?)
* (a) Consider the fixed point iteration \(x_{n+1}=F(x_n)\). Prove that if the initial iterate \(x_0\) satisfies \(x_0+p>0\), then all iterates remain on the same side of \(x\) as \(x_0\).
* (b) Prove that the fixed point iteration converges for all choices of initial guesses greater than \(-p+1/4\).
* (c) Whenever the fixed point iteration converges, what is its order of convergence?

**3.** To numerically solve the initial value problem
\[
Y'(t)=f(t,Y),\qquad \text{for all }t\in(0,1), \tag{1}
\]
\[
Y(0)=Y_0, \tag{2}
\]
consider using the Runge–Kutta type iteration
\[
y_{n+1}=y_n+(\alpha_1k_1+\alpha_2k_2)h,
\]
where \(k_1=f(t_n,y_n)\), \(k_2=f(t_n+\mu h,y_n+\mu hk_1)\), \(t_n=nh\), and \(\alpha_1,\alpha_2\) and \(\mu\) are three real parameters. Suppose \(f(t,Y)=Y^\lambda\) for some \(\lambda>0\). Find an interval \(I\subseteq\mathbb{R}\) such that for \(\lambda\in I\) there are choices of the parameters \(\alpha_1,\alpha_2,\mu\in(0,1)\) for which the method is of third order. For these choices of parameters, what is the order of convergence one can expect in general when the method is applied to (1)–(2) with any \(f(t,Y)\)?

**4.** Let \(x_0,x_1,\ldots,x_n\) be distinct points in a finite interval \([a,b]\) and \(f\in C^1[a,b]\). Show that for any given \(\epsilon>0\) there exists a polynomial \(p\) such that \(\lVert f-p\rVert_\infty<\epsilon\) and \(p(x_i)=f(x_i)\) for all \(i=0,1,\ldots,n\).

**5.** Let \(w(x)\) be a positive integrable function on \([a,b]\). Let \(p(x)\) denote the Hermite interpolant of \(f(x)\) such that \(d^\ell f/dx^\ell\) and \(d^\ell p/dx^\ell\) coincide at distinct nodes \(x_0,x_1,\ldots,x_n\) in \([a,b]\) for \(\ell=0,1\) and \(2\). Consider the quadrature that approximates \(\int_a^b f(x)w(x)\,dx\) by
\[
\int_a^b p(x)w(x)\,dx=\sum_{k=0}^n\left(A_kf(x_k)+A_k'f'(x_k)+A_k''f''(x_k)\right). \tag{3}
\]
* (a) Prove that the precision of the quadrature is at least \(4n+3\) if and only if the nodes are chosen such that \(\pi_{n+1}(x)\equiv(x-x_0)(x-x_1)\cdots(x-x_n)\) satisfies
  \[
  \int_a^b\pi_{n+1}(x)^3q(x)w(x)\,dx=0
  \]
  for all polynomials \(q\) of degree at most \(n\).
* (b) Prove that there cannot exist numbers \(\{A_i\},\{A_i'\},\{A_i''\},\{x_i\}\) such that a quadrature formula of the type (3) has precision greater than \(4n+3\).

**6.** For any given \(\epsilon>0\), a \(z\in\mathbb{C}\) is an “\(\epsilon\)-pseudoeigenvalue” of \(A\in\mathbb{C}^{m\times m}\) if \(\lVert(zI-A)^{-1}\rVert_2\geq 1/\epsilon\) (i.e., if \(zI-A\) is sufficiently close to being singular). The “\(\epsilon\)-pseudospectrum” of \(A\) is the set of all such \(\epsilon\)-pseudoeigenvalues. Here we adopt the convention that \(\lVert(zI-A)^{-1}\rVert_2=\infty\) if \(zI-A\) is singular. Prove the equivalence of the following statements. Here, \(\sigma_{\min}(zI-A)\) denotes the smallest singular value of \(zI-A\).
* (a) \(z\) is an eigenvalue of \(A+E\) for some perturbation \(E\in\mathbb{C}^{m\times m}\) with \(\lVert E\rVert_2\leq\epsilon\).
* (b) There is a vector \(u\in\mathbb{C}^m\) with \(\lVert(A-zI)u\rVert_2\leq\epsilon\) and \(\lVert u\rVert_2=1\).
* (c) \(\sigma_{\min}(zI-A)\leq\epsilon\).
* (d) \(z\) is in the \(\epsilon\)-pseudospectrum of \(A\).

**7.** This problem has two parts.
* (a) Prove that all norms in a finite dimensional space are equivalent: In other words, if \(\lVert\cdot\rVert_*\) and \(\lVert\cdot\rVert_{**}\) denote any two norms on \(\mathbb{C}^m\), then prove that there are positive constants \(C_1,C_2\) independent of \(u\) such that
  \[
  C_1\lVert u\rVert_*\leq\lVert u\rVert_{**}\leq C_2\lVert u\rVert_*\qquad\text{for all }u\in\mathbb{C}^m.
  \]
* (b) Let \(V\) be the space of all complex \(m\times m\) matrices with any norm. Prove that the subset of invertible matrices is an open subset of \(V\).

**8.** Consider the conjugate gradient algorithm for solving \(Ax=b\) for a symmetric positive definite \(A\in\mathbb{R}^{m\times m}\).
* (a) State a relationship between the \(n\)-th iterate of the algorithm and the best approximation to \(x\) from a Krylov space (be sure to specify the norm).
* (b) Prove that if \(A\) has only \(n\leq m\) distinct eigenvalues then the iteration (in the absence of round off errors) converges to the exact solution \(x\) in at most \(n\) steps no matter what the initial iterate is. (You may use 8a.)

**9.** Let \(A\in\mathbb{C}^{m\times m}\) be nonsingular. Show that \(A\) has an \(LU\) factorization if and only if all its leading principal submatrices are nonsingular. If an \(LU\) factorization exists, is it unique?

**10.** Let \(P\in\mathbb{C}^{m\times m}\) be a projector. Prove that \(\lVert P\rVert_2\geq 1\), with equality if and only if \(P\) is an orthogonal projector.
