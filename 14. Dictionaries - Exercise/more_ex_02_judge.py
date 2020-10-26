from collections import defaultdict

users = defaultdict(int)
contests = {}

line = input()
while not line == "no more time":
    username, contest, points = line.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {username: points}
        users[username] += points
    else:
        if username not in contests[contest]:
            contests[contest][username] = points
            users[username] += points
        else:
            prev_points = contests[contest][username]
            if points > prev_points:
                contests[contest][username] = points
                users[username] += points - prev_points

    line = input()

for contest in contests:
    participants = len(contests[contest])
    print(f"{contest}: {participants} participants")
    i = 1
    for participant, points in sorted(contests[contest].items(), key=lambda x: (-x[1], x[0])):
        print(f"{i}. {participant} <::> {points}")
        i += 1

print("Individual standings:")
i = 1
for user, points in sorted(users.items(), key=lambda x: (-x[1], x[0])):
    print(f"{i}. {user} -> {points}")
    i += 1


