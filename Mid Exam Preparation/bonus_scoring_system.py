import math

students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())
max_bonus_student = 0
max_attendance_student = 0

for student in range(students_count):
    attendance = int(input())
    total_bonus = attendance / lectures_count * (5 + initial_bonus)

    if total_bonus > max_bonus_student:
        max_bonus_student = total_bonus
        max_attendance_student = attendance

print(f"Max Bonus: {math.ceil(max_bonus_student)}.")
print(f"The student has attended {max_attendance_student} lectures.")