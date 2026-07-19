# Combinatorics PhD exam, May 2010

**1.** This problem has two parts.
* (a) Prove that
  \[
  \sum_{i=0}^{n} \binom{i}{k}=\binom{n+1}{k+1}.
  \]
* (b) Prove that the number of solutions of \(x_1+\cdots+x_k\leq n\) in positive integers is \(\binom{n}{k}\).

**2.** This problem has two parts.
* (a) Prove that the number of Hamiltonian cycles in the complete bipartite graph \(K_{n,n}\) is \(\frac{1}{2}(n-1)!n!\).
* (b) Let \(e\) be an edge of the complete graph \(K_n\). Use Cayley’s Theorem to find the number of spanning trees in \(K_n-e\).

**3.** Recall that the average degree of a graph \(G\) of order \(n\) is
\[
av(G)=\frac{\sum_{v\in V}\deg(v)}{n}.
\]
* (a) Prove that
  \[
  \chi(G)\leq 1+\Delta(G),
  \]
  where \(\chi\) denotes the chromatic number and \(\Delta\) the maximum degree.
* (b) For an arbitrary graph \(G\), prove or give a counterexample to the statement
  \[
  \chi(G)\leq 1+av(G).
  \]

**4.** Let \(C\) be a binary code and let \(\overline{C}\) be the code obtained from \(C\) by adding an even parity check. Find the minimum distance \(d(\overline{C})\) in terms of \(d(C)\).

**5.** Prove that balanced incomplete block designs with the following parameters do not exist:
\[
(12,8,6,4,3),\qquad (22,22,7,7,2).
\]

**6.** Find the unique sequence \(\{a_n\}\) with
\[
\sum_{k=0}^{n} a_k a_{n-k}=1.
\]

**7.** Use inclusion-exclusion to find a formula for the number of surjective functions \(f:X\to Y\) with \(|X|=n\) and \(|Y|=m\).

**8.** Let \(f(n,k)\) be the number of \(k\)-subsets of \(\{1,2,\ldots,n\}\) that do not contain a pair of consecutive integers.
* (a) Find a recurrence for \(f(n,k)\) by considering the \(k\)-subsets that do, and do not, contain \(1\).
* (b) Use part (a) to show that \(f(n,k)=\binom{n-k+1}{k}\).
