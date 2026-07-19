# Analysis, PhD exam, August 2018

*Do six of eight. Write solutions in a neat and logical fashion, giving complete reasons for all steps.*

**1.** Let \(X,Y\) be topological spaces. Prove, if \(f:X\to Y\) is continuous, then \(f\) is Borel measurable.

**2.** Let \((X,\mathcal M,\mu)\) be a \(\sigma\)-finite measure space and let \(f\in L^1(\mu)\). Prove that for every \(\epsilon>0\) there exists a \(\delta>0\) such that if \(E\in\mathcal M\) and \(\mu(E)<\delta\), then
\[
\int_E |f|\,d\mu<\epsilon.
\]

**3.** Do two. In each case, give a brief justification for your answer.
* (a) Give an example, if possible, of a sequence \((f_n)\subset L^1(\mathbb R)\) and an \(f\in L^1(\mathbb R)\) such that \(f_n\to f\) uniformly on \(\mathbb R\) but \(f_n\) does not converge to \(f\) in the \(L^1\) norm.
* (b) Evaluate
  \[
  \lim_{n\to\infty}\int_1^\infty \frac{e^{inx}}{x^n}\,dx.
  \]
* (c) Give an example to show that the \(\sigma\)-finiteness hypothesis is necessary in Tonelli’s theorem.

**4.** Let \((X,\mathcal M,\mu)\) be a \(\sigma\)-finite measure space and \(\mathcal N\subset\mathcal M\) a sub-\(\sigma\)-algebra. Put \(\nu=\mu|_{\mathcal N}\). Prove, if \(\nu\) is \(\sigma\)-finite and \(f\in L^1(\mu)\), then there exists a \(g\in L^1(\nu)\) such that for all \(E\in\mathcal N\),
\[
\int_E f\,d\mu=\int_E g\,d\nu.
\]

**5.** Let \((X,\mathcal M,\mu)\) be a \(\sigma\)-finite measure space. Fix a measurable function \(f:X\to\mathbb C\).
* (a) Assuming \(f\in L^\infty(\mu)\), show if \(g\in L^1(\mu)\), then \(fg\in L^1(\mu)\) and the mapping \(M_f:L^1(\mu)\to L^1(\mu)\) defined by \(M_fg=fg\) is a bounded linear transformation.
* (b) Conversely, show, if \(fg\in L^1(\mu)\) for each \(g\in L^1(\mu)\), then \(f\in L^\infty(\mu)\).

**6.** Fix \(1<p<\infty\) and let \(\frac1p+\frac1q=1\). Let \((f_n)\) be a sequence in \(L^p[0,1]\). Suppose that for every \(g\in L^q[0,1]\), the limit
\[
\lim_{n\to\infty}\int_0^1 f_ng
\]
exists. Prove that there exists an \(f\in L^p[0,1]\) such that
\[
\lim_{n\to\infty}\int_0^1 f_ng=\int_0^1 fg
\]
for all \(g\in L^q[0,1]\). (Hint: first show that the assignment \(g\mapsto\lim\int f_ng\) defines a linear functional on \(L^q\).)

**7.** Let \(X\) be a Banach space. Say a sequence \((x_n)\) from \(X\) converges weakly to \(x\in X\) if \(f(x_n)\to f(x)\) for every \(f\in X^*\). Prove that if \(Y\) is a closed subspace of \(X\), \((x_n)\subset Y\), and \(x_n\to x\) weakly, then \(x\in Y\).

**8.** Let \(X\) be a Banach space, \(Y\subset X\) a closed subspace. Say \(Y\) is complemented in \(X\) if there exists a closed subspace \(Z\subset X\) such that \(Y\cap Z=\{0\}\) and \(Y+Z=X\).

Prove, if \(Y\) is complemented in \(X\), then there exists a bounded linear operator \(T:X\to Y\) such that \(T(y)=y\) for all \(y\in Y\).
