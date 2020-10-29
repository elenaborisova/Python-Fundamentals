fires_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
put_out_cells = []

for fire_cell in fires_cells:
    tokens = fire_cell.split(" = ")
    fire_type = tokens[0]
    cell_value = int(tokens[1])

    if fire_type == "High" and 81 <= cell_value <= 125:
        if water - cell_value >= 0:
            water -= cell_value
            effort += 0.25 * cell_value
            total_fire += cell_value
            put_out_cells.append(cell_value)

    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        if water - cell_value >= 0:
            water -= cell_value
            effort += 0.25 * cell_value
            total_fire += cell_value
            put_out_cells.append(cell_value)

    elif fire_type == "Low" and 1 <= cell_value <= 50:
        if water - cell_value >= 0:
            water -= cell_value
            effort += 0.25 * cell_value
            total_fire += cell_value
            put_out_cells.append(cell_value)

    if water == 0:
        break

print("Cells:")
result = [print(f" - {cell}") for cell in put_out_cells]
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
