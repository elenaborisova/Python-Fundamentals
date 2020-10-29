waiting_people = int(input())
lift_spaces = list(map(int, input().split()))
full_train = 4 * len(lift_spaces)

while waiting_people > 0 and sum(lift_spaces) < full_train:

    for index, space in enumerate(lift_spaces):

        if space < 4:
            if waiting_people >= 4:
                filling_space = 4 - lift_spaces[index]
                lift_spaces[index] += filling_space
                waiting_people -= filling_space
            else:
                lift_spaces[index] += waiting_people
                waiting_people = 0

if waiting_people == 0 and sum(lift_spaces) < full_train:
    print(f"The lift has empty spots!\n"
          f"{' '.join(map(str, lift_spaces))}")

elif waiting_people > 0 and sum(lift_spaces) == full_train:
    print(f"There isn't enough space! {waiting_people} people in a queue!\n"         
          f"{' '.join(map(str, lift_spaces))}")

elif waiting_people == 0 and sum(lift_spaces) == full_train:
    print(' '.join(map(str, lift_spaces)))

