word = input()
new_word = ""

for char in word: # or range(len(word))
    new_word += char * 2 # or word[char]

print(new_word)

