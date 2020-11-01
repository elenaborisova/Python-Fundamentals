skill = input()

line = input()
while not line == "For Azeroth":
    tokens = line.split()
    command = tokens[0]

    if command == "GladiatorStance":
        skill = skill.upper()
        print(skill)

    elif command == "DefensiveStance":
        skill = skill.lower()
        print(skill)

    elif command == "Dispel":
        index = int(tokens[1])
        letter = tokens[2]

        if 0 <= index < len(skill):
            skill = skill[:index] + letter + skill[index + 1:]
            print("Success!")
        else:
            print("Dispel too weak.")

    elif command == "Target" and tokens[1] == "Change":
        substring = tokens[2]
        second_substring = tokens[3]

        skill = skill.replace(substring, second_substring)
        print(skill)

    elif command == "Target" and tokens[1] == "Remove":
        substring = tokens[2]

        skill = skill.replace(substring, "")
        print(skill)

    else:
        print("Command doesn't exist!")

    line = input()
