import turtle

x=turtle.Turtle()
x.begin_fill()
x.shape('turtle')
x.color('yellow')
x.speed(10)
def main_circle(x,side):
    x.forward(side)
    x.left(3)
for i in range(120):
    main_circle(x,10)
x.end_fill()

x.penup()
x.goto(-130,195)
x.color('red','blue')
x.pendown()

x.begin_fill()
x.color('blue')
def main_circle(x,side):
    x.forward(side)
    x.left(3)
for i in range(120):
    main_circle(x,2)
x.end_fill()

x.penup()
x.goto(130,195)
x.color('red','blue')
x.pendown()

x.begin_fill()
x.color('blue')
def main_circle(x,side):
    x.forward(side)
    x.left(3)
for i in range(120):
    main_circle(x,2)
x.end_fill()


x.penup()
x.goto(0,145)
x.color('red','black')
x.pendown()

x.begin_fill()
x.color('black')
def main_circle(x,side):
    x.forward(side)
    x.left(3)
for i in range(120):
    main_circle(x,1)
x.end_fill()

x.penup()
x.goto(-50,20)
x.color('red','red')
x.pendown()

x.begin_fill()
x.color('red')
def main_circle(x,side):
    x.forward(side)
    x.left(15)
for i in range(5):
    main_circle(x,45)
x.end_fill()

