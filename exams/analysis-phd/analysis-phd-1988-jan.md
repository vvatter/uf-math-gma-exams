# Analysis, PhD exam, January 1988

*Answer all six questions. Justify all work. To obtain any partial credit, all work must be presented in a neat and logical fashion.*

**1.** State and prove the Radon–Nikodym Theorem.

**2.** State and prove the Hahn–Banach Theorem.

**3.** Let \(\Omega\) be a topological space, \(\mathcal B(\Omega)\) the Borel subsets of \(\Omega\). Suppose that for each \(n\), \(\mu_n\) is a countably additive positive finite regular measure defined on \(\mathcal B(\Omega)\). Let
\[
\mu(\mathord\cdot)=\sum_{n=1}^{\infty}\frac{\mu_n(\mathord\cdot)}{2^n\bigl(1+\mu_n(\Omega)\bigr)}.
\]
Show that \(\mu\) is also a regular countably additive measure.

**4.** Let \(\{f_n:n\geq 0\}\) and \(\{g_n:n\geq -1\}\) be two sequences of real-valued measurable functions on a measurable space \((\Omega,\mathcal F)\). Let \(B\subset\mathbb R^1\) be a Borel set on \(\mathbb R^1\). Define
\[
T(w)=
\begin{cases}
\sup\{n\geq 0:f_n(w)\in B\},&\text{if }\{n\geq 0:f_n(w)\in B\}\text{ is bounded and nonempty},\\
0,&\text{if }\{n\geq 0:f_n(w)\in B\}=\varnothing,\\
-1,&\text{if }\{n\geq 0:f_n(w)\in B\}\text{ is unbounded}.
\end{cases}
\]
* (A) Prove \(T\) is \(\mathcal F\)-measurable.
* (B) Define \(h(w)=g_{T(w)}(w)\); prove \(h\) is \(\mathcal F\)-measurable.

**5.** Let \(T:(-\pi/2,\pi/2)\to\mathbb R\) be given by \(T(x)=\tan x\). Let \(\lambda\) be Lebesgue measure on \((-\pi/2,\pi/2)\) and define a measure \(\mu\) on \((\mathbb R,\mathcal B(\mathbb R))\) by setting \(\mu(A)=\lambda(T^{-1}(A))\). Compute \(\dfrac{d\mu}{dx}\).

**6.** Fix \(1\leq p<\infty\), and let \(f\in L^p(X,\mathcal A,\mu)\). Show that
\[
\lVert f\rVert_p=\sup\left\{\int fg\,d\mu:\lVert g\rVert_q\leq 1\right\}.
\]
Hint:
* 1. Show that if \(\lVert g\rVert_q\leq 1\), then \(\int fg\,d\mu\leq\lVert f\rVert_p\).
* 2. Show that \(g=|f|^{p-1}\in L^q\).
* 3. State why doing 1. and 2. solves the problem.
