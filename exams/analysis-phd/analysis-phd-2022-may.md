# Analysis PhD exam, May 2022

*Write solutions in a neat and logical fashion, giving complete reasons for all steps. Attempt SIX problems.*

**1.** State Tonelli’s theorem, and give an example to show that the \(\sigma\)-finiteness hypothesis is necessary.

**2.** Let \(\mu\) be a positive measure and let \((E_n)\) be a sequence of measurable sets with \(\mu(E_n)<\infty\) for all \(n\). Prove that if \(\mathbf{1}_{E_n}\to f\) in \(L^1(\mu)\), then there exists a measurable set \(E\) so that \(f=\mathbf{1}_E\) a.e. and \(\mu(E)=\lim \mu(E_n)\).

**3.** Let \(\mu\) and \(\nu\) be finite, positive measures defined on the same measurable space \((X,\mathcal{M})\), and suppose that \(\nu\ll\mu\).
* a) Prove that if \(L^1(\mu)\subset L^1(\nu)\), then the inclusion map \(\iota:L^1(\mu)\hookrightarrow L^1(\nu)\) is necessarily bounded.
* b) Prove that if \(L^1(\mu)\subset L^1(\nu)\) then \(\frac{d\nu}{d\mu}\in L^\infty(\mu)\).

**4.** Let \(\mu\) be a positive measure and suppose that \(1<p<r<q<\infty\). Prove that
\[
L^r(\mu)\subset L^p(\mu)+L^q(\mu).
\]
(That is, every \(f\in L^r(\mu)\) can be written as a sum \(f=g+h\) where \(g\in L^p(\mu)\) and \(h\in L^q(\mu)\).)

**5.** Let \(\mathcal{X}\) be a Banach space, and let \(\mathcal{M},\mathcal{N}\) be closed subspaces of \(\mathcal{X}\). Suppose that every \(x\in\mathcal{X}\) can be decomposed uniquely as
\[
x=m+n
\]
with \(m\in\mathcal{M}\), \(n\in\mathcal{N}\). Prove that the assignment \(x\to m\) defines a bounded linear operator from \(\mathcal{X}\) to \(\mathcal{M}\).

**6.** This problem has two parts.
* a) Prove that for each integer \(n\ge 0\), there exists a function \(f_n\in L^2[0,1]\) such that for every polynomial \(p\) of degree at most \(n\),
  \[
  p(1)=\int_0^1 p(x)f_n(x)\,dx.
  \]
  Is \(f_n\) unique?
* b) Is there a function \(f\in L^2[0,1]\) such that
  \[
  p(1)=\int_0^1 p(x)f(x)\,dx
  \]
  for all polynomials \(p\)? Prove or disprove.

**7.** This problem has two parts.
* a) State the Banach Isomorphism Theorem and the Closed Graph Theorem.
* b) Using the Banach Isomorphism Theorem (or otherwise), prove the Closed Graph Theorem.

**8.** (Short answer, you do not need to give a detailed proof, just a brief explanation.)
* a) Define the Fourier transform on \(L^1(\mathbb{R})\) and sketch its extension to \(L^2(\mathbb{R})\).
* b) Sketch a construction of a bounded linear functional \(\lambda\) on \(L^\infty(\mathbb{R})\) which is not of the form \(\lambda(f)=\int f(x)g(x)\,dx\) for any \(L^1\) function \(g\).
* c) Sketch a proof of the fact that there is no norm under which \(c_{00}\) is complete.
