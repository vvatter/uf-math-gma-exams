# Numerical Linear Algebra, first year exam, January 2024

*Do 4 (four) problems.*

**1.** Assume \(A\in\mathbb{C}^{m\times m}\).
* (a) Show that \(A\) has a Schur decomposition.
* (b) If \(A\) has a collection of \(m\) linearly independent eigenvectors, show that \(A\) is diagonalizable.

**2.** Let matrix \(A\in\mathbb{C}^{m\times n}\) with \(n<m\). Let \(b\in\mathbb{C}^m\), and let \(r\) denote the residual vector \(r=b-Ax\).
* (a) Show that \(x\) solves the least squares problem \(\min\lVert b-Ax\rVert_2\) if and only if \(r\in\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank, and describe how to find the least squares solution using the QR decomposition of \(A\).

**3.** Let \(A\in\mathbb{C}^{m\times n}\), with \(m\ge n\) and \(\operatorname{rank}(A)=p=n\ge 3\). Let \(a_1,a_2,\ldots\) denote the columns of \(A\).
* (a) Using the modified Gram–Schmidt process, write out expressions for \(q_1,q_2,q_3\), the first three columns of \(Q\) in the QR decomposition of \(A\).
* (b) Show the vector \(q_3\) found in part (a) is orthogonal to both \(q_1\) and \(q_2\).

**4.** Let \(\lVert\cdot\rVert\) be a subordinate (induced) matrix norm.
* (a) If \(E\) is a \(n\times n\) with \(\lVert E\rVert<1\), then show \(I+E\) is nonsingular and
  \[
  \lVert(I+E)^{-1}\rVert\leq \frac{1}{1-\lVert E\rVert}.
  \]
* (b) If \(A\) is a \(n\times n\) invertible and \(E\) is \(n\times n\) with \(\lVert A^{-1}\rVert\lVert E\rVert<1\), then show \(A+E\) is nonsingular and
  \[
  \lVert(A+E)^{-1}\rVert\leq \frac{\lVert A^{-1}\rVert}{1-\lVert A^{-1}\rVert\lVert E\rVert}.
  \]

**5.** If \(q_1,\ldots,q_n\) is an orthonormal basis for the subspace \(V\subset\mathbb{C}^m\) with \(m>n\), prove that the orthogonal projector onto \(V\) is \(QQ^*\), where \(Q\) is the matrix whose columns are the \(q_j\).
