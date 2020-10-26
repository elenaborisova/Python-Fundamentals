courses = {}

line = input()
while not line == "end":
    course_data = line.split(" : ")
    course_name = course_data[0]
    student_name = course_data[1]

    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name] += [student_name]

    line = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
for course, students in sorted_courses.items():
    print(f"{course}: {len(students)}")

    sorted_students = list(sorted(students))
    for student in sorted_students:
        print(f"-- {student}")

