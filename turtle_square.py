import turtle


t = turtle.Turtle()


def triangle(x, side):
    x.forward(side)
    x.left(120)


for x in range(3):
    triangle(t, 70)

t.penup()
t.goto(-15,-15)
t.color('red','green')
t.pendown()


def square (x,side):
    x.forward(side)
    x.left(90)

for x in range (4):
     square(t,100)

t.penup()
t.goto(-20,-20)
t.color('blue','blue')
t.pendown()


def square_5 (x,side):
    x.forward(side)
    x.left(72)

for x in range (5):
     square_5(t,110)

t.penup()
t.goto(-30,-30)
t.color('black','blue')
t.pendown()


def square_6 (x,side):
    x.forward(side)
    x.left(60)

for x in range (6):
     square_6(t,130)

t.penup()
t.goto(-40,-40)
t.color('black','blue')
t.pendown()


def square_7 (x,side):
    x.forward(side)
    x.left(52)

for x in range (7):
     square_7(t,150)
