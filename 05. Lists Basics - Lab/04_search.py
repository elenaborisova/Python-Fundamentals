n = int(input())
word = input()
string_list = []

for _ in range(n):
    string = input()
    string_list.append(string)

print(string_list)

for i in range(len(string_list) - 1, -1, -1):
    element = string_list[i]
    if word not in element:
        string_list.remove(element)

print(string_list)
