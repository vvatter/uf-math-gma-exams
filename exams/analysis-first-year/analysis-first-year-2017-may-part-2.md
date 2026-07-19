# Analysis first year exam, May 2017, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** Let \((f_n)_{n=0}^{\infty}\) be a sequence of differentiable functions. Decide whether each implication is valid, giving proof or counterexample as appropriate:
* (i) if \(f_n \to f\) uniformly on \((−\infty,\infty)\) then \(f_n^2 \to f^2\) uniformly on \((−\infty,\infty)\);
* (ii) if \(f_n \to f\) uniformly on \([−1,1]\) then \(\int_{−1}^1 f_n \to \int_{−1}^1 f\);
* (iii) if \(f_n \to f\) uniformly on \((−1,1)\) then \(f\) is differentiable and \(f_n' \to f'\) uniformly on \((−1,1)\).

**2.** Let \(f\) be a continuous real-valued function on \([0,1]\) and let \(\alpha \in (0,\infty)\). Assume that
\[
\int_0^1 t^{n\alpha}f(t)\,dt=0
\]
for all but finitely many values of \(n\in\mathbb N\). What conclusions can be drawn about \(f\)?

**3.** Let \(\mathcal F\) be an equicontinuous family of real-valued functions on the compact metric space \(X\). Denote by \(A\subseteq X\) the set whose elements are precisely those \(a\in X\) at which \(\mathcal F\) is bounded in the sense that \(\{f(a):f\in\mathcal F\}\subseteq\mathbb R\) is bounded. Prove that \(A\) is both open and closed.

**4.** Let \((f_n)_{n=0}^{\infty}\) be a sequence of measurable real-valued functions. Decide whether each of the following sets is measurable:
* (i) \(\{\omega:(f_n(\omega))_{n=0}^{\infty}\text{ is unbounded}\}\);
* (ii) \(\{\omega:(f_n(\omega))_{n=0}^{\infty}\text{ is periodic}\}\);
* (iii) \(\{\omega:(f_n(\omega))_{n=0}^{\infty}\text{ has distinct terms}\}\).

**5.** Let \((\Omega,\mathcal A,\mu)\) be a measure space that is finite in the sense that \(\mu(\Omega)<\infty\). Let \((f_n)_{n=0}^{\infty}\) be a sequence of non-negative measurable functions converging pointwise to \(f\) on \(\Omega\). True or false (proof or counterexample):
\[
\int_\Omega \frac{1}{1+f_n}\,d\mu \to \int_\Omega \frac{1}{1+f}\,d\mu \quad\text{as }n\to\infty.
\]
