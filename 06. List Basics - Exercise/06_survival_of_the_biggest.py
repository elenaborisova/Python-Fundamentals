numbers = list(map(int, input().split()))
n_to_remove = int(input())

for _ in range(n_to_remove):
    smallest_num = min(numbers)
    numbers.remove(smallest_num)

print(numbers)
