n = int(input())

is_open = False
is_closed = False
is_balanced = True

open_count = 0
closed_count = 0

total_closed_count = 0
total_opened_count = 0

for _ in range(n):
    char = input()

    if char == "(":
        is_open = True
        open_count += 1
        total_opened_count += 1

    elif char == ")" and is_open:
        is_closed = True
        closed_count += 1
        total_closed_count += 1

    elif char == ")" and not is_open:
        is_closed = False
        total_closed_count += 1

    if is_open and is_closed and open_count == 1 and closed_count == 1:
        is_balanced = True
        is_open = False
        is_closed = False
        open_count = 0
        closed_count = 0

    if open_count == 2:
        is_balanced = False
        break

if is_balanced and total_closed_count == total_opened_count:
    print("BALANCED")
else:
    print("UNBALANCED")
