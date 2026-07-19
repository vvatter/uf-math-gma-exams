# Numerical Analysis, PhD exam, September 2000

*Do any 8 of the following 10 problems.*

## Part 1: Numerical Linear Algebra

**1.** A square matrix \(A\) which can be decomposed into a form \(A=SDS^{-1}\), where \(D\) is diagonal, is said to be diagonalizable.
* (a) Is the matrix \[A=\begin{pmatrix}5&1\\0&3\end{pmatrix}\] diagonalizable? Why?
* (b) Can the above matrix \(A\) be diagonalized with a matrix \(S\) such that \(S^*S=I\)?

**2.** This problem has three parts.
* (a) State a procedure for factoring a matrix \(A\) (without pivoting) into a form \(A=LDU\), where \(L\) is unit lower triangular, \(U\) is unit upper triangular, and \(D\) is diagonal.
* (b) State sufficient conditions on \(A\) for the procedure in part (a) (without pivoting) to work.
* (c) What is the computational advantage of having lower and upper triangular matrices? An explanation without specific computation counts is sufficient.

**3.** This problem has two parts.
* (a) Under what conditions can a matrix be factored into a form \(A=U^*TU\), where \(U^*U=I\), and \(T\) is upper triangular?
* (b) If \(A\) is Hermitian, how is \(U\) constructed? (You don’t need to actually give an algorithm.)

**4.** This problem has three parts.
* (a) State the power method algorithm for finding a dominant eigenvalue and an associated eigenvector of a matrix \(A\). (An eigenvalue \(\lambda_i\) is said to be dominant if \(|\lambda_i|>|\lambda_k|\) for all other \(k\).)
* (b) Show that the power method converges (for almost any starting value) when \(A\) is real symmetric and has a dominant eigenvalue.
* (c) Explain how the inverse power method can be used to find non-dominant eigenvalues and eigenvectors for a matrix \(A\).

**5.** This problem has three parts.
* (a) Give a careful statement of the Gershgorin Circle Theorem.
* (b) Give a careful proof of the Gershgorin Circle Theorem.
* (c) Let \[A=\begin{pmatrix}5&.01&.03\\.02&4&.01\\.03&-.01&4\end{pmatrix}.\] What can you say about the location of the eigenvalues of \(A\)?

## Part II: Numerical Analysis

**6.** This problem has three parts.
* (a) State Newton’s method (the algorithm) for solving \(f(x)=0\), where \(f:\mathbb{R}\to\mathbb{R}\).
* (b) Assuming \(f\) is smooth and we have an initial guess sufficiently close to the root, state sufficient condition(s) for the method to converge quadratically.
* (c) How would you use Newton’s method to compute \(5^{1/3}\)?

**7.** This problem has three parts.
* (a) Give an exact expression for a Lagrange polynomial of degree \(n\) which would interpolate \(n+1\) given data points, \(f(x_k)\).
* (b) Describe the differences between Hermite polynomials and Lagrange polynomials.
* (c) Suppose we have a set of Lagrange polynomials of degree \(2n+1\) which interpolate a smooth function at the points \(x_0,x_0+h,x_1,x_1+h,x_2,x_2+h,\ldots,x_n,x_n+h\). What is the pointwise limit of this interpolant as \(h\to0\)?

**8.** This problem has two parts.
* (a) Describe Romberg’s technique for numerical approximation of an integral (based on the trapezoid rule).
* (b) Give a brief justification of the method.

**9.** Triple Recursion Formula. If \(\{\phi_n(x)\}\) is an orthogonal family of polynomials on \([a,b]\), with weight function \(w(x)\geq0\), and \(n\geq1\), then show that \[\phi_{n+1}(x)=(a_nx+b_n)\phi_n(x)-c_n\phi_{n-1}(x),\] for some constants \(a_n,b_n\), and \(c_n\). (Hint: Let \(g(x)=\phi_{n+1}(x)-a_nx\phi_n(x)\), where \(a_n\) is a constant chosen so that \(g(x)\) has degree \(n\).)

**10.** Let \(\{\phi_k\}\) be a system of orthogonal polynomials, with respect to a non-negative weight \(w(x)\), on \([a,b]\). Show that each of the polynomials \(\phi_k(x)\) must have exactly \(k\) simple zeros in \([a,b]\).
