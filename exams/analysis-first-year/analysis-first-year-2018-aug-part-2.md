# Analysis first year exam, August 2018, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** Let the sequence \((s_n)_{n=1}^{\infty}\) in \([0,1]\) be uniformly distributed in the sense that if \(0 \le a \le b \le 1\) then
\[
\lim_{n\to\infty}\frac{\#\{k\le n:s_k\in[a,b]\}}{n}=b-a.
\]
Let \(f:[0,1]\to\mathbb{R}\) and prove that
\[
\lim_{n\to\infty}\frac{f(s_1)+\cdots+f(s_n)}{n}=\int_0^1 f(t)\,dt
\]
in each of the following cases:
* (i) \(f\) is a step function (a finite linear combination of indicators of intervals);
* (ii) \(f\) is Riemann-integrable.

**2.** Fix \(a\in\mathbb{R}\) and for each integer \(n>0\) write \(f_n(t)=n^a t(1-t^2)^n\) whenever \(0\le t\le 1\).
* (i) Show that \((f_n)_{n=1}^{\infty}\) converges pointwise on \([0,1]\); say to \(f\).
* (ii) For which values of \(a\) does \((f_n)_{n=1}^{\infty}\) converge uniformly on \([0,1]\)? Justify.
* (iii) For which values of \(a\) is it true that \(\int_0^1 f_n\to\int_0^1 f\)? Justify.

**3.** Let \(f:[1,\infty)\to\mathbb{R}\) be continuous and satisfy \(\lim_{t\to\infty}f(t)=A\in\mathbb{R}\). Prove that there is a sequence \((p_n)_{n=0}^{\infty}\) of polynomials such that \(p_n(1/t)\) converges to \(f(t)\) uniformly for \(t\ge 1\).

**4.** Let \((f_n)_{n=1}^{\infty}\) be a sequence of real-valued measurable functions. Prove that each of the following sets is measurable:
* (i) \(B=\{\omega:(f_n(\omega))_{n=1}^{\infty}\text{ has no biggest term}\}\);
* (ii) \(C=\{\omega:\cos(f_n(\omega))>0\text{ for each }n>0\}\);
* (iii) \(D=\{\omega:(f_n(\omega))_{n=1}^{\infty}\text{ does not converge to a rational number}\}\).

**5.** State the Monotone Convergence Theorem. Use it to prove the following: let \((f_n)_{n=1}^{\infty}\) be a sequence of non-negative integrable functions with pointwise limit \(f\); if \(\int f_n\,d\mu\le M<\infty\) for each \(n\) then \(f\) is integrable and \(\int f\,d\mu\le M\).
