#Stephanie Bravo
#February 20, 2019
#This prograks takes a string as input and uses that string to control what the turtle draes.

import turtle

tortuga = turtle.Turtle()
myWin = turtle.Screen()

commands = input("Please enter a command string:")

for ch in commands:
    if ch == 'F':            #move forward
        tortuga.forward(50)
    elif ch == 'L':          #turn left
        tortuga.left(90)
    elif ch == 'R':          #turn right
        tortuga.right(90)
    elif ch == '^':          #lift pen
        tortuga.penup()
    elif ch == 'v':          #lower pen
        tortuga.pendown()
    elif ch== "B":
        tortuga.backward(50) #Backward 
    elif ch == "S":
        tortuga.stamp() ##stamp
    elif ch == "l":
        tortuga.left(45) ##left
    elif ch == "r":
        tortuga.right(45) ##right
    elif ch == "p":
        tortuga.pencolor("purple") ##pencolor
    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", c)

print("See graphics window for your image")
myWin.exitonclick() ##Close window when clicked
