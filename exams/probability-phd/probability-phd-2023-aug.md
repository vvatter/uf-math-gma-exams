# Probability PhD exam, August 2023

*Carefully justify your answers.*

**1.** Let \(X,Y:(\Omega,\mathcal{F},\mathbb{P})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))\) be random variables. Prove that
\[
\mathbb{P}(X+Y\ge 0)\le \mathbb{P}(X\ge 0)+\mathbb{P}(Y\ge 0).
\]

**2.** This problem has two parts.
* 1. Give the mathematical definition of:
    * (a) convergence almost sure,
    * (b) convergence in probability,
    * (c) convergence in \(L^1\),
    * (d) convergence in distribution.
* 2. For \(n\ge 1\), let \(X_n\) be uniformly distributed on \(\{1,\ldots,n\}\), that is
  \[
  \mathbb{P}(X_n=k)=\frac{1}{n},\qquad k\in\{1,\ldots,n\}.
  \]
  Prove that \(\left\{\frac{X_n}{n}\right\}_{n\ge 1}\) converges to \(U\) in distribution, where \(U\) is uniform on \([0,1]\).

**3.** Let \(\{X_i\}_{i\ge 1}\) be a sequence of i.i.d. continuous random variables having a uniform distribution on \([0,1]\). Define, for \(n\ge 1\),
\[
Y_n=\max(X_1,\ldots,X_n).
\]
* 1. Find the cumulative distribution function (CDF) of \(Y_n\), \(n\ge 1\).
* 2. Compute \(\mathbb{E}[Y_n]\) and \(\operatorname{Var}(Y_n)\).
* 3. Prove that \(\{Y_n\}\) converges to \(1\) in \(L^1\). What about almost sure convergence?

**4.** Let \(\{X_i\}_{i\ge 1}\) be a sequence of i.i.d. random variables with a Poisson distribution of parameter \(\lambda\).
* 1. Let \(n\ge 1\). Without justification, what is the distribution of \(X_1+\cdots+X_n\)?
* 2. State the weak and strong law of large numbers for i.i.d random variables.
* 3. Let \(\phi:\mathbb{R}\to\mathbb{R}\) be an arbitrary bounded continuous function. Prove that
  \[
  \lim_{n\to+\infty}\sum_{k=0}^{+\infty}e^{-n\lambda}\frac{(n\lambda)^k}{k!}\phi\left(\frac{k}{n}\right)=\phi(\lambda).
  \]

**5.** This problem has three parts.
* 1. Give the mathematical definition of standard Brownian motion.
* 2. Let \(\{B_t\}\) be a standard Brownian motion. Prove that \(\left\{\frac{B_n}{n}\right\}\) converges to \(0\) almost surely as \(n\to+\infty\) (\(n\in\mathbb{N}\)).
* 3. Find \(\mathbb{P}(B_2\ge 0,B_1\le 0)\).

**6.** Let \(\{M_n\}_{n\ge 0}\) be a sequence of integrable random variables adapted to a filtration \(\{\mathcal{F}_n\}\). Assume that for each bounded stopping time \(T\), \(\mathbb{E}[M_T]=\mathbb{E}[M_0]\). Show that \(\{M_n\}_{n\ge 0}\) is a martingale.

**7.** Let \(\{B_t\}\) be a standard Brownian motion. Define, for \(x\in\mathbb{R}\),
\[
T_x=\min\{t\ge 0:B_t=x\}.
\]
* 1. Prove that for all \(x\in\mathbb{R}\), \(T_x\) is finite almost surely (that is, \(\mathbb{P}(T_x<+\infty)=1\)).
* 2. Find \(\mathbb{P}(T_3<T_{-1})\). You can use a picture as justification.
