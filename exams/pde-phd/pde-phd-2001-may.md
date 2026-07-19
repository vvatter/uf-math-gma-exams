# Partial Differential Equations, PhD exam, May 2001

*Do all problems 1–4. Choose one problem from 5 and 6 and one problem from 7 and 8.*

**1.** Let \(B\) be the unit ball in \(\mathbb{R}^3\). For which values of \(\alpha\) does the function \(|x|^\alpha\) belong to \(H^1(B)\)? Justify your answer.

**2.** Let \(U\subset\mathbb{R}^n\) be open and bounded. Let \(u_m\) and \(v_m\) be bounded sequences in \(H^1(U)\). Show that there exist subsequences \(u_{m_j}\) of \(u_m\) and \(v_{m_j}\) of \(v_m\), and functions \(u,v\in H^1(U)\), such that
\[
\int_U u_{m_j}v_{m_j}\to\int_U uv,
\]
and
\[
\int_U D_{x_i}(u_{m_j}v_{m_j})\to D_{x_i}(uv),\qquad i=1,\ldots,n,
\]
as \(j\to\infty\).

**3.** Let \(U\subset\mathbb{R}^n\) be open, bounded, and connected with smooth boundary \(\partial U\). Let \(u(x,t)\) be a smooth solution to the IBV problem:
\[
u_t=\Delta u,\qquad (x,t)\in U_T,
\]
\[
\frac{\partial u}{\partial n}=0,\qquad (x,t)\in\partial U\times[0,T],
\]
\[
u(x,0)=f(x),\qquad x\in U.
\]
Let
\[
(u)_U(t)=\frac{1}{|U|}\int_U u(x,t)\,dx.
\]
Show that the following statements hold.

Hint: Consider the equation for \(v=u-(u)_U\), and use energy estimate for the equation of \(v\), and Poincaré's inequality.
* (a) \(\displaystyle \frac{d}{dt}(u)_U(t)\equiv0.\)
* (b) \(u\to(u)_U\) in \(L^2(U)\), as \(t\to\infty\).

**4.** Let \(U\subset\mathbb{R}^n\) be open, bounded, and connected with smooth boundary \(\partial U\). Let \(L\) be a uniformly elliptic differential operator of the form
\[
Lu=-\sum_{i,j=1}^n a_{ij}u_{x_i x_j}.
\]
Suppose that \(f\) is a bounded function and \(u,v\in C^2(\overline U)\) satisfy
\[
Lu=f,\qquad Lv\geq1,\qquad x\in U,
\]
\[
u(x)=0,\qquad v(x)\geq0,\qquad x\in\partial U.
\]
Suppose that there exists a point \(x_0\in\partial U\) such that \(v(x_0)=0\). Prove that there exists a constant \(C>0\) such that
\[
|Du(x_0)|\leq C\left|\frac{\partial v}{\partial n}(x_0)\right|.
\]

**5.** Let \(U\subset\mathbb{R}^n\) be open and bounded with smooth boundary \(\partial U\). We say that a function \(u\in H_0^2(U)\) is a weak solution of the biharmonic equation
\[
\Delta^2u=f,\qquad x\in U, \tag{5.1}
\]
\[
u=0,\qquad \frac{\partial u}{\partial n}=0,\qquad x\in\partial U, \tag{5.2}
\]
if
\[
\int_U\Delta u\Delta v\,dx=\int_U fv\,dx,\qquad\text{for any }v\in H_0^2(U). \tag{5.3}
\]
Prove the following statements:
* (a) For a given \(f\in L^2(U)\) there is an unique solution to the problem (5.3).
* (b) If \(u\in C^4(\overline U)\) and \(f\in C^0(\overline U)\) satisfy (5.3), then \(u\) satisfies (5.1) at each point \(x\in U\).

**6.** Let \(U\subset\mathbb{R}^n\) be open and bounded. Show that \(u\in H_0^1(U)\) is a weak solution to the boundary value problem
\[
-\Delta u+u=1,\qquad x\in U,
\]
\[
u=0,\qquad x\in\partial U,
\]
if and only if \(u\) minimizes
\[
E(v)=\int_U\bigl(|\nabla v|^2+v^2-2v\bigr)\,dx
\]
over \(v\in H_0^1(U)\).

**7.** Let \(U\subset\mathbb{R}^n\) be open and bounded. We say \(v\in C^2(\overline U)\) is subharmonic if \(-\Delta v\leq0\) for all \(x\in U\).
* (a) Prove that for any subharmonic \(v\),
  \[
  v(x)\leq\mathop{⨍}_{B(x,r)}v(y)\,dy,\qquad\text{for all }B(x,r)\subset U.
  \]
* (b) Let \(\phi:\mathbb{R}\to\mathbb{R}\) be smooth and convex. Suppose that \(u\) is harmonic and \(v=\phi(u)\). Prove that \(v\) is subharmonic.

**8.** Let \(U\subset\mathbb{R}^n\) be open and bounded with smooth boundary \(\partial U\).
* (a) Write the fundamental solution \(\Phi(x)\) of Laplace's equation.
* (b) Prove that for any point \(x\in U\) and any function \(u\in C^2(\overline U)\),
  \[
  u(x)=\int_U\Phi(y-x)\Delta u(y)\,dy
  +\int_{\partial U}\left(\Phi(y-x)\frac{\partial u}{\partial n}(y)-u(y)\frac{\partial\Phi}{\partial n}(y-x)\right)\,dS(y),
  \]
  where \(\Phi\) is the fundamental solution of Laplace's equation, and \(n\) is the outward unit normal to \(\partial U\).
