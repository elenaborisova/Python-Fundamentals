n = int(input())
positive = []
negative = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

positive_count = len(positive)
negative_sum = sum(negative)

print(positive)
print(negative)
print(f"Count of positives: {positive_count}. Sum of negatives: {negative_sum}")
