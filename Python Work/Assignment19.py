#Stephanie Bravo
#February 20, 2019
#This program asks the user for the number of hours untill weekend. prints out days and leftover hours.

hours = int(input("Enter number of hours:"))

days = hours//24

print("Days:", days)

leftover = hours%24

print("Hours:", leftover)
