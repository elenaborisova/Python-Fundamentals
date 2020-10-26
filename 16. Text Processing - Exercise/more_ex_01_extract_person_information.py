n = int(input())

for _ in range(n):
    line = input()
    name_start_index = 0
    name_end_index = 0
    age_start_index = 0
    age_end_index = 0

    for index, char in enumerate(line):
        if char == "@":
            name_start_index = index + 1
        elif char == "|":
            name_end_index = index
        elif char == "#":
            age_start_index = index + 1
        elif char == "*":
            age_end_index = index

    name = line[name_start_index:name_end_index]
    age = line[age_start_index:age_end_index]
    print(f"{name} is {age} years old.")
