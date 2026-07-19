# Complex Analysis, PhD exam, September 1992

*Present the solutions with the necessary details, so the partial credit can be properly assessed. Do all 9 problems.*

**1.** Construct a conformal map which maps the vertical strip \(0<\operatorname{Re} z<1\) onto the upper half-plane.

**2.** The function
\[
f(z)=\sum_{n=1}^{\infty}\frac{z^n}{n^2}
\]
is analytic in the unit circle \(|z|<1\). Can it be continued analytically beyond the circle \(|z|=1\)? Discuss the nature of the singularities (if any) on \(|z|=1\).

**3.** This problem has two parts.
* (a) Show that the function
  \[
  f(z)=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^z}
  \]
  is analytic in \(\operatorname{Re} z>0\).
* (b) Show that it can be analytically continued to the entire complex plane.

**4.** Let \(f(z)\) be analytic in the disc \(|z|\leq 1\). If
\[
|f(z)|\leq 1 \quad\text{for }|z|\leq 1,
\]
prove that
\[
\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}\quad\text{for }|z|\leq 1.
\]

**5.** Let \(F(z)\) be an entire function with the property that \(\operatorname{Re}F(z)\) is bounded from above. Prove that \(F(z)\) is constant.

**6.** Let \(\Omega\) be an open connected subset of \(\mathbb{C}\). Let \(\{f_n\}\) be a sequence of one-to-one analytic functions on \(\Omega\), and assume that \(\{f_n\}\) converges uniformly on any compact subset of \(\Omega\) to a function \(f\). Show that \(f\) is either one-to-one or a constant, and show that both possibilities can occur.

**7.** Suppose that \(f\) is entire, of order \(\rho\). Let \(n(r)\) be the number of zeros (counting the multiplicity) of \(f\) in the disk \(\{z:|z|\leq r\}\). Prove that
\[
\limsup_{r\to\infty}\frac{\log n(r)}{\log r}\leq\rho,
\]
and show, by examples, that equality can happen.

**8.** The expression
\[
\{f,z\}=\frac{f'''(z)}{f'(z)}-\frac{3}{2}\left\{\frac{f''(z)}{f'(z)}\right\}^2
\]
is called the Schwarzian derivative of \(f\). Prove the following:
* (a) If \(f(z)=a(z-z_0)^m+\cdots\), where \(m\) is an integer, then
  \[
  \{f,z\}=A(z-z_0)^{-2}+\cdots.
  \]
* (b) Find the value of \(A\).
* (c) What can you say about \(\{f,z\}\) at the point \(z_0\) if \(m=\pm1\)?

**9.** This problem has two parts.
* (a) Evaluate
  \[
  \frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}\frac{x^z}{z(z+1)}\,dz
  \]
  for \(x>1\).

  Hint: Write the above integral as \(\lim_{t\to\infty}I(t)\), where
  \[
  I(t)=\frac{1}{2\pi i}\int_{2-it}^{2+it}\frac{x^z}{z(z+1)}\,dz,
  \]
  and evaluate \(I(t)\) by using the residue theorem on the rectangle \(2-it\), \(2+it\), \(b+it\), and \(b-it\), where \(b\) is a large negative number.
* (b) What happens if \(0<x<1\)?
