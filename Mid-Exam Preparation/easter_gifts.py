gifts = input().split()

tokens = input()
while not tokens == "No Money":
    args = tokens.split()
    command = args[0]

    if command == "OutOfStock":
        gift_name = args[1]
        for index, gift in enumerate(gifts):
            if gift == gift_name:
                gifts[index] = "None"

    elif command == "Required":
        gift = args[1]
        index = int(args[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif command == "JustInCase":
        gift = args[1]
        gifts[-1] = gift

    tokens = input()

updated_gifts = [gift for gift in gifts if not gift == "None"]
print(" ".join(updated_gifts))