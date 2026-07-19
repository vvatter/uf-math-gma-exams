# Numerical Analysis, PhD exam, August 2020

*Do 4 (four) of the first 5 (1–5) and 4 (four) of the last 5 problems (6–10).*

**1.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\) with \(\operatorname{rank}(A)=p\) and \(p\le n\le m\).
* (a) Show \(\operatorname{Col}(A^*)=\operatorname{Span}\{v_1,v_2,\ldots,v_p\}\), where \(v_1,\ldots,v_p\) are the first \(p\) columns of \(V\).
* (b) Show \(\operatorname{Null}(A)=\operatorname{Span}\{v_{p+1},v_{p+2},\ldots,v_n\}\).
* (c) Find the economy singular value decompositions of the matrix \(A\) given by
  \[
  A=\begin{pmatrix}
  1&0&4\\
  1&0&4\\
  1&0&4\\
  1&0&4
  \end{pmatrix}.
  \]

**2.** Let \(A\in\mathbb{C}^{m\times n}\) with \(\operatorname{rank}(A)=n<m\). Let \(A=QR\) be the \(QR\) decomposition of \(A\), and \(A=Q_1R_1\) be the economy \(QR\) decomposition.
* (a) Show that \(x\in\mathbb{C}^n\) that solves \(R_1x=Q_1^*b\) is the least-squares solution to \(Ax=b\) for \(b\in\mathbb{C}^m\).
* (b) Find the economy \(QR\) decomposition of matrix \(B\) given by
  \[
  B=\begin{pmatrix}
  3&0&1\\
  0&2&0\\
  4&0&0\\
  0&0&1
  \end{pmatrix}.
  \]

**3.** Let \(A\) and \(S\) be \(n\times n\) matrices, and suppose \(S\) is nonsingular.
* (a) Show that \(A\) and \(B=SAS^{-1}\) have the same eigenvalues, and provide the relation between the eigenvectors of \(B\) and the eigenvectors of \(A\).
* (b) Suppose \(A\) is skew-Hermitian. Show the eigenvalues of \(A\) are pure imaginary.

**4.** Suppose the \(5\times5\) symmetric matrix \(A\) has eigenvalues known to within the given tolerances.
\[
\begin{aligned}
3.5&>\lambda_1>2.5\\
2.0&>\lambda_2>1.0\\
1.0&>\lambda_3>-1.0\\
-1.0&>\lambda_4>-2.0\\
-2.5&>\lambda_5>-3.5.
\end{aligned}
\]
* (a) Describe how shifting can be used so that the power method can be used to compute \(\lambda_1\) with guaranteed convergence.
* (b) What is the shift that provides the best convergence rate in the worst case?

**5.** For \(x,y>0\), consider computing \(f(x,y)=\sqrt{y+x^2}-\sqrt{y}\) in floating-point arithmetic with machine precision \(\epsilon_m\).
* (a) Explain the difficulties in computing \(f(x,y)\), if \(x\ll y\). What are the absolute and relative errors if \(x^2/y<\epsilon_m\), if \(f(x,y)\) is computed directly from the form given above?
* (b) Suppose \(x^2/y<\epsilon_m\). Describe a way to compute \(f(x,y)\) with more accuracy in this situation.

**6.** Let \(\{\phi_k\}_{k=0}^{n+1}\) be a set of orthogonal polynomials on \([a,b]\), with respect to the inner-product \((f,g)=\int_a^b f(x)g(x)w(x)\,dx\), indexed so that \(\phi_k\) is of degree \(k\). Prove that \(\phi_k\) has \(k\) distinct roots \(\{x_j^{(k)}\}_{j=1}^k\), with \(x_j^{(k)}\in[a,b]\), \(j=1,\ldots,k\).

**7.** Consider the interval \([a,b]\) with the partition \(a=x_1<x_2<\cdots<x_n<x_{n+1}=b\). Suppose \(s(x)\) is the natural cubic spline that interpolates the data \(\{(x_i,y_i)\}_{i=1}^{n+1}\), and that \(g\in C^2[a,b]\) interpolates the same data. Show that
\[
\int_a^b (s''(x))^2\,dx\leq\int_a^b (g''(x))^2\,dx.
\]

**8.** This problem has two parts.
* (a) Consider the inner product on \(C(0,2)\) given by \((f,g)=\int_0^2 f(t)g(t)\,dt\). Find three orthonormal polynomials \(\phi_0,\phi_1,\phi_2\) on \((0,2)\) with respect to the given inner product such that the degree of \(\phi_n\) is equal to \(n\), \(n=0,1,2\).
* (b) Find the nodes \(t_1\) and \(t_2\) and weights \(w_1\) and \(w_2\) which yield the weighted Gaussian Quadrature formula
  \[
  \int_0^2 f(t)\,dt\approx w_1f(t_1)+w_2f(t_2)
  \]
  with degree of exactness \(m=3\). You should find the nodes exactly, and may leave the weights \(w_1,w_2\) in integral form.

**9.** Prove for any \(f\in C[a,b]\) and integer \(n\geq0\), that the best uniform approximation of \(f\) in \(P_n\) is unique. You may assume the existence of at least one best uniform approximation of \(f\).

**10.** Suppose \(f\in C^{n+1}[a,b]\), and let \(p\in P_n\) be a polynomial that interpolates the data \(\{(x_i,f(x_i))\}_{i=0}^n\), where \(x_0,\ldots,x_n\), are distinct points in \([a,b]\). Consider an arbitrary fixed \(x\in[a,b]\), and derive an exact expression for the error \(f(x)-p(x)\).
