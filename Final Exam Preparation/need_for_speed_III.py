cars_count = int(input())
cars = {}

for _ in range(cars_count):
    car_data = input().split("|")
    car = car_data[0]
    mileage = int(car_data[1])
    fuel = int(car_data[2])

    cars[car] = {}
    cars[car]["mileage"] = mileage
    cars[car]["fuel"] = fuel


line = input()
while not line == "Stop":
    tokens = line.split(" : ")
    command = tokens[0]
    car = tokens[1]

    if command == "Drive":
        distance = int(tokens[2])
        fuel = int(tokens[3])

        if cars[car]["fuel"] >= fuel:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100_000:
                cars.pop(car)
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")

    elif command == "Refuel":
        fuel = int(tokens[2])

        if cars[car]["fuel"] + fuel <= 75:
            cars[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
            cars[car]["fuel"] = 75

    elif command == "Revert":
        kilometers = int(tokens[2])
        cars[car]["mileage"] -= kilometers

        if cars[car]["mileage"] < 10_000:
            cars[car]["mileage"] = 10_000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    line = input()


for car, car_info_dict in sorted(cars.items(), key=lambda x: (-x[1]["mileage"], x[0])):
    print(f"{car} -> Mileage: {car_info_dict['mileage']} kms, Fuel in the tank: {car_info_dict['fuel']} lt.")
