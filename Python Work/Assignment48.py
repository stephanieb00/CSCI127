#Stephanie Bravo
#April 9, 2019
#This program will ask the user to enter a string and willcontinue prompting the user for a new string until they enter a non-empty string

#Enter a non-empty string:

message = str(input("Enter a non-empty string:"))
#That was empty.  Try again. While Loop
while message == "":
    #Enter a non-empty string:
    print("That was empty.  Try again.")
    message = str(input("Enter a non-empty string:"))
#You entered:
print("You entered:", message)
