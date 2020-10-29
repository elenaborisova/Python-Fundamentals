import re

text = input()
mirror_words = []

hidden_pairs_pattern = r"(#|@)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
valid_word_pairs = re.findall(hidden_pairs_pattern, text)

if valid_word_pairs:
    print(f"{len(valid_word_pairs)} word pairs found!")

    for valid_pair in valid_word_pairs:
        first_word = valid_pair[1]
        second_word = valid_pair[2]

        if first_word == second_word[::-1]:
            mirror_words.append(f"{first_word} <=> {second_word}")
else:
    print("No word pairs found!")


if mirror_words:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")
