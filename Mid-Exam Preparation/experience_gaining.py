experience_needed = float(input())
battles = int(input())
n_battle = 0

for battle in range(1, battles + 1):
    experience_earned_per_battle = float(input())

    if battle % 3 == 0:
        experience_earned_per_battle += 0.15 * experience_earned_per_battle

    if battle % 5 == 0:
        experience_earned_per_battle -= 0.1 * experience_earned_per_battle

    experience_needed -= experience_earned_per_battle
    n_battle = battle
    if experience_needed <= 0:
        break

if experience_needed <= 0:
    print(f"Player successfully collected his needed experience for {n_battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_needed:.2f} more needed.")