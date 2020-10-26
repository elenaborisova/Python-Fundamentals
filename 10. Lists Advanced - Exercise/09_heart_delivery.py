neighborhood_hearts = list(map(int, input().split("@")))

line = input()
index = 0
while not line == "Love!":
    command, length = line.split()
    length = int(length)

    index += length
    if index >= len(neighborhood_hearts):
        index = 0

    if neighborhood_hearts[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighborhood_hearts[index] -= 2
        if neighborhood_hearts[index] == 0:
            print(f"Place {index} has Valentine's day.")

    line = input()


print(f"Cupid's last position was {index}.")
if sum(neighborhood_hearts) == 0:
    print("Mission was successful.")
else:
    no_valentines_count = len(list(filter(lambda x: x > 0, neighborhood_hearts)))
    print(f"Cupid has failed {no_valentines_count} places.")