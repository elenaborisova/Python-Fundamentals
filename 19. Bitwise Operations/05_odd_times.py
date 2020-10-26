numbers = list(map(int, input().split()))
result = 0
for num in numbers:
    result = result ^ num

print(result)
