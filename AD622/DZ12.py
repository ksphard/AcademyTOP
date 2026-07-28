
with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

pos1 = 1
pos2 = 2

lines[pos1], lines[pos2] = lines[pos2], lines[pos1]

with open("text.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

print("Строки успешно поменяны местами")