products = {}

command = input()
while not command == "buy":
    product_data = command.split()
    product_name = product_data[0]
    product_price = float(product_data[1])
    product_quantity = int(product_data[2])

    if product_name not in products:
        products[product_name] = [product_price, product_quantity]
    else:
        products[product_name][1] += product_quantity
        products[product_name][0] = product_price

    command = input()

for product_name, price_quantity in products.items():
    print(f"{product_name} -> {price_quantity[0] * price_quantity[1]:.2f}")

