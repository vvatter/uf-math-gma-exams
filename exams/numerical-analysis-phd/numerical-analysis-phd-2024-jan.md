# Numerical Analysis PhD exam, January 2024

*Do 4 (four) of the first 5 (1–5) and 4 (four) of the last 5 problems (6–10).*

**1.** Assume \(A \in \mathbb{C}^{m \times m}\).
* (a) Show that \(A\) has a Schur decomposition.
* (b) If \(A\) has a collection of \(m\) linearly independent eigenvectors, show that \(A\) is diagonalizable.

**2.** Let matrix \(A \in \mathbb{C}^{m \times n}\) with \(n < m\). Let \(b \in \mathbb{C}^m\), and let \(r\) denote the residual vector \(r=b-Ax\).
* (a) Show that \(x\) solves the least squares problem \(\min \lVert b-Ax\rVert_2\) if and only if \(r \in \operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank, and describe how to find the least squares solution using the QR decomposition of \(A\).

**3.** Let \(A \in \mathbb{C}^{m \times n}\), with \(m \geq n\) and \(\operatorname{rank}(A)=p=n \geq 3\). Let \(a_1,a_2,\cdots\) denote the columns of \(A\).
* (a) Using the modified Gram–Schmidt process, write out expressions for \(q_1,q_2,q_3\), the first three columns of \(Q\) in the QR decomposition of \(A\).
* (b) Show the vector \(q_3\) found in part (a) is orthogonal to both \(q_1\) and \(q_2\).

**4.** Let \(\lVert\,\cdot\,\rVert\) be a subordinate (induced) matrix norm.
* (a) If \(E\) is a \(n \times n\) with \(\lVert E\rVert<1\), then show \(I+E\) is nonsingular and
  \[
  \lVert(I+E)^{-1}\rVert \leq \frac{1}{1-\lVert E\rVert}.
  \]
* (b) If \(A\) is a \(n \times n\) invertible and \(E\) is \(n \times n\) with \(\lVert A^{-1}\rVert\lVert E\rVert<1\), then show \(A+E\) is nonsingular and
  \[
  \lVert(A+E)^{-1}\rVert \leq \frac{\lVert A^{-1}\rVert}{1-\lVert A^{-1}\rVert\lVert E\rVert}.
  \]

**5.** If \(q_1,\ldots,q_n\) is an orthonormal basis for the subspace \(V \subset \mathbb{C}^m\) with \(m>n\), prove that the orthogonal projector onto \(V\) is \(QQ^*\), where \(Q\) is the matrix whose columns are the \(q_j\).

**6.** Derive the three-point formula for the second derivative
\[
f''(x_0)=\frac{1}{h^2}\bigl(f(x_0-h)-2f(x_0)+f(x_0+h)\bigr)-\frac{h^2}{12}f^{(4)}(\eta),
\]
for some \(\eta \in [x_0-h,x_0+h]\).

**7.** Consider
\[
y'=4ty; \qquad t\in[0,1]; \qquad y(0)=2, \tag{1}
\]
which has solution \(Y(t)=2e^{2t^2}\).
* (a) Derive an error bound for the forward Euler scheme.
* (b) Derive the Taylor method of order 2 for (1).

**8.** Let \(P_1\) be the space of polynomials of degree at most one. Using the norm
\[
\lVert u\rVert_2=\left(\int_a^b u^2\,dx\right)^{1/2}.
\]
* (a) Find the least-squares approximation to \(f(x)=x^3\) in \(P_1\) over \([a,b]=[-1,1]\).
* (b) Find the least-squares approximation to \(f(x)=x^4\) in \(P_1\) over \([a,b]=[0,1]\).

**9.** Consider the fixed point problem \(x=f(x)\) where \(f(x)=e^{-(3+x)}\).
* (a) Assuming all computations are done in exact arithmetic, find the largest open interval in \(\mathbb{R}\) where the fixed point iteration \(x_{k+1}=f(x_k)\) is ensured to converge.
* (b) Write a Newton iteration for finding the fixed point.

**10.** Suppose \(f \in C^{n+1}[a,b]\), and let \(p \in P_n\) be a polynomial that interpolates the data \(\{(x_i,f(x_i))\}_{i=0}^n\), where \(x_0,\ldots,x_n\) are distinct points in \([a,b]\). Consider an arbitrary fixed \(x \in [a,b]\), and derive an exact expression for the error \(f(x)-p(x)\).
