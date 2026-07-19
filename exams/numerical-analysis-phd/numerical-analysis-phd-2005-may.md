# Numerical Analysis PhD exam, May 2005

*Do any eight of the ten problems below.*

**1.** This problem has three parts.
* (a) Consider the matrix \(A=uv^*\), where \(u\) and \(v\in\mathbb{C}^n\). Under what condition on \(u\) and \(v\) is \(A\) a projector?
* (b) Show that the Householder matrix \(H=I-2ww^*\), where \(\lVert w\rVert=1\), is unitary.
* (c) Given a vector \(x\in\mathbb{C}^n\) and an integer \(k\) with \(1<k<n\), derive a formula for a Householder matrix with the property that \((Hx)_i=0\) for \(i>k\) and \((Hx)_i=x_i\) for \(i<k\). Be sure to choose the signs so that the formula is numerically stable.

**2.** This problem has three parts.
* (a) Given a matrix \(A\in\mathbb{C}^{m\times n}\) with \(n\) linearly independent columns, derive the formula (the normal equation) for the least squares solution to the possibly overdetermined linear system \(Ax=b\).
* (b) Given a matrix \(A\in\mathbb{C}^{m\times n}\) with \(m\) linearly independent rows, derive the formula (the analogue of the normal equation) for the minimum norm solution \(Ax=b\).
* (c) Suppose you are given the singular value decomposition (SVD) \(A=U\Sigma V^*\). Derive a single formula for the least squares/minimum norm solution to \(Ax=b\) which is expressed in terms of \(U\), \(\Sigma\), and \(V\).

**3.** Consider the invertible linear system \(Ax=b\). Derive a tight bound for the condition number with respect to perturbations in \(b\). If \(A(x+\delta x)=b+\delta b\) is the perturbed system, then with the 2-norm, for which choice of \(b\) and for which perturbation \(\delta b\) is this bound tight?

**4.** Let
\[
C=\begin{bmatrix}
-a_1&-a_2&\cdots&-a_{n-1}&-a_n\\
1&0&\cdots&0&0\\
0&1&\ddots&\vdots&\vdots\\
\vdots&\ddots&\ddots&0&\vdots\\
0&\cdots&0&1&0
\end{bmatrix},
\qquad
e=\begin{bmatrix}1\\0\\\vdots\\\vdots\\0\end{bmatrix}.
\]
* (a) What is the characteristic polynomial of \(C\)?
* (b) Consider any \(A\in\mathbb{C}^{n\times n}\) and \(b\in\mathbb{C}^n\). Let the characteristic polynomial of \(A\) be
  \[
  p(\lambda)=\lambda^n+a_1\lambda^{n-1}+a_2\lambda^{n-2}+\cdots+a_{n-1}\lambda+a_n,
  \]
  \[
  K=[b,Ab,A^2b,\ldots,A^{n-1}b],
  \qquad
  R=\begin{bmatrix}
  1&a_1&a_2&\cdots&a_{n-1}\\
  0&1&a_1&\cdots&a_{n-2}\\
  \vdots&\ddots&\ddots&\ddots&\vdots\\
  \vdots&&\ddots&\ddots&a_1\\
  0&\cdots&\cdots&0&1
  \end{bmatrix}.
  \]
  Show that if \(K\) is invertible, then
  \[
  (KR)^{-1}A(KR)=C
  \qquad\text{and}\qquad
  (KR)^{-1}b=e.
  \]
  (Suggestion: Prove that \(A(KR)=(KR)C\) using \(p(A)=0\).)

**5.** Let \(A=QR\) be the factorization of \(A\) into the product of a unitary matrix and a triangular matrix. Suppose that the columns of \(A\) are linearly independent. Show that \(|r_{kk}|\) is the distance from the \(k\)-th column of \(A\) to the linear space spanned by the first \(k-1\) columns of \(A\).

**6.** Show that \(x=\pi+0.5\sin(x/2)\) has a unique solution \(\alpha\) in \(\mathbb{R}\). Give a fixed point iteration by which one can compute an approximation to \(\alpha\) numerically and prove that it converges at order one.

**7.** The Lagrange interpolation problem is to find a polynomial \(p_n(x)\) of degree at most \(n\) such that
\[
p_n(x_i)=y_i,\qquad i=0,\ldots,n,
\]
where \(x_0,\ldots,x_n\) are distinct real points and \(y_0,\ldots,y_n\) are given data. Prove that this problem always has a unique solution.

**8.** Consider the quadrature that approximates
\[
\int_a^b f(x)\,dx
\]
by
\[
I_3(f):=\int_a^b P_3(x)\,dx,
\]
where \(P_3(x)\) is the cubic Hermite interpolant to \(f(x)\) at the points \(x=a,b\). Obtain an error formula for this approximation. (This is called the corrected trapezoid rule.)

**9.** Consider multistep methods of the form
\[
y_{n+1}=y_{n-q}+h\sum_{j=-1}^{p}b_jf(x_{n-j},y_{n-j})
\]
with \(q\geq1\). Show that such methods do not satisfy the strong root condition. Find an example with \(q=1\) that is relatively stable.

**10.** Let \(S_n^1\) denote the space of linear splines based on knots \(a=t_0<t_1<\cdots<t_n=b\), i.e.,
\[
S_n^1=\left\{v:v|_{[t_j,t_{j+1}]}\text{ is linear for all }j=0,1,\ldots,n-1\text{ and }v\text{ is continuous on }[a,b]\right\}.
\]
Let \(s_f\in S_n^1\) interpolate a continuous function \(f\) at the knots.
* (a) Prove that \(\lVert s_f\rVert_\infty\leq\lVert f\rVert_\infty\). (Here \(\lVert v\rVert_\infty=\max_{x\in[a,b]}|v(x)|\).)
* (b) Prove that \(\lVert f-s_f\rVert_\infty\leq2\lVert f-s\rVert_\infty\) for any \(s\in S_n^1\).
* (c) Consider the error in best approximation to \(f\) from \(S_n^1\) and the error in approximating \(f\) by its linear interpolant \(s_f\). If one goes to zero, does the other go to zero?
