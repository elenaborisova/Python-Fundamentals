import re

n = int(input())
pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}\d+)P@\$"
successful_reg_count = 0

for _ in range(n):
    registration = input()
    valid_registration = re.fullmatch(pattern, registration)

    if valid_registration:
        username = valid_registration[1]
        password = valid_registration[2]
        successful_reg_count += 1

        print("Registration was successful")
        print(f"Username: {username}, Password: {password}")
    else:
        print("Invalid username or password")

print(f"Successful registrations: {successful_reg_count}")
