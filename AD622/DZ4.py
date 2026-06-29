numbers = [1, 2, 3, 4, 5, 6, 7]

print(numbers)


reverse = []
for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])
print(reverse)


odd = []
for i in range(0, len(numbers), 2):
    odd.append(numbers[i])
print(odd)


even = []
for i in range(1, len(numbers), 2):
    even.append(numbers[i])
print(even)


first = []
first.append(numbers[0])
print(first)


last = []
last.append(numbers[len(numbers) - 1])
print(last)


middle = []
middle.append(numbers[3])
print(middle)


last_three = []
for i in range(4, len(numbers)):
    last_three.append(numbers[i])
print(last_three)


back = []
for i in range(4, 1, -1):
    back.append(numbers[i])
print(back)


center = []
for i in range(2, 5):
    center.append(numbers[i])
print(center)