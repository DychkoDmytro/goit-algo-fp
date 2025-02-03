import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    """Рекурсивно малює фрактал 'Дерево Піфагора'"""
    if level == 0:
        return

    # Малюємо початкову вертикальну гілку
    t.forward(branch_length)

    # Зберігаємо позицію та напрямок перед розгалуженням
    pos = t.pos()
    angle = t.heading()

    # Поворот ліворуч і малювання лівої гілки
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Відновлення позиції та напрямку
    t.penup()
    t.goto(pos)
    t.setheading(angle)
    t.pendown()

    # Поворот праворуч і малювання правої гілки
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Повернення у вихідну точку
    t.penup()
    t.goto(pos)
    t.setheading(angle)
    t.pendown()
    t.backward(branch_length)

# Основна функція для запуску програми
def main():
    # Налаштування користувача
    recursion_level = int(input("Введіть рівень рекурсії (1-10): "))

    # Ініціалізація черепашки
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Поворот вгору
    t.penup()
    t.goto(0, -200)  # Початкова позиція
    t.pendown()

    # Малюємо дерево
    draw_pythagoras_tree(t, 100, recursion_level)

    # Завершення програми
    turtle.done()

if __name__ == "__main__":
    main()