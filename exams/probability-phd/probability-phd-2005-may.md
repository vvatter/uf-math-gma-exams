# Probability PhD exam, May 2005

**1.** Let \(X_1, X_2\) be two independent random variables with the same uniform distribution on \((\theta-1/2,\theta+1/2)\), and let \(Y_1=\min(X_1,X_2)\), \(Y_2=\max(X_1,X_2)\),
* (a). Find \(\mathbb{P}(Y_1\leq\theta\leq Y_2)\),
* (b). Find \(\mathbb{P}(Y_1\leq\theta\leq Y_2\mid Y_2-Y_1\geq 1/2)\).

**2.** Let \(\phi(t)\) be a characteristic function, prove that
* (a). \(1-\operatorname{Re}(\phi(2t))\leq 4(1-\operatorname{Re}(\phi(t)))\),
* (b). \(1-|\phi(2t)|^2\leq 4(1-|\phi(t)|^2)\).

**3.** Let \(\{X_n,n\geq 1\}\) be a sequence of i.i.d. nonnegative random variables. let \(S_0=0\), and \(S_n=X_1+\cdots+X_n\). For \(t>0\), we define
\[
\{\omega\mid N_t(\omega)=n\}=\{\omega\mid S_n(\omega)\leq t<S_{n+1}(\omega)\}
\]
show that
\[
\mathbb{E}(N_t(\omega))=\sum_{n=1}^{\infty}\mathbb{P}(S_n(\omega)\leq t).
\]

**4.** Let \(X_1,X_2,\ldots\) be a sequence of strictly positive random variables such that
\[
\mathbb{E}(X_{n+1}\mid\mathcal{F}_n)=f_n(X_n).
\]
For \(n\geq 2\), let
\[
M_n=\frac{X_1X_2\cdots X_n}{f_1(X_1)f_2(X_2)\cdots f_{n-1}(X_{n-1})}.
\]
* (a). Show that for \(n\geq 2\), \(M_n\) is a \(\mathcal{F}_n\)-martingale.
* (b). Does this martingale converges almost surely and in \(L^1\)? Explain it.

**5.** Let \(\{M_n,n\geq 0\}\) be a sequence of integrable random variables adapted to a filtration \(\mathcal{F}_n\). Assume that for each bounded stopping time \(T\), \(\mathbb{E}(M_T)=\mathbb{E}(M_0)\), show that \(\{M_n,n\geq 0\}\) is a martingale.

**6.** Let \(X\) and \(Y\) be random variables such that \(\mathbb{E}(X^2)<\infty\) and \(\mathbb{E}(Y^2)<\infty\), \(\mathbb{E}(X\mid Y)=Y\) and \(\mathbb{E}(Y\mid X)=X\). Show that \(X=Y\) a.s.

**7.** Let \(X,Y\) be two independent random variables with \(\mathbb{E}[Y]=0\). Show that for \(p\geq 1\)
\[
\mathbb{E}[|X|^p]\leq\mathbb{E}[|X+Y|^p].
\]

**8.** Let \((X,Y)\) be a random point on a unit circle with uniform distribution, that is
\[
\mathbb{P}((X,Y)\in A)=\frac{\operatorname{length}(A)}{2\pi}
\]
for any Borel subset \(A\) of \(C_2=\{(x,y)\mid x^2+y^2=1\}\). Find the marginal distribution of \(X\).

**9.** Let \(\mathcal{F}_n\) be a filtration, \(|X_n|\leq Y\), \(Y\) integrable. Suppose that \(X_n\longrightarrow X\) a.e. Using the martingale convergence theorem to prove that
\[
\mathbb{E}[X_n\mid\mathcal{F}_n]\longrightarrow\mathbb{E}[X\mid\mathcal{F}_\infty]\qquad\text{a.e.}
\]

**10.** Let \(Y\in L^p\), \(|X_n|\leq Y\) and \(X_n\longrightarrow X\) in distribution. Show that \(X_n\) converges to \(X\) in \(L^p\).
