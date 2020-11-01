password = input()

line = input()
while not line == "Done":
    tokens = line.split()
    command = tokens[0]

    if command == "TakeOdd":
        password = password[1::2]

    elif command == "Cut":
        index = int(tokens[1])
        length = int(tokens[2])

        substring = password[index:index + length]
        password = password.replace(substring, "", 1)

    elif command == "Substitute":
        substring = tokens[1]
        substitute = tokens[2]

        if substring not in password:
            print("Nothing to replace!")
            line = input()
            continue

        password = password.replace(substring, substitute)

    print(password)
    line = input()


print(f"Your password is: {password}")
