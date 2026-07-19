# Analysis, first year exam, May 2020, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** Let \(a<b\) and let \(f:[a,b]\to\mathbb{R}\) be Riemann integrable. Prove that if \(\int_a^b f=0\), then for each positive integer \(n\) there exist \(c<d\) in \([a,b]\) such that \(\sup\{f(t):c\leq t\leq d\}<1/n\). Hence, or otherwise, prove that if \(f>0\) throughout \([a,b]\), then \(\int_a^b f>0\).

**2.** Let \((x_n:n\geq 0)\) converge in the metric space \(X\) and let \((f_n:n\geq 0)\) be a sequence of continuous real-valued functions on \(X\).
* (a) Prove that if the sequence of functions is uniformly convergent, then \((f_n(x_n):n\geq 0)\) is convergent.
* (b) Show by example that if uniformly is replaced by pointwise, then \((f_n(x_n):n\geq 0)\) may not converge.

**3.** Let \(f:[0,1]\to\mathbb{R}\) be continuous and assume that
\[
\int_0^1 f(t)t^n\,dt=1/(n+1)
\]
for each integer \(n>1\). Deduce as much as is possible about \(f\).

**4.** Let \((f_n:n\geq 0)\) be a sequence of measurable real-valued functions on some measurable space. Prove that each of the following sets is measurable:
\[
A=\{\omega:f_n(\omega)\in[0,1]\text{ for finitely many }n\}
\]
\[
B=\{\omega:f_n(\omega)\in[0,1]\text{ for infinitely many }n\}
\]
\[
C=\left\{\omega:\text{the series }\sum_{n=0}^{\infty}f_n(\omega)\text{ is absolutely convergent}\right\}.
\]

**5.** For each positive integer \(n\), let \(f_n:[0,1]\to[0,1]\) be continuous; assume that \(f_n\to 0\) pointwise as \(n\to\infty\). Does it follow that
\[
\int_0^1 f_n(t)\,dt\to 0\quad\text{as }n\to\infty?
\]
Does your answer change if continuous is replaced by Riemann integrable?
