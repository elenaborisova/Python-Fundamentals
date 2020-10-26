electrons = int(input())
shell = []

index = 0
while electrons > 0:
    position = index + 1
    max_electrons_per_shield = 2 * (position ** 2)

    if electrons - max_electrons_per_shield < 0:
        shell.append(electrons)
        break

    shell.append(max_electrons_per_shield)

    index += 1
    electrons -= max_electrons_per_shield

print(shell)
