from math import pi
import numpy as np

## some comparison values
F_sun = 7.3494e7 # W/m2
sig_sb = 5.67e-8 #W/m2/K4

def planck(T):
    """ Function to calculate blackbody flux of a body at temperature T by integrating the Planck function"""
    kB = 1.38065e-23 # boltzmann constant
    hbar = 1.055e-34 # J s
    c = 2.998e8     # speed of lightm/s
    ### 
    return 

# calculate and print solar flux value
print("Solar Flux at T = 6000 K: {:0.3e} W/m^2".format(planck(6000)))

# calculate and print error
# err = ...
#print("Numerical error: ", err)

# calculate and print SB constant
#S B_calc = ...
#print(...)
