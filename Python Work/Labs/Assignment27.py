#Stephanie Bravo
#March 12, 2019
#This program will display a bouroughs population.

import matplotlib.pyplot as plt
import pandas as pd

borough = input("Enter borough name:")

filename = input("Enter output file name:")

pop = pd.read_csv("nycHistPop.csv", skiprows=5)

pop['Fraction'] = pop[borough]/pop['Total']

pop.plot(x = "Year", y = "Fraction")

fig = plt.gcf()
fig.savefig(filename)
#plt.show()
