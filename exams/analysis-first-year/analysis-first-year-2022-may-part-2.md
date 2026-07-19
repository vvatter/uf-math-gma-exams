# Analysis, first year exam, May 2022, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** Let \(f:[a,b]\to\mathbb{R}\) have the property that for each \(\varepsilon>0\) there exist Riemann integrable functions \(\ell\) and \(u\) on \([a,b]\) such that \(\ell\leq f\leq u\) and \(\int_a^b(u-\ell)<\varepsilon\). Does it follow that \(f\) is Riemann integrable on \([a,b]\)? Proof or counterexample.

**2.** Suppose \((p_n)_{n=0}^{\infty}\) is a sequence of polynomials in one variable.
* (i) Assume that \(p_n\to f\) uniformly on \([0,1]\) as \(n\to\infty\); deduce as much as possible about the function \(f:[0,1]\to\mathbb{R}\).
* (ii) Assume that \(p_n\to f\) uniformly on \(\mathbb{R}\) as \(n\to\infty\); deduce as much as possible about the function \(f:\mathbb{R}\to\mathbb{R}\).

**3.** Let the continuous function \(f:[0,1]\to\mathbb{R}\) satisfy
\[
\int_0^1 f(t)t^n\,dt=1/(n+2)
\]
for all but finitely many positive integers \(n\). Deduce as much as possible about \(f\).

**4.** Let \((f_n)_{n=0}^{\infty}\) be a sequence of measurable real-valued functions on some measurable space. Prove that each of the following sets is measurable:
* (i) \(A=\{\omega:\sum_{n=0}^{\infty}f_n(\omega)\text{ is absolutely convergent}\}\);
* (ii) \(C=\{\omega:\sum_{n=0}^{\infty}f_n(\omega)\text{ is conditionally convergent}\}\).

**5.** Let \((\Omega,\mathcal{A},\mu)\) be a measure space; let \(A_0\subseteq A_1\subseteq\cdots\) be an increasing sequence in \(\mathcal{A}\) such that \(\bigcup_{n=0}^{\infty}A_n=\Omega\); let \(f:\Omega\to\mathbb{R}\) be measurable; and let \(L\) be a real number. Consider the statements:

Prove that (i) implies (ii) and decide (with proof or counterexample) whether (ii) implies (i).
* (i) \(f\) is integrable on \(\Omega\) and \(\int_\Omega f\,d\mu=L\);
* (ii) \(f\) is integrable on each \(A_n\) and \(\int_{A_n}f\,d\mu\to L\) as \(n\to\infty\).
