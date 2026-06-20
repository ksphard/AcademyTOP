
number = int(input("Введите пятизначное число: "))

a = number // 10000
b = number // 1000 % 10
c = number // 100 % 10
d = number // 10 % 10
e = number % 10

product = a * b * c * d * e

average = (a + b + c + d + e) / 5

print(f"Произведение цифр числа {number}: {product}")
print(f"Среднее арифметическое: {average}")