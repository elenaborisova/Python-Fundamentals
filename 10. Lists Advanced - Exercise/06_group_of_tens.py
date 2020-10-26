import math
numbers = list(map(int, input().split(", ")))

boundary = 10
while not numbers == []:
    new_group = list(filter(lambda n: n <= boundary, numbers))
    numbers = [num for num in numbers if num not in new_group]
    print(f"Group of {boundary}'s: {new_group}")

    boundary += 10
