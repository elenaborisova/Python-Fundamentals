events = input().split("|")
energy = 100
coins = 100

for event in events:
    name, number = event.split("-")
    number = int(number)

    if name == "rest":
        if energy + number <= 100:
            energy += number
            print(f"You gained {number} energy.")
        else:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        print(f"Current energy: {energy}.")

    elif name == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        coins -= number
        if coins > 0:
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            break
else:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
