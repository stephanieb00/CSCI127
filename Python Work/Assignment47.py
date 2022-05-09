#Stephanie Bravo
#April 9, 2019
#This program makes a turtle walk 100 times and randomly turns.

import turtle
import random

tortuga = turtle.Turtle()
tortuga.speed(10)

for i in range(100):
    tortuga.forward(10)
    degrees = random.randrange(0,361,1)
    tortuga.right(degrees)
    


