import turtle as t

from fractals.basic import draw_binary_tree, draw_branch
from fractals.koch import koch, koch_snowflake, minkowski
from fractals.complex import ice_fractal_1, ice_fractal_2, levy, dragon, reset_gradient


def show_menu() -> None:

    print("=== ФРАКТАЛЬНАЯ МАСТЕРСКАЯ ===")
    print("1. Двоичное дерево")
    print("2. Фрактал 'Ветка'")
    print("3. Кривая Коха")
    print("4. Снежинка Коха")
    print("5. Кривая Минковского")
    print("6. Ледяной фрактал №1")
    print("7. Ледяной фрактал №2")
    print("8. Кривая Леви")
    print("9. Дракон Хартера-Хейтуэя")
    print("10. Выход")


def read_int(prompt: str, minimum: int, maximum: int) -> int:
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")
            continue

        if minimum <= value <= maximum:
            return value

        print(f"Ошибка: число должно быть от {minimum} до {maximum}.")


def read_float(prompt: str, minimum: float, maximum: float) -> float:
    while True:
        try:
            user_input = input(prompt).replace(",", ".")
            value = float(user_input)
        except ValueError:
            print("Ошибка: введите число.")
            continue

        if minimum <= value <= maximum:
            return value

        print(f"Ошибка: число должно быть от {minimum} до {maximum}.")


def prepare_turtle(turtle: t.Turtle, x: float, y: float, heading: float) -> None:
    turtle.reset()
    turtle.speed(0)

    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.pendown()


def main():
    screen = t.Screen()
    screen.setup(width=1000, height=800)
    screen.title("Фрактальная мастерская")

    turtle = t.Turtle()
    turtle.speed(0)

    while True:
        show_menu()
        choice = read_int("Выберите пункт меню: ", 1, 10)

        if choice == 10:
            break

        elif choice == 1:
            depth = read_int("Глубина рекурсии (1–10): ", 1, 10)
            size = read_float("Начальный размер (10–300): ", 10, 300)
            angle = read_float("Угол (1–89): ", 1, 89)

            prepare_turtle(turtle, 0, -300, 90)
            draw_binary_tree(turtle, depth, size, angle)

        elif choice == 2:
            depth = read_int("Глубина рекурсии (2–7): ", 2, 7)
            size = read_float("Размер (10–500): ", 10, 500)

            prepare_turtle(turtle, 0, -300, 90)
            draw_branch(turtle, size, depth)

        elif choice == 3:
            order = read_int("Глубина рекурсии (0–5): ", 0, 5)
            size = read_float("Длина кривой (10–700): ", 10, 700)

            prepare_turtle(turtle, -size / 2, 0, 0)
            koch(turtle, order, size)

        elif choice == 4:
            order = read_int("Глубина рекурсии (0–5): ", 0, 5)
            size = read_float("Длина стороны (10–500): ", 10, 500)

            prepare_turtle(turtle, 0, 0, 0)
            koch_snowflake(turtle, order, size)

        elif choice == 5:
            order = read_int("Глубина рекурсии (0–4): ", 0, 4)
            size = read_float("Длина кривой (10–600): ", 10, 600)

            prepare_turtle(turtle, -size / 2, 0, 0)
            minkowski(turtle, order, size)

        elif choice == 6:
            order = read_int("Глубина рекурсии (0–6): ", 0, 6)
            size = read_float("Размер отрезка (1–100): ", 1, 100)

            prepare_turtle(turtle, -400, -100, 0)
            ice_fractal_1(turtle, order, size)

        elif choice == 7:
            order = read_int("Глубина рекурсии (0–6): ", 0, 6)
            size = read_float("Размер отрезка (1–100): ", 1, 100)

            prepare_turtle(turtle, -350, -100, 0)
            ice_fractal_2(turtle, order, size)

        elif choice == 8:
            order = read_int("Глубина рекурсии (0–15): ", 0, 15)
            size = read_float("Размер (10–500): ", 10, 500)

            prepare_turtle(turtle, -60, -100, 0)
            reset_gradient(order)
            levy(turtle, order, size)

        elif choice == 9:
            order = read_int("Глубина рекурсии (0–15): ", 0, 15)
            size = read_float("Размер (10–500): ", 10, 500)

            prepare_turtle(turtle, -60, -100, 0)
            reset_gradient(order)
            dragon(turtle, order, size)

        screen.update()
        input("Нажмите Enter, чтобы вернуться в меню...")

    t.done()


if __name__ == "__main__":
    main()
