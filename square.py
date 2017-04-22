import turtle


def draw_square():
    ank = turtle.Turtle()
    window = turtle.Screen()

    window.bgcolor("red")
    for i in range(1,37):
        for j in range(1,5):
            ank.forward(100)
            ank.right(90)
        ank.right(10)

    window.exitonclick()


draw_square()
