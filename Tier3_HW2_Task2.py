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

# Вказуємо рівень рекурсії
recursion_level = 3  

# Малюємо три сторони сніжинки Коха
for i in range(3):
    koch_snowflake(t, recursion_level, 300)
    t.right(120)


turtle.done()
