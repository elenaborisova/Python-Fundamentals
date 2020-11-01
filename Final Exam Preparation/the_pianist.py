n = int(input())
pieces = {}

for _ in range(n):
    piece, composer, key = input().split("|")

    pieces[piece] = {}
    pieces[piece]["composer"] = composer
    pieces[piece]["key"] = key


line = input()
while not line == "Stop":
    tokens = line.split("|")
    command = tokens[0]
    piece = tokens[1]

    if command == "Add":
        composer = tokens[2]
        key = tokens[3]

        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {}
            pieces[piece]["composer"] = composer
            pieces[piece]["key"] = key
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = tokens[2]

        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    line = input()


for piece, piece_info in sorted(pieces.items(), key=lambda x: (x[0], x[1]["composer"])):
    print(f"{piece} -> Composer: {piece_info['composer']}, Key: {piece_info['key']}")
