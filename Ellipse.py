import turtle
t = turtle.Turtle()

t.seth(-45)
#t.seth(45)
r = 100

for i in range(0,2):
    t.circle(r, 90)
    t.circle(r // 2, 90)

turtle.done()
