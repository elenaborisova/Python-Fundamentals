people_count = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        people_count -= 2

    if day % 15 == 0:
        people_count += 5
        coins -= 2 * people_count

    if day % 3 == 0:
        coins -= 3 * people_count

    if day % 5 == 0:
        coins += 20 * people_count

    coins += 50
    coins -= 2 * people_count

coins_per_person = coins // people_count
print(f"{people_count} companions received {coins_per_person} coins each.")


