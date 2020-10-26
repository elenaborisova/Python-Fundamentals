first_line = input().split()
second_line = input().split()
third_line = input().split()

first_player = "1"
second_player = "2"
first_is_winner = False
second_is_winner = False

if first_line[0] == "1" and first_line[1] == "1" and first_line[2] == "1":
    first_is_winner = True
if second_line[0] == "1" and second_line[1] == "1" and second_line[2] == "1":
    first_is_winner = True
if third_line[0] == "1" and third_line[1] == "1" and third_line[2] == "1":
    first_is_winner = True
if first_line[0] == "1" and second_line[0] == "1" and third_line[0] == "1":
    first_is_winner = True
if first_line[1] == "1" and second_line[1] == "1" and third_line[1] == "1":
    first_is_winner = True
if first_line[2] == "1" and second_line[2] == "1" and third_line[2] == "1":
    first_is_winner = True
if first_line[0] == "1" and second_line[1] == "1" and third_line[2] == "1":
    first_is_winner = True
if first_line[2] == "1" and second_line[1] == "1" and third_line[0] == "1":
    first_is_winner = True

if first_line[0] == "2" and first_line[1] == "2" and first_line[2] == "2":
    second_is_winner = True
if second_line[0] == "2" and second_line[1] == "2" and second_line[2] == "2":
    second_is_winner = True
if third_line[0] == "2" and third_line[1] == "2" and third_line[2] == "2":
    second_is_winner = True
if first_line[0] == "2" and second_line[0] == "2" and third_line[0] == "2":
    second_is_winner = True
if first_line[1] == "2" and second_line[1] == "2" and third_line[1] == "2":
    second_is_winner = True
if first_line[2] == "2" and second_line[2] == "2" and third_line[2] == "2":
    second_is_winner = True
if first_line[0] == "2" and second_line[1] == "2" and third_line[2] == "2":
    second_is_winner = True
if first_line[2] == "2" and second_line[1] == "2" and third_line[0] == "2":
    second_is_winner = True

if first_is_winner:
    print("First player won")
elif second_is_winner:
    print("Second player won")
else:
    print("Draw!")

