def get_racer_time(racer):
    total_time = 0

    for i in range(len(racer)):
        time = racer[i]
        if time == 0:
            total_time -= total_time * 0.2
        total_time += time 

    return total_time


numbers = list(map(int, input().split()))

middle_index = len(numbers) // 2
first_racer = numbers[:middle_index]
second_racer = numbers[middle_index + 1:]

first_time = get_racer_time(first_racer)
second_time = get_racer_time(list(reversed(second_racer)))

if first_time < second_time:
    print(f"The winner is left with total time: {first_time:.1f}")
else:
    print(f"The winner is right with total time: {second_time:.1f}")
