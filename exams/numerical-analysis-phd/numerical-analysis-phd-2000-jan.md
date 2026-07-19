# Numerical Analysis PhD exam, January 2000

*Do any 8 of the following 10 problems.*

**1.** This problem has four parts.
* (1) Show: If a matrix \(A \in \mathbb{R}^{n \times n}\) has eigenvalues \(\lambda_1,\ldots,\lambda_n\) such that \(\lambda_i \ne \lambda_j\) for all \(i \ne j\), then the corresponding eigenvectors are linearly independent.
* (2) Show: If a symmetric matrix \(A \in \mathbb{R}^{n \times n}\) has eigenvalues \(\lambda_1,\ldots,\lambda_n\) such that \(\lambda_i \ne \lambda_j\) if \(i \ne j\), then the eigenvectors of \(A\) are orthogonal.
* (3) Show: If the matrix \(A \in \mathbb{R}^{n \times n}\) has \(n\) independent eigenvectors, then the matrix can be diagonalized.
* (4) Show: If \(A \in \mathbb{R}^{n \times n}\) is symmetric, then the matrix can be diagonalized by an orthogonal matrix.

**2.** This problem has three parts.
* (1) Give a careful statement of the singular value decomposition for an arbitrary matrix \(A \in \mathbb{R}^{m \times n}\).
* (2) Give a careful proof of the singular value decomposition.
* (3) Show how the singular value decomposition for \(A\) naturally yields a solution to the least squares problem \(\min_x \|Ax-y\|_2\).

**3.** This problem has three parts.
* (1) Show: If \(w\) is a unit vector in \(\mathbb{R}^n\), then the matrix \(H=I-2ww^t\) is an orthogonal projection.
* (2) Show: If \(w=\frac{x-y}{\|x-y\|}\), \(\|x\|=\|y\|\), and \(H=I-2ww^t\), then \(Hx=y\).
* (3) Given an arbitrary matrix \(A \in \mathbb{R}^{m \times n}\), construct an orthogonal matrix \(Q \in \mathbb{R}^{m \times m}\) and an upper triangular matrix \(R \in \mathbb{R}^{m \times n}\) such that \(A=QR\).

**4.** This problem has three parts.
* (1) Show: If \(\lambda_n\) is the unique eigenvalue of \(A \in \mathbb{R}^{n \times n}\) with largest magnitude and \(x_0\) is chosen arbitrarily in \(\mathbb{R}^n\), then the iteration \(x_k=A^k x_0\) will almost surely converge to a multiple of \(v_n\), the eigenvector associated with \(\lambda_n\).
* (2) If \(\lambda_k\) is a unique eigenvalue which does not have the largest magnitude from among the eigenvalues of \(A\), then describe a method that will compute the eigenvector corresponding to \(\lambda_k\).
* (3) Describe the \(QR\) iteration algorithm for computing the eigenvalues for a matrix \(A \in \mathbb{R}^{n \times n}\). Draw analogues between the \(QR\) method and the power method.

**5.** BACKGROUND: It can be shown that for \(\epsilon\) small there are differentiable functions \(x(\epsilon)\), and \(\lambda(\epsilon)\) such that \((A+\epsilon F)x(\epsilon)=\lambda(\epsilon)x(\epsilon)\), where \(\|F\|_2=1\). Let \(x=x(0)\) be a right eigenvector of \(A\), and \(y\) be a left eigenvector of \(A\).
* (1) If \(A=D+F\), where \(A,D,F \in \mathbb{R}^{n \times n}\) and \(D=\operatorname{diag}(A)\), then state and prove a theorem relating the location of the eigenvalues of \(A\) to the matrices \(D\) and \(F\).
* (2) Show: If \(A,D,F \in \mathbb{R}^{n \times n}\), \(Ax'(0)+Fx=\lambda'(0)x+\lambda x'(0)\).
* (3) Using part (2) above show that \(\left|\lambda'(0)\right|=\left\|\frac{y^tFx}{y^tx}\right\| \le \frac{1}{y^tx}\).
* (4) Explain the implications of (3) to the stability of eigenvalues of symmetric matrices, and highly unsymmetric matrices.

**6.** This problem has five parts.
* (1) Give a careful statement of the error formula for Lagrange interpolation.
* (2) Give a careful proof of the error for formula for Lagrange interpolation.
* (3) Give a careful definition of the Chebyshev Polynomials \(T_n(x)\).
* (4) Give a careful statement of the theorem that shows that the roots of \(T_n(x)\) provide the optimal choice on \([-1,1]\) for Lagrange interpolation.
* (5) For the function \(f(x)=\sin(\pi x)\) defined on \([-1,1]\) and polynomial interpolating function \(p_n(x)\) with interpolating points taken to be the roots of \(T_n(x)\), and tolerance \(\epsilon=0.00001\), find an integer \(n\) such that the interpolating polynomial \(p_n(x)\) has the property that \(|p_n(x)-f(x)|<\epsilon\) for all \(x \in [-1,1]\).

**7.** This problem has two parts.
* (1) Devise a 2nd order method for computing the cube root of a number.
* (2) Show that your method always works.

**8.** This problem has two parts.
* (1) Explain Romberg’s technique for numerical approximation of an integral.
* (2) Discuss the ideas and concepts that explain why the method works.

**9.** This problem has two parts.
* (1) Set up the system of linear equations to be solved when a finite difference approach is used to solve the two point boundary value problem: \(v''+b(x)v'+c(x)v=d(x)\), where \(v(0)=0\) and \(v(1)=0\).
* (2) Set up the system of linear equations to be solved when a collocation approach (with basis functions \(\sin(k\pi x)\)) is used to solve the two point boundary value problem: \(v''+b(x)v'+c(x)v=d(x)\), where \(v(0)=0\) and \(v(1)=0\).

**10.** This problem has three parts.
* (1) Describe the defining properties of the Legendre polynomials on the interval \([-1,1]\).
* (2) Give a careful statement of the theorem fundamental to Gauss Quadrature.
* (3) Show how the Gauss Quadrature method can be used to approximate the integral
  \[\int_0^1 \exp(x^2)\,dx.\]
