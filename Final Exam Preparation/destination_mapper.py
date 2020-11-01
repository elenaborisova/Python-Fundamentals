import re

places = input()

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
valid_places = re.findall(pattern, places)

places_names = [place[1] for place in valid_places]
travel_points = sum([len(place) for place in places_names])

print(f"Destinations: {', '.join(places_names)}")
print(f"Travel Points: {travel_points}")
