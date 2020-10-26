import re

sentence = input()
search_word = input()

pattern = rf"\b{search_word}\b"
word_occurrences = re.findall(pattern, sentence, re.IGNORECASE)

count = len(word_occurrences)
print(count)
