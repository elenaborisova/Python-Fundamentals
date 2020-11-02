dictionary = {}

words_definitions = input().split(" | ")
for word_definition in words_definitions:
    word, definition = word_definition.split(": ")
    if word not in dictionary:
        dictionary[word] = []

    dictionary[word] += [definition]


words = input().split(" | ")
for word in words:
    if word in dictionary:
        print(word)
        print(" -" + '\n -'.join(sorted(dictionary[word], key=lambda x: -len(x))))


command = input()
if command == "List":
    print(' '.join(sorted(dictionary.keys())))
