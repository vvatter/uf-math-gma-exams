# Analysis first year exam, August 2021, Part 2

*Answer FOUR questions in detail. State carefully any results used without proof.*

**1.** Let \(f_A\) be the indicator function of the countably infinite set \(A \subseteq [0,1]\): that is, \(f_A(t)\) is \(1\) when \(t \in A\) and \(0\) when \(t \in [0,1] \setminus A\).
* (i) Exhibit (with brief justification) such an \(A\) for which \(f_A\) is Riemann integrable, or prove that no such \(A\) exists.
* (ii) Exhibit (with brief justification) such an \(A\) for which \(f_A\) is not Riemann integrable, or prove that no such \(A\) exists.

**2.** For each \(n>0\) let the function \(f_n:X\to\mathbb{R}\) be continuous at all but finitely many points. Prove that if \(f_n\to f\) uniformly on \(X\), then \(f\) is continuous at all but countably many points.

**3.** \((f_n:n>0)\) is an equicontinuous sequence of real-valued functions on a compact space. Prove that if \(f_n\to f\) pointwise then \(f_n\to f\) uniformly.

**4.** Let \((f_n:n>0)\) be a sequence of measurable functions on \(\Omega\). Prove that each of the following sets is measurable:
* (i) \(\{\omega\in\Omega:\text{ the sequence }f_n(\omega)\text{ is eventually constant}\}\);
* (ii) \(\{\omega\in\Omega:\text{ the values }f_n(\omega)\text{ are all different}\}\).

**5.** Let \((f_n:n>0)\) be a sequence of non-negative integrable functions that converges pointwise to \(f\). Prove that if
\[
\int_\Omega f_n\,d\mu \to \int_\Omega f\,d\mu
\]
then
\[
\int_\Omega |f-f_n|\,d\mu \to 0.
\]
[It might help to consider the positive part \((f-f_n)^+=\max\{0,f-f_n\}\).]
