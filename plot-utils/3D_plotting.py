"""
Author: Amanda Manaster
Date: 03/08/2019
Purpose: 3D plotting example
"""
#import packages
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from landlab.plot.imshow import RasterModelGrid

#create simple sloped grid
mg = RasterModelGrid((25,25), 1)
surface = np.ones([625])
z = mg.add_field('topographic__elevation', surface + mg.node_y*0.05, at = 'node')

#create figure
plt.figure()
ax = plt.axes(projection = '3d') #projection is 3d
X = mg.node_x.reshape(mg.shape) #need data in (X,Y,Z)
Y = mg.node_y.reshape(mg.shape)
Z = z.reshape(mg.shape)

ax.plot_surface(X, Y, Z, cmap = 'gist_earth') #plot the surface

#add title, axis labels
plt.title('Example')
ax.set_xlabel('X (m)', fontsize = 10)
ax.set_ylabel('Y (m)', fontsize = 10)
ax.set_zlabel('Elevation (m)', fontsize = 10)
plt.show()