#Stephanie Bravo
#February 6,2019
#this program take the users image and creates a red and blue channel

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

imagen = plt.imread(input("Enter name of the input file:"))

imagen2 = imagen.copy() #This copies th original image
imagen2[:, :, 1] = 0 #green channel
#imagen2[:, :, 0] = 0 #red channel

plt.imsave(input("Enter name of the output file:"),imagen2)
