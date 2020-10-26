def transform_int_data(data):
    print(data * 2)


def transform_float_data(data):
    print(f"{(data * 1.5):.2f}")


def transform_string_data(data):
    print(f"${data}$")


data_type = input()

if data_type == "int":
    data = int(input())
    transform_int_data(data)

elif data_type == "real":
    data = float(input())
    transform_float_data(data)

elif data_type == "string":
    data = input()
    transform_string_data(data)
