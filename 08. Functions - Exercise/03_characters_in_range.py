def get_chars_between(first_char, second_char):
    start_index = ord(first_char)
    end_index = ord(second_char)

    result = [chr(i) for i in range(start_index + 1, end_index)]
    return " ".join(result)


first_char = input()
second_char = input()
print(get_chars_between(first_char, second_char))
