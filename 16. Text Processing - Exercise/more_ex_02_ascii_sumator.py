first_char = input()
second_char = input()
line = input()

first_ascii = ord(first_char)
second_ascii = ord(second_char)


result = 0
for char in line:
    char_ascii = ord(char)

    if first_ascii < char_ascii < second_ascii:
        result += char_ascii

print(result)
