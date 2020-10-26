word = input().casefold()
count = 0

if "water" in word:
    count += word.count("water")
if "sand" in word:
    count += word.count("sand")
if "fish" in word:
    count += word.count("fish")
if "sun" in word:
    count += word.count("sun")

print(count)
