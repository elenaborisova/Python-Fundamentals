from collections import defaultdict

words = input().lower().split()
words_dict = defaultdict(int)

for word in words:
    words_dict[word] += 1

print(' '.join([word for word, count in words_dict.items() if not count % 2 ==0]))
