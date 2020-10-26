def check_perfect_number(number):
    divisors_sum = 0
    for divisor in range(1, number // 2 + 1):
        if number % divisor == 0:
            divisors_sum += divisor

    if number > 0 and number == divisors_sum:
        return True


number = int(input())
is_perfect = check_perfect_number(number)

if is_perfect:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
