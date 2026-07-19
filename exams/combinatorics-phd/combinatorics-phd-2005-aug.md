# Combinatorics, PhD exam, August 2005

*Show your work.*

**1.** This problem has two parts.
* a. There are \(r\) black and \(n-r\) white balls in an urn. They are removed one at a time without replacement. What is the probability that exactly \(k\) drawings are required to get a white ball?
* b. Use your result to conclude that
  \[
  \sum_{k=1}^{r}\frac{(r)_k}{(n-1)_k}=\frac{r}{n-r}.
  \]

**2.** Each of \(n\) people is to be mailed an envelope containing a letter and a bill. How many ways \(Q_n\) are there of placing the \(n\) letters and \(n\) bills into \(n\) addressed envelopes so that no envelope contains both the correct letter and bill?

**3.** Let \(P_n\) be the total number of \(k\)-permutations of \(n\) for various \(k\), that is,
\[
P_n=\sum_{k=0}^{n}(n)_k,\qquad n=0,1,\ldots
\]
Show that
\[
P(t)=\sum_{n=0}^{\infty}P_n\frac{t^n}{n!}=(1-t)^{-1}e^t
\]
and use this to show that
\[
P_n=nP_{n-1}+1,\qquad n=1,2,\ldots,\quad P_0=1.
\]

**4.** Define the binary Hamming code \(H(r)\) of length \(2^r-1\). Show that \(H(r)\) is an exactly single error correcting code and that \(H(r)\) is a perfect code. Determine the number of codewords of weight 3 in \(H(r)\).

**5.** Show that the number of partitions of a number \(n\) into exactly \(m\) parts is equal to the number of partitions of \(n-m\) into no more than \(m\) parts.

**6.** An order on the set of ordered pairs of non-negative integers is defined by \((a_1,a_2)\leq(b_1,b_2)\) if \(a_i\leq b_i\) for \(i=1,2\). Find the Möbius function of this poset.

**7.** Determine for which values of \(m\) and \(n\) the complete bipartite graph \(K_{mn}\) is. Answer the same three questions for the \(n\)-cube. (Recall that the n-cube \(Q_n\) is defined as the graph whose vertices are the set of all binary sequences of length \(n\), where two vertices are adjacent if the corresponding sequences differ by exactly one digit.)
* (a) planar
* (b) Eulerian
* (c) Hamiltonian.

**8.** Let \(G\) be a triangle-free graph with \(n\) vertices, minimum degree \(k\) and girth \(g\). Prove that \(g\leq 2n/k\).

Hint: For an appropriate cycle \(C\) count the number of edges from \(C\) to \(G\mathbin{\backslash}C\) in two ways.
