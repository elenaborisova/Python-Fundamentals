COFFEE_PRICE = 1.5
WATER_PRICE = 1.0
COKE_PRICE = 1.4
SNACKS_PRICE = 2.0


def calculate_price(product: str, quantity: int):
    result = None
    if product == "coffee":
        result = COFFEE_PRICE * quantity
    elif product == "water":
        result = WATER_PRICE * quantity
    elif product == "coke":
        result = COKE_PRICE * quantity
    elif product == "snacks":
        result = SNACKS_PRICE * quantity
    return f"{result:.2f}"


product_to_order: str = input()
quantity_to_order: int = int(input())

print(calculate_price(product_to_order, quantity_to_order))
