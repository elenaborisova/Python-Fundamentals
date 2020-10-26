def get_odd_and_even_sum(number_as_str):
    odd_sum = 0
    even_sum = 0

    for digit_str in number_as_str:
        digit = int(digit_str)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return even_sum, odd_sum


number_as_str = input()
even_sum, odd_sum = get_odd_and_even_sum(number_as_str)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
