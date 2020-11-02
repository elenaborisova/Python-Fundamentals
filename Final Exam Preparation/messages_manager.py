messages = {}
capacity = int(input())

line = input()
while not line == "Statistics":
    tokens = line.split("=")
    command = tokens[0]

    if command == "Add":
        username = tokens[1]
        sent = int(tokens[2])
        received = int(tokens[3])

        if username not in messages:
            messages[username] = {}
            messages[username]["sent"] = sent
            messages[username]["received"] = received

    elif command == "Message":
        sender = tokens[1]
        receiver = tokens[2]

        if sender in messages and receiver in messages:
            messages[sender]["sent"] += 1
            if messages[sender]["sent"] + messages[sender]["received"] == capacity:
                messages.pop(sender)
                print(f"{sender} reached the capacity!")

            messages[receiver]["received"] += 1
            if messages[receiver]["received"] + messages[receiver]["sent"] == capacity:
                messages.pop(receiver)
                print(f"{receiver} reached the capacity!")

    elif command == "Empty":
        username = tokens[1]

        if username == "All":
            messages = {}
        elif username in messages:
            messages.pop(username)

    line = input()


print(f"Users count: {len(messages)}")

for username, messages in sorted(messages.items(), key=lambda x: (-x[1]["received"], x[0])):
    print(f"{username} - {messages['sent'] + messages['received']}")
