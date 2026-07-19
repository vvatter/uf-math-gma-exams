# Combinatorics, PhD exam, January 2019

**1.** Let \(a_n\) be the total number of leaves in all rooted non-plane trees with vertices bijectively labeled with elements of \(\{1,2,\cdots n\}\), so \(a_1=1\), \(a_2=2\), and \(a_3=12\). Find an explicit formula for \(a_n\).

**2.** Let \(G\) be a simple graph with the property that if the vertices \(u\) and \(v\) have the same degree, then there is no vertex adjacent to both \(u\) and \(v\). Prove that \(G\) contains a vertex of degree one.

**3.** Let \(h_n\) be the number of ways to color each of \(n\) distinct objects red, blue, or green, so that the number of red objects is even and the number of blue objects is odd. Find the exponential generating function for the sequence \(h_n\), then deduce an explicit formula for the numbers \(h_n\).

**4.** Let \(G\) be a connected, regular, simple graph. If \(G\) has \(22\) edges, how many vertices can \(G\) have? Note: for full credit, give a complete list of all possibilities, and make sure that every possibility on the list is indeed possible.

**5.** Choose a permutation \(p\) of length \(n\) uniformly at random. Let \(a_n\) be the probability that \(p\) has no fixed points and no cycles of length three. Compute \(\lim_{n\to\infty} a_n\).

**6.** Recall that the permanent of the \(n\times n\) matrix \(M\) is
\[
\operatorname{per}(M)=\sum_{\pi\in S_n}\prod_{i=1}^n M_{i,\pi(i)}
\]
and that a matrix is doubly stochastic if all of its entries are between \(0\) and \(1\), and each row sum and column sum equals \(1\).

Van der Waerden’s Conjecture (now a theorem) states that the permanent of an \(n\times n\) doubly stochastic matrix is at least \(n!/n^n\).

Show how van der Waerden’s Conjecture implies that the number of derangements of length \(n\) is at least \(n!\left(1-\frac{1}{n}\right)^n\).

**7.** Let \(G\) be a connected plane graph where all faces have an even number of edges. Prove that \(G\) is bipartite.

**8.** Recall that the Gaussian coefficients (or \(q\)-binomial coefficients) are defined by
\[
\begin{bmatrix}n\\k\end{bmatrix}_q=\frac{(q^n-1)(q^{n-1}-1)\cdots(q^{n-k+1}-1)}{(q^k-1)(q^{k-1}-1)\cdots(q-1)}.
\]
Prove that if \(q\) is a prime power then \(\begin{bmatrix}n\\k\end{bmatrix}_q\) counts the number of \(k\)-dimensional subspaces of an \(n\)-dimensional vector space over \(\operatorname{GF}(q)\).
