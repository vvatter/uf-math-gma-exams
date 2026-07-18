# Analysis, PhD exam, January 1989

*Answer 6 out of the 7 problems. Justify all work. To obtain any partial credit, all work must be presented in a neat, logical and concise fashion.*

**1.** Let \(f\) be a Borel-measurable function defined on \([0,1]\) with \(\infty>f(x)\ge 0\).
* Part (a) Prove that there is a non-increasing function \(f^*\) defined on \([0,1]\) such that
  \[
  m\{x:f^*(x)\ge\lambda\}=m\{x:f(x)\ge\lambda\}
  \]
  for every \(\lambda\ge 0\), where \(m\) is Lebesgue measure on \([0,1]\). (\(f^*\) is called a monotone rearrangement of \(f\).)
* Part (b) Show that \(\int f^*\,dm=\int f\,dm\).

**2.** Let \((X,\mathcal F,\mu)\) be a finite measure space, and let \(f\) and \(g\) be two measurable functions such that
\[
\mu(f\in A,\ g\in B)=\mu(f\in A)\mu(g\in B)
\]
for every \(A,B\in\mathcal B(\mathbb R)\). Let \(\nu(A)=\mu(g\in A)\). Show that
\[
\int H(f,g)\,d\mu=\int\!\int H(f,t)\,\nu(dt)\,d\mu
\]
for every positive \(\mathcal B(\mathbb R^2)\)-measurable function \(H\).

**3.** Consider \(\ell^\infty=\{(a_n)_{n=1}^\infty:\sup_n|a_n|<\infty\}\). This space becomes a Banach space when equipped with the norm \(\|(a_n)_{n=1}^\infty\|=\sup\{|a_n|:n\ge 1\}\).
* Part (a) Show there is a linear functional \(T:\ell^\infty\to\mathbb R\) with the property: if \(\lim_{n\to\infty}a_n\) exists, then
  \[
  T[(a_n)_{n=1}^\infty]=\lim_{n\to\infty}a_n.
  \]
  (Use the Hahn–Banach theorem.)
* Part (b) Modify your proof in (a) to show there is a linear functional \(S:\ell^\infty\to\mathbb R\) with the property: if \(\lim_{n\to\infty}n^{-1}\sum_{k\le n}a_k\) exists, then
  \[
  S[(a_n)_{n=1}^\infty]=\lim_{n\to\infty}n^{-1}\sum_{k\le n}a_k.
  \]

**4.** State and prove the Radon–Nikodym theorem.

**5.** State and prove Fubini’s theorem.

**6.** Let \(\mu\) be a measure on \(((0,\infty),\mathcal B(0,\infty))\) defined by
\[
\mu(A)=\int_A |x|^{-1/2}\,dx.
\]
Let \(T:(0,\infty)\to(0,\infty)\) be given by \(T(x)=x^{-1}\). Define a new measure \(\pi\) on \((0,\infty)\) by setting \(\pi(A)=\mu(T^{-1}(A))\). Compute \(d\pi/d\mu\).

**7.** Let \(c(t)\) be a function defined on \([0,\infty)\) with the following properties: \(c(t)\) is strictly increasing and continuous, \(c(0)=0\), and \(c(\infty)=\infty\). Let \(\tau_t=\inf\{s:c(s)>t\}\). Prove that
\[
\int_0^\infty f(t)\,c(dt)=\int_0^\infty f(\tau_t)\,dt
\]
for every positive continuous function \(f\) on \([0,\infty)\).
