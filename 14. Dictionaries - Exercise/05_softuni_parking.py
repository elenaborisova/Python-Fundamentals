n = int(input())
registered_users = {}

for _ in range(n):
    command_data = input().split()
    command = command_data[0]
    username = command_data[1]

    if command == "register":
        license_plate_number = command_data[2]
        if username in registered_users:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            registered_users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif command == "unregister":
        if username not in registered_users:
            print(f"ERROR: user {username} not found")
        else:
            registered_users.pop(username)
            print(f"{username} unregistered successfully")

for username, plate_number in registered_users.items():
    print(f"{username} => {plate_number}")