# Topology PhD exam, May 2023

*Work the following problems and show all your work. Support all statements to the best of your ability.*

**1.** Let \(X\) be a set. A filter base at \(x\in X\) is a nonempty collection \(\mathcal{U}_x\) of subsets of \(X\) containing \(x\) such that whenever \(U,V\in\mathcal{U}_x\) there exists \(W\in\mathcal{U}_x\) with \(W\subset U\cap V\). Assume that \(X\) has a filter base at each \(x\in X\) and that if \(U\in\mathcal{U}_x\) and \(y\in U\) then \(U\in\mathcal{U}_y\). Prove that \(\mathcal{B}=\bigcup_{x\in X}\mathcal{U}_x\) is a base for a topology.

**2.** Consider the torus \(T=S^1\times S^1\) with the following \(\Delta\)-complex structure.
* (a) Define a 2-chain that you can show is a cycle and which generates \(H_2(T)\). The resulting homology class is called a fundamental class of \(T\).
* (b) Define 1-cochains that you can show are cocycles and which generate \(H^1(T)\).
* (c) Compute a cup product which produces a cohomology class (Kronecker) dual to a fundamental class.

**3.** Show that the 2-sphere \(S^2\) is not a retract of the real projective plane \(\mathbb{RP}^2\), as well as that \(\mathbb{RP}^2\) is not a retract of \(S^2\).

**4.** Assume \(n>m\). Show that there are no maps from \(\mathbb{CP}^n\) to \(\mathbb{CP}^m\) that induces a nontrivial map \(H^2(\mathbb{CP}^m)\to H^2(\mathbb{CP}^n)\).

**5.** A map \(i:A\to X\) has the homotopy extension property (HEP) for the space \(Y\) if for each homotopy \(h:A\times I\to Y\) and each map \(f:X\to Y\) with \(f(i(a))=h(a,0)\) there exists a homotopy \(H:X\times I\to Y\) with \(H(x,0)=f(x)\) for all \(x\in X\) and \(H(i(a),t)=h(a,t)\) for all \(a\in A\) and all \(t\in I\). We call \(H\) an extension of \(h\) with initial condition \(f\). The map \(i:A\to X\) is a cofibration if it has the HEP for all spaces.

The mapping cylinder of \(i\), denoted \(Z(i)\), is the pushout of \(i:A\to X\) and the inclusion \(A\to A\times I\) given by \(a\mapsto(a,0)\).

Prove that the following three statements about \(i\) are equivalent:
* (a) \(i\) is a cofibration.
* (b) \(i\) has the HEP for the mapping cylinder \(Z(i)\).
* (c) \(Z(i)\) is a retract of \(X\times I\).

*Answer the following with complete definitions or statements or short proofs.*

**6.** Give the definition of a pushout and prove that if it exists then it is unique up to isomorphism.

**7.** The Klein bottle, \(K\), may be obtained by taking two Möbius bands, \(M\), and identifying their boundary, \(K=M\cup_{\partial M}M\). Apply the Seifert–van Kampen theorem to give a presentation of the fundamental group of \(K\).

**8.** Describe all of the two-fold coverings of \(S^1\vee S^1\).

**9.** Prove that for a finite CW-complex \(X\), \(H^1(X;\mathbb{Z})\) is torsion-free.

**10.** Compute the Euler characteristic of the manifold \(M=S^4\times\mathbb{RP}^2\times\mathbb{CP}^3\).

**11.** State the Baire Category Theorem.

**12.** Prove that for \(n\ne m\), \(\mathbb{R}^n\) is not homeomorphic to \(\mathbb{R}^m\).

**13.** Give an example of a space that is connected but not path connected.

**14.** State the Urysohn Lemma.

**15.** Is \(\mathbb{R}^{\omega}\) connected in the uniform topology?
