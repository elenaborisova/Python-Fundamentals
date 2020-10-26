import re

full_names = input()

search_pattern = r"\b([A-Z][a-z]+\s[A-Z][a-z]+)\b"
valid_names: list = re.findall(search_pattern, full_names)

print(" ".join(valid_names))
