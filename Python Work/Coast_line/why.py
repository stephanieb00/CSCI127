#Stephanie Bravo
#February 25, 2019

import numpy as np
import matplotlib.pyplot as plt

#Read in the data to an array, called elevations:
elevations = np.loadtxt("elevationsNYC.txt")

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
coastMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <=0:
            #less than or equal to zero
            coastMap[row,col,2] = 0.50     #Set the blue channel to 50%
            coastMap[row,col,0] = 0     #Set the red channel to 0%
            coastMap[row,col,1] = 0   #Set the green channel to 0%
        elif elevations[row,col] == 1.0:
            #exactyl 1
            coastMap[row,col,0] = 0.75     #Set the red channel to 75%
            coastMap[row,col,2] = 0.75     #Set the blue channel to 75%
            coastMap[row,col,1] = 0.75   #Set the green channel to 75%
        else:
            coastMap[row,col,0] = 0.50     #Set the red channel to 50%
            coastMap[row,col,2] = 0.50     #Set the blue channel to 50%
            coastMap[row,col,1] = 0.50   #Set the green channel to 50%
#sLoad the flood map image into smatplotlib.pyplot:
##plt.imshow(coastMap)
##
###Display the plot:
##plt.show()

#Save the image:
plt.imsave('coast.png' , coastMap)
