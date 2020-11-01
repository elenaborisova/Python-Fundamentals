heroes = {}

line = input()
while not line == "End":
    tokens = line.split()
    command = tokens[0]
    hero_name = tokens[1]

    if command == "Enroll":
        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif command == "Learn":
        spell_name = tokens[2]

        if hero_name in heroes:
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name] += [spell_name]
        else:
            print(f"{hero_name} doesn't exist.")

    elif command == "Unlearn":
        spell_name = tokens[2]

        if hero_name in heroes:
            if spell_name in heroes[hero_name]:
                heroes[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")

    line = input()


print("Heroes:")
for hero_name, spells in sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"== {hero_name}: {', '.join(spells)}")
