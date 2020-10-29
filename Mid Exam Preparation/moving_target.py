def shoot(index, power, targets):
    if 0 <= index < len(targets):  # if valid
        targets[index] -= power
        if targets[index] <= 0:
            targets.remove(targets[index])

    return targets


def add(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
        return targets
    else:
        print("Invalid placement!")


def strike(index, radius, targets):
    if 0 <= index + radius < len(targets) and 0 <= index - radius < len(targets):  # if valid
        target_to_remove = targets[index]

        for i in range(index + radius, index, -1):
            targets.remove(targets[i])
        for i in range(index - 1, index - radius - 1, -1):
            targets.remove(targets[i])

        targets.remove(target_to_remove)  # !!! remove it by value not by index cause index changes
        return targets
    else:
        print("Strike missed!")


targets = list(map(int, input().split()))

tokens = input().split()
while not tokens[0] == "End":
    command = tokens[0]

    if command == "Shoot":
        index = int(tokens[1])
        power = int(tokens[2])
        shoot(index, power, targets)

    elif command == "Add":
        index = int(tokens[1])
        value = int(tokens[2])
        add(index, value, targets)

    elif command == "Strike":
        index = int(tokens[1])
        radius = int(tokens[2])
        strike(index, radius, targets)

    tokens = input().split()

print("|".join(map(str, targets)))
