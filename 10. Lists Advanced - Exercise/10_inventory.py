def is_item_in_list(items, item):
    if item in items:
        return True
    return False


def collect(items, item):
    if not is_item_in_list(items, item):
        items.append(item)


def drop(items, item):
    if is_item_in_list(items, item):
        items.remove(item)


def combine(items, item):
    old_item, new_item = item.split(":")
    if is_item_in_list(items, old_item):
        old_item_index = items.index(old_item)
        items.insert(old_item_index + 1, new_item)


def renew(items, item):
    if is_item_in_list(items, item):
        item_index = items.index(item)
        items.append(items.pop(item_index))


items = input().split(", ")

line = input()
while not line == "Craft!":
    command, item = line.split(" - ")

    if command == "Collect":
        collect(items, item)

    elif command == "Drop":
        drop(items, item)

    elif command == "Combine Items":
        combine(items, item)

    elif command == "Renew":
        renew(items, item)

    line = input()

print(", ".join(items))
