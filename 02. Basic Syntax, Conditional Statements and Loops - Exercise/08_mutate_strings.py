first_string = input()
second_string = input()

for i in range(len(first_string)):
    mutated_string = ""
    if not first_string[i] == second_string[i]:
        mutated_string += second_string[:i + 1]
        mutated_string += first_string[i + 1:]
        print(mutated_string)

