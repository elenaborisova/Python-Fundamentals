def is_index_valid(targets, index):
    if 0 <= index < len(targets):
        return True
    return False


def shoot(targets, index, value):
    if is_index_valid(targets, index):
        targets[index] -= value
        if targets[index] <= 0:
            targets.pop(index)


def add(targets, index, value):
    if is_index_valid(targets, index):
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike(targets, index, value):
    left_index = index - value
    right_index = index + value

    if 0 <= right_index < len(targets) and 0 <= left_index < len(targets):
        targets = targets[:left_index] + targets[right_index + 1:]
    else:
        print("Strike missed!")
    return targets


targets = list(map(int, input().split()))

line = input()
while not line == "End":
    args = line.split()
    command = args[0]
    index = int(args[1])
    value = int(args[2])

    if command == "Shoot":
        shoot(targets, index, value)

    elif command == "Add":
        add(targets, index, value)

    elif command == "Strike":
        targets = strike(targets, index, value)

    line = input()


print("|".join(list(map(str, targets))))
