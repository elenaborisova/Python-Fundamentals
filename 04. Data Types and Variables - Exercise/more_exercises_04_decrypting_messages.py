key = int(input())
n = int(input())
message = ""

for _ in range(n):
    char = input()
    message += chr(ord(char) + key)

print(message)

