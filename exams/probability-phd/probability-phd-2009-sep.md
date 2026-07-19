# Probability PhD exam, September 2009

**1.** For each fixed \(n\), \(X_n^1, X_n^2, \ldots, X_n^n\) are independent random variables and have the same Binomial distribution, that is, \(\mathbb P(X_n^i=1)=p_n\) and \(\mathbb P(X_n^i=0)=1-p_n\) for \(i=1,2,\ldots,n\). Let \(S_n=X_n^1+X_n^2+\cdots+X_n^n\). Given the condition that \(np_n\) converges to a positive constant \(\beta\) as \(n\) goes to \(\infty\), find the limit distribution of \(S_n\) and prove it.

**2.** Let \(X\) and \(Y\) be two independent random variables with \(\mathbb E[Y]=0\). Show that for \(p\geq 1\), we have
\[
\mathbb E|X+Y|^p\geq \mathbb E|X|^p.
\]

**3.** Let \(X\) be a positive random variable with a probability density function \(f(x)\) that is continuous and \(U_n=nX-[nX]\), where \([a]\) means the largest integer which is less than \(a\). Find the limit distribution of \(U_n\) as \(n\) goes to \(\infty\).

**4.** Let \(X_1,X_2,\ldots,X_n\) be i.i.d. random variables with probability density function \(f(x)\), and \(M=\max(X_1,X_2,\ldots,X_n)\). Find the conditional expectation \(\mathbb E[X_1\mid M]\).

**5.** For a continuous function \(f(x)\) on \([0,1]\), define
\[
P_n(x)=\sum_{k=0}^n f\left(\frac{k}{n}\right)\binom{n}{k}x^k(1-x)^{n-k}.
\]
Show that \(P_n(x)\) converges to \(f(x)\) on \([0,1]\) as \(n\) goes to infinity.

**6.** Let \(S_n\) be a one-dimensional simple random walk, that is, \(S_n=X_1+\cdots+X_n\), where \(X_1,\ldots,X_n\) are i.i.d. random variables with \(\mathbb P(X_1=+1)=\mathbb P(X_1=-1)=1/2\), and \(S_0=0\). and let
\[
R_n=1+\max_{0\leq k\leq n}S_k-\min_{0\leq k\leq n}S_k
\]
be the number of points visited by time \(n\). Prove that \(R_n/\sqrt n\) converges weakly to some limit (in distribution).

**7.** Let \(B_t\) be standard Brownian motion with \(B_0=0\) and \(\tau=\inf\{t:B_t=a+bt\}\), where \(a>0\) and \(b\) are two constants. Prove that
* a).
  \[
  \mathbb E_0[e^{-\lambda\tau}]=\exp\{-ab-a\sqrt{b^2+2\lambda}\}
  \]
* b).
  \[
  \mathbb P_0(\tau<\infty)=\exp\{-2ab\}.
  \]

**8.** Let \(\{X_n,n=0,1,2,3,\ldots\}\) be a Markov chain on a countable irreducible state space \(S\). Let \(\phi\) be a nonnegative function with
\[
\mathbb E[\phi(X_1)\mid X_0=x]\leq \phi(x)
\]
for all but a finite number of \(x\). Prove that if \(\{x\mid \phi(x)\leq M\}\) is finite for any \(M<\infty\), then the Markov chain \(\{X_n,n=0,1,2,3,\ldots\}\) is recurrent.
