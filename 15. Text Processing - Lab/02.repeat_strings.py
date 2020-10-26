words = input().split()
result = "".join(map(lambda word: word * len(word), words))
print(result)
