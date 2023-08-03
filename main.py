from turtle import Turtle, Screen

nyx = Turtle()
screen = Screen()


def move_forward():
    nyx.forward(10)


def move_backwards():
    nyx.backward(10)


def move_left():
    new_heading = nyx.heading() + 10
    nyx.setheading(new_heading)


def move_right():
    new_heading = nyx.heading() - 10
    nyx.setheading(new_heading)


def clear_drawing():
    nyx.clear()
    nyx.penup()
    nyx.home()
    nyx.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_left, "a")
screen.onkey(move_backwards, "s")
screen.onkey(move_right, "d")
screen.onkey(clear_drawing, "c")
screen.exitonclick()

