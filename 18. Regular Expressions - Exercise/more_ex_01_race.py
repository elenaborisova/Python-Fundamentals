import re
from collections import defaultdict

participants = input().split(", ")
results = defaultdict(int)

name_pattern = r"[A-Za-z]"
digits_pattern = r"\d"


race_data = input()
while not race_data == "end of race":

    letters = re.findall(name_pattern, race_data)
    curr_name = "".join(letters)

    if curr_name in participants:
        digits = re.findall(digits_pattern, race_data)
        results[curr_name] += sum(list(map(int, digits)))

    race_data = input()


sorted_results = dict(sorted(results.items(), key=lambda x: -x[1]))

count = 1
for participant in sorted_results:
    if count == 1:
        print(f"1st place: {participant}")
    elif count == 2:
        print(f"2nd place: {participant}")
    elif count == 3:
        print(f"3rd place: {participant}")
        break
    count += 1
