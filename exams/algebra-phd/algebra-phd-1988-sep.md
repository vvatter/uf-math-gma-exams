# Algebra, PhD exam, September 1988

*Do seven problems, at least two from each section.*

## I. Group Theory.

**1.** Let \(G\) be the group of all \(3\times 3\) non-singular matrices of determinant \(1\) with coefficients in the field of \(3\) elements.
* (a) Find \(|G|\).
* (b) Find a Sylow \(3\)-subgroup of \(G\).
* (c) Compute \(|\operatorname{Syl}_3(G)|\), where \(\operatorname{Syl}_3(G)\) is the set of all Sylow \(3\)-subgroups of \(G\).

**2.** Let \(G\) be a finite group acting transitively on a set \(X\), \(x\in X\), and \(P\) be a Sylow \(p\)-subgroup of \(G_x\) for some prime \(p\). Consider the set \(\operatorname{Fix}(P)=\{y\in X\mid y^P=y\}\), the set of fixed points of \(P\).
* (a) Prove that \(N_G(P)\) acts on \(\operatorname{Fix}(P)\), i.e., maps \(\operatorname{Fix}(P)\) to \(\operatorname{Fix}(P)\).
* (b) Prove that \(N_G(P)\) acts transitively on \(\operatorname{Fix}(P)\).

**3.** Two permutation representations \(G\xrightarrow{\pi_i}\Sigma(X_i)\), (the symmetric group on \(X_i\) are equivalent if there exists \(\alpha:X_1\to X_2\) such that for all \(g\in G\), \(x\in X_1\), we have \(x(g\pi_1)\alpha=(x\alpha)(g\pi_2)\). Prove that the following two permutation representations of \(S_4\) of degree \(12\) are not equivalent:
* (a) on the right coset space of \(\langle(12)\rangle\).
* (b) on the right coset space of \(\langle(12)(34)\rangle\).

**4.** Let \(G\) be a finite group and \(A\leq \operatorname{Aut}(G)\) such that \(G=[G,A]\). Suppose \(N\leq G\) satisfying \([N,A]=1\). Use the 3-subgroup lemma to prove \(N\leq Z(G)\), the center of \(G\). (Recall the 3-subgroups lemma: For three subgroups \(X,Y,Z\) of a group \(M\), if \([X,Y,Z]=1\) and \([Y,Z,X]=1\), then \([Z,X,Y]=1\).)

## II. Homological algebra.

**1.** Let \(R\) be a ring and consider the following commutative diagram of \(R\)-modules and \(R\)-module homomorphisms such that each row is a short exact sequence. Prove that if \(\alpha\) and \(\gamma\) are isomorphisms then \(\beta\) is also an isomorphism.

**2.** Prove the \(\mathbb Z\)-module isomorphisms, where \(c=(m,n)\) is the greatest common divisor.
* (a) \(\mathbb Z/m\mathbb Z\otimes\mathbb Z/n\mathbb Z=\mathbb Z/c\mathbb Z\).
* (b) \(\operatorname{Hom}(\mathbb Z/m\mathbb Z,\mathbb Z/n\mathbb Z)=\mathbb Z/c\mathbb Z\).

**3.** A module \(P\) over a ring \(R\) is said to be projective if, given any diagram of \(R\)-module homomorphisms with \(g\) surjective, there exists an \(R\)-module homomorphism \(h:P\longrightarrow A\) such that the following diagram is commutative. Prove that the following conditions on a ring \(R\) with identity are equivalent:
* (a) Every \(R\)-module is projective.
* (b) Every short exact sequence of \(R\)-modules splits.

## III. Commutative algebra.

**1.** A non-empty subset \(S\) of a ring \(R\) with identity is called multiplicative if \(ab\in S\) whenever \(a,b\in S\).
* (a) If \(I\) is a proper ideal of \(R\) disjoint from \(S\), then prove that there exists an ideal \(P\) maximal with respect to containing \(I\) and being disjoint from \(S\). Furthermore, show that \(P\) is a prime ideal.
* (b) If \(P\) is a prime ideal of ring \(R\), define the localization of \(R\) at \(P\) and prove that the localization has a unique maximal ideal.

**2.** Find a reduced primary decomposition for the following ideals. Also give the prime ideals to which the primary ideals belong.
* (a) \((24)\) as an ideal in \(\mathbb Z\).
* (b) \((2x,x^2)\) as an ideal in \(\mathbb Z[x]\).
* (c) What theorems allow us to conclude that every ideal in \(\mathbb Z[x]\) has a primary decomposition.

**3.** Let \(R\) be a unique factorization domain and \(K\) its field of fractions.
* (a) Show that if \(a\in K\) is integral over \(R\), then \(a\in R\). (In other words, \(R\) is integrally closed.)
* (b) True or false: If \(S\) is a subring of \(K\) containing \(R\), then \(S\) is also a unique factorization domain. If true, prove your answer. If false give examples of \(R\), \(K\), and \(S\) that show it not to be true.

**4.** Determine, up to isomorphism, all semisimple rings of order \(1008=2^5\cdot 3^2\cdot 7\).
