import re

numbers = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, numbers)

for match in matches:
    print(match.group(0), end=" ")


# 2nd method
pattern = r"((^|(?<=\s))(-*)(\d+)((\.\d+)*)($|?+\s)))"

matches = re.findall(pattern, numbers)

for match in matches:
    number, *others = match
    print(number, end=" ")
