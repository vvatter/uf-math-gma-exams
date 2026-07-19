# Combinatorics, PhD exam, August 2017

**1.** Let \(a_n\) denote the number of strings of length \(n\) of the letters A, B, C, and D such that the letter A appears an odd number of times.
* (a) Find a closed formula for \(a_n\).
* (b) Find the exponential generating function for the sequence \(\{a_n\}\). (using no summation signs)

**2.** The set \([n] \times [n]\) is partially ordered by the relation \((a,b) \preceq (c,d)\) which holds when \(a \leq c\) and \(b \leq d\). Find, with proof, the length of a maximum chain and the length of a maximum antichain.

What is the size of a minimum chain decomposition of this poset. (Recall that a chain decomposition of a poset is a partition of its elements into disjoint chains.)

**3.** This problem has two parts.
* (a) Prove that, for a simple graph \(G\) with at least 5 vertices, at least one of \(G\) or its complement has a cycle.
* (b) Suppose that you color the edges of \(K_n\) using 2 colors. Show that there exists a monochromatic spanning tree.

**4.** A parity check matrix \(H\) of a binary linear code \(C\) can be defined as a generator matrix of the dual code \(C^\perp\).

Show that \(C\) is the null space of the transpose \(H^T\), where multiplication by \(H^T\) is on the right, i.e., \(cH^T\).

Show that the minimum distance of the code equals the cardinality of a minimum dependent set of columns of \(H\).

If a generator matrix of a binary linear code \(C\) is
\[
\begin{pmatrix}
1 & 0 & 1 & 0 & 1\\
0 & 1 & 1 & 1 & 0
\end{pmatrix},
\]
then show that \((c_1,c_2,c_3,c_4,c_5)\) is a codeword if and only if (modulo 2)
\[
\begin{aligned}
c_1+c_2+c_3&=0\\
c_2+c_4&=0\\
c_1+c_5&=0.
\end{aligned}
\]
What is the minimum distance of this code?

**5.** Let \(g(n)\) be the number of permutations of length \(n\) in which each cycle is of even length. Find the exponential generating function of the sequence \(g(n)\), where \(n=0,1,2,\ldots\).

**6.** Let \(t_n\) be the total number of cycles of all permutations of length \(n\). So \(t_1=1\), \(t_2=3\), and \(t_3=11\). Find an explicit formula for the numbers \(t_n\). Your answer can contain one summation sign.

**7.** Prove that the language \(\{a^{n^2}:n\in\mathbb{N}\}\) is not regular.

**8.** Let \(\beta\) be a permutation of length \(k\). Prove that there are precisely \(k^2+1\) permutations of length \(k+1\) containing \(\beta\).
