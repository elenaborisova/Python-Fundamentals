import math


def find_distance_to_center(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    return distance


def get_closest_distance(first_distance, second_distance):
    if first_distance <= second_distance:
        return True
    return False


x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

first_distance = find_distance_to_center(x1, y1)
second_distance = find_distance_to_center(x2, y2)
first_is_closest = get_closest_distance(first_distance, second_distance)

if first_is_closest:
    print(f"({int(x1)}, {int(y1)})")
else:
    print(f"({int(x2)}, {int(y2)})")

