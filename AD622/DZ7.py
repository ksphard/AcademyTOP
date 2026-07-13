
math = ["Matvei", "Evgeniya", "Michail", "Maxim", "Natalia"]


physics = ["Maxim", "Matvei", "Alexandr"]

all_winners = list(set(math + physics))
print("Все призеры:", all_winners)

both = set(math) & set(physics)
print("Призеры обеих олимпиад:", both)

math = both
print("Обновленный список призеров по математике:", math)


del physics