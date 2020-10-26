journey_cost = float(input())
months = int(input())
money_saved = 0

for month in range(1, months + 1):
    if month % 2 == 1 and month != 1:
        money_saved -= money_saved * 0.16

    elif month % 4 == 0:
        money_saved += money_saved * 0.25

    money_saved += 0.25 * journey_cost

if money_saved >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {money_saved - journey_cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {journey_cost - money_saved:.2f}lv. more.")