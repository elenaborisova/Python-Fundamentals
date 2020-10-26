import re

split_pattern = r",[ ]*"
demon_names = re.split(split_pattern, input())

for demon_name in sorted(demon_names):
    demon_name = demon_name.strip()

    health_pattern = r"[^\.+\-*\/0-9]"
    health_chars = re.findall(health_pattern, demon_name)
    total_health = sum([ord(char) for char in health_chars])

    damage_pattern = r"([-+]?\d+\.?\d*)"
    damage_digits = re.findall(damage_pattern, demon_name)
    total_damage = sum([float(digit) for digit in damage_digits])

    for char in demon_name:
        if char == "*":
            total_damage *= 2
        elif char == "/" and not total_damage == 0:
            total_damage /= 2

    print(f"{demon_name} - {total_health} health, {total_damage:.2f} damage")

