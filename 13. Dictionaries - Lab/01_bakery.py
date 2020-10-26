elements = input().split()
my_dict = {}

for index, food_quantity in enumerate(elements):
    if index % 2 == 0:
        my_dict[food_quantity] = int(elements[index + 1])

print(my_dict)
