
n = int(input("Введите количество ворон: "))

if n == 1:
    print("На ветке", n, "ворона")
elif n == 2 or n == 3 or n == 4:
    print("На ветке", n, "вороны")
elif n >= 0 and n <= 9:
    print("На ветке", n, "ворон")
else:
    print("Ошибка ввода данных")