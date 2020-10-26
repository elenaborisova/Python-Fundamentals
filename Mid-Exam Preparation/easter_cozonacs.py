budget = float(input())
flour_price_per_kg = float(input())

eggs_pack_price = 0.75 * flour_price_per_kg
milk_liter_price = flour_price_per_kg * 1.25
milk_per_cozonac_price = milk_liter_price * 1/4
one_cozunac_price = eggs_pack_price + flour_price_per_kg + milk_per_cozonac_price
cozonacs_count = 0
colored_eggs_count = 0

while True:
    if budget - one_cozunac_price <= 0:
        break

    budget -= one_cozunac_price
    cozonacs_count += 1
    colored_eggs_count += 3

    if cozonacs_count % 3 == 0:
        colored_eggs_count -= cozonacs_count - 2

print(f"You made {cozonacs_count} cozonacs! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
