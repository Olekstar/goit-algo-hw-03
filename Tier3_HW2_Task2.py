import turtle

# Функція для малювання сніжинки Коха
def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

# Ініціалізація Turtle
window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.color("blue")

# Встановлення початкової позиції
t.penup()
t.goto(-150, 90)
t.pendown()

# Отримання рівня рекурсії від користувача
recursion_level = int(input("Введіть рівень рекурсії (ціле число): "))

# Малюємо три сторони сніжинки Коха
for i in range(3):
    koch_snowflake(t, recursion_level, 300)
    t.right(120)


turtle.done()