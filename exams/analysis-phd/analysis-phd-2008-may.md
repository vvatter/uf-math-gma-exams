# Analysis, PhD exam, May 2008

*Write solutions in a neat and logical fashion, giving complete reasons for all steps.*

**1.** Define the Hardy–Littlewood maximal function. State and prove the Hardy–Littlewood maximal theorem. (Begin by proving a suitable covering lemma.)

**2.** Suppose \(f_n \to f\) in measure. Prove the following:
* a) If \(f_n \geq 0\) for all \(n\), then \(\int f \leq \liminf \int f_n\).
* b) If \(|f_n| \leq g\) for all \(n\) and \(g \in L^1\), then \(\int f = \lim \int f_n\).

**3.** Let \((X,\mathcal M,\mu)\) be a \(\sigma\)-finite measure space, \(\mathcal N\) a sub-\(\sigma\)-algebra of \(\mathcal M\), and \(\nu=\mu|_{\mathcal N}\). Prove that if \(f\in L^1(\mu)\), then there exists \(g\in L^1(\nu)\) (unique modulo \(\nu\)-null sets) such that
\[
\int_E f\,d\mu=\int_E g\,d\nu
\]
for all \(E\in\mathcal N\).

**4.** Suppose \(1<p<\infty\), \(f\in L^p(0,\infty)\), and \(p^{-1}+q^{-1}=1\). Define
\[
F(x)=\int_0^x f(t)\,dt.
\]
Show that \(\dfrac{F(x)}{x^{1/q}}\to0\) as \(x\to0\) and \(x\to\infty\).

**5.** Let \(\mathcal X,\mathcal Y\) be Banach spaces. Suppose that \((T_n)\) is a sequence of bounded linear operators from \(\mathcal X\) to \(\mathcal Y\) such that \(\lim T_nx\) exists for every \(x\in\mathcal X\). Prove that
\[
Tx:=\lim T_nx
\]
defines a bounded linear operator from \(\mathcal X\) to \(\mathcal Y\).

**6.** Let \(\mu\) be a \(\sigma\)-finite positive measure and \(1\leq p\leq\infty\). Let \(g\in L^\infty\). Prove that the operator
\[
Tf=gf
\]
is bounded on \(L^p\), and \(\lVert T\rVert=\lVert g\rVert_\infty\).

**7.** Let \(\mathcal X\) be a normed vector space over \(\mathbb C\). Prove that if \(\mathcal M\) is a closed subspace of \(\mathcal X\) and \(x\in\mathcal X\setminus\mathcal M\), then the subspace \(\mathcal M+\mathbb Cx\) is closed.

**8.** Let \(\mathcal E\) be a subset of a Hilbert space \(\mathcal H\). Prove that \((\mathcal E^\perp)^\perp\) is equal to the smallest closed subspace of \(\mathcal H\) containing \(\mathcal E\).
