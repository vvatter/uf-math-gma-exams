# Numerical Linear Algebra first year exam, May 2023

*Do 4 (four) problems.*

**1.** This problem has two parts.
* (a) If \(P\) is a projector, prove that \(\operatorname{null}(P)\cap\operatorname{range}(P)=\{0\}\) and \(\operatorname{null}(P)=\operatorname{range}(I-P)\).
* (b) Prove that \(P\) is an orthogonal projector if and only if it is Hermitian.

**2.** Let \(\lVert\cdot\rVert\) be a subordinate (induced) matrix norm.
* (a) If \(E\) is \(n\times n\) with \(\lVert E\rVert<1\), then show \(I+E\) is nonsingular and
  \[
  \lVert(I+E)^{-1}\rVert\leq\frac{1}{1-\lVert E\rVert}.
  \]
* (b) If \(A\) is \(n\times n\) invertible and \(E\) is \(n\times n\) with \(\lVert A^{-1}\rVert\lVert E\rVert<1\), then show \(A+E\) is nonsingular and
  \[
  \lVert(A+E)^{-1}\rVert\leq\frac{\lVert A^{-1}\rVert}{1-\lVert A^{-1}\rVert\lVert E\rVert}.
  \]

**3.** Define the matrices \(A\) and \(B\) by
\[
A=\begin{pmatrix}1&2&3\\2&4&6\\1&2&3\\2&4&6\end{pmatrix},
\qquad
B=\begin{pmatrix}1&1&0\\0&1&3\\0&1&3\\2&0&0\end{pmatrix}.
\]
* (a) Find a singular value decomposition of \(A\).
* (b) Find a QR decomposition of \(B\).

**4.** Assume \(A\in\mathbb{R}^{m\times m}\).
* (a) Prove that \(\langle x,y\rangle_A=x^*Ay\) is an inner product on \(\mathbb{R}^m\) if and only if \(A\) is symmetric and positive definite.
* (b) Assume that \(A\) is symmetric and positive definite. If \(x_*\) is the solution to \(Ax=b\) and \(\{p_1,\cdots,p_m\}\) is an orthonormal basis for \(\mathbb{R}^m\) with respect to \(\langle\ ,\ \rangle_A\) and \(x_*=\sum c_i p_i\), give a formula for the \(c_i\).

**5.** Let matrix \(A\in\mathbb{C}^{m\times n}\) with \(n<m\). Let a vector \(b\in\mathbb{C}^m\), and let \(r\) denote the residual vector \(r=b-Ax\).
* (a) Show that \(x\) solves the least-squares problem \(\min\lVert b-Ax\rVert_2\) if and only if \(r\in\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank, and describe how to find the least-squares solution using the QR decomposition of \(A\).
