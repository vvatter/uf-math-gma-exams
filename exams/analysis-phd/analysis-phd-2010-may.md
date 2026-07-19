# Analysis, PhD exam, May 2010

*Write solutions in a neat and logical fashion, giving complete reasons for all steps. Do any seven problems.*

**1.** Consider Lebesgue measure on the real line \(\mathbb{R}\). Give an example for each of the following, if possible. If not possible, give a brief explanation. A sequence \(f_n\) in \(L^1(\mathbb{R})\) converging to an \(f\) in \(L^1(\mathbb{R})\)... Which of these answers change if we replace \(\mathbb{R}\) by the interval \([0,1]\)?
* a) ...in the \(L^1\) norm but not in measure,
* b) ...in measure but not in the \(L^1\) norm,
* c) ...in the \(L^1\) norm but not a.e.,
* d) ...a.e. but not in measure.

**2.** Define the Hardy–Littlewood maximal function. State and prove the Hardy–Littlewood maximal theorem. (Begin by proving an appropriate covering lemma.)

**3.** This problem has two parts.
* a) State Egorov’s theorem.
* b) Suppose \((X,\mathcal{M},\mu)\) is a measure space with \(\mu(X)<\infty\) and \(f:X\to\mathbb{C}\) is measurable. Let \((f_n)\) be a sequence of integrable functions such that \(f_n\to f\) a.e. Suppose further that the sequence \(f_n\) is uniformly integrable, that is, for every \(\epsilon>0\) there exists a \(\delta>0\) such that if \(E\) is measurable and \(\mu(E)<\delta\), then
  \[
  \int_E |f_n|\,d\mu<\epsilon.
  \]
  Prove that \(f\) is integrable and
  \[
  \lim_{n\to\infty}\int_X |f_n-f|\,d\mu=0.
  \]

**4.** Let \(\mathcal{X},\mathcal{Y}\) be Banach spaces. Suppose that \((T_n)\) is a sequence of bounded linear operators from \(\mathcal{X}\) to \(\mathcal{Y}\) such that \(\lim_{n\to\infty}T_nx\) exists for every \(x\in\mathcal{X}\). Prove that
\[
Tx:=\lim_{n\to\infty}T_nx
\]
defines a bounded linear operator from \(\mathcal{X}\) to \(\mathcal{Y}\).

**5.** This problem has two parts.
* a) State the Lebesgue–Radon–Nikodym theorem.
* b) State and prove a version of the chain rule for Radon–Nikodym derivatives.

**6.** Let \(X\) be a normed vector space. Given \(x\in X\), define a linear functional \(\hat{x}:X^*\to\mathbb{C}\) by \(\hat{x}(f)=f(x)\). Prove that the map \(x\to\hat{x}\) is an isometry from \(X\) into \(X^{**}\).

**7.** Let \(\mathcal{H}\) be a Hilbert space and suppose \(\mathcal{M},\mathcal{N}\) are closed subspaces with \(\mathcal{M}\perp\mathcal{N}\). Prove that \(\mathcal{M}+\mathcal{N}\) is closed.

**8.** Suppose \((k_n)_{n=1}^{\infty}\) is a sequence of functions in \(L^1(\mathbb{R})\) satisfying the following. Prove that
\[
\lim_{n\to\infty}\|f-f*k_n\|_1=0
\]
for all \(f\in L^1(\mathbb{R})\). (Here \(*\) denotes convolution: \((f*g)(x):=\int_{-\infty}^{\infty}f(x-t)g(t)\,dt\).)
* a) \(\displaystyle \int_{-\infty}^{\infty}k_n(t)\,dt=1\) for all \(n\),
* b) \(\displaystyle \sup_n\int_{-\infty}^{\infty}|k_n(t)|\,dt<\infty\), and
* c) for each \(\delta>0\), \(\displaystyle \sup_{|t|\geq\delta}\{|k_n(t)|\}\to0\) as \(n\to\infty\).
