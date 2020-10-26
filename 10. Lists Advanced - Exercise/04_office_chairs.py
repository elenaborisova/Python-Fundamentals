rooms_count = int(input())
total_free_chairs = 0
has_enough_chairs = True

for room in range(1, rooms_count + 1):
    chairs, people = input().split()
    people = int(people)

    chairs_count = len(chairs)

    if chairs_count < people:
        print(f"{people - chairs_count} more chairs needed in room {room}")
        has_enough_chairs = False
    else:
        free_chairs = chairs_count - people
        total_free_chairs += free_chairs

if has_enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
