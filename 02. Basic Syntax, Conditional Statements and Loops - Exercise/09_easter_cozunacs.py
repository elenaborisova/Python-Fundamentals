budget = float(input())
flour_price_1kg = float(input())
cozunacs_count = 0
colored_eggs_count = 0

eggs_price_1pack = 0.75 * flour_price_1kg
milk_price_1l = flour_price_1kg * 1.25 # or + flour_price_1kg * 0.25
milk_price_1cozunac = 1/4 * milk_price_1l

one_cozunac_price = flour_price_1kg + eggs_price_1pack + milk_price_1cozunac

while one_cozunac_price <= budget:
    cozunacs_count += 1
    colored_eggs_count += 3

    if cozunacs_count % 3 == 0:
        colored_eggs_count -= cozunacs_count - 2

    budget -= one_cozunac_price

print(f"You made {cozunacs_count} cozonacs! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")

