def parse_to_char(word):
    digits = ""

    for symbol in word:
        if symbol.isdigit():
            digits += symbol
        else:
            break

    deciphered_digits = chr(int(digits))
    new_word = word.replace(digits, deciphered_digits)
    return new_word


def replace_in_word(word):
    alphas = list(word)
    alphas[1], alphas[-1] = alphas[-1], alphas[1]
    return "".join(alphas)


def decipher_message(word):
    new_word = parse_to_char(word)
    result = replace_in_word(new_word)
    return result


secret_message = input().split()
deciphered_message = [decipher_message(word) for word in secret_message]
print(" ". join(deciphered_message))
