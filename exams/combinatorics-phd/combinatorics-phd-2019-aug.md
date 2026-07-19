# Combinatorics, PhD exam, August 2019

**1.** List the infinite families of symmetries of the standard square tiling of the plane. (No two families should have more than the identity in common.)

**2.** Let \((v,b,r,k,\lambda)\) denote the number, respectively, of points, blocks, blocks containing a given point, points in each block, and blocks containing two distinct points of a balanced incomplete block design. Prove that
\[
bk=vr
\]
and
\[
\lambda(v-1)=r(k-1).
\]

**3.** Let \(h_n\) be the number of all words over the alphabet \(\{A,B,C\}\) that are of length \(n\) and in which a letter \(A\) is never immediately followed by a letter \(B\). Set \(h_0=1\). Find a closed form for the ordinary generating function
\[
H(z)=\sum_{n\ge 0}h_nz^n.
\]

**4.** Let \(\ell_n\) be the total number of leaves in all unlabeled plane binary trees on \(n\) vertices. (These trees are rooted, and each vertex has at most two children, and every child is either a left child or a right child, even if it is an only child.) Note that \(\ell_1=1\), \(\ell_2=2\), and \(\ell_3=6\).
* (a) Find the generating function
  \[
  L(z)=\sum_{n\ge 1}\ell_nz^n
  \]
  in closed form.
* (b) Find an explicit formula for the numbers \(\ell_n\).

**5.** Let \(t_n\) be the number of ways to choose a permutation of length \(n\), and then to color a subset (not necessarily proper) of its even cycles red. Find a closed formula for the exponential generating function of the numbers \(t_n\).

**6.** Recall that for a prime power \(q\), the Gaussian or \(q\)-binomial coefficient \(\left[\begin{smallmatrix}n\\k\end{smallmatrix}\right]_q\) is defined to be the number of \(k\) dimensional subspaces of an \(n\)-dimensional vector space over \(\mathrm{GF}(q)\). Equivalently, we can think of \(\left[\begin{smallmatrix}n\\k\end{smallmatrix}\right]_q\) as counting \(k\times n\) matrices over \(\mathrm{GF}(q)\) which are in reduced row echelon form and have no all-zero rows. Using either of these interpretations, prove that
\[
\left[\begin{smallmatrix}n\\k\end{smallmatrix}\right]_q
=
\left[\begin{smallmatrix}n-1\\k\end{smallmatrix}\right]_q
+q^{n-k}\left[\begin{smallmatrix}n-1\\k-1\end{smallmatrix}\right]_q
\]
for all \(n,k\ge 1\).

**7.** Recall that \(R(k,\ell)\) is the minimum integer \(n\) such that every graph on \(n\) vertices contains either a clique (complete subgraph) on \(k\) vertices or an independent set on \(\ell\) vertices. Prove that \(R(k,\ell)\) is finite for all \(k\) and \(\ell\).

**8.** Prove that \(R(k,k)>2^{k/2}\) for all \(k\). Hint: Consider a random graph.
