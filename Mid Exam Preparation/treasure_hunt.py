treasure_chest = input().split("|")

tokens = input().split()
while not tokens[0] == "Yohoho!":
    command = tokens[0]

    if command == "Loot":
        for i in range(1, len(tokens)):
            item = tokens[i]
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif command == "Drop":
        index = int(tokens[1])
        if 0 <= index < len(treasure_chest):
            treasure_chest.append(treasure_chest.pop(index))

    elif command == "Steal":
        count = int(tokens[1])
        stolen_items = []

        for i in range(len(treasure_chest) - 1, len(treasure_chest) - count - 1, -1):
            stolen_items.append(treasure_chest.pop(i))
            if not treasure_chest:  # if empty
                break

        print(", ".join(reversed(stolen_items)))

    tokens = input().split()

if treasure_chest:  # if not empty
    items_length = [len(item) for item in treasure_chest]
    average_gain = sum(items_length) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")
