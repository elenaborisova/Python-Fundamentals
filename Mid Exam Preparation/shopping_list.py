grocery_list = input().split("!")

tokens = input()
while not tokens == "Go Shopping!":
    args = tokens.split()
    command = args[0]

    if command == "Urgent":
        item = args[1]
        if item not in grocery_list:
            grocery_list.insert(0, item)

    elif command == "Unnecessary":
        item = args[1]
        if item in grocery_list:
            grocery_list.remove(item)

    elif command == "Correct":
        old_item = args[1]
        new_item = args[2]
        if old_item in grocery_list:
            old_item_index = grocery_list.index(old_item)
            grocery_list[old_item_index] = new_item

    elif command == "Rearrange":
        item = args[1]
        if item in grocery_list:
            item_index = grocery_list.index(item)
            grocery_list.append(grocery_list.pop(item_index))

    tokens = input()

print(", ".join(grocery_list))
