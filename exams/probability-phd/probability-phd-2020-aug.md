# Probability, PhD exam, August 2020

*Carefully justify your answers.*

**1.** This problem has three parts.
* 1. State the weak and strong law of large numbers for i.i.d. random variables.
* 2. Prove the weak law of large numbers (for i.i.d. random variables).
* 3. Prove the strong law of large numbers under the additional assumption of finite fourth moment \(\bigl(\mathbb{E}[X_1^4]<+\infty\bigr)\).

**2.** Let \(X,Y\) be independent and uniformly distributed on \([0,1]\).
* 1. Find the density of the random variable \(X+Y\).
* 2. Find the density of the random variable \(\mathbb{E}[X\mid X+Y]\).

**3.** Let \(\{X_n\}\) be a sequence of random variables uniformly bounded, that is, there exists \(M>0\) such that for all \(n\in\mathbb{N}\), \(|X_n|\le M\). Prove that \(\{X_n\}\) converges to \(0\) in \(L^1\) if and only if \(\{X_n\}\) converges to \(0\) in probability.

**4.** Let \(\{X_n\}\) be a sequence of random variables such that for all \(n\ge 1\), \(X_n\) has a Poisson distribution of parameter \(n\). Does the random variable
\[
\frac{X_n-n}{\sqrt n}
\]
converges in distribution as \(n\to+\infty\)? If so, what is the limit? What about convergence in probability? Carefully justify all your answers.

**5.** Let \(\{X_n\}\) be a sequence of i.i.d. random variables in \(L^1\) \(\bigl(\mathbb{E}[|X_1|]<+\infty\bigr)\). Take \(\mathcal{F}_n=\sigma\{X_1,\ldots,X_n\}\), \(n\ge 1\), and denote \(S_n=\sum_{k=1}^n X_k\), \(S_0=0\).
* 1. Let \(\tau\) be an \(\{\mathcal{F}_n\}\)-stopping time in \(L^1\). Prove that \(S_\tau\) is in \(L^1\), and
  \[
  \mathbb{E}[S_\tau]=\mathbb{E}[X_1]\mathbb{E}[\tau].
  \]
* 2. Let \(\{X_n\}\) be a sequence of i.i.d. random variables such that \(\mathbb{P}(X_1=1)=\mathbb{P}(X_1=-1)=\frac12\). Denote \(S_n=\sum_{k=1}^n X_k\), \(S_0=0\), and \(T=\inf\{n\ge 0:S_n=1\}\). Prove that \(\mathbb{E}[T]=+\infty\). (One may use question 1.)

**6.** Let \(X_1,\ldots,X_n\) be a sequence of i.i.d. random variables in \(L^1\). Compute \(\mathbb{E}[X_1\mid X_1+\cdots+X_n]\).

Hint: for all \(i,j\in\{1,\ldots,n\}\), \(\mathbb{E}[X_i\mid X_1+\cdots+X_n]=\mathbb{E}[X_j\mid X_1+\cdots+X_n]\).

**7.** This problem has two parts.
* 1. Give the definition of a standard Brownian motion.
* 2. Let \(\{B_t\}\) and \(\{\widetilde B_t\}\) be two independent standard Brownian motion. Let \(\rho\in(0,1)\). Define, for \(t\ge 0\),
  \[
  X_t=\rho B_t+\sqrt{1-\rho^2}\,\widetilde B_t.
  \]
  Is \(\{X_t\}\) a standard Brownian motion? Carefully justify.

**8.** Let \(\{B_t\}\) be a standard Brownian motion.
* 1. Fix \(u>0\). Prove that \(M_t=e^{uB_t-\frac12u^2t}\) is a martingale (with respect to the same filtration as \(\{B_t\}\)).
* 2. Fix \(a>0\). Define \(T_a=\inf\{t\ge 0:B_t=a\}\). Prove that \(T_a<+\infty\) a.s. and \(\mathbb{E}[T_a]=+\infty\).

  Hint: One may find the density of \(T_a\) by considering \(X_t=\max_{0\le s\le t}B_s\), and noticing that \(\{T_a\le t\}=\{X_t\ge a\}\).
