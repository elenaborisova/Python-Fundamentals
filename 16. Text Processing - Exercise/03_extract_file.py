file_path = input().split("\\")
name_and_ext = file_path[-1].split(".")
file_name = name_and_ext[0]
file_extension = name_and_ext[1]

print(f"File name: {file_name}\nFile extension: {file_extension}")