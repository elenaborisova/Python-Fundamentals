gift_names = input().split()

command = input()
while command != "No Money":
    commands = command.split()

    if commands[0] == "OutOfStock":
        gift = commands[1]
        for gift_name in gift_names:
            if gift_name == gift:
                index = gift_names.index(gift_name)
                gift_names[index] = "None"

    elif commands[0] == "Required":
        gift = commands[1]
        index = int(commands[2])
        if 0 <= index < len(gift_names):
            gift_names[index] = gift

    elif commands[0] == "JustInCase":
        gift = commands[1]
        gift_names[-1] = gift

    command = input()

for i in range(len(gift_names) - 1, -1, -1):
    if gift_names[i] == "None":
        gift_names.remove('None')

print(' '.join(gift_names))


