#Stephanie Bravo
#March 27, 2019
#This program will  list the top three contributing factors for the primary vehichle of collisions

#Import pandas for reading and analyzing CSV data:
import pandas as pd

#asking user for name of the input file
#csvFile = input("Enter file name:")
tickets = pd.read_csv(collisions2016.csv) 
#tickets = pd.read_csv(csvFile)		#Read in the file to a dataframe

#Print the message: Top three contributing factors for collisions::

print("Top three contributing factors for collisions:")
#"this is the attribute" and 
print(tickets["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
