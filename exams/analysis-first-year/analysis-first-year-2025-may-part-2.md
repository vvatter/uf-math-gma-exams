# Analysis, first year exam, May 2025, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** The sequence \((f_n)_{n=0}^{\infty}\) of real-valued functions on \([0,1]\) is uniformly bounded and converges to \(0\) pointwise. If each \(f_n\) is (i) continuous, (ii) Riemann integrable, (iii) Lebesgue integrable, does it follow that \(\int_0^1 f_n(t)\,dt \to 0\)? In each of the three cases, a proof or counterexample should be given.

**2.** Let \((f_n)_{n=0}^{\infty}\) be a sequence of continuous non-negative functions on \([0,1]\) converging pointwise to \(0\). Prove that if the extra condition
\[
\forall t\in[0,1]\quad f_0(t)\geq f_1(t)\geq\cdots\geq f_n(t)\geq\cdots
\]
is satisfied then \(f_n\to 0\) uniformly on \([0,1]\). Show that this conclusion can fail if the extra condition is removed.

**3.** Let the continuous real-valued function \(f\) on \([0,1]\) satisfy
\[
\forall n\in\mathbb N\quad \int_0^1 f(t)(1-t)^n\,dt=0.
\]
Deduce as much as possible about \(f\).

**4.** Let \((\Omega,\mathcal A,\mu)\) be a measure space. Let \((A_n)\) be a sequence in \(\mathcal A\) and define
\[
\liminf A_n=\bigcup_N\bigcap_{n\geq N}A_n.
\]
Prove that
\[
\mu(\liminf A_n)\leq\liminf\mu(A_n).
\]

**5.** Let \(f(x)=\sin x/x\) for \(x>0\). Show that if \(n\) is a positive integer then
\[
\int_{2n\pi}^{(2n+1)\pi}\frac{\sin x}{x}\,dx\geq\frac{2}{(2n+1)\pi}.
\]
Hence explain why \(f\) is not Lebesgue integrable on \((a,\infty)\) for any \(a>0\).
