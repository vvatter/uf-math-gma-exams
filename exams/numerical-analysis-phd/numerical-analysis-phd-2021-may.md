# Numerical Analysis, PhD exam, May 2021

*Do 4 (four) of the first 5 (1–5) and 4 (four) of the last 5 problems (6–10).*

**1.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\). Let \(u_j\) denote column \(j\) of \(U\).
* (a) Suppose \(\operatorname{rank}(A)=p<n<m\). Show \(\{u_1,u_2,\ldots,u_p\}\), is a basis for \(\operatorname{Col}(A)\), and \(\{u_{p+1},u_{p+2},\ldots,u_m\}\) is a basis for \(\operatorname{Null}(A^*)\).
* (b) Suppose \(k<\operatorname{rank}(A)\). What is the least-squares solution \(x\) that minimizes \(\lVert b-Cx\rVert_2\), where \(C\) is the rank-\(k\) matrix that minimizes \(\lVert A-C\rVert_2\)?

**2.** For \(x,y>0\), consider computing \(f(x,y)=\sqrt{y+x^2}-\sqrt{y}\) in floating-point arithmetic with machine precision \(\varepsilon_m\).
* (a) Explain the difficulties in computing \(f(x,y)\), if \(x^2\ll y\). What are the absolute and relative errors if \(x^2/y<\varepsilon_m\), if \(f(x,y)\) is computed directly from the form given above?
* (b) Suppose \(x^2/y<\varepsilon_m\). Describe a way to compute \(f(x,y)\) with more accuracy in this situation.

**3.** Let \(\{a_1,\ldots,a_n\}\) be a linearly independent set of vectors. Consider the Gram–Schmidt and modified Gram–Schmidt algorithms for computing an orthonormal basis \(\{q_1,\ldots,q_n\}\) so that \(\operatorname{span}\{q_1,\ldots,q_k\}=\operatorname{span}\{a_1,\ldots,a_k\}\), for each \(k=1,\ldots,n\).

Suppose in computing \(q_2\), an orthogonalization error is committed so that \(q_2^*q_1=\varepsilon\).
* (a) Use the Gram–Schmidt algorithm to compute \(v_3\) so that \(q_3=v_3/\lVert v_3\rVert\). What is \(v_3^*q_2\)?
* (b) Use the modified Gram–Schmidt algorithm to compute \(v_3\) so that \(q_3=v_3/\lVert v_3\rVert\). What is \(v_3^*q_2\)?

**4.** Compute the Cholesky decomposition of the following matrix, or explain why it does not exist.

\[
A=\begin{pmatrix}
1&1&2&0\\
1&5&4&2\\
2&4&14&1\\
0&2&1&5
\end{pmatrix}.
\]

**5.** Suppose \(A\) is Hermitian positive definite.
* (a) Prove that each principal submatrix of \(A\) is Hermitian positive definite.
* (b) Prove that an element of \(A\) with largest magnitude lies on the diagonal.

**6.** Show that if a polynomial of degree at most \(n\) has \(n+1\) (or more) zeros, then it is the zero polynomial.

**7.** This problem has two parts.
* (a) Prove for any \(f\in C[a,b]\) and integer \(n\geq 0\), that the best uniform approximation of \(f\) in \(\mathcal P_n\) is unique. You may assume the existence of at least one best uniform approximation of \(f\).
* (b) Is there some \(a\in\mathbb R\) for which \(p_1(x)=ax+1\) is the best uniform approximation to \(x^3\) in \(\mathcal P_1\) over \([-1,1]\)? If so, what is it? EXPLAIN.

**8.** Let \(\{\phi_k\}_{k=0}^{n+1}\) be a set of orthogonal polynomials on \([a,b]\), with respect to the inner-product \((f,g)=\int_a^b f(x)g(x)w(x)\,dx\), indexed so that \(\phi_k\) is of degree \(k\). Let \(\mathcal P_k\) be the space of polynomials of degree at most \(k\).
* (a) Determine the weights \(w_j\) so that the quadrature rule \(I_n(f)=\sum_{j=0}^n w_jf(x_j)\) satisfies \(I_n(f)=(1,f)\) for any \(f\in\mathcal P_n\), so long as the points \(\{x_j\}_{j=0}^n\) are distinct. You may present the weights as a set of linear equations (which you are not required to solve), or as a set of integrals (which you are not required to integrate). Justify your solution.
* (b) Prove that if the interpolation points \(\{x_j\}_{j=0}^n\) are the zeros of \(\phi_{n+1}\), then \(I_n(f)=(1,f)\) for any \(f\in\mathcal P_{2n+1}\).

**9.** Suppose \(f\in C^{n+1}[a,b]\), and let \(p\in\mathcal P_n\) be a polynomial that interpolates the data \(\{(x_i,f(x_i))\}_{i=0}^n\), where \(x_0,\ldots,x_n\), are distinct points in \([a,b]\). Consider an arbitrary fixed \(x\in[a,b]\), and derive an exact expression for the error \(f(x)-p(x)\).

**10.** The Littlewood–Salem–Izumi constant \(\alpha_0\) is the unique solution \(\alpha_0\in(0,1)\) of

\[
\int_0^{3\pi/2}\frac{\cos(t)}{t^\alpha}\,dt=0.
\]

Describe how you could use Newton’s method together with a composite Clenshaw–Curtis quadrature rule based on the \(\mathcal P_1\) interpolant over \(n\) subintervals to approximate \(\alpha_0\). Be specific about how each function used in the Newton method is defined, and be specific about how the nodes and weights for the quadrature rule are defined.

For reference, the first few Chebyshev polynomials are \(T_0(x)=1\), \(T_1(x)=x\), \(T_2(x)=2x^2-1\), \(T_3(x)=4x^3-3x\).
