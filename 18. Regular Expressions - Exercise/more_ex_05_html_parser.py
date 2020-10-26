import re

text = input()

title_pattern = r"<title>(.+)<\/title>"
raw_title = re.findall(title_pattern, text)
split_pattern = r"<[^><]+>"
split_title = re.split(split_pattern, "".join(raw_title))
title = "".join(split_title)

content_pattern = r"<body>(.+)<\/body>"
raw_content = re.findall(content_pattern, text)
split_content = re.split(split_pattern, "".join(raw_content))
content = "".join(split_content)


print(f"Title: {title}")
print(f"Content: {content}")
