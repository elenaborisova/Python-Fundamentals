def convert_number_to_binary(number):
    binary_digits = []
    while not number == 0:
        digit = number % 2
        binary_digits.append(digit)
        number //= 2

    return list(reversed(binary_digits))


number = int(input())
first_position_num = convert_number_to_binary(number)[-2]
print(first_position_num)
