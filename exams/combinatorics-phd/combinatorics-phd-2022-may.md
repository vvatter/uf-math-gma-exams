# Combinatorics, PhD exam, May 2022

**1.** Let \(G_n\) be the graph whose vertex set is the set of all permutations of \([n]\) (in one line notation), with two vertices adjacent if they differ by switching two consecutive entries in the permutation. What is the chromatic number of \(G_n\) (with proof).

**2.** Let \(T=(V,E)\) be a tournament that is not strongly connected. Show there is a partition \(V=A\sqcup B\) with \(A,B\) non-empty so that every edge between \(a\in A\) and \(b\in B\) is from \(a\) to \(b\).

**3.** Recall the permutation \(\pi=\pi_1\cdots\pi_n\) contains the permutation \(\sigma=\sigma_1\cdots\sigma_k\) if there is a subset \(\{i_1<\cdots<i_k\}\subseteq[n]\) so that \(\pi_{i_1}\cdots\pi_{i_k}\) has the same relative order as \(\sigma\), and that \(\pi\) avoids \(\sigma\) if it does not contain \(\sigma\). Let \(S_n(\sigma)\) be the set of permutations avoiding \(\sigma\). Prove that \(\lvert S_n(231)\rvert\) is the \(n\)th Catalan number \(C_n=\binom{2n}{n}/(n+1)\).

**4.** Determine the number of binary strings of length \(n\) beginning with \(0\), ending with \(1\), and such that the number of copies of \(00\) equals the number of copies of \(11\). For example, \(00011011\) has two copies of each.

**5.** Show that the number of partitions of \(n\) with no part divisible by \(k\) is equal to the number of partitions of \(n\) with each part appearing at most \(k-1\) times.

**6.** Let \(P\) be a finite poset with unique minimal element \(0\) and Möbius function \(\mu\). Let \(y\in P\) so that there is only one \(x\) covered by \(y\). Show \(\mu(0,y)=0\).

**7.** Let \(e_k(x_1,\ldots,x_n)\) be the elementary symmetric function in \(n\) variables and \(c(n,k)\) be the (signless) Stirling number of the first kind. Prove that
\[
e_{n+1-k}(1,2,\ldots,n)=c(n+1,k).
\]
For example, \(e_2(1,2,3)=1\cdot2+1\cdot3+2\cdot3=11=c(4,2)\).

(Hint: what is \(e_k(x_1,\ldots,x_n)\) in terms of symmetric functions in \(n-1\) variables?)

**8.** Let \(D_n\) be the set of permutations of \(n\) with no fixed points and \(F_n\) be the set of permutations with exactly one fixed point. Show
\[
\lvert D_n\rvert-\lvert F_n\rvert=(-1)^n.
\]
