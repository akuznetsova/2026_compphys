import matplotlib.pyplot as plt
import numpy as np
# Define grid size and number of iterations
Nx= 1000
Ny = Nx
maxiter=100

xmin,ymin = -2, -2
xmax,ymax = 2, 2

####


def is_mandelbrot(c,maxiter=100):
    """
    c: complex number
    maxiter: maximum number of iterations
    """
    ### your code here
    return

#if is_mandelbrot(-1.25 - 0j) < maxiter:
#    print(...)
#else:
#    print(...)

#

fig,ax = plt.subplots(constrained_layout=True)

####

fig.savefig('mandelbrot_[LASTNAME].png')
