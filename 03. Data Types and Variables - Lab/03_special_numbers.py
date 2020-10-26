n = int(input())

for number in range(1, n + 1):
    sum_of_digits = 0

    for char in str(number):
        sum_of_digits += int(char)

    is_special = sum_of_digits in (5, 7, 11)
    print(f"{number} -> {is_special}")
