encrypted_message = input()
numbers = list(filter(lambda x: x.isdigit(), encrypted_message))
non_numbers = list(filter(lambda x: not x.isdigit(), encrypted_message))

take_list = [int(numbers[i]) for i in range(len(numbers)) if i % 2 == 0]
skip_list = [int(numbers[i]) for i in range(len(numbers)) if not i % 2 == 0]

result_string = []
index = 0

while index < len(take_list):
    take_chars_count = take_list[index]
    skip_chars_count = skip_list[index]

    result_string += non_numbers[:take_chars_count]
    non_numbers = non_numbers[take_chars_count + skip_chars_count:]
    index += 1

print("".join(result_string))
