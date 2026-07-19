# Analysis, PhD exam, May 2024

*Write solutions in a neat and logical fashion, giving complete reasons for all steps.*

*Attempt SIX problems.*

**1.** Consider Lebesgue measure on the real line \(\mathbb{R}\). Give an example for each of the following, if possible. If not possible, give a brief explanation. A sequence \(f_n\) in \(L^1(\mathbb{R})\) converging to an \(f\) in \(L^1(\mathbb{R})\)...
* a) ...in the \(L^1\) norm but not in measure,
* b) ...in measure but not in the \(L^1\) norm,
* c) ...in the \(L^1\) norm but not a.e.,
* d) ...a.e. but not in measure.

**2.** State Tonelli’s theorem, and give an example to show that the \(\sigma\)-finiteness hypothesis is necessary.

**3.** For \(\sigma\)-finite measures \(\mu\) and \(\nu\), define what it means for \(\mu\) to be absolutely continuous with respect to \(\nu\), and singular with respect to \(\nu\). State the Lebesgue–Radon–Nikodym theorem.

**4.** Let \((X,\mathcal{M},\mu)\) be a \(\sigma\)-finite measure space. Suppose that \(g\) is a measurable function with the property that \(gf\in L^2\) for all \(f\in L^2\). Prove that \(g\in L^\infty\).

**5.** Fix \(1<p<\infty\), let \(\mu\) be a \(\sigma\)-finite measure, and let \((f_n)\) be a sequence in \(L^p(\mu)\). Suppose that there exists a function \(f\in L^p(\mu)\) such that
\[
\int f_n g\,d\mu \to \int fg\,d\mu
\]
for every \(g\in L^q(\mu)\), where \(\frac{1}{p}+\frac{1}{q}=1\).
* a) Prove that \(\sup_n\{\lVert f_n\rVert_p\}<+\infty\).
* b) Prove that \(\lVert f\rVert_p\leq\limsup\lVert f_n\rVert_p\).
* c) Give an example to show that strict inequality can hold in part (b).

**6.** Let \(\mathcal{X}\) be a normed vector space. Say \(x_n\to x\) weakly if \(f(x_n)\to f(x)\) for all \(f\in\mathcal{X}^*\). Prove that if \(\mathcal{M}\) is a norm closed subspace of \(\mathcal{X}\), and \((x_n)\) is a sequence in \(\mathcal{M}\) converging weakly to \(x\), then \(x\in\mathcal{M}\).

**7.** Let \(\mu\) be a finite signed Borel measure on \([0,1]\). Suppose that
\[
\int_0^1 \sin(2\pi nx)\,d\mu(x)=0 \quad\text{and}\quad \int_0^1 \cos(2\pi nx)\,d\mu(x)=0
\]
for all \(n=0,1,2,\ldots\). Prove that \(\mu=0\). Does it suffice to assume only the vanishing of the sine integrals? Prove, or give a counterexample.

**8.** Short answer.
* a) Give a brief explanation of how the Fourier transform is defined on \(L^2(\mathbb{R})\).
* b) Sketch a proof that the Banach space \(L^1(\mathbb{R})\) is not reflexive.
* c) Explain why the norm in \(\ell^1(\mathbb{N})\) cannot be given by an inner product.
