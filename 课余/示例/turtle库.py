import turtle
t = turtle.Pen()
t.pensize(3)


def fun(color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    for i in range(4):
        t.forward(200)
        t.left(90)
    t.forward(100)
    t.circle(100)


fun('red', 50, 50)
fun('blue', -250, 50)
fun('black', -250, -250)
fun('green', 50, -250)
turtle.done()
