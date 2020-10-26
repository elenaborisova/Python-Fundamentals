cards_list = input().split()
terminated_players = []
team_a_players = 11
team_b_players = 11
is_terminated = False

for player in cards_list:
    if player in terminated_players:
        continue

    if 'A' in player:
        team_a_players -= 1
    elif 'B' in player:
        team_b_players -= 1

    terminated_players.append(player)

    if team_a_players < 7 or team_b_players < 7:
        is_terminated = True
        break

print(f"Team A - {team_a_players}; Team B - {team_b_players}")
if is_terminated:
    print("Game was terminated")
