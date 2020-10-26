contacts = input().split()

while True:
    tokens = input().split()
    command = tokens[0]

    if command == "Add":
        contact = tokens[1]
        index = int(tokens[2])
        if contact not in contacts:
            contacts.append(contact)
        else:
            if 0 <= index < len(contacts):
                contacts.insert(index, contact)

    elif command == "Remove":
        index = int(tokens[1])
        if 0 <= index < len(contacts):
            contacts.pop(index)

    elif command == "Export":
        start_index = int(tokens[1])
        count = int(tokens[2])
        if 0 <= start_index < len(contacts):
            if count <= len(contacts):
                count_contacts = [contacts[i] for i in range(start_index, start_index + count)]
                print(" ".join(count_contacts))
            else:
                count_contacts = [contacts[i] for i in range(start_index, len(contacts))]
                print(" ".join(count_contacts))

    elif command == "Print":
        if tokens[1] == "Normal":
            print(f"Contacts: {' '.join(contacts)}")
            break
        elif tokens[1] == "Reversed":
            print(f"Contacts: {' '.join(reversed(contacts))}")
            break
