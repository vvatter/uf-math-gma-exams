# Analysis, PhD exam, January 1997

## I.

*State the following theorems.*

**1.** The monotone convergence theorem for nets in \(L^p\).

**2.** The Hahn decomposition theorem.

**3.** The Egorov theorem.

**4.** The Vitali convergence theorem.

**5.** The Radon–Nikodym theorem.

**6.** The Fubini theorem.

**7.** The representation of the dual of \(L^p\).

**8.** The Lebesgue dominated convergence theorem.

## II

*Prove one of the theorems 6 or 7.*

## III.

*Solve 5 of the following problems.*

*In what follows, \((X,\Sigma,\mu)\) is a measure space.*

**1.** Let \((f_n)\) be a sequence of real-valued measurable functions on \(X\), and let \(f\) be a real measurable function on \(X\). Prove that \((f_n)\) converges to \(f\) in \(\mu\)-measure, \(f_n\xrightarrow{\mu}f\), iff every subsequence \((f_{n_i})\) contains a further subsequence \((f_{n_{i_j}})\) converging to \(f\), \(\mu\)-a.e.

**2.** Let \((f_n)\) be a sequence of positive, \(\mu\)-integrable functions such that \(\sum_n\int f_n\,d\mu<\infty\). For each \(x\in X\), denote \[L(x)=\sup\{n:f_n(x)>1\}.\] Prove that \(L(x)<\infty\), \(\mu\)-a.e.

**3.** Let \(f:\mathbb R\to\mathbb R\) be a Lebesgue integrable function. Prove that for every \(\varepsilon>0\), there is a bounded interval \(I\) such that \(\left|\int_E f\,dx\right|<\varepsilon\) for every measurable set \(E\) with \(E\cap I=\varnothing\).

**4.** Let \(F\) be a Banach space and \(\mathcal F\subseteq\Sigma\) a sub-σ-algebra. Prove the existence of the conditional expectation \(E(f\mid\mathcal F)\) for every \(\mu\)-integrable function \(f:X\to F\).

**5.** Let \((X,\mathcal S,\mu)\) and \((Y,\mathcal T,\nu)\) be two real measure spaces. Prove the existence of the product measure \(\mu\times\nu\) and that \(|\mu\times\nu|=|\mu|\times|\nu|\).

**6.** Let \(\mu\) be the Lebesgue measure on \(\mathbb R\), and let \(f\) be a Lebesgue integrable function on \(\mathbb R\) such that \(\int_0^x f\,d\mu=0\) for every \(x\in\mathbb R\) (if \(x<0\), \(\int_0^x=-\int_x^0\)). What can you say about \(f\)?

**7.** Let \(\mu\) be the Lebesgue measure on \(\mathbb R\), and let \(f_n=-\varphi_{(n,\infty)}\), \(n=1,2,\ldots\). Show that \((f_n)\) is increasing but that the conclusion of the monotone convergence theorem is not true. Explain why.

**8.** Let \(\mu\) be the Lebesgue measure on \((0,1)\). Each point \(x\in(0,1]\) has a binary expansion \[x=\sum_{i=1}^{\infty}\frac{x_i}{2^i},\] where \(x_i=0\) or \(1\). (The expansion is unique except on a countable set, which we can throw out of the space.)
* (i) Define \(T_i(x)=x_i\). Sketch the graphs of \(T_1,T_2,T_3\).
* (ii) Let \(\mathcal F_k=\sigma(T_1,T_2,\ldots,T_k)\). Describe \(\mathcal F_k\).
* (iii) Let \(f\in L^2(\mu)\). Find a function \(g_1\) which is \(\mathcal F_1\)-measurable and satisfies \[\int_A g_1\,d\mu=\int_A f\,d\mu\quad\text{for }A\in\mathcal F_1.\] That is, find \(g_1=E(f\mid\mathcal F_1)\). Find \(g_2=E(f\mid\mathcal F_2)\).
