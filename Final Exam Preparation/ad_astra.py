import re

text = input()
pattern = r"(#|\|)([A-Za-z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
food_info = re.findall(pattern, text)

total_calories = sum([int(food[3]) for food in food_info])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for food in food_info:
    item_name = food[1]
    expiration_date = food[2]
    calories = food[3]

    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")

