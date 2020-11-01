guests = {}
disliked_meals_count = 0

line = input().split("-")
while not line[0] == "Stop":
    command = line[0]
    guest = line[1]
    meal = line[2]

    if command == "Like":
        if guest not in guests:
            guests[guest] = [meal]
        else:
            if meal not in guests[guest]:
                guests[guest] += [meal]

    elif command == "Unlike":
        if guest not in guests:
            print(f"{guest} is not at the party.")
        else:
            if meal not in guests[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                guests[guest].remove(meal)
                disliked_meals_count += 1
                print(f"{guest} doesn't like the {meal}.")

    line = input().split("-")


for guest, meals in sorted(guests.items(), key=lambda g: (-len(g[1]), g[0])):
    print(f"{guest}: {', '.join(meals)}")

print(f"Unliked meals: {disliked_meals_count}")