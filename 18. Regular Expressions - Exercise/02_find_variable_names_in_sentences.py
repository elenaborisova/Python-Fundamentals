import re

sentence = input()

pattern = r"\b_[A-Za-z00-9]+\b"
variable_names = re.findall(pattern, sentence)
names_only = []

for variable_name in variable_names:
    new_pattern = r"[A-Za-z00-9]+"
    names_only += re.findall(new_pattern, variable_name)

print(",".join(names_only))
