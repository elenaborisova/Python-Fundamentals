string = input()

line = input()
while not line == "Done":
    tokens = line.split()
    command = tokens[0]

    if command == "Change":
        char = tokens[1]
        replacement = tokens[2]

        string = string.replace(char, replacement)
        print(string)

    elif command == "Includes":
        substring = tokens[1]
        print(substring in string)

    elif command == "End":
        substring = tokens[1]
        print(string[-1:-len(substring) - 1:-1] == substring[::-1])

    elif command == "Uppercase":
        string = string.upper()
        print(string)

    elif command == "FindIndex":
        char = tokens[1]
        char_index = string.index(char)
        print(char_index)

    elif command == "Cut":
        start_index = int(tokens[1])
        length = int(tokens[2])

        string = string[start_index:start_index + length]
        print(string)

    line = input()
