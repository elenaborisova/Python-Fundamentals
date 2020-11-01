n = int(input())
plants = {}

for _ in range(n):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = int(plant_info[1])

    plants[plant] = {}
    plants[plant]["rarity"] = rarity
    plants[plant]["rating"] = []


command_input = input()
while not command_input == "Exhibition":
    tokens = command_input.split(": ")
    command = tokens[0]

    if command == "Rate":
        plant, rating = tokens[1].split(" - ")
        if int(rating) < 0 or plant not in plants:
            print("error")
            command_input = input()
            continue

        plants[plant]["rating"] += [int(rating)]

    elif command == "Update":
        plant, new_rarity = tokens[1].split(" - ")
        if int(new_rarity) < 0 or plant not in plants:
            print("error")
            command_input = input()
            continue

        plants[plant]["rarity"] = int(new_rarity)

    elif command == "Reset":
        plant = tokens[1]
        if plant in plants:
            plants[plant]["rating"] = []
        else:
            print("error")

    else:
        print("error")

    command_input = input()


for plant in plants:
    if sum(plants[plant]["rating"]) > 0 and len(plants[plant]["rating"]) > 0:
        average_rating = sum(plants[plant]["rating"]) / len(plants[plant]["rating"])
        plants[plant]["rating"] = average_rating
    else:
        plants[plant]["rating"] = 0

print("Plants for the exhibition:")
for plant, plant_data in sorted(plants.items(), key=lambda p: (p[1]["rarity"], p[1]["rating"]), reverse=True):
    print(f"- {plant}; Rarity: {plant_data['rarity']}; Rating: {plant_data['rating']:.2f}")
