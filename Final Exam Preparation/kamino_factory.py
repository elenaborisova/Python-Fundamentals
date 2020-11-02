dna_length = int(input())
max_count = 0
max_subsequences = []
all_samples = []

command = input()
while not command == "Clone them!":
    dna_sequence = list(map(int, command.split("!")))
    curr_count = 0
    max_curr_count = 0

    for digit in dna_sequence:
        if digit == 1:
            curr_count += 1
            if curr_count > max_curr_count:
                max_curr_count = curr_count

        elif digit == 0:
            curr_count = 0

    if max_curr_count > max_count:
        max_count = max_curr_count
        max_subsequences = [dna_sequence]
    elif max_curr_count == max_count:
        max_subsequences += [dna_sequence]

    all_samples += [dna_sequence]
    command = input()


leftmost_index = 10000
filtered_sequences = []
if len(max_subsequences) > 1:
    for subsequence in max_subsequences:
        for index, digit in enumerate(subsequence):
            if subsequence[index:index + max_count] == [1] * max_count:
                if index < leftmost_index:
                    leftmost_index = index
                    filtered_sequences = [subsequence]
                elif index == leftmost_index:
                    leftmost_index = index
                    filtered_sequences += [subsequence]


best_dna = []
max_sum = 0
if len(filtered_sequences) > 1:
    for filtered_sequence in filtered_sequences:
        if sum(filtered_sequence) > max_sum:
            max_sum = sum(filtered_sequence)
            best_dna = filtered_sequence
else:
    best_dna = filtered_sequences[0]


sample_index = 0
for sample in all_samples:
    if sample == best_dna:
        sample_index = all_samples.index(sample) + 1


print(f"Best DNA sample {sample_index} with sum: {sum(best_dna)}:")
print(' '.join(list(map(str, best_dna))))
