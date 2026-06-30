import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('millikan.txt')
x = data[:,0]
y = data[:,1]

def fit_lsq(x,y):
    """ 
    Function to calculate the best fit values of the slope m and y-intercept c given the x and y coordinates of a dataset
    by method of least-squares
    """
    ### your code here
    m = 0.0 # replace
    c = 0.0
    return m,c

m,c = fit_lsq(x,y)
print('slope =',m, '[V/Hz]')
print('intercept =',c, '[V]')



fig, ax = plt.subplots()

#####

fig.savefig('_millikan_[LASTNAME].png')

e = 1.602e-19  # coulombs
h = m * e
print('Planck’s constant =',h,'[J/Hz]')
print('Planck’s constant (accepted value) =',6.6261e-34,'[J/Hz]')

#error = ...
#print('Percent error in h {:.2f} %'.format(error))
