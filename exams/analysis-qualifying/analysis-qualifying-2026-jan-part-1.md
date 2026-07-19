# Analysis, qualifying exam, January 2026, Part 1

*Write solutions in a neat and logical fashion, giving complete reasons for all steps. Do three of four.*

**1.** Do two of three.
* (i) Give an example of a Lebesgue measurable set \(E \subseteq [0,1]\) that is closed, has positive measure, but contains no non-trivial interval or explain why no such example exists.
* (ii) Is the function \(g:\mathbb{R}\to\mathbb{R}\) defined by \(g(x)=\frac{1}{1+x^2}\) the Hardy–Littlewood maximal function of an \(\mathcal{L}^1(\mathbb{R})\) function \(f\)?
* (iii) Does there exist a measure space \((X,\mathcal{M},\mu)\) and a nested decreasing sequence \((E_n)_{n=1}^{\infty}\) of measurable sets such that
  \[
  \lim_{n\to\infty}\mu(E_n)\ne\mu\left(\bigcap_{n=1}^{\infty}E_n\right)?
  \]

**2.** Suppose \(f:[0,1]\times[0,1]\to\mathbb{R}\). Show, if (a)–(c), then \(F:[0,1]\to\mathbb{R}\) defined by
\[
F(x)=\int_{[0,1]}f(x,y)\,d\lambda(y)
\]
is continuous. Here \(\lambda\) denotes Lebesgue measure on \(\mathbb{R}\).
* (a) for each \(x\in[0,1]\) the function \(g_x(y)=f(x,y)\) is continuous;
* (b) for each \(y\in[0,1]\) the function \(h_y(x)=f(x,y)\) is continuous; and
* (c) \(f\) is bounded,

**3.** Let \((X,\mathcal{M})\) denote a measurable space and let \(P(X)\) denote the power set of \(X\). Prove, if \(\mathcal{M}\ne P(X)\) and \(\{x\}\in\mathcal{M}\) for each \(x\in X\), then there exists an \(A\notin\mathcal{M}\otimes\mathcal{M}\) such that \([A]_x,[A]^y\in\mathcal{M}\) for all \(x\in X\). Suggestion: First show \(\delta:X\to X\times X\) defined by \(\delta(x)=(x,x)\) is measurable from \((X,\mathcal{M})\) to \((X\times X,\mathcal{M}\otimes\mathcal{M})\).

**4.** Suppose \((X,\mathcal{M},\mu)\) is a measure space and \(f,g:X\to[0,\infty)\) are measurable. Show
* (a) \(\mu_f:\mathcal{M}\to[0,\infty]\) defined by \(\mu_f(A)=\int \chi_Af\,d\mu=\int_A f\,d\mu\) is a measure; and
* (b) \(\int g\,d\mu_f=\int gf\,d\mu\).
