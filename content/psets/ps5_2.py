import matplotlib.pyplot as plt
import numpy as np

# define constants
k = 6.  # spring constant
omega = 2.


def f(r,t):
    #...
    return 

def integrate_RK4(N, n, tf):
    """
    Inputs:
    N: number of masses
    n: number of timesteps
    tf: final time
    """

    return 


N = 5   # number of masses

fig, ax = plt.subplots(1,1, figsize=(7,5))

#
#

# print("All masses return to initial positions at: t = {} seconds".format(...))

ax.set_xlabel("Time [s]")
ax.set_ylabel("Displacement [m]")
ax.set_title('5 coupled masses, $m_i = 1$ kg')
ax.legend()

fig.savefig("springs_[LASTNAME].png")
