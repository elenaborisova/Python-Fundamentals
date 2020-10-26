lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0

for lost_fight in range(1, lost_fights_count + 1):
    if lost_fight % 2 == 0:
        expenses += helmet_price

    if lost_fight % 3 == 0:
        expenses += sword_price

    if lost_fight % 6 == 0: # % 2 and % 3
        expenses += shield_price

    if lost_fight % 12 == 0: # every second time his shield brakes (6 * 2)
        expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
