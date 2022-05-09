#Stephanie Bravo
#February 13, 2019
#This program runs a image of red and white stripes

import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter the size:"))

output = (input("Enter output file:"))

imagen = np.ones((size,size,3))
imagen[::2,:,1:] = 0 


plt.imsave(output, imagen)
