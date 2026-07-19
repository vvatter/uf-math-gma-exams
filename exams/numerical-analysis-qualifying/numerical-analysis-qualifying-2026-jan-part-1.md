# Numerical Analysis qualifying exam, January 2026, Part 1

*Do 4 (four) problems.*

**1.** Prove each of the following.
* (a) The matrix 2-norm is invariant under unitary transformation.
* (b) If \(n\times n\) matrix \(A\) is diagonal, then for any matrix \(p\)-norm \(\|\cdot\|_p\), it holds that \(\|A\|_p=\max_{1\le i\le n}|a_{ii}|\).

**2.** Suppose \(A\in\mathbb{C}^{m\times n}\). Prove or provide a counterexample for each of the following.
* (a) The Frobenius norm of a matrix is induced by (subordinate to) a vector norm.
* (b) \(\|A\|_2\le \|A\|_F\le \sqrt{n}\|A\|_2\).

**3.** Let \(A\in\mathbb{C}^{n\times n}\). You may use the fact (if you find it useful) That \(A\) has a Schur decomposition. Prove or provide a counterexample for each of the following.
* (a) If \(A\) is both normal and triangular then it is diagonal.
* (b) If \(A\) is normal then the 2-norm of \(A\) is equal to it’s spectral radius \(\rho(A)\).

**4.** This problem has two parts.
* (a) Let \(r_i=\sum_{j=1,\,j\ne i}^{n}|a_{ij}|\). Let \(D_i\) be the disk in \(\mathbb{C}\) with center \(a_{ii}\) and radius \(r_i\). Prove that if \(\lambda\) is an eigenvalue of \(A\), then \(\lambda\in\bigcup_i D_i\); in other words, \(\lambda\) is in at least one of the disks \(D_i\).
* (b) Determine all eigenvalues of the Householder reflector \(H(w)\), including their multiplicities. Justify your answer.

**5.** Define the matrices \(A\) and \(B\) by
\[
A=\begin{pmatrix}1&3&0\\1&3&0\\1&3&0\\1&3&0\end{pmatrix},\qquad B=\begin{pmatrix}1&0&1\\0&2&0\\1&0&0\\0&0&1\end{pmatrix}.
\]
* (a) Find a full singular value decomposition of \(A\).
* (b) Find an economy QR decomposition of \(B\).
