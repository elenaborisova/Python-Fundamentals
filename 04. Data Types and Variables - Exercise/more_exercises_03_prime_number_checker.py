number = int(input())
is_not_prime = False

for divisor in range(2, number):
    if number % divisor == 0:
        is_not_prime = True
        break

if is_not_prime:
    print("False")
else:
    print("True")
