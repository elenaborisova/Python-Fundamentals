number = int(input())
position = int(input())

mask = ~(1 << position)
result = mask & number

print(result)
