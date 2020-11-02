encrypted_string = input()
substrings = input().split()

is_valid = True

for char in encrypted_string:
    if (ord(char) < 100 or ord(char) > 125) and char != "#":
        is_valid = False
        break

if is_valid:
    first_substring = substrings[0]
    second_substring = substrings[1]
    decrypted_string = ""

    for char in encrypted_string:
        decrypted_string += chr(ord(char) - 3)

    decrypted_string = decrypted_string.replace(first_substring, second_substring)
    print(decrypted_string)
else:
    print("This is not the book you are looking for.")
