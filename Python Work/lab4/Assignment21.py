# Stephanie Bravo
# February 20, 2019
# Takes elevation data of NYC and displays using the default color map


#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt


#Read in the data to an array, called elevations:
elevations = np.loadtxt("elevationsNYC.txt")

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <=0:
            #Below sea level
           floodMap[row,col,2] = 1.0     #Set the blue channel to 1000%
        elif elevations[row,col] <=6:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0] = 1.0     #Set the red channel to 100%
        elif elevations[row,col] <=20:
            #color above the sandy storm surge and less then 20 feet.
            floodMap[row, col, 0] = 0.5
            floodMap[row, col, 1] = 0.5
            floodMap[row, col, 2] = 0.5
        else:
            #Above the 20 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%

###Load the flood map image into matplotlib.pyplot:
##plt.imshow(floodMap)
##
###Display the plot:
##plt.show()

#Save the image:
plt.imsave('floodMap.png', floodMap)
