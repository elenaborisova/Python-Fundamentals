def validate_index(i, text):
    if 0 <= i < len(text):
        return True
    return False


stops = input()

line = input()
while not line == "Travel":
    tokens = line.split(":")
    command = tokens[0]

    if command == "Add Stop":
        index = int(tokens[1])
        string = tokens[2]

        if validate_index(index, stops):
            stops = stops[:index] + string + stops[index:]

    elif command == "Remove Stop":
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if validate_index(start_index, stops) and validate_index(end_index, stops):
            stops = stops[:start_index] + stops[end_index + 1:]

    elif command == "Switch":
        old_string = tokens[1]
        new_string = tokens[2]

        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)
    line = input()


print(f"Ready for world tour! Planned stops: {stops}")