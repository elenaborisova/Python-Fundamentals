def is_valid(length, index):
    if 0 <= index < length:
        return True
    return False


def fire(index, damage):
    warship_status[index] -= damage
    return warship_status


def defend(start_index, end_index, damage):
    is_sunk = False
    for index, section in enumerate(pirate_ship_status):
        if start_index <= index <= end_index:
            pirate_ship_status[index] -= damage
            if pirate_ship_status[index] <= 0:
                is_sunk = True
                return is_sunk

    return is_sunk


def repair(index, health):
    if pirate_ship_status[index] + health <= max_health:
        pirate_ship_status[index] += health
    else:
        pirate_ship_status[index] = max_health

    return pirate_ship_status


def pirate_status(pirate_ship_status):
    need_repair_count = 0
    repair_threshold = 0.2 * max_health

    for section in pirate_ship_status:
        if section < repair_threshold:
            need_repair_count += 1

    return need_repair_count


pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
warship_length = len(warship_status)
pirate_length = len(pirate_ship_status)
max_health = int(input())

tokens = input().split()
while not tokens[0] == "Retire":
    command = tokens[0]

    if command == "Fire":
        index = int(tokens[1])
        damage = int(tokens[2])

        if not is_valid(warship_length, index):
            tokens = input().split()
            continue

        result = fire(index, damage)

        if warship_status[index] <= 0:
            print("You won! The enemy ship has sunken.")
            break

    elif command == "Defend":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        damage = int(tokens[3])

        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            is_sunk = defend(start_index, end_index, damage)
            if is_sunk:
                print(f'You lost! The pirate ship has sunken.')
                break

    elif command == "Repair":
        index = int(tokens[1])
        health = int(tokens[2])

        if 0 <= index < len(pirate_ship_status):
            repair(index, health)

    elif command == "Status":
        need_repair_count = pirate_status(pirate_ship_status)
        print(f"{need_repair_count} sections need repair.")

    tokens = input().split()

else: # if no break
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
