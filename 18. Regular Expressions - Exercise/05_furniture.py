import re

pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"

total_price = 0

line = input()
print("Bought furniture:")

while not line == "Purchase":

    valid_line = re.fullmatch(pattern, line)

    if valid_line:
        furniture_item = valid_line[1]
        price = float(valid_line[2])
        quantity = int(valid_line[4])

        print(furniture_item)
        total_price += price * quantity

    line = input()


print(f"Total money spend: {total_price:.2f}")

