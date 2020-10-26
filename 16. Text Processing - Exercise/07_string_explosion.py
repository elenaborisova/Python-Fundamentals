line = input()
total_strength = 0

i = 0
while i < len(line):
    char = line[i]

    if char == ">":
        strength = int(line[i + 1])
        total_strength += strength

    else:
        if total_strength > 0:
            line = line[:i] + line[i + 1:]
            i -= 1  # or continue
            total_strength -= 1

    i += 1

print(line)
