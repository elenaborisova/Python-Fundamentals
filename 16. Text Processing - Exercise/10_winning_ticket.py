def validate_ticket(ticket):
    if len(ticket) == 20:
        return True
    return False


def check_winning_symbols(ticket):
    winning_chars = ["@", "#", "$", "^"]
    win_char = ""
    curr_char = ""
    curr_count = 0
    max_count = 0

    for i in range(len(ticket)):
        char = ticket[i]
        if char in winning_chars:
            if char != curr_char or curr_char == "":
                curr_count = 1
                curr_char = char
            else:
                curr_count += 1
                curr_char = char
        else:
            if curr_count > max_count:
                max_count = curr_count
                win_char = curr_char
            curr_count = 0

    if curr_count > max_count:
        max_count = curr_count
        win_char = curr_char

    if max_count >= 6:
        return max_count, win_char
    return 0, ""


tickets = input().split(", ")

for ticket in tickets:
    ticket = ticket.strip()

    if validate_ticket(ticket):
        first_half = ticket[:10]
        second_half = ticket[10:]
        first_count, first_char = check_winning_symbols(first_half)
        second_count, second_char = check_winning_symbols(second_half)

        if first_count == second_count == 10 and first_char == second_char:
            print(f'ticket "{ticket}" - {first_count}{first_char} Jackpot!')
        elif first_count >= 6 and second_count >= 6 and first_char == second_char:
            print(f'ticket "{ticket}" - {min(first_count, second_count)}{first_char}')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")


