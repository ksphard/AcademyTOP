text = input("Введите текст: ")

words = text.lower().split()

count = 0

for word in words:
    if word.startswith("е"):
        count += 1

print("Количество слов:", count)