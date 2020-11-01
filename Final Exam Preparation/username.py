username = input()

line = input()
while not line == "Sign up":
    tokens = line.split()
    command = tokens[0]

    if line == "Case lower":
        username = username.lower()
        print(username)

    elif line == "Case upper":
        username = username.upper()
        print(username)

    elif command == "Reverse":
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            substring = username[start_index:end_index + 1]
            print(substring[::-1])

    elif command == "Cut":
        substring = tokens[1]

        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")

    elif command == "Replace":
        char = tokens[1]
        username = username.replace(char, "*")
        print(username)

    elif command == "Check":
        char = tokens[1]

        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")

    line = input()
