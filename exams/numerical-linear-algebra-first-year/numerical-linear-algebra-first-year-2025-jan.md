# Numerical Linear Algebra, first year exam, January 2025

*Do 4 (four) problems.*

**1.** Assume \(A \in \mathbb{C}^{m \times m}\).
* (a) Show that \(A\) has a Schur decomposition.
* (b) If \(A\) has a collection of \(m\) linearly independent eigenvectors, show that \(A\) is diagonalizable.

**2.** If \(q_1, \ldots, q_n\) is an orthonormal basis for the subspace \(V \subset \mathbb{C}^m\) with \(m>n\), prove that the orthogonal projector onto \(V\) is \(QQ^*\), where \(Q\) is the matrix whose columns are the \(q_j\).

**3.** Let \(A \in \mathbb{C}^{m \times n}\), with \(m \geq n\) and \(\operatorname{rank}(A)=n \geq 3\). Let \(a_1,a_2,\ldots\) denote the columns of \(A\).
* (a) Using the modified Gram–Schmidt process, write out expressions for \(q_1,q_2,q_3\), the first three columns of \(Q\) in the QR decomposition of \(A\).
* (b) Show the vector \(q_3\) found in part (a) is orthogonal to both \(q_1\) and \(q_2\).

**4.** Let \(\lVert \cdot \rVert\) be a subordinate (induced) matrix norm.
* (a) If \(E\) is a \(n \times n\) with \(\lVert E\rVert<1\), then show \(I+E\) is nonsingular and
  \[
  \lVert(I+E)^{-1}\rVert \leq \frac{1}{1-\lVert E\rVert}.
  \]
* (b) If \(A\) is a \(n \times n\) invertible and \(E\) is \(n \times n\) with \(\lVert A^{-1}\rVert\lVert E\rVert<1\), then show \(A+E\) is nonsingular and
  \[
  \lVert(A+E)^{-1}\rVert \leq \frac{\lVert A^{-1}\rVert}{1-\lVert A^{-1}\rVert\lVert E\rVert}.
  \]

**5.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A \in \mathbb{C}^{m \times n}\). Let \(u_j\) denote column \(j\) of \(U\).
* (a) Suppose \(\operatorname{rank}(A)=p<n<m\). Show \(\{u_1,u_2,\ldots,u_p\}\) is a basis for \(\operatorname{Col}(A)\) and \(\{u_{p+1},u_{p+2},\ldots,u_m\}\) is a basis for \(\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank and \(x \neq 0\). Let \(\sigma_i\), \(i=1,\ldots,n\), be the singular values of \(A\). Show
  \[
  \sigma_1 \geq \frac{\lVert Ax\rVert_2}{\lVert x\rVert_2} \geq \sigma_n>0.
  \]
  If you want to use the property that \(\lVert A\rVert_2=\sigma_1\), then you must prove that it holds.
