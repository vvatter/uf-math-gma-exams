# Analysis first year exam, January 2014, Part 1

*Do only 4 problems of the 6. Work must be presented in a neat and logical fashion to receive credit. Do not leave any gaps. State clearly any theorems used in proofs.*

**1.** Let \(F\) be a closed subset of the reals \(\mathbb{R}\) with the usual topology. Show \(F\) is a countable union of compact sets.

**2.** Let \(E\) be a nonempty subset of a metric space. State the definition of the distance \(\rho_E(x)\) of a point \(x\) to \(E\). Characterize \(\overline{E}\) in terms of \(\rho_E\), where \(\overline{E}\) is the closure of \(E\).

**3.** This problem has two parts.
* (a) Let \(f\) be a continuous function from a compact metric space \(X\) into a metric space \(Y\). Prove \(f(X)\) is compact.
* (b) Assume the setting in (a) with the further assumption that \(Y\) is the reals with the usual topology. Show that \(f\) assumes maximum and minimum values on \(X\).

**4.** Let \(f\) be a continuous map of a metric space \(X\) into a metric space \(Y\).
* (a) Show that if \(f\) is NOT uniformly continuous on \(X\), then for some \(\varepsilon>0\) there are sequences \(\{p_n\}\), \(\{q_n\}\) in \(X\) such that \(d_Y(f(p_n),f(q_n))>\varepsilon\) for each \(n\) but \(d_X(p_n,q_n)\to 0\).
* (b) Assume that \(X\) is compact. Show, using (a), that \(f\) is uniformly continuous on \(X\).

**5.** Let \(\{x_n\}\) be a sequence of points in \((a,b)\) and let \(\{c_n\}\) be a sequence of positive numbers such that \(\sum c_n\) converges. Define
\[
f(x)=\sum_{n:x_n<x}c_n,\qquad a<x<b,
\]
where the summation is understood as follows: sum over those indices \(n\) for which \(x_n<x\). If there are no points \(x_n<x\), define the sum to be zero.
* (a) Show \(f(x-)=f(x)\) for each \(x\) in \((a,b)\).
* (b) Show \(f(x_n+)-f(x_n-)=c_n\), for each \(n\).

**6.** Suppose \(f\) is continuous on \([0,\infty)\), differentiable on \((0,\infty)\), \(f(0)=0\) and \(f'\) is monotonically increasing. Define \(g\) on \((0,\infty)\) by \(g(x)=f(x)/x\), \(x>0\). Prove \(g\) is monotonically increasing.
