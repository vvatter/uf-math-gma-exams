# Analysis, PhD exam, June 1996

*In the sequel the word measure means positive, countably additive measure, unless otherwise stated. Do all of the following problems.*

**1.** Let \(f_n:\mathbb R\to\mathbb R\) be a sequence of Lebesgue-measurable functions which converges pointwise to a function \(g\). Prove, directly from the definition of measurability, that \(g\) is measurable.

**2.** For \(f\in L^1(\mathbb R)\), let \(f_t\) denote the translation of \(f\) by \(t\), i.e. \(f_t(x):=f(x-t)\). Show that the map \(t\mapsto f_t\) is a continuous map from \(\mathbb R\) to \(L^1(\mathbb R)\).

**3.** Let \(\mu\) denote the Lebesgue measure on \(\mathbb R\). Let \(T:\mathbb R\to\mathbb R\) be defined by \(T(x)=x^3-x\). Define a Borel measure \(\nu\) setting \(\nu(A):=\mu(T^{-1}A)\). Compute the Radon–Nikodym derivative \(\frac{d\nu}{d\mu}\).

**4.** Let \(K_n\subset[0,1]\) be a Cantor set of Lebesgue measure larger than \(1-\frac1n\). Let \(V:=\bigcup_{n=1}^{\infty}K_n\). Prove that, for any nullset \(N\), the set \(V\setminus N\) is not a \(G_\delta\) set. [Hint: Baire Category Theorem]

**5.** Let \(\mu\) and \(\nu\) be \(\sigma\)-finite measures on the measurable space \((X,\mathcal B)\). Prove, from first principles, that \(\nu\) can be written as \(\nu=\nu_{\mathrm{ac}}+\nu_{\mathrm{sing}}\), with \(\nu_{\mathrm{ac}}\ll\mu\) and \(\nu_{\mathrm{sing}}\perp\mu\).

**6.** Let \(x_n\) be a sequence in a Banach space \(B\). Assume that that the sequence \(x_n\) converges weakly to \(x\).
* (a) Show that \(x\) is the only weak limit of the sequence \(x_n\).
* (b) Show that \(\sup_n\lVert x_n\rVert<\infty\). [Hint for (b): Consider the \(x_n\) as elements of the double dual \(B^{**}\)]

**7.** Let \(K:[0,2\pi]\to\mathbb R\) be defined by \(K(x)=\frac14\sin(x)\). Show that for every \(h\in L^p([0,2\pi])\), there exists a unique solution \(f\) to the equation
\[
f+f*K=h.
\]
If \(h\) is \(C^\infty\), is it true that the solution \(f\) is \(C^\infty\)? Justify your answer.

**8.** A distribution \(T\) is called harmonic if \(\Delta T=0\), where \(\Delta=\sum_{j=1}^n\frac{\partial^2}{\partial x_j^2}\). Show that if \(T\) is a harmonic tempered distribution, then \(T\) is a polynomial. [Hint: a distribution with support \(\{0\}\) is a finite sum of multiples of Dirac’s \(\delta\) and its derivatives.]
