numbers = list(map(int, input().split()))

tokens = input().split()
while not tokens[0] == "End":
    command = tokens[0]

    if command == "Switch":
        index = int(tokens[1])
        if 0 <= index < len(numbers):
            numbers[index] *= -1

    elif command == "Change":
        index = int(tokens[1])
        value = int(tokens[2])
        if 0 <= index < len(numbers):
            numbers[index] = value

    elif command == "Sum" and tokens[1] == "Negative":
        negative_nums = [num for num in numbers if num < 0]
        print(sum(negative_nums))

    elif command == "Sum" and tokens[1] == "Positive":
        positive_nums = [num for num in numbers if num >= 0]
        print(sum(positive_nums))

    elif command == "Sum" and tokens[1] == "All":
        print(sum(numbers))

    tokens = input().split()

positive_nums = [num for num in numbers if num >= 0]
print(' '.join(map(str, positive_nums)))
