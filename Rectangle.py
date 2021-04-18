import turtle
t = turtle.Turtle()

for i in range(0,4):
    if i % 2 == 0:
        t.forward(100)
    else:
        t.forward(50)
    t.left(90)

turtle.done()
