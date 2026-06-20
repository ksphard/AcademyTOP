# print ( "Hello Python")
# print ( "Привет мир")

#name = "admin"
#print("Hello,", name)
#age = 20
#print (age)
#print(age, type(age))

#a = b= c =1
#print(a, b, c)
#import keyword
#print(keyword.kwlist)
month = int(input("Введите номер месяца: "))
if month == 1 or month == 2 or month == 3:
    print("Зима.")
elif month == 4 or month == 5 or month == 6:
    print("Лето.")
elif month == 7 or month == 8 or month == 9:
    print("Осень.")
elif month == 10 or month == 11 or month == 12:
    print("Зима.")
else:
    print("Ошибка ввода данных")