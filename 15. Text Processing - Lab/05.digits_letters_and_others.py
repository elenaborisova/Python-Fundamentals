def all_digits(text):
    return get_all_chars_matching_condition(text, lambda char: char.isdigit())


def all_letters(text):
    return get_all_chars_matching_condition(text, lambda char: char.isalpha())


def all_other_chars(text):
    return get_all_chars_matching_condition(text, lambda char: not char.isalnum())


def get_all_chars_matching_condition(text, condition_fn):
    result = ""
    for char in text:
        if condition_fn(char):
            result += char
    return result


text = input()
print(all_digits(text))
print(all_letters(text))
print(all_other_chars(text))
