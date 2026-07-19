# Analysis, PhD exam, January 2019

*Do three from part A and three from part B. Write solutions in a neat and logical fashion, giving complete reasons for all steps.*

## Part A

**1.** Let \(X,Y\) be topological spaces. Prove that every continuous function \(f:X\to Y\) is Borel measurable.

**2.** Short answer.
* (a) Give an example, if possible, of a closed set \(E\subset\mathbb R\) of positive Lebesgue measure that contains no interval.
* (b) For \(n\geq 2\), let \(f_n=e^{inx}x^{-n}\). Find
  \[
  \lim_{n\to\infty}\int_1^\infty f_n\,dx.
  \]
* (c) Give an example, if possible, of strict inequality in Fatou’s Lemma.

**3.** Let \(X=Y=[0,1]\), \(\mathcal M=\mathcal B_{[0,1]}\) denote the Borel \(\sigma\)-algebra, and \(\mathcal N=2^{\mathbb R}\). Let \(\mu\) Lebesgue measure on \(\mathcal M\), and let \(\nu\) counting measure on \(\mathcal N\). Prove that \(\Delta=\{(x,x):x\in[0,1]\}\subset[0,1]\times[0,1]\) is an element of the product \(\sigma\)-algebra \(\mathcal M\otimes\mathcal N\) and compute
\[
\int_X\left(\int_Y \mathbf 1_\Delta(x,y)\,d\nu(y)\right)d\mu(x),\qquad
\int_Y\left(\int_X \mathbf 1_\Delta(x,y)\,d\mu(x)\right)d\nu(y). \tag{1}
\]
Explain the relation to Tonelli’s Theorem on product integration.

**4.** State the Hahn Decomposition Theorem. Prove, if \(\rho\) is a signed measure on the measurable space \((X,\mathcal M)\), then there exist unique positive measures \(\rho_\pm\) on \(\mathcal M\) such that \(\rho_+\perp\rho_-\) and \(\rho=\rho_+-\rho_-\).

Assuming \(\mu\) is a positive measure on \(\mathcal M\) and \(f\in L^1(\mu)\) is real-valued, identify \(\rho_\pm\) for the signed measure
\[
\rho(E)=\int_E f\,d\mu.
\]

## Part B

**5.** State the Baire Category Theorem. Suppose \(X\) is a Banach space. Prove that, as a vector space, \(X\) does not have a countable basis. (Here countable means equinumerous with \(\mathbb N\).)

**6.** Let \((\varphi_n)\) be a sequence from \(L^1(\mathbb R)\) with the following properties:

Show, if \(f\in L^1(\mathbb R)\), then \(\varphi_n\star f\) converges to \(f\) in \(L^1(\mathbb R)\).
* (i) \(\varphi_n\geq 0\) for all \(n\),
* (ii) \(\displaystyle \int\varphi_n\,dx=1\) for all \(n\);
* (iii) for each \(\delta>0\), \(\displaystyle \lim_{n\to\infty}\int_{|x|>\delta}\varphi_n\,dx=0\).

**7.** Let \(X\) be a Banach space, \(Y\subset X\) a closed subspace. Say \(Y\) is complemented in \(X\) if there exists a closed subspace \(Z\subset X\) such that \(Y\cap Z=\{0\}\) and \(Y+Z=X\).

Prove that if \(Y\) is complemented in \(X\), then there exists a bounded linear operator \(T:X\to Y\) such that \(T(y)=y\) for all \(y\in Y\).

**8.** Let \(S:\ell^2(\mathbb N)\to\ell^2(\mathbb N)\) denote the shift operator defined, for \(f=(f(n))_{n=0}^\infty\in\ell^2(\mathbb N)\), by
\[
Sf(n)=
\begin{cases}
f(n-1),&n\geq 1;\\
0,&n=0.
\end{cases}
\]
Show \(S\) is an isometry (and in particular is bounded) and find \(S^*\) and \(SS^*\). Is \(S\) unitary?
