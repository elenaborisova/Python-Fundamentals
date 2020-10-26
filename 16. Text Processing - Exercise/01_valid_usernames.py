def validate_username(username):
    if not 3 <= len(username) <= 16:
        return False

    valid_chars = ["-", "_"]
    for char in username:
        if not char.isalnum() and char not in valid_chars:
            return False

    return True


usernames = input().split(", ")
valid_usernames = []

for username in usernames:
    is_valid = validate_username(username)
    if is_valid:
        valid_usernames.append(username)

print("\n".join(valid_usernames))
