n = int(input())
capacity = 255
total_liters = 0

for _ in range(n):
    liters = int(input())

    if capacity - liters < 0:
        print(f"Insufficient capacity!")
    else:
        capacity -= liters
        total_liters += liters

print(total_liters)
