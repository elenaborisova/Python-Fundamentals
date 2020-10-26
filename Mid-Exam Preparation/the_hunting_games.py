days = int(input())
players_count = int(input())
group_energy = float(input())
daily_water_per_person = float(input())
daily_food_per_person = float(input())
total_water = daily_water_per_person * days * players_count
total_food = daily_food_per_person * days * players_count

for day in range(1, days + 1):
    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    if day % 2 == 0:
        group_energy += 0.05 * group_energy
        total_water -= 0.3 * total_water

    if day % 3 == 0:
        total_food -= total_food / players_count
        group_energy += group_energy * 0.1

else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")