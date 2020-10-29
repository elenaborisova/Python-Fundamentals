numbers = list(map(int, input().split()))
average_value = sum(numbers) / len(numbers)
top_numbers = []

for _ in range(5):
    if max(numbers) > average_value:
        top_numbers.append(max(numbers))
        numbers.remove(max(numbers))

if top_numbers:
    print(" ".join(map(str, top_numbers)))
else:
    print("No")