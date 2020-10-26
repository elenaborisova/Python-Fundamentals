from collections import defaultdict

bakery = defaultdict(int)

while True:
    command = input()
    if command == "statistics":
        break
        
    product, quantity = command.split(": ")
    bakery[product] += int(quantity)

print(f"Products in stock:")
for product, quantity in bakery.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")
