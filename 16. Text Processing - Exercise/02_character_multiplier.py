two_strings = input().split()
first_string = two_strings[0]
second_string = two_strings[1]
total_sum = 0

if len(first_string) == len(second_string):
    for i in range(len(first_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])

elif len(first_string) > len(second_string):
    last_index = 0
    for i in range(len(second_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])
        last_index = i + 1
    for i in range(last_index, len(first_string)):
        total_sum += ord(first_string[i])

else:
    last_index = 0
    for i in range(len(first_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])
        last_index = i + 1
    for i in range(last_index, len(second_string)):
        total_sum += ord(second_string[i])

print(total_sum)

