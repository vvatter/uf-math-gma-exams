# Ergodic Theory, PhD exam, May 2025

*Answer 4 problems total, and at least one problem from each category: General ergodic Theory (problems 1–3), Ergodicity and Mixing Properties (problems 4–6), and Topological Dynamics (problems 7–8).*

**1.** Equip the circle \(\mathbb{R}/\mathbb{Z}\) with the usual Lebesgue measure. Let \(\alpha\in\mathbb{R}\) be irrational and let \(T:\mathbb{R}/\mathbb{Z}\to\mathbb{R}/\mathbb{Z}\) be rotation by \(\alpha\), i.e., \(T(x)=x+\alpha\ (\mathrm{mod}\ \mathbb{Z})\). Prove that \(T\) is ergodic.

**2.** Let \(T:X\to X\) be an invertible measure preserving transformation on a probability space \((X,\mathcal{B},\mu)\). State and prove the Poincaré recurrence theorem for \(T\).

**3.** Let \(\Gamma\) be a countable group acting by measure preserving transformations on standard probability spaces \((X,\mathcal{B}_X,\mu)\), \((Y,\mathcal{B}_Y,\nu)\), and \((Z,\mathcal{B}_Z,\eta)\). Suppose that \(\pi_Y:X\to Y\) and \(\pi_Z:X\to Z\) are measure preserving \(\Gamma\)-equivariant maps from \(X\) to \(Y\) and \(Z\), respectively. Under the following assumptions, prove that the pushforward of \(\mu\) under the map \(\pi_Y\times\pi_Z:X\to Y\times Z\), \(x\mapsto(\pi_Y(x),\pi_Z(x))\), is exactly the product measure \(\nu\times\eta\).
* (a) The action of \(\Gamma\) on \((Y,\mathcal{B}_Y,\nu)\) is ergodic.
* (b) The action of \(\Gamma\) on \((Z,\mathcal{B}_Z,\eta)\) is the identity action on \(Z\), i.e., every element of \(\Gamma\) fixes every point of \(Z\).

**4.** Let \(\Gamma\) be a countable group acting by measure preserving transformations on a standard probability space \((X,\mathcal{B},\mu)\). Define what it means for the action to be weakly mixing, and define what it means for the action to be compact (for both properties there are many equivalent definitions, you just need to provide one definition for each). Prove that if the action is both weakly mixing and compact then \(\mu\) is a point mass.

**5.** Let \(T:X\to X\) be an invertible measure preserving transformation on a standard probability space \((X,\mathcal{B},\mu)\). Define what it means for \(T\) to be mixing. Give an example of a nontrivial mixing transformation, and prove that it is mixing.

**6.** Let \(T:X\to X\) be an invertible measure preserving transformation on a probability space \((X,\mathcal{B},\mu)\), and let \(h:X\to\mathbb{C}\) be a function in \(L^2(X,\mathcal{B},\mu)\). Prove that the sequence \(\frac{1}{n}\sum_{i=0}^{n-1}h\circ T^i\) converges in \(L^2(X,\mathcal{B},\mu)\) to \(P_T(h)\), where \(P_T\) denotes the orthogonal projection onto the subspace of \(T\)-invariant functions.

**7.** Let \(X\) be a compact Hausdorff space, and let \(G\) be a (discrete) group acting by homeomorphisms on \(X\). Define what it means for the action to be topologically transitive. Prove that if \(X\) is metrizable then the action of \(G\) on \(X\) is topologically transitive if and only if there exists a point in \(X\) whose \(G\)-orbit is dense.

**8.** Let \(X\) be a compact Hausdorff space, and let \(G\) be a (discrete) group acting by homeomorphisms on \(X\). Let \(x_0\in X\) and assume that the \(G\)-orbit of \(x_0\) is dense in \(X\). Prove that the action of \(G\) on \(X\) is minimal if and only if for every open neighborhood \(U\) of \(x_0\), the set \(A_{U,x_0}=\{g\in G:g\cdot x_0\in U\}\) is syndetic in \(G\). [A subset \(A\) of \(G\) is called syndetic in \(G\) if there is a finite subset \(F\) of \(G\) with \(FA=G\).]
