total_price = 0

command = input()
while command != "special" and command != "regular":
    price = float(command)

    if price >= 0:
        total_price += price
    else:
        print("Invalid price!")

    command = input()

taxes = 0.2 * total_price
price_with_tax = total_price + taxes
if total_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        price_with_tax -= price_with_tax * 0.1
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {price_with_tax:.2f}$")
