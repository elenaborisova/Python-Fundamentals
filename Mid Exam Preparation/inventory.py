items = input().split(", ")

tokens = input().split(" - ")
while not tokens[0] == "Craft!":
    command = tokens[0]
    item = tokens[1]

    if command == "Collect":
        if item not in items:
            items.append(item)

    elif command == "Drop":
        if item in items:
            items.remove(item)

    elif command == "Combine Items":
        combine = item.split(":")
        old_item = combine[0]
        new_item = combine[1]

        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)

    elif command == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)

    tokens = input().split(" - ")

print(", ".join(items))