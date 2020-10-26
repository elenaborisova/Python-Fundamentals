substrings = input().split(", ")
strings = input().split(", ")

valid_substrings = [substring for substring in substrings for string in strings if substring in string]
unique_valid_substrings = sorted(set(valid_substrings), key=valid_substrings.index)

print(unique_valid_substrings)
