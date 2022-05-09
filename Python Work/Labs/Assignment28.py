#Stephanie Bravo
#March 13, 2019
#This program will compute the average and maximimum population over time for a borough chosen by user. 

#imports libraries
import matplotlib.pyplot as plt
import pandas as pd

#Reads file name of the spreadsheet with the data
pop = pd.read_csv("nycHistPop.csv", skiprows=5)

#Asks user for borough name

borough = input("Enter borough:")

#Prints the Average Population
print("Average population:", pop[borough].mean())

#Prints the mMximum Population
print("Maximum population:", pop[borough].max())
