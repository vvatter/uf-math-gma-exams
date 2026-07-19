# Numerical Analysis PhD exam, August 2016, Part 2

*You have 2 hours to answer the following questions. You must show all your work as neatly and clearly as possible and indicate the final answer clearly. You may not use a calculator.*

**1.** The iteration
\[
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)-\frac{1}{2}f''(x_n)\frac{f(x_n)}{f'(x_n)}}
\]
for solving the equation \(f(x)=0\) is known as Halley’s method.
* (a) Show that the method can, alternatively, be interpreted as applying Newton’s method to the equation \(g(x)=0\), with \(g(x)=f(x)/\sqrt{f'(x)}\).
* (b) Assuming \(\alpha\) is a simple root of the equation, and \(x_n\to\alpha\) as \(n\to\infty\), show that convergence is at least cubic. Hint: Part (a) might help.

**2.** Do the following parts which are unrelated.
* (a) Derive a Taylor method of order two for the first order initial value problem (IVP)
  \[
  \begin{cases}
  y'=\dfrac{y^2}{1+t},\\
  y(1)=-\dfrac{1}{\ln 2}.
  \end{cases}
  \tag{1}
  \]
* (b) Derive a numerical method for the following second order IVP by replacing the derivatives with centered differences over the mesh \(t_{n+1}=t_n+h\) where \(h=1/N\).
  \[
  \begin{cases}
  y''+2y'+y=\cos t, & 0\le t\le 1,\\
  y(0)=1,\\
  y'(0)=0.
  \end{cases}
  \tag{2}
  \]

**3.** Consider a quadrature rule of the form
\[
\int_0^1 f(x)\,dx\approx Af(0)+Bf'(0)+Cf(\gamma)+Df(1).
\]
* (a) Determine the constants \(A,B,C,D\), and \(\gamma\) so that the quadrature formula has maximum degree of exactness.
* (b) What is the degree of exactness of the formula in part (a)?

**4.** For the function \(f(x)=\ln(x)\) for \(x\in[1,2]\), find the minimax approximation polynomial of degree one. Give the exact value of the minimax error.

**5.** This problem has the following parts.
* (a) Relative to the \(L^2\) norm on the interval \([1,3]\), find the least squares approximation to the function \(f(x)=1/x\) using polynomials of degree at most one.
* (b) Find the least squares error of the approximation above.
