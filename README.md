The Lagrange polynomial is one of methods function interpolations.
For computing Lagrange polynomials, it is useful to write them as a linear combination of Lagrange basis polynomials:
$L_{n}=\displaystyle\sum^{n}_{i=1}f(x_{i})\prod ^{n}_{j=1, i\neq j}\frac{x - x_{j}}{x_{i} - x_{j}}$
In this file function LagrangePolynomial has 3 arguments:
 - nodes
 - function values in these nodes
 - set of points from left boundary to right boundary