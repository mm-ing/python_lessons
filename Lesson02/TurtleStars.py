import turtle

ak = turtle.Turtle()
ak.getscreen().bgcolor("#994444")
ak.speed(10)

ak.penup()
ak.goto((-200,100))
ak.pendown()

def star(turtle,size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
        turtle.end_fill()

star(ak,300)

turtle.done()