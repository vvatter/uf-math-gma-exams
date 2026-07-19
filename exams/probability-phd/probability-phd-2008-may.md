# Probability PhD exam, May 2008

**1.** Let \(\mathcal F\) be a sigma field. Two random variables \(X\) and \(Y\) satisfy
\[
\mathbb E[Y^2\mid\mathcal F]=X^2,\qquad \mathbb E[Y\mid\mathcal F]=X.
\]
Show that \(X=Y\) a.s.

**2.** Let \(X\) and \(Y\) be two independent random variables with the same probability distribution \(F(x)\). If \((X+Y)/\sqrt{2}\) has the same probability distribution \(F(x)\), then
\[
F(x)=\int_{-\infty}^{x}\frac{1}{\sqrt{2\pi}}e^{-y^2/2}\,\mathrm{d}y.
\]

**3.** Let \(f_n(x_1,\ldots,x_n)\) be the probability density function of the random vector \((X_1,\ldots,X_n)\) and \(g_n(x_1,\ldots,x_n)\) be the probability density function of the random vector \((Y_1,\ldots,Y_n)\). We define
\[
Z_n=\frac{g_n(X_1,\ldots,X_n)}{f_n(X_1,\ldots,X_n)},
\]
if \(f_n(X_1,\ldots,X_n)>0\), otherwise \(Z_n=0\). Show that \(\{Z_n,n=1,2,\ldots\}\) is a supermartingale.

**4.** Let \(X_1,X_2,\ldots\) be a sequence of i.i.d random variables with mean \(0\) and variance \(\sigma^2<\infty\). If \(S_n=X_1+X_2+\cdots+X_n\), then
\[
\lim_{n\to\infty}\mathbb E\left[\frac{|S_n|}{\sqrt n}\right]=\sqrt{\frac{2}{\pi}}\sigma.
\]

**5.** Let \(B_t\) be a standard Brownian motion and define
\[
D_n=\max_{n\le t\le n+1}|B_t-B_n|.
\]
Prove that \(D_n/n\) converges to \(0\) with probability one.

**6.** Consider square integrable random vectors
\[
Y=\bigl(y(1),y(2),\ldots,y(d)\bigr)
\]
and
\[
Y_n=\bigl(y_n(1),y_n(2),\ldots,y_n(d)\bigr),\qquad n\in\mathbb N,
\]
which satisfy
\[
\lim_{n\to\infty}\mathbb E\bigl(|y_n(j)-y(j)|^2\bigr)=0\qquad\text{for }j=1,2,\ldots,d.
\]
Show that the mean of \(Y_n\) converges to the mean of \(Y\), and the covariance matrix of \(Y_n\) converges to that of \(Y\).

**7.** Suppose that \(\{X_t\}\) and \(\{Y_t\}\) are both standard Brownian motion and are independent. Let \(\mathcal F_t\) denote the \(\sigma\)-field \(\sigma(X_s,Y_s\mid s\in[0,t])\). Prove that
\[
Z_t=X_t^2Y_t-\int_0^t Y_u\,\mathrm{d}u
\]
is an \(\mathcal F_t\)-martingale.

**8.** Let \(\mathcal F\) be a sub-sigma field of \(\mathcal G\) and \(Z\) be a nonnegative random variable defined on probability space \((\Omega,\mathcal G,\mathbb P)\) with \(\mathbb E_{\mathbb P}[Z]=1\). Define
\[
\mathbb Q(A)=\int_A Z\,\mathrm{d}\mathbb P\qquad\text{for }A\in\mathcal G.
\]
* a). Show that \(\mathbb Q\) is a probability measure on \((\Omega,\mathcal G)\).
* b). For a random variable \(X\), we have
  \[
  \mathbb E_{\mathbb Q}[X\mid\mathcal F]=\frac{\mathbb E_{\mathbb P}[ZX\mid\mathcal F]}{\mathbb E_{\mathbb P}[Z\mid\mathcal F]}.
  \]
