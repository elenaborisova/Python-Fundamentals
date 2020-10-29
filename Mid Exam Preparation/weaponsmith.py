parts = input().split("|")

tokens = input()
while not tokens == "Done":
    if "Move Left" in tokens:
        args = tokens.split()
        index = int(args[2])
        if 0 < index < len(parts):  # < only cause we wanna check if we can move to left
            parts[index], parts[index - 1] = parts[index - 1], parts[index]

    elif "Move Right" in tokens:
        args = tokens.split()
        index = int(args[2])
        if 0 <= index < len(parts) - 1:  # -1 to check if the move is possible
            parts[index], parts[index + 1] = parts[index + 1], parts[index]

    elif "Check Even" in tokens:
        evens = [parts[i] for i in range(len(parts)) if i % 2 == 0]
        print(" ".join(evens))

    elif "Check Odd" in tokens:
        odds = [parts[i] for i in range(len(parts)) if i % 2 == 1]
        print(" ".join(odds))

    tokens = input()

print(f"You crafted {''.join(parts)}!")