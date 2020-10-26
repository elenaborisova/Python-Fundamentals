def validate_length(password):
    if len(password) < 6 or len(password) > 10:
        return "Password must be between 6 and 10 characters"


def validate_has_only_letters_and_digits(password):
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return "Password must consist only of letters and digits"


def validate_at_least_two_digits(password):
    digits_count = 0
    for char in password:
        if char.isdigit():
            digits_count += 1
    if digits_count < 2:
        return "Password must have at least 2 digits"


def validate(password):
    validators = [
        validate_length,
        validate_has_only_letters_and_digits,
        validate_at_least_two_digits
    ]
    validation_errors = []
    for validator in validators:
        result = validator(password)
        if result is not None:
            validation_errors.append(result)
    if len(validation_errors) == 0:
        return "Password is valid"
    else:
        return "\n".join(validation_errors)


password = input()
result = validate(password)
print(result)
