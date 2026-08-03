from math import sin, cos, pi,sqrt
import numpy as np
g = 9.81
l = 0.4 

def f(r,t):
    """ Evaluates the rhs for a double pendulum system given a vector r

    """
    # ....
    # ... =  -(omega1 * omega1 * sin(2*theta1-2*theta2) + 2 * omega2 * omega2 * sin(theta1-theta2) + (3 * sin(theta1) + sin(theta1 - 2*theta2)) * g/l) / (3. - cos(2*theta1 - 2*theta2))
    # ...  = (4 * omega1 * omega1 * sin(theta1-theta2) + omega2 * omega2 * sin(2*theta1 - 2*theta2) - 2*(sin(theta2) - sin(2*theta1 -theta2)) * g/l) / (3. - cos(2*theta1 - 2*theta2))
    return 

def integrate_RK4(r0,tf,dt):
    ## 
    return


def compute_e(...):
    ###
    return E - E[0]


# r0 = ...
# dt = ...
tf = 10
# ....  = integrate_RK4(r0,tf,dt)

fig,ax = plt.subplots(2, sharex=True,constrained_layout=True)
# ax[0].plot(...,label=r'$\theta_1$')
# ax[0].plot(...,label=r'$\theta_2$')

# plot exact solution
# ax[0].plot(..., color='black',label='single',ls='dashed')
#ax[0].legend()

#ax[1].plot(t,compute_e(..))

ax[1].set_xlabel("time [s]")
ax[0].set_ylabel(r"$\theta(t)$")
ax[1].set_ylabel(r"$\Delta e(t)$ [J]")

fig.savefig("doublependulumtime_[LASTNAME].png")


#fig,ax = plt.subplots(...)
#fig.set_size_inches((6.5,3))


#...set_ylabel(r"$\omega$")
#...set_xlabel(r"$\theta$")

#fig.savefig("doublependulumphase_[LASTNAME].png")
