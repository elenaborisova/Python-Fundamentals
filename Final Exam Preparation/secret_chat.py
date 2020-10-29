message = input()

line = input()
while not line == "Reveal":
    args = line.split(":|:")
    command = args[0]

    if command == "InsertSpace":
        index = int(args[1])
        message = message[:index] + " " + message[index:]

    elif command == "Reverse":
        substring = args[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
        else:
            print("error")
            line = input()
            continue

    elif command == "ChangeAll":
        substring = args[1]
        replacement = args[2]
        message = message.replace(substring, replacement)

    print(message)
    line = input()

print(f"You have a new text message: {message}")