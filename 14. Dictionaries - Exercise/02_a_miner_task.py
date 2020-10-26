resource_quantities = {}

while True:
    text = input()
    if text == "stop":
        break
    resource = text
    quantity = int(input())

    if resource not in resource_quantities:
        resource_quantities[resource] = 0

    resource_quantities[resource] += quantity

for resource, quantity in resource_quantities.items():
    print(f"{resource} -> {quantity}")
    