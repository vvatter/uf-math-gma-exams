# Numerical Analysis, PhD exam, May 2012

*Answer any 8 questions.*

**1.** Suppose that \(A\) and \(B\in\mathbb{C}^{n\times n}\) are Hermitian matrices. If \(\sigma(A)\) denotes the largest eigenvalue of \(A\), then show that
\[
\sigma(A+B)\leq \sigma(A)+\sigma(B).
\]

**2.** Suppose that \(A\in\mathbb{C}^{n\times n}\) is an invertible matrix, \(u\in\mathbb{C}^n\), and \(v\in\mathbb{C}^n\). Let \(v^*\) denote the conjugate transpose of \(v\).
* (a) Show that
  \[
  \det(A-uv^*)=(1-v^*A^{-1}u)\det A.
  \]
* (b) Show that \(A-uv^*\) is invertible if and only if \(v^*A^{-1}u\neq 1\). Moreover, if \(v^*A^{-1}u\neq 1\), then
  \[
  (A-uv^*)^{-1}=A^{-1}+\left(\frac{1}{1-v^*A^{-1}u}\right)A^{-1}uv^*A^{-1}.
  \]

**3.** This problem has two parts.
* (a) Suppose \(p\) and \(q\in\mathbb{R}\) with \(p\) and \(q\) positive and \(p^{-1}+q^{-1}=1\). Show that for any matrix \(A\in\mathbb{C}^{m\times n}\), we have \(\lVert A\rVert_p=\lVert A^*\rVert_q\).
* (b) Prove that
  \[
  \lVert A\rVert_2^2\leq \lVert A\rVert_p\lVert A\rVert_q
  \]
  for any \(A\in\mathbb{C}^{m\times n}\) and any positive \(p\) and \(q\in\mathbb{R}\) with \(p^{-1}+q^{-1}=1\).

**4.** This problem has two parts.
* (a) For any matrices \(A\) and \(B\), show that the nonzero eigenvalues of \(AB\) and \(BA\) are the same.
* (b) If \(AB\) is normal, \(\lVert\cdot\rVert_2\) is the 2-norm of a matrix, and \(\lVert\cdot\rVert\) is an induced matrix norm, then show that \(\lVert AB\rVert_2\leq\lVert BA\rVert\).

**5.** Let \(P\) and \(Q\) be two \(m\times m\) orthogonal projectors. Prove that \(\lVert P-Q\rVert_2\leq 1\).

**6.** Consider the following minimization problem:
\[
\tau_n=\inf_{\deg Q<n}\left(\max_{x\in[-1,1]}\lvert x^n+Q(x)\rvert\right).
\]
Prove that \(\tau_n=\frac{1}{2^{n-1}}\), the infimum is in fact a minimum, attained at a unique \(Q^*\) satisfying
\[
x^n+Q^*(x)=\frac{1}{2^{n-1}}T_n(x),
\]
where \(\{T_n\}\) are the Chebyshev’s polynomials.

**7.** Design an algorithm with a cubic rate of convergence for computing the quantity \(\sqrt{5}\). Prove that your algorithm is indeed cubic. Find an interval \([a,b]\subset[0,+\infty)\) such that any iterative sequence starting in \([a,b]\) will converge to \(\sqrt{5}\).

**8.** State the classical Hermite interpolation problem. Prove that the problem is well-posed, i.e. prove the existence and uniqueness of solutions. Derive the error formula for the interpolating polynomial.

**9.** Describe Simpson’s Rule for numerical integration. State (without proof) the error formula of the Trapezoidal Rule. Show that the error bound cannot be improved.

**10.** Let \(w(x)>0\) be integrable on \([a,b]\). Define an orthogonal polynomial family \(\{\phi_n\}\) on \([a,b]\) with weight \(w(x)\). Prove that between two consecutive zeros of \(\phi_n\) there is exactly one zero of \(\phi_{n-1}\). You may use the triple recursion formula without proof.
