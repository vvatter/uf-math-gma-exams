# Analysis, PhD exam, May 1997

*Be sure to write all steps in a neat and logical fashion to receive credit. Give reasons for your steps.

Definition: A σ-algebra \(\mathcal F\) is separable if \(\mathcal F=\sigma\{A_j:j\geq 1\}\) for some sequence of sets \(A_j\).*

**1.** Let \(\{\mathcal F_k\}\) be a sequence of separable σ-algebras of subsets of a set \(X\). Let \(\mathcal F\) be the smallest σ-algebra of subsets of \(X\) which contains \(\mathcal F_k\) for each \(k\). Prove that \(\mathcal F\) is separable. [Hint: Use the monotone class theorem.]

**2.** Let \((X,\mathcal F,\mu)\) be a finite measure space and let \((Y,\Sigma)\) be a measurable space. Let \(f:X\to Y\) be \(\mathcal F,\Sigma\)-measurable. Define \(\nu(B)=\mu(f^{-1}(B))\) for \(B\in\Sigma\). Show \(\nu\) is a measure on \(\Sigma\), and if \(g:Y\to[0,\infty]\) is \(\Sigma\)-measurable, then \(\int_Y g\,d\nu=\int_X g\circ f\,d\mu\).

**3.** Let \(m\) be Lebesgue measure on \(\mathbb R\). Let \(f_m=-\mathbf 1_{A_m}\), where \(A_m=(m,\infty)\). Show \((f_m)\) is increasing, but the monotone convergence theorem is not true. Why is this?

**4.** Let \((X,\mathcal S,\mu)\) and \((Y,\mathcal J,\nu)\) be two finite measure spaces. Construct the product measure \(\mu\times\nu\) on \(\mathcal S\otimes\mathcal J\). Be sure to prove \(\mu\times\nu\) is countably additive.

**5.** Let \((X,\Sigma,\mu)\) be a finite measure space. Prove that the dual of \(L^1(X,\Sigma,\mu)\) is isometrically isomorphic to \(L^\infty(X,\Sigma,\mu)\).

**6.** Let \((X,\mathcal F,\mu)\) be a finite measure space. Suppose that \(\mathcal F\) is separable. Show \(L^1(X,\mathcal F,\mu)\) is separable.

**7.** Let \((X,\mathcal F,\mu)\) be a measure space. Let \(\{f_m\}\) be a sequence of measurable functions such that \(\int_X|f_m|\,d\mu<\frac{1}{2^m}\). Does it follow that \(\sum_{m=1}^\infty f_m\) converges a.e. \(\mu\) on \(X\)?

**8.** Let \((\Omega,\mathcal F,P)\) be a probability space. Let \(X:\Omega\to\mathbb R\) be an integrable function. Let \(F(x)=P(X<x)\), for \(x\in\mathbb R\).
* (a) Show \(F:\mathbb R\to[0,1]\) is monotone, left continuous, \(\lim_{x\to-\infty}F(x)=0\), and \(\lim_{x\to\infty}F(x)=1\).
* (b) Show \(\int_\Omega X^2\,dP=\int_\mathbb R x^2\,dF(x)\).

**9.** Let \((\Omega,\mathcal F,P)\) be a probability space. Let \((X_m)\) be a sequence of independent random variables on \(\Omega\).
* (a) Show \((\overline{\lim}X_m>3)\) is a tail event relative to \((X_m)\).
* (b) If \(P(\overline{\lim}X_m>3)>0.2\), what is \(P(\overline{\lim}X_m>3)\)?

**10.** Let \(\ell^\infty\) be the Banach space consisting of all real sequences \((a_i)\) such that \(\sup_i|a_i|<\infty\), with \(\|(a_i)\|:=\sup_i|a_i|\). Let \(c\) be the subspace of \(\ell^\infty\) consisting of \((a_i)\) such that \(\lim a_i\) exists. Prove that there exists a continuous linear functional \(F:\ell^\infty\to\mathbb R\) such that \(F((a_i))=\lim a_i\) for each \((a_i)\in c\). [Hint: Use the Hahn–Banach theorem.]
