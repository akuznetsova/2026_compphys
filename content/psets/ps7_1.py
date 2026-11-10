import matplotlib.pyplot as plt
import numpy as np

# use numpy random number generator
rng = np.random.default_rng(seed=23434)
# constants
N = 10000
tauBi = 46. * 60
tauTl = 2.2 * 60
tauPb = 3.3 * 60

def p_decay(tau):
    return 

def decay_chain(N_0,dt=1,tmax=20000):
    nBi = N_0
    nTl = nPb = nD = 0 
    # your code here
    # main loop:

            #print("At time = {} min, there are now {} Bi parent atoms, {} Tl atoms, {} Pb atoms, and {} Bi daughter atoms".format(t/60,nBi, nTl, nPb, nD))
    return

# time, Bi_P, Tl, Pb, Bi_D = decay_chain(N)
fig, ax = plt.subplots(1,1, figsize=(6.5,4))
isotopes = [Bi_P, Tl, Pb, Bi_D]
labels = ['$^{213}$Bi','$^{209}$Tl','$^{209}$Pb','$^{209}$Bi']


ax.set_xlabel("")
ax.set_ylabel("")
ax.set_title(r'Radioactive Decay Chain for $^{213}$Bi')
## 
fig.savefig('decay_[LASTNAME].png')
