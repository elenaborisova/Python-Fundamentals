nums = list(map(int, input().split(", ")))
even_nums_indices = [index for index, num in enumerate(nums) if num % 2 == 0]
print(even_nums_indices)
