message = input()

instructions = input()
while not instructions == "Decode":
    tokens = instructions.split("|")
    command = tokens[0]

    if command == "Move":
        letters_count = int(tokens[1])

        substring = message[:letters_count]
        message = message[letters_count:] + substring

    elif command == "Insert":
        index = int(tokens[1])
        value = tokens[2]

        if 0 <= index <= len(message):
            message = message[:index] + value + message[index:]

    elif command == "ChangeAll":
        substring = tokens[1]
        replacement = tokens[2]

        message = message.replace(substring, replacement)

    instructions = input()


print(f"The decrypted message is: {message}")
