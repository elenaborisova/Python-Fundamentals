animals = input()

animals_list = animals.split(", ")
sheep_count = 0

for i in range(len(animals_list) - 1, -1, -1):
    animal = animals_list[i]
    if animal == "wolf" and i == len(animals_list) - 1:
        print("Please go away and stop eating my sheep")
    elif animal == "sheep":
        sheep_count += 1
    elif animal == "wolf":
        print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
        break
