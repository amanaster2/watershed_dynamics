"""
Author: Amanda Manaster
Date: 03/12/2019
Purpose: Create animation of figures using ImageMagick

Note: must install ImageMagick to save animation. 
https://imagemagick.org/script/download.php
"""

#import packages
import matplotlib.pyplot as plt 
import matplotlib.image as mgimg
from matplotlib import animation
import numpy as np

#add ImageMagick exe to path to save animations
plt.rcParams['animation.convert_path'] = r'C:\Program Files\ImageMagick-7.0.8-Q16\magick.exe'

#initialize figure
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

#create empty list for images 
myimages = []

#create array to loop through - should correspond to num of images
T = np.arange(0,1100,50)

#loops through images
for i in range(len(T)):

    #read in figure
    fname = 'C:/Users/Amanda/Desktop/3DFigs/year%i.png' % T[i] #this is where your images are saved
    img = mgimg.imread(fname) #read in images
    imgplot = plt.imshow(img) #plot

    #append image to the list
    myimages.append([imgplot])

#animate using mpl.animation.ArtistAnimation
my_anim = animation.ArtistAnimation(fig, myimages)

#define writer to save animation
writer = animation.ImageMagickFileWriter(fps = 2)

#save animation
my_anim.save('C:/Users/Amanda/Desktop/test.gif', writer=writer, dpi = 300)
