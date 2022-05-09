#Stephanie Bravo
#February 6, 2019
#This program will print different shades of green.

import turtle

turtle.colormode(255)

tortuga = turtle.Turtle()

tortuga.backward(100) #this stops tortuga from running out the screen.

for i in range(0,255,10):
    tortuga.forward(10)
    tortuga.pensize(i)
    tortuga.color(0,i,0)
    
