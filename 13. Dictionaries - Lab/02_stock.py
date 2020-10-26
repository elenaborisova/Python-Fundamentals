from collections import defaultdict

elements = input().split()
search_products = input().split()
products_quantities = defaultdict(int)

for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = elements[i + 1]
    products_quantities[product] = int(quantity)

for search_product in search_products:
    quantity = products_quantities[search_product] 
    if quantity:
        print(f"We have {quantity} of {search_product} left")
    else:
        print(f"Sorry, we don't have {search_product}")
