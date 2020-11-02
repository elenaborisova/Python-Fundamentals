import re


def encrypt_word(word, key):
    result = ""

    for char in word:
        if char == " " or char == "'":
            result += char
            continue
        elif ord(char) + key > 122:
            result += chr(96 + key - (122 - ord(char)))
        elif ord(char) + key > 90 and not 97 <= ord(char) <= 122:
            result += chr(64 + key - (90 - ord(char)))
        else:
            result += chr(ord(char) + key)

    return result


pattern = r"([A-Z][a-z' ]+):([A-Z ]+)"

line = input()
while not line == "end":
    valid_line = re.fullmatch(pattern, line)

    if valid_line:
        artist = valid_line[1]
        song = valid_line[2]
        key = len(artist)
        encrypted_line = ""

        encrypted_line += encrypt_word(artist, key)
        encrypted_line += "@"
        encrypted_line += encrypt_word(song, key)

        print(f"Successful encryption: {encrypted_line}")
    else:
        print("Invalid input!")

    line = input()
