import re

n = int(input())
pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#"

for _ in range(n):
    line = input()
    valid_line = re.fullmatch(pattern, line)

    if valid_line:
        boss_name = valid_line[1]
        title = valid_line[2]

        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armour: {len(title)}")
    else:
        print("Access denied!")
