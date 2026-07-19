# Analysis PhD exam, January 2012

*Answer SIX questions. Write solutions in a neat and logical fashion, giving complete reasons for all steps and stating carefully any substantial theorems used.*

**1.** Let \(V\) be the vector space of all complex sequences \(z=(z_n)_{n\in\mathbb N}\) and for each \(n\in\mathbb N\) denote the \(n\)th coordinate map by
\[
\phi_n:V\to\mathbb C:z\mapsto z_n.
\]
Does \(V\) carry a norm relative to which the linear functional \(\phi_n\) is bounded for infinitely many values of \(n\)? Explain.

**2.** State the Baire Category Theorem.

Decide whether the vector space \(c_{00}\) comprising all finitely-nonzero complex sequences carries a complete norm (by considering suitable subspaces of finite dimension, or otherwise).

**3.** State the Closed Graph Theorem.

Prove the Banach Isomorphism Theorem.

**4.** Let \(1\leq p<\infty\) and define norms \(\|\cdot\|_p\) and \(\|\cdot\|_\infty\) on \(C[0,1]\ni f\) by
\[
\|f\|_p=\left(\int_0^1|f(t)|^p\,dt\right)^{1/p}
\]
\[
\|f\|_\infty=\sup\{|f(t)|:0\leq t\leq1\}
\]
as usual. Show that on \(C[0,1]\):
* (i) \(\|\cdot\|_p\) and \(\|\cdot\|_\infty\) are inequivalent;
* (ii) \(\|\cdot\|_p\) is incomplete.

**5.** Let \(\mathbb H\) be a complex Hilbert space and \(\phi:\mathbb H\to\mathbb C\) a bounded linear functional. Prove that there exists a unique \(u\in\mathbb H\) such that \(\phi(v)=\langle u\mid v\rangle\) for each \(v\in\mathbb H\).

**6.** Say what it means for one measure to be absolutely continuous relative to another.

Let \((\mu_n)_{n=1}^{\infty}\) be a sequence of finite measures on the \(\sigma\)-algebra \(\mathcal F\). Prove that there exists a finite measure \(\lambda\) on \(\mathcal F\) such that \(\mu_n\ll\lambda\) for each \(n\geq1\).

**7.** Let \((\Omega,\mathcal F,\mu)\) be a finite measure space on which \(f\) is a measurable real-valued function. Prove that the rule
\[
t\in\mathbb R\Rightarrow F(t)=\int_\Omega e^{itf(\omega)}\,d\mu(\omega)
\]
defines a continuous function \(F:\mathbb R\to\mathbb C\).

**8.** Let \((\Omega,\mathcal F,\mu)\) be a \(\sigma\)-finite measure space, let \(g:\Omega\to\mathbb C\) be measurable and let \(p\geq1\). Show that pointwise multiplication
\[
f\in L_p\Rightarrow\Phi_g(f)=gf
\]
defines a bounded linear operator \(\Phi_g\) on \(L_p\) iff \(g\in L_\infty\). Note: Recall that \(g\in L_\infty\) iff there exists \(K\geq0\) such that \(\mu\{|g|>K\}=0\).
