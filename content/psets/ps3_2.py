import matplotlib.pyplot as plt
import numpy as np
from gaussxw import gaussxw
# Gaussian points/weights
# ...

# potential function
def V(x):
    return x**4

# function to calculate the period for a given amplitude
def P(a):
    """
    Function that calculates the period of an anharmonic oscillator given some amplitude a using the Gaussian Quadrature method
    """
    # ....
    return 

# print value for a = 1
print("For $a=1$, the period is",P(1))

# main program to make plot

fig, ax = plt.subplots()
#ax.plot(...)
# ...
# ....
fig.savefig('anharmonic_[LASTNAME].png')
