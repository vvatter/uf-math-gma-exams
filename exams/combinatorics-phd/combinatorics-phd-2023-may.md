# Combinatorics PhD exam, May 2023

**1.** Let \(a_1,a_2,\ldots,a_{10}\) be positive integers not exceeding \(100\). Prove that there are disjoint, nonempty subsets \(S\) and \(T\) of \([10]\) so that
\[
\sum_{i\in S}a_i=\sum_{j\in T}a_j.
\]

**2.** Prove that the number of permutations of length \(n+1\) that have exactly two cycles is equal to the number of all cycles in all \(n!\) permutations of length \(n\). (For instance, if \(n=3\), then both of these numbers are equal to \(11\).)

**3.** Let \(P\) be a convex polyhedron whose faces are all either \(a\)-gons or \(b\)-gons, and whose vertices are each incident to three edges. Let \(p_a\), \(p_b\), and \(n\) respectively denote the number of \(a\)-gonal faces, \(b\)-gonal faces, and vertices of \(P\). Prove that \(p_a(6-a)+p_b(6-b)=12\).

**4.** A city has three high schools, each of them attended by \(n\) students. Each student knows exactly \(n+1\) students who attend a high school different from his. Prove that we can choose three students, one from each school, so that each of them knows the other two.

**5.** Let \(L_n\) be the total number of leaves in all binary plane trees with \(n\) vertices. These are trees in which all non-leaf vertices have one or two children, and every child is a left child or a right child, even if it is an only child. So \(L_1=1\), \(L_2=2\), and \(L_3=6\). Find an explicit formula for the numbers \(L_n\).

**6.** Let \(c:S\to\{0,1\}^*\) be a prefix-free code in which \(b_i\) codewords have length \(i\). Prove that \(\sum_i \frac{b_i}{2^i}\leq 1\).

**7.** Let \(T\) be a rooted non-plane \(2\)-tree (that is, every non-leaf vertex has two children) with \(n\) leaves. For instance, for \(n=4\), there are two such trees, one in which each leaf is at edge-distance two from the root, and one in which the edge-distances of the leaves from the root are \(1\), \(2\), \(3\), and \(3\). Let \(\operatorname{sym}(T)\) be the number of non-leaf vertices \(v\) of \(T\) such that the two children of \(v\) are the roots of identical subtrees. Your answers to parts (a) and (b) can contain \(\operatorname{sym}(T)\), but your answer to part (c) should not.
* (a) How many automorphisms does \(T\) have?
* (b) How many different ways are there to bijectively label the leaves of \(T\) with the numbers \(1,2,\ldots,n\)?
* (c) Find an explicit formula for \(\sum_T \frac{1}{|\operatorname{Aut}(T)|}\), where the sum is taken over all rooted non-plane \(2\)-trees with \(n\) leaves. For example, for \(n=4\), the two trees mentioned above have, respectively, eight and two automorphisms, so the requested sum is \(\frac18+\frac12=\frac58\).

**8.** Let \(k\) be a fixed positive integer, and let \(F_k(z)=\sum_{n\geq k}c(n,k)z^n/n!\), where \(c(n,k)\) is the signless Stirling number of the first kind.
* (a) Find \(F_k(z)\) in an explicit form.
* (b) Is \(F_k(z)\) an algebraic power series over \(\mathbb{C}\)?
* (c) Is \(F_k(z)\) a \(d\)-finite power series over \(\mathbb{C}\)?
