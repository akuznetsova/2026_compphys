import numpy as np
import matplotlib.pyplot as plt

target = 1e-6     # target accuracy
def f(x,c):
    return 
def fprime(x,c):
    return 

def relax(f,c,omega=0,accuracy=target,verbose=True):
    """ function to solve x = f(x) using overrelaxation framework 
    if omega = 0, returns solution with the standard relaxation method"""
    #####
    ### ....
    ####

    # sometimes you want to print and sometimes it's annoying
    if verbose == True:
        print("omega = ", omega, "number of iterations:", i, "x=", x)
    return x

# original relaxation method
relax(f,c=2)

# find optimum overshoot

## your code here

# print results for overshoot that gives half the iterations as before
omega_opt = 'your number goes here'
print('With optimal overshoot, omega ={}:'.format(omega_opt))
relax(f,c=2,omega=omega_opt)

# find and plot x for different values of c
c_vals = np.linspace(0,3,300)
x_vals = np.array([relax(f,c,verbose=False) for c in c_vals])

fig, ax = plt.subplots()
ax.plot(c_vals,x_vals,lw=2)
ax.set_xlabel('c')
ax.set_ylabel('x')
ax.set_title('Solutions for $x = 1 - e^{cx}$')

fig.savefig('relax_[LASTNAME].png')


