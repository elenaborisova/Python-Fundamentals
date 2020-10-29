cities = {}

cities_data = input()
while not cities_data == "Sail":
    tokens = cities_data.split("||")
    city = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])

    if city not in cities:
        cities[city] = {}
        cities[city]["population"] = population
        cities[city]["gold"] = gold
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

    cities_data = input()


events = input()
while not events == "End":
    tokens = events.split("=>")
    event = tokens[0]
    city = tokens[1]

    if event == "Plunder":
        people = int(tokens[2])
        gold = int(tokens[3])

        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            cities.pop(city)
            print(f"{city} has been wiped off the map!")

    elif event == "Prosper":
        gold = int(tokens[2])

        if gold >= 0:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

    events = input()


if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, city_info in sorted(cities.items(), key=lambda x: (-x[1]["gold"], x[0])):
        print(f"{city} -> Population: {city_info['population']} citizens, Gold: {city_info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
