contests = {}

line = input()
while not line == "end of contests":
    args = line.split(":")
    contest = args[0]
    password = args[1]

    if contest not in contests:
        contests[contest] = password

    line = input()


users = {}

line = input()
while not line == "end of submissions":
    args = line.split("=>")
    contest = args[0]
    password = args[1]
    username = args[2]
    points = (int(args[3]))
    flag = False

    if contest in contests and password == contests[contest]:
        if username not in users:
            users[username] = [contest, points]

        else:
            for index, value in enumerate(users[username]):
                if contest == value:
                    flag = True
                    if points > int(users[username][index + 1]):
                        users[username][index + 1] = points
                        break
            if flag:
                line = input()
                continue
            else:
                users[username] += [contest, points]

    line = input()


winner = ""
max_points = 0

for user, values in users.items():
    curr_sum = [value for value in values if str(value).isdigit()]
    if sum(curr_sum) > max_points:
        max_points = sum(curr_sum)
        winner = user

print(f"Best candidate is {winner} with total {max_points} points.")
print("Ranking:")

sorted_users = dict(sorted(users.items()))
for user, values in sorted_users.items():
    print(f"{user}")

    course_points = {values[i]: values[i + 1] for i in range(0, len(values), 2)}
    sorted_course_points = dict(sorted(course_points.items(), key=lambda x: -x[1]))

    for contest, points in sorted_course_points.items():
        print(f"#  {contest} -> {points}")
