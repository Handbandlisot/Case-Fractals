import turtle as t
import colorsys
import math

# Палитра для ледяных фракталов: цвет зависит от уровня ветвления
ICE_COLORS = ["black", "royalblue", "deepskyblue", "mediumturquoise",
              "mediumseagreen", "orange", "crimson"]

# Счётчик для плавного градиента вдоль кривой (Леви, дракон)
_grad = {"i": 0, "n": 1}


def reset_gradient(order: int) -> None:
    """Сбрасывает градиент перед рисованием новой кривой."""
    _grad["i"] = 0
    _grad["n"] = 2 ** order


def _gradient_forward(turtle: t.Turtle, size: float) -> None:
    """Рисует отрезок цветом, зависящим от его номера по ходу кривой."""
    hue = 0.75 * _grad["i"] / max(_grad["n"] - 1, 1)   # от красного к фиолетовому
    turtle.pencolor(colorsys.hsv_to_rgb(hue, 1, 0.9))
    turtle.forward(size)
    _grad["i"] += 1


def ice_fractal_1(turtle: t.Turtle, order: int, size: float, depth: int = 0) -> None:
    """
    «Ледяной» фрактал №1.
    :param turtle: Объект черепашки, используемый для рисования.
    :param order: Глубина рекурсии (порядок фрактала).
    :param size: Длина самого мелкого отрезка (порядок 0).
                 Полная длина основания равна 2**order * size.
    :param depth: Уровень ветвления (для цвета), вручную не задаётся.
    """
    if order == 0:
        turtle.pencolor(ICE_COLORS[depth % len(ICE_COLORS)])
        turtle.forward(size)
    else:
        ice_fractal_1(turtle, order - 1, size, depth)

        turtle.left(90)
        ice_fractal_1(turtle, order - 1, size * 0.5, depth + 1)

        turtle.right(180)
        ice_fractal_1(turtle, order - 1, size * 0.5, depth + 1)

        turtle.left(90)

        ice_fractal_1(turtle, order - 1, size, depth)


def ice_fractal_2(turtle: t.Turtle, order: int, size: float, depth: int = 0) -> None:
    """
    «Ледяной» фрактал №2.
    :param turtle: Объект черепашки, используемый для рисования.
    :param order: Глубина рекурсии (порядок фрактала).
    :param size: Длина самого мелкого отрезка (порядок 0).
                 Полная длина основания равна 2**order * size.
    :param depth: Уровень ветвления (для цвета), вручную не задаётся.
    """
    if order == 0:
        turtle.pencolor(ICE_COLORS[depth % len(ICE_COLORS)])
        turtle.forward(size)
    else:
        ice_fractal_2(turtle, order - 1, size, depth)

        turtle.left(120)
        ice_fractal_2(turtle, order - 1, size * 0.5, depth + 1)

        turtle.right(180)
        ice_fractal_2(turtle, order - 1, size * 0.5, depth + 1)

        turtle.left(120)
        ice_fractal_2(turtle, order - 1, size * 0.5, depth + 1)

        turtle.right(180)
        ice_fractal_2(turtle, order - 1, size * 0.5, depth + 1)

        turtle.left(120)
        ice_fractal_2(turtle, order - 1, size, depth)


def levy(turtle: t.Turtle, order: int, size: float) -> None:
    """
    Кривая Леви (цвет плавно меняется вдоль кривой).
    :param turtle: Объект черепашки, используемый для рисования.
    :param order: Глубина рекурсии (порядок фрактала).
    :param size: Длина базового отрезка.
    """
    if order == 0:
        _gradient_forward(turtle, size)
    else:
        turtle.left(45)
        levy(turtle, order - 1, size / math.sqrt(2))
        turtle.right(90)
        levy(turtle, order - 1, size / math.sqrt(2))
        turtle.left(45)


def dragon(turtle: t.Turtle, order: int, size: float, direction: int = 1) -> None:
    """
    Дракон Хартера-Хейтуэя (цвет плавно меняется вдоль кривой).
    :param turtle: Объект черепашки, используемый для рисования.
    :param order: Глубина рекурсии (порядок фрактала).
    :param size: Длина базового отрезка.
    :param direction: Направление поворота (1 или -1).
    """
    if order == 0:
        _gradient_forward(turtle, size)
    else:
        turtle.left(direction * 45)
        dragon(turtle, order - 1, size / math.sqrt(2), 1)
        turtle.right(direction * 90)
        dragon(turtle, order - 1, size / math.sqrt(2), -1)
        turtle.left(direction * 45)


