tasks_times = list(map(int, input().split()))

tokens = input().split()
while not tokens[0] == "End":
    command = tokens[0]

    if command == "Complete":
        index = int(tokens[1])
        if 0 <= index < len(tasks_times):
            tasks_times[index] = 0

    elif command == "Change":
        index = int(tokens[1])
        time = int(tokens[2])
        if 0 <= index < len(tasks_times):
            tasks_times[index] = time

    elif command == "Drop":
        index = int(tokens[1])
        if 0 <= index < len(tasks_times):
            tasks_times[index] = -1

    elif command == "Count" and tokens[1] == "Completed":
        completed_tasks = [task for task in tasks_times if task == 0]
        print(len(completed_tasks))

    elif command == "Count" and tokens[1] == "Incomplete":
        incomplete_tasks = [task for task in tasks_times if task > 0]
        print(len(incomplete_tasks))

    elif command == "Count" and tokens[1] == "Dropped":
        dropped_tasks = [task for task in tasks_times if task < 0]
        print(len(dropped_tasks))

    tokens = input().split()

incomplete_tasks = [task for task in tasks_times if task > 0]
print(" ".join(map(str, incomplete_tasks)))
