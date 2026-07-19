# Analysis first year exam, August 2017, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** Let \(f:[0,1]\to[0,1)\) be continuous. Decide whether it follows that
\[
\int_0^1 \frac{1}{1-f(t)}\,dt=\sum_{n=0}^{\infty}\int_0^1 f(t)^n\,dt,
\]
giving proof or counterexample as appropriate. [Note the intervals carefully.]

**2.** Let \(f:\mathbb{R}\to\mathbb{R}\) be nonconstant; for each positive integer \(n\) and each real \(t\) define \(f_n(t)=f(nt)\). Prove that there exists no \(\varepsilon>0\) such that \((f_n)_{n=1}^{\infty}\) is equicontinuous on the interval \((-\varepsilon,\varepsilon)\).

**3.** Let \(f:\mathbb{R}\to\mathbb{R}\) be continuous. Either
* (i) show that there exists a sequence of polynomials converging pointwise to \(f\) on \(\mathbb{R}\)
* (ii) or show that there need not exist a sequence of polynomials converging uniformly to \(f\) on \(\mathbb{R}\).

**4.** Let \((f_n)_{n=1}^{\infty}\) be a sequence of measurable real-valued functions. Prove that each of the following sets is measurable:
* (i) \(A=\{\omega:f_n(\omega)\to\infty\text{ as }n\to\infty\}\);
* (ii) \(B=\{\omega:f_n(\omega)\text{ is eventually irrational}\}\);
* (iii) \(C=\{\omega:f_n(\omega)>0\text{ for infinitely many }n\}\).

**5.** Let \(f:[0,\infty)\to\mathbb{R}\) be locally Lebesgue integrable and assume that \(f(t)\to1\) as \(t\to\infty\). Prove that for each positive integer \(n\) we may define
\[
a_n=\frac{1}{n}\int_0^{\infty}e^{-t/n}f(t)\,dt\in\mathbb{R}
\]
and prove that \(a_n\to1\) as \(n\to\infty\).

Suggestion: Say \(|f(t)-1|\leq\varepsilon\) whenever \(t\geq A\) and split the integral.
