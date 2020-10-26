
def calculate_factorial(number):
    result = 1 
    for num in range(1, number + 1):
        result *= num
    return result


def calculate_numbers_division(first_num_fact, second_num_fact):
    result = first_num_fact / second_num_fact
    return result


first_num = int(input())
second_num = int(input())
first_num_factorial = calculate_factorial(first_num)
second_num_factorial = calculate_factorial(second_num)
print(f"{calculate_numbers_division(first_num_factorial, second_num_factorial):.2f}")
