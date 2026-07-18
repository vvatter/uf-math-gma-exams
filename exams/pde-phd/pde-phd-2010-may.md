# Partial Differential Equations, PhD exam, May 2010

**1.** Suppose \(u \in C_1^2(\mathbb{R}^n \times [0,T]) \cap C(\mathbb{R}^n \times [0,T])\) solves
\[
\begin{cases}
u_t-\displaystyle\sum_{i,j=1}^n a_{ij}\partial_{ij}u=0, & \text{in }\mathbb{R}^n\times(0,T],\\
u=g, & \text{on }\mathbb{R}^n\times\{t=0\}.
\end{cases}
\]
where \((a_{ij})_{n\times n}\) is a positive definite, symmetric constant matrix, \(g\) is a given smooth function. Suppose in addition that
\[
u(x,t)\leq Ae^{a|x|^2},\qquad x\in\mathbb{R}^n,\quad t\in[0,T]
\]
for some \(a,A>0\). Prove
\[
\sup_{\mathbb{R}^n\times[0,T]}u=\sup_{\mathbb{R}^n}g.
\]

**2.** Let \(u\) solve
\[
\begin{cases}
u_{tt}-u_{xx}=0, & \mathbb{R}_+\times(0,\infty),\\
u=g,\quad u_t=h, & \text{on }\mathbb{R}_+\times\{t=0\},\\
u=0, & \text{on }\{x=0\}\times(0,\infty).
\end{cases}
\]
where \(g,h\) are smooth, given functions of \(x\) such that \(g(0)=h(0)=0\). Write the explicit expression of \(u\).

**3.** Let \(B_1\) be the unit ball in \(\mathbb{R}^n\) (\(n\geq 3\)), \(p\in\left(1,\frac{2n}{n-2}\right)\) and \(\alpha\in(0,1)\), show that there exists a \(C\) depending only on \(n,p,\alpha\) such that
\[
\left(\int_{B_1}|u|^p\,dx\right)^{\!1/p}\leq C(n,p,\alpha)\left(\int_{B_1}|\nabla u|^2\right)^{\!1/2},
\]
for all \(u\in H^1(B_1)\) that satisfy the following property:
\[
|\{x\in B_1;\ u(x)=0\}|\geq\alpha|B_1|.
\]

**4.** Suppose \(u\in C^2\) solves
\[
u_{tt}-\Delta u=0\qquad\text{in }\mathbb{R}^n\times(0,\infty).
\]
Fix \(x_0\in\mathbb{R}^n\), \(t_0>0\) and consider the cone
\[
C=\{(x,t);\ 0\leq t\leq t_0,\ |x-x_0|\leq t_0-t\}.
\]
Prove that if \(u\equiv u_t\equiv0\) on \(B(x_0,t_0)\times\{t=0\}\), then \(u\equiv0\) in \(C\).

**5.** Let \((a_{ij}(x))_{n\times n}\) be smooth, symmetric on \(B_1\) and there exist \(0<\lambda<\Lambda\) such that
\[
\lambda|\xi|^2\leq\sum_{i,j=1}^n a_{ij}(x)\xi_i\xi_j\leq\Lambda|\xi|^2,\qquad \forall x\in B_1,\quad \forall\xi\in\mathbb{R}^n.
\]
Let \(b_i\) (\(i=1,2,\ldots,n\)), \(c\) and \(f\) be smooth functions on \(B_1\). Show that there exists \(\delta>0\) such that if
\[
\|b_i\|_{L^\infty(B_1)}+\|c\|_{L^\infty(B_1)}\leq\delta,\qquad i=1,\ldots,n,
\]
then there exists a smooth function \(u\) that solves the Dirichlet boundary problem uniquely:
\[
\begin{cases}
-\displaystyle\sum_{i,j=1}^n\partial_i\bigl(a_{ij}(x)\partial_j u\bigr)+\displaystyle\sum_{i=1}^n b_i(x)\partial_i u(x)+c(x)u(x)=f, & B_1,\\
u=0, & \text{on }\partial B_1.
\end{cases}
\]

**6.** Let \(\{u_m\}\) be a sequence of smooth functions satisfying \(u_m(x)\leq C\) and \(|\Delta u_m|\leq C\) for some constant \(C\) uniformly over \(B_1\), the unit ball. Prove that over \(B_{1/2}\), along a subsequence, either \(u_m\) converges to \(-\infty\) uniformly, or \(u_m\) converges to a function \(u\) in \(C^2\) norm.

**7.** Let \(\{a_{ij}\}_{n\times n}\) (\(n\geq2\)) be a positive definite, symmetric, constant matrix, \(b_1,\ldots,b_n,c\) be smooth functions on \(B_1\), the unit ball in \(\mathbb{R}^n\). Show that the minimum of the following variational form
\[
I(w)=\int_{B_1}\sum_{i,j=1}^n\left(a_{ij}\partial_iw\partial_jw+\sum_i b_i\partial_iw\,w+cw^2\right)dx,\qquad w\in H_0^1(B_1)
\]
under the constraint: \(\int_{B_1}|w|^2=1\) can be reached by a smooth function.
