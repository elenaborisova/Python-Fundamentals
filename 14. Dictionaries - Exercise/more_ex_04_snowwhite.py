from collections import defaultdict

dwarfs = {}
name_color_count = defaultdict(int)

line = input()
while not line == "Once upon a time":
    name, color, physics = line.split(" <:> ")
    physics = int(physics)

    name_color_count[(name, color)] += 1

    if (name, color) not in dwarfs:
        dwarfs[(name, color)] = physics
    else:
        if dwarfs[(name, color)] < physics:
            dwarfs[(name, color)] = physics

    line = input()

    
for key, value in sorted(dwarfs.items(), key=lambda x: (-x[1], -x.count(x[0][1]))):
    name, color = key
    physics = value
    print(f"({color}) {name} <-> {physics}")
