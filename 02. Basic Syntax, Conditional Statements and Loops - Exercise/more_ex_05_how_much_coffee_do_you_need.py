coffees = 0
overdosed = False
command_lower = ["coding", "movie", "dog", "cat"]
command_upper = ["CODING", "MOVIE", "DOG", "CAT"]

command = input()
while command != "END":

    if command in command_lower:
        coffees += 1
    elif command in command_upper:
        coffees += 2

    if coffees > 5:
        overdosed = True

    command = input()


if overdosed:
    print("You need extra sleep")
else:
    print(coffees)