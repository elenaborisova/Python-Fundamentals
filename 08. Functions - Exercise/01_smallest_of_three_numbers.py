def get_smallest_num(num_one: int, num_two: int, num_three: int):
    result = min(num_one, num_two, num_three)
    return result


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(get_smallest_num(num_one, num_two, num_three))
