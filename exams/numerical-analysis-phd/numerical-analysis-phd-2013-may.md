# Numerical Analysis, PhD exam, May 2013

*Do 5 of 7*

**1.** (General Fixed Point Theory) Assume that \(g(x)\) is continuously differentiable on \([a,b]\), that \(g([a,b])\subseteq [a,b]\), and that
\[
\lambda=\max_{a\leq x\leq b}|g'(x)|<1.
\]
Show that the following are true:
* (i) \(x=g(x)\) has a unique solution \(\alpha\) in \([a,b]\),
* (ii) For any initial choice \(x_0\) in \([a,b]\), with \(x_{n+1}=g(x_n)\), \(\lim_{n\to\infty}x_n=\alpha\), and
* (iii)
  \[
  \lim_{n\to\infty}\frac{\alpha-x_{n+1}}{\alpha-x_n}=g'(\alpha).
  \]
* (iv) Does the statement remain true if the interval \((a,b)\) is open?
* (v) Assume in addition that \(g'(\alpha)=0\) and show that the sequence converges quadratically.
* (vi) (Newton’s Method) Assume that \(f(x)\), \(f'(x)\), and \(f''(x)\) are continuous in \([a,b]\), and that for some \(\alpha\in[a,b]\), \(f(\alpha)=0\), and \(f'(\alpha)\neq0\). Then if \(x_0\) is chosen close enough to \(\alpha\), the iterates
  \[
  x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
  \]
  converge to \(\alpha\). Moreover they converge quadratically.
* (vii) State Newton’s method for \(f(x)=0\) if \(f:\mathbb{R}^n\to\mathbb{R}^n\).

**2.** Theorem: (Lagrange Error Formula) Let \(x_0,x_1,x_2,\ldots,x_n\) be distinct real numbers, \(l_j(x)\) be the corresponding Lagrange polynomials and suppose that \(f\) is a given real-valued function with \(n+1\) continuous derivatives. Let \(I\) be an interval containing all of the \(x_k\), and \(t\). Then there is a \(\xi\in I\) such that
\[
f(t)-\sum_{j=0}^{n}f(x_j)l_j(t)=\frac{(t-x_0)(t-x_1)\cdots(t-x_n)}{(n+1)!}f^{(n+1)}(\xi).
\]

**3.** Let \(\{p_n\}\) be an orthogonal family on \([a,b]\) constructed by using the Gram–Schmidt process on \(1,t,t^2,t^3,\ldots\). Prove that all of the zeros of \(p_n(t)\) are contained in \([a,b]\).

**4.** Given Simpson’s rule for numerical integration, i.e.
\[
\int_{t_n}^{t_{n+2}}f(x)\,dx\approx\frac{2h}{6}\bigl(f(t_n)+4f(t_{n+1})+f(t_{n+2})\bigr),\qquad t_n=t_0+nh,
\]
* (i) Explain where the formula comes from (you don’t need to derive it).
* (ii) Prove that it is exact for cubic polynomials.
* (iii) Show that the local error is \(O(h^5)\).

**5.** Gaussian Quadrature: Show that you can find \(n\) points on an interval \([a,b]\) (tell us which points), and a formula which uses only the value of the function \(f(x)\) at these points, and weights \(w_k\) such that the approximation formula
\[
\int_a^b f(x)\,dx\approx I_n(f)\equiv\sum_{k=1}^{n}w_kf(x_k)
\]
is exact for polynomials of order \(2n-1\).

**6.** Assume that you are solving the initial value problem \(y'(t)=f(t,y)\), with \(y(0)\) given. Assume further that \(f(t,y)\) satisfies the Lipschitz condition \(|f(t,y_1)-f(t,y_2)|\leq K|y_1-y_2|\) for all \(t\in[a,b]\). Explain Euler’s method and derive a cumulative error formula, not just a local error formula.

**7.** (General Multistep Methods) Assume that you are solving the initial value problem \(y'(t)=f(t,y)\), with \(y(0)\) given. Consider a general formula of the type
\[
y_{n+1}=\sum_{j=0}^{p}a_jy_{n-j}+h\sum_{j=-1}^{p}b_jf(t_{n-j},y_{n-j}).
\]
Furthermore, let us define the local truncation error as
\[
T_n(Y)=Y(t_{n+1})-\left(\sum_{j=0}^{p}a_jY(t_{n-j})+h\sum_{j=-1}^{p}b_jf(t_{n-j},Y(t_{n-j}))\right),
\]
where \(Y(t_n)\) is the exact value of the initial value problem and \(y_n\) is the approximated value of the problem at \(t_n\). We let
\[
\tau_n(Y)=\frac{1}{h}T_n(Y).
\]
Given this prove the following:

Let \(m\geq1\) be a given integer. In order that \(\max|\tau(Y)|\to0\) as \(h\to0\) for all continuously differentiable \(Y(x)\), it is necessary and sufficient that
\[
\sum_{j=0}^{p}a_j=1,\qquad\text{and}\qquad-\sum_{j=0}^{p}ja_j+\sum_{j=-1}^{p}b_j=1. \tag{1}
\]
Furthermore, for \(\tau(h)=O(h^m)\) for functions \(Y(x)\) that are \(m+1\) times continuously differentiable, it is necessary and sufficient that (1) hold and
\[
\sum_{j=0}^{p}(-j)^ia_j+i\sum_{j=-1}^{p}(-j)^{i-1}b_j=1,\qquad \text{for }i=2,3,\ldots,m.
\]

*Appendix: Recall that the Hermite polynomials can be written as
\[
H_n(x)=\sum_{j=1}^{n}f(x_j)h_j(x)+\sum_{j=1}^{n}f'(x_j)\tilde h_j(x).
\]
If the points \(x_j\) are chosen to be the zeros of the orthogonal polynomials on \([a,b]\), then
\[
\tilde h_j(x)=\frac{\psi_n(x)l_j(x)}{\psi_n'(x_j)},
\]
where \(l_j(x)\) is the Lagrange interpolant for \(x_j\).*
