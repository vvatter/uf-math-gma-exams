# Complex Analysis, PhD exam, May 2000

*Notes. Please write up solutions to the eight problems 1–8, below. Please write LARGE, as the grader’s eyes are older and weaker than your eyes.*

*A square \(S\subset\mathbb C\) is a set of the form \([a,a+L]\times[b,b+L]\), where \(L\) is positive. Use “\(s:=\mathrm{Foo}\)” to mean that Foo is the definition of the new symbol \(s\).*

**1.** Find complex numbers \(a,b,c,d\), with \(ad-bc\ne0\), so that the Möbius transformation
\[
\mu(z):=\frac{az+b}{cz+d}
\]
carries the imaginary axis to the circle whose radius is \(2\) and whose center is \(3=3+0i\).

**2.** With \(B\) the open unit ball \(|z|<1\), consider a non-constant analytic function \(h:B\to\mathbb C\).
* i: Suppose that \(\Re(h(z))\ge0\) for each \(z\in B\). Prove that the inequality can then be strengthened to “\(>\)”.
* ii: With \(\Re(h(z))>0\) on \(B\), suppose further that \(h(0)=1\). Prove, for each \(z\in B\), that
  \[
  \frac{1-|z|}{1+|z|}\le |h(z)|\le\frac{1+|z|}{1-|z|}.
  \]

**3.** Suppose that \(P()\) is a monic polynomial with degree \(N\ge1\). Let \(\alpha_1,\ldots,\alpha_N\) be an enumeration (with multiplicity) of the zeros of \(P()\).
* ①: Suppose that \(\forall k:\ \Re(\alpha_k)>0\). Prove that all the zeros of the derivative, \(P'\), also lie in the positive half-plane, as follows: Establish that
  \[
  \frac{P'(z)}{P(z)}=\frac{1}{z-\alpha_1}+\frac{1}{z-\alpha_2}+\cdots+\frac{1}{z-\alpha_N},
  \]
  then use it to complete the proof.
* ②: Prove Lucas’s theorem: If all the zeros of a non-constant polynomial \(P\) lie in a convex polygon \(Q\subset\mathbb C\), then all the zeros of \(P'\) lie in \(Q\).
* ③: Show that ② can fail if \(P()\) is allowed to be a rational function: Namely, by letting
  \[
  P(z):=\frac{z}{z^2+1},
  \]
  find a half-plane \(H\) which owns a zero of \(P'\) but has no zero of \(P\).

**4.** Use the Residue Calculus to compute
\[
I:=\int_0^{+\infty}\frac{1}{[x^4+4]\cdot[x^2+9]^9}\,dx.
\]
To save arithmetic, you may define some explicit points \(P_1,\ldots,P_L\in\mathbb C\) (what should \(L\) be?) and explicit functions \(h_1,\ldots,h_L\), and then may express your answer in the form
\[
I=[h_1(P_1)+\cdots+h_L(P_L)]\cdot\text{Constant}.
\]
(Do not bother to perform the function-evaluation.)

**5.** This problem has two parts.
* a: State (but do not prove) Morera’s Theorem. (You may use this without proof in (b), if you wish.)
* b: Prove this version of the Schwarz Reflection Principle: Suppose \(f\) is continuous in the closed upper half-plane \(H=\mathbb R\times[0,\infty)\) and is analytic on the interior of \(H\). Further suppose that \(f\) is real-valued on the real-axis. By defining \(\Phi=f\) on \(H\), and
  \[
  \Phi(z):=\overline{f(\overline z)},\qquad\text{for all }z\in\mathbb C\setminus H,
  \]
  extend \(f\) to all of \(\mathbb C\). Then this \(\Phi\) is analytic.

**6.** This problem has three parts.
* ①: Please state Picard’s Theorem.
* ②: Let \(f\) be meromorphic in the whole complex plane. Suppose that the range of \(f\) omits three distinct values (one of them can be \(\infty\)). Prove that \(f\) is constant.
* ③: Suppose that \(f\) and \(g\) are entire functions such that, on \(\mathbb C\),
  \[
  f^3+g^3=1.
  \]
  Prove that \(f\) and \(g\) are each constant functions. [Note: Symbol \(f^3\) means \(f\cdot f\cdot f\).]

**7.** Fix a real \(b>0\). Write down an entire function, \(f\), that vanishes precisely on the sequence \((z_n)_{n=1}^{\infty}\), where \(z_n:=n^b\).

**8.** Show that all roots of polynomial \(P(z):=z^5+15z+1\) lie in the ball \(|z|<2\), but that only one root satisfies \(|z|<\frac32\).
