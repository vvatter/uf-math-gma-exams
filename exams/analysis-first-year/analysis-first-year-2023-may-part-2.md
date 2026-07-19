# Analysis, first year exam, May 2023, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** Prove that the function \(f:[a,b]\to\mathbb{R}\) is Riemann-integrable if and only if for each \(\epsilon>0\) there exist Riemann-integrable functions \(\ell\) and \(u\) on \([a,b]\) such that \(\ell\leq f\leq u\) and \(\int_a^b(u-\ell)<\epsilon\).

**2.** Let \(f:[0,1]\to\mathbb{R}\) be continuous; for each \(n\in\mathbb{N}\) and each \(t\in[0,1]\) define \(f_n(t)=f(t)t^n\). Prove that the sequence \((f_n:n\in\mathbb{N})\) converges uniformly on \([0,1]\) if and only if \(f(1)\) has a specific value, which should be found.

**3.** Let \(f:[-1,1]\to\mathbb{R}\) be continuous. Prove that if
\[
\int_{-1}^1 f(t)t^n\,dt=0
\]
whenever the natural number \(n\) is odd, then the function \(f\) is even.

**4.** Let \((f_n:n\in\mathbb{N})\) be a sequence of measurable real-valued functions on some measurable space. Prove that each of these three sets is measurable:
\[
\begin{aligned}
C&=\{\omega:\text{ the sequence }f_n(\omega)\text{ is Cauchy}\};\\
D&=\{\omega:\text{ the sequence }f_n(\omega)\text{ has all terms different}\};\\
E&=\{\omega:\text{ the sequence }f_n(\omega)\text{ is eventually constant}\}.
\end{aligned}
\]

**5.** The bounded function \(f:[0,1]\times[0,1]\to\mathbb{R}\) is separately continuous: that is, \(f(x,y)\) is continuous in \(x\) when \(y\) is fixed and continuous in \(y\) when \(x\) is fixed. Prove the continuity of the function \(F:[0,1]\to\mathbb{R}\) defined by
\[
F(x)=\int_0^1 f(x,y)\,dy.
\]
