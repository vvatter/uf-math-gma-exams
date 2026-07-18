# Combinatorics, PhD exam, May 1991

*Do 9 out of 12 problems. Show all of your work.*

**1.** How many \(k\)-tuples \((A_1,A_2,\ldots,A_k)\) of nested subsets of an \(n\)-set are there, where \(A_1\subseteq A_2\subseteq\cdots\subseteq A_k\)?

**2.** How many words of length \(n\) are there in the alphabet \((a,b,c)\) with no two adjacent \(a\)’s? With no two adjacent letters equal?

**3.** Find the generating function for the sequence \(\{a_n\}\) given by the recurrence
\[
a_n=a_{n-1}+6a_{n-2}+2^n
\]
where \(a_0=1\) and \(a_1=3\).

**4.** Bipartite graphs:
* (a) Determine for which values of \(m\) and \(n\) the complete bipartite graph \(K_{mn}\) is
    * (1) planar;
    * (2) Eulerian;
    * (3) Hamiltonian.
* (b) Prove: A plane graph where every face has an even number of edges must be bipartite.

**5.** Prove that
\[
\sum_{k=1}^{n} S(n,k)x(x-1)\cdots(x-k+1)=x^n.
\]

**6.** Use Möbius inversion to find the number of integers between \(1\) and \(n\) and coprime to \(n\), given the prime factorization of \(n\).

**7.** Prove or disprove: There is a matching from \(V\) to \(W\) in a bipartite graph if, for some fixed \(k\), there are \(k\) or more edges incident with each vertex of \(V\) and \(k\) or fewer edges incident with each vertex of \(W\).

**8.** Let \(A_{m,n}\) be the collection of all sets \(X=\{N_1,N_2,\ldots,N_k\}\), where \(k\) is a non-negative integer, and for each \(i\leq k\), \(N_i\) is a positive integer divisor of \(N=2^m3^n\), and where \(N_i\mid N_j\) only if \(i=j\). Define a partial order on \(A_{m,n}\), where \(X=\{N_1,N_2,\ldots,N_k\}\), \(X'=\{N'_1,N'_2,\ldots,N'_l\}\), by \(X\preceq X'\) if and only if \(N_i\in X\Rightarrow\) there exists \(N'_j\in X'\) with \(N_i\mid N'_j\). Prove that \(A_{m,n}\) is a distributive lattice, and determine its poset of join-irreducible elements.

**9.** Let \(I\) be a collection of subsets of \(E\), where \(E\) is finite, and suppose that \(I\neq\varnothing\) and that \(Y\in I,\ X\subseteq Y\Rightarrow X\in I\). Let \(c:E\to\mathbb{R}^+\) assign a positive real number to each element of \(E\). Consider the optimization problem:

Find \(\max_{X\in I}\sum_{x\in X}c(x)\)

Prove that the greedy algorithm solves this problem if and only if \(I\) is the collection of independent sets of some matroid on \(E\).

**10.** State the MacWilliams identity, and use it to compute the weight polynomial of the \((15,11)\) Hamming binary code.

**11.** A \((v,k,\lambda)\)-design \(\Sigma\) is an incidence structure consisting of a set \(S\) of \(v\) points and a collection of \(k\)-subsets of \(S\) called blocks, such that every pair of points of \(S\) is contained in precisely \(\lambda\) blocks.

Prove that, in the range \(30\leq v\leq45\), a \((v,6,1)\)-design exists if and only if \(v=31\).

**12.** Use the Hall Multiplier Theorem
* (i) to prove the non-existence of a cyclic \((31,10,3)\) difference set.
* (ii) to find a cyclic \((31,6,1)\) difference set.
