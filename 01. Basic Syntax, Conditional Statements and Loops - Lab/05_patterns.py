GROW = 1
SHRINK = -1

desired_size = int(input())
direction = GROW
current_size = 0

while (current_size < desired_size and direction == GROW) or (direction == SHRINK and current_size > 0):
    current_size += direction
    print("*" * current_size)

    if desired_size == current_size:
        direction = SHRINK
