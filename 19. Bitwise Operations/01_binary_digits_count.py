def convert_number_to_binary(positive_number_int):
    binary_digits = []
    while not positive_number_int == 0:
        digit = positive_number_int % 2
        binary_digits.append(digit)
        positive_number_int //= 2

    return list(reversed(binary_digits))


def find_count(result, binary_digit):
    return result.count(binary_digit)


positive_number_int = int(input())
binary_digit = int(input())

result = convert_number_to_binary(positive_number_int)
count = find_count(result, binary_digit)
print(count)


number = bin(int(input()))
print(number)
