# Topology, PhD exam, August 2020

*Work the following problems and show all work. Support all statements to the best of your ability. Answer problems 6–15 with complete definitions, statements, or short proofs.*

**1.** Let \(X\) be a topological space. Given two points \(a,b\in X\), a collection of sets \(A_1,\ldots,A_n\) is a simple chain from \(a\) to \(b\) if \(a\in A_1\), \(b\in A_n\), and \(A_i\cap A_j\ne\varnothing\) if and only if \(|i-j|\le 1\). Prove that if \(\{U_\alpha\}\) is a collection of open sets covering \(X\) and \(X\) is connected, then there is a simple chain of elements in \(\{U_\alpha\}\) joining any pair of points \(a,b\in X\). (Hint: Consider the set \(C_a\) of all \(b\) so that there is a simple chain of elements joining \(a\) and \(b\). Show that \(C_a\) is both open and closed.)

**2.** Let \(X=S^2\cup_f e^3\cup_h e^5\), where \(f:S^2\to S^2\) has degree \(n\) and \(h:S^4\to S^2\cup_f e^3\) is continuous.
* (a) What is the Euler characteristic of \(X\)?
* (b) Determine \(H_\bullet(X;\mathbb{Z})\) and \(H^\bullet(X;\mathbb{Z}_2)\) as a function of \(n\).
* (c) Can \(X\) have the homotopy type of a closed 5-manifold? (If the answer depends on \(n\), explain.)

**3.** Let \(X\) be the space \(\mathbb{R}P^3/\mathbb{R}P^1\) (the space obtained by collapsing \(\mathbb{R}P^1\subset\mathbb{R}P^3\) to a point). Compute the integral homology groups of \(X\).

**4.** Let \(\mathbb{R}P^2\) be the real projective plane and fix a basepoint \(x_0\in\mathbb{R}P^2\). Note that we can realize the wedge sum \(\mathbb{R}P^2\vee\mathbb{R}P^2\) as \((\mathbb{R}P^2\times\{x_0\})\cup(\{x_0\}\times\mathbb{R}P^2)\subset\mathbb{R}P^2\times\mathbb{R}P^2\).
* (a) Compute the fundamental groups of \(\mathbb{R}P^2\vee\mathbb{R}P^2\) and \(\mathbb{R}P^2\times\mathbb{R}P^2\).
* (b) Show that \(\mathbb{R}P^2\vee\mathbb{R}P^2\) is not a retract of \(\mathbb{R}P^2\times\mathbb{R}P^2\).
* (c) Show that any map \(f:\mathbb{R}P^2\vee\mathbb{R}P^2\to S^1\) is null-homotopic.

**5.** Compute \(H_\bullet(M;\mathbb{Z}_2)\), where \(M\) is the space with integral homology groups
\[
H_k(M;\mathbb{Z})=
\begin{cases}
\mathbb{Z} & k=0,2,4,\\
\mathbb{Z}_2 & k=1,\\
\mathbb{Z}_3 & k=3,\\
0 & \text{otherwise.}
\end{cases}
\]

**6.** Let \(M\) be an orientable simply-connected 3-manifold. Compute the integral homology of \(M\).

**7.** Compute \(\chi(\mathbb{R}P^2\times\mathbb{C}P^4\times S^4)\).

**8.** Give an example of a space that is connected but not locally connected.

**9.** State the Urysohn Lemma.

**10.** Prove that if \(m\ne n\), then \(\mathbb{R}^m\) is not homeomorphic to \(\mathbb{R}^n\).

**11.** Let \(\mathbb{N}\) be the set of natural numbers and let \(\mathbb{N}^*\) be its one-point compactification. Let \(X\) be any topological space. Prove that a sequence \(\{a_n\}\) in \(X\) converges to \(a\) if and only if the map \(f:\mathbb{N}^*\to X\) defined by \(f(n)=a_n\) and \(f(\infty)=a\) is continuous. (Here \(\mathbb{N}\) has the discrete topology.)

**12.** State the Borsuk–Ulam Theorem.

**13.** Describe the possible connected covering spaces of \(S^1\times S^1\).

**14.** Does the following exact sequence of abelian groups necessarily split? Prove or give a counterexample.
\[
0\to\mathbb{Z}\to\mathbb{Z}\oplus\mathbb{Z}\to A\to 0
\]

**15.** Compute the integral homology of the space \(\mathbb{C}P^2\times\mathbb{R}P^3\).
