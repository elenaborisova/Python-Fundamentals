force_sides = {}

command = input()
while not command == "Lumpawaroo":
    if "|" in command:
        user_data = command.split(" | ")
        force_side = user_data[0]
        force_user = user_data[1]

        if force_side not in force_sides:
            force_sides[force_side] = []

        all_values = []
        for current_list in force_sides.values():
            all_values += current_list


        if force_user not in all_values:
            force_sides[force_side] += [force_user]

    elif "->" in command:
        user_data = command.split(" -> ")
        force_user = user_data[0]
        force_side = user_data[1]
        old_side = ""

        for side, users in force_sides.items():
            if force_user in users:
                old_side = side
                break

        if not old_side == "":
            force_sides[old_side].remove(force_user)

            if force_side not in force_sides:
                force_sides[force_side] = []

            force_sides[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        else:
            if force_side not in force_sides:
                force_sides[force_side] = []

            force_sides[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    command = input()

force_sides = dict(sorted(force_sides.items(), key=lambda x: (-len(x[1]), x[0])))

for side, users in force_sides.items():
    if len(users) > 0:  # if not empty
        print(f"Side: {side}, Members: {len(users)}")

        for user in sorted(users):
            print(f"! {user}")
