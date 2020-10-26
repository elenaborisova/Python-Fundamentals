numbers_string = input()

numbers_list = numbers_string.split()
numbers_list = list(map(int, numbers_list))
new_list = []

for number in numbers_list:
    number *= -1
    new_list.append(number)

print(new_list)
