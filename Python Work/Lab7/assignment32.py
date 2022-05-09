#Stephanie Bravo
#March 13, 2019
#This program will print out the fraction of children over time. 

import pandas as pd
import matplotlib.pyplot as plt
#Asks the user to specify the input file:
homeless = pd.read_csv(input("Enter name of input file:"))
#Askss the user for the name of the output file:
output= input("Enter name of output file:")

homeless['Fraction Children'] = homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]
#Make a plot of the fraction og the total population that are children over time 
homeless.plot(x = "Date of Census", y = "Fraction Children")

#store plot into output file:
fig = plt.gcf()
fig.savefig(output)
