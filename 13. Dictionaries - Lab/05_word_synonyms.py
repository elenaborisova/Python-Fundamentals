from collections import defaultdict

n = int(input())
words_with_synonyms = defaultdict(list)

for _ in range(n):
    word = input()
    synonym = input()
    words_with_synonyms[word] += [synonym]

for word, synonym in words_with_synonyms.items():
    print(f"{word} - {', '.join(synonym)}")
