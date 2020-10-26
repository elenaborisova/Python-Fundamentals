targets = list(map(int, input().split("|")))
points = 0

tokens = input().split("@")
while not tokens[0] == "Game over":
    command = tokens[0]

    if command == "Shoot Left":
        start_index = int(tokens[1])
        length = int(tokens[2])

        if 0 <= start_index < len(targets):
            # if start_index - length < 0:
            #     current_index = (start_index - length) % len(targets)
            # else:
            #     current_index = start_index - length
            #
            # if targets[current_index] >= 5:
            #     targets[current_index] -= 5
            #     points += 5
            # elif 0 < targets[current_index] < 5:
            #     points += targets[current_index]
            #     targets[current_index] = 0

            for i in range(length):
                start_index -= 1
                if start_index == -len(targets):
                    start_index = 0

            if targets[start_index] < 5:
                points += targets[start_index]
                targets[start_index] = 0
            else:
                targets[start_index] -= 5
                points += 5

    elif command == "Shoot Right":
        start_index = int(tokens[1])
        length = int(tokens[2])
        if 0 <= start_index < len(targets):
            # if start_index + length > len(targets):
            #     current_index = (start_index + length) % len(targets)
            # else:
            #     current_index = start_index + length
            # if targets[current_index] >= 5:
            #     targets[current_index] -= 5
            #     points += 5
            # elif 0 < targets[current_index] < 5:
            #     points += targets[current_index]
            #     targets[current_index] = 0

            for i in range(length):
                if start_index == len(targets) - 1:
                    start_index = 0
                else:
                    start_index += 1

            if targets[start_index] < 5:
                points += targets[start_index]
                targets[start_index] = 0
            else:
                targets[start_index] -= 5
                points += 5

    elif command == "Reverse":
        targets.reverse()

    tokens = input().split("@")

targets = list(map(str, targets))
print(" - ".join(targets))
print(f"Iskren finished the archery tournament with {points} points!")

