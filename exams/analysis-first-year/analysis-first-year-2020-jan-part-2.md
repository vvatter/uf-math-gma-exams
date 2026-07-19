# Analysis first year exam, January 2020, Part 2

*Do exactly 4 problems. Work must be presented in a neat and logical fashion in order to receive credit. Do not leave any gaps. When a theorem is used in a proof it must be precisely stated.*

**1.** Let \(f\) and \(f_n\) (\(n>0\)) be real-valued functions on \((0,1)\) with \(f_n\to f\). Decide (with proof) the truth/falsity of each of the following statements when the convergence of \(f_n\) to \(f\) is (a) pointwise (b) uniform:
* (i) if each \(f_n\) is increasing on \((0,1)\) then so is \(f\);
* (ii) if each \(f_n\) is bounded then so is \(f\).

**2.** Let \(f:[0,1]\times[0,1]\to\mathbb{R}\) be a continuous function and let \(\epsilon>0\). Prove that there exist finitely many continuous functions \(g_1,\ldots,g_n:[0,1]\to\mathbb{R}\) and \(h_1,\ldots,h_n:[0,1]\to\mathbb{R}\) such that
\[
\left|f(x,y)-\sum_{j=1}^{n}g_j(x)h_j(y)\right|<\epsilon \quad\text{for all }(x,y)\in[0,1]\times[0,1].
\]

**3.** Let \(f_n\) be a sequence of nonnegative measurable functions and suppose there is an \(L^1\) function \(g\) such that \(f_n\leq g\) for all \(n\). Prove that
\[
\limsup_{n\to\infty}\int f_n\leq\int\limsup_{n\to\infty}f_n.
\]
Give an example to show the conclusion can fail if the hypothesis \(f_n\leq g\) is removed.

**4.** Let \((X,\mathcal{M})\) be a measurable space and \(f_n:X\to\mathbb{R}\), \(n=1,2,3,\ldots\) a sequence of measurable functions. Prove that each of the following subsets of \(X\) is measurable:
* a) \(\{x\mid f_n(x)\to+\infty\}\);
* b) \(\{x\mid f_{n+1}(x)>f_n(x)\text{ for infinitely many }n\}\);
* c) \(\{x\mid f_n(x)\text{ is rational for all }n\}\).

**5.** Let \(E\subset[0,1]\) be a Lebesgue measurable set with \(m(E)>0\). Prove that there exists a point \(0<c<1\) such that
\[
m(E\cap[0,c])=\frac{1}{2}m(E).
\]
