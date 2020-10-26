numbers = list(map(int, input().split()))

tokens = input()
while not tokens == "end":
    args = tokens.split()
    command = args[0]

    if command == "swap":
        index_one = int(args[1])
        index_two = int(args[2])
        numbers[index_one], numbers[index_two] = numbers[index_two], numbers[index_one]

    elif command == "multiply":
        index_one = int(args[1])
        index_two = int(args[2])
        numbers[index_one] *= numbers[index_two]

    elif command == "decrease":
        numbers = [numbers[i] - 1 for i in range(len(numbers))]

        # for i in range(len(numbers)):
        #     numbers[i] -= 1

    tokens = input()

print(", ".join(map(str, numbers)))
