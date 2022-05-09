#Stephanie Bravo
#March 13, 2019
#This program will ask user for the hour of the day in 24 hour time and print

#checks what the number is and processes it.
def hour(x):
    #"Good Morning" if it is strictly before 12.
    if x < 12:
        print("Good Morning")
    #"Good Afternoon" if it is 12 or greater, but strictly before 17.
    elif x >= 12 and x < 17:
        print("Good Afternoon")
    #"Good Evening" otherwise.
    else:
        print("Good Evening")

#Sets hour to the number user input
hour(int(input("Enter hour (in 24 hour time):")))
