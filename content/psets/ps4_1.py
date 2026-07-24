import matplotlib.pyplot as plt
import numpy as np
# define constants
m = 9.1094e-31      # electron mass
e = 1.6022e-19      # electron charge  
V = 20.0            # height of walls in eV
w = 1e-9            # width of the well
hbar = 1.0546e-34   # planck's constant
accuracy = 1e-3

# plot the functions y1, y2, y3
def y1(E):
    return 

def y2(E):
    return 

def y3(E): 
    return 


fig, ax = plt.subplots(1,1, figsize=(7,5))
#ax.plot(..., label='y1 (LHS)',lw=2)
#ax.plot(..., label='y2 (even states)',lw=2)
#ax.plot(..., label='y3 (odd states) ',lw=2)
ax.set_ylim(-10,10)
ax.set_xlabel("E [eV]")
ax.set_ylabel("y(E)")
ax.set_title("Square Well Energies")
ax.legend()


# make guesses
# guesses = ...

# define the two functions that we need to find the roots of
def f_even(E):
    """ 
    square well potential for even states
    """
    return 

def f_odd(E):
    """ square well potential for odd states """
    return 

# function to do binary search
def solve_binary(f,x1,x3,err = accuracy):
    """
    solves for the roots of function given by f using the interval bounds x1 and x3
    returns the location of the energies to the given accuracy, err
    """
    # your code here
    return 0.5*(x1 + x3)

###
# E_even = 
# E_odd = 

# .....
#ax.scatter(E_even, y1(np.array(E_even)),color='black')
#ax.scatter(E_odd, y1(np.array(E_odd)),color='black')
fig.savefig('squarewell_[LASTNAME].png')
