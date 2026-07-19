# Analysis, first year exam, January 2024, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** Prove that the function \(f:[a,b]\to\mathbb{R}\) is Riemann integrable iff for each \(\varepsilon>0\) there exist Riemann integrable functions \(\ell,u:[a,b]\to\mathbb{R}\) such that \(\ell\leq f\leq u\) pointwise on \([a,b]\) and \(\int_a^b(u-\ell)<\varepsilon\).

**2.** For each positive integer \(n\) let \(f_n:[0,1]\to[0,1]\) be a Riemann integrable function. Which (if any) of the following conditions is sufficient to ensure that \(\int_0^1 f_n(t)\,dt\to0\) as \(n\to\infty\)?
* (i) \(f_n\to0\) uniformly on \([0,1]\);
* (ii) \(f_n\to0\) pointwise on \([0,1]\).

**3.** To each continuous function \(f:[0,1]\to\mathbb{R}\) associate the sequence \((a(f)_n)_{n=0}^{\infty}\) defined by
\[
a(f)_n=\int_0^1 f(t)t^n\,dt.
\]
Prove that the map \(f\mapsto a(f)\) is injective.

**4.** Let the bounded set \(X\subseteq\mathbb{R}\) be Lebesgue measurable. Prove that:
* (i) for each \(\varepsilon>0\) there exists an open set \(U\supseteq X\) whose Lebesgue measure \(\lambda(U)\) is less than \(\lambda(X)+\varepsilon\);
* (ii) there exists a Borel set \(B\supseteq X\) such that \(\lambda(B)=\lambda(X)\).

**5.** Let \((f_n)_{n=0}^{\infty}\) be a sequence of functions on the measurable space \((X,\mathcal{A})\) with values in \([0,\infty)\). Prove that each of the following subsets of \(X\) is measurable:
* (i) \(B=\{x:\text{ the sequence }(f_n(x))_{n=0}^{\infty}\text{ is bounded}\}\);
* (ii) \(C=\{x:\text{ the series }\sum_{n=0}^{\infty}f_n(x)\text{ is convergent}\}\).
