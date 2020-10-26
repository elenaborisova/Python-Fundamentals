from collections import defaultdict

players = {}
total_skill = defaultdict(int)

line = input()
while not line == "Season end":
    if " -> " in line:
        player, position, skill = line.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {position: skill}
            total_skill[player] += skill
        else:
            if position in players[player]:
                prev_skill = players[player][position]
                if skill > prev_skill:
                    players[player][position] = skill
                    total_skill[player] += skill - prev_skill
            else:
                players[player][position] = skill
                total_skill[player] += skill

    elif " vs " in line:
        first_player, second_player = line.split(" vs ")

        if first_player in players and second_player in players:
            for first_position in players[first_player]:
                if first_position in players[second_player]:
                    if total_skill[first_player] > total_skill[second_player]:
                        total_skill.pop(second_player)
                        players.pop(second_player)
                        break
                    elif total_skill[second_player] > total_skill[first_player]:
                        total_skill.pop(first_player)
                        players.pop(first_player)
                        break

    line = input()


for player, t_skill in sorted(total_skill.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {t_skill} skill")

    for position, skill in sorted(players[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
