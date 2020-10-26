RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)

fires = input().split("#")
water_available = int(input())
total_effort = 0
saved_cells = []

for fire in fires:
    fires_cells = fire.split(" = ")
    fire_type = fires_cells[0]
    cell_value = int(fires_cells[1])

    is_valid = (
        (fire_type == "High" and cell_value in RANGE_HIGH) or
        (fire_type == "Medium" and cell_value in RANGE_MEDIUM) or
        (fire_type == "Low" and cell_value in RANGE_LOW)
    )

    if is_valid and water_available >= cell_value:
        water_available -= cell_value
        effort = 0.25 * cell_value
        total_effort += effort
        saved_cells.append(cell_value)

print("Cells:")
for saved_cell in saved_cells:
    print(f"- {saved_cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(saved_cells)}")
