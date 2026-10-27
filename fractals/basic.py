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
        return

    segment_size = size / (depth + 1)

    for branch_index in range(depth):
        turtle.forward(segment_size)

        # Левая ветка
        turtle.left(45)
        # При вычислении длины учитываем, сколько уровней ветвления осталось
        draw_branch(turtle, 0.5 * segment_size * (depth - branch_index - 1), depth - branch_index - 1)

        # Переход к правой ветке (возвращаемся на 45 вправо, т.е. на исходную)
        turtle.right(45)

        # Правая ветка
        turtle.right(45)
        draw_branch(turtle, 0.5 * segment_size * (depth - branch_index - 1), depth - branch_index - 1)

        # Возврат на ствол (смотрим прямо вверх)
        turtle.left(45)

    turtle.forward(segment_size)
    # Возврат к основанию ствола задним ходом
    turtle.backward(size)

