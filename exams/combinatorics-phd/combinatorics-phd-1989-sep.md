# Combinatorics, PhD exam, September 1989

*Do 7 out of 9 problems.*

**1.** Define the Ramsey number \(r(m,n)\) and prove that
\[
r(m,n) \leq \binom{m+n-2}{m-1}.
\]

**2.** The 12 edges of a cube are each colored one of two colors. Two such colored cubes are regarded as equivalent if one can be rotated so that it becomes identically colored to the other. Compute the number of equivalence classes of these colored cubes.

**3.** Let \(\Sigma\) be a block design with parameters \(b,v,r,k,\lambda\).
* (i) Prove that
  \[
  MM^T=
  \begin{pmatrix}
  r & \lambda & \cdots & \lambda\\
  \lambda & r & \cdots & \lambda\\
  \vdots & \vdots & \ddots & \vdots\\
  \lambda & \lambda & \cdots & r
  \end{pmatrix},
  \]
  where \(M^T\) is the transpose of \(M\), an incidence matrix for \(\Sigma\).
* (ii) Compute the determinant of \(MM^T\).
* (iii) Prove that \(b \geq v\).
* (iv) If \(b=v\) is an even integer, prove that \(k-\lambda\) is the square of an integer.

**4.** Give responses to any 4 out of the 5 parts. You may use the conclusions of (ii) and (iii) in responding to parts (iv) and (v) even if you omit their proofs.
* (i) State the Hall Multiplier Theorem for cyclic difference sets.
* (ii) Assume that \(D\) is a cyclic \((v,k,\lambda)\)-difference set with a multiplier \(m\) which satisfies \((v,m-1)=1\). Prove the existence of a cyclic \((v,k,\lambda)\)-difference set \(D'\) which is fixed by \(m\); i.e., which satisfies \(D'm=D'\).
* (iii) If there is a cyclic \((v,k,\lambda)\)-difference set \(D'\) fixed by a multiplier \(m\) and if \(v\) is a prime number, prove the existence of a cyclic \((v,k,\lambda)\)-difference set \(D''\) that satisfies \(1\in D''=D''m\).
* (iv) Prove that there is no cyclic \((67,12,2)\)-difference set.
* (v) Find a cyclic \((73,9,1)\)-difference set.

**5.** A \(t\)-\((v,k,\lambda)\) design \(\Sigma\) is an incidence structure consisting of a set \(S\) of \(v\) points and a collection of \(k\)-subsets of \(S\) called blocks such that every \(t\)-subset of \(S\) is contained in precisely \(\lambda\) blocks.
* (i) If \(t\geq 1\), prove that \(\Sigma\) is also a \((t-1)\)-\((v,k,\lambda')\) design with
  \[
  \lambda'=\frac{(v-t+1)\lambda}{k-t+1}.
  \]
* (ii) Let \(\Sigma\) be a \(4\)-\((23,7,1)\) design. Let \(\Sigma^*\) be the incidence structure defined on the point set of \(\Sigma\) by taking as blocks the complements of the blocks of \(\Sigma\). Prove that \(\Sigma^*\) is a \(4\)-\((23,16,\lambda^*)\) design, and give the value of \(\lambda^*\).

  Hints: For \(0\leq s\leq 3\), \(\Sigma\) is an \(s\)-\((23,7,\lambda_s)\) design. Use the principle of inclusion and exclusion.

**6.** State and prove Dilworth's Theorem for a finite poset.

**7.** Let \(\{a_n\}_{n=0}^{\infty}\) be a sequence satisfying a homogeneous linear recurrence relation. Define
\[
r_n=\frac{a_n}{a_{n-1}},\qquad n=1,2,3,\ldots.
\]
Give necessary and sufficient conditions on the recurrence relation for \(r_n\) to approach a finite limit, and give a way to find the limit when it exists.

**8.** Describe a combinatorial algorithm of polynomial time efficiency to solve the following problem. Prove that your algorithm has the required efficiency using theorems from the combinatorics class.

Input: \(X\) a finite set, \(\{A_1,A_2,\ldots,A_n\}\) a collection of subsets of \(X\), and \(p:X\to\mathbb{R}\) a function.

Output: \(\{x_1,x_2,\ldots,x_n\}\) distinct elements of \(X\) which maximize
\[
\sum_{i=1}^n p(x_i)
\]
subject to \(x_i\in A_i\) for all \(i\).

(Assume there exists a set of \(n\) elements satisfying the restriction \(x_i\in A_i\), \(\forall i\).)

**9.** Find the number of spanning sets in a vector space \(V\) of dimension \(n\) over \(\operatorname{GF}(q)\), the finite field with \(q\) elements. (Hint: try Möbius inversion.)
