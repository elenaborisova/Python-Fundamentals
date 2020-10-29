side = float(input())
sheets_count = int(input())
sheet_area = float(input())

box_area = (side * side) * 6
covered_area = 0

for sheet in range(1, sheets_count + 1):
    if sheet % 3 == 0:
        covered_area += sheet_area * 0.25
    else:
        covered_area += sheet_area

covered_percentage = covered_area / box_area * 100
print(f"You can cover {covered_percentage:.2f}% of the box.")


