import turtle

def red_star(t, side):
    t.fillcolor('red')
    t.pencolor('black')  # to highlight the lines
    t.pendown()
    t.width(3)
    t.begin_fill()
    for i in range(5):
        t.fd(side)
        t.left(72)
        t.forward(side)
        t.right(144)
    t.end_fill()

t = turtle.Turtle()
s = t.screen
s.delay(0)
t.hideturtle()
t.penup()
red_star(t, 50)
s.exitonclick()
s.mainloop()