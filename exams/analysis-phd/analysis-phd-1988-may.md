# Analysis, PhD exam, May 1988

*Answer seven out of the eight questions. Justify all work. To obtain any partial credit, all work must be presented in a neat and logical fashion.*

**1.** Prove that \(L^1(S,\mathcal A,\mu)\) is a complete space.

**2.** State and prove the Hahn–Banach theorem.

**3.** State and prove Fubini’s theorem.

**4.** Prove that there exists no sequence \((c_n)_{n=1}^{\infty}\) of real numbers such that an infinite series \(\sum a_n\) of real numbers converges if and only if \((c_n a_n)_{n=1}^{\infty}\) is a bounded sequence.

[Hint: Without loss of generality, assume such a sequence exists, with \(c_n\ne 0\) for all \(n\). Consider the mapping \(T:\ell_\infty\to\ell_1\) given by \(T((x_n))=\frac{x_n}{c_n}\) and use the open mapping theorem.]

**5.** Prove that there exists no Banach space of algebraic dimension \(\aleph_0\).

[Hint: show that a finite dimensional subspace is closed and then use the Baire category theorem.]

**6.** Let \(f:\mathbb R\to\mathbb R\) be a Lebesgue measurable function. Show that there exists a Borel measurable function \(g\) such that \(f=g\) a.e. (a.e. with respect to Lebesgue measure).

**7.** Let \(\mu\) be a measure on \(([0,\infty),\mathcal B([0,\infty)))\) defined by
\[
\mu(A)=\int_A x\,dx.
\]
Let \(T:[0,\infty)\to[0,\infty)\) be given by \(T(x)=e^x-1\). Define a new measure \(\pi\) on \(([0,\infty),\mathcal B([0,\infty)))\) by setting \(\pi(A)=\mu(T^{-1}(A))\). Compute \(d\pi/d\mu\).

**8.** Let \(\lambda\) be Lebesgue measure on \((\mathbb R,\mathcal B(\mathbb R))\). If \(A\in\mathcal B(\mathbb R)\), define the set \(-A=\{x:-x\in A\}\). Define \(\mathcal C=\{A\in\mathcal B(\mathbb R):A=-A\}\).
* Part (a) Show \(\mathcal C\) is a sigma-algebra.
* Part (b) Define two new measures \(\mu\) and \(\nu\) on the measurable space \((\mathbb R,\mathcal C)\) by setting
  \[
  \mu(A)=\int_A x\,dx \qquad\text{whenever }A\in\mathcal C,
  \]
  \[
  \nu(A)=\int_{A\cap[0,\infty)}x\,dx \qquad\text{whenever }A\in\mathcal C.
  \]
  Since \(\lambda\) may also be considered as a measure on \((\mathbb R,\mathcal C)\), we can find two \(\mathcal C\)-measurable functions \(d\mu/d\lambda\) and \(d\nu/d\lambda\) so that
  \[
  \mu(A)=\int_A \frac{d\mu}{d\lambda}\,dx \qquad\text{whenever }A\in\mathcal C,
  \]
  \[
  \nu(A)=\int_A \frac{d\nu}{d\lambda}\,dx \qquad\text{whenever }A\in\mathcal C.
  \]
  Compute these two functions.
