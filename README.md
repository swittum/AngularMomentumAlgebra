# AngularMomentumAlgebra (SU(2)/SO(3))
The commutation relations for the Lie Algebras of SU(2) and SO(3) can in natural units be expressed as 
$$ [L_i, L_j] = \mathrm{i}\epsilon_{ijk}L_k.$$
The casimir element of this algebra is given by the square of the total momentum operator, i.e.
$$L^2 = \sum_i L_i^2.$$
A common way of deriving the representations of this algebra is by the usage of the ladder operators defined as 
$$L_\pm = L_x\pm\mathrm{i}L_y.$$
The script AngularMomentum.py follows this method, providing a representation for every value of the quantum number of total angular momentum $l$. For a use example, see the notebook file AngularMomentum.ipynb.
