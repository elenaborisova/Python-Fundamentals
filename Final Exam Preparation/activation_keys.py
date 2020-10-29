key = input()

data = input()
while not data == "Generate":
    tokens = data.split(">>>")
    command = tokens[0]

    if command == "Contains":
        substring = tokens[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        start_index = int(tokens[2])
        end_index = int(tokens[3])

        if tokens[1] == "Upper":
            key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
        elif tokens[1] == "Lower":
            key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]

        print(key)

    elif command == "Slice":
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        key = key[:start_index] + key[end_index:]
        print(key)

    data = input()

print(f"Your activation key is: {key}")
