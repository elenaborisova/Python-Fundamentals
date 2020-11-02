import re

n = int(input())
pattern = r"^(\$|%)([A-Z][a-z]{2,})\1: \[(\d+)]\|\[(\d+)]\|\[(\d+)]\|$"

for _ in range(n):
    message = input()
    valid_message = re.fullmatch(pattern, message)

    if valid_message:
        tag = valid_message[2]
        first_num = int(valid_message[3])
        second_num = int(valid_message[4])
        third_num = int(valid_message[5])

        print(f"{tag}: {chr(first_num) + chr(second_num) + chr(third_num)}")
    else:
        print("Valid message not found!")
