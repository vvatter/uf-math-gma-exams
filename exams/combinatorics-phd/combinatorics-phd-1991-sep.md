# Combinatorics, PhD exam, September 1991

*Do 4 out of 5 problems.*

**1.** A \(k\)-arc of a projective plane \(\Pi\) is a set of \(k\) points, no three of which are collinear. Prove that every 4-arc in the plane \(PG(2,4)\) lies in exactly two 5-arcs.

**2.** Use (without proof) the assertion of problem #1 to prove that the 6-arcs of \(\Pi=PG(2,4)\) form a block design \(\Sigma\) on the point set of \(\Pi\), with \(v=21\) and \(k=6\). Compute \(\lambda\).

**3.** State the Hall Multiplier Theorem, and use it to find a \((91,10,1)\) difference set.

**4.** HC is the problem of deciding whether a graph has a Hamiltonian circuit or not, and this problem is known to be NP-complete. Use this fact to prove that HP is also NP-complete, where HP is the problem of deciding whether a graph has a Hamiltonian path (with unspecified initial and terminal vertices).

**5.** Let \(E\) be a finite set and \(P\) a partition of \(E\). Call a subset \(I\) of \(E\) independent (\(I\in\mathcal I\)) if no two elements of \(I\) are in the same block of \(P\).
* 1. Prove that \((E,\mathcal I)\) is a matroid (called a partition matroid).
* 2. For a bipartite graph \(B\) with edge set \(E\), let \(\mathcal M\subseteq 2^E\) denote the set of matchings on \(B\). Show that \((E,\mathcal M)\) is not a matroid.
* 3. Prove that \(\mathcal M\) is the intersection of two partition matroids. In other words there are partition matroids \((E,\mathcal I_1)\) and \((E,\mathcal I_2)\) such that \(\mathcal M=\mathcal I_1\cap\mathcal I_2\).

  Part 3 is significant because there is a general result that states that if \((E,\mathcal M)\) is such a matroid intersection then there is a polynomial algorithm to find a maximum cardinality independent set.
