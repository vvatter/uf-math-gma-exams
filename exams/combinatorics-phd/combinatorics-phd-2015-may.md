# Combinatorics, PhD exam, May 2015

**1.** Let \(f(n)\) be the number of simple undirected graphs on vertex set \([n]\) in which each vertex has degree at most two. Find the exponential generating function of the sequence \(f(n)\). You can assume that \(f(0)=1\).

**2.** We partition a group of \(n\) people into blocks \(A\), \(B\), and \(C\), and ask each block to form a line. We also require that \(A\) have an odd number of people, and that \(B\) have an even number of people. Let \(h(n)\) be the number of ways to do this. Find the exponential generating function of the numbers \(h(n)\).

**3.** Let \(f(n)\) be the number of ways to choose a subset \(S\) of \([n]\), then to choose a permutation \(p\) on \([n]\) so that if \(s\in S\), then \(p(s)\notin S\). Find a formula for \(f(n)\).

**4.** This problem has two parts.
* (a) Find the number of permutations of length \(n\) whose first ascent occurs in position \(i\).
* (b) The number of all permutations of length \(n\) whose first ascent occurs in an even position is equal to the number of some other easily defined permutations that we studied this semester. What is that class of permutations, and why are the two numbers equal?

**5.** This Fall, the United States Congress will have \(n\) working days, split into an unspecified number of sessions. Within each session, one day will be designated for a plenary meeting, and each of the remaining days (if there are any remaining days) will be designated for either committee work or subcommittee work.

Find an explicit formula for the number of ways the US Congress can schedule its season.

**6.** Compute the order polynomial \(\Omega(n,P)\) of the 4-element poset \(P\) that consists of one maximum element and three minimal elements.

(Recall that \(\Omega(n,P)\) is the number of order-preserving maps from \(P\) to \([n]\). That is, the number of maps \(f:P\to[n]\) so that if \(x\le_P y\), then \(f(x)\le f(y)\).)

**7.** Prove the Sylvester–Gallai Theorem: In any configuration of \(n\) points in the plane, not all on a line, there is a line which contains exactly two of the points.

**8.** Prove Pick’s Theorem: The area of any (not necessarily convex) polygon \(P\) in the plane with vertices on the integer lattice is given by
\[
A(P)=n_{int}+\frac{1}{2}n_{bd}-1,
\]
where \(n_{int}\) and \(n_{bd}\) are the numbers of lattice points in the interior and on the boundary, respectively, of \(P\).

(You can assume without proof that \(P\) has a triangulation using all \(n_{int}\) lattice points in the interior and all \(n_{bd}\) lattice points on the boundary.)
