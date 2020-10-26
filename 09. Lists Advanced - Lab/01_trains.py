def add_people(people, wagons):
    wagons[-1] += people
    return wagons


def insert_people(index, people, wagons):
    wagons[index] += people
    return wagons


def leave_people(index, people, wagons):
    wagons[index] -= people
    return wagons


wagons_count = int(input())
wagons = [0 for _ in range(wagons_count)]

command = input().split()
while not command[0] == "End":
    if command[0] == "add":
        people = int(command[1])
        add_people(people, wagons)

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        insert_people(index, people, wagons)

    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        leave_people(index, people, wagons)

    command = input().split()

print(wagons)
