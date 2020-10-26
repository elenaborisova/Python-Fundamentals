import re

pattern = r"(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)"

while True:
    text = input()

    if not text:
        break

    valid_emails = re.finditer(pattern, text)

    for email in valid_emails:
        print(email.group(0))
