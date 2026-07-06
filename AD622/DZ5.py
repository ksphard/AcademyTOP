import math


def rectangle(a, b):
    return a * b


def triangle(a, h):
    return (a * h) / 2


def circle(r):
    return math.pi * r ** 2


print("1 - прямоугольник")
print("2 - треугольник")
print("3 - круг")

choice = int(input("Выберите фигуру: "))

if choice == 1:
    a = float(input("Введите длину: "))
    b = float(input("Введите ширину: "))
    print("Площадь:", rectangle(a, b))

elif choice == 2:
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь:", triangle(a, h))

elif choice == 3:
    r = float(input("Радиус: "))
    print("Площадь:", round(circle(r), 2))

else:
    print("Ошибка! Такой фигуры нет.")