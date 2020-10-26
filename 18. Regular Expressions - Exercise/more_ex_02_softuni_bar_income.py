import re

pattern = r"%([A-Z][a-z]+)%[^%\|\$\.]*<(\w+)>[^%\|\$\.]*\|(\d+)\|[^%\|\$\.]*?(\d+(\.\d+)?)\$"

total_income = 0

line = input()
while not line == "end of shift":
    valid_line = re.fullmatch(pattern, line)

    if valid_line:
        name = valid_line[1]
        product = valid_line[2]
        count = int(valid_line[3])
        price = float(valid_line[4])

        print(f"{name}: {product} - {count * price:.2f}")
        total_income += count * price

    line = input()

print(f"Total income: {total_income:.2f}")

