import re

pattern = r"([A-Za-z0-9!@#$?]+)=(\d+)<<(.+)"

line = input()
while not line == "Last note":

    match = re.fullmatch(pattern, line)

    if match:
        peak_name = match[1]
        length = int(match[2])
        code = match[3]

        if len(code) == length:
            decoded_name = ""
            for char in peak_name:
                if char.isalnum():
                    decoded_name += char

            print(f"Coordinates found! {decoded_name} -> {code}")
        else:
            print("Nothing found!")
    else:
        print("Nothing found!")

    line = input()
