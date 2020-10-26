import re

text = input()

user_pattern = r"(^| )[A-Za-z0-9]+(([\.\-_])[A-Za-z0-9]+)*"
host_pattern = r"[A-Za-z]+(-[A-Za-z]+)*(\.[A-Za-z]+(-[A-Za-z])*)+"
email_pattern = rf"({user_pattern}@{host_pattern})"

valid_emails = re.findall(email_pattern, text)

for email in valid_emails:
    print(email[0])
