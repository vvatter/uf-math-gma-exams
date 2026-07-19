# Analysis PhD exam, January 2023

*Write solutions in a neat and logical fashion, giving complete reasons for all steps. Attempt SIX problems.*

**1.** For any two of the following, either give an example or explain why no example exists.
* a) a sequence of Lebesgue measurable functions on \(\mathbb{R}\) which converges in measure but not Lebesgue a.e.
* b) a closed set \(E \subset [0,1]\) with positive Lebesgue measure, but which contains no open intervals
* c) a decreasing sequence of nonnegative measurable functions on \(\mathbb{R}\) such that \(\lim \int f_n \ne \int \lim f_n\)

**2.** Prove that for any positive measure \(\mu\), the space \(L^1(\mu)\) is complete in the \(L^1\) norm.

**3.** Let \((\mu_n)\) be a sequence of finite signed measures on a measurable space \((X,\mathcal{M})\). Prove that there exists a finite, positive measure \(\nu\) on \((X,\mathcal{M})\) such that \(\mu_n \ll \nu\) for all \(n\).

**4.** Suppose that \(f \in L^1[0,1]\) and \(\int_0^x f\,dm=0\) for all \(x \in [0,1]\). What can you conclude about \(f\)? (Prove your claim.)

**5.** Let \(\mathcal{X}\) be a Banach space. Say that a sequence \((x_n) \subset \mathcal{X}\) converges weakly to \(x \in \mathcal{X}\) if \(f(x_n) \to f(x)\) for all \(f \in \mathcal{X}^*\). Prove the following:
* a) If \((x_n)\) converges weakly, then \(\sup_n \lVert x_n\rVert < \infty\).
* b) Weak limits are unique. (That is, if \(x_n \to x\) weakly and \(x_n \to y\) weakly, then \(x=y\).)

**6.** This problem has two parts.
* a) State the closed graph theorem.
* b) Let \(\mathcal{X}\) be a Banach space with closed subspaces \(\mathcal{Y},\mathcal{Z} \subset \mathcal{X}\). Suppose that every \(x \in \mathcal{X}\) admits a unique decomposition \(x=y+z\) with \(y \in \mathcal{Y}\), \(z \in \mathcal{Z}\). Prove that there is a constant \(C\) so that \(\lVert y\rVert \le C\lVert x\rVert\) and \(\lVert z\rVert \le C\lVert x\rVert\).

**7.** Let \(H\) be a Hilbert space and \(T:H \to H\) a bounded linear operator. Define the adjoint operator \(T^*:H \to H\) and prove that it is bounded, with \(\lVert T^*\rVert=\lVert T\rVert\).

**8.** (Short answer, you do not need to give a detailed proof, just a brief explanation.)
* a) Define the Fourier transform on \(L^1(\mathbb{R})\) and sketch its extension to \(L^2(\mathbb{R})\).
* b) Sketch a construction of a bounded linear functional \(\lambda\) on \(L^\infty(\mathbb{R})\) which is not of the form \(\lambda(f)=\int f(x)g(x)\,dx\) for any \(L^1\) function \(g\).
* c) Sketch a proof of the fact that there is no norm under which \(c_{00}\) is complete.
