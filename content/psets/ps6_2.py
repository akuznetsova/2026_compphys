import matplotlib.pyplot as plt
import numpy as np
from dcst import dst, idst

# constants
L = 1e-8
N = 1000
dx = L/N
m = 9.109e-31
hbar = 1.055e-34


x0 = L/2
sigma = 1e-10
kappa = 5e10
x = np.linspace(0,L-dx,N)

# create arrays for the real/imaginary parts
#

# initial conditions


# perform the forward transforms to calculate alpha_k and eta_k



def realwave(t):
    """ evaluate the real part of the wavefunction at the desired time t """
    return 

dt = 1e-16

#fig, ax = ...

#fig.suptitle(r'Particle in a Box $\psi(x,t)$')
#fig.savefig('_spectralwave_LASTNAME.png')
