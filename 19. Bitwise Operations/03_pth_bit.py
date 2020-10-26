number = int(input())
position = int(input())

result = (number >> position) & 1

print(result)
