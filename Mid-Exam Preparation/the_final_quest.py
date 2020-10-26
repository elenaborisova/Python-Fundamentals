words = input().split()

tokens = input().split()
while not tokens[0] == "Stop":
    command = tokens[0]

    if command == "Delete":
        index = int(tokens[1])
        if 0 <= index + 1 < len(words):
            words.pop(index + 1)

    elif command == "Swap":
        first_word = tokens[1]
        second_word = tokens[2]
        if first_word in words and second_word in words:
            first_index = words.index(first_word)
            second_index = words.index(second_word)
            words[first_index], words[second_index] = words[second_index], words[first_index]

    elif command == "Put":
        word = tokens[1]
        index = int(tokens[2])
        if 0 <= index - 1 <= len(words):
            words.insert(index - 1, word)

    elif command == "Sort":
        words.sort(reverse=True)

    elif command == "Replace":
        first_word = tokens[1]
        second_word = tokens[2]
        if second_word in words:
            second_index = words.index(second_word)
            words[second_index] = first_word

    tokens = input().split()

print(" ".join(words))
