import numpy as np
import matplotlib.pyplot as plt

# define constants
M = 5.97219e24 # Earth mass (kg)
m = 7.34763e22 # Moon mass (kg)
R = 3.844e8 # Earth moon distance (m)
L1 = 3.264e8 # L1 (m)

# set up the problem
# a = 1
# G = 1
# M1 = ..
# M2 = ..
# rcm = ...
# x1,y1 = -rcm, 0
# x2,y2 = x1 + a, 0

def s(x,y,x0=0,y0=0):
    """
    calculate the separation between two points, default (x0=0,y0=0) calculates the distance to the origin
    """
    return np.sqrt((x-x0)**2 + (y-y0)**2)

def Phi(x,y):
    """
    calculate the potential at points x and y
    """
    return 


# set up a grid of points
# N=300
# x = 
# y = 
# .....
# fill potential array 
# Phi_g = ...
# ...

# plot the potential surface
fig,ax = plt.subplots(1)
# im = ax.pcolormesh(..,cmap='magma_r',vmin=1,vmax=2)
# plt.colorbar(im,ax=ax,label=r'$\Phi \ [-3/2 GM_1/a]$')

# plot contours, provided 'levels' restrict the values over which contours are plotted in order to see the features 

# ax.contour(..., levels=np.linspace(1,1.1,30),colors='black',linewidths=1,alpha=0.5)

ax.set_xlabel("x/a")
ax.set_ylabel("y/a")
ax.set_title(r"$\Phi(x,y)$ for Earth-Moon System")
fig.savefig("Lagrange_[LASTNAME].png")

def secant_gradient(f,x0,x1,gamma = 0.1,target=1e-4, N=50):
    """
    calculate extrema using gradient descent, where gamma is a constant of order the reciprocal second derivative
    needs two guesses x0 and x1 to use the numerical derivative (secant method)
    exits after reaching target error or N iterations, whichever comes first
    """
    #### 
    return 

# x0, x1 = starting guesses
# L1 = ...
# ...
# print("The L1 Lagrange point distance from Earth: {:.3e} km".format(L1/1e3))

