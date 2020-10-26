def find_sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    elif num == 0:
        return 0


num1 = int(input())
num2 = int(input())
num3 = int(input())

product = find_sign(num1) * find_sign(num2) * find_sign(num3)
if product > 0:
    print("positive")
elif product < 0:
    print("negative")
else:
    print("zero")

