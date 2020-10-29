neighborhood = list(map(int, input().split("@")))
curr_index = 0

command = input().split()
while not command[0] == "Love!":
    length = int(command[1])

    if curr_index + length < len(neighborhood):
        curr_index += length
    else:
        curr_index = 0

    if neighborhood[curr_index] == 0:
        print(f"Place {curr_index} already had Valentine's day.")
    else:
        neighborhood[curr_index] -= 2
        if neighborhood[curr_index] == 0:
            print(f"Place {curr_index} has Valentine's day.")

    command = input().split()

print(f"Cupid's last position was {curr_index}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    no_valentine_houses = [house for house in neighborhood if house > 0]
    print(f"Cupid has failed {len(no_valentine_houses)} places.")