import re

text = input()

threshold_pattern = r"\d"
all_digits = re.findall(threshold_pattern, text)
threshold = 1

for digit in all_digits:
    threshold *= int(digit)

print(f"Cool threshold: {threshold}")

emoji_pattern = r"((::|\*\*)([A-Z][a-z]{2,})\2)"
valid_emojis = re.findall(emoji_pattern, text)
cool_emojis = []

for valid_emoji in valid_emojis:
    emoji_name = valid_emoji[2]

    coolness = 0
    for char in emoji_name:
        coolness += ord(char)

    if coolness >= threshold:
        cool_emojis.append(valid_emoji[0])


print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
if cool_emojis:
    print("\n".join(cool_emojis))
