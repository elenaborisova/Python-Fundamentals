steps_made = int(input())
one_step_length_cm = float(input())
target_distance_meters = int(input())
distance_travelled_cm = 0

for step in range(1, steps_made + 1):
    if step % 5 == 0:
        distance_travelled_cm += one_step_length_cm * 0.7  # its 30% shorter than usual
    else:
        distance_travelled_cm += one_step_length_cm

distance_travelled_meters = distance_travelled_cm / 100
percentage_travelled = distance_travelled_meters / target_distance_meters * 100
print(f"You travelled {percentage_travelled:.2f}% of the distance!")

