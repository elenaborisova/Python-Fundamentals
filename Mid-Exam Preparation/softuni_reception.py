first_employee_students_per_hour = int(input())
second_employee_students_per_hour = int(input())
third_employee_students_per_hour = int(input())
total_students_count = int(input())

hours = 0
while total_students_count > 0:
    hours += 1
    if not hours % 4 == 0:
        total_students_count -= first_employee_students_per_hour + second_employee_students_per_hour \
                                + third_employee_students_per_hour


print(f"Time needed: {hours}h.")
