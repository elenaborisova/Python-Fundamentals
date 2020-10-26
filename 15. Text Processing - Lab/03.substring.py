def replace_all(replace_string, actual_string):
    while replace_string in actual_string:
        actual_string = actual_string.replace(replace_string, "")
    return actual_string


print(replace_all(input(), input()))
