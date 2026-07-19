# Numerical Analysis, first year exam, August 2017

*Do all 5 (five) problems.*

**1.** Let \(f(x)=e^x\).
* (a) Find the linear Taylor polynomial \(T_1(x)\) of \(f(x)\) expanded about \(x_0=1/2\) and give an estimate for the maximum of \(|T_1(x)-f(x)|\) on the interval \([0,1]\).
* (b) Find the linear minimax approximation \(P_1(x)\) to \(f(x)\) on \([0,1]\) and find the maximum error of \(|P_1(x)-f(x)|\) on \([0,1]\).
* (c) Find the linear least squares approximation to \(f\) on \([0,1]\).

**2.** The midpoint method for DE’s is
\[
w_0=\alpha
\]
\[
w_{n+1}=w_n+hf\left(t_n+\frac{h}{2},w_n+\frac{h}{2}f(t_n,w_n)\right).
\]
Apply this method to the IVP, \(y'=\lambda y;\ y(0)=1\), with \(\lambda<0\) and find the constant \(c\) so that \(|h\lambda|<c\) implies that \(w_n\to0\) as \(n\to\infty\).

**3.** Derive this three-point formula for the second derivative.
\[
f''(x_0)=\frac{1}{h^2}\bigl(f(x_0-h)-2f(x_0)+f(x_0+h)\bigr)-\frac{h^2}{12}f^{(4)}(\eta)
\]
for some \(\eta\in[x_0-h,x_0+h]\).

**4.** Let \(f(x)=2^x\) Let \(x_0=-1,x_1=0,x_2=1\). Find the total error bound for the degree two interpolating polynomial \(p_2(x)\) with these nodes and \(f\) on the interval \([-1,1]\), i.e. derive a \(K\) with
\[
\max_{t\in[-1,1]}|f(t)-p_2(t)|<K.
\]

**5.** Let \(g\in C^2([a,b])\) and \(p\in(a,b)\) with \(g(p)=p\), \(g'(p)=0\), \(g''(p)\ne0\).
* (a) Show there is an \(\epsilon>0\) so that for all \(x\in[p-\epsilon,p+\epsilon]\), we have \(g^n(x)\to p\) as \(n\to\infty\).
* (b) With \(\epsilon\) as in part (a), show that for all \(x\in[p-\epsilon,p+\epsilon]\), we have \(|g(x)-p|\le M|x-p|^2\) where \(M=\max\{|g''(x)|:|x-p|\le\epsilon\}/2\).
