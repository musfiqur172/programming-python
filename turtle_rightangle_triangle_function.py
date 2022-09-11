import turtle


def triangle(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

    turtle.exitonclick()


triangle(100)