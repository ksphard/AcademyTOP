import json
import csv

# Читаем JSON
with open("todos.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Создаем CSV
with open("todos.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=data[0].keys(),
        delimiter=";",
        lineterminator="\n"
    )

    writer.writeheader()

    for row in data:
        writer.writerow(row)

print("Готово!")