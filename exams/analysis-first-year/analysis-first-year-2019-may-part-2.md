# Analysis first year exam, May 2019, Part 2

*Do exactly 4 problems. Work must be presented in a neat and logical fashion in order to receive credit. Do not leave any gaps. When a theorem is used in a proof it must be precisely stated.*

**1.** Let \(f_n:[a,b]\to\mathbb{R}\) be a uniformly bounded sequence of Riemann integrable functions. Prove that if \(f_n\to f\) uniformly, then \(f\) is Riemann integrable.

**2.** Let \(f:[0,1]\to\mathbb{R}\) be continuous. Suppose that
\[
\int_0^1 f(x)x^{2019k}\,dx=0
\]
for all integers \(k\ge 0\). Must \(f\) be identically \(0\)? Prove, or give a counterexample.

**3.** Let \(f_n:[0,1]\to\mathbb{R}\) be a sequence of measurable functions and suppose there is a function \(g\in L^1[0,1]\) such that \(|f_n|\le g\) for all \(n\). Consider the functions
\[
F_n(t)=\int_0^t f_n(x)\,dx.
\]
Prove
* i) each \(F_n\) is continuous on \([0,1]\)
* ii) there is a subsequence \((F_{n_k})\) converging uniformly on \([0,1]\).

**4.** Let \((X,\mathcal{M})\) be a measurable space and \(f_n:X\to\mathbb{R}\), \(n=1,2,3,\ldots\), a sequence of measurable functions. Prove that each of the following subsets of \(X\) is measurable:
* a) \(\{x\mid f_n(x)>0\text{ for infinitely many values of }n\}\)
* b) \(\{x\mid \text{the sequence }(f_n(x))\text{ is eventually monotone}\}\)
* c) \(\left\{x\,\middle|\,\displaystyle\lim_{n\to\infty}n f_n(x)=0\right\}\)

**5.** Let \(f_1\ge f_2\ge f_3\ge\cdots\) be nonnegative measurable functions on a measure space \((X,\mathcal{M},\mu)\), and put \(f=\lim f_n\). Suppose that \(\int f_k\,d\mu<\infty\) for some \(k\). Prove that
\[
\int f\,d\mu=\lim\int f_n\,d\mu.
\]
Give a counterexample to show that the conclusion can fail if the finiteness hypothesis is dropped.
