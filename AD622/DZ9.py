def counter(city):
    count = 0

    def visit():
        nonlocal count
        count += 1
        print(city, count)

    return visit


moscow = counter("Москва")
sochi = counter("Сочи")

moscow()
moscow()
sochi()
sochi()
moscow()