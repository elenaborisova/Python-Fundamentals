lines = int(input())
sum_letters = 0

for line in range(lines):
    letter = input()
    sum_letters += ord(letter)

print(f"The sum equals: {sum_letters}")
