import matplotlib.pyplot as plt
import numpy as np
# from numpy.linalg import ...

# constants
hbar = 1.0546e-34  # Planck's constant
q = 1.6022e-19     # electron charge
M = 9.1094e-31     # electron mass
L = 5e-10          # width of the well
a = 10*q           # 10 eV
to_print = 10      # number of energies to print


def H(m,n):
    """
    function return an element of the matrix H by index m and n
    """


def Eigenstates(N):
    """ function to calculate the eigen values of an mxn matrix"""


    return eigenvalues, eigenvector

# compute the results for 10x10 matrix
N = 10             
eigenvalues_10, eigenvector_10 = Eigenstates(N)

# print the results
print('For 10x10 matrix:')
for n in range(to_print):
    print('E[%d] = %.3f eV' % (n+1,eigenvalues_10[n]/q))

# compute the results for 100x100 matrix
N = 100
eigenvalues_100, eigenvector_100 = Eigenstates(N)

print('For 100x100 matrix:')
# print the results
for n in range(to_print):
    print('E[%d] = %.3f eV' % (n+1,eigenvalues_100[n]/q))

# plot the first eigenstates
fig, ax = plt.subplots(1,1, figsize=(6,3))

Npoints = 100
x = np.linspace(0,L,Npoints)

###
###
###

ax.set_xlabel("x [nm]")
ax.set_ylabel("PDF")
ax.set_title("Asymmetric Well Potential States")
ax.legend()
fig.savefig("wellpdf_[LASTNAME].png")
