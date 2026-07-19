# Numerical Analysis PhD exam, August 2021

*Do 4 (four) of the first 5 (1–5) and 4 (four) of the last 5 problems (6–10).*

*You may use the following degree \(n\) orthogonal polynomials as you like.*
\[
\begin{array}{c|c|c}
n & \text{Legendre} & \text{Chebyshev} \\
\hline
0 & 1 & 1 \\
1 & x & x \\
2 & 3x^2-1 & 2x^2-1 \\
3 & 5x^3-3x & 4x^3-3x \\
4 & 35x^4-30x^2+3 & 8x^4-8x^2+1
\end{array}
\]

**1.** Suppose \(A\in\mathbb{C}^{m\times m}\).
* (a) Suppose \(A\) is normal and upper-triangular. Show that \(A\) is diagonal.
* (b) Prove that a Schur decomposition diagonalizes \(A\) if and only if \(A\) is normal.

**2.** This problem has two parts.
* (a) Suppose \(A\in\mathbb{C}^{m\times n}\) with \(m\ge n\). Show that \(A^*A\) is nonsingular if and only if \(A\) has full rank.
* (b) Suppose \(A\in\mathbb{C}^{m\times m}\), and let \(a_j\) be the \(j\)th column of \(A\). Prove the inequality
  \[
  |\det A|\le \prod_{j=1}^{m}\lVert a_j\rVert_2.
  \]
  (Hint: it may be useful to consider the QR decomposition of \(A\).)

**3.** Define the matrices \(A\) and \(B\) by
\[
A=\begin{pmatrix}
1&2&3\\
1&2&3\\
1&2&3\\
1&2&3
\end{pmatrix},
\qquad
B=\begin{pmatrix}
3&0&0\\
0&4&1\\
4&0&1\\
0&3&1
\end{pmatrix}.
\]
* (a) Find an economy singular value decomposition of \(A\).
* (b) Find an economy QR decomposition of \(B\).

**4.** Let \(\{a_1,\ldots,a_n\}\) be a linearly independent set of vectors. Consider the Gram–Schmidt and modified Gram–Schmidt algorithms for computing an orthonormal basis \(\{q_1,\ldots,q_n\}\) so that \(\operatorname{span}\{q_1,\ldots,q_k\}=\operatorname{span}\{a_1,\ldots,a_k\}\), for each \(k=1,\ldots,n\).

Suppose in computing \(q_2\), an orthogonalization error is committed so that \(q_2^*q_1=\varepsilon\).
* (a) Use the Gram–Schmidt algorithm to compute \(v_3\) so that \(q_3=v_3/\lVert v_3\rVert\). What is \(v_3^*q_2\)?
* (b) Use the modified Gram–Schmidt algorithm to compute \(v_3\) so that \(q_3=v_3/\lVert v_3\rVert\). What is \(v_3^*q_2\)?

**5.** Suppose \(A\in\mathbb{C}^{m\times m}\).
* (a) Prove Gershgorin’s disk theorem: Let \(r_i=\sum_{j=1,\,j\ne i}^{m}|a_{ij}|\). Let \(D_i\) be the disk in \(\mathbb{C}\) with center \(a_{ii}\) and radius \(r_i\). If \(\lambda\) is an eigenvalue of \(A\), then \(\lambda\in\bigcup_i D_i\); in other words, \(\lambda\) is in at least one of the disks \(D_i\).
* (b) Suppose \(A\) is Hermitian positive definite. Prove that an element of \(A\) with largest magnitude lies on the diagonal.

**6.** Consider the function \(f(t)\) on \([-1,1]\) given by
\[
f(t)=
\begin{cases}
1+t, & -1\le t\le 0,\\
1-t, & 0\le t\le 1.
\end{cases}
\]
Let \(P_k\) be the space of polynomials of degree at most \(k\).
* (a) Find the best uniform approximation of \(f\) in \(P_1\) over \([-1,1]\).
* (b) Find the best approximation of \(f\) in \(P_1\) in the norm induced by the inner-product \((u,v)=\int_{-1}^{1}uv\,dt\).
* (c) Find the best approximation of \(f\) in \(P_2\) in the norm induced by the inner-product \((u,v)=\int_{-1}^{1}uv\,dt\).

**7.** Let \(\{\phi_k\}_{k=0}^{n+1}\) be a set of orthogonal polynomials on \([a,b]\), with respect to the inner-product \((f,g)=\int_a^b f(x)g(x)w(x)\,dx\), indexed so that \(\phi_k\) is of degree \(k\). Recall that the weight function \(w\) for the inner-product satisfies \(w\in L^\infty\) and \(w(x)>0\) for almost every \(x\in[a,b]\). Prove that \(\phi_k\) has \(k\) distinct roots \(\{x_j^{(k)}\}_{j=1}^k\), with \(x_j^{(k)}\in[a,b]\), \(j=1,\ldots,k\).

**8.** Find \(x_0,x_1,x_2\in[a,b]\), and \(c_0,c_1,c_2\in\mathbb{R}\), that maximize the degree of exactness for the quadrature formula
\[
\int_a^b f(x)\,dx\approx c_0f(x_0)+c_1f(x_1)+c_2f(x_2).
\]

**9.** The Littlewood–Salem–Izumi constant \(\alpha_0\) is the unique solution \(\alpha_0\in(0,1)\) of
\[
\int_0^{3\pi/2}\frac{\cos(t)}{t^\alpha}\,dt=0.
\]
Describe how you could use Newton’s method together with a composite 2 point Gauss quadrature rule over \(N\) subintervals to approximate \(\alpha_0\). Be specific about how each function used in the Newton method is defined, and be specific about how the nodes and weights for the quadrature rule are defined.

**10.** Consider the ODE \(y'=f(x,y)\) on an interval \(a\le x\le b\), with \(h=(b-a)/N\) for some given value of \(N\).
* (a) Suppose \(f\) is \(C^1\) on \([a,b]\). Compute the local truncation error (also called truncation error) for the forward Euler method \(y_{k+1}=y_k+hf(x_k,y_k)\).
* (b) Suppose \(f=y^\lambda\) and \(y(a)=1\). For what values of \(\lambda\) will the forward Euler method converge for \(h\) small enough? You are not required to state how small \(h\) needs to be. If your solution requires any additional assumptions, they should be clearly stated.
