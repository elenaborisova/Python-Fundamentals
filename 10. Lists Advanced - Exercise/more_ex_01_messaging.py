def get_digits_sum(str_num):
    digits_sum = 0
    for digit in str_num:
        digits_sum += int(digit)

    return digits_sum


def get_message(digits_sum, line):
    message = ""

    if digits_sum > len(line):
        index = digits_sum - len(line)
        message += line[index]
        line = line[:index] + line[index + 1:]
    else:
        index = digits_sum
        message += line[index]
        line = line[:index] + line[index + 1:]

    return message, line


numbers = input().split()
line = input()
message = ""

for str_num in numbers:
    digits_sum = get_digits_sum(str_num)
    message += get_message(digits_sum, line)[0]
    line = get_message(digits_sum, line)[1]

print(message)
