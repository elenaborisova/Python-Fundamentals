string = input()
capitals = []

for index in range(len(string)):
    char = string[index]
    if char.isupper():
        capitals.append(index)

print(capitals)
