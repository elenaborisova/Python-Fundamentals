import math


def find_distance_to_center(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    return distance


def get_longest_line(first_pair_distance, second_pair_distance):
    if first_pair_distance >= second_pair_distance:
        first_line = find_distance_to_center(x1, y1)
        second_line = find_distance_to_center(x2, y2)
        if first_line <= second_line:
            print(f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})")
        else:
            print(f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})")

    else:
        third_line = find_distance_to_center(x3, y3)
        fourth_line = find_distance_to_center(x4, y4)
        if third_line <= fourth_line:
            print(f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})")
        else:
            print(f"({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

first_pair_distance = find_distance_to_center(x1, y1) + find_distance_to_center(x2, y2)
second_pair_distance = find_distance_to_center(x3, y3) + find_distance_to_center(x4, y4)

get_longest_line(first_pair_distance, second_pair_distance)