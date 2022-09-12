import turtle

turtle.shape('turtle')
turtle.width(5)
turtle.color('grey')
turtle.speed(7)
turtle.pensize(1)
turtle.color('red', 'yellow')

A = [(50, 90, -3, 3), (56, 90, -6, 6), (62, 90, -9, 9), (68, 90, -12, 12), (74, 90, -15, 15), (80, 90, -18, 18)]

for distance, angle, jump1, jump2 in A:
    turtle.forward(distance)
    turtle.right(angle)
    turtle.forward(distance)
    turtle.right(angle)
    turtle.forward(distance)
    turtle.right(angle)
    turtle.forward(distance)
    turtle.right(angle)
    turtle.penup()
    turtle.goto(jump1, jump2)
    turtle.pendown()

turtle.penup()
turtle.forward(250)
turtle.color('red', 'black')
turtle.pendown()

B = [(100, 100, 30), (100, 100, 30), (100, 100, 30), (100, 100, 30), (100, 100, 30), (100, 100, 30), (100, 100, 30),
     (100, 100, 30), (100, 100, 30), (100, 100, 30), (100, 100, 30), (100, 100, 30), ]
for move_forward, move_backward, angle_of_deviation in B:
    turtle.forward(move_forward)
    turtle.stamp()
    turtle.backward(move_backward)
    turtle.right(angle_of_deviation)

