# Analysis PhD exam, May 2005

*Give complete proofs and computations. Be particularly careful to indicate why the most crucial steps in your proof are true.*

**1.** Let \(\mu\) be a positive Radon measure on a locally compact Hausdorff space \(T\). Let \(f_n:T\to\overline{\mathbb R}\) be \(\mu\)-measurable for all \(n\in\mathbb N\). Prove that \(\sup\{f_n\mid n\in\mathbb N\}\) is \(\mu\)-measurable.

**2.** Let \(E\) be a complex Banach space. Suppose \(\{x_n\}_{n\in\mathbb N}\subset E\) converges in the weakened topology \(\sigma(E,E')\) to \(x\in E\), i.e. \(\lvert\langle x_n-x,y\rangle\rvert\to0\) for all \(y\in E'\) as \(n\to\infty\). Prove that \(x\) is contained in the closure of the linear span of the set \(\{x_n\}_{n\in\mathbb N}\).

**3.** Let \(E\) be a topological vector space. Prove the following:
* (a) If \(A\subset E\) is arbitrary and \(U\subset E\) is open, then \(A+U\) is open.
* (b) If \(A\subset E\) is compact and \(B\subset E\) is closed, then \(A+B\) is closed.
* (c) The sum of closed subsets may fail to be closed.

**4.** Let \(\delta\in\mathcal D'(\mathbb R)\) denote the distribution given by \(\delta(\phi)=\phi(0)\), for all \(\phi\in\mathcal D(\mathbb R)\). Prove your answers are correct.
* (a) For which \(f\in C^\infty(\mathbb R)\) is \(f\cdot\delta'=0\)?
* (b) What is the support of \(\delta\)?
* (c) If \(X\in\mathcal D'(\mathbb R)\), \(f\in C^\infty(\mathbb R)\), and \(f\) restricted to the support of \(X\) is \(0\), is it true that \(f\cdot X=0\)?

**5.** Let \(K:[0,1]\times[0,1]\to\mathbb R\) be continuous and \(f:[0,1]\times\mathbb R\to\mathbb R\) be continuous and bounded. Show that the Hammerstein equation
\[
u(s)=\int_0^1 K(s,t)f(t,u(t))\,dt,\qquad s\in[0,1],
\]
has a solution in \(E=\{x:[0,1]\to\mathbb R\mid x\text{ continuous}\}\).

**6.** Let \(1\in\mathcal D'(\mathbb R)\) be given by \(1(\phi)=\int_{\mathbb R}\phi\,dx\), for all \(\phi\in\mathcal D(\mathbb R)\). Compute \((1*\delta')(\phi)\) for all \(\phi\in\mathcal D(\mathbb R)\).

**7.** Let \(\mu\) be a \(\sigma\)-finite positive Radon measure on a locally compact Hausdorff space \(T\). Let \(\{f_n\}_{n\in\mathbb N}\subset L^p(T,\mu)\) for some \(p\in[1,\infty)\). Suppose that \(\lim_{n\to\infty}f_n(t)=f(t)\) \(\mu\)-a.e., that \(f\in L^p(T,\mu)\), and that \(\lim_{n\to\infty}\int\lvert f_n\rvert^p\,d\mu=\int\lvert f\rvert^p\,d\mu\). Prove that \(\lim_{n\to\infty}\int\lvert f_n-f\rvert^p\,d\mu=0\). Hint: Bring the Lebesgue Dominated Convergence Theorem and the \(\sigma\)-finiteness of the measure into play.

**8.** Let \(\mathcal H\) be a Hilbert space with inner product \((\cdot,\cdot)\), and let \(\{y_\alpha\}_{\alpha\in A}\subset\mathcal H\) be an orthonormal family. Let \(x\in\mathcal H\).
* (a) Prove that \(\sum_\alpha (x,y_\alpha)y_\alpha\) converges strongly to an element \(y\in\mathcal H\).
* (b) Prove that the vector \(x-y\) is orthogonal to the closure of the linear span of the set \(\{y_\alpha\}_{\alpha\in A}\).
