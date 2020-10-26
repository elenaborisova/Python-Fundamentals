line = input()
unique_chars = ""

for index, char in enumerate(line):
    if index + 1 < len(line):
        next_char = line[index + 1]
        if not next_char == char:
            unique_chars += char
    else:
        unique_chars += char

print(unique_chars)
