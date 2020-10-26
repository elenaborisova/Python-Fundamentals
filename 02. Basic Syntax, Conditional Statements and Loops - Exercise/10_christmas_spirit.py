allowed_quantity = int(input())
days = int(input())

christmas_spirit = 0
total_cost = 0

ornament_set = 0
tree_skirt = 0
tree_garlands = 0
tree_lights = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        allowed_quantity += 2

    if day % 2 == 0:
        ornament_set += 2 * allowed_quantity
        christmas_spirit += 5

    if day % 3 == 0:
        tree_skirt += 5 * allowed_quantity
        tree_garlands += 3 * allowed_quantity
        christmas_spirit += 13

    if day % 5 == 0:
        tree_lights += 15 * allowed_quantity
        christmas_spirit += 17

    if day % 5 == 0 and day % 3 == 0:
        christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        tree_skirt += 5
        tree_garlands += 3
        tree_lights += 15

        if day == days:
            christmas_spirit -= 30


total_cost = ornament_set + tree_lights + tree_skirt + tree_garlands

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
