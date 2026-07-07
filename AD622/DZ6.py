import random


def create_tuple(start, end):
    numbers = []

    for i in range(10):
        numbers.append(random.randint(start, end))

    return tuple(numbers)



tuple1 = create_tuple(0, 5)
tuple2 = create_tuple(-5, 0)


tuple3 = tuple1 + tuple2


count_zero = tuple3.count(0)


print(tuple1)
print(tuple2)
print(tuple3)
print("0 =", count_zero)