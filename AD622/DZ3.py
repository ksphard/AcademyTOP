count = int(input("Количество символов: "))
symbol = input("Тип символа: ")
orientation = int(input("Ориентация линии (0 - горизонтальная, 1 - вертикальная): "))

if orientation == 0:
    for i in range(count):
        print(symbol, end=" ")
elif orientation == 1:
    for i in range(count):
        print(symbol)
else:
    print("Ошибка! Неверно указана ориентация.")