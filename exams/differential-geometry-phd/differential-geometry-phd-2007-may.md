# Differential Geometry, PhD exam, May 2007

*Attempt SIX problems. Write solutions in a neat and logical fashion, giving complete reasons for all steps and stating carefully any substantial theorems used.*

**1.** Decide which of the following are submanifolds of \(\mathbb{R}^3\):
* (a) \(A=\{(x,y,z):z^2=x^2+y^2-1\}\);
* (b) \(B=\{(x,y,z):z^2=x^2+y^2+1\}\);
* (c) \(C=\{(x,y,z):z^2=x^2+y^2\}\).

**2.** Defining the terms involved, prove the Cartan identity
\[
L_\zeta=(\zeta\mathbin{\lrcorner})\circ d+d\circ(\zeta\mathbin{\lrcorner})
\]
for the Lie derivative of differential forms along the vector field \(\zeta\).

**3.** Let \(\theta\in\Omega^1(M)\) be nonsingular (that is, nowhere zero) with \(\theta\wedge d\theta=0\). Briefly explaining why it is possible, choose \(\alpha\in\Omega^1(M)\) such that \(d\theta=\theta\wedge\alpha\) and choose \(\beta\in\Omega^1(M)\) such that \(d\alpha=\theta\wedge\beta\).
* (a) Prove that the three-form \(\alpha\wedge d\alpha\) on \(M\) is closed.
* (b) Prove that if also \(d\theta=\theta\wedge\alpha'\) then \(\alpha'\wedge d\alpha'-\alpha\wedge d\alpha\) is exact.

**4.** Let \(k\in\mathbb{R}\) and define \(\omega_m\in\Omega^m(\mathbb{R}^{m+1}-\{0\})\) by
\[
(x_0^2+\cdots+x_m^2)^k\omega_m=\sum_{j=0}^m(-1)^j x_j\,dx_0\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_m,
\]
where the circumflex over a term indicates that it is omitted.
* (a) Determine the value(s) of \(k\) (if any) for which the \(m\)-form \(\omega_m\) is closed.
* (b) Determine the value(s) of \(k\) (if any) for which the \(2\)-form \(\omega_2\) is exact.

**5.** Define the Poisson bracket between smooth functions on a symplectic manifold, both in invariant form and in terms of (local) Darboux coordinates. Let \(\omega=\sum_{j=1}^3dp_j\wedge dq_j\) be the standard symplectic form on \(\mathbb{R}^6\) and define
\[
L_1=q_2p_3-q_3p_2,\qquad L_2=q_3p_1-q_1p_3,\qquad L_3=q_1p_2-q_2p_1.
\]
Explaining the terms, prove that if \(L_1\) and \(L_2\) are constants of the motion for a given Hamiltonian function on \((\mathbb{R}^6,\omega)\) then so is \(L_3\).

**6.** Let \(G\) be both a group and a smooth manifold; suppose that the group operation \(p:G\times G\to G\) is smooth. By considering the function
\[
f:G\times G\to G\times G:(x,y)\mapsto(x,p(x,y))
\]
or otherwise, prove that the inversion map \(G\to G:g\mapsto g^{-1}\) is smooth. [It may be assumed that the tangent map of \(p\) at \((a,b)\) is given by
\[
\xi\in T_aG,\ \eta\in T_bG\Rightarrow p_*(\xi,\eta)=\lambda_*^a\eta+\rho_*^b\xi,
\]
where \(\lambda^a:G\to G\times G:y\mapsto(a,y)\) and \(\rho^b:G\to G\times G:x\mapsto(x,b)\).]

**7.** Let \(\sigma:G\times M\to M:(g,x)\mapsto\sigma_g(x)\) be a smooth (left) action of the Lie group \(G\) on the smooth manifold \(M\). Explain how the induced map \(\dot{\sigma}:\mathfrak{g}\to\mathrm{Vec}\,M\) is defined. For \(\xi\in\mathfrak{g}\) and \(x\in M\) define
\[
\gamma:\mathbb{R}\to M:t\mapsto\sigma_{\exp(t\xi)}(x).
\]
Show that the tangent vector to this curve at time \(t\) is given by
\[
\dot{\gamma}(t)=(\sigma_{\exp(t\xi)})_*\dot{\gamma}(0).
\]
Hence show that if the action \(\sigma\) is free and \(\dot{\sigma}(\xi)_x=0\) for some \(x\in M\), then \(\xi=0\).
