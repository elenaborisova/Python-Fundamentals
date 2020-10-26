curr_version = input().split(".")
next_version = str(int(''.join(curr_version)) + 1)
print('.'.join(next_version))
