import re

n = int(input())
attacked_and_destroyed_planets = {"A": [], "D": []}

for _ in range(n):
    encrypted_message = input()
    letters = ["s", "t", "a", "r"]
    matches = [char for char in encrypted_message.lower() if char in letters]

    key = len(matches)
    decrypted_message = ""

    for char in encrypted_message:
        ascii_value = ord(char) - key
        decrypted_message += chr(ascii_value)

    pattern = r"@(?P<name>[A-Za-z]+)[^@\-!:>]*:(?P<pop>\d+)[^@\-!:>]*!(?P<attack>[AD])![^@\-!:>]*->(?P<count>\d+)"
    planet_data = re.search(pattern, decrypted_message)

    if planet_data:  # if valid
        planet_name = planet_data["name"]
        attack_type = planet_data["attack"]

        if attack_type == "A":
            attacked_and_destroyed_planets["A"] += [planet_name]
        elif attack_type == "D":
            attacked_and_destroyed_planets["D"] += [planet_name]


for attack_type, planet_names in attacked_and_destroyed_planets.items():
    if attack_type == "A":
        print(f"Attacked planets: {len(planet_names)}")
        for planet in sorted(planet_names):
            print(f"-> {planet}")

    elif attack_type == "D":
        print(f"Destroyed planets: {len(planet_names)}")
        for planet in sorted(planet_names):
            print(f"-> {planet}")

