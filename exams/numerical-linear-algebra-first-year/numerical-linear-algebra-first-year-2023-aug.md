# Numerical Linear Algebra first year exam, August 2023

*Do 4 (four) problems.*

**1.** Suppose \(A\) is Hermitian positive definite.
* (a) Prove that each principal submatrix of \(A\) is Hermitian positive definite.
* (b) Prove that an element of \(A\) with largest magnitude lies on the diagonal.
* (c) Prove that \(A\) has a Cholesky decomposition.

**2.** Let \(P\in\mathbb{C}^{m\times n}\) be a projector. Show that \(\lVert P\rVert_2=1\) if and only if \(P\) is an orthogonal projector.

**3.** Let \(A\in\mathbb{C}^{m\times n}\), with \(m\geq n\) and \(\operatorname{rank}(A)=p=n\geq 3\). Let \(a_1,a_2,\ldots\) denote the columns of \(A\).
* (a) Using the modified Gram–Schmidt process, write out expressions for \(q_1,q_2,q_3\), the first three columns of \(Q\) in the QR decomposition of \(A\).
* (b) Show the vector \(q_3\) found in part (a) is orthogonal to both \(q_1\) and \(q_2\).

**4.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\). Let \(u_j\) denote column \(j\) of \(U\).
* (a) Suppose \(\operatorname{rank}(A)=p<n<m\). Show \(\{u_1,u_2,\ldots,u_p\}\) is a basis for \(\operatorname{Col}(A)\) and \(\{u_{p+1},u_{p+2},\ldots,u_m\}\) is a basis for \(\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank and \(x\neq 0\). Let \(\sigma_i\), \(i=1,\ldots,n\), be the singular values of \(A\). Show
  \[
  \sigma_1\geq\frac{\lVert Ax\rVert_2}{\lVert x\rVert_2}\geq\sigma_n>0.
  \]
  If you want to use the property that \(\lVert A\rVert_2=\sigma_1\), then you must prove that.

**5.** Let \(A\in\mathbb{C}^{m\times m}\) be Hermitian.
* (a) Show that all eigenvalues of \(A\) are real.
* (b) Define the stationary iterative method (a.k.a. fixed point method)
  \[
  x^{(k+1)}=Ax^{(k)}+b. \tag{1}
  \]
  Suppose (1) has fixed-point \(x\), namely \(x\) satisfies \(x=Ax+b\). Show the iteration (1) converges to \(x\) from any starting guess \(x^{(0)}\), that is \(x^{(k)}\to x\) as \(k\to\infty\), if and only if the eigenvalues \(\lambda_i\) of \(A\) satisfy \(|\lambda_i|<1\), \(i=1,\ldots,m\). You may use the fact that Hermitian matrix \(A\) is unitarily diagonalizable.
