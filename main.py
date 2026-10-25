import turtle as t


def koch(turtle: t.Turtle, order: int, size: float) -> None:
    """Function, drawing a Koch curve.

    Args:
        turtle: Turtle object used for drawing.
        order: Recursion depth (0 draws a straight segment).
        size: Length of the whole curve.
    """
    if order == 0:
        turtle.forward(size)
        return

    koch(turtle, order - 1, size / 3)
    turtle.left(60)

    koch(turtle, order - 1, size / 3)
    turtle.right(120)

    koch(turtle, order - 1, size / 3)
    turtle.left(60)

    koch(turtle, order - 1, size / 3)


def koch_snowflake(turtle: t.Turtle, order: int, size: float) -> None:
    """Function, drawing a Koch snowflake.

    Moves the turtle to the starting point and draws three Koch
    curves, turning by 120 degrees between them.

    Args:
        turtle: Turtle object used for drawing.
        order: Recursion depth of each Koch curve.
        size: Length of one side of the snowflake.
    """
    x = -(size / 2)
    y = size * 3 ** 0.5 / 4

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    koch(turtle, order, size)
    turtle.right(120)

    koch(turtle, order, size)
    turtle.right(120)

    koch(turtle, order, size)


def minkowski(turtle: t.Turtle, order: int, size: float) -> None:
    """Function, drawing a Minkowski sausage (Minkowski curve).

    Args:
        turtle: Turtle object used for drawing.
        order: Recursion depth (0 draws a straight segment).
        size: Length of the whole curve.
    """
    if order == 0:
        turtle.forward(size)
        return

    minkowski(turtle, order - 1, size / 4)
    turtle.left(90)

    minkowski(turtle, order - 1, size / 4)
    turtle.right(90)

    minkowski(turtle, order - 1, size / 4)
    turtle.right(90)

    minkowski(turtle, order - 1, size / 2)
    turtle.left(90)

    minkowski(turtle, order - 1, size / 4)
    turtle.left(90)

    minkowski(turtle, order - 1, size / 4)
    turtle.right(90)

    minkowski(turtle, order - 1, size / 4)


if __name__ == "__main__":
    screen = t.Screen()
    screen.setup(width=800, height=600)
    screen.tracer(0)

    turtle = t.Turtle()

    minkowski(turtle, 4, 400)

    screen.update()
    t.done()