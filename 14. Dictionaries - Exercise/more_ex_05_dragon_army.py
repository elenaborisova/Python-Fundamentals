n = int(input())
dragons = {}

for _ in range(n):
    color, name, damage, health, armor = input().split()
    if damage == "null":
        damage = 45
    else:
        damage = int(damage)
    if health == "null":
        health = 250
    else:
        health = int(health)
    if armor == "null":
        armor = 10
    else:
        armor = int(armor)

    if color not in dragons:
        dragons[color] = {name: [damage, health, armor]}
    else:
        dragons[color][name] = [damage, health, armor]


for color, stats_dict in dragons.items():
    total_values = [0, 0, 0]
    for key, value in stats_dict.items():
        total_values[0] += value[0]
        total_values[1] += value[1]
        total_values[2] += value[2]

    average_values = ["%.2f"%(value / len(stats_dict)) for value in total_values]
    print(f"{color}::({'/'.join(list(map(str, average_values)))})")

    for key, value in sorted(stats_dict.items(), key=lambda x: x[0]):
        print(f"-{key} -> damage: {value[0]}, health: {value[1]}, armor: {value[2]}")
