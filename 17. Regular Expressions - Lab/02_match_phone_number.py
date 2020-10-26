import re

phone_numbers = input()

search_pattern = r"(\+359-2-\d{3}-\d{4}|\+359 2 \d{3} \d{4})\b"
valid_numbers = re.findall(search_pattern, phone_numbers)

print(", ".join(valid_numbers))
