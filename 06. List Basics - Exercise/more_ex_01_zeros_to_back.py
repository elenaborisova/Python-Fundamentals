strings = input().split(", ")
numbers = []
zeros_count = 0

for string in strings:
    numbers.append(int(string))

for i in range(len(numbers) - 1, -1, -1):
    element = numbers[i]
    if element == 0:
        zeros_count += 1
        numbers.remove(0)

for i in range(zeros_count):
    numbers.append(0)

print(numbers)

