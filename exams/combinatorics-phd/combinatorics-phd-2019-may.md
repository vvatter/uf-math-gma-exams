# Combinatorics, PhD exam, May 2019

**1.** A bus carrying \(n\) tourists stops at a restaurant. The tourists sit down around an unspecified number of circular tables, then each table orders red wine or white wine. In how many ways can that happen? (Two arrangements are considered identical if everyone has the same left neighbor in both of them.)

**2.** Let \(G\) be a simple graph of order \(n\) such that each vertex has degree at least \((n-1)/2\).
* (a) Prove that the diameter of \(G\) is at most 2.
* (b) Prove that \(G\) has a Hamiltonian path.
* (c) Prove that \(G\) is not planar if \(n>10\).

**3.** Let \(D(z)\) denote the generating function for Dyck paths (where the coefficient of \(z^n\), \([z^n]D(z)\), is the number of Dyck paths on \(2n\) steps).
* (a) Derive a functional equation for \(D(z)\).
* (b) The Lagrange Inversion Formula states that if the formal power series \(f(z)\) is defined implicitly by the equation \(f=z\phi(f)\) for a formal power series \(\phi\) with \(\phi(0)\ne 0\) and \(f(0)=0\) and \(f'(0)\ne 0\), then
  \[
  [z^n]f(z)=\frac{1}{n}[z^{n-1}]\phi^n(z).
  \]
  Use the Lagrange Inversion Formula to obtain a formula for \([z^n]D(z)\).
* (c) Derive a functional equation for the bivariate generating function \(R(z,u)\) which counts Dyck paths according to their length (with the \(z\) variable) and number of returns to the \(x\)-axis (with the \(u\) variable). (Your equation for this part may involve \(D(z)\).)

**4.** A player pays a fixed amount of \(n\) dollars to a casino for the right to participate in the following game. A fair coin is tossed several times until a tail is obtained. If the first tail is obtained as the result of the \(i\)th coin toss, then the player receives a payout of \(2^i\) dollars, and the game ends.
* (a) Assuming that the casino has unlimited resources to pay its obligations and that the player has an unlimited amount of time to play, what is the value of \(n\) that the player should pay for the right to play this game? (We say that the player should pay \(n\) dollars so long as \(n\) is less than the amount of his expected winnings.)
* (b) What is the probability that the casino will pay less than 1000 dollars when the player wins?
* (c) What is the expected value of the player’s payout if the casino has “only” \(10^{14}\) dollars available for payouts? (This is more than the world’s annual GDP.)

**5.** Show that every pentagon with two parallel sides and every hexagon with three pairs of equal parallel sides is the prototile of a monohedral tiling of the plane.

**6.** Recall that for a prime power \(q\), the Gaussian or \(q\)-binomial coefficient \(\genfrac{[}{]}{0pt}{}{n}{k}_q\) is defined to be the number of \(k\) dimensional subspaces of an \(n\)-dimensional vector space over \(\operatorname{GF}(q)\). Equivalently, we can think of \(\genfrac{[}{]}{0pt}{}{n}{k}_q\) as counting \(k\times n\) matrices over \(\operatorname{GF}(q)\) which are in reduced row echelon form and have no all-zero rows. Using either of these interpretations, prove that
\[
\genfrac{[}{]}{0pt}{}{n}{k}_q
=
\genfrac{[}{]}{0pt}{}{n-1}{k-1}_q
+q^k\genfrac{[}{]}{0pt}{}{n-1}{k}_q
\]
for all \(n,k\ge 1\).

**7.** Imagine writing all \(n!\) permutations of length \(n\) in cycle notation on a (large) piece of paper and then randomly selecting one cycle, with each cycle having the same chance to be selected. On average, what will be the length of the selected cycle?

**8.** Sperner’s Theorem states that if \(A\) is an antichain (a family of pairwise incomparable elements) in \(2^{[n]}\) (the power set of \([n]\) ordered by containment), then
\[
|A|\le \binom{n}{\lfloor n/2\rfloor}.
\]
Prove Sperner’s Theorem. (You might consider saturated chains, which are chains of the form \(\emptyset=S_0\subsetneq S_1\subsetneq\cdots\subsetneq S_n=[n]\).)
