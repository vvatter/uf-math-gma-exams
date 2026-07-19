# Differential Geometry, PhD exam, May 1992

*Problems 1–4 are Section I; answer three questions from Problems 1–4. Problems 5–7 are Section II; answer each of Problems 5–7.*

**1.** State the preimage (or regular value) theorem. Let \(M\) be the vector space of \(m\times m\) real matrices and \(S\) its subspace of symmetric matrices. By considering the function
\[
F:M\longrightarrow S:A\longmapsto A^tA
\]
or otherwise, show that the orthogonal group \(O(m)\) is naturally a submanifold of \(M\) having dimension \(\frac12m(m-1)\). With which subspace of \(M\) is \(T_IO(m)\) naturally identified?

**2.** What are the integral curves of a vector field? What does it mean to say that a vector field is complete? Show that \(\xi=y^2\frac{\partial}{\partial x}\) and \(\eta=x^2\frac{\partial}{\partial y}\) are complete vector fields on \(\mathbb R^2\) but that \(\xi+\eta\) is not complete. Can the Lie bracket of two different incomplete vector fields be complete? Justify.

**3.** How is the exterior derivative \(d\omega\in\Omega^{k+1}(M)\) of \(\omega\in\Omega^k(M)\) defined? Let \(\omega\) be a volume form on the orientable manifold \(M\) and let \(\xi\) be a vector field on \(M\). Show that \(L_\xi\omega\) is exact and that \(L_\xi\omega=f_\xi\omega\) for some smooth function \(f_\xi\in C(M)\) on \(M\). Find an explicit formula for \(f_\xi\) if
\[
\xi=a_1\frac{\partial}{\partial x_1}+\cdots+a_m\frac{\partial}{\partial x_m}
\]
on \(M=\mathbb R^m\) with \(a_1,\ldots,a_m\in C(\mathbb R^m)\) and \(\omega=dx_1\wedge\cdots\wedge dx_m\) in the usual coordinates. Hence suggest a suitable name for \(f_\xi\) in general.

**4.** Let \(\omega=x\,dy-y\,dx\) be the standard one-form on the unit circle \(S^1\). Let \(f:\mathbb R\longrightarrow S^1\) be the inverse of stereographic projection from \((0,1)\). Compute \(f^*\omega\) and hence show that
\[
\int_{S^1}\omega=2\pi.
\]
How does this calculation establish that \(\omega\) is not exact on \(S^1\)? Is \(f^*\omega\) exact on \(\mathbb R\)? Why?

**5.** Explain what is meant by a Lie group \(G\), its Lie algebra \(\mathfrak g\), and the adjoint representation \(\operatorname{Ad}\) of \(G\) on \(\mathfrak g\). How does the adjoint representation of \(Gl(m,\mathbb R)\) appear in terms of the natural identifications? Show that if \(G\) is connected then the kernel of the adjoint representation coincides with the centre of \(G\). It may be assumed that if \(t\in\mathbb R\), \(g\in G\), and \(\xi\in\mathfrak g\), then
\[
\exp(t\operatorname{Ad}_g\xi)=g(\exp t\xi)g^{-1}.
\]

**6.** Let \((M,\omega)\) be a symplectic manifold. How is the Hamiltonian vector field \(\xi_H\) of \(H\in C(M)\) defined? How is the Poisson bracket defined on \(C(M)\)? Show that if \((p_1,\ldots,p_m,q_1,\ldots,q_m)\) are (local) symplectic coordinates on \(M\), then the integral curves of \(\xi_H\) satisfy the Hamilton equations
\[
\dot q_j=\frac{\partial H}{\partial p_j},\qquad \dot p_j=-\frac{\partial H}{\partial q_j}.
\]
Show also that the Poisson centralizer of \(H\in C(M)\) is precisely the set of all functions on \(M\) constant along integral curves of \(\xi_H\), and suggest a mechanical interpretation of this result.

**7.** Define a geodesic in terms of the Levi-Civita connection \(\nabla\) on the Riemannian manifold \((M,g)\), and give the form taken by the geodesic equation in local coordinates. For the metric \(g\) on the open upper half-plane \(M\) having \(\left\{y\frac{\partial}{\partial x},y\frac{\partial}{\partial y}\right\}\) as orthonormal vector fields, show that the nonzero Christoffel symbols are
\[
\Gamma^y_{yy}=\Gamma^x_{xy}=\Gamma^x_{yx}=-\Gamma^y_{xx}=-\frac1y.
\]
Hence show that vertical upper half-lines and upper semicircles centered on the \(x\)-axis are geodesics. It may be assumed that if \(\xi,\eta,\zeta\) are vector fields on \(M\), then
\[
2g(\nabla_\xi\eta,\zeta)=\xi\cdot g(\eta,\zeta)+\eta\cdot g(\xi,\zeta)-\zeta\cdot g(\xi,\eta)-g(\xi,[\eta,\zeta])-g(\eta,[\xi,\zeta])+g(\zeta,[\xi,\eta]).
\]
