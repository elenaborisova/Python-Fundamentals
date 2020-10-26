days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0

for day in range(1, days + 1):
    total_plunder += daily_plunder

    if day % 3 == 0:
        total_plunder += daily_plunder * 0.5

    if day % 5 == 0:
        total_plunder -= total_plunder * 0.3

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    difference = expected_plunder - total_plunder
    percentage = difference / expected_plunder * 100
    print(f"Collected only {100 - percentage:.2f}% of the plunder.")
