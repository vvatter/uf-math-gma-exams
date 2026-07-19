# Probability PhD exam, May 2003

*Write clearly. State precisely results you use. Do not omit steps.*

**1.** Let \((\overline X_m)_{m=1}^{\infty}\) be an i.i.d. sequence of real valued variables on \((\Omega,\mathcal F,P)\). Let \(\mathcal F_m=\sigma(\overline X_1,\ldots,\overline X_m)\). Put \(S_m=\overline X_1+\cdots+\overline X_m\), for \(m\geq1\), and put \(S_0=0\). Which of the following sequences are martingales relative to \(\mathcal F_m\)? For those which are not martingales with respect to this filtration, what conditions have to be added to make them martingales?
* a) \(S_m\), \(m=0,1,2,\ldots\), \(E[|\overline X_1|]<\infty\).
* b) \(\overline X_1^2+\cdots+\overline X_m^2-m\lambda\), \(m=1,2,\ldots\), \(E(\overline X_1^2)<\infty\), \(\lambda\) real.
* c) \(\exp(\alpha S_m-m\lambda)\), \(m=0,1,2,\ldots\), where \(\varphi(\alpha)=E[\exp(\alpha\overline X_1)]<\infty\), \(\alpha,\lambda\) real.
* d) \(\overline Y_m=S_{\min(m,T)}\), \(m=0,1,2,\ldots\), where \(P(\overline X_1=\pm1)=\frac12\) and \(T=\min\{n>0:S_n=0\}\).

**2.** Let \(\{\alpha_m\}_{m=1,2,\ldots}\) be a sequence of probability measures on \(\mathbb R\). Show the following are equivalent:
* a) There exists a probability measure \(\alpha\) on \(\mathbb R\) such that \(\lim_{m\to\infty}\alpha_m(I)=\alpha(I)\) for all closed intervals \(I\) on \(\mathbb R\) whose end points are continuity points of \(\alpha\).
* b) If \(\{F_m\}\), respectively \(F\), are the distribution functions of \(\{\alpha_m\}\), respectively \(\alpha\), then \(\lim_{m\to\infty}F_m(x)=F(x)\) at every point \(x\) of continuity of \(F\).

**3.** Let \(\{\alpha_m\}_{m=1,2,\ldots}\) be a sequence of probability measures on \(\mathbb R\), and let \(\{\varphi_m(t)\}_{m=1,2,\ldots}\) be the corresponding characteristic functions. Assume that \(\lim_{m\to\infty}\varphi_m(t)=\varphi(t)\) for all \(t\in\mathbb R\), and \(\varphi(t)\) is continuous at \(t=0\). Prove that \(\varphi(t)\) is the characteristic function of some probability measure and that the conditions of Problem 2 hold.

**4.** If \(\overline X\) is a real valued random variable, show that for \(0<\varepsilon<1\),
\[
E\left[\frac{|\overline X|}{1+|\overline X|}\right]\leq \varepsilon+P[|\overline X|>\varepsilon]
\]
and that
\[
P(|\overline X|>\varepsilon)\leq\frac{1+\varepsilon}{\varepsilon}E\left[\frac{|\overline X|}{1+|\overline X|}\right].
\]
Deduce that the set of real valued random variables on a given probability space can (with suitable identification) be regarded as a metric space if the distance between two random variables \(\overline X\) and \(\overline Y\) is defined to be
\[
d(\overline X,\overline Y)=E\left[\frac{|\overline X-\overline Y|}{1+|\overline X-\overline Y|}\right],
\]
and that convergence in this metric space corresponds to convergence in probability.

**5.** This problem has three parts.
* a) Let \(\overline X_m\), \(m=1,2,\ldots\), be i.i.d., \(\overline X_m>0\), \(E[\overline X_m]=1\), and \(\overline Y_m=\prod_{k=1}^m\overline X_k\). Prove that \(\overline Y_m\) is a martingale relative to the filtration \(\mathcal F_m=\sigma(\overline X_1,\ldots,\overline X_m)\). Show that \(\lim_{m\to\infty}\overline Y_m=\overline Y_\infty\) exists a.s.
* b) Show that \(P[\overline Y_\infty=0]=0\) or \(1\).

  Hint: Recall infinite products and the zero-one law.
* c) Using b), show that
  \[
  E[\overline Y_\infty]=1\quad\Longleftrightarrow\quad P[\overline Y_\infty>0]=1.
  \]

**6.** Let \(\overline X_m\), \(m=1,2,\ldots\), be a supermartingale such that
\[
E[|\overline X_{m+1}-\overline X_m|\mid\mathcal F_m]<M\quad\text{a.s.}
\]
Show that for any two optional times \(S\leq T\), \(E[T]<\infty\), we have \(E[|\overline X_T|]<\infty\) and
\[
E(\overline X_T\mid\mathcal F_S)\leq\overline X_S.
\]
