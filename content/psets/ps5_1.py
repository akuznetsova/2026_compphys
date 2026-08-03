import matplotlib.pyplot as plt
import numpy as np


def f(r,t):
    """
    define the function that computes the right hand side (RHS) for the Lotka-Volterra Equations 
    """
    return 

def integrate_RK4(r0,tf,dt):
    """
    integrate the initial conditions (r0) to time tf using the RK4 method with timestep dt
    """

    return 

# define constants
alpha = 1.
beta = gamma = 0.5
delta = 2.

r0 = np.array([2,2],float)   # initial conditions [x=2,y=2]
#
#
#
# print("At t=10, there are {:.3f}k rabbits compared to {:.3f}k foxes".format(...)


fig, ax = plt.subplots(1,1, figsize=(7,5))
#ax.plot(..., label='Rabbits')
#ax.plot(..., label='Foxes')
ax.set_xlim(0,30)
ax.set_xlabel("Time")
ax.set_ylabel("Population [thousand]")
ax.set_title('Rabbits vs. Foxes for equal initial populations')
ax.legend()

fig.savefig("LVpop_[LASTNAME].png")
