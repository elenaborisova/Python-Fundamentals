energy = int(input())
won_battles = 0

command = input()
while not command == "End of battle":
    distance = int(command)

    if energy - distance >= 0:
        energy -= distance
        won_battles += 1
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break

    if won_battles % 3 == 0:
        energy += won_battles

    command = input()

else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")