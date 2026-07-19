# Numerical Analysis, PhD exam, January 2026

*Do 4 (four) of the first 5 (1–5) and 4 (four) of the last 5 problems (6–10).*

**1.** Prove each of the following.
* (a) The matrix 2-norm is invariant under unitary transformation.
* (b) If \(n \times n\) matrix \(A\) is diagonal, then for any matrix \(p\)-norm \(\|\cdot\|_p\), it holds that \(\|A\|_p = \max_{1\leq i\leq n}|a_{ii}|\).

**2.** Suppose \(A\in\mathbb{C}^{m\times n}\). Prove or provide a counterexample for each of the following.
* (a) The Frobenius norm of a matrix is induced by (subordinate to) a vector norm.
* (b) \(\|A\|_2\leq\|A\|_F\leq\sqrt{n}\|A\|_2\).

**3.** Let \(A\in\mathbb{C}^{n\times n}\). You may use the fact (if you find it useful) That \(A\) has a Schur decomposition. Prove or provide a counterexample for each of the following.
* (a) If \(A\) is both normal and triangular then it is diagonal.
* (b) If \(A\) is normal then the 2-norm of \(A\) is equal to it’s spectral radius \(\rho(A)\).

**4.** This problem has two parts.
* (a) Let \(r_i=\sum_{j=1,j\ne i}^n|a_{ij}|\). Let \(D_i\) be the disk in \(\mathbb{C}\) with center \(a_{ii}\) and radius \(r_i\). Prove that if \(\lambda\) is an eigenvalue of \(A\), then \(\lambda\in\bigcup_i D_i\); in other words, \(\lambda\) is in at least one of the disks \(D_i\).
* (b) Determine all eigenvalues of the Householder reflector \(H(w)\), including their multiplicities. Justify your answer.

**5.** Define the matrices \(A\) and \(B\) by
\[
A=\begin{pmatrix}1&3&0\\1&3&0\\1&3&0\\1&3&0\end{pmatrix},\qquad B=\begin{pmatrix}1&0&1\\0&2&0\\1&0&0\\0&0&1\end{pmatrix}.
\]
* (a) Find a full singular value decomposition of \(A\).
* (b) Find an economy QR decomposition of \(B\).

**6.** Consider the function \(g(x)=e^{-x}\).
* (a) Prove that \(g\) is a contraction on \(G=[\ln 1.1,\ln 3]\).
* (b) Prove that \(g\) maps \(G=[\ln 1.1,\ln 3]\) into \(G=[\ln 1.1,\ln 3]\).
* (c) Prove that \(x_{k+1}=g(x_k)\) converges to an unique fixed point \(z\in G=[\ln 1.1,\ln 3]\) for any initial value \(x_0\in G=[\ln 1.1,\ln 3]\).

**7.** Consider the finite difference formula
\[
f'(t_j)=\frac{1}{12h}\bigl[f(t_j-2h)-8f(t_j-h)+8f(t_j+h)-f(t_j+2h)\bigr]+O(h^4).
\]
* (a) Derive this formula by using Taylor’s theorem.
* (b) Derive this formula by using Lagrange polynomial representation.

**8.** Given a differentiable function \(f(x)\), consider the problem of finding a polynomial \(p(x)\in\mathbb{P}^n\) such that
\[
p(x_0)=f(x_0),\qquad p'(x_i)=f'(x_i),\qquad i=1,2,\ldots,n,
\]
where \(x_i\), \(i=1,2,\ldots,n\), are distinct nodes. (It is not excluded that \(x_1=x_0\).) Show that the problem has a unique solution and describe how it can be obtained.

**9.** Let \(Q_m(f)\) denote the \(m\)-point Gaussian quadrature rule over the interval \([a,b]\) and with continuous weight function \(\rho(x)\geq 0\), that is,
\[
Q_m(f)=\sum_{i=1}^m\alpha_i f(x_i)\approx J(f)=\int_a^b\rho(x)f(x)\,dx.
\]
Show that, if \(a\) and \(b\) are finite and \(f\) is continuous, then \(Q_m(f)\to J(f)\) as \(m\to\infty\).

**10.** Consider numerically solving the initial value problem
\[
y'(t)=f(t,y),\quad 0<t\leq t_f,\qquad\text{with }y(0)=\eta.
\]
Assume \(f\) is sufficiently differentiable and let \(h\) denote the step size. Show that all convergent members of the family of methods
\[
y_{n+2}+(\theta-2)y_{n+1}+(1-\theta)y_n=\frac14h\bigl[(6+\theta)f_{n+2}+3(\theta-2)f_n\bigr],
\]
parameterized by \(\theta\), are also \(A_0\)-stable.
