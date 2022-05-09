#CSci 127 Teaching Staff
#October 2018
#Count which cars got the most parking tickets

#Import pandas for reading and analyzing CSV data:
import pandas as pd

#asking user for name of the input file
csvFile = input("Enter file name:")
tickets = pd.read_csv(csvFile)		#Read in the file to a dataframe

#Ask the user for the attribute (column header) to search by.
attribute = input("Enter attribute:")

#Print the message The 10 worst offenders are:

print("The 10 worst offenders are:")

#Print 10 worst & number of tickets
print(tickets[attribute].value_counts()[:10])
