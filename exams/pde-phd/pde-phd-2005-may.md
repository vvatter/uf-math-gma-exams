# Partial Differential Equations PhD exam, May 2005

**1.** Let \(\Omega\) be a bounded smooth set in \(\mathbb{R}^n\) (\(n\ge 2\)) and let \(L:\mathbb{R}^n\times\mathbb{R}\times\overline{\Omega}\to\mathbb{R}\) be a smooth mapping. Assume in addition that \(L\) is bounded below and the mapping \(p\mapsto L(p,z,x)\) is convex for each \(z\in\mathbb{R}\), \(x\in\overline{\Omega}\subseteq\mathbb{R}^n\). Prove that \(I(w):=\int_\Omega L(Dw,w,x)\,dx\) is weakly lower semicontinuous on \(W^{1,q}(\Omega)\) (\(1<q<\infty\)).

**2.** Let \(\{a_{ij}\}_{n\times n}\) (\(n\ge 2\)) be a positive definite constant matrix. Let \(B_1\) be the unit ball in \(\mathbb{R}^n\). Find the Euler–Lagrange equation for
\[
I(w)=\int_{B_1}\sum_{i,j=1}^n\bigl(a_{ij}\partial_iw\partial_jw\bigr)\,dx,\qquad w\in H_0^1(B_1),
\]
under the constraint \(\int_{B_1}|w|^2=1\).

**3.** Prove that if \(\lambda>0\) is large enough, there exists a function \(u\in H^2(B_1)\cap H_0^1(B_1)\) solving
\[
\begin{cases}
-\Delta u+\lambda u=\sqrt{1+|Du|^2}, & \text{in }B_1,\\
u=0, & \text{on }\partial B_1.
\end{cases}
\]

**4.** Let \(\Omega\) be a bounded smooth subset of \(\mathbb{R}^n\) (\(n\ge 2\)) and let \(u\) be a classical solution of
\[
\begin{cases}
\Delta u(x)+a(x)u(x)=0, & \Omega,\\
u\ge 0, & \partial\Omega,
\end{cases}
\]
where \(a(x)\) is a smooth function. Suppose there exists \(\phi(x)>0\) and smooth over \(\overline{\Omega}\) such that
\[
\Delta\phi+a(x)\phi\le 0,\qquad \Omega.
\]
Show that either \(u>0\) or \(u=0\) in \(\Omega\).

**5.** Let \(u\in C^2(B_1)\) be a solution of
\[
\begin{cases}
-\Delta u=e^u, & B_1\subset\mathbb{R}^2,\\
u=1, & \text{on }\partial B_1.
\end{cases}
\]
Prove that:
* (1): \(u>1\) in \(B_1\).
* (2): \(u\) is radially symmetric and \(\dfrac{du}{dr}<0\) for all \(r\in(0,1)\).

**6.** This problem has two parts.
* (a) Show there exists a unique minimizer \(u\in A\) of
  \[
  I[w]=\int_\Omega\left(\frac12|Dw|^2-fw\right)dx,
  \]
  where \(\Omega\) is a bounded smooth subset of \(\mathbb{R}^n\) (\(n\ge 2\)), \(f\in L^2(\Omega)\),
  \[
  A=\{w\in H_0^1(\Omega);\ |Dw|\le 1\ \text{a.e.}\}.
  \]
* (b) Prove
  \[
  \int_\Omega Du\cdot D(w-u)\,dx\ge\int_\Omega f(w-u)\,dx
  \]
  for all \(w\in A\).

**7.** Let \(u\in W^{1,p}(B_1)\). Prove that \(u^+,u^-,|u|\in W^{1,p}(B_1)\) and for almost all points over each region \((u>0,u<0,u=0)\) (Recall \(u=u^+-u^-\)),
\[
Du^+=
\begin{cases}
Du, & u>0,\\
0, & u\le 0,
\end{cases}
\qquad
Du^-=
\begin{cases}
-Du, & u<0,\\
0, & u\ge 0,
\end{cases}
\qquad
D|u|=
\begin{cases}
Du, & u>0,\\
-Du, & u<0,\\
0, & u=0.
\end{cases}
\]
Hint: Let
\[
f_\epsilon(u)=
\begin{cases}
(u^2+\epsilon^2)^{1/2}-\epsilon, & u>0,\\
0, & u\le 0.
\end{cases}
\]
For all \(\phi\in C_0^1(B_1)\),
\[
\int_{B_1}f_\epsilon(u)D\phi\,dx
=-\int_{\{u>0\}}\frac{uDu}{\sqrt{u^2+\epsilon^2}}\phi\,dx.
\]

**8.** Let \(a_{ij}(x)\), \(b_i(x)\) (\(i,j=1,\ldots,n\)), \(c(x)\) be \(C^\infty\) functions over \(B_1\) (\(n\ge 2\)). Let \(\lambda_0,\lambda_1\) be two positive constants satisfying
\[
0<\lambda_0|\xi|^2\le a_{ij}(x)\xi_i\xi_j\le\lambda_1|\xi|^2
\qquad \forall x\in B_1,\quad \forall\xi\in\mathbb{R}^n.
\]
Suppose \(u\in W^{1,q}\) is a weak solution of
\[
\sum_{i,j}\partial_i\bigl(a_{ij}(x)\partial_j u\bigr)
+\sum_i b_i(x)\partial_i u(x)+c(x)u=u^2,\qquad B_1.
\]
Look for the smallest \(q_0>1\) such that for \(q>q_0\), \(u\in C^\infty(B_1)\). Prove your statement.

Hint: The following estimates should be used: Suppose \(u\in W^{1,q}(B_1)\) verifies
\[
\sum_{i,j}\partial_i\bigl(a_{ij}(x)\partial_j u\bigr)
+\sum_i b_i(x)\partial_i u(x)+c(x)u=f(x),\qquad B_1,
\]
in the sense of distribution, \(f\in L^q\), \(q\in(1,\infty)\). Then
\[
\|u\|_{W^{2,q}(B_{1/2})}
\le C\bigl(\|u\|_{L^q(B_1)}+\|f\|_{L^q(B_1)}\bigr).
\]
If we further know \(u\in C^\alpha(\overline{B}_1)\) and \(f\in C^\alpha(\overline{B}_1)\) for some \(\alpha\in(0,1)\), then the following Schauder estimate holds:
\[
\|u\|_{C^{2,\alpha}(B_{1/2})}
\le C\bigl(\|u\|_{C^\alpha(B_1)}+\|f\|_{C^\alpha(B_1)}\bigr).
\]
