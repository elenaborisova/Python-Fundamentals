elements = input().split()
moves = 0
has_won = False

command = input()
while not command == "end":
    args = command.split()
    index_one = int(args[0])
    index_two = int(args[1])
    moves += 1

    if index_one == index_two or \
            0 > index_one or index_one >= len(elements) \
            or 0 > index_two or index_two >= len(elements):

        new_element = f"-{moves}a"
        middle_index = len(elements) // 2
        elements.insert(middle_index, new_element)
        elements.insert(middle_index, new_element)
        print("Invalid input! Adding additional elements to the board")

    elif elements[index_one] == elements[index_two]:
        print(f"Congrats! You have found matching elements - {elements[index_one]}!")
        element_to_remove = elements[index_one]
        elements.remove(element_to_remove)
        elements.remove(element_to_remove)

    elif not elements[index_one] == elements[index_two]:
        print("Try again!")

    if len(elements) == 0:
        has_won = True
        print(f"You have won in {moves} turns!")
        break

    command = input()

if not has_won:
    print(f"Sorry you lose :(\n"
          f"{' '.join(elements)}")