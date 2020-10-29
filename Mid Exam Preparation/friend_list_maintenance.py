friends = input().split(", ")

tokens = input().split()
while not tokens[0] == "Report":
    command = tokens[0]
    if command == "Blacklist":
        name = tokens[1]
        if name in friends:
            name_index = friends.index(name)
            friends[name_index] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif command == "Error":
        index = int(tokens[1])
        if not friends[index] == "Blacklisted" and not friends[index] == "Lost":
            print(f"{friends[index]} was lost due to an error.")
            friends[index] = "Lost"

    elif command == "Change":
        index = int(tokens[1])
        new_name = tokens[2]
        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name

    tokens = input().split()

print(f"Blacklisted names: {friends.count('Blacklisted')}")
print(f"Lost names: {friends.count('Lost')}")
print(" ".join(friends))
