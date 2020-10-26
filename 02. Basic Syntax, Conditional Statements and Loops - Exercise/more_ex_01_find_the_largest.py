number = input()
new_list = []
new_string = ""

for index, digit in enumerate(number):
    new_list.append(int(digit)) # convert digit into integer

while new_list: # while list is not empty
    max_num = str(max(new_list)) # convert to string in order to add to new_string
    new_string += max_num
    new_list.remove(max(new_list))


result = int(new_string)
print(result)
