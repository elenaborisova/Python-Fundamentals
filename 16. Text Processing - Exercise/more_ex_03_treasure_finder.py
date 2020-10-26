def decrypt_line(line):
    key_index = 0
    decrypted_line = ""

    for index, char in enumerate(line):
        if key_index < len(key):
            ascii_char = ord(char)
            ascii_char -= key[key_index]
            decrypted_line += chr(ascii_char)
            key_index += 1
        else:
            key_index = 0
            ascii_char = ord(char)
            ascii_char -= key[key_index]
            decrypted_line += chr(ascii_char)
            key_index += 1

    return decrypted_line


def get_treasure_coordinates(decrypted_line):
    type_start_index = 0
    type_end_index = 0
    coordinates_start_index = 0
    coordinates_end_index = 0
    is_open = False

    for index, char in enumerate(decrypted_line):
        if char == "&" and not is_open:
            type_start_index = index + 1
            is_open = True
        elif char == "&" and is_open:
            type_end_index = index
        elif char == "<":
            coordinates_start_index = index + 1
        elif char == ">":
            coordinates_end_index = index

    treasure_type = decrypted_line[type_start_index:type_end_index]
    coordinates = decrypted_line[coordinates_start_index:coordinates_end_index]
    return treasure_type, coordinates


key = list(map(int, input().split()))

line = input()
while not line == "find":
    decrypted_line = decrypt_line(line)
    treasure_type, coordinates = get_treasure_coordinates(decrypted_line)

    print(f"Found {treasure_type} at {coordinates}")
    line = input()
