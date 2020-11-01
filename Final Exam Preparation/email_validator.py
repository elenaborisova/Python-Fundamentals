email = input()

commands_data = input()
while not commands_data == "Complete":
    tokens = commands_data.split()
    command = tokens[0]

    if commands_data == "Make Upper":
        email = email.upper()
        print(email)

    elif commands_data == "Make Lower":
        email = email.lower()
        print(email)

    elif command == "GetDomain":
        count = int(tokens[1])
        print(email[-count:])

    elif command == "GetUsername":
        if "@" in email:
            symbol_index = email.index("@")
            print(email[:symbol_index])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif command == "Replace":
        char = tokens[1]
        email = email.replace(char, "-")
        print(email)

    elif command == "Encrypt":
        ascii_values = [str(ord(char)) for char in email]
        print(" ".join(ascii_values))

    commands_data = input()
