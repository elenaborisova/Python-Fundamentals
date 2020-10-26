divisor = int(input())
bound = int(input())
max_n = 1

for n in range(1, bound + 1):
    if n % divisor == 0:
        max_n = n

print(max_n)
