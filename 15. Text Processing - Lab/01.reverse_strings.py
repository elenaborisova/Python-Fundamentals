def reverse_string(string):
    reversed_string = ""
    for char in reversed(string):
        reversed_string += char
    return reversed_string


words = []
while True:
    command = input()
    if command == "end":
        break
    words.append(command)

for word in words:
    print(f"{word} = {reverse_string(word)}")
