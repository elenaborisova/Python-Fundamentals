numbers = input().split()

tokens = input().split()
while not tokens[0] == "END":
    command = tokens[0]

    if command == "Change":
        painting_number = tokens[1]
        changed_number = tokens[2]
        if painting_number in numbers:
            painting_index = numbers.index(painting_number)
            numbers[painting_index] = changed_number

    elif command == "Hide":
        painting_number = tokens[1]
        if painting_number in numbers:
            numbers.remove(painting_number)

    elif command == "Switch":
        painting_number = tokens[1]
        second_painting_number = tokens[2]
        if painting_number in numbers and second_painting_number in numbers:
            first_index = numbers.index(painting_number)
            second_index = numbers.index(second_painting_number)
            numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]

    elif command == "Insert":
        place = int(tokens[1])
        painting_number = tokens[2]
        if 0 <= place + 1 <= len(numbers):
            numbers.insert(place + 1, painting_number)

    elif command == "Reverse":
        numbers.reverse()

    tokens = input().split()

print(" ".join(numbers))