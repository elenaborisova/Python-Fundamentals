pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
max_health = int(input())
flag = False

tokens = input().split()
while not tokens[0] == "Retire":
    command = tokens[0]

    if command == "Fire":
        index = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                flag = True
                break

    if flag:
        break

    elif command == "Defend":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        damage = int(tokens[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    flag = True
                    break
    if flag:
        break

    elif command == "Repair":
        index = int(tokens[1])
        health = int(tokens[2])
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] + health <= max_health:
                pirate_ship[index] += health
            else:
                pirate_ship[index] = max_health

    elif command == "Status":
        repair_threshold = max_health * 0.2
        need_repair_sections = [section for section in pirate_ship if section < repair_threshold]
        print(f"{len(need_repair_sections)} sections need repair.")

    tokens = input().split()

else:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")

