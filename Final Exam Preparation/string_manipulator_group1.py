string = input()

line = input()
while not line == "End":
    tokens = line.split()
    command = tokens[0]

    if command == "Translate":
        char = tokens[1]
        replacement = tokens[2]
        string = string.replace(char, replacement)
        print(string)

    elif command == "Includes":
        substring = tokens[1]
        print(substring in string)

    elif command == "Start":
        substring = tokens[1]
        print(string[:len(substring)] == substring)

    elif command == "Lowercase":
        string = string.lower()
        print(string)

    elif command == "FindIndex":
        char = tokens[1]

        for i in range(len(string) - 1, -1, -1):
            if string[i] == char:
                print(i)
                break

    elif command == "Remove":
        start_index = int(tokens[1])
        count = int(tokens[2])
        string = string[:start_index] + string[start_index + count:]
        print(string)

    line = input()
