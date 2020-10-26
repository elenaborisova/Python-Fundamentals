text = input()

for index, char in enumerate(text):
    emoticon = ""
    if char == ":" and index + 1 < len(text) and text[index + 1] != " ":
        emoticon += char + text[index + 1]
        print(emoticon)