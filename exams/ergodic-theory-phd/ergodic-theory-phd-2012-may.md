# Ergodic Theory PhD exam, May 2012

*Do all problems.*

*Notation:*
*• The statement that \((X,\mathcal{B},\mu,f)\) is a mpt (measure preserving transformation) means that \(X\) is a set with the probability measure \(\mu\) defined on the \(\sigma\)-algebra \(\mathcal{B}\) and \(f\) is a bijective, bi-measurable map \(f:X\to X\) which preserves the measure \(\mu\).*
*• The statement that \((X,d,\mathcal{B},\mu,f)\) is a mph (measure preserving homeomorphism) means that \((X,\mathcal{B},\mu,f)\) is a mpt and in addition, \((X,d)\) is a compact metric space, \(f\) is a homeomorphism, and \(\mathcal{B}\) is the Borel \(\sigma\)-algebra.*

**1.** Let \((X,d)\) be a compact metric space and \(f:X\to X\) a homeomorphism.
* (a) Define the recurrent set \(\Lambda(f)\) and the nonwandering set \(\Omega(f)\) and show they are both compact, invariant sets.
* (b) Show that \(\Lambda(f)\subset\Omega(f)\) and give an example where the inclusion is proper.
* (c) Define the omega-limit set \(\omega(x,f)\) of a point \(x\in X\) and show it is a compact, invariant set.
* (d) Prove or disprove: For every \(x\in X\), that \(\omega(x,f)\subset\Lambda(f)\).

**2.** Let \((X,d)\) be a compact metric space and \(f:X\to X\) a homeomorphism.
* (a) Show that there is always an \(f\)-invariant subset \(Z\subset X\) so that \(f\) restricted to \(Z\) is minimal.
* (b) Show that there is always a measure \(\mu\) so that \((X,d,\mathcal{B},\mu,f)\) is a mph.

**3.** Assume \((X,d,\mathcal{B},\mu,f)\) is a mph.
* (a) Define the support, \(\operatorname{supp}(\mu)\), of the measure \(\mu\) and show it is a compact, invariant set.
* (b) Show that almost every point in \(\operatorname{supp}(\mu)\) is recurrent.
* (c) Show that every point in \(\operatorname{supp}(\mu)\) is nonwandering.
* (d) Show that \(\mu(\Omega(f))=1\).
* (e) If \((X,d,\mathcal{B},\mu,f)\) is ergodic, show that \(f\) is full orbit transitive on \(\operatorname{supp}(\mu)\).
* (f) Show that \(\operatorname{supp}(\mu)\subset\Lambda(f)\), where \(\Lambda(f)\) is the recurrent set of \(f\).

**4.** State carefully with complete hypothesis.
* (a) Birkhoff’s pointwise ergodic theorem
* (b) von Neumann’s \(L^2\)-mean ergodic theorem

**5.** Let
\[
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
* (a) Define the one-sided subshift of finite type \(\Sigma_A^+\) determined by \(A\) and the shift map \(\sigma:\Sigma_A^+\to\Sigma_A^+\).
* (b) Define one of the standard metrics on \(\Sigma_A^+\).
* (c) Show that periodic points of \(\sigma\) are dense in \(\Sigma_A^+\).
* (d) Show that \((\Sigma_A^+,\sigma)\) is forward orbit transitive.
* (e) Let \(N_k\) be the number of fixed points of \(\sigma^k\) in \(\Sigma_A^+\). Compute explicitly
  \[
  \lim_{k\to\infty}\frac{\log(N_k)}{k}
  \]
  and justify your answer completely.

**6.** Fix a \(p\) with \(0<p<1\).
* (a) Define the Bernoulli measure \(\mu_p\) on the two-sided shift on two symbols \(\Sigma_2\).
* (b) Show that \((\Sigma_2,\mathcal{B},\sigma,\mu_p)\) is strong mixing (you don’t have to prove it is a mpt, you may assume that is true).
* (c) Define \(\alpha:\Sigma_2\to\mathbb{R}\) by
  \[
  \alpha(\ldots s_{-1}s_0s_1s_2\ldots)=2s_{-1}-s_0+s_2^2.
  \]
  Compute the following limit for \(\mu_p\)-almost every sequence \(\underline{s}\in\Sigma_2\):
  \[
  \lim_{N\to\infty}\frac{1}{N}\sum_{i=0}^{N-1}\alpha(\sigma^i(\underline{s})).
  \]
  and justify your answer completely.

**7.** Let \(f:\mathbb{R}^2\to\mathbb{R}^2\) be defined by \(f(x,y)=(3x,(1/2)y)\).
* (a) Show that the origin is an unstable fixed point for \(f\).
* (b) Find an invariant, Borel probability measure for \(f\) (Hint: don’t try too hard).
* (c) Show that your invariant measure in (b) is the only invariant, Borel probability measure.
