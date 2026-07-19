# Probability, PhD exam, May 2023

*Carefully justify your answers.*

**1.** Give the mathematical definition of:
* 1. conditional expectation,
* 2. martingale,
* 3. Poisson process,
* 4. standard Brownian motion.

**2.** This problem has three parts.
* 1. State the weak and strong law of large numbers for i.i.d. random variables.
* 2. Prove the strong law of large numbers under the additional assumption of finite fourth moment (\mathbb E[X_1^4]<+\infty).
* 3. Let (\{B_t\}) be a standard Brownian motion. Prove that (\left\{\frac{B_n}{n}\right\}) converges to (0) almost surely as (n\to+\infty) (n\in\mathbb N).

**3.** This problem has two parts.
* 1. Let (X) be a random variable with a standard Gaussian distribution. Find the probability density function of (e^X).
* 2. Let (X) be a random variable with a standard Cauchy distribution. Find the probability density function of (\frac{1}{X}).

**4.** This problem has two parts.
* 1. Let (p\ge 1). Prove that if (X) is a random variable, then
  [\mathbb E[|X|^p]=\int_0^{+\infty}p x^{p-1}\mathbb P(|X|\ge x)\,dx.]
* 2. Let (p\ge 1). Let (X) and (Y) be two independent random variables with (\mathbb E[Y]=0). Show that
  [\mathbb E[|X+Y|^p]\ge\mathbb E[|X|^p].]

**5.** Let (\{a_n\}_{n\ge1}) be a sequence of real numbers such that (0<\sum_{k=1}^{+\infty}|a_k|^2<+\infty). Denote (\|a_n\|=\sqrt{\sum_{k=1}^n|a_k|^2}) and (\|a\|=\sqrt{\sum_{k=1}^{+\infty}|a_k|^2}). Let (\{X_n\}_{n\ge1}) be a sequence of i.i.d. symmetric Bernoulli, that is
[\forall k\ge1,\qquad \mathbb P(X_k=1)=\mathbb P(X_k=-1)=\frac12.]
Denote, for (n\ge1), (S_n=\sum_{k=1}^n a_kX_k), and denote (\mathcal F_n=\sigma\{S_1,\ldots,S_n\}).
* 1. Prove that (\{S_n\}) is an (\{\mathcal F_n\})-martingale.
* 2. Prove that (\{S_n\}) converges almost surely.
* 3. Prove that for all (n\ge1), for all (\lambda\in\mathbb R),
  [\mathbb E[e^{\lambda S_n}]\le e^{\frac{\lambda^2\|a_n\|^2}{2}}.]
  (Hint: (\frac{e^x+e^{-x}}2\le e^{\frac{x^2}{2}}))
* 4. Use question 3. and the symmetry of (S_n) to prove that for all (n\ge1), for all (x\ge0),
  [\mathbb P(|S_n|\ge x)\le 2e^{-\frac{x^2}{2\|a_n\|^2}}.]
  (Hint: The minimum of the function (\lambda\mapsto e^{-\lambda x}e^{\frac{\lambda^2\|a_n\|^2}{2}}) is attained at (\lambda=\frac{x}{\|a_n\|^2}))
* 5. Deduce the Khintchine inequality: (\forall p\ge1), (\forall n\ge1),
  [\mathbb E\left[\left|\sum_{k=1}^n a_kX_k\right|^p\right]^{\frac1p}\le C\|a_n\|,]
  where (C) is a numerical constant depending on (p) only (You do not need to compute (C)).

  (Hint: (\mathbb E[|X|^p]=\int_0^{+\infty}p x^{p-1}\mathbb P(|X|\ge x)\,dx))

**6.** This problem has three parts.
* 1. Give the definition of convergence of a sequence of random variables in probability and in distribution.
* 2. Which mode of convergence is stronger between convergence in probability and in distribution? Prove it.
* 3. Give a counterexample showing that convergence in probability is not equivalent to convergence in distribution.

**7.** Let (\{B_t\}) be a standard Brownian motion. Define, for (x\in\mathbb R),
[T_x=\min\{t\ge0:B_t=x\}.]
* 1. Prove that for all (x\in\mathbb R), (T_x) is finite almost surely (that is, (\mathbb P(T_x<+\infty)=1)).
* 2. Find (\mathbb P(T_{-2}<T_1)). You can use a picture as justification.

**8.** Let (n\in\mathbb N). Let (X_1,\ldots,X_n) be i.i.d. random variables in (L_1). Find (\mathbb E[X_1\mid X_1+\cdots+X_n]).
