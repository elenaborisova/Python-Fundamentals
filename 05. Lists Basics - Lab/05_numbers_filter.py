n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

command = input()

filtered_numbers = []
for number in numbers:
    filter_passes = ( # or instead of ( ) we can use \ on every line
        (command == "even" and number % 2 == 0) or
        (command == "odd" and number % 2 != 0) or
        (command == "negative" and number < 0) or
        (command == "positive" and number >= 0)
    )
    if filter_passes:
        filtered_numbers.append(number)

print(filtered_numbers)
