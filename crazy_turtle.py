from random import *
import random as rand
import turtle
def screen(*args):
    drawing_area = turtle.Screen()
    drawing_area.bgcolor('yellow')
    drawing_area.setup(750, 750)

screen()

x = turtle.Turtle()
x.shape('turtle')
x.color('black')
x.speed(10)

def crazy():
    for k in range(1000):
        k = rand.randint(0, 360)
        x.forward(k)
        x.right(k)

crazy()


