start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

summa = 0

if start % 2 == 0:
    start += 1

while start <= end:
    summa += start
    start += 2

print("Сумма нечетных чисел =", summa)