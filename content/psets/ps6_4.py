import matplotlib.pyplot as plt
import numpy as np
from math import pi
# from numpy.fft import ...
sigma = 25

x = np.loadtxt('blur.txt',float)

# make a plot of the original image
fig, ax = plt.subplots(1,2, figsize=(6,3))
im = ax[0].imshow(x, cmap='gray') 

# compute the point spread function (PSF)

# psf = ...
# hint: make a plot of the PSF to check it


# fourier transform the picture and the PSF


# divide one by the other


# invert the transform and plot the new image


#for a in ax:
#    a.axis('off')

#ax[0].set_title(r'Blurred Image, $\sigma=25$')
#ax[1].set_title('Deconvolved Image')
#fig.savefig('_deblur_[LASTNAME].png')
