# Numerical Analysis PhD exam, May 1999

*Do any 8 of the following 10 problems.*

**1.** This problem has six parts.
* (1) Give a careful statement and proof of the singular value decomposition.
* (2) Give a careful statement of the \(QR\) factorization theorem.
* (3) Indicate how the Householder transformations are used in the proof of the \(QR\) factorization theorem.
* (4) Describe the \(QR\) Iteration Algorithm with shift \(\mu\).
* (5) Describe how the \(QR\) Iteration is used to compute the \(SVD\).
* (6) How can the singular values be used to compute the condition number of a matrix.

**2.** Give a careful proof of the following Theorem: If \(p\geq 1\),

1. \(\mathbf A\in\mathbb R^{n\times n}\) is invertible,
2. \(\mathbf b\) and \(\Delta\mathbf b\) are vectors in \(\mathbb R^n\), and
3. \(\mathbf x\) and \(\Delta\mathbf x\) are vectors in \(\mathbb R^n\) and are solutions to \(\mathbf A\mathbf x=\mathbf b\), and \(\mathbf A\Delta\mathbf x=\Delta\mathbf b\), respectively,

then
\[
\frac{\|\Delta\mathbf x\|_p}{\|\mathbf x\|_p}\leq \kappa_p(\mathbf A)\frac{\|\Delta\mathbf b\|_p}{\|\mathbf b\|_p}.
\]

**3.** This problem has three parts.
* (1) Describe how Jacobi rotations can be used to diagonalize a real symmetric matrix.
* (2) Give the error estimate for a single Jacobi rotation.
* (3) Give the error estimates for repeated Jacobi rotations.

**4.** This problem has two parts.
* (1) Write out the system of linear equations to be solved to find the periodic spline interpolation for the given data points \((x_0,y_0),(x_1,y_1),\ldots,(x_n,y_n)\), where \(x_0<x_1<\cdots<x_n\) and \(y_n=y_0\).
* (2) What method would you recommend for solving the system of linear equations. Explain!!

**5.** This problem has three parts.
* (1) Give a careful definition of the Householder transformation.
* (2) Explain why the Householder transformation is preferred over the Gram–Schmidt orthogonalization process for creating an orthonormal basis. (Give an example if necessary.)
* (3) Show how Householder transformations can be used to bidiagonalize any real matrix.

**6.** This problem has four parts.
* (1) Give a careful statement of the Pythagorean Theorem property for clamped cubic splines.
* (2) Give a careful statement of the integral minimization property for clamped cubic splines.
* (3) If \(s_n(x)\) denotes the clamped cubic spline interpolant for a function \(f(x)\) at the knots \((x_0,y_0),(x_1,y_1),\ldots,(x_n,y_n)\), then give a precise statement for the error between \(s_n(x)\) and \(f(x)\).
* (4) Prove the error formula given in step (3) above.

**7.** This problem has three parts.
* (1) If \(p_n(x)=\frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n\), then show that \(\int_{-1}^1 x^m p_n(x)\,dx=0\) for all \(m<n\). (Hint: Think small values of \(m\) and \(n\), induction, and parts.)
* (2) What can you conclude about the relationship between the polynomials \(p_n(x)\) and the Legendre polynomials?
* (3) Explain the method of Gauss quadrature for the numerical approximation of the integral of a function.

**8.** This problem has three parts.
* (1) Discuss the ideas behind the linear shooting method for approximating the solution of a linear two point boundary value problem. In particular, explain how the Runge–Kutta method can be used in the approximation.
* (2) Describe how the Galerkin method can be used to solve a 2 point boundary value problem on the interval \([0,1]\).
* (3) Explain why splines have an advantage over \(\sin(kx)\) as choices of test functions for the Galerkin method.

**9.** This problem has three parts.
* (1) Give a careful statement of the Contraction Mapping Theorem.
* (2) Outline a proof of the Contraction Mapping Theorem.
* (3) Indicate how Aitken’s method can be used to accelerate convergence.

**10.** This problem has two parts.
* (1) Give a careful statement of the error formula for the trapezoidal rule for approximating an integral.
* (2) Give a careful proof of the error formula for the trapezoidal rule.
