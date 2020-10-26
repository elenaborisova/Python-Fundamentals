submissions = {}
languages_submissions = {}

command = input()
while not command == "exam finished":
    submission = command.split("-")
    username = submission[0]

    if submission[1] == "banned":
        submissions.pop(username)

    else:
        language = submission[1]
        points = int(submission[2])

        if username not in submissions:
            submissions[username] = [points]
        else:
            submissions[username] += [points]

        if language not in languages_submissions:
            languages_submissions[language] = 1
        else:
            languages_submissions[language] += 1

    command = input()

submissions = dict(sorted(submissions.items(), key=lambda x: (-max(x[1]), x[0])))

print("Results:")
for username, points in submissions.items():
    print(f"{username} | {max(points)}")

languages_submissions = dict(sorted(languages_submissions.items(), key=lambda x: (-x[1], x[0])))

print("Submissions:")
for language, count in languages_submissions.items():
    print(f"{language} - {count}")


