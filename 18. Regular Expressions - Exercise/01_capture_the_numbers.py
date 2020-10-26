import re

pattern = r"\d+"
only_numbers = []

while True:
    text = input()

    if not text:
        break

    only_numbers += re.findall(pattern, text)

print(" ".join(only_numbers))
