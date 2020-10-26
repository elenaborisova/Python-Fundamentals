n = int(input())
ships = []
destroyed_ships_count = 0

for _ in range(n):
    row = list(map(int, input().split()))
    ships.append(row)

attacks = input().split()

for attack in attacks:
    args = attack.split("-")
    row = int(args[0])
    col = int(args[1])

    if ships[row][col] > 0:
        ships[row][col] -= 1
        if ships[row][col] == 0:
            destroyed_ships_count += 1

print(destroyed_ships_count)
