# Analysis, PhD exam, January 2024

*Write solutions in a neat and logical fashion, giving complete reasons for all steps. Attempt SIX problems.*

**1.** Let \((X,\mathcal{M},\mu)\) be a finite measure space. Let \((f_n)\) be a sequence of measurable functions and suppose that \(\sum_n \int |f_n|\,d\mu<\infty\). Consider the series \(\sum_n f_n(x)\). Does this series converge… Prove your claims.
* a) pointwise a.e.?
* b) in measure?
* c) in the \(L^1\) norm?

**2.** State Tonelli’s theorem, and give an example to show that the \(\sigma\)-finiteness hypothesis is necessary.

**3.** This problem has two parts.
* a) Let \(\nu\) be a signed measure on \((X,\mathcal{M})\). Define what it means for a set to be positive, negative or null for \(\nu\), and state the Hahn decomposition theorem.
* b) Prove that if \(\nu\) is a signed measure, then there exist unique positive measures \(\nu^+,\nu^-\) so that \(\nu=\nu^+-\nu^-\) and \(\nu^+\perp\nu^-\).

**4.** Let \(\varphi_n:\mathbb{R}\to\mathbb{C}\) be a sequence of Lebesgue measurable functions and suppose that there is a number \(M\) such that \(\|\varphi_n\|_\infty\le M\) for all \(n\). Prove that if
\[
\int_a^b \varphi_n(t)\,dt\to 0
\]
for every interval \([a,b]\subset\mathbb{R}\), then
\[
\int_{-\infty}^{\infty}\varphi_n(t)f(t)\,dt\to 0
\]
for every \(f\in L^1(\mathbb{R})\).

**5.** Let \(\mu\) and \(\nu\) be finite, positive measures defined on the same measurable space \((X,\mathcal{M})\), and suppose that \(\nu\ll\mu\).
* a) Prove that if \(L^1(\mu)\subset L^1(\nu)\), then the inclusion map \(\iota:L^1(\mu)\hookrightarrow L^1(\nu)\) is necessarily bounded.
* b) Prove that if \(L^1(\mu)\subset L^1(\nu)\) then \(\frac{d\nu}{d\mu}\in L^\infty(\mu)\).

**6.** Let \(\mathcal{X},\mathcal{Y}\) be Banach spaces and \(T:\mathcal{X}\to\mathcal{Y}\) a linear map. Prove that if \(f\circ T\in\mathcal{X}^*\) for all \(f\in\mathcal{Y}^*\), then \(T\) is bounded.

**7.** Short answer.
* a) Explain why there is no norm on \(c_{00}\) (the space of finitely nonzero sequences) which makes it into a Banach space.
* b) Explain why there is no bounded, surjective linear map from \(c_0\) onto \(\ell^\infty\).
* c) Explain why the norm in \(L^1(\mathbb{R})\) cannot be given by an inner product.

**8.** Let \(H\) be a Hilbert space with orthonormal basis \(\{e_k\}_{k=1}^\infty\). Let \((h_n)\) be a sequence in \(H\) and let \(h\in H\). Prove that the following statements are equivalent:
* 1) \(\langle h_n,g\rangle\to\langle h,g\rangle\) for all \(g\in H\).
* 2) \(\langle h_n,e_k\rangle\to\langle h,e_k\rangle\) for all \(k=1,2,\ldots\), AND \(\sup_n\|h_n\|<\infty\).
