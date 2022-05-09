#Stephanie Bravo
#March 20, 2019
#This program will print the upper right corner of the photo


#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

#Input image
imagen = plt.imread(input("Enter image file name:"))

#Setting height to the hegit of the image
height = imagen.shape[0]

#Setting width to the width of the image
width = imagen.shape[1]
#copying the original image to create the second one we are going to edit
imagen2 = imagen.copy()

#Cropping to show the upper right
imagen2= imagen[:height//2, width//2:]

#Saving image
plt.imsave(input("Enter output file:"),imagen2)

