# Combinatorics, PhD exam, May 2018

**1.** Consider the set \(T_n\) of (not rooted) trees with \(n \ge 3\) labeled leaves for which each interior (non-leaf) vertex has degree 3.
* (a) Prove that each tree in \(T_n\) has exactly \(2n-3\) edges.
* (b) Prove that the number of trees in \(T_n\) is \((2n-5)!!=1\cdot 3\cdot 5\cdot 7\cdots(2n-7)\cdot(2n-5)\).

**2.** The famous Dilworth Theorem for a finite poset \(P\) states that the minimum number of chains in any partition of \(P\) into chains is equal to the maximum number of elements in an antichain of \(P\).
* (a) Prove that if \(P\) has size at least \(rs+1\), then there is either a chain of size \(r\) or an antichain of size \(s\).
* (b) There are many proofs of the following Erdős–Szekeres theorem: For any sequence \(a_1,a_2,\ldots,a_{n^2+1}\) of integers, there is a subsequence of length \(n+1\) that is monotone. Prove the Erdős–Szekeres theorem using Dilworth’s theorem, i.e., part (a).

**3.** Prove that
\[
\sum_{i=0}^{n}(-1)^i\binom{n}{i}i^k=
\begin{cases}
0 & \text{if }0\le k<n,\\
(-1)^n n! & \text{if }k=n.
\end{cases}
\]
What is the sum if \(k>n\)?

Hint: Count surjective mappings from \([k]\) to \([n]\).

**4.** Recall: The girth of a graph is the length of the shortest cycle (and \(\infty\) if the graph has no cycles).
* (a) Prove that a planar graph of girth (minimum cycle length) at least 6 has a vertex of degree at most 2.
* (b) The Four Color Theorem states that any planar graph is 4-colorable. Grötzsch proved that any triangle-free planar graph is 3-colorable. Without using his result, prove that a planar graph of girth at least 6 is 3-colorable.

**5.** How many strings can be formed using the alphabet \(\{A,B,C,D,E\}\) if
* (a) the letter \(A\) occurs an odd number of times
* (b) the letters \(A\) and \(B\) are both used an odd number of times.

**6.** Let \(f(n)\) be the number of ways to tile a \(1\times n\) path with \(1\times 2\) tiles that are red, blue, or green, and \(1\times 1\) tiles that are yellow, orange, black, or white.
* (a) Find an explicit formula for \(f(n)\).
* (b) On average, how many \(1\times 1\) tiles will a \(1\times n\) path contain?

**7.** Choose a derangement \(p\) of length \(n\) uniformly at random. Recall that a derangement is a permutation with no 1-cycles. On average, how many 2-cycles does \(p\) contain?

**8.** Let \(C\) be a binary code of length \(n\) and minimum distance \(d\ge 2e+1\). Prove the following two bounds (the Hamming bound and Singleton bound).
\[
|C|\le \frac{2^n}{\displaystyle\sum_{i=0}^{e}\binom{n}{i}}
\]
\[
|C|\le 2^{n-d+1}
\]
