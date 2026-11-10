import matplotlib.pyplot as plt
import numpy as np

# use numpy random number generator
rng = np.random.default_rng()

def energy(s):
    ''' function to calculate the energy given an MxM state matrix''' 
    return 


def MC_Ising(M,N,T):
    """ function to run a Metropolis simulation of the Ising model for an MxM lattice, of N steps, with temperature T 

    Returns: magnetization over MC steps and final state of lattice spin array"""

    # return M_tot, s

# parameters
M = 20
N = 100000
J = 1.



fig,ax = plt.subplots(1,4,constrained_layout=True,figsize=(8,3),dpi=200)
for T,color in zip(range(1,4),['C0','C1','C2']):
    # mag,spins = MC_Ising(M,N,T)
    # im=ax[T].pcolormesh(spins,cmap='PuOr',vmin=-1,vmax=1)
    # ax[T].set_title('T = {}'.format(T))
    #ax[0].plot(...,label='T = {}'.format(T),color=color)
for a in ax[1:]:
    a.axis('off')
# plt.colorbar(im,ax=ax[-1],label='$s_{i,j}$')
# ax[0].set_ylim(-1,1)

fig.savefig('ising_[LASTNAME].png')
