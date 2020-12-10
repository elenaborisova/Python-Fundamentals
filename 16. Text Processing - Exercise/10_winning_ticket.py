def is_valid(ticket):
    return len(ticket) == 20


def is_jackpot(ticket):
    for win_char in win_chars:
        if win_char * 20 == ticket:
            print(f'ticket "{ticket}" - 10{win_char} Jackpot!')
            return True
    return False


def is_match(ticket):
    left_half = ticket[:10]
    right_half = ticket[10:]

    for win_char in win_chars:
        if win_char * 6 in left_half and win_char * 6 in right_half:
            left_count = left_half.count(win_char)
            right_count = right_half.count(win_char)
            count = min(left_count, right_count)
            print(f'ticket "{ticket}" - {count}{win_char}')
            return True

    return False


tickets = input().split(", ")
win_chars = ["@", "$", "#", "^"]

for ticket in tickets:
    ticket = ticket.strip()

    if not is_valid(ticket):
        print("invalid ticket")
        continue
    if is_jackpot(ticket):
        continue
    if is_match(ticket):
        continue

    print(f'ticket "{ticket}" - no match')
