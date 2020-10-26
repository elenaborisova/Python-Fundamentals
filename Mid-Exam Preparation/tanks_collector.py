owned_tanks = input().split(", ")
n = int(input())

for _ in range(n):
    tokens = input().split(", ")
    command = tokens[0]

    if command == "Add":
        tank_name = tokens[1]
        if tank_name in owned_tanks:
            print("Tank is already bought")
        else:
            print("Tank successfully bought")
            owned_tanks.append(tank_name)

    elif command == "Remove":
        tank_name = tokens[1]
        if tank_name in owned_tanks:
            print("Tank successfully sold")
            owned_tanks.remove(tank_name)
        else:
            print("Tank not found")

    elif command == "Remove At":
        index = int(tokens[1])
        if 0 <= index < len(owned_tanks):
            owned_tanks.pop(index)
            print("Tank successfully sold")
        else:
            print("Index out of range")

    elif command == "Insert":
        index = int(tokens[1])
        tank_name = tokens[2]
        if 0 <= index < len(owned_tanks) and tank_name not in owned_tanks:
            owned_tanks.insert(index, tank_name)
            print("Tank successfully bought")
        elif 0 <= index < len(owned_tanks) and tank_name in owned_tanks:
            print("Tank is already bought")
        else:
            print("Index out of range")

print(", ".join(owned_tanks))
