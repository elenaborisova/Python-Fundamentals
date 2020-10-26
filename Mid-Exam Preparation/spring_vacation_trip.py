days = int(input())
group_budget = float(input())
people_count = int(input())
fuel_per_km = float(input())
daily_food_cost_per_person = float(input())
room_price_per_night_per_person = float(input())

distance_cost = 0
hotel_expenses = room_price_per_night_per_person * people_count * days
food_expenses = daily_food_cost_per_person * people_count * days

if people_count > 10:
    hotel_expenses -= hotel_expenses * 0.25

total_expenses = hotel_expenses + food_expenses + distance_cost

for day in range(1, days + 1):
    daily_travelled_distance_km = float(input())
    distance_cost = daily_travelled_distance_km * fuel_per_km
    total_expenses += distance_cost

    if day % 3 == 0 or day % 5 == 0:
        total_expenses += total_expenses * 0.4

    if day % 7 == 0:
        total_expenses -= total_expenses / people_count

    if total_expenses > group_budget:
        print(f"Not enough money to continue the trip. You need {total_expenses - group_budget:.2f}$ more.")
        break
else:
    print(f"You have reached the destination. You have {group_budget - total_expenses:.2f}$ budget left.")


