factor = int(input())
count = int(input())
multiples = []

for number in range(1, count + 1):
    number *= factor
    multiples.append(number)

print(multiples)
