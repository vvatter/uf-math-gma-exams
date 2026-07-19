# Complex Analysis PhD exam, May 2006

*Give complete proofs and computations. Partial credit will be given where justified.*

**1.** Let \(0<a<1\). Evaluate the integral
\[
\int_{-\infty}^{\infty}\frac{e^{ax}}{1+e^x}\,dx,
\]
where \(a\in(0,1)\).

**2.** This problem has two parts.
* (a) Prove that
  \[
  \cos \pi z=\prod_{n=1}^{\infty}\left(1-\frac{4z^2}{(2n-1)^2}\right).
  \]
* (b) Deduce from (a) that
  \[
  \tan \pi z=\frac{8}{\pi}\sum_{n=1}^{\infty}\frac{z}{(2n-1)^2-4z^2}.
  \]

**3.** Let \(G\) be a region and \(u:G\to\mathbb{R}\) be harmonic. Let \(v\) be a harmonic conjugate to \(u\) in \(G\). Show that the product \(u\cdot v\) is harmonic.

**4.** This problem has two parts.
* (a) Show that if \(f\) is analytic on the closed disk \(\overline{B(0;1)}\), then
  \[
  |f(a)|^2\leq \frac{1}{\pi R^2}\int_0^{2\pi}\int_0^R|f(a+re^{i\theta})|^2r\,dr\,d\theta.
  \]
* (b) Let \(G\) be a region and \(M\in\mathbb{R}\) be fixed. Let
  \[
  \mathcal{F}=\left\{f\in H(G)\mathrel{\bigg|}\int_G|f(z)|^2\,dx\,dy\leq M\right\}.
  \]
  Show that \(\mathcal{F}\) is a normal family.

**5.** Let \(f(z)=\sum_{n=0}^{\infty}a_nz^n\) and \(g(z)=\sum_{n=0}^{\infty}b_nz^n\) be analytic on \(\overline{B(0;1)}\). Let
\[
F(z)=\frac{1}{2\pi i}\int_{\partial B(0;1)}\frac{f(w)}{w}g\left(\frac{z}{w}\right)\,dw,\qquad z\in B(0;1),
\]
with the contour taken with counterclockwise orientation. Show that
\[
F(z)=\sum_{n=0}^{\infty}a_nb_nz^n,\qquad z\in B(0;1).
\]

**6.** Let \(G=\{z\in\mathbb{C}\mid |z|<1\text{ and }|2z-1|>1\}\), and let \(f\in H(G)\).
* (a) Must there exist a sequence of polynomials \(P_n\) such that \(P_n\to f\) uniformly on compact subsets of \(G\)? Explain your reasoning.
* (b) Must there exist such a sequence which converges to \(f\) uniformly on \(G\)? Explain your reasoning.
* (c) Must there exist such a sequence which converges to \(f\) uniformly on \(G\), if \(f\) is now required to be analytic in some neighborhood of \(\overline{G}\)? Explain your reasoning.

**7.** Let \(G\) be a region and \(A\) be a discrete and relatively closed subset of \(G\). Assume that \(f\in H(G\setminus A)\) is injective.
* (a) Prove that no point of \(A\) can be an essential singularity of \(f\).
* (b) Prove that if \(a\in A\) is a pole for \(f\), then \(a\) is a pole of order 1.

**8.** Let \(f\) be analytic on \(\overline{B(0;1)}\). If \(|f(z)|<1\) on \(\partial B(0;1)\), prove that there exists a unique \(z_0\in B(0;1)\) (counting multiplicity) such that \(f(z_0)=z_0\). If \(|f(z)|\leq 1\) on \(\partial B(0;1)\), does the same conclusion hold? Justify your assertion.
