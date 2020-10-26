cards = input().split(":")
new_deck = []

tokens = input().split()
while not tokens[0] == "Ready":
    command = tokens[0]

    if command == "Add":
        card_name = tokens[1]
        if card_name in cards:
            new_deck.append(card_name)
        else:
            print("Card not found.")

    elif command == "Insert":
        card_name = tokens[1]
        index = int(tokens[2])
        if card_name in cards and 0 <= index < len(cards):
            new_deck.insert(index, card_name)
        else:
            print("Error!")

    elif command == "Remove":
        card_name = tokens[1]
        if card_name in new_deck:
            new_deck.remove(card_name)
        else:
            print("Card not found.")

    elif command == "Swap":
        first_card = tokens[1]
        second_card = tokens[2]
        first_index = new_deck.index(first_card)
        second_index = new_deck.index(second_card)
        new_deck[first_index], new_deck[second_index] = new_deck[second_index], new_deck[first_index]

    elif command == "Shuffle" and tokens[1] == "deck":
        new_deck.reverse()

    tokens = input().split()

print(" ".join(new_deck))
