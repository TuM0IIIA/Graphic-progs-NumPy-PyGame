import turtle

drawing_area = turtle.Screen()
drawing_area.bgcolor('orange')
drawing_area.setup(800, 500)

border = turtle.Turtle()
border.hideturtle()
border.width(5)
border.color('green')
border.penup()
border.goto(-1000, -500)
border.pendown()
border.goto(1000, -500)

x = turtle.Turtle()
x.shape('circle')
x.color('black')

x.width(2)
x.penup()
x.goto(-800, 0)
x.pendown()
x.speed_x = 30
x.speed_y = 0

gravitation = 14

while True:

    print(x.speed_y, x.position())
    x.speed_y = x.speed_y - gravitation
    x.goto(x.xcor() + x.speed_x, x.ycor() + x.speed_y)

    if x.ycor() <= -450:
        x.speed_y = -x.speed_y
    #if x.xcor() >= 1500 or x.xcor() <= -900:  In case u need side borders use this loop
    #    x.speed_x = -x.speed_x

