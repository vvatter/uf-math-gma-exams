# Numerical Analysis, PhD exam, August 2019, Part 2

*Do 4 (four) problems.*

**1.** Consider using Newton’s method to find \(x \in \mathbb{R}^n\) such that \(F(x)=0\), for \(F:D\subseteq\mathbb{R}^n\to\mathbb{R}^n\), where \(D\) is open and convex and \(F\) is continuously differentiable on \(D\).

Suppose \(x^*\) satisfies \(F(x^*)=0\); and \(J(x)\), the Jacobian of \(F\) evaluated at \(x\), satisfies \(\|J^{-1}(x)\|\leq\mu\) for some number \(\mu>0\) for all \(x\) in a convex neighborhood \(N\subseteq D\) that contains \(x^*\).
* (a) Assuming there is a constant \(0<\theta<1\) for which \(\|J(x)-J(y)\|\leq\theta/\mu\) for all \(x,y\in N\), show that \(\{x_k\}\) converges at least linearly to \(x^*\) whenever \(x_0\in N\).
* (b) Assuming there is a constant \(\kappa\) such that \(\|J(y)-J(x)\|\leq\kappa\|y-x\|\) for each \(x,y\in N\), show that \(\{x_k\}\) converges quadratically to \(x^*\) whenever \(x_0\in N\).

**2.** Consider the data points \((x_1,y_1)=(0,-1)\), \((x_2,y_2)=(1,3)\), \((x_3,y_3)=(2,2)\).
* (a) Construct the both the Newton and Lagrange forms of the interpolating polynomial through \((x_1,y_1)\), \((x_2,y_2)\), \((x_3,y_3)\) (each can be left in the form of a linear combination of basis functions, but each basis function and coefficient should be explicitly shown).
* (b) Let \(f(x)=1/x\) and show for \(x_0,\ldots,x_n\neq 0\) that
  \[
  f[x_0,x_1,\ldots,x_n]=(-1)^n\prod_{i=0}^n\frac{1}{x_i}.
  \]

**3.** The third Chebyshev polynomial \(T_3\) is given by \(T_3(x)=4x^3-3x\).
* (a) Find the Chebyshev points on \(-2\leq x\leq 2\).
* (b) Find the global interpolating polynomial on \(-2\leq x\leq 2\) that interpolates \(f(x)=e^x\) at the Chebyshev nodes.
* (c) Suppose you were given 200 pieces of data, equally spaced on \(-2\leq x\leq 2\), and you want to approximate values that lie between data points. Explain what kind of interpolant you would use to fit these data, and why.

**4.** Consider the function
\[
s(x)=\begin{cases}
s_1(x)=(x+1)^3-3x, & -1\leq x\leq 0,\\
s_2(x)=(1-x)^3+3x, & 0\leq x\leq 1.
\end{cases}
\]
* (a) Is \(s(x)\) a cubic spline? If so, what kind?
* (b) The trapezoid rule for numerical integration over \(a\leq x\leq b\) has an error given by
  \[
  \int_a^b f(x)\,dx=I_T-\frac{1}{12}(b-a)^3f''(\eta),\qquad \text{for some }\eta\in(a,b).
  \]
  Determine a bound for the error in the composite trapezoid rule assuming \([a,b]\) is broken up into \(n\) equally spaced intervals of length \(h=(b-a)/n\).
* (c) Use either the midpoint rule or the trapezoid rule with \(n=1\) then \(n=2\) to approximate \(\int_{-1}^1s(x)\,dx\). Explain which rule you chose to use and why.

**5.** Let \(x_0=a\), \(x_1=a+h\) and \(x_2=b=a+2h\), and let \(f\in C^2[a,b]\).
* (a) Construct the difference approximation to \(f''(x_1)\) based on the \(P_2\) interpolant of \(f\) on \([a,b]\) with interpolation points \(x_0,x_1,x_2\) (you should explicitly show how the difference approximation is derived from the interpolant).
* (b) The \(p_2\) difference approximation satisfies \(\left|f''(x_1)-p_2''(x_1)\right|\leq Mh^2/12\), where \(M\) is a constant that depends on \(f\). Suppose the data is noisy and the approximation is based on the values \(f_i\) where \(f_i-f(x_i)=\epsilon_i\) with \(|\epsilon_i|<\epsilon\), \(i=0,1,2\), for a given value of \(\epsilon\). What is the best accuracy with which \(f''(x_1)\) can be approximated? For what value of \(h\) is it attained?
