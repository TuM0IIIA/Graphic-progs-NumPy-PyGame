import turtle

drawing_area = turtle.Screen()
drawing_area.bgcolor('grey')
drawing_area.setup(800, 300)

x=turtle.Turtle()
x.shape('turtle')
x.color('indigo')
x.speed(2)
x.width(5)

A=(-250,-200,-150,-100,-50,0,50,100,150,180,200,250,45,90,135)
def one(*args):
    x.penup()
    x.goto(A[0],A[6])
    x.pendown()
    x.left(A[-3])
    x.goto(A[1],A[7])
    x.right(A[-1])
    x.forward(A[7])
    x.penup()
one()

def two(*args):
    x.goto(A[2],A[7])
    x.pendown()
    x.left(A[5])
    x.forward(A[6])
    x.left(A[-2])
    x.forward(A[6])
    x.left(A[-2])
    x.forward(A[6])
    x.backward(A[7])
    x.penup()
two()

def three(*args):
    x.goto(A[4], A[6])
    x.pendown()
    x.goto(A[5], A[7])
    x.right(A[-6])
    x.forward(A[-8])
    x.penup()
three()

def four(*args):
    x.goto(A[6], A[7])
    x.pendown()
    x.left(A[-2])
    x.forward(A[6])
    x.goto(A[6], A[6])
    x.right(A[-2])
    x.forward(A[6])
    x.penup()
four()

x.goto(150,100)

def fifth(*args):
    x.pendown()
    x.forward(A[7])
    x.left(A[-2])
    x.forward(A[6])
    x.left(A[-2])
    x.forward(A[7])
    x.left(A[-2])
    x.forward(A[6])
    x.penup()
fifth()

x.goto(250,100)
x.left(90)

fifth()

