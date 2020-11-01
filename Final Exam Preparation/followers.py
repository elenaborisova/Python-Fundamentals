followers = {}

line = input()
while not line == "Log out":
    tokens = line.split(": ")
    command = tokens[0]
    username = tokens[1]

    if command == "New follower":
        if username not in followers:
            followers[username] = {}
            followers[username]["likes"] = 0
            followers[username]["comments"] = 0

    elif command == "Like":
        count = int(tokens[2])

        if username not in followers:
            followers[username] = {}
            followers[username]["likes"] = count
            followers[username]["comments"] = 0
        else:
            followers[username]["likes"] += count

    elif command == "Comment":
        if username not in followers:
            followers[username] = {}
            followers[username]["likes"] = 0
            followers[username]["comments"] = 1
        else:
            followers[username]["comments"] += 1

    elif command == "Blocked":
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            followers.pop(username)

    line = input()


print(f"{len(followers)} followers")
for username, follower_data in sorted(followers.items(), key=lambda x: (-x[1]["likes"], x[0])):
    print(f"{username}: {follower_data['likes'] + follower_data['comments']}")
