import re

n = int(input())
pattern = r"(\*|@)([A-Z][a-z]{2,})\1: \[([A-Za-z])]\|\[([A-Za-z])]\|\[([(A-Za-z])]\|$"

for _ in range(n):
    message = input()
    valid_message = re.search(pattern, message)

    if valid_message:
        tag = valid_message[2]
        first_letter = valid_message[3]
        second_letter = valid_message[4]
        third_letter = valid_message[5]

        print(f"{tag}: {ord(first_letter)} {ord(second_letter)} {ord(third_letter)}")
    else:
        print("Valid message not found!")
