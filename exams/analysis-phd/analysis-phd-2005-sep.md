# Analysis, PhD exam, September 2005

*Give complete proofs and computations. Be particularly careful to indicate why the most crucial steps in your proof are true. Partial credit will be given where justified.*

**1.** Let \(\Omega\subset\mathbb R^n\) be open. Prove that \(A\subset\mathcal D(\Omega)\) is bounded if and only if
\[
\sup\{|\Lambda(\varphi)|\mid \varphi\in A\}<\infty,
\]
for every \(\Lambda\in\mathcal D'(\Omega)\).

**2.** Let \(\mu\) be Lebesgue measure on \(\mathbb R\) and \(f\) be \(\mu\)-integrable on \([0,1]\). Suppose \(\int_0^r f\,d\mu=0\), for every rational \(r\in[0,1]\). Give a complete characterization of \(f\).

**3.** Let \(\mathcal H\) be a Hilbert space and suppose \(A\) is a bounded operator on \(\mathcal H\) such that the range of \(A\) is finite dimensional. Let \(\{y_1,\ldots,y_n\}\) be an orthonormal basis for the range of \(A\). Prove that there exist \(x_1,\ldots,x_n\in\mathcal H\) such that
\[
Ax=\sum_{j=1}^n[x,x_j]y_j,
\]
for all \(x\in\mathcal H\).

**4.** Let \(A\) be a bounded operator on a Hilbert space \(\mathcal H\) such that \(A(B_1)=\{Ax\mid x\in B_1\}\) is compact, where \(B_1\) is the closed unit ball of \(\mathcal H\). Prove that, as a map from \(B_1\) with the weak vector topology to \(\mathcal H\) with the norm topology, \(A\) is continuous. (Hint: show that the weak and norm topologies on \(A(B_1)\) must coincide under the given hypothesis.)

**5.** Let \(\mu\) be a positive Radon measure on \(\mathbb R^N\) and \(f\) be \(\mu\)-integrable. Show that for each \(\epsilon>0\) there exist an upper semi-continuous function \(u_\epsilon\) and a lower semi-continuous function \(v_\epsilon\) such that \(u_\epsilon\leq f\leq v_\epsilon\) and \(\int(v_\epsilon-u_\epsilon)\,d\mu<\epsilon\).

**6.** Let \(\mu\) be a finite positive Radon measure on \(\mathbb R^N\) and \(\{f_n\}_{n\in\mathbb N}\subset L^2(\mu)\) with \(\|f_n\|_2\leq1\). Suppose \(\{f_n\}_{n\in\mathbb N}\) converges \(\mu\)-a.e. to \(f\). Show that \(\int|f_n-f|\,d\mu\to0\), as \(n\to\infty\).

**7.** Let \(E\) be a topological vector space. Prove that if \(A\) and \(B\) are compact subsets of \(E\), then so is \(A+B\).

**8.** Consider \(X\in\mathcal D(\mathbb R^2)^*\) defined by
\[
\mathcal D(\mathbb R^2)\ni\phi\mapsto X(\phi)=\int_{\mathbb R}\phi(x,-x)\,dx.
\]
Note. So \(X\) is a solution of the PDE \((\partial_1-\partial_2)X=0\) which is not a classical solution.
* (a) Show that \(X\) is a distribution of order zero.
* (b) What is the support of \(X\)? (Prove it.) Use this to prove that \(X\) is not a regular distribution with continuous coefficient function.
* (c) Show that \((\partial_1-\partial_2)X=0\).
