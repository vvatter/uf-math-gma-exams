# Partial Differential Equations PhD exam, September 2010

**1.** Let \(U\) be either \(\mathbb R_+^n\) or the unit ball in \(\mathbb R^n\) (\(n\ge 2\)). Write the expression of the Green’s function for \(-\Delta\) with respect to the Dirichlet condition on \(\partial U\).

**2.** Let \(U\subset\mathbb R^n\) be a bounded open set with smooth boundary \(\partial U\), \(A=(a_{ij})_{n\times n}\) be a symmetric, positive definite constant matrix. For the following variational form:
\[
I(w):=\frac12\int_U\sum_{i,j=1}^n a_{ij}\partial_iw\partial_jw\,dx;\qquad w\in H_g^1:=\{w\in H^1(U);\ w=g\text{ on }\partial U\},
\]
where \(g\) is a smooth function on \(\partial U\), prove that the minimizer \(u\) exists and is smooth.

**3.** Let \(A=(a_{ij})_{n\times n}\) be a symmetric and positive definite constant matrix. Suppose \(u\) satisfies
\[
\sum_{i,j=1}^n a_{ij}\partial_{ij}u=0,\qquad \text{in }\mathbb R^n,
\]
and \(u\ge -1\) in \(\mathbb R^n\). Show that \(u\equiv\text{constant}\).

**4.** Let \(\phi(x)=\dfrac{1}{n(n-2)\alpha(n)}|x|^{2-n}\) be the fundamental solution for the Laplace operator in \(\mathbb R^n\) (\(n\ge 3\)). Here \(\alpha(n)\) is the volume of the unit ball \(B_1\). Suppose \(f(x)\in C^2(\mathbb R^n)\) and satisfies
\[
|D^jf(x)|\le C(1+|x|)^{-2-\epsilon-j},\qquad \forall x\in\mathbb R^n,\quad j=0,1,2,
\]
where \(\epsilon\) is a positive number. Then
\[
u(x)=\int_{\mathbb R^n}\phi(x-y)f(y)\,dy
\]
satisfies
\[
-\Delta u(x)=f(x)\qquad \mathbb R^n.
\]

**5.** Let \(u\in W^{1,p}(\mathbb R^n)\), where \(p>n\). Show that
\[
\frac{1}{r^n}\int_{B(x,r)}|u(x)-u(y)|\,dy\le C(n)\int_{B(x,r)}\frac{|Du(y)|}{|x-y|^{n-1}}\,dy.
\]

**6.** Write down an explicit formula for a solution of
\[
\begin{cases}
u_t-\Delta u+cu=f, & \mathbb R^n\times(0,\infty),\\
u=g, & \mathbb R^n\times\{t=0\},
\end{cases}
\]
where \(c\in\mathbb R\).

**7.** Let \(U\subset\mathbb R^n\) be an open, bounded subset of \(\mathbb R^n\) with smooth boundary. Set \(U_T=U\times[0,T]\), \(\Gamma_T=\overline{U_T}\setminus U_T\), where \(T>0\). Prove that there exists at most one solution \(u\in C^2(\overline{U_T})\) of
\[
\begin{cases}
u_{tt}-\Delta u=f, & U_T,\\
u=0, & \Gamma_T,\\
u_t=h, & U\times\{t=0\},
\end{cases}
\]
where \(g,h\) are smooth functions.
