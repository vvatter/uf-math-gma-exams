# Probability PhD exam, May 1998

**1.** Let \(X\) and \(Y\) be independent and uniform on \([0,1]\). Find:
* a) the distribution of \(X+Y\).
* b) the conditional density of \(X\) given \(X+Y=z\).

**2.** Let \(X_0,X_1,\ldots,X_n,\ldots\) be i.i.d. with mean \(m\). Let \(N\) be Poisson with mean \(\lambda\), independent of the \(X\)’s. Define
\[
Y=X_0+\cdots+X_N.
\]
Prove that \(Y\) is integrable. Find \(E(Y)\).

**3.** State precisely (all for i.i.d.):
* a) the strong law of large numbers and prove it.
* b) the central limit theorem.
* c) the law of the iterated logarithm.

**4.** Define a martingale relative to a filtration \(\{\mathcal F_n\}\), \(n=0,1,2,\ldots\). Define a stopping time relative to this filtration. State the optional sampling theorem. State and prove the martingale convergence theorem.

**5.** What is an infinitely divisible distribution on \(\mathbb R^1\). Prove that a non-trivial infinitely divisible distribution cannot have compact support.

**6.** Define a standard Brownian Motion \(W\) starting at 0. Define new processes \(W_1,W_2,W_3\) by:
\[
W_1(t)=cW\!\left(\frac{t}{c^2}\right),\qquad t\geq0,\quad c\text{ real},\ c\neq0,
\]
\[
W_2(t)=tW\!\left(\frac1t\right),\qquad t>0,\quad W_2(0)=0,
\]
\[
W_3(t)=
\begin{cases}
W(1)-W(1-t),&0\leq t\leq1,\\
W(t),&\text{otherwise.}
\end{cases}
\]
Show that \(W_1,W_2,W_3\) are the standard Brownian motions.

**7.** Let \(\varphi(t)=\int e^{itx}\,\mu(dx)\) be a characteristic function where \(\mu\) is a probability measure on \(\mathbb R^1\).
* a) Suppose \(|\varphi(t)|=1\) for some \(t\neq0\). Then prove that unless \(|\varphi(t)|\equiv1\), there is a smallest \(t_0>0\) and a \(d\) such that \(\mu\) is concentrated on the set \(\left\{d+\frac{2\pi j}{t_0}\right\}\), \(j=0,\pm1,\pm2,\ldots\).
* b) Using a) prove that \(|\cos t|\) is not a characteristic function. Hint: \(\cos t\) and \(\cos^2t\) are characteristic functions.
