notes = []

while True:
    command = input().split("-", maxsplit=1)
    if command[0] == "End":
        break

    importance = int(command[0])
    task = command[1]
    notes.append((importance, task))

tasks_in_priority = [task for importance, task in sorted(notes)]

print(tasks_in_priority)
