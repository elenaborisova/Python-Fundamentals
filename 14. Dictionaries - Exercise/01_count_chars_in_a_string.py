from collections import defaultdict

string = input()
char_count = defaultdict(int)

for char in string:
    if not char == " ":
        char_count[char] += 1 
        
for char, count in char_count.items():
    print(f"{char} -> {count}")
