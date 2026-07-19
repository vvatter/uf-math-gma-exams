# Numerical Analysis PhD exam, September 2011

*Answer any 8 questions.*

**1.** This problem has two parts.
* (a) For any matrices \(A\) and \(B\), show that the nonzero eigenvalues of \(AB\) and \(BA\) are the same.
* (b) If \(AB\) is normal, \(\lVert\cdot\rVert_2\) is the 2-norm of a matrix, and \(\lVert\cdot\rVert\) is an induced matrix norm, then show that \(\lVert AB\rVert_2\leq \lVert BA\rVert\).

**2.** This problem has two parts.
* (a) Suppose \(p\) and \(q\in\mathbb{R}\) with \(p\) and \(q\) positive and \(p^{-1}+q^{-1}=1\). Show that for any matrix \(A\in\mathbb{C}^{m\times n}\), we have \(\lVert A\rVert_p=\lVert A^*\rVert_q\).
* (b) Prove that
  \[
  \lVert A\rVert_2^2\leq \lVert A\rVert_p\lVert A\rVert_q
  \]
  for any \(A\in\mathbb{C}^{m\times n}\) and any positive \(p\) and \(q\in\mathbb{R}\) with \(p^{-1}+q^{-1}=1\).

**3.** Let \(P\) and \(Q\) be two \(m\times m\) orthogonal projectors. Prove that \(\lVert P-Q\rVert_2\leq 1\).

**4.** Let \(P\) and \(Q\) be Hermitian positive definite matrices. Prove that
\[
x^*Px\leq x^*Qx\quad\text{for all }x\in\mathbb{C}^n
\]
if and only if
\[
x^*Q^{-1}x\leq x^*P^{-1}x\quad\text{for all }x\in\mathbb{C}^n.
\]

**5.** Suppose \(A\) is a Hermitian positive definite matrix split into \(A=C+C^*+D\) where \(D\) is also Hermitian positive definite. Prove that \(B=C+\omega^{-1}D\) is invertible whenever \(0<\omega<2\). Consider the iteration \(x_{n+1}=x_n+B^{-1}(b-Ax_n)\), with any initial iterate \(x_0\). Prove that \(x_n\) converges to \(x=A^{-1}b\) whenever \(0<\omega<2\).

**6.** Let \(f:R\to R\) be a contraction with constant \(\lambda\in(0,1)\). Prove that there exists a unique fixed point \(\alpha\) of \(f\). Prove the inequality
\[
\lvert f^n(x)-\alpha\rvert\leq \frac{\lambda^n}{1-\lambda}\lvert f(x)-x\rvert,\qquad \forall x\in R,\ \forall n\in N.
\]

**7.** Derive the two point Gaussian quadrature for approximating \(\int_{-1}^1 f(x)x^2\,dx\).

**8.** State the Hermite interpolation problem. Prove that the problem is well-posed, i.e. prove the existence and uniqueness of solutions. Derive the error formula for the interpolating polynomial.

**9.** Describe Simpson’s rule for numerical integration (\(n=3\)). State and prove the error formula of Simpson’s rule.

**10.** Let \(w(x)>0\) be integrable on \([a,b]\). Define an orthogonal polynomial family \(\{\phi_n\}\) on \([a,b]\) with weight \(w(x)\). Prove that
* (i) \(\phi_n(x)\) has \(n\) distinct roots in the interval \((a,b)\), and
* (ii) between any two consecutive zeros of \(\phi_n\) there is a zero of \(\phi_{n-1}\).
