people = {}

line = input()
while not line == "Results":
    tokens = line.split(":")
    command = tokens[0]

    if command == "Add":
        person_name = tokens[1]
        health = int(tokens[2])
        energy = int(tokens[3])

        if person_name not in people:
            people[person_name] = {}
            people[person_name]["health"] = health
            people[person_name]["energy"] = energy
        else:
            people[person_name]["health"] += health

    elif command == "Attack":
        attacker_name = tokens[1]
        defender_name = tokens[2]
        damage = int(tokens[3])

        if attacker_name in people and defender_name in people:
            people[defender_name]["health"] -= damage
            if people[defender_name]["health"] <= 0:
                people.pop(defender_name)
                print(f"{defender_name} was disqualified!")

            people[attacker_name]["energy"] -= 1
            if people[attacker_name]["energy"] == 0:
                people.pop(attacker_name)
                print(f"{attacker_name} was disqualified!")

    elif command == "Delete":
        username = tokens[1]

        if username == "All":
            people = {}
        elif username in people:
            people.pop(username)

    line = input()


print(f"People count: {len(people)}")

for person, data in sorted(people.items(), key=lambda x: (-x[1]["health"], x[0])):
    print(f"{person} - {data['health']} - {data['energy']}")
