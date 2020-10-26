import re

dates = input()

pattern = r"\b(\d{2})([/\.-])([A-Z][a-z]{2})\2(\d{4})\b"
valid_dates = re.findall(pattern, dates)

for valid_date in valid_dates:
    print(f"Day: {valid_date[0]}, Month: {valid_date[2]}, Year: {valid_date[3]}")
