n = int(input())
students = {}
above_average_students = {}

for _ in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name] += [student_grade]


for student_name, grades in students.items():
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.50:
        above_average_students[student_name] = average_grade

filtered_students = dict(sorted(above_average_students.items(), key=lambda x: -x[1]))

for student_name, average_grade in filtered_students.items():
    print(f"{student_name} -> {average_grade:.2f}")
