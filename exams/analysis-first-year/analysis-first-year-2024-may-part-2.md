# Analysis, first year exam, May 2024, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** Let \(f:[a,b]\to\mathbb{R}\) be Riemann integrable, let \(g\) be a real-valued function on \([a,b]\), and let \(D=\{t\in[a,b]:f(t)\ne g(t)\}\).
* (i) Show by example that if \(D\) is countably infinite then \(g\) can fail to be Riemann integrable.
* (ii) Prove that if \(D\) is finite then \(g\) must be Riemann integrable.

**2.** Prove Dini’s theorem that, if the sequence \((f_n)_{n=0}^{\infty}\) of continuous real-valued functions on a compact space decreases pointwise to zero, then the convergence is uniform. Show by example that uniform convergence can fail if decreases pointwise is replaced by converges pointwise.

**3.** State the Weierstrass approximation theorem. Determine exactly which continuous functions \(f:[-1,1]\to\mathbb{R}\) satisfy the requirement that for each strictly positive integer \(n\),
\[
\int_{-1}^{1}f(t)t^n\,dt=0.
\]

**4.** Let \((\Omega,\mathcal{A},\mu)\) be a measure space and let \((A_n)_{n=1}^{\infty}\) be a sequence in \(\mathcal{A}\). For each positive integer \(N\), let \(B_N\) be the set containing exactly those \(\omega\in\Omega\) that lie in \(A_n\) for at least \(N\) values of \(n\). By considering the series \(\sum_{n=1}^{\infty}\mathbf{1}_{A_n}\) of indicator functions, prove that
\[
N\mu(B_N)\leq\sum_{n=1}^{\infty}\mu(A_n).
\]

**5.** Let the non-negative function \(f:\mathbb{R}\to\mathbb{R}\) be integrable with respect to Lebesgue measure \(\lambda\) and for each real \(t\) define
\[
F(t)=\int_0^t f\,d\lambda.
\]
Prove that the function \(F\) is continuous. Must \(F\) be uniformly continuous? Explain.
