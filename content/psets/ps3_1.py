import matplotlib.pyplot as plt
import numpy as np
from gaussxw import gaussxw

# Retrive gaussian quadrature points and weights
N=50
x,w = gaussxw(N)

# define the integrand function
def f(x):
    return 

# function to compute cv for a given input temperature
def cv(T):
    """ Compute the heat capacity of a solid at temperature T using the Debye function"""
    # Define constants
    #V = ..           # volume in cubic meters
    #n = ...         # number density of Aluminum
    #thetaD = ..       # Debye temperature of Aluminum (K)
    kB = 1.38065e-23      # Boltzmann's constant (SI units)

    ### your code here

    return

# print heat capacity at room temperature
print("Heat Capacity of Aluminum at room temperature: {} J/K".format(cv(295)))

# main part of the program to plot cv(T)


fig, ax = plt.subplots()
#ax.plot(...)
#ax.set_xlabel(...)
#ax.set_ylabel(...)
#ax.set_title(...)
fig.savefig('Debye_[LASTNAME].png')
