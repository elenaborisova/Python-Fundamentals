cards = input().split()
shuffles_count = int(input())
middle_length = len(cards) // 2
shuffled_deck = []

for shuffle in range(shuffles_count):
    first_half = [card for index, card in enumerate(cards) if index < middle_length]
    # first_half = cards[:middle_length]
    second_half = [card for index, card in enumerate(cards) if index >= middle_length]
    # second_half = cards[middle_length:]

    for first_card in first_half:
        shuffled_deck.append(first_card)
        for second_card in second_half:
            shuffled_deck.append(second_card)
            second_half.remove(second_card)
            break

    cards = shuffled_deck
    shuffled_deck = []

print(cards)

