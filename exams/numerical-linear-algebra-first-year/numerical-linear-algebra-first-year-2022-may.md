# Numerical Linear Algebra, first year exam, May 2022

*Do 4 (four) problems.*

**1.** Prove or provide a counterexample to each of the following.
* (a) If matrix \(A\) is normal and triangular, then it is diagonal.
* (b) Every matrix has a Schur factorization.

**2.** This problem has two parts.
* (a) For \(v\in\mathbb{C}^n\), define \(f_A(v):=(v^*Av)^{1/2}\). Under what condition(s) on \(A\in\mathbb{C}^{n\times n}\) is \(f_A(\cdot)\) a norm on \(\mathbb{C}^n\)? (Full credit will only be given for a general condition or conditions. An example is not sufficient.) Prove that \(f_A(\cdot)\) is a norm on \(\mathbb{C}^n\) under the condition(s) you require.
* (b) Assuming the condition(s) you require in (a), given a matrix \(A\), determine the best constants \(\alpha\) and \(\beta\) to satisfy the inequality
  \[
  \alpha\lVert v\rVert_2\leq f_A(v)\leq\beta\lVert v\rVert_2.
  \]

**3.** Let \(A=U\Sigma V^*\) be the singular value decomposition of \(A\in\mathbb{C}^{m\times n}\). Let \(u_j\) denote column \(j\) of \(U\).
* (a) Suppose \(\operatorname{rank}(A)=p<n<m\). Show \(\{u_1,u_2,\ldots,u_p\}\), is a basis for \(\operatorname{Col}(A)\), and \(\{u_{p+1},u_{p+2},\ldots,u_m\}\) is a basis for \(\operatorname{Null}(A^*)\).
* (b) Suppose \(A\) is full rank and \(x\neq 0\). Let \(\sigma_i\), \(i=1,\ldots,n\), be the singular values of \(A\). Show
  \[
  \sigma_1\geq\frac{\lVert Ax\rVert_2}{\lVert x\rVert_2}\geq\sigma_n>0.
  \]
  If you want to use the property that \(\lVert A\rVert_2=\sigma_1\), then you must prove that also.

**4.** Let \(\{a_1,\ldots,a_n\}\) be a linearly independent set of vectors. Consider the Gram–Schmidt and modified Gram–Schmidt algorithms for computing an orthonormal basis \(\{q_1,\ldots,q_n\}\) so that \(\operatorname{Span}\{q_1,\ldots,q_k\}=\operatorname{Span}\{a_1,\ldots,a_k\}\), for each \(k=1,\ldots,n\). Suppose in computing \(q_2\), an orthogonalization error is committed so that \(q_2^*q_1=\epsilon\).
* (a) Use the Gram–Schmidt algorithm to compute \(v_3\) so that \(q_3=v_3/\lVert v_3\rVert\). What is \(v_3^*q_2\)?
* (b) Use the modified Gram–Schmidt algorithm to compute \(v_3\) so that \(q_3=v_3/\lVert v_3\rVert\). What is \(v_3^*q_2\)?

**5.** Compute the Cholesky decomposition of the following matrix, or explain why it does not exist.
\[
A=\begin{pmatrix}
1 & 1/2 & 2 & 3\\
1/2 & 5/16 & 3/2 & 5/2\\
2 & 3/2 & 17 & 17\\
3 & 5/2 & 17 & 31
\end{pmatrix}.
\]
