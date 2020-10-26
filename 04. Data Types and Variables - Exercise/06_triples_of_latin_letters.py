n = int(input())

for first in range(ord('a'), ord('a') + n):
    for second in range(ord('a'), ord('a') + n):
        for third in range(ord('a'), ord('a') + n):
            print(chr(first), end="")
            print(chr(second), end="")
            print(chr(third), end="")
            print()
