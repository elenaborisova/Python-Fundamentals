items_with_prices = input().split("|")
budget = float(input())
new_prices = []
profit = 0

for item_with_price in items_with_prices:
    tokens = item_with_price.split("->")
    item_type = tokens[0]
    item_price = float(tokens[1])

    if item_type == "Clothes" and item_price <= 50.00:
        if budget - item_price >= 0:
            budget -= item_price
            new_price = item_price * 1.4
            new_prices.append(f"{new_price:.2f}")
            profit += new_price - item_price

    elif item_type == "Shoes" and item_price <= 35.00:
        if budget - item_price >= 0:
            budget -= item_price
            new_price = item_price * 1.4
            new_prices.append(f"{new_price:.2f}")
            profit += new_price - item_price

    elif item_type == "Accessories" and item_price <= 20.50:
        if budget - item_price >= 0:
            budget -= item_price
            new_price = item_price * 1.4
            new_prices.append(f"{new_price:.2f}")
            profit += new_price - item_price

print(" ".join(new_prices))
print(f"Profit: {profit:.2f}")

budget += sum(map(float, new_prices))
if budget - 150 >= 0:
    print("Hello, France!")
else:
    print("Time to go.")
