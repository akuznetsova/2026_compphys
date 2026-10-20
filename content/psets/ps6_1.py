import matplotlib.pyplot as plt
import numpy as np
# constants
L = 20.  # length (depth) of the system (m)
D = 0.1   # thermal diffusivity 
A = 10.  #sinusoidal variation
B = 12.
tau = 365
T_L = 11.   # constant temperature at the bottom

#N =   # number of grid points
#dx = L/N
#dt =   # time step in days

# set up initial conditions

#def HeatCrust(T0,t0,tf,N,dt):

tmax = 10.01 * 365   # ten years of evolution in days
# times at which we want to see the solution
s1 = 9.25*365
s2 = 9.50*365
s3 = 9.75*365
s4 = 10.0*365


#fig.savefig('crustheat_[LASTNAME].png')
