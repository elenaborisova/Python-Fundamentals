import re

n = int(input())
pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})]"

for _ in range(n):
    message_data = input()
    valid_message = re.fullmatch(pattern, message_data)

    if valid_message:
        command = valid_message[1]
        message = valid_message[2]
        ascii_values = [str(ord(char)) for char in message]
        print(f"{command}: {' '.join(ascii_values)}")
    else:
        print("The message is invalid")
