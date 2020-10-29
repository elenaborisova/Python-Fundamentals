def potion_command(health, number):
    if health + number <= 100:
        health += number
        print(f"You healed for {number} hp.")
    else:
        print(f"You healed for {100 - health} hp.")
        health = 100

    print(f"Current health: {health} hp.")
    return health


def chest_command(number, bitcoins):
    bitcoins += number
    print(f"You found {number} bitcoins.")
    return bitcoins


def monster_attack(command, health, number, index):
    health -= number
    if health > 0:
        print(f"You slayed {command}.")
    else:
        print(f"You died! Killed by {command}.")
        print(f"Best room: {index}")
    return health


dungeons_rooms = input().split("|")
health = 100
bitcoins = 0

for index, room in enumerate(dungeons_rooms, start=1):
    tokens = room.split()
    command = tokens[0]
    number = int(tokens[1])

    if command == "potion":
        health = potion_command(health, number)

    elif command == "chest":
        bitcoins = chest_command(number, bitcoins)

    else:
        health = monster_attack(command, health, number, index)
        if health <= 0:
            break
else:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

