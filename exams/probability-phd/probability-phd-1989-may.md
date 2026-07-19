# Probability PhD exam, May 1989

**1.** Let \(X_n\) be independent identically distributed random variables and \(S_n=\sum_{i=1}^n X_i\). Suppose
\[
\mathrm E\left[\sup_n\left|\frac{S_n}{n}\right|\right]<\infty.
\]
Show that
\[
\mathrm E\bigl[|X_1|\log^+|X_1|\bigr]<\infty,
\]
where
\[
\log^+x=\begin{cases}
\log x,&x\geq 1,\\
0,&\text{otherwise}.
\end{cases}
\]
Hint: \(C_n=\prod_{j=1}^n \mathrm P[|X_j|\leq j]\to c>0\). If \(T=\inf\{n:|X_n|>n\}\), then
\[
\sum_{n=1}^{\infty}\frac1n\int_{\{T=n\}}|X_n|\,dp
=\sum_{n=1}^{\infty}\frac{C_{n-1}}n\int_{\{|X_1|>n\}}|X_1|\,dp
\]
and
\[
\sum_{n=1}^{\infty}\frac1n\int_{\{T=n\}}|S_{n-1}|\,dp<\infty.
\]

**2.** Let \(X_n\) be independent Poisson variables. Suppose \(\sum_{n=1}^{\infty}X_n<\infty\) a.s. Show that \(\sum_{n=1}^{\infty}\mathrm E[X_n]<\infty\).

Hint. Borel–Cantelli.

**3.** This problem has two parts.
* a) Define the notion of conditional expectation. In particular explain the notion \(\mathrm E[X\mid Y]\) where \(X\) and \(Y\) are random variables.
* b) Suppose \(X,Y\) are random variables such that \(\mathrm E(X^2),\mathrm E(Y^2)<\infty\) and
  \[
  \mathrm E[X\mid Y]=Y,
  \qquad
  \mathrm E[Y\mid X]=X.
  \]
  Show that \(X=Y\) a.s.

**4.** This problem has three parts.
* a) A sequence of characteristic functions on \(\mathbb R^1\) converging pointwise to a characteristic function does so uniformly on compact sets. Explain why - no need to give complete proofs.
* b) Let \(b_n\in\mathbb R\) and \(f\) a characteristic function not identically equal to \(1\). Suppose \(f(b_nt)\) converges to a characteristic function. Show that \(\lim b_n=b\in\mathbb R\).
* c) Let \(\phi(t)=\frac18[1+7e^{it}]\). Show that \(\phi\) is a characteristic function but that \(|\phi|\) is not.

  Hint. \(|\phi|^2\) is the characteristic function of a measure concentrated on \(\{-1,0,1\}\). If \(|\phi|\) is the characteristic function of a measure \(m\), then \(|\phi|^2\) is the characteristic function of \(m*m\).

**5.** Let \(X_t\) be a standard Brownian motion.
* (i) Show that \((X_t)\), \((X_t^2-t)\), and \(e^{uX_t-\frac12u^2t}\) are all martingales.
* (ii) Let \(T_a(w)=\inf\{t:X_t(w)=a\}\) for \(a>0\), the inf being defined to be \(+\infty\) if the set is empty. Using (i), compute \(\mathrm E[e^{-\lambda T_a}]\) for \(\lambda>0\), and show that \(T_a<\infty\) a.s. and \(\mathrm E[T_a]=\infty\).

**6.** State and sketch the proof of the martingale convergence theorem.

**7.** Using the martingale convergence theorem prove the following:

Let \(F_n\) be an increasing sequence of \(\sigma\)-fields, \(X_n\) a sequence of random variables dominated by an integrable random variable \(Y\): \(|X_n|\leq Y\). Suppose \(X_n\to X\) a.s. Then
\[
\mathrm E[X_n\mid F_n]\to \mathrm E[X\mid F_\infty]\quad\text{a.s.}
\]
Hint. Put the
\[
U_n=\sup_{m\geq n}|X_m-X|.
\]
Then for \(m\geq n\),
\[
\mathrm E[|X_m-X|\mid F_m]\leq \mathrm E[U_n\mid F_m].
\]
\[
\mathrm E\left\{\limsup_m\mathrm E[|X_m-X|\mid F_m]\right\}
\leq \mathrm E\{\mathrm E[U_n\mid F_\infty]\}=\mathrm E[U_n].
\]
