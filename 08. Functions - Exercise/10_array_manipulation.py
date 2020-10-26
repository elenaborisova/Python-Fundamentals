def exchange(numbers, index):
    numbers = numbers[index + 1:] + numbers[:index + 1]
    return numbers


def find_max_even_index(numbers):
    evens = [num for num in numbers if num % 2 == 0]

    if evens:  # if not empty
        max_even = max(evens)

        result = None
        for index, num in enumerate(numbers):  # to find the rightmost one
            if num == max_even:
                result = index
        print(result)
    else:
        print("No matches")


def find_max_odd_index(numbers):
    odds = [num for num in numbers if num % 2 == 1]

    if odds:  # if not empty
        max_odd = max(odds)

        result = None
        for index, num in enumerate(numbers):
            if num == max_odd:
                result = index
        print(result)
    else:
        print("No matches")


def find_min_even_index(numbers):
    evens = [num for num in numbers if num % 2 == 0]

    if evens:  # if not empty
        min_even = min(evens)

        result = None
        for index, num in enumerate(numbers):
            if num == min_even:
                result = index
        print(result)
    else:
        print("No matches")


def find_min_odd_index(numbers):
    odds = [num for num in numbers if num % 2 == 1]

    if odds:  # if not empty
        min_odd = min(odds)

        result = None
        for index, num in enumerate(numbers):
            if num == min_odd:
                result = index
        print(result)
    else:
        print("No matches")


def get_first_count_even(numbers, count):
    if count <= len(numbers):
        evens = [num for num in numbers if num % 2 == 0]
        result = [evens[i] for i in range(count) if i < len(evens)]
        print(result)
    else:
        print("Invalid count")


def get_first_count_odd(numbers, count):
    if count <= len(numbers):
        odds = [num for num in numbers if num % 2 == 1]
        result = [odds[i] for i in range(count) if i < len(odds)]
        print(result)
    else:
        print("Invalid count")


def get_last_count_even(numbers, count):
    if count <= len(numbers):
        evens = [num for num in numbers if num % 2 == 0]

        result = []
        counter = 0
        for i in range(len(evens) - 1, -1, -1):
            result.append(evens[i])
            counter += 1
            if count == counter:
                break

        result.reverse()
        print(result)
    else:
        print("Invalid count")


def get_last_count_odd(numbers, count):
    if count <= len(numbers):
        odds = [num for num in numbers if num % 2 == 1]

        result = []
        counter = 0
        for i in range(len(odds) - 1, -1, -1):
            result.append(odds[i])
            counter += 1
            if count == counter:
                break

        result.reverse()
        print(result)
    else:
        print("Invalid count")


numbers = list(map(int, input().split()))

line = input().split()
while not line[0] == "end":
    command = line[0]

    if command == "exchange":
        index = int(line[1])
        if 0 <= index < len(numbers):
            numbers = exchange(numbers, index)
        else:
            print("Invalid index")

    elif command == "max":
        if line[1] == "even":
            find_max_even_index(numbers)
        elif line[1] == "odd":
            find_max_odd_index(numbers)

    elif command == "min":
        if line[1] == "even":
            find_min_even_index(numbers)
        elif line[1] == "odd":
            find_min_odd_index(numbers)

    elif command == "first":
        count = int(line[1])

        if line[2] == "even":
            get_first_count_even(numbers, count)

        elif line[2] == "odd":
            get_first_count_odd(numbers, count)

    elif command == "last":
        count = int(line[1])

        if line[2] == "even":
            get_last_count_even(numbers, count)
        elif line[2] == "odd":
            get_last_count_odd(numbers, count)

    line = input().split()

print(numbers)
