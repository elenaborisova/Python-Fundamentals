field_size = int(input())
initial_indexes = list(map(int, input().split()))

field = ["0"] * field_size
for initial_index in initial_indexes:
    field[initial_index] = "1"


command = input()
while not command == "end":
    tokens = command.split()
    ladybug_index = int(tokens[0])
    direction = tokens[1]
    fly_length = int(tokens[2])

    if not field[ladybug_index] == "1":
        command = input()
        continue

    elif direction == "right":
        field[ladybug_index] = "0"
        new_index = ladybug_index + fly_length

        while new_index < len(field):
            if field[new_index] == "1":
                new_index += fly_length
            else:
                field[new_index] = "1"
                break

    elif direction == "left":
        field[ladybug_index] = "0"
        new_index = ladybug_index - fly_length

        while new_index > 0:
            if field[new_index] == "1":
                new_index -= fly_length
            else:
                field[new_index] = "1"
                break

    command = input()

print(" ".join(field))
