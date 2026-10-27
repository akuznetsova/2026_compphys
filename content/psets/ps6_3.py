import matplotlib.pyplot as plt
import numpy as np
# from numpy.fft import ...

# load in data
data = np.loadtxt('sunspots.txt',float)
x, y = data[:,0], data[:,1]

# plot the power spectrum
# fig, ax = 

# ax.set_xlabel("k")
# ax.set_ylabel(r"$|c_k|^2$")
# ax.set_title('Sunspot Power Spectrum')
# fig.savefig('_sunspotFT_[LASTNAME].png')

# identify peak frequency
# k_peak = ...
# period_years = 

# print("The dominant sunspot period is {:.2f} years".format(period_years))


def running_average(y, r=5):
    """ Function to calculate a running mean in a window of r points on dataset y"""
    return

# de-trend the data
# trend = running_average(...)
# trend -= trend[0]
# ...

# phase-fold the times
#t0 = ...  initial time offset to phase fold, ideally this is a time at which the detrended sunspot number is at is median baseline
N = 2.0 # N = 2.0 lets you see two period cycles over which it is more obvious if you're on the right track
phase = ((x - t0) / (period_years*12)) % N 

phase_x = np.linspace(0,2,100)
# C = 
# A = 
# sine_curve = 

# plot the data
fig, ax = plt.subplots(1,2, figsize=(8,4),constrained_layout=True, sharey=True)
ax[0].plot(...)
ax[0].set_xlim(0,1000)
ax[0].set_title('Detrended Sunspot Data')
ax[0].set_xlabel("time [months]")
ax[0].set_ylabel("Sunspot number")

# ax[1].scatter(...)
# ax[1].plot(phase_x, sine_curve,color='black',label='model: A = {:.1f}, C = {:.1f}'.format(A,C))
ax[1].legend()
ax[1].set_title('Phase-folded Sunspot Cycle')
ax[1].set_xlabel(r"phase $\phi$")

fig.savefig('_sunspotmodel_[LASTNAME].png')
