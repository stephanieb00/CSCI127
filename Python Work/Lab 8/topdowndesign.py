#Intro Programming Lab:  A program with a herd of turtles

import turtle

#welcome message
def welcomeMessage():
    print()
    print("Welcome to our herd of turtles demonstration!")
    print()

#ask the user for the number of turtles
def getInput():
    n = eval(input("Please enter the number of turtles: "))
    return(n)

#Set Up Screen
def setUpScreen():
    w = turtle.Screen()
    w.bgcolor("green")
    return w

#Set Up Turtles
def setUpTurtles(n):
    tList = []
    #Create turtles:
    for i in range(n):
        t = turtle.Turtle()
        #Make the turtle appear turtle-shaped
        t.shape("turtle")       
        tList.append(t)
        
    #Changes Color to blue default and default direction
    for i in range(n):
        tList[i].color(0,0,i/(2*n)+.5)
        tList[i].right(i*360/n)

    return tList

#Move the turtle forward
def moveForward(tList):
     for t in tList:
        t.forward(30)

#Stamp
def stamp(tList):
    for t in tList:
        t.stamp()

#Main
def main():
    #Writes a welcome message to the shell
    welcomeMessage()
    #Ask for number of turles
    numTurtles = getInput()
    #Set up a green turtle window
    w = setUpScreen()
    #Make a list of turtles, different colors
    turtleList = setUpTurtles(numTurtles)
    #Loop
    for i in range(10):
        #Move each turtle in the list forward
        moveForward(turtleList)
        #Stamp where the turtle stopped
        stamp(turtleList)       

if __name__ == "__main__":
    main()
