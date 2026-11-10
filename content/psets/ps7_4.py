import matplotlib.pyplot as plt
import numpy as np

# use numpy random number generator
rng = np.random.default_rng()

def f(x):
    return x*x - np.cos(4 * np.pi *x)
def g(x):
    return np.cos(x) + np.cos(np.sqrt(2)*x) + np.cos(np.sqrt(3)*x)

def global_min(x0,func,Tmin,Tmax,tau,xbounds=[-10,10]):
    """ simulated annealing for some function func with parameters Tmin, Tmax, tau, on some range described by xbounds """
    # your code here
    print('Took {} steps to find the minimum at x={}'.format(step,x))
    return 

fig,ax = plt.subplots(1)
# ax.plot(global_min(...))
# ax.set_xlabel('steps')
# ax.set_ylabel(...)
# ax.set_title(r'Simulated Annealing for $f(x) = x^2 - cos(4\pi x)$')
fig.savefig('min1_[LASTNAME].png')



# x0 = 2.0
# max_iter = 10
# for i in range(max_iter):
    #global_min(x0, g, ...)
# print(r"Global minimimum should be at x = {} for y = {}".format(gmin,gval))
