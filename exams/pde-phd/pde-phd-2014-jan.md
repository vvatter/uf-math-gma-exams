# Partial Differential Equations PhD exam, January 2014

**1.** Let \(\Omega\) be an open subset of \(\mathbb{R}^n\) and let \(u\in C^2(\Omega)\) be a harmonic function in \(\Omega\). Prove that \(u\) is analytic in \(\Omega\).

**2.** Let \(U\) be an open and bounded set in \(\mathbb{R}^n\) with smooth boundary. Suppose \(u_1\) and \(u_2\) are both smooth solutions to
\[
\begin{cases}
u_t-\Delta u=0, & \text{in } U_T:=U\times(0,T],\\
u=g, & \text{on } \partial U\times[0,T].
\end{cases}
\]
If \(u_1(x,T)=u_2(x,T)\) for all \(x\in U\), prove that \(u_1\equiv u_2\) within \(U_T\).

**3.** Suppose \(u\) is a smooth solution to
\[
u_{tt}-\Delta u=0, \qquad \text{in } \mathbb{R}^n\times(0,\infty)
\]
and
\[
u\equiv u_t\equiv 0 \qquad \text{on } B(x_0,t_0)\times\{t=0\}.
\]
Let
\[
C=\{(x,t)\mid 0\leq t\leq t_0,\ |x-x_0|\leq t_0-t\}.
\]
Prove that \(u\equiv 0\) within \(C\).

**4.** Use characteristics to solve the following equation:
\[
\begin{cases}
x_1u_{x_1}+2x_2u_{x_2}+u_{x_3}=3u, & \mathbb{R}_+^3,\\
u(x_1,x_2,0)=g(x_1,x_2), & \partial\mathbb{R}_+^3,
\end{cases}
\]
where \(g\) is a given smooth function.

**5.** Fix \(\alpha>0\) and let \(U=B(0,1)\) (open ball). Show there exists a constant \(C\), depending only on \(n\) and \(\alpha\), such that
\[
\int_U u^2\,dx\leq C\int_U |Du|^2\,dx,
\]
provided
\[
|\{x\in U\mid u(x)=0\}|\geq\alpha, \qquad u\in H^1(U).
\]

**6.** Use Hopf–Lax formula to find a solution of
\[
\begin{cases}
u_t+\dfrac{1}{2}|Du|^2=0, & \mathbb{R}^n\times(0,\infty),\\
u=-\dfrac{1}{2}|x|, & \mathbb{R}^n\times\{t=0\}.
\end{cases}
\]
Is this solution unique in the weak sense?

**7.** Let \(U\) be a bounded subset of \(\mathbb{R}^n\), \(u\in W^{2,p}(U)\cap W_0^{1,p}(U)\), and \(2\leq p<\infty\). Prove that
\[
\int_U |Du|^p\,dx\leq C\left(\int_U |u|^p\,dx\right)^{\frac12}\left(\int_U |D^2u|^p\,dx\right)^{\frac12}
\]
for some \(C\) independent of \(u\).
