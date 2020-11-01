users = {}

line = input()
while not line == "Statistics":
    tokens = line.split("->")
    command = tokens[0]
    username = tokens[1]

    if command == "Add":
        if username not in users:
            users[username] = []
        else:
            print(f"{username} is already registered")

    elif command == "Send":
        email = tokens[2]
        users[username] += [email]

    elif command == "Delete":
        if username in users:
            users.pop(username)
        else:
            print(f"{username} not found!")

    line = input()


print(f"Users count: {len(users)}")

for username, emails in sorted(users.items(), key=lambda u: (-len(u[1]), u[0])):
    print(username)
    for email in emails:
        print(f"- {email}")
