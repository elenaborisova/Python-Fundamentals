bands = {}

line = input()
while not line == "start of concert":
    tokens = line.split("; ")
    command = tokens[0]
    band_name = tokens[1]

    if command == "Add":
        new_members = tokens[2].split(", ")
        new_members = list(new_members)

        if band_name not in bands:
            bands[band_name] = {}
            bands[band_name]["members"] = new_members
            bands[band_name]["time"] = 0
        else:
            for member in new_members:
                if member not in bands[band_name]["members"]:
                    bands[band_name]["members"] += [member]

    elif command == "Play":
        time = int(tokens[2])

        if band_name not in bands:
            bands[band_name] = {}
            bands[band_name]["members"] = []
            bands[band_name]["time"] = time
        else:
            bands[band_name]["time"] += time

    line = input()

band_name = input()


total_time = sum([values["time"] for values in bands.values()])
print(f"Total time: {total_time}")

for band, band_data in sorted(bands.items(), key=lambda x: (-x[1]["time"], x[0])):
    print(f"{band} -> {band_data['time']}")

print(band_name)
print('=> ' + '\n=> '.join(bands[band_name]['members']))
