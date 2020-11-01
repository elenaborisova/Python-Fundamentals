import re

n = int(input())
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for _ in range(n):
    barcode = input()
    valid_barcode = re.fullmatch(pattern, barcode)

    if valid_barcode:
        digits = [char for char in valid_barcode[0] if char.isdigit()]
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
