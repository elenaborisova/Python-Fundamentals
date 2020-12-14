email = input()

line = input()
while not line == "Complete":
    tokens = line.split()
    command = tokens[0]

    if command == "Make" and tokens[1] == "Upper":
        email = email.upper()
        print(email)

    elif command == "Make" and tokens[1] == "Lower":
        email = email.lower()
        print(email)

    elif command == "GetDomain":
        count = int(tokens[1])
        print(email[len(email) - count:])

    elif command == "GetUsername":
        if "@" in email:
            at_index = email.index("@")
            print(email[:at_index])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif command == "Replace":
        char = tokens[1]
        email = email.replace(char, "-")
        print(email)

    elif command == "Encrypt":
        ascii_values = [str(ord(char)) for char in email]
        print(" ".join(ascii_values))

    line = input()