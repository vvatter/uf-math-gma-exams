# Numerical Analysis, PhD exam, January 2009

*Answer any 8 questions.*

**1.** Let \(M=\begin{bmatrix}A & B^t\\ B & C\end{bmatrix}\) be real symmetric and positive definite matrix. Let \(S=C-BA^{-1}B^t\) be the Schur complement. Prove that \(S\) is symmetric and positive definite.

**2.** Let \(\lVert\cdot\rVert_p\) for \(1\le p\le\infty\) denote the norm on \(m\times n\) matrices induced by the \(\ell^p\)-norm on vectors in \(\mathbb{C}^m\) and \(\mathbb{C}^n\). Prove that
\[
\lVert A\rVert_2\le \sqrt{\lVert A\rVert_1\lVert A\rVert_\infty},\qquad\text{for all }A\in\mathbb{C}^{m\times n}.
\]

**3.** Show that if \(P\) and \(Q\) be Hermitian positive definite matrices satisfying \(x^*Px\le x^*Qx\), for all \(x\in\mathbb{C}^n\), then \(\lVert P\rVert_F\le\lVert Q\rVert_F\).

**4.** Let \(T\) be any square matrix and let \(\lVert\cdot\rVert\) denote any induced norm. Prove that \(\displaystyle\lim_{n\to\infty}\lVert T^n\rVert^{1/n}\) exists and equals \(\displaystyle\inf_{n=1,2,\ldots}\lVert T^n\rVert^{1/n}\).

**5.** Let \(P\) and \(Q\) be two \(m\times m\) orthogonal projectors. Prove that \(\lVert P-Q\rVert_2\le 1\).

**6.** Let \(x_0,x_1,\ldots,x_n\) be distinct points in a finite interval \([a,b]\) and \(f\in C^1[a,b]\). Show that for any given \(\varepsilon>0\) there exists a polynomial \(p\) such that \(\lVert f-p\rVert_\infty<\varepsilon\) and \(p(x_i)=f(x_i)\) for all \(i=0,1,\ldots,n\) (where \(\lVert\cdot\rVert_\infty\) denotes the \(L^\infty(a,b)\)-norm).

**7.** Let \(\hat f(s)\) be the continuous Fourier transform of \(f(t)\in L^2[-\infty,\infty]\). Suppose further that \(\hat f(s)=0\) for \(|s|>\pi\). Derive the interpolation formula
\[
f(t)=\sum_{k=-\infty}^{\infty}f(k)\frac{\sin(\pi(t-k))}{\pi(t-k)}.
\]

**8.** Let \(L_n(f)\) be the Lagrange polynomial interpolating a function \(f\) at nodes \(a=x_0<x_1<\cdots<x_n=b\).
* (a) Give the formula for \(L_n(f)\).
* (b) Prove that there is a unique polynomial of degree at most \(n\) interpolating \(f\) at the nodes.
* (c) State and prove the formula for the error \(f(x)-L_n(f)(x)\) when \(f(x)\in C^{n+1}[a,b]\).

**9.** Assume that \(g\) is continuously differentiable real-valued function and \(a\le g(x)\le b\) on \([a,b]\). Show the following:
* (a) There is an \(\alpha\in[a,b]\) such that \(g(\alpha)=\alpha\).
* (b) If \(|g'(x)|<1\) on \([a,b]\), then there is only one fixed point on the interval \([a,b]\).
* (c) If we generate iterates using the recurrence \(x_{n+1}=g(x_n)\) starting from some \(x_0\in[a,b]\), then we have
  \[
  |\alpha-x_n|\le \frac{\lambda^n}{1-\lambda}|x_1-x_0|\qquad\text{where}\qquad \lambda=\max_{x\in[a,b]}|g'(x)|.
  \]

**10.** Let \(\{\phi_n(x):n\ge 0\}\) be an orthogonal family of polynomials on the interval \((a,b)\) with weight function \(w(x)\ge 0\) for all \(x\in[a,b]\). Show that the polynomial \(\phi_n(x)\) has exactly \(n\) distinct real roots in the open interval \((a,b)\).
