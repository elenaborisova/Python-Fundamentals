import math

daily_biscuits_per_worker = int(input())
workers_count = int(input())
total_competitor_biscuits = int(input())
total_biscuits = 0

for day in range(1, 31):
    if day % 3 == 0:
        total_biscuits += math.floor((daily_biscuits_per_worker * workers_count) * 0.75)
    else:
        total_biscuits += daily_biscuits_per_worker * workers_count

print(f"You have produced {total_biscuits} biscuits for the past month.")
if total_biscuits > total_competitor_biscuits:
    difference = total_biscuits - total_competitor_biscuits
    percentage = difference / total_competitor_biscuits * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    difference = total_competitor_biscuits - total_biscuits
    percentage = difference / total_competitor_biscuits * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")
