shops = input().split()
n = int(input())

for _ in range(n):
    tokens = input().split()
    command = tokens[0]

    if command == "Include":
        shop = tokens[1]
        shops.append(shop)

    elif command == "Visit":
        position = tokens[1]
        count = int(tokens[2])
        if count <= len(shops):
            if position == "first":
                for i in range(count - 1, -1, -1):
                    shops.pop(i)
            elif position == "last":
                for i in range(len(shops) - 1, len(shops) - count - 1, -1):
                    shops.pop(i)

    elif command == "Prefer":
        shop_index_one = int(tokens[1])
        shop_index_two = int(tokens[2])
        if 0 <= shop_index_one < len(shops) and 0 <= shop_index_two < len(shops):
            shops[shop_index_one], shops[shop_index_two] = shops[shop_index_two], shops[shop_index_one]

    elif command == "Place":
        shop = tokens[1]
        shop_index = int(tokens[2])
        if 0 <= shop_index + 1 < len(shops):
            shops.insert(shop_index + 1, shop)

print(f"Shops left:\n{' '.join(shops)}")