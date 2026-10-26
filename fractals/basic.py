import turtle as t

def draw_binary_tree(turtle: t.Turtle, depth: int, size: float, angle: float) -> None:
    """
    Рисует рекурсивное двоичное дерево.
    :param turtle: Объект черепашки, используемый для рисования.
    :param depth: Глубина рекурсии.
    :param size: Длина ветки на текущем уровне рекурсии.
    :param angle: Угол отклонения дочерних веток от родительской ветки.
    """
    if depth == 0:
        turtle.forward(size)
        turtle.backward(size)

    else:
        turtle.forward(size)

        turtle.right(angle)
        draw_binary_tree(turtle, depth - 1, size / 2, angle)

        turtle.left(2 * angle)
        draw_binary_tree(turtle, depth - 1, size / 2, angle)

        turtle.right(angle)
        turtle.backward(size)


def draw_branch(turtle: t.Turtle, size, depth):
    """
    Рисует рекурсивный фрактал «Ветка».
    :param turtle: Объект черепашки, используемый для рисования.
    :param size: Длина центральной ветки на текущем уровне рекурсии.
    :param depth: Глубина рекурсии и количество точек ветвления.
    """
    if depth == 0:
        turtle.left(180)
        return

    x = size / (depth + 1)
    for i in range(depth):
        turtle.forward(x)
        turtle.left(45)
        draw_branch(turtle, 0.5 * x * (depth - i - 1), depth - i - 1)
        turtle.left(90)
        draw_branch(turtle, 0.5 * x * (depth - i - 1), depth - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)

