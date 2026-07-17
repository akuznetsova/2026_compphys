import numpy as np
import matplotlib.pyplot as plt

# define constants
# C = 1.         # charge in coulombs
e0 = 8.8542e-12   # permitivity of free space
# L = 1.0            # size of square in meters
#                   # number of points on a side
#                  # grid spacing
eps = 1e-12        # small number to avoid divide by 0


def E_field(d = 0.1):
    """
    function to calculate the electric field between two oppositely charged point charges a distance d away from one another
    at every grid point on a surface plane
    """
    return 


# visualize the potential
fig, ax = plt.subplots(1,1, figsize=(7,5))

# im = ax.pcolormesh(..., vmin=..., vmax=... cmap=...) 
# ax.scatter(...) #plot positions of two charges
cb = fig.colorbar(im, ax=ax, pad=0.01)
cb.set_label('Potential (V)')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')

fig.savefig('_epot_[LASTNAME].png')

# calculate the electric field
# Ex, Ey = np.ones_like(...), np.ones_like(...)

# ...


# plot the magnitude of the E field
# Emag = np.sqrt(Ex**2 + Ey**2)

fig, ax = plt.subplots(1,1, figsize=(7,5))

# ....
# Note: if you're having issues with plotting the directions with quiver, you may want to:
# downsample your data: plot only a subset of your vectors
# rescale your data
fig.savefig('_efield_[LASTNAME].png')
