import re

pattern = r"(#|\$|%|\*|&)([A-Za-z]+)\1=(\d+)!!(.+)"

while True:
    try:
        line = input()
        if not line:
            break
    except EOFError:
        break

    match = re.fullmatch(pattern, line)

    if match:
        name = match[2]
        length = int(match[3])
        code = match[4]
        if len(code) == length:
            decrypted_code = ""
            for char in code:
                decrypted_code += chr(ord(char) + length)

            print(f"Coordinates found! {name} -> {decrypted_code}")
        else:
            print("Nothing found!")
    else:
        print("Nothing found!")
