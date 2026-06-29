start = int(input("Введите начало диапозон: "))
end = int(input("Введите конец диапозона: "))
summa = 0
current = start
while current <= end:
    if current %2 !=0:
        summa = summa + current
    current = current + 1
print("Сумма целых нечетных чисел:", summa)
