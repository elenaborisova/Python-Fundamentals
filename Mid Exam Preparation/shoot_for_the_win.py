targets = list(map(int, input().split()))
shot_targets_count = 0

command = input()
while not command == "End":
    index = int(command)

    if 0 <= index < len(targets) and targets[index] != -1:  # if index is valid and not already shot
        for i in range(len(targets)):
            if targets[i] > targets[index] and i != index and targets[i] != -1:  # if greater, not the same, and not shot
                targets[i] -= targets[index]
            elif targets[i] <= targets[index] and i != index and targets[i] != -1:
                targets[i] += targets[index]

        targets[index] = -1
        shot_targets_count += 1

    command = input()

print(f"Shot targets: {shot_targets_count} -> {' '.join(map(str, targets))}")