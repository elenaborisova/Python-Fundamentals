def get_tribonacii_sequence(num_count):
    tribonacci_sequence = ""
    first_num = 0
    second_num = 0
    third_num = 0
    curr_num = 1

    for _ in range(1, num_count + 1):
        tribonacci_sequence += str(curr_num) + " "
        first_num = second_num
        second_num = third_num
        third_num = curr_num
        curr_num = first_num + second_num + third_num

    return tribonacci_sequence


num_count = int(input())
print(get_tribonacii_sequence(num_count))
