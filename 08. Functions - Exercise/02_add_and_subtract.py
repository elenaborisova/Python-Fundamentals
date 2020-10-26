def sum_numbers(a: int, b: int):
    return a + b


def subtract(a: int, b: int):
    return a - b


def solve(a, b, c):
    total_sum = sum_numbers(num_one, num_two)
    result = subtract(total_sum, num_three)
    return result


num_one = int(input())
num_two = int(input())
num_three = int(input())

print(solve(num_one, num_two, num_three))
