n = int(input())
heroes = {}

for _ in range(n):
    hero_data = input().split()
    hero_name = hero_data[0]
    hit_points = int(hero_data[1])
    mana_points = int(hero_data[2])

    heroes[hero_name] = {}
    heroes[hero_name]["HP"] = hit_points
    heroes[hero_name]["MP"] = mana_points


line = input()
while not line == "End":
    tokens = line.split(" - ")
    command = tokens[0]
    hero_name = tokens[1]

    if command == "CastSpell":
        mana_points_needed = int(tokens[2])
        spell_name = tokens[3]

        if heroes[hero_name]["MP"] >= mana_points_needed:
            heroes[hero_name]["MP"] -= mana_points_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(tokens[2])
        attacker = tokens[3]

        heroes[hero_name]["HP"] -= damage
        if heroes[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == "Recharge":
        amount = int(tokens[2])

        if heroes[hero_name]["MP"] + amount > 200:
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['MP']} MP!")
            heroes[hero_name]["MP"] = 200
        else:
            heroes[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif command == "Heal":
        amount = int(tokens[2])

        if heroes[hero_name]["HP"] + amount > 100:
            print(f"{hero_name} healed for {100 - heroes[hero_name]['HP']} HP!")
            heroes[hero_name]["HP"] = 100
        else:
            heroes[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")

    line = input()


for hero_name, hero_points in sorted(heroes.items(), key=lambda x: (-x[1]["HP"], x[0])):
    print(f"{hero_name}\n  HP: {hero_points['HP']}\n  MP: {hero_points['MP']}")
