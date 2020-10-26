class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        zoo_name = self.name
        if species == 'mammal':
            return f'Mammals in {zoo_name}: {", ".join(self.mammals)}\nTotal animals: {Zoo.__animals}'
        elif species == 'fish':
            return f'Fishes in {zoo_name}: {", ".join(self.fishes)}\nTotal animals: {Zoo.__animals}'
        elif species == 'bird':
            return f'Birds in {zoo_name}: {", ".join(self.birds)}\nTotal animals: {Zoo.__animals}'


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())
for _ in range(n):
    animal_info = input().split()
    species = animal_info[0]
    name = animal_info[1]
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
