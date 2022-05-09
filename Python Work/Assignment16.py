#Stephanie Bravo
#Febraury 8, 2019
#This program uses the users 5 integers and the turtle will move said integer degrees left.

import turtle

tortuga = turtle.Turtle()

for i in range(5):
    d = input("Enter a number:")
    tortuga.left(d)
    tortuga.forward(100)
              
