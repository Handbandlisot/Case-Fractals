import turtle
import colorsys
import math

# Палитра для ледяных фракталов: цвет зависит от уровня ветвления
ICE_COLORS = ["black", "royalblue", "deepskyblue", "mediumturquoise",
              "mediumseagreen", "orange", "crimson"]

# Счётчик для плавного градиента вдоль кривой (Леви, дракон)
_grad = {"i": 0, "n": 1}


def _gradient_forward(size: float) -> None:
    """Рисует отрезок цветом, зависящим от его номера по ходу кривой."""
    hue = 0.75 * _grad["i"] / max(_grad["n"] - 1, 1)   # от красного к фиолетовому
    turtle.pencolor(colorsys.hsv_to_rgb(hue, 1, 0.9))
    turtle.forward(size)
    _grad["i"] += 1


def ice_fractal_1(order: int, size: float, depth: int = 0) -> None:
    """
    «Ледяной» фрактал №1.
    :param order: Глубина рекурсии (порядок фрактала).
    :param size: Длина самого мелкого отрезка (порядок 0).
                 Полная длина основания равна 2**order * size.
    :param depth: Уровень ветвления (для цвета), вручную не задаётся.
    """
    if order == 0:
        turtle.pencolor(ICE_COLORS[depth % len(ICE_COLORS)])
        turtle.forward(size)
    else:
        ice_fractal_1(order - 1, size, depth)

        turtle.left(90)
        ice_fractal_1(order - 1, size * 0.5, depth + 1)

        turtle.right(180)
        ice_fractal_1(order - 1, size * 0.5, depth + 1)

        turtle.left(90)

        ice_fractal_1(order - 1, size, depth)


def ice_fractal_2(order: int, size: float, depth: int = 0) -> None:
    """
    «Ледяной» фрактал №2.
    :param order: Глубина рекурсии (порядок фрактала).
    :param size: Длина самого мелкого отрезка (порядок 0).
                 Полная длина основания равна 2**order * size.
    :param depth: Уровень ветвления (для цвета), вручную не задаётся.
    """
    if order == 0:
        turtle.pencolor(ICE_COLORS[depth % len(ICE_COLORS)])
        turtle.forward(size)
    else:
        ice_fractal_2(order - 1, size, depth)

        turtle.left(120)
        ice_fractal_2(order - 1, size * 0.5, depth + 1)

        turtle.right(180)
        ice_fractal_2(order - 1, size * 0.5, depth + 1)

        turtle.left(120)
        ice_fractal_2(order - 1, size * 0.5, depth + 1)

        turtle.right(180)
        ice_fractal_2(order - 1, size * 0.5, depth + 1)

        turtle.left(120)
        ice_fractal_2(order - 1, size, depth)


def levy(order: int, size: float) -> None:
    """
    Кривая Леви (цвет плавно меняется вдоль кривой).
    :param order: Глубина рекурсии (порядок фрактала).
    :param size: Длина базового отрезка.
    """
    if order == 0:
        _gradient_forward(size)
    else:
        turtle.left(45)
        levy(order - 1, size / math.sqrt(2))
        turtle.right(90)
        levy(order - 1, size / math.sqrt(2))
        turtle.left(45)


def dragon(order: int, size: float, direction: int = 1) -> None:
    """
    Дракон Хартера-Хейтуэя (цвет плавно меняется вдоль кривой).
    :param order: Глубина рекурсии (порядок фрактала).
    :param size: Длина базового отрезка.
    :param direction: Направление поворота (1 или -1).
    """
    if order == 0:
        _gradient_forward(size)
    else:
        turtle.left(direction * 45)
        dragon(order - 1, size / math.sqrt(2), 1)
        turtle.right(direction * 90)
        dragon(order - 1, size / math.sqrt(2), -1)
        turtle.left(direction * 45)


def demo(func, order: int, size: float, start: tuple) -> None:
    """Очищает экран, ставит черепашку в start и рисует фрактал."""
    turtle.reset()
    turtle.tracer(0)          # рисуем без анимации, чтобы было быстро
    turtle.pensize(2)
    _grad["i"] = 0
    _grad["n"] = 2 ** order   # число отрезков кривой, нужно для градиента
    turtle.penup()
    turtle.goto(*start)
    turtle.pendown()
    func(order, size)
    turtle.update()           # показываем готовую картинку


if __name__ == "__main__":
    demo(ice_fractal_1, 4, 50, (-400, -100))
    input("Фрактал 1 готов, Enter для следующего...")

    demo(ice_fractal_2, 3, 87, (-350, -100))
    input("Фрактал 2 готов, Enter для следующего...")

    demo(levy, 10, 250, (-60, -100))
    input("Кривая Леви готова, Enter для следующего...")

    demo(dragon, 12, 250, (-60, -100))
    turtle.done()
    