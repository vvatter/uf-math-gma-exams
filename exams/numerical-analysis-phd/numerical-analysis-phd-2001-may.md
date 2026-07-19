# Numerical Analysis PhD exam, May 2001

*Do any 8 of the following 10 problems.*

## Part 1: Numerical Linear Algebra

**1.** This problem has five parts.
* (a) Under what conditions does a real \(n\) by \(n\) matrix \(A\) have a Schur decomposition \(A=U^{\mathrm T}TU\), where \(U\) and \(T\) are real \(n\) by \(n\) matrices with \(U\) orthogonal and \(T\) upper triangular?
* (b) Under what conditions on \(A\) is \(T\) diagonal?
* (c) Does the matrix
  \[
  A=\begin{pmatrix}1&0&1\\1&-1&0\\0&1&1\end{pmatrix}
  \]
  have an orthogonal set of eigenvectors?
* (d) Give a careful statement of the singular value decomposition of a real \(m\) by \(n\) matrix.
* (e) Under what conditions does the singular value decomposition exist?

**2.** Consider the linear system \(Ax=b\).
* (a) If the rows of \(A\) are linearly independent, derive a formula for the solution of minimal 2-norm.
* (b) If the columns of \(A\) are linearly independent, derive a formula for the \(x\) that minimizes the 2-norm of the residual \(r=b-Ax\).
* (c) Use the singular value decomposition of \(A\) to give a formula for the \(x\) that minimizes the 2-norm of the residual, and among all the \(x\)’s which minimize the 2-norm, it has minimal norm.

**3.** This problem has two parts.
* (a) Given a vector \(x\in\mathbb R^n\) and a natural number \(k<n\), give a formula for a unit vector \(w\) for which the vector \(y=(I-2ww^{\mathrm T})x\) satisfies the following conditions: \(y_i=x_i\) for \(i<k\) and \(y_i=0\) for \(i>k\).
* (b) Using these Householder transformations, write a pseudo code (or a matlab code) for reducing a real symmetric matrix to tridiagonal form using Householder similarity transformations.

**4.** This problem has three parts.
* (a) State and prove the Gershgorin Circle Theorem.
* (b) Let
  \[
  A=\begin{pmatrix}5&1&3\\2&4&1\\3&-1&4\end{pmatrix}.
  \]
  What can you say about the location of the eigenvalues of \(A\)?
* (c) Use the Gershgorin Circle Theorem to estimate the size of the largest root of the polynomial \(p(x)=x^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}+\cdots+a_1x+a_0\).

**5.** This problem has two parts.
* (a) Find the ellipse or hyperbola, of the form \(ax^2+by^2=1\), that best fits \(n\) data points \((x_1,y_1),(x_2,y_2),\ldots,(x_n,y_n)\) in the plane by computing the least squares solution to the \(n\) linear equations gotten by substituting each of the data points into the quadratic equation.
* (b) Test your method with the dataset \((1,1),(2,4),(3,9),(4,16)\).

## Part II: Numerical Analysis

**6.** This problem has three parts.
* (a) State Newton’s method (the algorithm) for solving \(f(x)=0\) where \(f:\mathbb R\to\mathbb R\).
* (b) Assuming \(f\) is smooth and we have an initial guess sufficiently close to a root \(p\), state sufficient condition(s) for the method to converge quadratically.
* (c) Show that Newton’s method applied to \(x^5=2\) converges quadratically to the root \(2^{1/5}\) from any starting guess \(x>0\).

**7.** This problem has three parts.
* (a) Given a function \(f\) with \(n+1\) continuous derivatives on the interval \(I=[-1,1]\), show that, given \(n+1\) points \(\{x_0,x_1,\ldots,x_n\}\) in \(I\), there exists a unique polynomial \(P_n(x)\) of degree \(\le n\) such that
  \[
  P_n(x_i)=f(x_i)\qquad\text{for }i=0,\ldots,n.
  \]
* (b) Prove that, given \(t\in I\), there exists \(\eta\in I\) such that
  \[
  f(t)-P_n(t)=\frac{(t-x_0)\cdots(t-x_n)}{(n+1)!}f^{(n+1)}(\eta).
  \]
* (c) From the above we get that (all norms are on the interval \(I\))
  \[
  \lVert f-P_n\rVert_\infty\le \max_{t\in I}\left|(t-x_0)(t-x_1)\cdots(t-x_n)\right|\frac{\lVert f^{(n+1)}\rVert_\infty}{(n+1)!}.
  \]
  What choice for the points \(x_0,\ldots,x_n\) minimizes the right hand side of this error bound?

**8.** This problem has two parts.
* (a) Find a function \(q(x)\) which has a continuous first derivative for each \(x\in(-\infty,\infty)\) with the properties:
  \[
  q(x)=\begin{cases}
  1,&\text{if }x=0,\\
  0,&\text{for all }|x|\ge 2,\\
  a_0+a_1x+a_2x^2,&\text{for all }x\in[-2,-1],\\
  b_0+b_1x+b_2x^2,&\text{for all }x\in[-1,1],\\
  c_0+c_1x+c_2x^2,&\text{for all }x\in[1,2].
  \end{cases}
  \]
* (b) Use the function \(q(x)\) defined in part a to interpolate a set of equally spaced points \((x_0,y_0),(x_1,y_1),\ldots,(x_n,y_n)\), where \(h=x_{k+1}-x_k\) for all \(k\). In particular, describe how to find constants \(c_k\) so that the function
  \[
  Q(x)=\sum_{k=0}^n c_k q\!\left(\frac{x-x_k}{h}\right)
  \]
  has the property that \(Q(x_k)=y_k\) for all \(k\).

**9.** Let \(P_2(x)\) be a quadratic polynomial interpolating \(g(x)\) at \(x=0,h,2h\).
* (a) Use this to derive a numerical integration formula \(I_h\) for
  \[
  I=\int_0^{3h}g(x)\,dx.
  \]
* (b) Use a Taylor series expansion of \(g(x)\) to show
  \[
  I-I_h=\frac{3}{8}h^4g^{(3)}(0)+O(h^5).
  \]

**10.** Triple Recursion Formula. If \(\{\phi_n(x)\}\) is an orthogonal family of polynomials on \([a,b]\), with respect to the weight function \(w(x)\ge 0\), and \(n\ge 1\), then show that
\[
\phi_{n+1}(x)=(a_nx+b_n)\phi_n(x)-c_n\phi_{n-1}(x),
\]
for some constants \(a_n,b_n\), and \(c_n\). (Hint: Let \(g(x)=\phi_{n+1}(x)-a_nx\phi_n(x)\), where \(a_n\) is a constant chosen so that \(g(x)\) has degree \(n\).)
