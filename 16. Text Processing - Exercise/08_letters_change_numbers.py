def find_letter_position(letter):
    alphabet_position = ord(letter) - 64  # default

    if letter.islower():
        alphabet_position = ord(letter) - 96

    return alphabet_position


def calculate_result(string):
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])

    first_letter_position = find_letter_position(first_letter)
    last_letter_position = find_letter_position(last_letter)

    if first_letter.isupper():
        number /= first_letter_position
    else:
        number *= first_letter_position

    if last_letter.isupper():
        number -= last_letter_position
    else:
        number += last_letter_position

    return number


line = input().split()
total_sum = 0

for string in line:
    total_sum += calculate_result(string)

print(f"{total_sum:.2f}")
