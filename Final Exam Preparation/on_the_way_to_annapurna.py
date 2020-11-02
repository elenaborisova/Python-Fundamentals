stores = {}

line = input()
while not line == "END":
    tokens = line.split("->")
    command = tokens[0]
    store = tokens[1]

    if command == "Add":
        items = tokens[2].split(",")

        if store not in stores:
            stores[store] = []

        stores[store].extend(items)

    elif command == "Remove":
        if store in stores:
            stores.pop(store)

    line = input()


print("Stores list:")
for store, items in sorted(stores.items(), key=lambda x: (len(x[1]), x[0]), reverse=True):
    print(store)
    for item in items:
        print(f"<<{item}>>")
