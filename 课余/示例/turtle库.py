import turtle
t = turtle.Pen()
t.left(36)
t.speed(0)
for j in range(360//6):
    for i in range(5):
        t.forward(200)
        t.left(144)
    t.left(6)
    t.forward(20)
turtle.done()
