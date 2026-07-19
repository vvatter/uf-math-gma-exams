# Probability, PhD exam, September 1997

**1.** Let \(X\) and \(Y\) be independent and uniform on \([0,1]\). Find
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

**5.** What is an infinitely divisible distribution on \(\mathbb R^1\)? Prove that a non-trivial infinitely divisible distribution cannot have compact support.

**6.** Define a standard Brownian Motion \(W\) starting at 0. Define new processes \(W_1,W_2,W_3\) by:
\[
W_1(t)=cW\!\left(\frac{t}{c^2}\right),\qquad t\ge 0,\quad c\text{ real}\ne0,
\]
\[
W_2(t)=tW\!\left(\frac1t\right),\qquad t>0,\quad W_2(0)=0,
\]
\[
W_3(t)=
\begin{cases}
W(1)-W(1-t),&0\le t\le1,\\
W(t),&\text{otherwise}.
\end{cases}
\]
Show that \(W_1,W_2,W_3\) are the standard Brownian motions.

**7.** Let \(\varphi(t)=\int e^{itx}\,\mu(dx)\) be a characteristic function where \(\mu\) is a probability measure on \(\mathbb R^1\).
* a) Suppose \(|\varphi(t)|=1\) for some \(t\ne0\). Then prove that unless \(|\varphi(t)|\equiv1\), there is a smallest \(t_0\ne0\) and a \(d\) such that \(\mu\) is concentrated on the set
  \[
  \left\{d+\frac{2\pi j}{t_0}\right\},\qquad j=0,\pm1,\pm2,\ldots.
  \]
* b) Using a) prove that \(|\cos t|\) is not a characteristic function. Hint: \(\cos t\) and \(\cos^2t\) are characteristic functions.

**8.** Let \(S_n=(U_n,V_n)\) denote the position after \(n\) steps of a random walk on \(\mathbb Z^2\), starting from \((0,0)\). Suppose that
\[
U_{n+1}=U_n\pm1,
\qquad
V_{n+1}=V_n\pm1,
\]
where the signs are picked by two independent tosses of a fair coin, independently at each step. Define
\[
p_n=P(S_n=(0,0)),
\]
\[
\tau_n=\inf\{m>\tau_{n-1}:S_m=(0,0)\}.
\]
An easy fact is \(P(\tau_n<\infty)=P(\tau_1<\infty)^n\).
* (1) Prove that for any random walk \(S_n\in\mathbb Z^2\) the following are equivalent:
    * (i) \(P(\tau_n<\infty)=1\).
    * (ii) \(P(S_n=(0,0)\text{ i.o.})=1\).
    * (iii) \(\displaystyle\sum_{n=1}^{\infty}P(S_n=(0,0))=\infty\).
* (2) Find a formula for \(p_n\), \(n>0\).
* (3) Use (1) and Stirling’s formula
  \[
  n!\approx\sqrt{2\pi n}\left(\frac ne\right)^n e^S
  \qquad(S\to0\text{ as }n\to\infty)
  \]
  to show that the diagonal random walk in \(\mathbb Z^2\) is recurrent.

**9.** Let \((P_t)_{t>0}\) be a Markov semigroup. Assume \(P_t(x,dy)=p_t(x,y)\,dy\) with \(p_t(x,y)=p_t(y,x)\) and \(p_t(x,y)\le M(t)\), where \(M(t)\) is a constant depending on \(t\). If \(\mu\) is a finite signed measure, show that
\[
\int p_t(x,y)\,\mu(dx)\mu(dy)\ge0.
\]

**10.** An urn at \(t=0\) contains \(R_0\) (\(\ge1\)) red balls and \(B_0\) (\(\ge1\)) black balls, and “random sampling with double replacement” is called out as follows:

(i) Choose a ball at random (meaning that each ball in the urn has the same probability to be drawn), and note its color;

(ii) Replace this ball in the urn together with an extra ball of the same color;

(iii) Go to (i).

Let \(M_t\) be the proportion in red balls in the urn after \(t\) such operations, so that
\[
M_0=\frac{R_0}{R_0+B_0}.
\]
Show that, with respect to a suitable filtration (which you should specify), the sequence \(M_0,M_1,\ldots,M_t,\ldots\) is a martingale. Prove that \(M_t\) converges as \(t\to+\infty\) almost surely to a random variable \(M_\infty\), \(0\le M_\infty\le1\). Show that
\[
M_0=EM_1=EM_2=\cdots=EM_t=EM_\infty,
\]
and that
\[
M_0^2\le E[M_1^2]\le\cdots\le E[M_t^2]\le E[M_\infty^2],
\]
and that
\[
P(M_\infty=M_0)<1.
\]

*NOTE. You may quote without proof any martingale theorems you need, but should state them carefully.*

**11.** Let \(X_n\) be independent and all distributed according to standard normal distribution. Find constants \(C_n\) such that
\[
\limsup \frac{X_n}{C_n}=1\qquad\text{a.s.}
\]
Hint.
\[
\int_a^\infty e^{-b^2/2}\,db\le\frac1a e^{-a^2/2},
\]
and let \(c_n^2=2\log(n\log n)\).
