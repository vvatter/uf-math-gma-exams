# Numerical Analysis first year exam, January 2025

*Do 4 (four) problems.*

**1.** \(g(x)=\frac{x}{2}+\frac{a}{2x}\) has \(x=\sqrt{a}\) as a fixed point where \(a>0\). Suppose we use the fixed point method with a starting point \(x_0>\sqrt{a}\). Use the theory of the fixed point method to determine the condition on \(x_0\) which guarantees
\[
|x_{k+1}-\sqrt{a}|\leq \frac{1}{2}|x_k-\sqrt{a}|,\qquad k\geq 1.
\]

**2.** Let \(f\in C[0,1]\) and let \(\sum_{i=1}^n w_i f(x_i)\) (\(n\geq 1\)) be an approximation to \(\int_0^1 f(x)\,dx\). Assume that \(0\leq w_i\leq 1\), \(0\leq x_i\leq 1\) (\(i=1,2,\ldots,n\)). Let
\[
E_n(f)=\int_0^1 f(x)\,dx-\sum_{i=1}^n w_i f(x_i)
\]
be the error in the approximation. Assume that \(E_n(p_n)=0\) for \(p_n\), which denotes any polynomial of degree \(\leq n\). Use the Weierstrass approximation theorem to prove that, given \(\epsilon>0\), there is an \(N>0\) such that \(|E_n(f)|<\epsilon\) when \(n>N\).

**3.** Given a differentiable function \(f(x)\), consider the problem of finding a polynomial \(p(x)\in\mathbb{P}^n\) such that
\[
p(x_0)=f(x_0),\qquad p'(x_i)=f'(x_i),\qquad i=1,2,\ldots,n,
\]
where \(x_i\), \(i=1,2,\ldots,n\), are distinct nodes. (It is not excluded that \(x_1=x_0\).) Show that the problem has a unique solution and describe how it can be obtained.

**4.** Let \(\{p_i(x)\}_{i=0}^{\infty}\) be the sequence of orthogonal polynomials obtained from the Gram–Schmidt orthogonalization process of \(\{x^i\}_{i=0}^{\infty}\). Consider the quadrature formula \(Q(f)=\sum_{j=0}^m \alpha_j f(x_j)\) for \(J(f)=\int_a^b f(x)\rho(x)\,dx\). Prove that \(Q(f)\) is exact for polynomials of degree \(\leq 2m+1\) if and only if the quadrature nodes \(x_j\) (\(j=0,1,\ldots,m\)) are the roots of \(p_{m+1}(x)\) and the quadrature weights \(\alpha_j=\int_a^b l_j(x)\rho(x)\,dx\), (\(j=0,1,\ldots,m\)).

**5.** Consider numerically solving the initial value problem
\[
y'(t)=f(t,y),\quad 0<t\leq t_f,\qquad \text{with }y(0)=\eta.
\]
Assume \(f\) is sufficiently differentiable and let \(h\) denote the step size. Show that the method
\[
y_{n+2}-y_{n+1}=\frac{1}{4}h(f_{n+2}+2f_{n+1}+f_n)
\]
is \(A_0\) stable.
