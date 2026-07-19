# Analysis, PhD exam, May 2016

*Do THREE problems from 1–4 (Part A) and THREE problems from 5–8 (Part B). Write solutions in a neat and logical fashion, giving complete reasons for all steps.*

**1.** Consider Lebesgue measure on the real line \(\mathbb{R}\). Give an example for each of the following, if possible. If not possible, give a brief explanation. A sequence \((f_n)\) in \(L^1(\mathbb{R})\) converging to an \(f\) in \(L^1(\mathbb{R})\)...
* a) ...in the \(L^1\) norm but not in measure,
* b) ...in measure but not in the \(L^1\) norm,
* c) ...in the \(L^1\) norm but not a.e.,
* d) ...a.e. but not in measure.

**2.** Let \(\nu\) be a signed measure on \((X,\mathcal{M})\).
* a) Define what it means for a set to be positive, negative or null for \(\nu\), and state the Hahn decomposition theorem.
* b) Prove there exist unique positive measures \(\nu^+,\nu^-\) on \(\mathcal{M}\) so that \(\nu=\nu^+-\nu^-\) and \(\nu^+\perp\nu^-\).

**3.** Let \(\mu\) be a finite, regular Borel measure on \([0,1]\). Suppose that
\[
\int_0^1 x^n\,d\mu=0 \qquad \text{for } n=0,1,2,\ldots
\]
Prove that \(\mu=0\).

**4.** Let \((X,\mathcal{M},\mu)\) be a \(\sigma\)-finite measure space. Let \(\mathcal{N}\) be a sub-\(\sigma\) algebra of \(\mathcal{M}\) and let \(\nu\) be the restriction of \(\mu\) to \(\mathcal{N}\). Prove that for each \(f\in L^1(\mu)\), there exists a \(g\in L^1(\nu)\) such that
\[
\int_E f\,d\mu=\int_E g\,d\nu
\]
for all \(E\in\mathcal{N}\).

**5.** Let \(\mathcal{X}\) be a normed vector space. Say a sequence \((x_n)\) from \(\mathcal{X}\) converges weakly to \(x\in\mathcal{X}\) if \(f(x_n)\to f(x)\) for all \(f\in\mathcal{X}^*\). Prove that if \(\mathcal{M}\) is a norm closed subspace of \(\mathcal{X}\), and \((x_n)\) is a sequence in \(\mathcal{M}\) converging weakly to \(x\in\mathcal{X}\), then \(x\in\mathcal{M}\).

**6.** Let \(\mathcal{H}\) be a Hilbert space and \(\mathcal{M},\mathcal{N}\) closed subspaces of \(\mathcal{H}\). Prove that if \(\mathcal{M}\perp\mathcal{N}\), then \(\mathcal{M}+\mathcal{N}\) is closed.

**7.** Fix \(1<p<\infty\), let \(\mu\) be a \(\sigma\)-finite measure, and let \((f_n)\) be a sequence in \(L^p(\mu)\). Suppose that there exists a function \(f\in L^p(\mu)\) such that
\[
\int f_ng\,d\mu\to\int fg\,d\mu
\]
for every \(g\in L^q(\mu)\), where \(\frac1p+\frac1q=1\).
* a) Prove that \(\sup_n\{\lVert f_n\rVert_p\}<+\infty\).
* b) Prove that \(\lVert f\rVert_p\leq\limsup\lVert f_n\rVert_p\).

**8.** Let \((\varphi_n)\) be a sequence in \(L^1(\mathbb{R})\) with the following properties. Prove that \(f*\varphi_n\to f\) in \(L^1(\mathbb{R})\).
* i) \(\varphi_n\geq 0\) for all \(n\),
* ii) \(\int_{\mathbb{R}}\varphi_n(x)\,dx=1\) for all \(n\), and
* iii) for every \(\delta>0\), \(\lim_{n\to\infty}\int_{|x|>\delta}\varphi_n(x)\,dx=0\).
