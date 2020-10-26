line = input().upper()
result = ""
curr_res = ""

for index, char in enumerate(line):

    if char.isdigit():
        if index + 1 < len(line) and line[index + 1].isdigit():
            next_char = line[index + 1]
            digit = int(char + next_char)
            result += curr_res * digit
            curr_res = ""
        else:
            digit = int(char)
            result += curr_res * digit
            curr_res = ""
    else:
        curr_res += char


print(f"Unique symbols used: {len(set(result))}")
print(result)
