items = input().split("|")
budget = int(input())
profit = 0
new_prices = []

for item in items:
    items_prices = item.split("->")
    item_type = items_prices[0]
    item_price = float(items_prices[1])

    can_be_bought = (
        (item_type == "Clothes" and item_price <= 50) or
        (item_type == "Shoes" and item_price <= 35) or
        (item_type == "Accessories" and item_price <= 20.50)
    )

    if can_be_bought and budget >= item_price:
        budget -= item_price
        new_price = item_price * 1.4
        new_prices.append(new_price)
        profit += new_price - item_price

new_prices_strings = []
for new_price in new_prices:
    new_prices_strings.append(str(f"{new_price:.2f}"))

print(" ".join(new_prices_strings))  # only works with strings
print(f"Profit: {profit:.2f}")

budget += sum(new_prices)

if budget - 150 >= 0:
    print("Hello, France!")
else:
    print("Time to go.")

